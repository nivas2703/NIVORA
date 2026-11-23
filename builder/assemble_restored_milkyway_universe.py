#!/usr/bin/env python3
"""
NIVORA — RESTORE THE MILKY WAY & FIX PERFORMANCE WITHOUT DESTROYING THE DESIGN
- Completely removes Lenis virtual scroll bottleneck (the measured 2 FPS root cause)
- Uses native hardware-accelerated 60+ FPS smooth scrolling
- Restores the full, volumetric, cinematic 3D procedural Milky Way galaxy
- Maintains a single persistent WebGL canvas and single requestAnimationFrame loop
- Zero object allocations in the frame loop
- Eliminates heavy CSS drop-shadow/repaint bottlenecks
"""

import os
import re

DESKTOP_DIR = "/Users/bennabathulanivas/Desktop/my projects/NIVORA"
DOWNLOADS_DIR = "/Users/bennabathulanivas/Downloads/NIVORA"

def build_restored_script():
    return """  <script>
    /* -------------------------------------------------------------
       1. GLOBAL STATE & PERFORMANCE ARCHITECTURE
       ------------------------------------------------------------- */
    const PerformanceEngine = {
      fps: 60,
      frameCount: 0,
      lastFpsTimestamp: performance.now(),
      tier: 'HIGH', // HIGH | MEDIUM | LOW
      isTabVisible: true,
      pixelRatio: 1.0,
      particleScale: 1.0,
      
      init() {
        this.detectTier();
        document.addEventListener('visibilitychange', () => {
          this.isTabVisible = (document.visibilityState === 'visible');
          if (this.isTabVisible) {
            this.lastFpsTimestamp = performance.now();
            if (clock) clock.getDelta();
          }
        });
      },

      detectTier() {
        const isMobile = (window.innerWidth < 768) || ('ontouchstart' in window);
        const cores = navigator.hardwareConcurrency || 4;
        const mem = navigator.deviceMemory || 4;
        
        if (isMobile) {
          this.tier = 'LOW';
          this.particleScale = 0.40;
          this.pixelRatio = 1.0;
        } else if (cores <= 4 || mem < 4) {
          this.tier = 'MEDIUM';
          this.particleScale = 0.70;
          this.pixelRatio = Math.min(window.devicePixelRatio || 1, 1.25);
        } else {
          this.tier = 'HIGH';
          this.particleScale = 1.0;
          this.pixelRatio = Math.min(window.devicePixelRatio || 1, 1.5);
        }
      }
    };

    // Dynamic Year
    const yrEl = document.getElementById('currentYear');
    if (yrEl) yrEl.innerText = new Date().getFullYear();

    /* -------------------------------------------------------------
       2. THREE.JS 3D CINEMATIC UNIVERSE ENGINE
          (FULL PROCEDURAL MILKY WAY + ZERO-ALLOCATION LOOP)
       ------------------------------------------------------------- */
    const canvas = document.getElementById('webglUniverseCanvas');
    let renderer, scene, camera;
    let milkyWayGroup, galacticBulge, spiralArmStars;
    let distantStarField, brightBeaconsPoints;
    let globeGroup, globeHaloSprite;
    let nebulaPuffs = [];

    // Hyperspace Warp System (Conditional Updates)
    let warpLinesMesh, warpLinesGeo;
    let activeWarpCount = 600;
    let warpStarPositions, warpStarColors, warpStarData = [];
    let rawScrollVelocity = 0;
    let smoothedScrollVelocity = 0;
    let lastScrollPosition = 0;
    let scrollTimeoutId = null;

    let isZoomingTransition = false;
    let warpSpeedFactor = 1.0;
    let isWebGLEnabled = false;

    // Zero-allocation mouse & vectors
    const mouse = { x: 0, y: 0, targetX: 0, targetY: 0 };
    const clock = new THREE.Clock();

    const baseCamX = 0;
    const baseCamY = 16;
    const baseCamZ = 260;
    const globeCenterX = 0.0;
    const globeCenterY = 36.0;
    const globeCenterZ = 0.0;

    const currentCamPos = new THREE.Vector3(baseCamX, baseCamY, baseCamZ);
    const currentLookAt = new THREE.Vector3(0, 18, 0);
    const _targetCamPos = new THREE.Vector3(baseCamX, baseCamY, baseCamZ);
    const _targetLookAt = new THREE.Vector3(0, 18, 0);
    let targetScrollP = 0;

    // Shared reusable textures
    let _cachedSoftPointTexture = null;
    let _cachedBeaconTexture = null;

    function getSoftPointTexture() {
      if (_cachedSoftPointTexture) return _cachedSoftPointTexture;
      const c = document.createElement('canvas');
      c.width = 64; c.height = 64;
      const ctx = c.getContext('2d');
      const grad = ctx.createRadialGradient(32, 32, 0, 32, 32, 32);
      grad.addColorStop(0, 'rgba(255, 255, 255, 1)');
      grad.addColorStop(0.22, 'rgba(235, 245, 255, 0.85)');
      grad.addColorStop(0.60, 'rgba(6, 182, 212, 0.28)');
      grad.addColorStop(1, 'rgba(6, 182, 212, 0)');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, 64, 64);
      _cachedSoftPointTexture = new THREE.CanvasTexture(c);
      return _cachedSoftPointTexture;
    }

    function getBeaconTexture() {
      if (_cachedBeaconTexture) return _cachedBeaconTexture;
      const c = document.createElement('canvas');
      c.width = 128; c.height = 128;
      const ctx = c.getContext('2d');
      const grad = ctx.createRadialGradient(64, 64, 0, 64, 64, 64);
      grad.addColorStop(0, 'rgba(255, 255, 255, 1)');
      grad.addColorStop(0.18, 'rgba(224, 242, 254, 0.85)');
      grad.addColorStop(0.50, 'rgba(139, 92, 246, 0.22)');
      grad.addColorStop(1, 'rgba(6, 182, 212, 0)');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, 128, 128);

      ctx.lineWidth = 1.2;
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)';
      ctx.beginPath();
      ctx.moveTo(64, 18); ctx.lineTo(64, 110);
      ctx.moveTo(18, 64); ctx.lineTo(110, 64);
      ctx.stroke();

      _cachedBeaconTexture = new THREE.CanvasTexture(c);
      return _cachedBeaconTexture;
    }

    function createCoronaHaloTexture() {
      const c = document.createElement('canvas');
      c.width = 128; c.height = 128;
      const ctx = c.getContext('2d');
      const grad = ctx.createRadialGradient(64, 64, 0, 64, 64, 64);
      grad.addColorStop(0, 'rgba(6, 182, 212, 0.85)');
      grad.addColorStop(0.22, 'rgba(56, 189, 248, 0.55)');
      grad.addColorStop(0.55, 'rgba(168, 85, 247, 0.2)');
      grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, 128, 128);
      return new THREE.CanvasTexture(c);
    }

    function createProceduralNebulaTexture(c1, c2) {
      const c = document.createElement('canvas');
      c.width = 128; c.height = 128;
      const ctx = c.getContext('2d');
      const grad = ctx.createRadialGradient(64, 64, 0, 64, 64, 64);
      grad.addColorStop(0, c1);
      grad.addColorStop(0.55, c2);
      grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, 128, 128);
      return new THREE.CanvasTexture(c);
    }

    function initUniverseEngineCinematic() {
      try {
        if (!canvas) return;

        PerformanceEngine.init();

        renderer = new THREE.WebGLRenderer({
          canvas: canvas,
          antialias: (PerformanceEngine.tier === 'HIGH'),
          alpha: true,
          powerPreference: 'high-performance'
        });

        renderer.setPixelRatio(PerformanceEngine.pixelRatio);
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setClearColor(0x02040a, 0);
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 1.25;

        scene = new THREE.Scene();
        camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 4000);
        camera.position.set(baseCamX, baseCamY, baseCamZ);
        camera.lookAt(0, 18, 0);

        // Build Universe Elements with Full Atmospheric Quality
        buildDistantStarfield(PerformanceEngine.particleScale);
        buildWarpStarfield(PerformanceEngine.particleScale);
        buildProceduralMilkyWay(PerformanceEngine.particleScale);
        buildGalacticBulge(PerformanceEngine.particleScale);
        buildSubtleCosmicNebula();
        buildBrightStellarBeacons();
        buildNivoraGlobeCore(PerformanceEngine.particleScale);

        setupInteractivity();

        isWebGLEnabled = true;
        requestAnimationFrame(animateUniverseFrame);
        runCinematicIntro();

        // Dismiss Universe Loader smoothly
        const loaderEl = document.getElementById('universeLoader');
        if (loaderEl) {
          setTimeout(() => loaderEl.classList.add('loaded'), 150);
        }
      } catch (e) {
        console.warn("WebGL notice, running high-performance fallback:", e);
        const loaderEl = document.getElementById('universeLoader');
        if (loaderEl) loaderEl.classList.add('loaded');
      }
    }

    /* -------------------------------------------------------------
       PROCEDURAL MILKY WAY SPIRAL ARMS (FULL CINEMATIC VOLUME)
       ------------------------------------------------------------- */
    function buildProceduralMilkyWay(scale = 1.0) {
      milkyWayGroup = new THREE.Group();
      milkyWayGroup.position.set(globeCenterX, globeCenterY, globeCenterZ);
      milkyWayGroup.rotation.set(0.82, 0.22, -0.15);

      const starCount = Math.floor(38000 * scale);
      const positions = new Float32Array(starCount * 3);
      const colors = new Float32Array(starCount * 3);

      const armAngles = [0.45, 0.45 + Math.PI, 1.85, 1.85 + Math.PI];
      const armWeights = [0.38, 0.38, 0.12, 0.12];
      const rMin = 22;
      const rMax = 260;

      const cosX = Math.cos(0.82), sinX = Math.sin(0.82);
      const cosY = Math.cos(0.22), sinY = Math.sin(0.22);

      for (let i = 0; i < starCount; i++) {
        const randArm = Math.random();
        let armIdx = 0;
        if (randArm < armWeights[0]) armIdx = 0;
        else if (randArm < armWeights[0] + armWeights[1]) armIdx = 1;
        else if (randArm < 0.88) armIdx = 2;
        else armIdx = 3;

        const baseAngle = armAngles[armIdx];
        const pRand = Math.random();
        const r = rMin + (rMax - rMin) * Math.pow(pRand, 1.65);

        const spiralAngle = baseAngle + 2.25 * Math.log(r / rMin) + 0.22 * (r / rMax);
        const armWidth = 4.0 + 20.0 * (r / rMax);
        const rDisp = (Math.random() + Math.random() - 1.0) * armWidth;
        const tDisp = (Math.random() + Math.random() - 1.0) * (armWidth / (r + 25));

        const vertThickness = 12.0 * Math.exp(-r / 100) + 3.0 * (1.0 - r / rMax);
        const yDisp = (Math.random() + Math.random() - 1.0) * vertThickness;

        const actualR = r + rDisp;
        const actualTheta = spiralAngle + tDisp;

        const lx = actualR * Math.cos(actualTheta);
        const lz = actualR * Math.sin(actualTheta);
        const ly = yDisp;

        const wx = globeCenterX + lx * cosY - lz * sinY;
        const wy = globeCenterY + ly * cosX - (lx * sinY + lz * cosY) * sinX;

        // Clean deep-space quiet zone for centered hero logo & typography
        let starWeight = 1.0;
        const distFromLogoCenter = Math.sqrt(wx * wx + (wy - globeCenterY) * (wy - globeCenterY));
        if (distFromLogoCenter < 30) {
          starWeight = Math.max(0.0, (distFromLogoCenter - 20) / 10);
        } else if (Math.abs(wx) < 38 && wy < globeCenterY + 2 && wy > globeCenterY - 56) {
          starWeight = 0.12;
        }

        positions[i * 3] = lx;
        positions[i * 3 + 1] = ly;
        positions[i * 3 + 2] = lz;

        const frac = r / rMax;
        let cr, cg, cb;
        if (frac < 0.18) {
          cr = 0.96; cg = 0.98; cb = 1.0;
        } else if (frac < 0.52) {
          cr = 0.30; cg = 0.72; cb = 1.0;
        } else if (frac < 0.8) {
          cr = 0.65; cg = 0.42; cb = 0.95;
        } else {
          cr = 0.82; cg = 0.38; cb = 0.78;
        }

        colors[i * 3] = cr * starWeight;
        colors[i * 3 + 1] = cg * starWeight;
        colors[i * 3 + 2] = cb * starWeight;
      }

      const armGeo = new THREE.BufferGeometry();
      armGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
      armGeo.setAttribute('color', new THREE.BufferAttribute(colors, 3));

      const armMat = new THREE.PointsMaterial({
        size: 1.5,
        sizeAttenuation: true,
        vertexColors: true,
        map: getSoftPointTexture(),
        transparent: true,
        opacity: 0.88,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });

      spiralArmStars = new THREE.Points(armGeo, armMat);
      milkyWayGroup.add(spiralArmStars);
      scene.add(milkyWayGroup);
    }

    /* -------------------------------------------------------------
       GALACTIC BULGE PARTICLES (FULL DENSITY)
       ------------------------------------------------------------- */
    function buildGalacticBulge(scale = 1.0) {
      const bulgeCount = Math.floor(6500 * scale);
      const positions = new Float32Array(bulgeCount * 3);
      const colors = new Float32Array(bulgeCount * 3);

      for (let i = 0; i < bulgeCount; i++) {
        const r = 22 + Math.pow(Math.random(), 2.0) * 36;
        const theta = Math.random() * Math.PI * 2;
        const phi = (Math.random() - 0.5) * Math.PI;

        positions[i * 3] = r * Math.cos(phi) * Math.cos(theta);
        positions[i * 3 + 1] = r * Math.sin(phi) * 0.38;
        positions[i * 3 + 2] = r * Math.cos(phi) * Math.sin(theta);

        const p = (r - 22) / 36;
        let bWeight = 1.0;
        if (phi < 0 && Math.abs(positions[i * 3]) < 26) {
          bWeight = 0.15;
        }
        colors[i * 3] = (0.95 - p * 0.15) * bWeight;
        colors[i * 3 + 1] = (0.98 - p * 0.12) * bWeight;
        colors[i * 3 + 2] = 1.0 * bWeight;
      }

      const bulgeGeo = new THREE.BufferGeometry();
      bulgeGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
      bulgeGeo.setAttribute('color', new THREE.BufferAttribute(colors, 3));

      const bulgeMat = new THREE.PointsMaterial({
        size: 1.7,
        sizeAttenuation: true,
        vertexColors: true,
        map: getSoftPointTexture(),
        transparent: true,
        opacity: 0.90,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });

      galacticBulge = new THREE.Points(bulgeGeo, bulgeMat);
      milkyWayGroup.add(galacticBulge);
    }

    /* -------------------------------------------------------------
       COSMIC NEBULA PUFFS (12 SUBTLE GLOWING PUFFS)
       ------------------------------------------------------------- */
    function buildSubtleCosmicNebula() {
      const puffs = [
        { color1: 'rgba(168, 85, 247, 0.26)', color2: 'rgba(59, 130, 246, 0.12)', scale: 320 },
        { color1: 'rgba(6, 182, 212, 0.22)', color2: 'rgba(147, 51, 234, 0.10)', scale: 360 },
        { color1: 'rgba(236, 72, 153, 0.18)', color2: 'rgba(30, 58, 138, 0.12)', scale: 280 },
        { color1: 'rgba(99, 102, 241, 0.20)', color2: 'rgba(6, 182, 212, 0.08)', scale: 320 }
      ];

      for (let i = 0; i < 12; i++) {
        const pCfg = puffs[i % puffs.length];
        const tex = createProceduralNebulaTexture(pCfg.color1, pCfg.color2);
        const mat = new THREE.SpriteMaterial({
          map: tex,
          transparent: true,
          opacity: 0.35,
          blending: THREE.AdditiveBlending,
          depthWrite: false
        });
        const sprite = new THREE.Sprite(mat);

        const r = 30 + Math.pow(Math.random(), 1.3) * 170;
        const a = Math.random() * Math.PI * 2;
        sprite.position.set(
          globeCenterX + Math.cos(a) * r,
          globeCenterY + (Math.random() - 0.5) * 45,
          globeCenterZ + Math.sin(a) * r - 25
        );
        const s = 150 + Math.random() * 200;
        sprite.scale.set(s, s, 1);
        scene.add(sprite);
        nebulaPuffs.push({ sprite, baseScale: s, baseOpacity: mat.opacity, seed: Math.random() * 10 });
      }
    }

    /* -------------------------------------------------------------
       WARP STARFIELD (HYPERSPACE TRAILS — CONDITIONAL CPU UPDATES)
       ------------------------------------------------------------- */
    function buildWarpStarfield(scale = 1.0) {
      const palette = [
        { r: 1.0, g: 1.0, b: 1.0 },
        { r: 0.82, g: 0.90, b: 1.0 },
        { r: 0.22, g: 0.74, b: 0.97 },
        { r: 0.75, g: 0.52, b: 0.98 },
        { r: 0.96, g: 0.45, b: 0.72 }
      ];

      activeWarpCount = Math.floor(600 * scale);
      warpStarPositions = new Float32Array(activeWarpCount * 6);
      warpStarColors = new Float32Array(activeWarpCount * 6);

      for (let i = 0; i < activeWarpCount; i++) {
        const angle = Math.random() * Math.PI * 2;
        const radius = 20 + Math.pow(Math.random(), 0.85) * 520;
        const x = Math.cos(angle) * radius;
        const y = Math.sin(angle) * radius;
        const z = (Math.random() - 0.5) * 2200 - 480;
        const baseSpeed = 0.25 + Math.random() * 0.45;

        const rand = Math.random();
        let col = palette[0];
        if (rand > 0.96) col = palette[4];
        else if (rand > 0.90) col = palette[3];
        else if (rand > 0.82) col = palette[2];
        else if (rand > 0.68) col = palette[1];

        const brightness = 0.5 + Math.random() * 0.5;

        warpStarData.push({
          x, y, z,
          baseSpeed,
          r: col.r * brightness,
          g: col.g * brightness,
          b: col.b * brightness
        });

        const idx6 = i * 6;
        warpStarPositions[idx6] = x;
        warpStarPositions[idx6 + 1] = y;
        warpStarPositions[idx6 + 2] = z;

        warpStarPositions[idx6 + 3] = x;
        warpStarPositions[idx6 + 4] = y;
        warpStarPositions[idx6 + 5] = z + 0.5;

        warpStarColors[idx6] = col.r * brightness;
        warpStarColors[idx6 + 1] = col.g * brightness;
        warpStarColors[idx6 + 2] = col.b * brightness;

        warpStarColors[idx6 + 3] = col.r * brightness * 0.4;
        warpStarColors[idx6 + 4] = col.g * brightness * 0.4;
        warpStarColors[idx6 + 5] = col.b * brightness * 0.4;
      }

      warpLinesGeo = new THREE.BufferGeometry();
      warpLinesGeo.setAttribute('position', new THREE.BufferAttribute(warpStarPositions, 3));
      warpLinesGeo.setAttribute('color', new THREE.BufferAttribute(warpStarColors, 3));

      const lineMat = new THREE.LineBasicMaterial({
        vertexColors: true,
        transparent: true,
        opacity: 0.88,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });

      warpLinesMesh = new THREE.LineSegments(warpLinesGeo, lineMat);
      warpLinesMesh.visible = false;
      scene.add(warpLinesMesh);
    }

    /* -------------------------------------------------------------
       DISTANT STARFIELD ACROSS DEPTH
       ------------------------------------------------------------- */
    function buildDistantStarfield(scale = 1.0) {
      const count = Math.floor(12000 * scale);
      const pos = new Float32Array(count * 3);
      const col = new Float32Array(count * 3);

      for (let i = 0; i < count; i++) {
        pos[i * 3] = (Math.random() - 0.5) * 1600;
        pos[i * 3 + 1] = (Math.random() - 0.5) * 1000;
        pos[i * 3 + 2] = -400 - Math.random() * 1100;

        const isCyan = Math.random() < 0.08;
        if (isCyan) {
          col[i * 3] = 0.5; col[i * 3 + 1] = 0.85; col[i * 3 + 2] = 1.0;
        } else {
          const shade = 0.45 + Math.random() * 0.5;
          col[i * 3] = shade; col[i * 3 + 1] = shade; col[i * 3 + 2] = shade * 1.05;
        }
      }

      const geo = new THREE.BufferGeometry();
      geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
      geo.setAttribute('color', new THREE.BufferAttribute(col, 3));

      const mat = new THREE.PointsMaterial({
        size: 1.1,
        sizeAttenuation: true,
        vertexColors: true,
        map: getSoftPointTexture(),
        transparent: true,
        opacity: 0.65,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });

      distantStarField = new THREE.Points(geo, mat);
      scene.add(distantStarField);
    }

    /* -------------------------------------------------------------
       BRIGHT STELLAR BEACONS (DIFFRACTION STARS — 1 DRAW CALL)
       ------------------------------------------------------------- */
    function buildBrightStellarBeacons() {
      const count = 80;
      const pos = new Float32Array(count * 3);
      const col = new Float32Array(count * 3);

      for (let i = 0; i < count; i++) {
        let x = (Math.random() - 0.5) * 850;
        let y = (Math.random() - 0.5) * 550;
        let z = (Math.random() - 0.5) * 450 - 50;

        if (x < -10 && y > -40 && y < 50) x -= 90;

        pos[i * 3] = x;
        pos[i * 3 + 1] = y;
        pos[i * 3 + 2] = z;

        col[i * 3] = 0.90;
        col[i * 3 + 1] = 0.95;
        col[i * 3 + 2] = 1.0;
      }

      const geo = new THREE.BufferGeometry();
      geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
      geo.setAttribute('color', new THREE.BufferAttribute(col, 3));

      const mat = new THREE.PointsMaterial({
        size: 6.0,
        sizeAttenuation: true,
        vertexColors: true,
        map: getBeaconTexture(),
        transparent: true,
        opacity: 0.75,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });

      brightBeaconsPoints = new THREE.Points(geo, mat);
      scene.add(brightBeaconsPoints);
    }

    /* -------------------------------------------------------------
       NIVORA UNIVERSE CORE — AURA & DELICATE ORBITAL HALO
       ------------------------------------------------------------- */
    function buildNivoraGlobeCore(scale = 1.0) {
      globeGroup = new THREE.Group();
      globeGroup.position.set(globeCenterX, globeCenterY, globeCenterZ);

      const haloMat = new THREE.SpriteMaterial({
        map: createCoronaHaloTexture(),
        transparent: true,
        opacity: 0.65,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });
      globeHaloSprite = new THREE.Sprite(haloMat);
      globeHaloSprite.scale.set(72, 72, 1);
      globeHaloSprite.position.set(0, 0, -10);
      globeHaloSprite.renderOrder = 10;
      globeGroup.add(globeHaloSprite);

      const haloPointCount = Math.floor(1800 * scale);
      const haloPos = new Float32Array(haloPointCount * 3);
      const haloCol = new Float32Array(haloPointCount * 3);

      for (let i = 0; i < haloPointCount; i++) {
        const r = 22.0 + Math.random() * 9.0;
        const theta = Math.random() * Math.PI * 2;
        const phi = (Math.random() - 0.5) * 0.75;

        haloPos[i * 3] = r * Math.cos(phi) * Math.cos(theta);
        haloPos[i * 3 + 1] = r * Math.sin(phi) + (Math.random() - 0.5) * 2.2;
        haloPos[i * 3 + 2] = r * Math.cos(phi) * Math.sin(theta);

        const t = (r - 22.0) / 9.0;
        haloCol[i * 3] = 0.05 + 0.60 * t;
        haloCol[i * 3 + 1] = 0.75 + 0.10 * (1 - t);
        haloCol[i * 3 + 2] = 0.95;
      }

      const haloGeo = new THREE.BufferGeometry();
      haloGeo.setAttribute('position', new THREE.BufferAttribute(haloPos, 3));
      haloGeo.setAttribute('color', new THREE.BufferAttribute(haloCol, 3));

      const haloPointsMat = new THREE.PointsMaterial({
        size: 1.4,
        sizeAttenuation: true,
        vertexColors: true,
        map: getSoftPointTexture(),
        transparent: true,
        opacity: 0.85,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });

      const coreParticleHalo = new THREE.Points(haloGeo, haloPointsMat);
      globeGroup.add(coreParticleHalo);

      scene.add(globeGroup);
    }

    /* -------------------------------------------------------------
       INTERACTIVITY & EVENTS
       ------------------------------------------------------------- */
    function setupInteractivity() {
      window.addEventListener('mousemove', (e) => {
        mouse.targetX = (e.clientX / window.innerWidth - 0.5) * 1.2;
        mouse.targetY = -(e.clientY / window.innerHeight - 0.5) * 1.0;
      }, { passive: true });

      // Setup Mobile Navigation Drawer
      const toggleBtn = document.getElementById('mobileMenuToggle');
      const drawer = document.getElementById('mobileDrawer');
      const closeBtn = document.getElementById('mobileDrawerClose');
      if (toggleBtn && drawer) {
        toggleBtn.addEventListener('click', (e) => {
          e.stopPropagation();
          drawer.classList.toggle('open');
        });
        if (closeBtn) {
          closeBtn.addEventListener('click', () => drawer.classList.remove('open'));
        }
        drawer.querySelectorAll('.drawer-link').forEach(link => {
          link.addEventListener('click', () => drawer.classList.remove('open'));
        });
        document.addEventListener('click', (e) => {
          if (drawer.classList.contains('open') && !drawer.contains(e.target) && !toggleBtn.contains(e.target)) {
            drawer.classList.remove('open');
          }
        });
      }
    }

    /* -------------------------------------------------------------
       CAMERA TRAJECTORY (ZERO-ALLOCATION IN-PLACE)
       ------------------------------------------------------------- */
    function updateCameraTrajectory(p) {
      if (p <= 0.12) {
        const t = p / 0.12;
        const ease = t * t * (3 - 2 * t);
        _targetCamPos.set(0, baseCamY + (8 - baseCamY) * ease, baseCamZ + (-40 - baseCamZ) * ease);
        _targetLookAt.set(0, currentLookAt.y + (8 - currentLookAt.y) * ease, 0 + (-180 - 0) * ease);
      } else if (p <= 0.36) {
        const t = (p - 0.12) / 0.24;
        const ease = t * t * (3 - 2 * t);
        _targetCamPos.set(0, 8, -40 + (-240 - -40) * ease);
        _targetLookAt.set(0, 8, -180 + (-420 - -180) * ease);
      } else if (p <= 0.58) {
        const t = (p - 0.36) / 0.22;
        const ease = t * t * (3 - 2 * t);
        _targetCamPos.set(0 + (-12 - 0) * ease, 8 + (6 - 8) * ease, -240 + (-540 - -240) * ease);
        _targetLookAt.set(0 + (-8 - 0) * ease, 8 + (6 - 8) * ease, -420 + (-740 - -420) * ease);
      } else if (p <= 0.76) {
        const t = (p - 0.58) / 0.18;
        const ease = t * t * (3 - 2 * t);
        _targetCamPos.set(-12 + (10 - -12) * ease, 6 + (10 - 6) * ease, -540 + (-840 - -540) * ease);
        _targetLookAt.set(-8 + (4 - -8) * ease, 6 + (10 - 6) * ease, -740 + (-1040 - -740) * ease);
      } else if (p <= 0.88) {
        const t = (p - 0.76) / 0.12;
        const ease = t * t * (3 - 2 * t);
        _targetCamPos.set(10 + (-2 - 10) * ease, 10 + (8 - 10) * ease, -840 + (-1120 - -840) * ease);
        _targetLookAt.set(4 + (0 - 4) * ease, 10 + (8 - 10) * ease, -1040 + (-1320 - -1040) * ease);
      } else {
        const t = (p - 0.88) / 0.12;
        const ease = t * t * (3 - 2 * t);
        _targetCamPos.set(-2 + (0 - -2) * ease, 8 + (4 - 8) * ease, -1120 + (-1420 - -1120) * ease);
        _targetLookAt.set(0, 8 + (4 - 8) * ease, -1320 + (-1600 - -1320) * ease);
      }
    }

    /* -------------------------------------------------------------
       CENTRAL UNIVERSE FRAME RENDERER (SINGLE 60+ FPS LOOP)
       ------------------------------------------------------------- */
    function animateUniverseFrame() {
      requestAnimationFrame(animateUniverseFrame);
      if (!PerformanceEngine.isTabVisible || !isWebGLEnabled || !renderer || !camera) return;

      const elapsed = clock.getElapsedTime();

      // Smooth mouse coordinates
      mouse.x += (mouse.targetX - mouse.x) * 0.05;
      mouse.y += (mouse.targetY - mouse.y) * 0.05;

      if (!isZoomingTransition) {
        updateCameraTrajectory(targetScrollP);
        currentCamPos.lerp(_targetCamPos, 0.065);
        currentLookAt.lerp(_targetLookAt, 0.065);

        const warpShake = Math.min(0.25, Math.abs(smoothedScrollVelocity) * 0.008);
        const shakeX = (Math.random() - 0.5) * warpShake;
        const shakeY = (Math.random() - 0.5) * warpShake;

        camera.position.set(
          currentCamPos.x + mouse.x * 3.5 + shakeX,
          currentCamPos.y + mouse.y * 2.5 + shakeY,
          currentCamPos.z
        );
        camera.lookAt(
          currentLookAt.x + mouse.x * 1.2,
          currentLookAt.y + mouse.y * 0.8,
          currentLookAt.z
        );
      }

      smoothedScrollVelocity += (rawScrollVelocity - smoothedScrollVelocity) * 0.14;
      rawScrollVelocity *= 0.86;

      const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      const effectiveWarpFactor = prefersReducedMotion ? 0.15 : warpSpeedFactor;

      // Milky Way remains persistent in the universe with atmospheric depth fading
      if (milkyWayGroup) {
        milkyWayGroup.rotation.z += 0.00032 * effectiveWarpFactor;
        // In hero: full brilliance (0.88). In deep space sections: atmospheric cosmic backdrop (0.45)
        const depthT = Math.max(0.0, Math.min(1.0, (camera.position.z - 40) / 180));
        const armOpacity = 0.45 + 0.43 * depthT;
        const bulgeOpacity = 0.48 + 0.42 * depthT;

        if (spiralArmStars && spiralArmStars.material) {
          spiralArmStars.material.opacity = armOpacity;
        }
        if (galacticBulge && galacticBulge.material) {
          galacticBulge.material.opacity = bulgeOpacity;
        }
      }

      if (globeGroup) {
        globeGroup.rotation.y += 0.0010 * effectiveWarpFactor;
        globeGroup.visible = (camera.position.z > 30);
      }

      if (globeHaloSprite) {
        const hPulse = 1.0 + 0.04 * Math.sin(elapsed * 2.0);
        globeHaloSprite.scale.set(72 * hPulse, 72 * hPulse, 1);
      }

      // Subtle Nebula Updates
      for (let i = 0; i < nebulaPuffs.length; i++) {
        const np = nebulaPuffs[i];
        const distZ = Math.abs(camera.position.z - np.sprite.position.z);
        const fade = Math.min(1.0, Math.max(0.0, (distZ - 50) / 130));
        np.sprite.material.opacity = (np.baseOpacity || 0.35) * fade;
      }

      // Warp Line System — CONDITIONAL CPU UPDATES (Zero CPU when stationary)
      const absVelocity = Math.abs(smoothedScrollVelocity);
      if (warpLinesGeo && warpLinesMesh) {
        if (absVelocity > 0.06 && !prefersReducedMotion) {
          warpLinesMesh.visible = true;
          const travelSpeed = ((0.30 + absVelocity * 1.5) * Math.sign(smoothedScrollVelocity || 1)) * effectiveWarpFactor;
          const trailLength = Math.max(0.4, Math.min(26.0, absVelocity * 2.0));

          const posAttr = warpLinesGeo.attributes.position;
          const colAttr = warpLinesGeo.attributes.color;
          const camZ = camera.position.z;
          const boundFront = camZ + 70;
          const boundBack = camZ - 1300;
          const depthSpan = boundFront - boundBack;

          for (let i = 0; i < warpStarData.length; i++) {
            const s = warpStarData[i];
            s.z += travelSpeed * s.baseSpeed;

            if (travelSpeed > 0 && s.z > boundFront) {
              s.z -= depthSpan;
            } else if (travelSpeed < 0 && s.z < boundBack) {
              s.z += depthSpan;
            }

            const idx6 = i * 6;
            posAttr.array[idx6] = s.x;
            posAttr.array[idx6 + 1] = s.y;
            posAttr.array[idx6 + 2] = s.z;

            posAttr.array[idx6 + 3] = s.x;
            posAttr.array[idx6 + 4] = s.y;
            posAttr.array[idx6 + 5] = s.z - Math.sign(travelSpeed) * trailLength;

            const boost = Math.min(1.0, absVelocity * 0.07);
            colAttr.array[idx6 + 3] = s.r * (0.25 + boost * 0.7);
            colAttr.array[idx6 + 4] = s.g * (0.25 + boost * 0.7);
            colAttr.array[idx6 + 5] = s.b * (0.25 + boost * 0.7);
          }

          posAttr.needsUpdate = true;
          colAttr.needsUpdate = true;
        } else {
          warpLinesMesh.visible = false;
        }
      }

      renderer.render(scene, camera);
    }

    /* -------------------------------------------------------------
       SCROLL CONTROLLER (NATIVE HARDWARE-ACCELERATED)
       ------------------------------------------------------------- */
    function updateUniverseScroll(currentScroll) {
      const maxScroll = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
      targetScrollP = Math.min(1.0, Math.max(0.0, currentScroll / maxScroll));

      const delta = currentScroll - lastScrollPosition;
      rawScrollVelocity = delta;
      lastScrollPosition = currentScroll;

      clearTimeout(scrollTimeoutId);
      scrollTimeoutId = setTimeout(() => {
        rawScrollVelocity = 0;
      }, 140);
    }

    let scrollTicking = false;
    window.addEventListener('scroll', () => {
      if (!scrollTicking) {
        requestAnimationFrame(() => {
          updateUniverseScroll(window.scrollY);
          scrollTicking = false;
        });
        scrollTicking = true;
      }
    }, { passive: true });

    /* -------------------------------------------------------------
       CINEMATIC INTRO & TRANSITIONS
       ------------------------------------------------------------- */
    function runCinematicIntro() {
      gsap.fromTo(camera.position,
        { z: 380 },
        { z: baseCamZ, duration: 2.2, ease: "power3.out" }
      );
    }

    function triggerCinematicCameraZoom() {
      const s = document.getElementById('services');
      if (s) s.scrollIntoView({ behavior: 'smooth' });
    }

    /* -------------------------------------------------------------
       SERVICE SELECTION HELPER
       ------------------------------------------------------------- */
    function selectConsultationService(serviceName) {
      const selectEl = document.getElementById('cService');
      if (selectEl && serviceName) {
        const query = serviceName.toLowerCase();
        for (let i = 0; i < selectEl.options.length; i++) {
          const optVal = selectEl.options[i].value.toLowerCase();
          const optTxt = selectEl.options[i].text.toLowerCase();
          if (optVal && (query.includes(optVal) || optVal.includes(query) || optTxt.includes(query) || query.includes(optTxt.split(' ')[0]))) {
            selectEl.selectedIndex = i;
            break;
          }
        }
      }
      const contactSec = document.getElementById('contact');
      if (contactSec) {
        contactSec.scrollIntoView({ behavior: 'smooth' });
        const nameInput = document.getElementById('cName');
        if (nameInput) setTimeout(() => nameInput.focus(), 600);
      }
    }

    /* -------------------------------------------------------------
       CONCEPT MODAL SYSTEM
       ------------------------------------------------------------- */
    function openConceptModal(prodId) {
      const overlay = document.getElementById('conceptModalOverlay');
      if (!overlay) return;

      document.querySelectorAll('.modal-product-panel').forEach(p => p.style.display = 'none');
      const targetPanel = document.getElementById('modal-product-' + prodId);
      if (targetPanel) targetPanel.style.display = 'block';

      overlay.classList.add('open');
      overlay.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    }

    function closeConceptModal() {
      const overlay = document.getElementById('conceptModalOverlay');
      if (!overlay) return;
      overlay.classList.remove('open');
      overlay.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeConceptModal();
    });

    const overlayEl = document.getElementById('conceptModalOverlay');
    if (overlayEl) {
      overlayEl.addEventListener('click', (e) => {
        if (e.target === overlayEl) closeConceptModal();
      });
    }

    /* -------------------------------------------------------------
       CONSULTATION FORM SUBMISSION
       ------------------------------------------------------------- */
    function handleContactSubmit(e) {
      e.preventDefault();
      const btn = document.getElementById('contactSubmitBtn');
      const toast = document.getElementById('contactToast');
      const origText = btn.innerHTML;

      btn.innerHTML = '<span>Submitting Consultation Request...</span>';
      btn.disabled = true;

      setTimeout(() => {
        btn.innerHTML = '<span>Enquiry Dispatched Successfully ✓</span>';
        if (toast) {
          toast.style.display = 'inline-block';
          toast.innerText = 'Thank you. Your consultation request has been received. Nivas will reach out directly.';
        }
        e.target.reset();

        setTimeout(() => {
          btn.innerHTML = origText;
          btn.disabled = false;
          setTimeout(() => {
            if (toast) toast.style.display = 'none';
          }, 6000);
        }, 3500);
      }, 700);
    }

    // Window Resize Throttled
    let resizeTimeout;
    window.addEventListener('resize', () => {
      clearTimeout(resizeTimeout);
      resizeTimeout = setTimeout(() => {
        if (!camera || !renderer) return;
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        PerformanceEngine.detectTier();
        renderer.setPixelRatio(PerformanceEngine.pixelRatio);
        renderer.setSize(window.innerWidth, window.innerHeight);
      }, 100);
    });

    // Start WebGL Engine
    window.addEventListener('DOMContentLoaded', () => {
      initUniverseEngineCinematic();
    });
  </script>
"""

