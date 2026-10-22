// Renderiza un post (JSON) a 3 PNG 1080x1350 usando KaTeX + Chromium
const fs = require('fs');
const path = require('path');
const katex = require('katex');
const { chromium } = require('playwright-core');

const CONFIG = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'config.json'), 'utf8'));
const HANDLE = '@' + CONFIG.handle;
const KATEX_CSS = path.join(__dirname, 'node_modules/katex/dist/katex.min.css');

function tex(s) {
  // $$...$$ display, $...$ inline. Un signo peso literal se escribe \\$
  return s.replace(/\\\$/g, '\u0000')
    .replace(/\$\$([\s\S]+?)\$\$/g, (_, m) => katex.renderToString(m, { displayMode: true, throwOnError: true }))
    .replace(/\$([^$]+?)\$/g, (_, m) => katex.renderToString(m, { throwOnError: true }))
    .replace(/\u0000/g, '$');
}

const CSS = `
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1350px;background:#0F1B2D;color:#F4F1EA;font-family:'Inter',sans-serif;overflow:hidden}
.page{position:relative;width:1080px;height:1350px;padding:80px 84px;display:flex;flex-direction:column}
.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:54px 54px;pointer-events:none}
.top{display:flex;justify-content:space-between;align-items:center;position:relative}
.chips{display:flex;gap:14px}
.chip{font-size:26px;font-weight:600;letter-spacing:.04em;padding:10px 22px;border-radius:999px;background:rgba(255,255,255,.08);color:#C9D3E3}
.chip.lvl{background:#F5B83D;color:#0F1B2D}
.num{font-size:26px;color:#7F8DA6;font-weight:500}
h1{font-size:30px;font-weight:700;letter-spacing:.18em;color:#F5B83D;margin:calc(56px*var(--k)) 0 22px;position:relative}
.page{--k:1}
.stmt{font-size:calc(44px*var(--k));line-height:1.38;font-weight:450;position:relative}
.stmt .katex{font-size:1.05em}
.katex{white-space:nowrap}
.opts{padding-top:40px}
.opts{margin-top:auto;display:flex;flex-direction:column;gap:calc(20px*var(--k));position:relative}
.opt{display:flex;align-items:center;gap:28px;padding:calc(20px*var(--k)) 30px;border-radius:22px;background:rgba(255,255,255,.055);border:2px solid rgba(255,255,255,.07);font-size:calc(40px*var(--k))}
.opt b{width:62px;height:62px;flex:none;border-radius:50%;display:flex;align-items:center;justify-content:center;background:#1E2E47;color:#F5B83D;font-size:32px}
.opt.ok{border-color:#4ED39A;background:rgba(78,211,154,.12)}
.opt.ok b{background:#4ED39A;color:#0F1B2D}
.foot{display:flex;justify-content:space-between;align-items:center;margin-top:46px;font-size:26px;color:#7F8DA6;position:relative}
.foot .h{color:#C9D3E3;font-weight:600}
.swipe{color:#F5B83D;font-weight:600}
.steps{display:flex;flex-direction:column;gap:calc(30px*var(--k));position:relative}
.step{display:flex;gap:28px}
.step i{font-style:normal;flex:none;width:54px;height:54px;border-radius:14px;background:#F5B83D;color:#0F1B2D;font-weight:800;font-size:28px;display:flex;align-items:center;justify-content:center;margin-top:4px}
.step div{font-size:calc(37px*var(--k));line-height:1.42}
.ans{margin-top:auto;padding:34px 38px;border-radius:24px;background:rgba(78,211,154,.12);border:2px solid #4ED39A;font-size:42px;font-weight:600;position:relative}
.ans span{color:#4ED39A}
.trap{padding:34px 38px;border-radius:24px;background:rgba(245,184,61,.1);border:2px solid rgba(245,184,61,.5);font-size:calc(37px*var(--k));line-height:1.42;position:relative}
.trap strong{color:#F5B83D}
.cta{margin-top:auto;text-align:center;position:relative}
.cta p{font-size:40px;font-weight:600;line-height:1.35}
.cta small{display:block;margin-top:18px;font-size:30px;color:#7F8DA6}
`;

function shell(post, idx, total, body) {
  return `<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="file://${KATEX_CSS}"><style>${CSS}</style></head>
<body><div class="page"><div class="grid"></div>
<div class="top"><div class="chips"><span class="chip lvl">${post.nivel}</span><span class="chip">${post.eje}</span></div><span class="num">#${post.id}</span></div>
${body}
<div class="foot"><span class="h">${HANDLE}</span><span>${idx}/${total}</span>${idx < total ? '<span class="swipe">Desliza →</span>' : '<span></span>'}</div>
</div></body></html>`;
}

