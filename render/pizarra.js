// Renderiza la "hoja de cuaderno" de la solucion (1080x1920): fondo vacio, hoja completa
// y las cajas de cada linea escrita, para animar el lapiz en Python.
// Uso: node pizarra.js post.json carpeta_salida
const fs = require('fs');
const path = require('path');
const katex = require('katex');
const { chromium } = require('playwright-core');

const CONFIG = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'config.json'), 'utf8'));
const HANDLE = '@' + CONFIG.handle;
const KATEX_CSS = path.join(__dirname, 'node_modules/katex/dist/katex.min.css');
const FUENTE = path.join(__dirname, 'node_modules/@fontsource/caveat/files/caveat-latin-700-normal.woff2');
const L = 'ABCDE';

function tex(s) {
  return s.replace(/\\\$/g, '\u0000')
    .replace(/\$\$([\s\S]+?)\$\$/g, (_, m) => katex.renderToString(m, { displayMode: true, throwOnError: true }))
    .replace(/\$([^$]+?)\$/g, (_, m) => katex.renderToString(m, { throwOnError: true }))
    .replace(/\u0000/g, '$');
}

const CSS = `
@font-face{font-family:Mano;src:url(file://${FUENTE}) format('woff2')}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1920px;overflow:hidden;background:#F7F3E8;font-family:Mano,cursive;color:#1B3A8C}
.hoja{position:relative;width:1080px;height:1920px;padding:170px 90px 300px 130px;
  background-image:linear-gradient(rgba(70,120,200,.18) 2px,transparent 2px),linear-gradient(90deg,rgba(70,120,200,.18) 2px,transparent 2px);
  background-size:54px 54px}
.margen{position:absolute;top:0;bottom:0;left:96px;width:3px;background:rgba(220,60,60,.45)}
.top{position:absolute;top:70px;left:130px;right:90px;display:flex;justify-content:space-between;font-family:Inter,sans-serif;font-size:30px;font-weight:700;color:#8A93A6}
.top b{color:#C2410C}
h1{font-size:120px;line-height:1;margin:60px 0 60px;color:#C2410C}
.paso{margin-bottom:80px}
.linea{display:block;font-size:80px;line-height:1.15}
.linea.f{font-size:64px;padding:14px 0 6px 40px;color:#0F2A6B}
.linea .katex{font-size:1em;white-space:nowrap}
.resp{display:inline-block;white-space:nowrap;margin-top:20px;font-size:78px;color:#B91C1C;padding:8px 34px;border:5px solid #B91C1C;border-radius:46% 54% 50% 50% / 60% 45% 55% 40%}
.pie{position:absolute;left:130px;right:90px;bottom:330px;font-size:60px;color:#C2410C;text-align:center}
`;

(async () => {
  const [, , jsonPath, outDir] = process.argv;
  const post = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
  fs.mkdirSync(outDir, { recursive: true });
  const pz = post.pizarra; // [{lineas:[texto|$formula$], voz:"..."}], cierre:{voz}
  const pasos = pz.pasos.map((p, i) => `<div class="paso" data-paso="${i}">${p.lineas.map(l =>
    `<span class="linea ${/^\$.*\$$/.test(l.trim()) ? 'f' : ''}">${tex(l)}</span>`).join('')}</div>`).join('');
  const resp = `<div class="paso" data-paso="${pz.pasos.length}"><span class="linea resp">Respuesta: ${L[post.correcta]}) ${tex(post.alternativas[post.correcta])}</span></div>`;
  const html = `<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="file://${KATEX_CSS}"><style>${CSS}</style></head>
<body><div class="hoja"><div class="margen"></div>
<div class="top"><span><b>PAES ${post.nivel}</b> · ${post.tema}</span><span>${HANDLE}</span></div>
<div id="c"><h1>Solución</h1>${pasos}${resp}</div>
<div class="pie" id="pie">Sigue a ${HANDLE} ✏️</div></div></body></html>`;
  const f = path.resolve(outDir, 'pizarra.html');
  fs.writeFileSync(f, html);
  const browser = await chromium.launch({ executablePath: process.env.CHROME || undefined });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto('file://' + f);
  await page.evaluate(() => document.fonts.ready);
  // Cajas: una por renglon visual de cada linea, agrupadas por paso
  const datos = await page.evaluate(() => {
    const cont = document.getElementById('c');
    const pie = document.getElementById('pie').getBoundingClientRect();
    const fin = cont.getBoundingClientRect().bottom;
    const R = r => ({ x: Math.floor(r.left) - 6, y: Math.floor(r.top) - 6, w: Math.ceil(r.width) + 12, h: Math.ceil(r.height) + 12 });
    const h1 = R(document.querySelector('h1').getBoundingClientRect());
    const renglones = el => {
      const rg = document.createRange(); rg.selectNodeContents(el);
      const rs = [...rg.getClientRects()].filter(r => r.width > 2 && r.height > 8);
      const filas = [];
      for (const r of rs.sort((a, b) => a.top - b.top || a.left - b.left)) {
        const f = filas.find(f => Math.abs((f.top + f.bottom) / 2 - (r.top + r.bottom) / 2) < 25);
        if (f) { f.left = Math.min(f.left, r.left); f.right = Math.max(f.right, r.right); f.top = Math.min(f.top, r.top); f.bottom = Math.max(f.bottom, r.bottom); }
        else filas.push({ left: r.left, right: r.right, top: r.top, bottom: r.bottom });
      }
      return filas.map(f => R({ left: f.left, top: f.top, width: f.right - f.left, height: f.bottom - f.top }));
    };
    const pasos = [...document.querySelectorAll('.paso')].map(p => [...p.querySelectorAll('.linea')].flatMap(l =>
      l.classList.contains('resp') ? [R(l.getBoundingClientRect())] : renglones(l)));
    return { h1, pasos, pie: R(pie), desborde: fin > pie.top - 10 };
  });
  if (datos.desborde) { console.error('DESBORDE en la pizarra'); await browser.close(); process.exit(2); }
  await page.screenshot({ path: path.join(outDir, 'llena.png') });
  await page.addStyleTag({ content: '#c, #pie{visibility:hidden}' });
  await page.screenshot({ path: path.join(outDir, 'vacia.png') });
  await browser.close();
  fs.unlinkSync(f);
  fs.writeFileSync(path.join(outDir, 'pizarra.json'), JSON.stringify(datos, null, 1));
  console.log(`pizarra: ${datos.pasos.length} bloques`);
})();
