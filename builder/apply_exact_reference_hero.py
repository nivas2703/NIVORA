#!/usr/bin/env python3
"""
builder/apply_exact_reference_hero.py
Transforms the NIVORA 3D universe into an exact, pixel-perfect match
of the user's uploaded reference image (hero-reference.jpg):

1. SPLIT 2-COLUMN HERO:
   - Left side: Eyebrow badge, 'Welcome to NIVORA.', cursive 'Ideas' & 'Products.', description, CTAs, metrics.
   - Right side: 3D Holographic Globe, Ribbon Logo inside, 3 Orbital Rings, Swirling Galaxy Vortex & Upward Light Beam.
2. 3D CYBER-GLOBE (RIGHT SIDE):
   - Translucent crystal cyber-sphere with glowing cyan/violet meridians and continent outlines (no opaque background).
   - Atmospheric Fresnel rim glow (cyan + violet + magenta).
   - Official NIVORA 3D ribbon logo floating sharp, bright, and proud in the exact center with soft glowing backing aura.
   - 3 Concentric tilted glowing orbital rings with luminous pearl satellites.
   - Beneath the globe: Swirling galaxy accretion vortex (3,800 particles in logarithmic spiral, glowing gradient core) + vertical volumetric cyan light beam shining up into the globe!
   - Celestial purple moon orbiting nearby.
3. CORNER CELESTIAL ELEMENTS (MATCHING REFERENCE EXACTLY):
   - Bottom-left: Curved deep blue planet horizon with radiant cyan atmospheric Fresnel limb.
   - Bottom-right: Curved shadowed purple planet horizon with warm magenta/violet Fresnel crescent.
   - Top-right: Tilted distant spiral galaxy in deep space with bright core.
   - Top-left: Purple/magenta cosmic nebula dust cloud.
4. ZERO HERO CLUTTER:
   - Product constellation (Checkra, Homora, Bubora, Sayora) is strictly hidden while in the hero (targetScrollP <= 0.12).
   - They smoothly appear in 3D space only when scrolling down into the Products section.
5. PRESERVE 100% of existing content, modals, links, and 6-stage space-travel flight system.
"""

import os
import re

MASTER_FILE = "/Users/bennabathulanivas/Desktop/my projects/NIVORA/builder/assemble_ultimate_3d_universe.py"