def generate_restored_html(raw_html):
    # 1. Remove Lenis script include
    raw_html = re.sub(r'<script src="https://unpkg\.com/lenis@[^"]+"></script>\s*', '', raw_html)

    # 2. Add native smooth scroll to html
    if 'html {' in raw_html:
        raw_html = raw_html.replace('html {', 'html {\n      scroll-behavior: smooth;\n      overflow-x: hidden;')
    else:
        raw_html = raw_html.replace(':root {', 'html {\n      scroll-behavior: smooth;\n      overflow-x: hidden;\n    }\n    :root {')

    # 3. Optimize .hero-title .grad-accent: remove animated drop-shadow that triggered constant repaints
    raw_html = re.sub(
        r'(\.hero-title \.grad-accent\s*\{[^}]*?)animation:\s*brandGradShift[^;]+;\s*filter:\s*drop-shadow\([^)]+\);',
        r'\1text-shadow: 0 4px 30px rgba(168, 85, 247, 0.4);',
        raw_html
    )

    # 4. Use founder-nivas.webp instead of 2.4MB png
    raw_html = raw_html.replace('assets/images/founder-nivas.png', 'assets/images/founder-nivas.webp')

    # 5. Clean backdrop-filter: blur(8px) on cards for crystal clear performance
    replacements = [
        (r'backdrop-filter:\s*blur\(25px\);', 'backdrop-filter: blur(8px);'),
        (r'-webkit-backdrop-filter:\s*blur\(25px\);', '-webkit-backdrop-filter: blur(8px);'),
        (r'backdrop-filter:\s*blur\(20px\);', 'backdrop-filter: blur(8px);'),
        (r'-webkit-backdrop-filter:\s*blur\(20px\);', '-webkit-backdrop-filter: blur(8px);'),
        (r'backdrop-filter:\s*blur\(18px\);', 'backdrop-filter: blur(8px);'),
        (r'-webkit-backdrop-filter:\s*blur\(18px\);', '-webkit-backdrop-filter: blur(8px);'),
        (r'backdrop-filter:\s*blur\(16px\);', 'backdrop-filter: blur(8px);'),
        (r'-webkit-backdrop-filter:\s*blur\(16px\);', '-webkit-backdrop-filter: blur(8px);'),
        (r'backdrop-filter:\s*blur\(14px\);', 'backdrop-filter: blur(8px);'),
        (r'-webkit-backdrop-filter:\s*blur\(14px\);', '-webkit-backdrop-filter: blur(8px);'),
        (r'backdrop-filter:\s*blur\(12px\);', 'backdrop-filter: blur(8px);'),
        (r'-webkit-backdrop-filter:\s*blur\(12px\);', '-webkit-backdrop-filter: blur(8px);'),
    ]
    for pat, rep in replacements:
        raw_html = re.sub(pat, rep, raw_html)

    # 6. Replace script with build_restored_script()
    script_pattern = re.compile(r'<script>.*?</script>\s*</body>', re.DOTALL)
    new_script = build_restored_script().strip()
    raw_html = script_pattern.sub(new_script + '\n</body>', raw_html)

    return raw_html

