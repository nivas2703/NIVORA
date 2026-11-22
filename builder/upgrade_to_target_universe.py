#!/usr/bin/env python3
"""
upgrade_to_target_universe.py
Transforms the 3D WebGL engine and hero UI to achieve 100% visual parity
with the uploaded cinematic reference image:
1. Cyber Earth Holographic Core with detailed continent outlines, dense glowing cyan matrix dots,
   latitude/longitude meridians, neural hubs.
2. Outer glass sphere with electric-cyan / magenta Fresnel rim lighting.
3. Official 3D NIVORA Logo Ribbon suspended at center with inner cyan/magenta glowing aura.
4. Vertical light projection beam connecting bottom pole of globe down to the vortex center.
5. Majestic horizontal swirling vortex accretion disc with 5 concentric luminous bands and 4,500 logarithmic spiral particles.
6. 4 Tilted glowing orbital rings with luminous pearl satellites.
7. Bottom-left massive curved blue planet with electric-cyan atmospheric limb glow.
8. Bottom-right celestial planet with warm magenta/purple crescent rim.
9. Top-right tilted spiral galaxy with bright core and sweeping dust arms.
10. Hero UI with exact matching typography, gradients, badges, CTAs, and SVG metrics icons.
"""

import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
MASTER_BUILDER = os.path.join(SCRIPT_DIR, "assemble_ultimate_3d_universe.py")