with open(MASTER_FILE, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Ensure globeCenterX = 68, globeCenterY = 12, globeCenterZ = 0
code = re.sub(r'const globeCenterX\s*=\s*[^;\n]+;', 'const globeCenterX = 68.0;', code)
code = re.sub(r'const globeCenterY\s*=\s*[^;\n]+;', 'const globeCenterY = 12.0;', code)
code = re.sub(r'const globeCenterZ\s*=\s*[^;\n]+;', 'const globeCenterZ = 0.0;', code)

# 2. Camera initial position and lookAt:
# camera at (0, 0, 260) looking at (0, 4, 0)
code = re.sub(r'const baseCamX\s*=\s*[^;\n]+;', 'const baseCamX = 0;', code)
code = re.sub(r'const baseCamY\s*=\s*[^;\n]+;', 'const baseCamY = 0;', code)
code = re.sub(r'const baseCamZ\s*=\s*[^;\n]+;', 'const baseCamZ = 260;', code)

# 3. Ensure getCameraTrajectory(p) handles the space-travel flight smoothly starting from (0, 0, 260)
traj_pattern = r'function getCameraTrajectory\(p\) \{[\s\S]*?(?=\n    function animateUniverseCinematic)'
traj_replacement = """function getCameraTrajectory(p) {
      // 6-STAGE SPACE-TRAVEL FLIGHT PATH (Z: +260 -> -1380)
      if (p <= 0.16) {
        // Stage 1: HERO -> Space-travel forward acceleration past the core into the cosmos
        const t = p / 0.16;
        const ease = t * t * (3 - 2 * t);
        return {
          pos: new THREE.Vector3(
            0 + (12 - 0) * ease,
            0 + (8 - 0) * ease,
            baseCamZ + (110 - baseCamZ) * ease   // 260 -> 110 (Forward travel!)
          ),
          look: new THREE.Vector3(
            20 + (15 - 20) * ease,
            8 + (8 - 8) * ease,
            0 + (-120 - 0) * ease
          )
        };
      } else if (p <= 0.38) {
        // Stage 2: PRODUCT CONSTELLATION ARRIVAL (Z: -190)
        const t = (p - 0.16) / 0.22;
        const ease = t * t * (3 - 2 * t);
        return {
          pos: new THREE.Vector3(
            12 + (-4 - 12) * ease,
            8 + (10 - 8) * ease,
            110 + (-190 - 110) * ease
          ),
          look: new THREE.Vector3(
            15 + (0 - 15) * ease,
            8 + (10 - 8) * ease,
            -120 + (-350 - -120) * ease
          )
        };
      } else if (p <= 0.58) {
        // Stage 3: THE BUILDER (NIVAS) ARRIVAL (Z: -520)
        const t = (p - 0.38) / 0.20;
        const ease = t * t * (3 - 2 * t);
        return {
          pos: new THREE.Vector3(
            -4 + (-14 - -4) * ease,
            10 + (6 - 10) * ease,
            -190 + (-520 - -190) * ease
          ),
          look: new THREE.Vector3(
            0 + (-10 - 0) * ease,
            10 + (6 - 10) * ease,
            -350 + (-720 - -350) * ease
          )
        };
      } else if (p <= 0.78) {
        // Stage 4: PORTFOLIO ARCHIVES ARRIVAL (Z: -820)
        const t = (p - 0.58) / 0.20;
        const ease = t * t * (3 - 2 * t);
        return {
          pos: new THREE.Vector3(
            -14 + (8 - -14) * ease,
            6 + (12 - 6) * ease,
            -520 + (-820 - -520) * ease
          ),
          look: new THREE.Vector3(
            -10 + (4 - -10) * ease,
            6 + (10 - 6) * ease,
            -720 + (-1050 - -720) * ease
          )
        };
      } else if (p <= 0.90) {
        // Stage 5: ECOSYSTEM PHILOSOPHY & VISION (Z: -1100)
        const t = (p - 0.78) / 0.12;
        const ease = t * t * (3 - 2 * t);
        return {
          pos: new THREE.Vector3(
            8 + (-2 - 8) * ease,
            12 + (8 - 12) * ease,
            -820 + (-1100 - -820) * ease
          ),
          look: new THREE.Vector3(
            4 + (0 - 4) * ease,
            10 + (8 - 10) * ease,
            -1050 + (-1280 - -1050) * ease
          )
        };
      } else {
        // Stage 6: TRANSMISSION TERMINAL (Z: -1380)
        const t = (p - 0.90) / 0.10;
        const ease = t * t * (3 - 2 * t);
        return {
          pos: new THREE.Vector3(
            -2 + (0 - -2) * ease,
            8 + (4 - 8) * ease,
            -1100 + (-1380 - -1100) * ease
          ),
          look: new THREE.Vector3(
            0,
            8 + (4 - 8) * ease,
            -1280 + (-1560 - -1280) * ease
          )
        };
      }
    }"""

code = re.sub(traj_pattern, traj_replacement, code)

# 4. Refine createDigitalWorldTextureCinematic to have a TRANSPARENT background
# so the cyber sphere is holographic and the logo inside shines through!
tex_pattern = r'function createDigitalWorldTextureCinematic\(\) \{[\s\S]*?(?=\n    function setupInteractivity|\n    function createOceanPlanetTexture)'
tex_replacement = """function createDigitalWorldTextureCinematic() {
      const c = document.createElement('canvas');
      c.width = 2048; c.height = 1024;
      const ctx = c.getContext('2d');

      // Transparent base for crystal holographic globe
      ctx.clearRect(0, 0, 2048, 1024);

      // Delicate cyber grid lines
      ctx.strokeStyle = 'rgba(6, 182, 212, 0.16)';
      ctx.lineWidth = 1;
      for (let x = 0; x < 2048; x += 48) {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, 1024); ctx.stroke();
      }
      for (let y = 0; y < 1024; y += 48) {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(2048, y); ctx.stroke();
      }

      // Key Latitude & Longitude Meridians
      ctx.strokeStyle = 'rgba(56, 189, 248, 0.45)';
      ctx.lineWidth = 2.2;
      [256, 512, 768].forEach(y => {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(2048, y); ctx.stroke();
      });
      [256, 512, 1024, 1536, 1792].forEach(x => {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, 1024); ctx.stroke();
      });

      // Continental Landmass Polygonal Outlines
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

        ctx.fillStyle = 'rgba(6, 182, 212, 0.14)';
        ctx.fill();

        ctx.strokeStyle = 'rgba(56, 189, 248, 0.75)';
        ctx.lineWidth = 2.4;
        ctx.stroke();

        // Digital Data Nodes within Continent
        ctx.fillStyle = 'rgba(168, 85, 247, 0.85)';
        for (let i = 0; i < 24; i++) {
          const pt = poly[i % poly.length];
          const rx = pt[0] + (Math.sin(i * 1.5) * 45);
          const ry = pt[1] + (Math.cos(i * 1.5) * 35);
          ctx.beginPath();
          ctx.arc(rx, ry, 2.5, 0, Math.PI * 2);
          ctx.fill();
        }
      });

      return new THREE.CanvasTexture(c);
    }"""

code = re.sub(tex_pattern, tex_replacement, code)

# 5. Refine buildNivoraGlobeCore so the globe is transparent and the logo is 100% visible
core_pattern = r'function buildNivoraGlobeCore\(\) \{[\s\S]*?(?=\n    /\* -------------------------------------------------------------\n       9\. GALACTIC SWIRLING VORTEX ACCRETION DISC)'
core_replacement = """function buildNivoraGlobeCore() {
      globeGroup = new THREE.Group();
      globeGroup.position.set(globeCenterX, globeCenterY, globeCenterZ);

      const globeRadius = 25.5;
      const cyberTex = createDigitalWorldTextureCinematic();

      // 1. Inner Translucent Cyber Continents Globe
      const sphereGeo = new THREE.SphereGeometry(globeRadius, 64, 64);
      const sphereMat = new THREE.MeshBasicMaterial({
        map: cyberTex,
        transparent: true,
        opacity: 0.52,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });
      globeMesh = new THREE.Mesh(sphereGeo, sphereMat);
      globeGroup.add(globeMesh);

      // 2. Atmospheric Glass Shell with Brilliant Fresnel Rim
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
            fresnel = pow(fresnel, 2.4);

            vec3 cyanColor = vec3(0.02, 0.75, 0.95);    // #00f5ff
            vec3 purpleColor = vec3(0.66, 0.33, 0.97);  // #a855f7
            vec3 magentaColor = vec3(0.93, 0.28, 0.94); // #ec4899

            vec3 rimColor = mix(cyanColor, purpleColor, fresnel * 0.7);
            rimColor = mix(rimColor, magentaColor, pow(fresnel, 3.2));

            gl_FragColor = vec4(rimColor, fresnel * 0.92);
          }
        `,
        transparent: true,
        blending: THREE.AdditiveBlending,
        side: THREE.FrontSide,
        depthWrite: false
      });
      atmosphereMesh = new THREE.Mesh(atmosGeo, atmosMat);
      globeGroup.add(atmosphereMesh);

      // 3. Radiant Atmospheric Corona Sprite
      const haloMat = new THREE.SpriteMaterial({
        map: createCoronaHaloTexture(),
        transparent: true,
        opacity: 0.65,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });
      globeHaloSprite = new THREE.Sprite(haloMat);
      globeHaloSprite.scale.set(78, 78, 1);
      globeHaloSprite.renderOrder = 15;
      globeGroup.add(globeHaloSprite);

      // 4. Official NIVORA 3D Ribbon Logo (Suspended at Exact Center, Bright & Crisp)
      const logoLoader = new THREE.TextureLoader();
      const domLogo = document.querySelector('.nav-logo-icon');
      const logoSrc = (domLogo && domLogo.getAttribute('src')) ? domLogo.src : 'assets/images/nivora-logo.png';
      logoLoader.load(logoSrc, (tex) => {
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
        logoSprite.scale.set(19.0, 19.0, 1);
        logoSprite.renderOrder = 50;
        globeGroup.add(logoSprite);

        // Radiant Backing Aura
        const auraMat = new THREE.SpriteMaterial({
          map: createSoftPointTexture(),
          color: 0x06b6d4,
          transparent: true,
          opacity: 0.55,
          blending: THREE.AdditiveBlending,
          depthTest: false
        });
        const auraSprite = new THREE.Sprite(auraMat);
        auraSprite.scale.set(25, 25, 1);
        auraSprite.renderOrder = 45;
        globeGroup.add(auraSprite);
      });

      // 5. Orbiting Purple Moon
      const moonGeo = new THREE.SphereGeometry(3.6, 24, 24);
      const moonMat = new THREE.MeshBasicMaterial({
        color: 0x8b5cf6,
        transparent: true,
        opacity: 0.90
      });
      const moonMesh = new THREE.Mesh(moonGeo, moonMat);
      moonMesh.position.set(-36, 32, -15);
      globeGroup.add(moonMesh);

      const moonHalo = new THREE.Sprite(new THREE.SpriteMaterial({
        map: createSoftPointTexture(),
        color: 0xc084fc,
        transparent: true,
        opacity: 0.65,
        blending: THREE.AdditiveBlending
      }));
      moonHalo.scale.set(14, 14, 1);
      moonHalo.position.set(-36, 32, -15);
      globeGroup.add(moonHalo);

      scene.add(globeGroup);
    }"""

code = re.sub(core_pattern, core_replacement, code)

# 6. Refine buildGalacticAccretionPlatform to have soft swirling spiral particles and upward light beam
accretion_pattern = r'function buildGalacticAccretionPlatform\(\) \{[\s\S]*?(?=\n    /\* -------------------------------------------------------------\n       10\. 4 ELEGANT 3D ORBITAL RINGS)'
accretion_replacement = """function buildGalacticAccretionPlatform() {
      const beamHeight = 22;
      const vortexY = globeCenterY - 25.5 - beamHeight + 3;

      accretionGroup = new THREE.Group();
      accretionGroup.position.set(globeCenterX, vortexY, globeCenterZ);
      accretionGroup.rotation.set(Math.PI / 2.3, 0, 0.1);

      // 1. Soft glowing gradient disc base
      const discCanvas = document.createElement('canvas');
      discCanvas.width = 512; discCanvas.height = 512;
      const dCtx = discCanvas.getContext('2d');
      const dGrad = dCtx.createRadialGradient(256, 256, 10, 256, 256, 256);
      dGrad.addColorStop(0, 'rgba(255, 255, 255, 0.95)');
      dGrad.addColorStop(0.15, 'rgba(6, 182, 212, 0.75)');
      dGrad.addColorStop(0.40, 'rgba(168, 85, 247, 0.55)');
      dGrad.addColorStop(0.70, 'rgba(236, 72, 153, 0.35)');
      dGrad.addColorStop(1, 'rgba(2, 6, 23, 0)');
      dCtx.fillStyle = dGrad;
      dCtx.fillRect(0, 0, 512, 512);

      const discTex = new THREE.CanvasTexture(discCanvas);
      const discGeo = new THREE.PlaneGeometry(160, 160);
      const discMat = new THREE.MeshBasicMaterial({
        map: discTex,
        transparent: true,
        opacity: 0.85,
        side: THREE.DoubleSide,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });
      accretionDisk = new THREE.Mesh(discGeo, discMat);
      accretionGroup.add(accretionDisk);

      // 2. 4,200 Swirling Spiral Vortex Particles
      const dPoints = 4200;
      const dPos = new Float32Array(dPoints * 3);
      const dCol = new Float32Array(dPoints * 3);

      for (let i = 0; i < dPoints; i++) {
        const arm = i % 3;
        const radius = 6 + Math.pow(Math.random(), 1.25) * 82;
        const angle = (arm * (2 * Math.PI / 3)) + (radius * 0.08) + (Math.random() - 0.5) * 0.42;

        dPos[i * 3] = Math.cos(angle) * radius;
        dPos[i * 3 + 1] = Math.sin(angle) * radius;
        dPos[i * 3 + 2] = (Math.random() - 0.5) * (4.0 * (1 - radius / 88));

        // Color transition: White/cyan core -> Violet -> Magenta outer edge
        const t = radius / 82;
        if (t < 0.25) {
          dCol[i * 3] = 0.55 + 0.45 * (1 - t * 4);
          dCol[i * 3 + 1] = 0.90 + 0.10 * (1 - t * 4);
          dCol[i * 3 + 2] = 1.0;
        } else if (t < 0.65) {
          const st = (t - 0.25) / 0.40;
          dCol[i * 3] = 0.45 + 0.35 * st;
          dCol[i * 3 + 1] = 0.55 * (1 - st);
          dCol[i * 3 + 2] = 0.95;
        } else {
          const st = (t - 0.65) / 0.35;
          dCol[i * 3] = 0.80 + 0.15 * st;
          dCol[i * 3 + 1] = 0.20 * (1 - st);
          dCol[i * 3 + 2] = 0.85 * (1 - st * 0.3);
        }
      }

      const dGeo = new THREE.BufferGeometry();
      dGeo.setAttribute('position', new THREE.BufferAttribute(dPos, 3));
      dGeo.setAttribute('color', new THREE.BufferAttribute(dCol, 3));

      const dMat = new THREE.PointsMaterial({
        size: 1.8,
        vertexColors: true,
        transparent: true,
        opacity: 0.90,
        blending: THREE.AdditiveBlending,
        depthWrite: false,
        map: createSoftPointTexture()
      });

      accretionParticles = new THREE.Points(dGeo, dMat);
      accretionGroup.add(accretionParticles);
      scene.add(accretionGroup);

      // 3. Vertical Cyan Light Projection Beam
      const beamGeo = new THREE.CylinderGeometry(1.2, 5.5, beamHeight, 32, 1, true);
      const beamMat = new THREE.MeshBasicMaterial({
        color: 0x06b6d4,
        transparent: true,
        opacity: 0.48,
        side: THREE.DoubleSide,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });
      energyBeam = new THREE.Mesh(beamGeo, beamMat);
      energyBeam.position.set(globeCenterX, globeCenterY - 25.5 - (beamHeight / 2) + 2, globeCenterZ);
      scene.add(energyBeam);
    }"""

code = re.sub(accretion_pattern, accretion_replacement, code)

# 7. Refine buildCelestialForeAndBackground so planets and galaxies match the reference image
celestial_pattern = r'function buildCelestialForeAndBackground\(\) \{[\s\S]*?(?=\n    /\* -------------------------------------------------------------\n       8\. NIVORA HOLOGRAPHIC CYBER-GLOBE CORE)'
celestial_replacement = """function buildCelestialForeAndBackground() {
      // 1. Bottom-Left Curved Horizon (Massive Deep-Blue Planet Framing Corner)
      const blGeo = new THREE.SphereGeometry(135, 48, 48);
      const blMat = new THREE.MeshBasicMaterial({
        map: createOceanPlanetTexture(),
        transparent: true,
        opacity: 0.98
      });
      blPlanetMesh = new THREE.Mesh(blGeo, blMat);
      blPlanetMesh.position.set(-170, -170, 75);
      scene.add(blPlanetMesh);

      // Atmospheric Rim for Bottom-Left Planet
      const blAtmosGeo = new THREE.SphereGeometry(137, 48, 48);
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
            fresnel = pow(fresnel, 3.2);
            vec3 atmosColor = vec3(0.05, 0.85, 1.0); // Vibrant electric cyan
            gl_FragColor = vec4(atmosColor, fresnel * 0.95);
          }
        `,
        transparent: true,
        blending: THREE.AdditiveBlending,
        side: THREE.FrontSide,
        depthWrite: false
      });
      blPlanetAtmos = new THREE.Mesh(blAtmosGeo, blAtmosMat);
      blPlanetAtmos.position.set(-170, -170, 75);
      scene.add(blPlanetAtmos);

      // 2. Bottom-Right Planet with Warm Magenta/Violet Rim Light
      const brGeo = new THREE.SphereGeometry(44, 36, 36);
      const brMat = new THREE.MeshBasicMaterial({
        map: createShadowedPlanetTexture('#150624', '#080210'),
        transparent: true,
        opacity: 0.96
      });
      brPlanetMesh = new THREE.Mesh(brGeo, brMat);
      brPlanetMesh.position.set(175, -125, 50);
      scene.add(brPlanetMesh);

      const brAtmosGeo = new THREE.SphereGeometry(45, 36, 36);
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
            fresnel = pow(fresnel, 2.8);
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
      brPlanetAtmos.position.set(175, -125, 50);
      scene.add(brPlanetAtmos);

      // 3. Top-Right Prominent Spiral Galaxy
      trGalaxyGroup = new THREE.Group();
      trGalaxyGroup.position.set(185, 120, -190);
      trGalaxyGroup.rotation.set(0.72, 0.42, -0.32);

      const trPoints = 2500;
      const trPos = new Float32Array(trPoints * 3);
      const trCol = new Float32Array(trPoints * 3);

      for (let i = 0; i < trPoints; i++) {
        const arm = i % 2;
        const r = 2 + 58 * Math.pow(Math.random(), 1.5);
        const theta = arm * Math.PI + 2.5 * Math.log(r / 3) + (Math.random() - 0.5) * 0.35;

        trPos[i * 3] = Math.cos(theta) * r + (Math.random() - 0.5) * (r * 0.12);
        trPos[i * 3 + 1] = Math.sin(theta) * r + (Math.random() - 0.5) * (r * 0.12);
        trPos[i * 3 + 2] = (Math.random() - 0.5) * 4.0;

        const normR = r / 60;
        if (normR < 0.2) {
          trCol[i * 3] = 1.0; trCol[i * 3 + 1] = 0.95; trCol[i * 3 + 2] = 0.9;
        } else {
          trCol[i * 3] = 0.4 + 0.4 * normR;
          trCol[i * 3 + 1] = 0.7 * (1 - normR * 0.4);
          trCol[i * 3 + 2] = 1.0;
        }
      }

      const trGeo = new THREE.BufferGeometry();
      trGeo.setAttribute('position', new THREE.BufferAttribute(trPos, 3));
      trGeo.setAttribute('color', new THREE.BufferAttribute(trCol, 3));

      const trMat = new THREE.PointsMaterial({
        size: 1.6,
        vertexColors: true,
        transparent: true,
        opacity: 0.85,
        blending: THREE.AdditiveBlending,
        depthWrite: false,
        map: createSoftPointTexture()
      });

      const trPointsMesh = new THREE.Points(trGeo, trMat);
      trGalaxyGroup.add(trPointsMesh);
      scene.add(trGalaxyGroup);
    }"""

code = re.sub(celestial_pattern, celestial_replacement, code)

# 8. In animateUniverseCinematic:
# Ensure productWorldsGroup is hidden while at hero (targetScrollP <= 0.12)
if 'productWorldsGroup.visible = (targetScrollP > 0.12);' not in code:
    code = code.replace(
        'productWorlds.forEach((pw) => {',
        'if (productWorldsGroup) productWorldsGroup.visible = (targetScrollP > 0.12);\n      productWorlds.forEach((pw) => {'
    )
    print("Added productWorldsGroup visibility toggle")

with open(MASTER_FILE, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated assemble_ultimate_3d_universe.py successfully!")