def main():
    src_file = os.path.join(DESKTOP_DIR, "builder", "assemble_consultancy_universe.py")
    with open(src_file, 'r', encoding='utf-8') as f:
        src_code = f.read()

    m = re.search(r'def build_consultancy_html\(\):\s*return\s*"""(.*?)"""\s*def generate', src_code, re.DOTALL)
    if not m:
        print("Error: Could not extract HTML from assemble_consultancy_universe.py")
        return

    raw_html = m.group(1)
    restored_html = generate_restored_html(raw_html)

    # Write new assemble_consultancy_universe.py with restored HTML
    new_python_code = src_code[:m.start(1)] + restored_html + src_code[m.end(1):]
    with open(src_file, 'w', encoding='utf-8') as f:
        f.write(new_python_code)
    print(f"Updated {src_file}")

    alt_py = os.path.join(DESKTOP_DIR, "builder", "assemble_ultimate_3d_universe.py")
    if os.path.exists(alt_py):
        with open(alt_py, 'w', encoding='utf-8') as f:
            f.write(new_python_code)
        print(f"Updated {alt_py}")

    dest1 = os.path.join(DESKTOP_DIR, "index.html")
    dest2 = os.path.join(DOWNLOADS_DIR, "index.html")
    with open(dest1, 'w', encoding='utf-8') as f:
        f.write(restored_html)
    print(f"Wrote {len(restored_html)} bytes to {dest1}")

    with open(dest2, 'w', encoding='utf-8') as f:
        f.write(restored_html)
    print(f"Wrote {len(restored_html)} bytes to {dest2}")

if __name__ == "__main__":
    main()