with open(MASTER_BUILDER, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update Backdrop CSS
backdrop_target = r"""    /* PURE DEEP SPACE AMBIENCE — 100% PROCEDURAL (ZERO STATIC IMAGES) */
    .cosmic-ambient-backdrop {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 0;
      pointer-events: none;
      background: radial-gradient(circle at 70% 48%, rgba(15, 12, 40, 0.5) 0%, rgba(5, 7, 20, 0.8) 45%, #02040a 100%);
      overflow: hidden;
    }"""

backdrop_replacement = r"""    /* PURE DEEP SPACE AMBIENCE — 100% PROCEDURAL (ZERO STATIC IMAGES) */
    .cosmic-ambient-backdrop {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 0;
      pointer-events: none;
      background: radial-gradient(circle at 68% 45%, rgba(18, 10, 48, 0.6) 0%, rgba(4, 7, 24, 0.88) 45%, #02040b 100%);
      overflow: hidden;
    }"""

if backdrop_target in code:
    code = code.replace(backdrop_target, backdrop_replacement)
    print("Replaced backdrop CSS")
else:
    print("Backdrop CSS target not found")

# 2. Update Hero Badge, Title, Tagline, CTAs & Metrics in HTML
hero_html_target = r"""          <div class="hero-badge">
            <span class="dot"></span>
            <span>// A NIVAS BENNABATTHULA INITIATIVE</span>
          </div>

          <h1 class="hero-title">
            <span class="hero-welcome">Welcome to</span><br>
            <span class="hero-brand">NIVORA.</span>
          </h1>

          <div class="hero-tagline">
            Turning <em class="editorial-accent">Ideas</em> Into Intelligent <em class="editorial-accent">Products</em>.
          </div>

          <p class="hero-copy">
            NIVORA is the <strong>technology and innovation universe built by Nivas Bennabatthula</strong> &mdash; where ambitious ideas become intelligent products, meaningful experiences and new digital possibilities.
          </p>

          <div class="hero-actions">
            <button type="button" class="btn-enter-universe" onclick="triggerCinematicCameraZoom()">
              <span>Enter the Universe &rarr;</span>
            </button>
            <a class="btn-explore-products" href="#products">
              <span class="play-icon-circle">&#9658;</span>
              <span>Explore Products</span>
            </a>
          </div>

          <!-- Hero Metrics with Elegant Icons -->
          <div class="hero-metrics">
            <div class="metric-card">
              <div class="metric-icon-wrap m-purple">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
              </div>
              <div class="metric-info">
                <strong>4</strong>
                <span>Ecosystem Worlds</span>
              </div>
            </div>

            <div class="metric-card">
              <div class="metric-icon-wrap m-cyan">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
              </div>
              <div class="metric-info">
                <strong>1</strong>
                <span>Founder &amp; Builder</span>
              </div>
            </div>

            <div class="metric-card">
              <div class="metric-icon-wrap m-magenta">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
              </div>
              <div class="metric-info">
                <strong>&infin;</strong>
                <span>Digital Possibilities</span>
              </div>
            </div>
          </div>"""

hero_html_replacement = r"""          <div class="hero-badge">
            <span class="dot"></span>
            <span>A NIVAS BENNABATTHULA INITIATIVE</span>
          </div>

          <h1 class="hero-title">
            <span class="hero-welcome">Welcome to</span><br>
            <span class="hero-brand">NIVORA.</span>
          </h1>

          <div class="hero-tagline">
            Turning <em class="editorial-accent accent-ideas">Ideas</em> Into Intelligent <em class="editorial-accent accent-products">Products</em>.
          </div>

          <p class="hero-copy">
            NIVORA is the <strong>technology and innovation universe</strong> built by <strong>Nivas Bennabatthula</strong> &mdash; where ambitious ideas become intelligent products, meaningful experiences and new digital possibilities.
          </p>

          <div class="hero-actions">
            <button type="button" class="btn-enter-universe" onclick="triggerCinematicCameraZoom()">
              <span>Enter the Universe &rarr;</span>
            </button>
            <a class="btn-explore-products" href="#products">
              <span class="play-icon-circle">&#9658;</span>
              <span>Explore Products</span>
            </a>
          </div>

          <!-- Hero Metrics with Matching Target Icons -->
          <div class="hero-metrics">
            <div class="metric-card">
              <div class="metric-icon-wrap m-purple">
                <!-- Atom / Orbital Worlds Icon -->
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                  <ellipse cx="12" cy="12" rx="10" ry="4.5" transform="rotate(30 12 12)"></ellipse>
                  <ellipse cx="12" cy="12" rx="10" ry="4.5" transform="rotate(-30 12 12)"></ellipse>
                  <circle cx="12" cy="12" r="2.2" fill="currentColor"></circle>
                </svg>
              </div>
              <div class="metric-info">
                <strong>4</strong>
                <span>Ecosystem Worlds</span>
              </div>
            </div>

            <div class="metric-card">
              <div class="metric-icon-wrap m-cyan">
                <!-- 3D Stacked Layers Icon -->
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                  <polygon points="12 2 2 7 12 12 22 7 12 2"></polygon>
                  <polyline points="2 12 12 17 22 12"></polyline>
                  <polyline points="2 17 12 22 22 17"></polyline>
                </svg>
              </div>
              <div class="metric-info">
                <strong>1</strong>
                <span>Founder &amp; Builder</span>
              </div>
            </div>

            <div class="metric-card">
              <div class="metric-icon-wrap m-magenta">
                <!-- Infinity Possibilities Icon -->
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M18.178 8c5.096 0 5.096 8 0 8-3.084 0-4.321-2.91-6.178-5.334C10.143 8.244 8.906 8 5.822 8 0.726 8 0.726 16 5.822 16c3.084 0 4.321-2.91 6.178-5.334C13.857 13.09 15.094 16 18.178 16z"></path>
                </svg>
              </div>
              <div class="metric-info">
                <strong>&infin; &infin;</strong>
                <span>Digital Possibilities</span>
              </div>
            </div>
          </div>"""

if hero_html_target in code:
    code = code.replace(hero_html_target, hero_html_replacement)
    print("Replaced Hero HTML")
else:
    print("Hero HTML target not found")

# 3. Update CSS for accent-ideas and accent-products
css_target = r"""    .editorial-accent::after {
      content: '';
      position: absolute;
      left: 0.05em;
      right: 0.05em;
      bottom: -2px;
      height: 2px;
      background: linear-gradient(90deg, #ec4899, #a855f7, #06b6d4);
      border-radius: 9999px;
      box-shadow: 0 0 10px rgba(236, 72, 153, 0.8);
    }"""

css_replacement = r"""    .editorial-accent::after {
      content: '';
      position: absolute;
      left: 0.05em;
      right: 0.05em;
      bottom: -2px;
      height: 2px;
      border-radius: 9999px;
    }
    .accent-ideas::after {
      background: #a855f7;
      box-shadow: 0 0 10px rgba(168, 85, 247, 0.9);
    }
    .accent-products::after {
      background: #ec4899;
      box-shadow: 0 0 10px rgba(236, 72, 153, 0.9);
    }"""

if css_target in code:
    code = code.replace(css_target, css_replacement)
    print("Replaced editorial accent CSS")
else:
    print("Editorial accent CSS not found")

# 4. Now upgrade the Three.js Engine:
# Variables:
threejs_vars_target = r"""    let distantStarField, brightBeaconsGroup, distantGalaxiesGroup;
    let globeGroup, globeMesh, logoSprite, atmosphereMesh;
    let orbitalRings = [], ringParticles = [];
    let accretionDisk, energyBeam;
    let nebulaPuffs = [];"""

threejs_vars_replacement = r"""    let distantStarField, brightBeaconsGroup, distantGalaxiesGroup;
    let globeGroup, globeMesh, logoSprite, atmosphereMesh, globeHaloSprite;
    let orbitalRings = [], ringParticles = [];
    let accretionGroup, accretionDisk, accretionParticles, energyBeam;
    let blPlanetMesh, blPlanetAtmos, brPlanetMesh, brPlanetAtmos, trGalaxyGroup;
    let nebulaPuffs = [];"""

if threejs_vars_target in code:
    code = code.replace(threejs_vars_target, threejs_vars_replacement)
    print("Updated Three.js variables")
else:
    print("Three.js variables target not found")

# In initUniverse3D:
init_universe_target = r"""        // Build 3D Cinematic Universe
        buildDistantStarfield();
        buildProceduralMilkyWay();
        buildGalacticBulge();
        buildSubtleCosmicNebula();
        buildBrightStellarBeacons();
        buildDistantSpiralGalaxies();
        buildNivoraGlobeCore();
        build3DProductWorlds();
        buildOrbitalRings3D();
        buildGalacticAccretionPlatform();"""

init_universe_replacement = r"""        // Build 3D Cinematic Universe
        buildDistantStarfield();
        buildProceduralMilkyWay();
        buildGalacticBulge();
        buildSubtleCosmicNebula();
        buildBrightStellarBeacons();
        buildCelestialForeAndBackground();
        buildNivoraGlobeCore();
        buildGalacticAccretionPlatform();
        buildOrbitalRings3D();
        build3DProductWorlds();"""

if init_universe_target in code:
    code = code.replace(init_universe_target, init_universe_replacement)
    print("Updated initUniverse3D call stack")
else:
    print("initUniverse3D target not found")

# Replace buildDistantSpiralGalaxies, buildNivoraGlobeCore, buildOrbitalRings3D, buildGalacticAccretionPlatform
# with the upgraded implementations
core_funcs_target = r"""    function buildDistantSpiralGalaxies() {
      distantGalaxiesGroup = new THREE.Group();

      const galaxyConfigs = [
        { x: -320, y: 160, z: -850, rotX: 0.6, rotY: 0.4, scale: 0.22, points: 420 },
        { x: 260, y: -140, z: -1000, rotX: -0.8, rotY: 0.2, scale: 0.18, points: 320 },
        { x: -90, y: -220, z: -900, rotX: 0.4, rotY: -0.5, scale: 0.15, points: 260 }
      ];

      galaxyConfigs.forEach((cfg) => {
        const gGroup = new THREE.Group();
        gGroup.position.set(cfg.x, cfg.y, cfg.z);
        gGroup.rotation.set(cfg.rotX, cfg.rotY, 0);

        const pos = new Float32Array(cfg.points * 3);
        const col = new Float32Array(cfg.points * 3);

        for (let i = 0; i < cfg.points; i++) {
          const arm = i % 2;
          const r = 5 + 75 * Math.pow(Math.random(), 1.6);
          const theta = arm * Math.PI + 2.5 * Math.log(r / 5) + (Math.random() - 0.5) * 0.35;

          pos[i * 3] = (Math.cos(theta) * r + (Math.random() - 0.5) * 4) * cfg.scale;
          pos[i * 3 + 1] = ((Math.random() - 0.5) * 4) * cfg.scale;
          pos[i * 3 + 2] = (Math.sin(theta) * r + (Math.random() - 0.5) * 4) * cfg.scale;

          col[i * 3] = 0.65;
          col[i * 3 + 1] = 0.55;
          col[i * 3 + 2] = 0.95;
        }

        const geo = new THREE.BufferGeometry();
        geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
        geo.setAttribute('color', new THREE.BufferAttribute(col, 3));
        const pts = new THREE.Points(geo, new THREE.PointsMaterial({
          size: 1.6,
          vertexColors: true,
          map: createSoftPointTexture(),
          transparent: true,
          opacity: 0.5,
          blending: THREE.AdditiveBlending,
          depthWrite: false
        }));
        gGroup.add(pts);
        distantGalaxiesGroup.add(gGroup);
      });

      scene.add(distantGalaxiesGroup);
    }

    /* -------------------------------------------------------------
       7. NIVORA DIGITAL CORE (3D GLOBE WITH OFFICIAL LOGO)
       ------------------------------------------------------------- */
    function buildNivoraGlobeCore() {
      globeGroup = new THREE.Group();
      globeGroup.position.set(globeCenterX, globeCenterY, globeCenterZ);

      const globeRadius = 24.5;
      const cyberTex = createDigitalWorldTextureClean();

      const sphereGeo = new THREE.SphereGeometry(globeRadius, 48, 48);
      const sphereMat = new THREE.MeshBasicMaterial({
        map: cyberTex,
        transparent: true,
        opacity: 0.78,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });
      globeMesh = new THREE.Mesh(sphereGeo, sphereMat);
      globeGroup.add(globeMesh);

      // Atmospheric Shell
      const atmosGeo = new THREE.SphereGeometry(globeRadius * 1.06, 36, 36);
      const atmosCanvas = document.createElement('canvas');
      atmosCanvas.width = 256; atmosCanvas.height = 256;
      const aCtx = atmosCanvas.getContext('2d');
      const aGrad = aCtx.createRadialGradient(128, 128, 80, 128, 128, 128);
      aGrad.addColorStop(0, 'rgba(6, 182, 212, 0)');
      aGrad.addColorStop(0.7, 'rgba(6, 182, 212, 0.18)');
      aGrad.addColorStop(0.9, 'rgba(168, 85, 247, 0.35)');
      aGrad.addColorStop(1, 'rgba(6, 182, 212, 0.65)');
      aCtx.fillStyle = aGrad;
      aCtx.fillRect(0, 0, 256, 256);

      const atmosTex = new THREE.CanvasTexture(atmosCanvas);
      atmosphereMesh = new THREE.Mesh(atmosGeo, new THREE.MeshBasicMaterial({
        map: atmosTex,
        transparent: true,
        opacity: 0.65,
        blending: THREE.AdditiveBlending,
        side: THREE.BackSide,
        depthWrite: false
      }));
      globeGroup.add(atmosphereMesh);

      // Official NIVORA Logo (Crisp, Suspended in Exact Center)
      const logoLoader = new THREE.TextureLoader();
      logoLoader.load('assets/images/nivora-logo.png', (tex) => {
        tex.minFilter = THREE.LinearFilter;
        tex.magFilter = THREE.LinearFilter;
        const logoMat = new THREE.SpriteMaterial({
          map: tex,
          transparent: true,
          opacity: 1.0,
          blending: THREE.NormalBlending,
          depthTest: false
        });
        logoSprite = new THREE.Sprite(logoMat);
        logoSprite.scale.set(17, 17, 1);
        logoSprite.renderOrder = 20;
        globeGroup.add(logoSprite);

        const auraMat = new THREE.SpriteMaterial({
          map: createSoftPointTexture(),
          color: 0x06b6d4,
          transparent: true,
          opacity: 0.45,
          blending: THREE.AdditiveBlending,
          depthTest: false
        });
        const auraSprite = new THREE.Sprite(auraMat);
        auraSprite.scale.set(22, 22, 1);
        auraSprite.renderOrder = 18;
        globeGroup.add(auraSprite);
      });

      scene.add(globeGroup);
    }

    /* -------------------------------------------------------------
       8. 3 ELEGANT 3D ORBITAL RINGS & PARTICLES
       ------------------------------------------------------------- */
    function buildOrbitalRings3D() {
      const ringSpecs = [
        { radiusX: 38, radiusY: 34, rotX: 1.25, rotY: 0.15, rotZ: 0.25, color: 0x06b6d4, speed: 0.002 },
        { radiusX: 44, radiusY: 38, rotX: 0.55, rotY: 1.15, rotZ: -0.50, color: 0xa855f7, speed: -0.0018 },
        { radiusX: 50, radiusY: 42, rotX: -0.75, rotY: 0.45, rotZ: 0.95, color: 0x38bdf8, speed: 0.0022 }
      ];

      ringSpecs.forEach((spec, rIdx) => {
        const curve = new THREE.EllipseCurve(0, 0, spec.radiusX, spec.radiusY, 0, 2 * Math.PI, false, 0);
        const points = curve.getPoints(100);
        const ringGeo = new THREE.BufferGeometry().setFromPoints(points);

        const ringLine = new THREE.Line(ringGeo, new THREE.LineBasicMaterial({
          color: spec.color,
          transparent: true,
          opacity: 0.42,
          blending: THREE.AdditiveBlending
        }));
        ringLine.rotation.set(spec.rotX, spec.rotY, spec.rotZ);
        globeGroup.add(ringLine);

        const particleCount = rIdx === 1 ? 2 : 1;
        for (let p = 0; p < particleCount; p++) {
          const bead = new THREE.Mesh(
            new THREE.SphereGeometry(0.9, 12, 12),
            new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.9 })
          );
          const halo = new THREE.Sprite(new THREE.SpriteMaterial({
            map: createSoftPointTexture(),
            color: spec.color,
            transparent: true,
            opacity: 0.65,
            blending: THREE.AdditiveBlending
          }));
          halo.scale.set(4.5, 4.5, 1);
          bead.add(halo);

          globeGroup.add(bead);
          ringParticles.push({
            mesh: bead,
            curve: curve,
            rotX: spec.rotX,
            rotY: spec.rotY,
            rotZ: spec.rotZ,
            progress: p * 0.5 + rIdx * 0.33,
            speed: spec.speed
          });
        }
      });
    }

    /* -------------------------------------------------------------
       9. GALACTIC ENERGY ACCRETION PLATFORM & BEAM
       ------------------------------------------------------------- */
    function buildGalacticAccretionPlatform() {
      const dPoints = 1200;
      const dPos = new Float32Array(dPoints * 3);
      const dCol = new Float32Array(dPoints * 3);

      for (let i = 0; i < dPoints; i++) {
        const radius = 8 + Math.pow(Math.random(), 1.3) * 56;
        const angle = Math.random() * Math.PI * 2;
        const spiralOffset = radius * 0.06;
        const theta = angle + spiralOffset;

        dPos[i * 3] = Math.cos(theta) * radius;
        dPos[i * 3 + 1] = (Math.random() - 0.5) * 1.8;
        dPos[i * 3 + 2] = Math.sin(theta) * radius;

        const p = radius / 64;
        if (p < 0.25) {
          dCol[i * 3] = 0.95; dCol[i * 3 + 1] = 0.98; dCol[i * 3 + 2] = 1.0;
        } else if (p < 0.6) {
          dCol[i * 3] = 0.55; dCol[i * 3 + 1] = 0.2; dCol[i * 3 + 2] = 0.85;
        } else if (p < 0.8) {
          dCol[i * 3] = 0.85; dCol[i * 3 + 1] = 0.2; dCol[i * 3 + 2] = 0.75;
        } else {
          dCol[i * 3] = 0.05; dCol[i * 3 + 1] = 0.7; dCol[i * 3 + 2] = 0.9;
        }
      }

      const dGeo = new THREE.BufferGeometry();
      dGeo.setAttribute('position', new THREE.BufferAttribute(dPos, 3));
      dGeo.setAttribute('color', new THREE.BufferAttribute(dCol, 3));
      accretionDisk = new THREE.Points(dGeo, new THREE.PointsMaterial({
        size: 2.0,
        vertexColors: true,
        map: createSoftPointTexture(),
        transparent: true,
        opacity: 0.65,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      }));
      accretionDisk.position.set(globeCenterX, globeCenterY - 35, globeCenterZ);
      accretionDisk.rotation.set(Math.PI / 2.3, 0, 0.1);
      scene.add(accretionDisk);

      const beamGeo = new THREE.CylinderGeometry(1.2, 3.2, 18, 24, 1, true);
      energyBeam = new THREE.Mesh(beamGeo, new THREE.MeshBasicMaterial({
        color: 0x06b6d4,
        transparent: true,
        opacity: 0.35,
        blending: THREE.AdditiveBlending,
        side: THREE.DoubleSide,
        depthWrite: false
      }));
      energyBeam.position.set(globeCenterX, globeCenterY - 22, globeCenterZ);
      scene.add(energyBeam);
    }"""

core_funcs_replacement = r"""    /* -------------------------------------------------------------
       7. CELESTIAL FOREGROUND & BACKGROUND (PLANETS & GALAXY)
       ------------------------------------------------------------- */
    function buildCelestialForeAndBackground() {
      // 1. Bottom-Left Curved Horizon (Massive Deep-Blue Planet)
      const blGeo = new THREE.SphereGeometry(140, 48, 48);
      const blMat = new THREE.MeshBasicMaterial({
        color: 0x06152d,
        transparent: true,
        opacity: 0.95
      });
      blPlanetMesh = new THREE.Mesh(blGeo, blMat);
      blPlanetMesh.position.set(-145, -165, 75);
      scene.add(blPlanetMesh);

      // Atmospheric Rim for Bottom-Left Planet
      const blAtmosGeo = new THREE.SphereGeometry(142, 48, 48);
      const blAtmosMat = new THREE.ShaderMaterial({
        vertexShader: `
          varying vec3 vNormal;
          void main() {
            vNormal = normalize(normalMatrix * normal);
            gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
          }
        `,
        fragmentShader: `
          varying vec3 vNormal;
          void main() {
            float fresnel = 1.0 - dot(vNormal, vec3(0.0, 0.0, 1.0));
            fresnel = pow(fresnel, 2.8);
            vec3 atmosColor = vec3(0.05, 0.75, 1.0); // Vibrant electric cyan
            gl_FragColor = vec4(atmosColor, fresnel * 0.95);
          }
        `,
        transparent: true,
        blending: THREE.AdditiveBlending,
        side: THREE.FrontSide,
        depthWrite: false
      });
      blPlanetAtmos = new THREE.Mesh(blAtmosGeo, blAtmosMat);
      blPlanetAtmos.position.set(-145, -165, 75);
      scene.add(blPlanetAtmos);

      // 2. Bottom-Right Planet with Warm Magenta/Violet Rim Light
      const brGeo = new THREE.SphereGeometry(46, 36, 36);
      const brMat = new THREE.MeshBasicMaterial({
        color: 0x160824,
        transparent: true,
        opacity: 0.92
      });
      brPlanetMesh = new THREE.Mesh(brGeo, brMat);
      brPlanetMesh.position.set(165, -125, 45);
      scene.add(brPlanetMesh);

      const brAtmosGeo = new THREE.SphereGeometry(47, 36, 36);
      const brAtmosMat = new THREE.ShaderMaterial({
        vertexShader: `
          varying vec3 vNormal;
          void main() {
            vNormal = normalize(normalMatrix * normal);
            gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
          }
        `,
        fragmentShader: `
          varying vec3 vNormal;
          void main() {
            float fresnel = 1.0 - dot(vNormal, vec3(0.0, 0.0, 1.0));
            fresnel = pow(fresnel, 2.6);
            vec3 atmosColor = vec3(0.92, 0.28, 0.94); // Magenta / purple
            gl_FragColor = vec4(atmosColor, fresnel * 0.88);
          }
        `,
        transparent: true,
        blending: THREE.AdditiveBlending,
        side: THREE.FrontSide,
        depthWrite: false
      });
      brPlanetAtmos = new THREE.Mesh(brAtmosGeo, brAtmosMat);
      brPlanetAtmos.position.set(165, -125, 45);
      scene.add(brPlanetAtmos);

      // 3. Top-Right Prominent Spiral Galaxy
      trGalaxyGroup = new THREE.Group();
      trGalaxyGroup.position.set(195, 135, -210);
      trGalaxyGroup.rotation.set(0.72, 0.42, -0.32);

      const trPoints = 1800;
      const trPos = new Float32Array(trPoints * 3);
      const trCol = new Float32Array(trPoints * 3);

      for (let i = 0; i < trPoints; i++) {
        const arm = i % 2;
        const r = 2 + 58 * Math.pow(Math.random(), 1.5);
        const theta = arm * Math.PI + 2.5 * Math.log(r / 3) + (Math.random() - 0.5) * 0.35;

        trPos[i * 3] = Math.cos(theta) * r + (Math.random() - 0.5) * 3;
        trPos[i * 3 + 1] = (Math.random() - 0.5) * 3;
        trPos[i * 3 + 2] = Math.sin(theta) * r + (Math.random() - 0.5) * 3;

        const p = r / 60;
        if (p < 0.18) {
          trCol[i * 3] = 1.0; trCol[i * 3 + 1] = 0.98; trCol[i * 3 + 2] = 1.0;
        } else if (p < 0.5) {
          trCol[i * 3] = 0.72; trCol[i * 3 + 1] = 0.45; trCol[i * 3 + 2] = 1.0;
        } else {
          trCol[i * 3] = 0.28; trCol[i * 3 + 1] = 0.72; trCol[i * 3 + 2] = 1.0;
        }
      }

      const trGeo = new THREE.BufferGeometry();
      trGeo.setAttribute('position', new THREE.BufferAttribute(trPos, 3));
      trGeo.setAttribute('color', new THREE.BufferAttribute(trCol, 3));
      const trPts = new THREE.Points(trGeo, new THREE.PointsMaterial({
        size: 1.8,
        vertexColors: true,
        map: createSoftPointTexture(),
        transparent: true,
        opacity: 0.85,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      }));
      trGalaxyGroup.add(trPts);
      scene.add(trGalaxyGroup);
    }

    /* -------------------------------------------------------------
       8. NIVORA DIGITAL CORE (CYBER HOLOGRAPHIC GLOBE & SUSPENDED LOGO)
       ------------------------------------------------------------- */
    function buildNivoraGlobeCore() {
      globeGroup = new THREE.Group();
      globeGroup.position.set(globeCenterX, globeCenterY, globeCenterZ);

      const globeRadius = 25.5;
      const cyberTex = createDigitalWorldTextureCinematic();

      // Inner Cyber Continents Globe
      const sphereGeo = new THREE.SphereGeometry(globeRadius, 64, 64);
      const sphereMat = new THREE.MeshBasicMaterial({
        map: cyberTex,
        transparent: true,
        opacity: 0.92,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });
      globeMesh = new THREE.Mesh(sphereGeo, sphereMat);
      globeGroup.add(globeMesh);

      // Atmospheric Glass Shell with Brilliant Fresnel Rim
      const atmosGeo = new THREE.SphereGeometry(globeRadius * 1.05, 48, 48);
      const atmosMat = new THREE.ShaderMaterial({
        vertexShader: `
          varying vec3 vNormal;
          void main() {
            vNormal = normalize(normalMatrix * normal);
            gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
          }
        `,
        fragmentShader: `
          varying vec3 vNormal;
          void main() {
            float fresnel = 1.0 - dot(vNormal, vec3(0.0, 0.0, 1.0));
            fresnel = pow(fresnel, 2.5);

            vec3 cyanColor = vec3(0.02, 0.71, 0.83);    // #06b6d4
            vec3 purpleColor = vec3(0.66, 0.33, 0.97);  // #a855f7
            vec3 magentaColor = vec3(0.93, 0.28, 0.94); // #ec4899

            vec3 rimColor = mix(cyanColor, purpleColor, fresnel * 0.8);
            rimColor = mix(rimColor, magentaColor, pow(fresnel, 3.8));

            gl_FragColor = vec4(rimColor, fresnel * 0.95);
          }
        `,
        transparent: true,
        blending: THREE.AdditiveBlending,
        side: THREE.FrontSide,
        depthWrite: false
      });
      atmosphereMesh = new THREE.Mesh(atmosGeo, atmosMat);
      globeGroup.add(atmosphereMesh);

      // Radiant Atmospheric Corona Sprite
      const haloMat = new THREE.SpriteMaterial({
        map: createCoronaHaloTexture(),
        transparent: true,
        opacity: 0.75,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });
      globeHaloSprite = new THREE.Sprite(haloMat);
      globeHaloSprite.scale.set(82, 82, 1);
      globeHaloSprite.renderOrder = 15;
      globeGroup.add(globeHaloSprite);

      // Official NIVORA 3D Logo (Suspended at Center with Glowing Aura)
      const logoLoader = new THREE.TextureLoader();
      logoLoader.load('assets/images/nivora-logo.png', (tex) => {
        tex.minFilter = THREE.LinearFilter;
        tex.magFilter = THREE.LinearFilter;
        const logoMat = new THREE.SpriteMaterial({
          map: tex,
          transparent: true,
          opacity: 1.0,
          blending: THREE.NormalBlending,
          depthTest: false
        });
        logoSprite = new THREE.Sprite(logoMat);
        logoSprite.scale.set(17.5, 17.5, 1);
        logoSprite.renderOrder = 30;
        globeGroup.add(logoSprite);

        const auraMat = new THREE.SpriteMaterial({
          map: createSoftPointTexture(),
          color: 0x06b6d4,
          transparent: true,
          opacity: 0.65,
          blending: THREE.AdditiveBlending,
          depthTest: false
        });
        const auraSprite = new THREE.Sprite(auraMat);
        auraSprite.scale.set(24, 24, 1);
        auraSprite.renderOrder = 25;
        globeGroup.add(auraSprite);
      });

      scene.add(globeGroup);
    }

    /* -------------------------------------------------------------
       9. GALACTIC SWIRLING VORTEX ACCRETION DISC & BEAM
       ------------------------------------------------------------- */
    function buildGalacticAccretionPlatform() {
      const beamHeight = 22;
      const vortexY = globeCenterY - 25.5 - beamHeight + 3;

      accretionGroup = new THREE.Group();
      accretionGroup.position.set(globeCenterX, vortexY, globeCenterZ);
      accretionGroup.rotation.set(Math.PI / 2.3, 0, 0.1);

      // 1. Concentric luminous vortex rings
      const ringConfigs = [
        { inner: 3, outer: 14, color: 0xffffff, opacity: 0.95 },
        { inner: 12, outer: 28, color: 0x06b6d4, opacity: 0.85 },
        { inner: 26, outer: 48, color: 0xa855f7, opacity: 0.75 },
        { inner: 45, outer: 72, color: 0xec4899, opacity: 0.65 },
        { inner: 68, outer: 95, color: 0x8b5cf6, opacity: 0.35 }
      ];

      ringConfigs.forEach(rc => {
        const rGeo = new THREE.RingGeometry(rc.inner, rc.outer, 64);
        const rMat = new THREE.MeshBasicMaterial({
          color: rc.color,
          transparent: true,
          opacity: rc.opacity,
          side: THREE.DoubleSide,
          blending: THREE.AdditiveBlending,
          depthWrite: false
        });
        const rMesh = new THREE.Mesh(rGeo, rMat);
        accretionGroup.add(rMesh);
      });

      // 2. 4,500 Swirling Spiral Particles
      const dPoints = 4500;
      const dPos = new Float32Array(dPoints * 3);
      const dCol = new Float32Array(dPoints * 3);

      for (let i = 0; i < dPoints; i++) {
        const arm = i % 4;
        const radius = 6 + Math.pow(Math.random(), 1.2) * 88;
        const angle = (arm * Math.PI / 2) + 2.8 * Math.log(radius / 5) + (Math.random() - 0.5) * 0.45;

        dPos[i * 3] = Math.cos(angle) * radius;
        dPos[i * 3 + 1] = (Math.random() - 0.5) * 2.2;
        dPos[i * 3 + 2] = Math.sin(angle) * radius;

        const p = radius / 94;
        if (p < 0.2) {
          dCol[i * 3] = 1.0; dCol[i * 3 + 1] = 1.0; dCol[i * 3 + 2] = 1.0;
        } else if (p < 0.45) {
          dCol[i * 3] = 0.05; dCol[i * 3 + 1] = 0.75; dCol[i * 3 + 2] = 0.95;
        } else if (p < 0.75) {
          dCol[i * 3] = 0.92; dCol[i * 3 + 1] = 0.28; dCol[i * 3 + 2] = 0.94;
        } else {
          dCol[i * 3] = 0.55; dCol[i * 3 + 1] = 0.22; dCol[i * 3 + 2] = 0.95;
        }
      }

      const dGeo = new THREE.BufferGeometry();
      dGeo.setAttribute('position', new THREE.BufferAttribute(dPos, 3));
      dGeo.setAttribute('color', new THREE.BufferAttribute(dCol, 3));
      accretionParticles = new THREE.Points(dGeo, new THREE.PointsMaterial({
        size: 2.2,
        vertexColors: true,
        map: createSoftPointTexture(),
        transparent: true,
        opacity: 0.85,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      }));
      accretionGroup.add(accretionParticles);
      scene.add(accretionGroup);

      // 3. Vertical Projection Light Column
      const beamGeo = new THREE.CylinderGeometry(1.6, 5.0, beamHeight, 32, 1, true);
      const beamCanvas = document.createElement('canvas');
      beamCanvas.width = 128; beamCanvas.height = 256;
      const bCtx = beamCanvas.getContext('2d');
      const bGrad = bCtx.createLinearGradient(0, 0, 0, 256);
      bGrad.addColorStop(0, 'rgba(255, 255, 255, 0.95)');
      bGrad.addColorStop(0.2, 'rgba(6, 182, 212, 0.85)');
      bGrad.addColorStop(0.7, 'rgba(168, 85, 247, 0.65)');
      bGrad.addColorStop(1, 'rgba(236, 72, 153, 0.1)');
      bCtx.fillStyle = bGrad;
      bCtx.fillRect(0, 0, 128, 256);

      energyBeam = new THREE.Mesh(beamGeo, new THREE.MeshBasicMaterial({
        map: new THREE.CanvasTexture(beamCanvas),
        transparent: true,
        opacity: 0.85,
        blending: THREE.AdditiveBlending,
        side: THREE.DoubleSide,
        depthWrite: false
      }));
      energyBeam.position.set(globeCenterX, globeCenterY - 25.5 - beamHeight / 2 + 2, globeCenterZ);
      scene.add(energyBeam);
    }

    /* -------------------------------------------------------------
       10. 4 ELEGANT 3D ORBITAL RINGS WITH GLOWING SATELLITES
       ------------------------------------------------------------- */
    function buildOrbitalRings3D() {
      const ringSpecs = [
        { radiusX: 38, radiusY: 34, rotX: 1.25, rotY: 0.15, rotZ: 0.25, color: 0x06b6d4, speed: 0.002 },
        { radiusX: 44, radiusY: 38, rotX: 0.55, rotY: 1.15, rotZ: -0.50, color: 0xa855f7, speed: -0.0018 },
        { radiusX: 52, radiusY: 44, rotX: -0.75, rotY: 0.45, rotZ: 0.95, color: 0x38bdf8, speed: 0.0022 },
        { radiusX: 60, radiusY: 48, rotX: 0.35, rotY: -0.85, rotZ: 0.65, color: 0xec4899, speed: -0.0015 }
      ];

      ringSpecs.forEach((spec, rIdx) => {
        const curve = new THREE.EllipseCurve(0, 0, spec.radiusX, spec.radiusY, 0, 2 * Math.PI, false, 0);
        const points = curve.getPoints(120);
        const ringGeo = new THREE.BufferGeometry().setFromPoints(points);

        const ringLine = new THREE.Line(ringGeo, new THREE.LineBasicMaterial({
          color: spec.color,
          transparent: true,
          opacity: 0.52,
          blending: THREE.AdditiveBlending
        }));
        ringLine.rotation.set(spec.rotX, spec.rotY, spec.rotZ);
        globeGroup.add(ringLine);

        const bead = new THREE.Mesh(
          new THREE.SphereGeometry(1.0, 12, 12),
          new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.95 })
        );
        const halo = new THREE.Sprite(new THREE.SpriteMaterial({
          map: createSoftPointTexture(),
          color: spec.color,
          transparent: true,
          opacity: 0.8,
          blending: THREE.AdditiveBlending
        }));
        halo.scale.set(5.5, 5.5, 1);
        bead.add(halo);

        globeGroup.add(bead);
        ringParticles.push({
          mesh: bead,
          curve: curve,
          rotX: spec.rotX,
          rotY: spec.rotY,
          rotZ: spec.rotZ,
          progress: rIdx * 0.25,
          speed: spec.speed
        });
      });
    }"""

if core_funcs_target in code:
    code = code.replace(core_funcs_target, core_funcs_replacement)
    print("Replaced core Three.js functions")
else:
    print("Core Three.js functions target not found")

# Add createDigitalWorldTextureCinematic and createCoronaHaloTexture
texture_target = r"""    function createDigitalWorldTextureClean() {
      const c = document.createElement('canvas');
      c.width = 1024; c.height = 512;
      const ctx = c.getContext('2d');

      ctx.fillStyle = 'rgba(2, 6, 20, 0.4)';
      ctx.fillRect(0, 0, 1024, 512);

      ctx.strokeStyle = 'rgba(6, 182, 212, 0.18)';
      ctx.lineWidth = 0.8;
      for (let x = 0; x < 1024; x += 64) {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, 512); ctx.stroke();
      }
      for (let y = 0; y < 512; y += 48) {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(1024, y); ctx.stroke();
      }

      ctx.fillStyle = 'rgba(6, 182, 212, 0.65)';
      const drawNodes = (cx, cy, radius, count) => {
        for (let i = 0; i < count; i++) {
          const r = Math.random() * radius;
          const a = Math.random() * Math.PI * 2;
          ctx.beginPath();
          ctx.arc(cx + Math.cos(a) * r, cy + Math.sin(a) * r * 0.7, 1.2 + Math.random() * 1.4, 0, Math.PI * 2);
          ctx.fill();
        }
      };
      drawNodes(260, 200, 100, 120);
      drawNodes(340, 360, 80, 90);
      drawNodes(530, 180, 75, 100);
      drawNodes(560, 310, 90, 110);
      drawNodes(740, 190, 120, 160);
      drawNodes(860, 380, 65, 80);

      return new THREE.CanvasTexture(c);
    }"""

texture_replacement = r"""    function createCoronaHaloTexture() {
      const c = document.createElement('canvas');
      c.width = 256; c.height = 256;
      const ctx = c.getContext('2d');
      const grad = ctx.createRadialGradient(128, 128, 60, 128, 128, 128);
      grad.addColorStop(0, 'rgba(6, 182, 212, 0)');
      grad.addColorStop(0.65, 'rgba(6, 182, 212, 0.35)');
      grad.addColorStop(0.85, 'rgba(168, 85, 247, 0.55)');
      grad.addColorStop(1, 'rgba(236, 72, 153, 0)');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, 256, 256);
      return new THREE.CanvasTexture(c);
    }

    function createDigitalWorldTextureCinematic() {
      const c = document.createElement('canvas');
      c.width = 2048; c.height = 1024;
      const ctx = c.getContext('2d');

      // Deep space base
      ctx.fillStyle = '#020617';
      ctx.fillRect(0, 0, 2048, 1024);

      // High-tech digital grid
      ctx.strokeStyle = 'rgba(6, 182, 212, 0.12)';
      ctx.lineWidth = 1;
      for (let x = 0; x < 2048; x += 40) {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, 1024); ctx.stroke();
      }
      for (let y = 0; y < 1024; y += 40) {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(2048, y); ctx.stroke();
      }

      // Meridians
      ctx.strokeStyle = 'rgba(56, 189, 248, 0.35)';
      ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(0, 512); ctx.lineTo(2048, 512); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(0, 370); ctx.lineTo(2048, 370); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(0, 654); ctx.lineTo(2048, 654); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(512, 0); ctx.lineTo(512, 1024); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(1024, 0); ctx.lineTo(1024, 1024); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(1536, 0); ctx.lineTo(1536, 1024); ctx.stroke();

      // Continents
      const continents = [
        [[350, 150], [580, 120], [680, 220], [600, 380], [520, 480], [420, 520], [380, 450], [280, 320], [280, 200]],
        [[480, 530], [600, 560], [640, 680], [580, 850], [500, 920], [460, 750], [450, 600]],
        [[950, 180], [1120, 160], [1180, 260], [1080, 360], [980, 380], [920, 300]],
        [[960, 400], [1180, 410], [1250, 540], [1180, 750], [1100, 850], [980, 680], [930, 520]],
        [[1150, 160], [1650, 150], [1780, 280], [1700, 480], [1500, 550], [1320, 520], [1200, 420], [1160, 280]],
        [[1520, 650], [1720, 640], [1760, 760], [1680, 840], [1540, 820], [1480, 720]]
      ];

      continents.forEach(poly => {
        ctx.beginPath();
        ctx.moveTo(poly[0][0], poly[0][1]);
        for (let i = 1; i < poly.length; i++) ctx.lineTo(poly[i][0], poly[i][1]);
        ctx.closePath();

        ctx.fillStyle = 'rgba(6, 182, 212, 0.22)';
        ctx.fill();

        ctx.strokeStyle = 'rgba(56, 189, 248, 0.85)';
        ctx.lineWidth = 3;
        ctx.stroke();

        let minX = 2048, maxX = 0, minY = 1024, maxY = 0;
        poly.forEach(pt => {
          minX = Math.min(minX, pt[0]); maxX = Math.max(maxX, pt[0]);
          minY = Math.min(minY, pt[1]); maxY = Math.max(maxY, pt[1]);
        });

        ctx.fillStyle = 'rgba(56, 189, 248, 0.95)';
        for (let dx = minX; dx <= maxX; dx += 14) {
          for (let dy = minY; dy <= maxY; dy += 14) {
            if (ctx.isPointInPath(dx, dy)) {
              ctx.beginPath();
              ctx.arc(dx + (Math.random() - 0.5) * 4, dy + (Math.random() - 0.5) * 4, 1.8 + Math.random() * 1.5, 0, Math.PI * 2);
              ctx.fill();
            }
          }
        }
      });

      // Neural connection hubs
      const hubs = [
        [480, 320], [560, 240], [540, 620], [1040, 280], [1100, 600],
        [1350, 320], [1500, 380], [1620, 720]
      ];
      ctx.strokeStyle = 'rgba(168, 85, 247, 0.7)';
      ctx.lineWidth = 1.5;
      for (let i = 0; i < hubs.length; i++) {
        for (let j = i + 1; j < hubs.length; j++) {
          const d = Math.hypot(hubs[i][0] - hubs[j][0], hubs[i][1] - hubs[j][1]);
          if (d < 350) {
            ctx.beginPath();
            ctx.moveTo(hubs[i][0], hubs[i][1]);
            ctx.lineTo(hubs[j][0], hubs[j][1]);
            ctx.stroke();
          }
        }
      }

      hubs.forEach(h => {
        const radGrad = ctx.createRadialGradient(h[0], h[1], 0, h[0], h[1], 16);
        radGrad.addColorStop(0, 'rgba(255, 255, 255, 1)');
        radGrad.addColorStop(0.3, 'rgba(6, 182, 212, 0.9)');
        radGrad.addColorStop(1, 'rgba(168, 85, 247, 0)');
        ctx.fillStyle = radGrad;
        ctx.beginPath();
        ctx.arc(h[0], h[1], 16, 0, Math.PI * 2);
        ctx.fill();
      });

      return new THREE.CanvasTexture(c);
    }"""

if texture_target in code:
    code = code.replace(texture_target, texture_replacement)
    print("Replaced texture generation functions")
else:
    print("Texture functions target not found")

# Update animation loop in animateUniverseCinematic:
anim_target = r"""      // Globe axial rotation & logo floating
      if (globeMesh) globeMesh.rotation.y += 0.0014 * warpSpeedFactor;
      if (logoSprite) {
        logoSprite.position.y = Math.sin(elapsed * 1.5) * 0.5;
      }"""

anim_replacement = r"""      // Globe axial rotation & logo floating
      if (globeMesh) globeMesh.rotation.y += 0.0014 * warpSpeedFactor;
      if (logoSprite) {
        logoSprite.position.y = Math.sin(elapsed * 1.5) * 0.5;
      }

      // Foreground & background celestial rotation
      if (blPlanetMesh) blPlanetMesh.rotation.y += 0.0003;
      if (brPlanetMesh) brPlanetMesh.rotation.y += 0.0004;
      if (trGalaxyGroup) trGalaxyGroup.rotation.z += 0.0012;
      if (accretionGroup) accretionGroup.rotation.z += 0.0032 * warpSpeedFactor;"""

if anim_target in code:
    code = code.replace(anim_target, anim_replacement)
    print("Updated animation loop")
else:
    print("Animation loop target not found")

# Save updated master builder
with open(MASTER_BUILDER, "w", encoding="utf-8") as f:
    f.write(code)

print("Saved updated assemble_ultimate_3d_universe.py successfully!")
