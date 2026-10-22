// Renderiza las escenas de un Reel (1080x1920) a PNG y deja escenas.json con las duraciones.
// Uso: node reel.js post.json carpeta_salida
const fs = require('fs');
const path = require('path');
const katex = require('katex');
const { chromium } = require('playwright-core');

const CONFIG = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'config.json'), 'utf8'));
const HANDLE = '@' + CONFIG.handle;
const KATEX_CSS = path.join(__dirname, 'node_modules/katex/dist/katex.min.css');
const L = 'ABCDE';

function tex(s) {
  return s.replace(/\\\$/g, '\u0000')
    .replace(/\$\$([\s\S]+?)\$\$/g, (_, m) => katex.renderToString(m, { displayMode: true, throwOnError: true }))
    .replace(/\$([^$]+?)\$/g, (_, m) => katex.renderToString(m, { throwOnError: true }))
    .replace(/\u0000/g, '$');
}

const CSS = `
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1920px;background:#0F1B2D;color:#F4F1EA;font-family:'Inter',sans-serif;overflow:hidden}
.page{position:relative;width:1080px;height:1920px;padding:150px 84px 260px;display:flex;flex-direction:column;--k:1}
.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:54px 54px}
.top{display:flex;justify-content:space-between;align-items:center;position:relative}
.chips{display:flex;gap:14px}
.chip{font-size:30px;font-weight:600;padding:12px 26px;border-radius:999px;background:rgba(255,255,255,.08);color:#C9D3E3}
.chip.lvl{background:#F5B83D;color:#0F1B2D}
.handle{font-size:30px;color:#C9D3E3;font-weight:600}
h1{font-size:34px;font-weight:700;letter-spacing:.18em;color:#F5B83D;margin:auto 0 30px;position:relative}
.page::after{content:'';margin-top:auto}
.page h1 ~ h1{margin-top:60px}
.stmt{font-size:calc(50px*var(--k));line-height:1.38;position:relative}
.opts{margin-top:60px;display:flex;flex-direction:column;gap:calc(22px*var(--k));position:relative}
.opt{display:flex;align-items:center;gap:30px;padding:calc(24px*var(--k)) 32px;border-radius:24px;background:rgba(255,255,255,.055);border:3px solid rgba(255,255,255,.07);font-size:calc(44px*var(--k))}
.opt b{width:68px;height:68px;flex:none;border-radius:50%;display:flex;align-items:center;justify-content:center;background:#1E2E47;color:#F5B83D;font-size:34px}
.opt.ok{border-color:#4ED39A;background:rgba(78,211,154,.16)}
.opt.ok b{background:#4ED39A;color:#0F1B2D}
.opt.dim{opacity:.35}
.count{position:absolute;right:84px;bottom:110px;width:170px;height:170px;border-radius:50%;background:#F5B83D;color:#0F1B2D;font-size:96px;font-weight:800;display:flex;align-items:center;justify-content:center}
.bar{position:absolute;left:84px;right:290px;bottom:180px;height:16px;border-radius:999px;background:rgba(255,255,255,.1);overflow:hidden}
.bar i{display:block;height:100%;background:#F5B83D}
.ask{position:absolute;left:84px;bottom:110px;font-size:40px;font-weight:700;color:#F5B83D}
.hook{margin:auto 0;text-align:center;position:relative}
.hook p{font-size:84px;font-weight:800;line-height:1.15}
.hook p span{color:#F5B83D}
.hook small{display:block;margin-top:40px;font-size:40px;color:#C9D3E3}
.steps{display:flex;flex-direction:column;gap:calc(38px*var(--k));position:relative}
.step{display:flex;gap:30px}
.step i{font-style:normal;flex:none;width:62px;height:62px;border-radius:16px;background:#F5B83D;color:#0F1B2D;font-weight:800;font-size:32px;display:flex;align-items:center;justify-content:center;margin-top:6px}
.step div{font-size:calc(42px*var(--k));line-height:1.42}
.step.new div{color:#fff}
.step.old{opacity:.55}
.big{margin-top:60px;padding:40px 44px;border-radius:28px;background:rgba(78,211,154,.14);border:3px solid #4ED39A;font-size:52px;font-weight:700;position:relative}
.big span{color:#4ED39A}
.trap{padding:40px 44px;border-radius:28px;background:rgba(245,184,61,.1);border:3px solid rgba(245,184,61,.5);font-size:calc(42px*var(--k));line-height:1.42;position:relative}
.trap strong{color:#F5B83D}
.cta{margin-top:90px;text-align:center;position:relative}
.cta p{font-size:56px;font-weight:800;line-height:1.25}
.cta p span{color:#F5B83D}
.cta small{display:block;margin-top:24px;font-size:36px;color:#C9D3E3}
`;

