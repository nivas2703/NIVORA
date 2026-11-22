// test_space_travel_journey.js
const http = require('http');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');

const PORT = 8998;
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
    '--remote-debugging-port=9224',
    '--disable-gpu',
    '--window-size=1920,1080',
    '--user-data-dir=/tmp/chrome-space-travel-profile-' + Date.now()
  ]);

  let listRes, pages;
  for (let attempt = 0; attempt < 10; attempt++) {
    try {
      await new Promise(r => setTimeout(r, 600));
      listRes = await fetch('http://127.0.0.1:9224/json/list');
      pages = await listRes.json();
      if (pages && pages.length) break;
    } catch (e) {}
  }
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

  console.log('Navigating to Space-Travel Test...');
  await send('Page.navigate', { url: `http://localhost:${PORT}/` });
  await new Promise(r => setTimeout(r, 1800));

  // 1. Initial Hero state (NIVORA CORE)
  console.log('Capturing: 01_space_hero_core.png');
  await screenshot('01_space_hero_core.png');

  // 2. Simulate fast scroll DOWN to trigger warp streaks / motion trails!
  console.log('Simulating Fast Scroll DOWN to trigger motion streaks...');
  await evaluate(`
    window.scrollBy({ top: 900, behavior: 'instant' });
  `);
  // Capture immediately while velocity is high (star trails stretched)
  await new Promise(r => setTimeout(r, 60));
  await screenshot('02_space_warp_streaks_down.png');

  // 3. Arrival at Products (Destination: Product Constellation)
  console.log('Arriving at Destination: Products Constellation...');
  await evaluate(`
    document.getElementById('products').scrollIntoView({ behavior: 'instant', block: 'start' });
  `);
  await new Promise(r => setTimeout(r, 500));
  await screenshot('03_space_dest_products.png');

  // 4. Travel to The Builder (About)
  console.log('Travelling to Destination: The Builder (About)...');
  await evaluate(`
    document.getElementById('about').scrollIntoView({ behavior: 'instant', block: 'start' });
  `);
  await new Promise(r => setTimeout(r, 500));
  await screenshot('04_space_dest_about.png');

  // 5. Travel to Creation Field (Portfolio)
  console.log('Travelling to Destination: Creation Field (Portfolio)...');
  await evaluate(`
    document.getElementById('portfolio').scrollIntoView({ behavior: 'instant', block: 'start' });
  `);
  await new Promise(r => setTimeout(r, 500));
  await screenshot('05_space_dest_portfolio.png');

  // 6. Travel to The Transmission Point (Contact)
  console.log('Travelling to Destination: Transmission (Contact)...');
  await evaluate(`
    document.getElementById('contact').scrollIntoView({ behavior: 'instant', block: 'start' });
  `);
  await new Promise(r => setTimeout(r, 500));
  await screenshot('06_space_dest_transmission.png');

  // 7. Simulate Fast Scroll UP (Reverse Warp Travel)
  console.log('Simulating Reverse Scroll UP (reverse star flow)...');
  await evaluate(`
    window.scrollBy({ top: -800, behavior: 'instant' });
  `);
  await new Promise(r => setTimeout(r, 60));
  await screenshot('07_space_reverse_warp.png');

  console.log('Space Travel test sequence completed successfully!');
  chromeProc.kill();
  server.close();
  process.exit(0);
}

run().catch(err => {
  console.error(err);
  process.exit(1);
});
