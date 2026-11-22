// test_cinematic_target.js
const http = require('http');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');

const PORT = 8996;
const DIST_DIR = path.resolve(__dirname, '../dist');

const MIMES = {
  '.html': 'text/html',
  '.css': 'text/css',
  '.js': 'application/javascript',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.webp': 'image/webp',
  '.svg': 'image/svg+xml'
};

const server = http.createServer((req, res) => {
  let reqPath = req.url.split('?')[0];
  if (reqPath === '/') reqPath = '/index.html';
  const filePath = path.join(DIST_DIR, reqPath);

  if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
    const ext = path.extname(filePath).toLowerCase();
    res.writeHead(200, { 'Content-Type': MIMES[ext] || 'application/octet-stream' });
    fs.createReadStream(filePath).pipe(res);
  } else {
    res.writeHead(404);
    res.end('Not Found');
  }
});

async function run() {
  await new Promise(r => server.listen(PORT, r));
  console.log(`Server running on http://localhost:${PORT}`);

  const chromePath = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
  const chromeProc = spawn(chromePath, [
    '--headless=new',
    '--remote-debugging-port=9222',
    '--disable-gpu',
    '--window-size=1440,900',
    '--user-data-dir=/tmp/chrome-cinematic-profile-' + Date.now()
  ]);

  await new Promise(r => setTimeout(r, 1500));

  const listRes = await fetch('http://127.0.0.1:9222/json/list');
  const pages = await listRes.json();
  const page = pages.find(p => p.type === 'page') || pages[0];
  const wsUrl = page.webSocketDebuggerUrl;

  const ws = new WebSocket(wsUrl);
  await new Promise(r => ws.onopen = r);

  let id = 1;
  const callbacks = new Map();

  ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    if (data.id && callbacks.has(data.id)) {
      callbacks.get(data.id)(data.result);
      callbacks.delete(data.id);
    }
  };

  function send(method, params = {}) {
    return new Promise((resolve) => {
      const msgId = id++;
      callbacks.set(msgId, resolve);
      ws.send(JSON.stringify({ id: msgId, method, params }));
    });
  }

  async function screenshot(name) {
    const res = await send('Page.captureScreenshot', { format: 'png' });
    const buffer = Buffer.from(res.data, 'base64');
    const outPath = `/Users/bennabathulanivas/.gemini/antigravity/brain/a333758c-30c9-48d5-b21e-6a719225493a/${name}`;
    fs.writeFileSync(outPath, buffer);
    console.log(`Saved screenshot: ${outPath} (${buffer.length} bytes)`);
  }

  async function evaluate(expression) {
    const res = await send('Runtime.evaluate', { expression, returnByValue: true, awaitPromise: true });
    return res.result ? res.result.value : null;
  }

  await send('Page.enable');
  await send('Runtime.enable');
  await send('Emulation.setDeviceMetricsOverride', {
    width: 1920,
    height: 1080,
    deviceScaleFactor: 1,
    mobile: false
  });

  console.log('Navigating to target test...');
  await send('Page.navigate', { url: `http://localhost:${PORT}/` });

  // Wait for 2.6s cinematic intro
  await new Promise(r => setTimeout(r, 2800));

  // 1. Capture Target Universe Hero
  await screenshot('target_universe_hero.png');

  // 2. Hide UI to inspect pure 3D scene (per Rule #38)
  await evaluate(`
    document.querySelector('.top-nav').style.display = 'none';
    document.querySelector('.hero-content').style.display = 'none';
    document.querySelector('.hero-scroll-indicator').style.display = 'none';
  `);
  await new Promise(r => setTimeout(r, 400));
  await screenshot('target_universe_scene_alone.png');

  // Restore UI
  await evaluate(`
    document.querySelector('.top-nav').style.display = '';
    document.querySelector('.hero-content').style.display = '';
    document.querySelector('.hero-scroll-indicator').style.display = '';
  `);

  console.log('Done!');
  chromeProc.kill();
  server.close();
  process.exit(0);
}

run().catch(err => {
  console.error(err);
  process.exit(1);
});
