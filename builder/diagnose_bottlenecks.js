// builder/diagnose_bottlenecks.js
const http = require('http');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');
const WebSocket = require('/Users/bennabathulanivas/Downloads/NIVORA/node_modules/ws');

const PORT = 8995;
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

async function main() {
  await new Promise(r => server.listen(PORT, r));
  console.log(`Diagnostic server running on http://localhost:${PORT}`);

  const chromeProc = spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', [
    '--headless=new',
    '--remote-debugging-port=9235',
    '--enable-webgl',
    '--use-gl=angle',
    '--use-angle=metal',
    '--no-sandbox',
    '--window-size=1920,1080', '--disable-frame-rate-limit', '--disable-gpu-vsync'
  ]);

  let wsUrl = null;
  for (let i = 0; i < 30; i++) {
    try {
      const data = await new Promise((resolve, reject) => {
        http.get('http://127.0.0.1:9235/json', res => {
          let buf = '';
          res.on('data', d => buf += d);
          res.on('end', () => resolve(JSON.parse(buf)));
        }).on('error', reject);
      });
      if (data && data.length > 0 && data[0].webSocketDebuggerUrl) {
        wsUrl = data[0].webSocketDebuggerUrl;
        break;
      }
    } catch (e) {
      await new Promise(r => setTimeout(r, 200));
    }
  }

  if (!wsUrl) throw new Error("Could not connect to Chrome port 9235");

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

  async function evaluate(expression) {
    const res = await send('Runtime.evaluate', { expression, returnByValue: true, awaitPromise: true });
    return res && res.result ? res.result.value : null;
  }

  await send('Page.enable');
  await send('Runtime.enable');
  await send('Page.navigate', { url: `http://localhost:${PORT}/` });
  await new Promise(r => setTimeout(r, 2000));

  // Test 1: Baseline scroll FPS with Lenis
  console.log("Test 1: Normal Scrolling FPS...");
  const t1 = await evaluate(`
    new Promise(resolve => {
      let frames = 0, start = performance.now();
      function f() {
        frames++;
        window.scrollBy(0, 30);
        if (performance.now() - start < 1500) requestAnimationFrame(f);
        else resolve(Math.round((frames * 1000) / (performance.now() - start)));
      }
      requestAnimationFrame(f);
    })
  `);
  console.log("Test 1 Result:", t1, "FPS");

  // Test 2: Disable Lenis and test native scroll
  console.log("Test 2: Without Lenis (native scroll only)...");
  await evaluate(`if (lenis) { lenis.destroy(); lenis = null; }`);
  const t2 = await evaluate(`
    new Promise(resolve => {
      let frames = 0, start = performance.now();
      function f() {
        frames++;
        window.scrollBy(0, 30);
        if (performance.now() - start < 1500) requestAnimationFrame(f);
        else resolve(Math.round((frames * 1000) / (performance.now() - start)));
      }
      requestAnimationFrame(f);
    })
  `);
  console.log("Test 2 Result (Without Lenis):", t2, "FPS");

  // Test 3: Disable all CSS backdrop-filters & filters
  console.log("Test 3: Without backdrop-filters & drop-shadows...");
  await evaluate(`
    const style = document.createElement('style');
    style.innerHTML = '* { backdrop-filter: none !important; -webkit-backdrop-filter: none !important; filter: none !important; }';
    document.head.appendChild(style);
  `);
  const t3 = await evaluate(`
    new Promise(resolve => {
      let frames = 0, start = performance.now();
      function f() {
        frames++;
        window.scrollBy(0, 30);
        if (performance.now() - start < 1500) requestAnimationFrame(f);
        else resolve(Math.round((frames * 1000) / (performance.now() - start)));
      }
      requestAnimationFrame(f);
    })
  `);
  console.log("Test 3 Result (No filters):", t3, "FPS");

  // Test 4: Pure stationary WebGL render loop (no scroll)
  console.log("Test 4: Stationary rendering FPS...");
  const t4 = await evaluate(`
    new Promise(resolve => {
      let frames = 0, start = performance.now();
      function f() {
        frames++;
        if (performance.now() - start < 1500) requestAnimationFrame(f);
        else resolve(Math.round((frames * 1000) / (performance.now() - start)));
      }
      requestAnimationFrame(f);
    })
  `);
  console.log("Test 4 Result (Stationary):", t4, "FPS");

  ws.close();
  chromeProc.kill();
  server.close();
}

main().catch(err => {
  console.error("Diagnosis error:", err);
  process.exit(1);
});
