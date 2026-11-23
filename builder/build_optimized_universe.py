#!/usr/bin/env python3
"""
NIVORA — Performance-First Optimization Assembler
Upgrades the WebGL Universe engine into a high-performance, single-rAF,
adaptive architecture with reduced particle count, zero allocations in loop,
DPR capping, optimized CSS blur filters, and IntersectionObserver-driven rendering.
"""

import os
import re

DESKTOP_DIR = "/Users/bennabathulanivas/Desktop/my projects/NIVORA"
DOWNLOADS_DIR = "/Users/bennabathulanivas/Downloads/NIVORA"

def build_optimized_script():
    return """  <script>
    /* -------------------------------------------------------------
       1. CENTRALIZED ANIMATION MANAGER & ADAPTIVE PERFORMANCE
       ------------------------------------------------------------- */
    const PerformanceEngine = {
      fps: 60,
      frameCount: 0,
      lastFpsTimestamp: performance.now(),
      mode: 'HIGH', // HIGH | MEDIUM | LOW
      isTabVisible: true,
      subscribers: [],
      pixelRatio: 1.0,
      
      init() {
        this.detectInitialTier();
        document.addEventListener('visibilitychange', () => {
          this.isTabVisible = (document.visibilityState === 'visible');
          if (this.isTabVisible) {
            this.lastFpsTimestamp = performance.now();
            if (clock) clock.getDelta();
          }
        });
        
        requestAnimationFrame((t) => this.tick(t));
      },

      detectInitialTier() {
        const isMobile = (window.innerWidth < 768) || ('ontouchstart' in window);
        const cores = navigator.hardwareConcurrency || 4;
        const mem = navigator.deviceMemory || 4;
        
        if (isMobile || cores <= 4 || mem < 4) {
          this.mode = isMobile ? 'LOW' : 'MEDIUM';
        } else {
          this.mode = 'HIGH';
        }

        // Cap DPR: 1.0 for mobile/low, max 1.5 for desktop
        const rawDpr = window.devicePixelRatio || 1;
        this.pixelRatio = (this.mode === 'LOW') ? 1.0 : Math.min(rawDpr, (this.mode === 'MEDIUM' ? 1.25 : 1.5));
      },

      subscribe(fn) {
        this.subscribers.push(fn);
      },

      tick(timestamp) {
        requestAnimationFrame((t) => this.tick(t));
        if (!this.isTabVisible) return;

        // Rolling FPS Calculation every 3.0s
        this.frameCount++;
        const elapsed = timestamp - this.lastFpsTimestamp;
        if (elapsed >= 3000) {
          this.fps = (this.frameCount * 1000) / elapsed;
          this.frameCount = 0;
          this.lastFpsTimestamp = timestamp;
          this.evaluateAdaptiveQuality();
        }

        // 1. Central Lenis Tick
        if (lenis) {
          lenis.raf(timestamp);
        }

        // 2. Central Universe & Animation Ticks
        for (let i = 0; i < this.subscribers.length; i++) {
          this.subscribers[i](timestamp);
        }
      },

      evaluateAdaptiveQuality() {
        if (this.fps < 36 && this.mode !== 'LOW') {
          this.mode = 'LOW';
          this.applyQualityTier();
        } else if (this.fps < 48 && this.mode === 'HIGH') {
          this.mode = 'MEDIUM';
          this.applyQualityTier();
        }
      },

      applyQualityTier() {
        if (!renderer) return;
        const targetDpr = (this.mode === 'LOW') ? 1.0 : (this.mode === 'MEDIUM' ? 1.25 : 1.5);
        if (this.pixelRatio !== targetDpr) {
          this.pixelRatio = targetDpr;
          renderer.setPixelRatio(this.pixelRatio);
        }
      }
    };

    /* -------------------------------------------------------------
       2. LENIS SMOOTH SCROLLING (SINGLE LOOP INTEGRATED)
       ------------------------------------------------------------- */
    let lenis = null;
    try {
      if (typeof Lenis !== 'undefined') {
        lenis = new Lenis({
          duration: 1.15,
          easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
          smoothWheel: true,
          touchMultiplier: 1.4,
          infinite: false
        });
      }
    } catch (err) {
      console.warn("Lenis init notice:", err);
    }

    // Dynamic Year
    const yrEl = document.getElementById('currentYear');
    if (yrEl) yrEl.innerText = new Date().getFullYear();

    /* -------------------------------------------------------------
       3. THREE.JS OPTIMIZED 3D UNIVERSE ENGINE
       ------------------------------------------------------------- */
    const canvas = document.getElementById('webglUniverseCanvas');
    let renderer, scene, camera;
    let milkyWayGroup, galacticBulge, spiralArmStars;
    let distantStarField, brightBeaconsPoints, distantGalaxiesGroup;
    let globeGroup, globeHaloSprite;
    let nebulaPuffs = [];

    // Hyperspace Warp System (Ultra-Lightweight)
    let warpLinesMesh, warpLinesGeo;
    let activeWarpCount = 400;
    let warpStarPositions, warpStarColors, warpStarData = [];
    let rawScrollVelocity = 0;
    let smoothedScrollVelocity = 0;
    let lastScrollPosition = 0;
    let isUserScrolling = false;
    let scrollTimeoutId = null;

    let isZoomingTransition = false;
    let warpSpeedFactor = 1.0;
    let isWebGLEnabled = false;
    let isHeroInView = true;

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
      c.width = 32; c.height = 32;
      const ctx = c.getContext('2d');
      const grad = ctx.createRadialGradient(16, 16, 0, 16, 16, 16);
      grad.addColorStop(0, 'rgba(255, 255, 255, 1)');
      grad.addColorStop(0.25, 'rgba(235, 245, 255, 0.85)');
      grad.addColorStop(0.65, 'rgba(160, 210, 255, 0.25)');
      grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, 32, 32);
      _cachedSoftPointTexture = new THREE.CanvasTexture(c);
      return _cachedSoftPointTexture;
    }

    function getBeaconTexture() {
      if (_cachedBeaconTexture) return _cachedBeaconTexture;
      const c = document.createElement('canvas');
      c.width = 64; c.height = 64;
      const ctx = c.getContext('2d');
      const cx = 32, cy = 32;
      const grad = ctx.createRadialGradient(cx, cy, 0, cx, cy, 28);
      grad.addColorStop(0, 'rgba(255, 255, 255, 1)');
      grad.addColorStop(0.18, 'rgba(186, 230, 253, 0.9)');
      grad.addColorStop(0.5, 'rgba(56, 189, 248, 0.25)');
      grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, 64, 64);
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
          antialias: (PerformanceEngine.mode === 'HIGH'),
          alpha: true,
          powerPreference: 'high-performance'
        });

        renderer.setPixelRatio(PerformanceEngine.pixelRatio);
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setClearColor(0x02040a, 0);
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 1.2;

        scene = new THREE.Scene();
        camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 3500);
        camera.position.set(baseCamX, baseCamY, baseCamZ);
        camera.lookAt(0, 18, 0);

        // Adaptive Starfield Counts
        buildDistantStarfield();
        buildWarpStarfield();
        buildProceduralMilkyWay();
        buildGalacticBulge();
        buildSubtleCosmicNebula();
        buildBrightStellarBeacons();
        buildNivoraGlobeCore();

        setupInteractivity();
        setupVisibilityObservers();

        isWebGLEnabled = true;
        PerformanceEngine.subscribe(animateUniverseFrame);
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
       PROCEDURAL MILKY WAY SPIRAL ARMS (OPTIMIZED DENSITY)
       ------------------------------------------------------------- */
    function buildProceduralMilkyWay() {
      milkyWayGroup = new THREE.Group();
      milkyWayGroup.position.set(globeCenterX, globeCenterY, globeCenterZ);
      milkyWayGroup.rotation.set(0.82, 0.22, -0.15);

      // Desktop High: ~3,400 | Medium: ~2,200 | Mobile: ~1,100 | Low: ~600
      let starCount = 3400;
      if (PerformanceEngine.mode === 'LOW') starCount = 600;
      else if (PerformanceEngine.mode === 'MEDIUM') starCount = 2200;
      else if (window.innerWidth < 768) starCount = 1100;

      const positions = new Float32Array(starCount * 3);
      const colors = new Float32Array(starCount * 3);

      const armAngles = [0.45, 0.45 + Math.PI, 1.85, 1.85 + Math.PI];
      const armWeights = [0.38, 0.38, 0.12, 0.12];
      const rMin = 22;
      const rMax = 255;

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
        size: 1.6,
        sizeAttenuation: true,
        vertexColors: true,
        map: getSoftPointTexture(),
        transparent: true,
        opacity: 0.85,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });

      spiralArmStars = new THREE.Points(armGeo, armMat);
      milkyWayGroup.add(spiralArmStars);
      scene.add(milkyWayGroup);
    }

    /* -------------------------------------------------------------
       GALACTIC BULGE PARTICLES (OPTIMIZED)
       ------------------------------------------------------------- */
    function buildGalacticBulge() {
      let bulgeCount = 600;
      if (PerformanceEngine.mode === 'LOW') bulgeCount = 90;
      else if (PerformanceEngine.mode === 'MEDIUM') bulgeCount = 350;
      else if (window.innerWidth < 768) bulgeCount = 180;

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
        size: 1.8,
        sizeAttenuation: true,
        vertexColors: true,
        map: getSoftPointTexture(),
        transparent: true,
        opacity: 0.88,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });

      galacticBulge = new THREE.Points(bulgeGeo, bulgeMat);
      milkyWayGroup.add(galacticBulge);
    }

    /* -------------------------------------------------------------
       COSMIC NEBULA PUFFS (REDUCED TO 8 BACKGROUND ACCENTS)
       ------------------------------------------------------------- */
    function buildSubtleCosmicNebula() {
      const puffs = [
        { color1: 'rgba(168, 85, 247, 0.24)', color2: 'rgba(59, 130, 246, 0.10)', scale: 300 },
        { color1: 'rgba(6, 182, 212, 0.20)', color2: 'rgba(147, 51, 234, 0.08)', scale: 340 },
        { color1: 'rgba(236, 72, 153, 0.16)', color2: 'rgba(30, 58, 138, 0.10)', scale: 260 },
        { color1: 'rgba(99, 102, 241, 0.18)', color2: 'rgba(6, 182, 212, 0.08)', scale: 300 }
      ];

      const count = (PerformanceEngine.mode === 'LOW') ? 4 : 8;
      for (let i = 0; i < count; i++) {
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

        const r = 35 + Math.pow(Math.random(), 1.3) * 160;
        const a = Math.random() * Math.PI * 2;
        sprite.position.set(
          globeCenterX + Math.cos(a) * r,
          globeCenterY + (Math.random() - 0.5) * 40,
          globeCenterZ + Math.sin(a) * r - 30
        );
        const s = 140 + Math.random() * 180;
        sprite.scale.set(s, s, 1);
        scene.add(sprite);
        nebulaPuffs.push({ sprite, baseScale: s, baseOpacity: mat.opacity, seed: Math.random() * 10 });
      }
    }

    /* -------------------------------------------------------------
       WARP STARFIELD (HYPERSPACE STREAKS — CONDITIONAL CPU UPDATES)
       ------------------------------------------------------------- */
    function buildWarpStarfield() {
      const palette = [
        { r: 1.0, g: 1.0, b: 1.0 },
        { r: 0.82, g: 0.90, b: 1.0 },
        { r: 0.22, g: 0.74, b: 0.97 },
        { r: 0.75, g: 0.52, b: 0.98 },
        { r: 0.96, g: 0.45, b: 0.72 }
      ];

      activeWarpCount = (PerformanceEngine.mode === 'LOW' || window.innerWidth < 768) ? 180 : 400;
      warpStarPositions = new Float32Array(activeWarpCount * 6);
      warpStarColors = new Float32Array(activeWarpCount * 6);

      for (let i = 0; i < activeWarpCount; i++) {
        const angle = Math.random() * Math.PI * 2;
        const radius = 25 + Math.pow(Math.random(), 0.85) * 480;
        const x = Math.cos(angle) * radius;
        const y = Math.sin(angle) * radius;
        const z = (Math.random() - 0.5) * 2000 - 450;
        const baseSpeed = 0.28 + Math.random() * 0.42;

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
        warpStarPositions[idx6 + 5] = z + 0.4;

        warpStarColors[idx6] = col.r * brightness;
        warpStarColors[idx6 + 1] = col.g * brightness;
        warpStarColors[idx6 + 2] = col.b * brightness;

        warpStarColors[idx6 + 3] = col.r * brightness * 0.35;
        warpStarColors[idx6 + 4] = col.g * brightness * 0.35;
        warpStarColors[idx6 + 5] = col.b * brightness * 0.35;
      }

      warpLinesGeo = new THREE.BufferGeometry();
      warpLinesGeo.setAttribute('position', new THREE.BufferAttribute(warpStarPositions, 3));
      warpLinesGeo.setAttribute('color', new THREE.BufferAttribute(warpStarColors, 3));

      const lineMat = new THREE.LineBasicMaterial({
        vertexColors: true,
        transparent: true,
        opacity: 0.85,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });

      warpLinesMesh = new THREE.LineSegments(warpLinesGeo, lineMat);
      warpLinesMesh.visible = false;
      scene.add(warpLinesMesh);
    }

    /* -------------------------------------------------------------
       DISTANT STARFIELD ACROSS DEPTH (OPTIMIZED)
       ------------------------------------------------------------- */
    function buildDistantStarfield() {
      let count = 1200;
      if (PerformanceEngine.mode === 'LOW') count = 250;
      else if (PerformanceEngine.mode === 'MEDIUM') count = 700;
      else if (window.innerWidth < 768) count = 350;

      const pos = new Float32Array(count * 3);
      const col = new Float32Array(count * 3);

      for (let i = 0; i < count; i++) {
        pos[i * 3] = (Math.random() - 0.5) * 1500;
        pos[i * 3 + 1] = (Math.random() - 0.5) * 950;
        pos[i * 3 + 2] = -380 - Math.random() * 1100;

        const isCyan = Math.random() < 0.10;
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
        size: 1.2,
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
       BRIGHT STELLAR BEACONS (SINGLE POINTS SYSTEM — 1 DRAW CALL)
       ------------------------------------------------------------- */
    function buildBrightStellarBeacons() {
      const beaconCount = (PerformanceEngine.mode === 'LOW') ? 25 : 60;
      const pos = new Float32Array(beaconCount * 3);
      const col = new Float32Array(beaconCount * 3);

      for (let i = 0; i < beaconCount; i++) {
        let x = (Math.random() - 0.5) * 800;
        let y = (Math.random() - 0.5) * 520;
        let z = (Math.random() - 0.5) * 420 - 40;

        if (x < -10 && y > -40 && y < 50) x -= 80;

        pos[i * 3] = x;
        pos[i * 3 + 1] = y;
        pos[i * 3 + 2] = z;

        col[i * 3] = 0.85 + Math.random() * 0.15;
        col[i * 3 + 1] = 0.92 + Math.random() * 0.08;
        col[i * 3 + 2] = 1.0;
      }

      const geo = new THREE.BufferGeometry();
      geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
      geo.setAttribute('color', new THREE.BufferAttribute(col, 3));

      const mat = new THREE.PointsMaterial({
        size: 5.5,
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
    function buildNivoraGlobeCore() {
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
      globeHaloSprite.scale.set(70, 70, 1);
      globeHaloSprite.position.set(0, 0, -10);
      globeGroup.add(globeHaloSprite);

      const haloPointCount = (PerformanceEngine.mode === 'LOW') ? 120 : 350;
      const haloPos = new Float32Array(haloPointCount * 3);
      const haloCol = new Float32Array(haloPointCount * 3);

      for (let i = 0; i < haloPointCount; i++) {
        const r = 22.0 + Math.random() * 8.0;
        const theta = Math.random() * Math.PI * 2;
        const phi = (Math.random() - 0.5) * 0.70;

        haloPos[i * 3] = r * Math.cos(phi) * Math.cos(theta);
        haloPos[i * 3 + 1] = r * Math.sin(phi) + (Math.random() - 0.5) * 2.0;
        haloPos[i * 3 + 2] = r * Math.cos(phi) * Math.sin(theta);

        const t = (r - 22.0) / 8.0;
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
       SECTION VISIBILITY OBSERVERS (STOP ANIMATING OFF-SCREEN)
       ------------------------------------------------------------- */
    function setupVisibilityObservers() {
      const heroEl = document.getElementById('hero');
      if (heroEl && 'IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
          entries.forEach(entry => {
            isHeroInView = entry.isIntersecting;
            if (milkyWayGroup) {
              milkyWayGroup.visible = isHeroInView;
            }
            if (globeGroup) {
              globeGroup.visible = isHeroInView && (camera.position.z > 30);
            }
          });
        }, { threshold: 0.05 });
        observer.observe(heroEl);
      }
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
       CENTRAL UNIVERSE FRAME RENDERER (COORDINATED VIA MANAGER)
       ------------------------------------------------------------- */
    function animateUniverseFrame(timestamp) {
      if (!isWebGLEnabled || !renderer || !camera) return;

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

      // Only animate Milky Way when hero section is in view
      if (isHeroInView) {
        if (milkyWayGroup) {
          milkyWayGroup.rotation.z += 0.00030 * effectiveWarpFactor;
          const mwFade = Math.max(0.0, Math.min(1.0, (camera.position.z - 40) / 140));
          if (spiralArmStars && spiralArmStars.material) {
            spiralArmStars.material.opacity = 0.85 * mwFade;
            spiralArmStars.visible = mwFade > 0.01;
          }
          if (galacticBulge && galacticBulge.material) {
            galacticBulge.material.opacity = 0.88 * mwFade;
            galacticBulge.visible = mwFade > 0.01;
          }
        }

        if (globeGroup) {
          globeGroup.rotation.y += 0.0010 * effectiveWarpFactor;
          globeGroup.visible = (camera.position.z > 30);
        }

        if (globeHaloSprite) {
          const hPulse = 1.0 + 0.04 * Math.sin(elapsed * 2.0);
          globeHaloSprite.scale.set(70 * hPulse, 70 * hPulse, 1);
        }
      }

      // Subtle Nebula Updates (only 8 sprites, pulse throttled)
      for (let i = 0; i < nebulaPuffs.length; i++) {
        const np = nebulaPuffs[i];
        const distZ = Math.abs(camera.position.z - np.sprite.position.z);
        const fade = Math.min(1.0, Math.max(0.0, (distZ - 60) / 140));
        np.sprite.material.opacity = (np.baseOpacity || 0.35) * fade;
        np.sprite.visible = fade > 0.02;
      }

      // Warp Line System — CONDITIONAL CPU BUFFER MUTATIONS (Idle = ZERO CPU WORK)
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
       SCROLL CONTROLLER
       ------------------------------------------------------------- */
    function updateUniverseScroll(currentScroll) {
      const maxScroll = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
      targetScrollP = Math.min(1.0, Math.max(0.0, currentScroll / maxScroll));

      const delta = currentScroll - lastScrollPosition;
      rawScrollVelocity = delta;
      lastScrollPosition = currentScroll;
      isUserScrolling = true;

      clearTimeout(scrollTimeoutId);
      scrollTimeoutId = setTimeout(() => {
        isUserScrolling = false;
        rawScrollVelocity = 0;
      }, 140);
    }

    if (lenis) {
      lenis.on('scroll', (e) => {
        updateUniverseScroll(e.scroll);
      });
    } else {
      let ticking = false;
      window.addEventListener('scroll', () => {
        if (!ticking) {
          requestAnimationFrame(() => {
            updateUniverseScroll(window.scrollY);
            ticking = false;
          });
          ticking = true;
        }
      }, { passive: true });
    }

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
      if (lenis) {
        lenis.scrollTo('#services', { duration: 1.6 });
      } else {
        const s = document.getElementById('services');
        if (s) s.scrollIntoView({ behavior: 'smooth' });
      }
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
        if (lenis) {
          lenis.scrollTo(contactSec, { duration: 1.2 });
        } else {
          contactSec.scrollIntoView({ behavior: 'smooth' });
        }
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
      if (lenis) lenis.stop();
    }

    function closeConceptModal() {
      const overlay = document.getElementById('conceptModalOverlay');
      if (!overlay) return;
      overlay.classList.remove('open');
      overlay.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
      if (lenis) lenis.start();
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
        PerformanceEngine.detectInitialTier();
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

def optimize_html_content(html):
    # 1. Optimize CSS backdrop-filters and blur filters
    # Replace .hero-logo-glow-disc blur(30px)
    html = re.sub(
        r'(\.hero-logo-glow-disc\s*\{[^}]*?)filter:\s*blur\(30px\);',
        r'\1/* filter blur removed for 60fps performance */',
        html
    )

    # Replace heavy backdrop-filter: blur(14px - 25px) on cards with smooth blur(6px - 8px)
    replacements = [
        (r'backdrop-filter:\s*blur\(25px\);', 'backdrop-filter: blur(8px);'),
        (r'-webkit-backdrop-filter:\s*blur\(25px\);', '-webkit-backdrop-filter: blur(8px);'),
        (r'backdrop-filter:\s*blur\(20px\);', 'backdrop-filter: blur(8px);'),
        (r'-webkit-backdrop-filter:\s*blur\(20px\);', '-webkit-backdrop-filter: blur(8px);'),
        (r'backdrop-filter:\s*blur\(18px\);', 'backdrop-filter: blur(8px);'),
        (r'-webkit-backdrop-filter:\s*blur\(18px\);', '-webkit-backdrop-filter: blur(8px);'),
        (r'backdrop-filter:\s*blur\(16px\);', 'backdrop-filter: blur(6px);'),
        (r'-webkit-backdrop-filter:\s*blur\(16px\);', '-webkit-backdrop-filter: blur(6px);'),
        (r'backdrop-filter:\s*blur\(14px\);', 'backdrop-filter: blur(6px);'),
        (r'-webkit-backdrop-filter:\s*blur\(14px\);', '-webkit-backdrop-filter: blur(6px);'),
        (r'backdrop-filter:\s*blur\(12px\);', 'backdrop-filter: blur(6px);'),
        (r'-webkit-backdrop-filter:\s*blur\(12px\);', '-webkit-backdrop-filter: blur(6px);'),
    ]

    for pat, rep in replacements:
        html = re.sub(pat, rep, html)

    # 2. Add loading="lazy" and prevent layout shifts to any remaining below-the-fold images
    html = html.replace('class="founder-portrait">', 'class="founder-portrait" loading="lazy" width="180" height="180">')
    html = html.replace('class="folivio-main-logo">', 'class="folivio-main-logo" loading="lazy" width="76" height="76">')

    # 3. Replace the entire script block with the optimized single-rAF engine
    script_pattern = re.compile(r'<script>\s*/\*\s*--+\s*1\.\s*GLOBAL STATE.*?</script>', re.DOTALL)
    new_script = build_optimized_script().strip()
    html, count = script_pattern.subn(new_script, html)
    if count == 0:
        print("Warning: script_pattern replacement count was 0. Trying alternate script replacement...")
        # Alternate fallback: replace from `<script>` to `</body>`
        alt_pattern = re.compile(r'<script>.*?</script>\s*</body>', re.DOTALL)
        html = alt_pattern.sub(new_script + '\n</body>', html)

    return html

def main():
    src_file = os.path.join(DESKTOP_DIR, "builder", "assemble_consultancy_universe.py")
    with open(src_file, 'r', encoding='utf-8') as f:
        src_code = f.read()

    # Extract the HTML template from build_consultancy_html()
    # Find start and end of HTML string
    m = re.search(r'def build_consultancy_html\(\):\s*return\s*"""(.*?)"""\s*def generate', src_code, re.DOTALL)
    if not m:
        print("Error: Could not extract HTML from assemble_consultancy_universe.py")
        return

    raw_html = m.group(1)
    optimized_html = optimize_html_content(raw_html)

    # Write new assemble_consultancy_universe.py with optimized HTML
    new_python_code = src_code[:m.start(1)] + optimized_html + src_code[m.end(1):]
    with open(src_file, 'w', encoding='utf-8') as f:
        f.write(new_python_code)
    print(f"Updated {src_file}")

    # Also update assemble_ultimate_3d_universe.py
    alt_py = os.path.join(DESKTOP_DIR, "builder", "assemble_ultimate_3d_universe.py")
    if os.path.exists(alt_py):
        with open(alt_py, 'w', encoding='utf-8') as f:
            f.write(new_python_code)
        print(f"Updated {alt_py}")

    # Output directly to Desktop and Downloads index.html
    dest1 = os.path.join(DESKTOP_DIR, "index.html")
    dest2 = os.path.join(DOWNLOADS_DIR, "index.html")
    with open(dest1, 'w', encoding='utf-8') as f:
        f.write(optimized_html)
    print(f"Wrote {len(optimized_html)} bytes to {dest1}")

    with open(dest2, 'w', encoding='utf-8') as f:
        f.write(optimized_html)
    print(f"Wrote {len(optimized_html)} bytes to {dest2}")

if __name__ == "__main__":
    main()
