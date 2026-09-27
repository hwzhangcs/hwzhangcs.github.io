#!/usr/bin/env node
// Render the built /cv/ page to assets/hanwen-zhang-cv.pdf using the site's print styles.
// Usage: bundle exec jekyll build --config _config.yml,_config_docker.yml && node scripts/build_cv_pdf.js [_site]
// Requires Playwright with Chromium: npm i -D playwright && npx playwright install chromium
const { chromium } = require('playwright');
const http = require('http'), fs = require('fs'), path = require('path');

const root = path.resolve(process.argv[2] || '_site');
const out = path.resolve(__dirname, '../assets/hanwen-zhang-cv.pdf');
const types = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.svg': 'image/svg+xml', '.woff2': 'font/woff2' };

const server = http.createServer((req, res) => {
  let file = path.join(root, decodeURIComponent(req.url.split(/[?#]/)[0]));
  if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');
  if (!fs.existsSync(file)) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { 'content-type': types[path.extname(file)] || 'application/octet-stream' });
  fs.createReadStream(file).pipe(res);
}).listen(0, async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ colorScheme: 'light' });
  await page.goto(`http://localhost:${server.address().port}/cv/`, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.querySelectorAll('details').forEach(detail => { detail.open = true; }));
  await page.pdf({ path: out, format: 'A4', margin: { top: '16mm', bottom: '16mm', left: '16mm', right: '16mm' } });
  await browser.close();
  server.close();
  console.log(`Wrote ${out}`);
});
