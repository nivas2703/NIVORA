// test_universe_flow.js
const http = require('http');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');

const PORT = 8992;
const DIST_DIR = path.resolve(__dirname, '../dist');

// MIME types
const MIMES = {
  '.html': 'text/html',
  '.css': 'text/css',
  '.js': 'application/javascript',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.webp': 'image/webp',
  '.svg': 'image/svg+xml'
};

// 1. Static Server
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

  // 2. Launch Chrome
  const chromePath = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
  const chromeProc = spawn(chromePath, [
    '--headless=new',
    '--remote-debugging-port=9222',
    '--disable-gpu',
    '--window-size=1440,900',
    '--user-data-dir=/tmp/chrome-test-profile-' + Date.now()
  ]);

  // Wait for debug port
  await new Promise(r => setTimeout(r, 1500));

  // Get WebSocket debugger URL
  const listRes = await fetch('http://127.0.0.1:9222/json/list');
  const pages = await listRes.json();
  const page = pages.find(p => p.type === 'page') || pages[0];
  const wsUrl = page.webSocketDebuggerUrl;
  console.log('Connected to Chrome:', wsUrl);

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

  // Enable Page & Runtime
  await send('Page.enable');
  await send('Runtime.enable');

  // Navigate
  console.log('Navigating...');
  await send('Page.navigate', { url: `http://localhost:${PORT}/` });
  await new Promise(r => setTimeout(r, 1200));

  // 1. Hero Screenshot
  await screenshot('universe_01_hero.png');

  // 2. Scroll to destinations
  console.log('Scrolling to destinations...');
  await evaluate(`
    document.getElementById('destinations').scrollIntoView({ behavior: 'instant', block: 'start' });
  `);
  await new Promise(r => setTimeout(r, 800));
  await screenshot('universe_02_destinations.png');

  // 3. Click Explore Concept on CHECKRA
  console.log('Clicking Explore Concept on CHECKRA...');
  await evaluate(`
    document.querySelector('.destination-planet-card.p-checkra .btn-explore-concept').click();
  `);
  await new Promise(r => setTimeout(r, 800));
  await screenshot('universe_03_checkra_world.png');

  // 4. Return to universe
  console.log('Returning to Universe...');
  await evaluate(`
    document.querySelector('.btn-return-universe').click();
  `);
  await new Promise(r => setTimeout(r, 600));

  // 5. Click Explore Concept on SAYORA
  console.log('Clicking Explore Concept on SAYORA...');
  await evaluate(`
    document.querySelector('.destination-planet-card.p-sayora .btn-explore-concept').click();
  `);
  await new Promise(r => setTimeout(r, 800));
  await screenshot('universe_04_sayora_world.png');

  // 6. Return and screenshot ecosystem & founder
  await evaluate(`
    document.querySelector('.btn-return-universe').click();
  `);
  await new Promise(r => setTimeout(r, 600));

  await evaluate(`
    document.getElementById('ecosystem').scrollIntoView({ behavior: 'instant', block: 'start' });
  `);
  await new Promise(r => setTimeout(r, 600));
  await screenshot('universe_05_ecosystem_founder.png');

  console.log('All screenshots completed successfully!');
  ws.close();
  chromeProc.kill();
  server.close();
  process.exit(0);
}

run().catch(err => {
  console.error('Test error:', err);
  process.exit(1);
});