function shell(post, body) {
  return `<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="file://${KATEX_CSS}"><style>${CSS}</style></head>
<body><div class="page"><div class="grid"></div>
<div class="top"><div class="chips"><span class="chip lvl">PAES ${post.nivel}</span><span class="chip">${post.tema}</span></div><span class="handle">${HANDLE}</span></div>
${body}</div></body></html>`;
}

function opciones(post, modo) {
  return `<div class="opts">${post.alternativas.map((a, i) => {
    const cls = modo === 'resp' ? (i === post.correcta ? 'ok' : 'dim') : '';
    return `<div class="opt ${cls}"><b>${L[i]}</b><span>${tex(a)}</span></div>`;
  }).join('')}</div>`;
}

function escenas(post) {
  const E = [];
  E.push({ dur: 1.6, html: shell(post, `<div class="hook"><p>¿Lo resuelves en<br><span>15 segundos</span>? ⏱️</p><small>Problema tipo PAES · ${post.eje}</small></div>`) });
  const prob = `<h1>PROBLEMA</h1><div class="stmt">${tex(post.enunciado)}</div>${opciones(post, '')}`;
  const SEG = 15;
  for (let n = SEG; n >= 1; n--) {
    E.push({ dur: 1.3, tick: true, html: shell(post, `${prob}<div class="bar"><i style="width:${((SEG + 1 - n) / SEG) * 100}%"></i></div><div class="ask">Comenta tu respuesta 👇</div><div class="count">${n}</div>`) });
  }
  if (process.env.REEL_MODO === 'problema') return E;
  E.push({ dur: 2.4, ding: true, html: shell(post, `<h1>RESPUESTA</h1><div class="stmt">${tex(post.enunciado)}</div>${opciones(post, 'resp')}`) });
  post.pasos.forEach((_, k) => {
    const pasos = post.pasos.slice(0, k + 1).map((p, i) => `<div class="step ${i === k ? 'new' : 'old'}"><i>${i + 1}</i><div>${tex(p)}</div></div>`).join('');
    const extra = k === post.pasos.length - 1 ? `<div class="big">Respuesta: <span>${L[post.correcta]}) ${tex(post.alternativas[post.correcta])}</span></div>` : '';
    E.push({ dur: 3.4, whoosh: true, html: shell(post, `<h1>SOLUCIÓN</h1><div class="steps">${pasos}</div>${extra}`) });
  });
  E.push({ dur: 3.6, html: shell(post, `<h1>LA TRAMPA</h1><div class="trap">${tex(post.trampa)}</div><div class="cta"><p>Un problema PAES<br>todos los días 📚</p><p style="margin-top:20px"><span>Sigue a ${HANDLE}</span></p><small>Guarda y comparte con tu curso</small></div>`) });
  return E;
}

(async () => {
  const [, , jsonPath, outDir] = process.argv;
  const post = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch({ executablePath: process.env.CHROME || undefined });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  const lista = [];
  for (const [i, e] of escenas(post).entries()) {
    const f = path.resolve(outDir, `e${String(i).padStart(2, '0')}.html`);
    fs.writeFileSync(f, e.html);
    await page.goto('file://' + f);
    await page.evaluate(() => document.fonts.ready);
    const malo = await page.evaluate(() => {
      const pg = document.querySelector('.page');
      const choca = () => {
        const kids = [...pg.children].filter(c => !c.classList.contains('grid') && getComputedStyle(c).position !== 'absolute');
        const ultimo = kids[kids.length - 1].getBoundingClientRect();
        const anchos = [...document.querySelectorAll('.stmt, .opt, .step div, .trap')].some(e => e.scrollWidth > e.clientWidth + 2);
        return ultimo.bottom > 1920 - 250 || anchos;
      };
      let k = 1;
      while (choca() && k > 0.7) { k -= 0.04; pg.style.setProperty('--k', k.toFixed(2)); }
      return choca();
    });
    if (malo) { console.error(`DESBORDE en escena ${i}`); await browser.close(); process.exit(2); }
    const png = path.resolve(outDir, `e${String(i).padStart(2, '0')}.png`);
    await page.screenshot({ path: png });
    fs.unlinkSync(f);
    lista.push({ png, dur: e.dur, tick: !!e.tick, ding: !!e.ding, whoosh: !!e.whoosh });
  }
  await browser.close();
  fs.writeFileSync(path.join(outDir, 'escenas.json'), JSON.stringify(lista, null, 1));
  console.log(`${lista.length} escenas`);
})();
