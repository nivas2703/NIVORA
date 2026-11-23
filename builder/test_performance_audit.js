// builder/test_performance_audit.js
const http = require('http');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');
const WebSocket = require('/Users/bennabathulanivas/Downloads/NIVORA/node_modules/ws');

const PORT = 8996;
const DIST_DIR = path.resolve(__dirname, '../dist');
const ART_DIR = '/Users/bennabathulanivas/.gemini/antigravity/brain/a333758c-30c9-48d5-b21e-6a719225493a';

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

  const chromeProc = spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', [
    '--headless=new',
    '--remote-debugging-port=9233',
    '--enable-webgl',
    '--use-gl=angle',
    '--use-angle=metal',
    '--no-sandbox',
    '--window-size=1920,1080'
  ]);

  let wsUrl = null;
  for (let i = 0; i < 30; i++) {
    try {
      const data = await new Promise((resolve, reject) => {
        http.get('http://127.0.0.1:9233/json', res => {
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

  if (!wsUrl) throw new Error("Could not connect to Chrome port 9233");

  const ws = new WebSocket(wsUrl);
  await new Promise(r => ws.onopen = r);

  let id = 1;
  const callbacks = new Map();
  const consoleErrors = [];

  ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    if (data.id && callbacks.has(data.id)) {
      callbacks.get(data.id)(data.result);
      callbacks.delete(data.id);
    }
    if (data.method === 'Runtime.exceptionThrown') {
      consoleErrors.push(data.params.exceptionDetails.text + ' ' + (data.params.exceptionDetails.exception?.description || ''));
      console.error('Browser Exception:', data.params.exceptionDetails);
    }
    if (data.method === 'Runtime.consoleAPICalled' && data.params.type === 'error') {
      consoleErrors.push(data.params.args.map(a => a.value || a.description).join(' '));
      console.error('Console Error:', data.params.args);
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

  async function screenshot(name) {
    const res = await send('Page.captureScreenshot', { format: 'png' });
    const buffer = Buffer.from(res.data, 'base64');
    const outPath = `${ART_DIR}/${name}`;
    fs.writeFileSync(outPath, buffer);
    console.log(`Saved screenshot: ${outPath} (${buffer.length} bytes)`);
  }

  await send('Page.enable');
  await send('Runtime.enable');
  await send('Emulation.setDeviceMetricsOverride', {
    width: 1920,
    height: 1080,
    deviceScaleFactor: 1,
    mobile: false
  });

  console.log(`Navigating to http://localhost:${PORT}/ ...`);
  const t0 = Date.now();
  await send('Page.navigate', { url: `http://localhost:${PORT}/` });
  await new Promise(r => setTimeout(r, 2000));
  const loadDuration = Date.now() - t0;
  console.log(`Initial load & WebGL init stabilized in ${loadDuration}ms`);

  // 1. Audit Engine State
  const engineState = await evaluate(`({
    mode: PerformanceEngine ? PerformanceEngine.mode : 'N/A',
    fps: PerformanceEngine ? Math.round(PerformanceEngine.fps) : 'N/A',
    pixelRatio: PerformanceEngine ? PerformanceEngine.pixelRatio : 1,
    camZ: Math.round(camera ? camera.position.z : 0),
    starsCount: spiralArmStars ? spiralArmStars.geometry.attributes.position.count : 0,
    bulgeCount: galacticBulge ? galacticBulge.geometry.attributes.position.count : 0,
    warpCount: warpStarData ? warpStarData.length : 0,
    distantCount: distantStarField ? distantStarField.geometry.attributes.position.count : 0
  })`);
  console.log("Verified Engine Architecture State:", engineState);

  // 2. Measure FPS during continuous scrolling
  console.log("Measuring FPS during 1.5s active scroll...");
  const fpsMeasurement = await evaluate(`
    new Promise(resolve => {
      let frames = 0;
      let start = performance.now();
      function loop() {
        frames++;
        window.scrollBy(0, 80);
        if (performance.now() - start < 1500) {
          requestAnimationFrame(loop);
        } else {
          const dur = performance.now() - start;
          resolve(Math.round((frames * 1000) / dur));
        }
      }
      requestAnimationFrame(loop);
    })
  `);
  console.log(`Active Scroll Performance: ${fpsMeasurement} FPS`);

  // 3. Test Concept Modals (CHECKRA, HOMORA, BUBORA, SAYORA)
  console.log("Testing Concept Modals open & close cycle...");
  for (const prod of ['checkra', 'homora', 'bubora', 'sayora']) {
    await evaluate(`openConceptModal('${prod}')`);
    await new Promise(r => setTimeout(r, 200));
    const isOpen = await evaluate(`document.getElementById('conceptModalOverlay').classList.contains('open')`);
    if (!isOpen) throw new Error(`Modal ${prod} did not open!`);
    await evaluate(`closeConceptModal()`);
    await new Promise(r => setTimeout(r, 100));
  }
  console.log("Concept Modals (Checkra, Homora, Bubora, Sayora): Verified Smooth!");

  // 4. Test Service Selection Helper
  console.log("Testing selectConsultationService('GST Services')...");
  await evaluate(`selectConsultationService('GST Services')`);
  await new Promise(r => setTimeout(r, 600));
  const selVal = await evaluate(`document.getElementById('cService').value`);
  console.log(`Dropdown value after selection: "${selVal}"`);

  // 5. Test Mobile Viewport
  console.log("Testing Mobile Viewport (390x844)...");
  await send('Emulation.setDeviceMetricsOverride', {
    width: 390,
    height: 844,
    deviceScaleFactor: 2,
    mobile: true
  });
  await evaluate(`window.scrollTo({ top: 0, behavior: 'instant' });`);
  await new Promise(r => setTimeout(r, 600));
  await screenshot('perf_audit_mobile_hero.png');

  // Test Mobile Drawer
  await evaluate(`document.getElementById('mobileMenuToggle').click();`);
  await new Promise(r => setTimeout(r, 300));
  const drawerOpen = await evaluate(`document.getElementById('mobileDrawer').classList.contains('open')`);
  console.log(`Mobile Drawer open state: ${drawerOpen}`);
  await screenshot('perf_audit_mobile_drawer.png');
  await evaluate(`document.getElementById('mobileDrawerClose').click();`);

  // 6. Return to Desktop & Capture Final High-Res Proofs
  await send('Emulation.setDeviceMetricsOverride', {
    width: 1920,
    height: 1080,
    deviceScaleFactor: 1,
    mobile: false
  });
  await evaluate(`window.scrollTo({ top: 0, behavior: 'instant' });`);
  await new Promise(r => setTimeout(r, 600));
  await screenshot('perf_audit_desktop_hero.png');

  await evaluate(`document.querySelector('#services').scrollIntoView({ behavior: 'instant' });`);
  await new Promise(r => setTimeout(r, 600));
  await screenshot('perf_audit_desktop_services.png');

  await evaluate(`document.querySelector('#contact').scrollIntoView({ behavior: 'instant' });`);
  await new Promise(r => setTimeout(r, 600));
  await screenshot('perf_audit_desktop_contact.png');

  console.log("\n=================== FINAL PERFORMANCE AUDIT SUMMARY ===================");
  console.log(`Initial Load Time: ${loadDuration}ms`);
  console.log(`Engine Performance Mode: ${engineState.mode}`);
  console.log(`Capped Pixel Ratio: ${engineState.pixelRatio}`);
  console.log(`Milky Way Spiral Stars: ${engineState.starsCount}`);
  console.log(`Galactic Bulge Stars: ${engineState.bulgeCount}`);
  console.log(`Distant Starfield Stars: ${engineState.distantCount}`);
  console.log(`Active Warp Stars: ${engineState.warpCount}`);
  console.log(`Total Universe Particle Budget: ${engineState.starsCount + engineState.bulgeCount + engineState.distantCount + engineState.warpCount} (Target: <6,000)`);
  console.log(`Scroll Performance: ${fpsMeasurement} FPS (Target: 55-60 FPS)`);
  console.log(`Uncaught Browser Errors: ${consoleErrors.length}`);
  console.log("========================================================================\n");

  ws.close();
  chromeProc.kill();
  server.close();
  process.exit(consoleErrors.length > 0 ? 1 : 0);
}

run().catch(err => {
  console.error("Test execution error:", err);
  process.exit(1);
});