function slides(post) {
  const L = 'ABCDE';
  const s1 = shell(post, 1, 3, `
<h1>PROBLEMA · ${post.tema.toUpperCase()}</h1>
<div class="stmt">${tex(post.enunciado)}</div>
<div class="opts">${post.alternativas.map((a, i) => `<div class="opt"><b>${L[i]}</b><span>${tex(a)}</span></div>`).join('')}</div>`);

  const s2 = shell(post, 2, 3, `
<h1>SOLUCIÓN</h1>
<div class="steps">${post.pasos.map((p, i) => `<div class="step"><i>${i + 1}</i><div>${tex(p)}</div></div>`).join('')}</div>
<div class="ans">Respuesta correcta: <span>${L[post.correcta]}) ${tex(post.alternativas[post.correcta])}</span></div>`);

  const s3 = shell(post, 3, 3, `
<h1>LA TRAMPA</h1>
<div class="trap">${tex(post.trampa)}</div>
<h1 style="margin-top:60px">CLAVE PARA LA PAES</h1>
<div class="stmt" style="font-size:38px">${tex(post.clave)}</div>
<div class="cta"><p>¿Qué alternativa marcaste?<br>Coméntala 👇</p><small>Guarda el post para repasar · Nuevos problemas todos los días</small></div>`);
  return [s1, s2, s3];
}

function caption(post) {
  const tags = ['#PAES', '#PAES2027', '#PAESMatematica', '#Matematica', '#PreuniversitarioOnline', '#EnsayoPAES', '#Chile',
    post.nivel === 'M2' ? '#PAESM2' : '#PAESM1', '#' + post.tema.normalize('NFD').replace(/[^A-Za-z0-9]/g, '')];
  return `${post.gancho || '¿Te atreves con este problema PAES?'}\n\n` +
    `📌 ${post.nivel} · ${post.eje} · ${post.tema}\n` +
    `1️⃣ Intenta resolverlo\n2️⃣ Comenta tu alternativa\n3️⃣ Desliza para ver la solución 👉\n\n` +
    `Guarda este post para repasar antes de la prueba.\n\n${tags.join(' ')}`;
}

(async () => {
  const [, , jsonPath, outDir] = process.argv;
  const post = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch({ executablePath: process.env.CHROME || undefined });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  const out = [];
  for (const [i, html] of slides(post).entries()) {
    const f = path.join(outDir, `${post.id}_${i + 1}.html`);
    fs.writeFileSync(f, html);
    await page.goto('file://' + f);
    await page.evaluate(() => document.fonts.ready);
    const prob = await page.evaluate(() => {
      const pg = document.querySelector('.page');
      const revisar = () => {
      const r = s => { const e = document.querySelector(s); return e ? e.getBoundingClientRect() : null; };
      const out = [];
      const foot = r('.foot');
      if (foot && foot.bottom > 1350 - 30) out.push('el pie se sale de la lámina');
      const pares = [['.stmt', '.opts'], ['.steps', '.ans'], ['.stmt', '.cta']];
      for (const [a, b] of pares) { const A = r(a), B = r(b); if (A && B && A.bottom > B.top - 8) out.push(`${a} se monta sobre ${b}`); }
      document.querySelectorAll('.stmt, .opt, .step div, .trap, .ans').forEach(e => { if (e.scrollWidth > e.clientWidth + 2) out.push('texto se sale a lo ancho'); });
      return out;
      };
      let out = revisar();
      for (let k = 0.96; out.length && k >= 0.7; k -= 0.04) { pg.style.setProperty('--k', k.toFixed(2)); out = revisar(); }
      return out;
    });
    if (prob.length) { console.error(`DESBORDE en lámina ${i + 1}: ${prob.join('; ')}`); await browser.close(); process.exit(2); }
    const png = path.join(outDir, `${i + 1}.jpg`);
    await page.screenshot({ path: png, type: 'jpeg', quality: 92 });
    fs.unlinkSync(f);
    out.push(png);
  }
  // Historia vertical 1080x1920 con la lamina del problema
  const story = `<!doctype html><html><head><meta charset="utf-8"><style>
    *{margin:0;padding:0;box-sizing:border-box}
    body{width:1080px;height:1920px;background:#0F1B2D;font-family:'Inter',sans-serif;color:#F4F1EA;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:56px}
    .t{font-size:54px;font-weight:800;text-align:center;line-height:1.2}
    .t span{color:#F5B83D}
    img{width:960px;border-radius:36px;box-shadow:0 30px 80px rgba(0,0,0,.45)}
    .b{font-size:46px;font-weight:700;text-align:center;line-height:1.3;background:#F5B83D;color:#0F1B2D;padding:28px 48px;border-radius:999px}
    .h{font-size:34px;color:#C9D3E3;font-weight:600}
  </style></head><body>
    <div class="t">🧠 Problema PAES <span>${post.nivel}</span><br>¿Te atreves?</div>
    <img src="file://${path.resolve(outDir, '1.jpg')}">
    <div class="b">Solución en el último post 👆</div>
    <div class="h">${HANDLE}</div>
  </body></html>`;
  const sf = path.join(outDir, 'historia.html');
  fs.writeFileSync(sf, story);
  await page.setViewportSize({ width: 1080, height: 1920 });
  await page.goto('file://' + path.resolve(sf));
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: path.join(outDir, 'historia.jpg'), type: 'jpeg', quality: 90 });
  fs.unlinkSync(sf);
  await browser.close();
  fs.writeFileSync(path.join(outDir, 'caption.txt'), caption(post));
  fs.writeFileSync(path.join(outDir, 'post.json'), JSON.stringify(post, null, 1));
  console.log(out.join('\n'));
})();
