// Renderiza una lista de trozos HTML a PNG. Uso: node html2png.js trabajos.json
// trabajos.json: [{html, out, w, h, transparente, rects:true|false}]
const fs = require('fs');
const path = require('path');
const { chromium } = require(process.env.RENDER_DIR + '/node_modules/playwright-core');

(async () => {
  const trabajos = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const browser = await chromium.launch({ executablePath: process.env.CHROME });
  const page = await browser.newPage();
  for (const t of trabajos) {
    await page.setViewportSize({ width: t.w, height: t.h });
    const f = path.resolve(t.out + '.html');
    fs.writeFileSync(f, t.html);
    await page.goto('file://' + f);
    await page.evaluate(() => document.fonts.ready);
    if (t.rects) {
      const datos = await page.evaluate(() => {
        const R = r => ({ x: Math.floor(r.left) - 6, y: Math.floor(r.top) - 6, w: Math.ceil(r.width) + 12, h: Math.ceil(r.height) + 12 });
        const renglones = el => {
          const rg = document.createRange(); rg.selectNodeContents(el);
          const rs = [...rg.getClientRects()].filter(r => r.width > 2 && r.height > 8);
          const filas = [];
          for (const r of rs.sort((a, b) => a.top - b.top || a.left - b.left)) {
            const f = filas.find(f => Math.abs((f.top + f.bottom) / 2 - (r.top + r.bottom) / 2) < 25);
            if (f) { f.left = Math.min(f.left, r.left); f.right = Math.max(f.right, r.right); f.top = Math.min(f.top, r.top); f.bottom = Math.max(f.bottom, r.bottom); }
            else filas.push({ ...r.toJSON() });
          }
          return filas.map(f => R({ left: f.left, top: f.top, width: f.right - f.left, height: f.bottom - f.top }));
        };
        return [...document.querySelectorAll('[data-bloque]')].map(b =>
          b.classList.contains('caja') ? [R(b.getBoundingClientRect())] : [...b.querySelectorAll('.linea')].flatMap(renglones));
      });
      fs.writeFileSync(t.out + '.json', JSON.stringify(datos));
    }
    await page.screenshot({ path: t.out, omitBackground: !!t.transparente });
    if (t.oculto) {
      await page.addStyleTag({ content: t.oculto });
      await page.screenshot({ path: t.out.replace('.png', '_vacia.png'), omitBackground: !!t.transparente });
    }
    fs.unlinkSync(f);
  }
  await browser.close();
})();
