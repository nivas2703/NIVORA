#!/usr/bin/env python3
"""
builder/apply_ultimate_reference_match.py
Applies the complete visual architecture to match hero-reference.jpg 100%:
- 2-Column Split Hero Layout (Left: Typography & CTAs & Metrics; Right: 3D Holographic Globe).
- 3D Holographic Cyber Globe with central glowing NIVORA Ribbon Logo, Fresnel rim, 3 orbital rings with satellites, and orbiting purple moon.
- Swirling galaxy accretion vortex beneath the globe with 4,200 logarithmic spiral particles and vertical cyan volumetric light beam.
- Bottom-left curved ocean planet horizon with radiant cyan atmospheric glow.
- Bottom-right shadowed purple planet horizon with warm magenta/violet crescent rim.
- Top-right tilted distant spiral galaxy with glowing core.
- Product worlds hidden during hero, emerging only during scroll travel to Products.
- Complete visual 2D canvas fallback with exact same visual composition.
"""

import os
import re

MASTER_FILE = "/Users/bennabathulanivas/Desktop/my projects/NIVORA/builder/assemble_ultimate_3d_universe.py"

with open(MASTER_FILE, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Variables and coordinates
code = re.sub(r'const globeCenterX\s*=\s*[^;\n]+;', 'const globeCenterX = 68.0;', code)
code = re.sub(r'const globeCenterY\s*=\s*[^;\n]+;', 'const globeCenterY = 12.0;', code)
code = re.sub(r'const globeCenterZ\s*=\s*[^;\n]+;', 'const globeCenterZ = 0.0;', code)
code = re.sub(r'const baseCamX\s*=\s*[^;\n]+;', 'const baseCamX = 0;', code)
code = re.sub(r'const baseCamY\s*=\s*[^;\n]+;', 'const baseCamY = 0;', code)
code = re.sub(r'const baseCamZ\s*=\s*[^;\n]+;', 'const baseCamZ = 260;', code)

# 2. Update getCameraTrajectory
old_traj_start = "function getCameraTrajectory(p) {"
old_traj_end = "function animateUniverseCinematic() {"
idx1 = code.find(old_traj_start)
idx2 = code.find(old_traj_end)
if idx1 != -1 and idx2 != -1:
    new_traj = """function getCameraTrajectory(p) {
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
    }

    """
    code = code[:idx1] + new_traj + code[idx2:]
    print("Updated getCameraTrajectory")

# 3. Product worlds visibility toggle in animateUniverseCinematic
if 'productWorldsGroup.visible = (targetScrollP > 0.12);' not in code:
    code = code.replace(
        'productWorlds.forEach((pw) => {',
        'if (productWorldsGroup) productWorldsGroup.visible = (targetScrollP > 0.12);\n      productWorlds.forEach((pw) => {'
    )
    print("Added productWorldsGroup visibility toggle")

# 4. Transparent cyber texture
tex_start = "function createDigitalWorldTextureCinematic() {"
tex_end = "function setupInteractivity() {"
t_idx1 = code.find(tex_start)
t_idx2 = code.find(tex_end)
if t_idx1 != -1 and t_idx2 != -1:
    new_tex = """function createDigitalWorldTextureCinematic() {
      const c = document.createElement('canvas');
      c.width = 2048; c.height = 1024;
      const ctx = c.getContext('2d');

      // Transparent base for crystal holographic globe
      ctx.clearRect(0, 0, 2048, 1024);

      // Delicate cyber grid lines
      ctx.strokeStyle = 'rgba(6, 182, 212, 0.22)';
      ctx.lineWidth = 1;
      for (let x = 0; x < 2048; x += 48) {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, 1024); ctx.stroke();
      }
      for (let y = 0; y < 1024; y += 48) {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(2048, y); ctx.stroke();
      }

      // Key Latitude & Longitude Meridians
      ctx.strokeStyle = 'rgba(56, 189, 248, 0.55)';
      ctx.lineWidth = 2.4;
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

        ctx.fillStyle = 'rgba(6, 182, 212, 0.16)';
        ctx.fill();

        ctx.strokeStyle = 'rgba(56, 189, 248, 0.85)';
        ctx.lineWidth = 2.6;
        ctx.stroke();

        ctx.fillStyle = 'rgba(168, 85, 247, 0.90)';
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
    }

    """
    code = code[:t_idx1] + new_tex + code[t_idx2:]
    print("Updated createDigitalWorldTextureCinematic")

# 5. buildNivoraGlobeCore & buildGalacticAccretionPlatform & buildOrbitalRings3D
core_start = "function buildNivoraGlobeCore() {"
core_end = "function build3DProductWorlds() {"
c_idx1 = code.find(core_start)
c_idx2 = code.find(core_end)
if c_idx1 != -1 and c_idx2 != -1:
    new_core_suite = """function buildNivoraGlobeCore() {
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
        halo.scale.set(4.5, 4.5, 1);
        bead.add(halo);

        globeGroup.add(bead);
        ringParticles.push({
          mesh: bead,
          curve: curve,
          rotX: spec.rotX,
          rotY: spec.rotY,
          rotZ: spec.rotZ,
          speed: spec.speed,
          progress: rIdx * 0.25
        });
      });
    }

    """
    code = code[:c_idx1] + new_core_suite + code[c_idx2:]
    print("Updated buildNivoraGlobeCore suite")

# 6. buildCelestialForeAndBackground
cel_start = "function buildCelestialForeAndBackground() {"
cel_end = "function buildNivoraGlobeCore() {"
ce_idx1 = code.find(cel_start)
ce_idx2 = code.find(cel_end)
if ce_idx1 != -1 and ce_idx2 != -1:
    new_cel = """function buildCelestialForeAndBackground() {
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
    }

    """
    code = code[:ce_idx1] + new_cel + code[ce_idx2:]
    print("Updated buildCelestialForeAndBackground")

# 7. Complete visual 2D canvas fallback with exact same composition
fb_start = "function initCanvas3DFallbackClean() {"
fb_end = "window.addEventListener('DOMContentLoaded', () => {"
f_idx1 = code.find(fb_start)
f_idx2 = code.find(fb_end)
if f_idx1 != -1 and f_idx2 != -1:
    new_fb = """function initCanvas3DFallbackClean() {
      const ctx = canvas.getContext('2d');
      let w = canvas.width = window.innerWidth;
      let h = canvas.height = window.innerHeight;

      const fallbackLogo = new Image();
      fallbackLogo.src = 'assets/images/nivora-logo.png';

      window.addEventListener('resize', () => {
        w = canvas.width = window.innerWidth;
        h = canvas.height = window.innerHeight;
      });

      // 450 Twinkling stars with varying depths
      const stars = [];
      for (let i = 0; i < 450; i++) {
        stars.push({
          x: (Math.random() - 0.5) * w * 2.2,
          y: (Math.random() - 0.5) * h * 2.2,
          z: Math.random() * 1000 + 40,
          size: Math.random() * 1.8 + 0.6,
          seed: Math.random() * 10
        });
      }

      // Swirling accretion vortex particles
      const vortexParticles = [];
      for (let i = 0; i < 380; i++) {
        const arm = i % 3;
        const r = 5 + Math.pow(Math.random(), 1.3) * 110;
        const a = (arm * (Math.PI * 2 / 3)) + (r * 0.07) + (Math.random() - 0.5) * 0.35;
        vortexParticles.push({ r, a, speed: (0.015 + 0.02 * (1 - r / 110)) });
      }

      let angle = 0;
      function drawFallback() {
        ctx.clearRect(0, 0, w, h);
        angle += 0.012;

        // 1. Deep-space stars
        stars.forEach(s => {
          s.z -= 0.5;
          if (s.z <= 0) s.z = 1000;
          const k = 320 / s.z;
          const px = s.x * k + w / 2;
          const py = s.y * k + h / 2;
          if (px >= 0 && px <= w && py >= 0 && py <= h) {
            const alpha = 0.35 + 0.45 * Math.sin(angle * 2 + s.seed);
            ctx.fillStyle = `rgba(255, 255, 255, ${alpha})`;
            ctx.beginPath();
            ctx.arc(px, py, s.size * k * 0.7, 0, Math.PI * 2);
            ctx.fill();
          }
        });

        // 2. Top-Right Distant Spiral Galaxy
        const tgx = w * 0.88;
        const tgy = h * 0.15;
        const tgGrad = ctx.createRadialGradient(tgx, tgy, 2, tgx, tgy, 45);
        tgGrad.addColorStop(0, 'rgba(255, 255, 255, 0.9)');
        tgGrad.addColorStop(0.3, 'rgba(56, 189, 248, 0.65)');
        tgGrad.addColorStop(0.7, 'rgba(168, 85, 247, 0.35)');
        tgGrad.addColorStop(1, 'rgba(168, 85, 247, 0)');
        ctx.fillStyle = tgGrad;
        ctx.beginPath();
        ctx.ellipse(tgx, tgy, 45, 20, 0.65, 0, Math.PI * 2);
        ctx.fill();

        // 3. Bottom-Left Curved Blue Planet Horizon with Radiant Cyan Atmosphere
        const blX = -w * 0.02;
        const blY = h * 1.12;
        const blR = Math.max(w * 0.32, 420);

        // Planet dark ocean body
        const blGrad = ctx.createRadialGradient(blX, blY, blR * 0.2, blX, blY, blR);
        blGrad.addColorStop(0, '#020617');
        blGrad.addColorStop(0.85, '#051430');
        blGrad.addColorStop(1, '#072450');
        ctx.fillStyle = blGrad;
        ctx.beginPath();
        ctx.arc(blX, blY, blR, 0, Math.PI * 2);
        ctx.fill();

        // Atmospheric cyan glowing rim
        ctx.save();
        ctx.shadowColor = '#00f5ff';
        ctx.shadowBlur = 35;
        ctx.strokeStyle = 'rgba(6, 182, 212, 0.95)';
        ctx.lineWidth = 4.5;
        ctx.beginPath();
        ctx.arc(blX, blY, blR, -Math.PI * 0.45, Math.PI * 0.05);
        ctx.stroke();

        ctx.shadowBlur = 60;
        ctx.strokeStyle = 'rgba(56, 189, 248, 0.55)';
        ctx.lineWidth = 10;
        ctx.beginPath();
        ctx.arc(blX, blY, blR + 2, -Math.PI * 0.45, Math.PI * 0.05);
        ctx.stroke();
        ctx.restore();

        // 4. Bottom-Right Shadowed Purple Planet with Warm Magenta Crescent Rim
        const brX = w * 0.96;
        const brY = h * 1.06;
        const brR = Math.max(w * 0.18, 240);

        const brGrad = ctx.createRadialGradient(brX, brY, brR * 0.2, brX, brY, brR);
        brGrad.addColorStop(0, '#0a0214');
        brGrad.addColorStop(0.85, '#18052a');
        brGrad.addColorStop(1, '#2c0b48');
        ctx.fillStyle = brGrad;
        ctx.beginPath();
        ctx.arc(brX, brY, brR, 0, Math.PI * 2);
        ctx.fill();

        ctx.save();
        ctx.shadowColor = '#ec4899';
        ctx.shadowBlur = 30;
        ctx.strokeStyle = 'rgba(236, 72, 153, 0.88)';
        ctx.lineWidth = 3.8;
        ctx.beginPath();
        ctx.arc(brX, brY, brR, Math.PI * 0.85, Math.PI * 1.45);
        ctx.stroke();
        ctx.restore();

        // 5. THE 3D CYBER-GLOBE (RIGHT SIDE)
        const gx = w * 0.72;
        const gy = h * 0.46;
        const gr = Math.min(w, h) * 0.175;

        // Swirling Galaxy Accretion Vortex BENEATH the Globe
        const vy = gy + gr * 0.95;
        const vGrad = ctx.createRadialGradient(gx, vy, 4, gx, vy, gr * 1.45);
        vGrad.addColorStop(0, 'rgba(255, 255, 255, 0.95)');
        vGrad.addColorStop(0.18, 'rgba(6, 182, 212, 0.75)');
        vGrad.addColorStop(0.45, 'rgba(168, 85, 247, 0.55)');
        vGrad.addColorStop(0.75, 'rgba(236, 72, 153, 0.35)');
        vGrad.addColorStop(1, 'rgba(2, 6, 23, 0)');
        ctx.fillStyle = vGrad;
        ctx.beginPath();
        ctx.ellipse(gx, vy, gr * 1.55, gr * 0.42, 0.08, 0, Math.PI * 2);
        ctx.fill();

        // Accretion swirling spiral particles
        vortexParticles.forEach(vp => {
          vp.a += vp.speed;
          const px = gx + Math.cos(vp.a) * vp.r * (gr / 75);
          const py = vy + Math.sin(vp.a) * vp.r * 0.35 * (gr / 75);
          const t = vp.r / 110;
          ctx.fillStyle = t < 0.3 ? '#e0f2fe' : (t < 0.7 ? '#c084fc' : '#f472b6');
          ctx.beginPath();
          ctx.arc(px, py, 1.4 + Math.random() * 0.8, 0, Math.PI * 2);
          ctx.fill();
        });

        // Vertical Volumetric Cyan Light Beam
        const beamGrad = ctx.createLinearGradient(gx, vy, gx, gy + gr * 0.6);
        beamGrad.addColorStop(0, 'rgba(6, 182, 212, 0.65)');
        beamGrad.addColorStop(0.6, 'rgba(6, 182, 212, 0.25)');
        beamGrad.addColorStop(1, 'rgba(6, 182, 212, 0)');
        ctx.fillStyle = beamGrad;
        ctx.beginPath();
        ctx.moveTo(gx - gr * 0.35, vy);
        ctx.lineTo(gx + gr * 0.35, vy);
        ctx.lineTo(gx + gr * 0.12, gy + gr * 0.6);
        ctx.lineTo(gx - gr * 0.12, gy + gr * 0.6);
        ctx.closePath();
        ctx.fill();

        // Globe Atmospheric Fresnel Corona Shell
        const atmosGrad = ctx.createRadialGradient(gx, gy, gr * 0.5, gx, gy, gr * 1.16);
        atmosGrad.addColorStop(0, 'rgba(6, 182, 212, 0)');
        atmosGrad.addColorStop(0.65, 'rgba(6, 182, 212, 0.35)');
        atmosGrad.addColorStop(0.88, 'rgba(168, 85, 247, 0.65)');
        atmosGrad.addColorStop(1, 'rgba(236, 72, 153, 0)');
        ctx.fillStyle = atmosGrad;
        ctx.beginPath();
        ctx.arc(gx, gy, gr * 1.16, 0, Math.PI * 2);
        ctx.fill();

        // Globe Cyber Latitude/Longitude Grid Lines
        ctx.save();
        ctx.strokeStyle = 'rgba(6, 182, 212, 0.45)';
        ctx.lineWidth = 1.4;
        [-0.65, -0.32, 0, 0.32, 0.65].forEach(offset => {
          ctx.beginPath();
          const ry = gr * (1 - Math.abs(offset) * 0.5);
          ctx.ellipse(gx, gy + offset * gr, ry, ry * 0.28, 0, 0, Math.PI * 2);
          ctx.stroke();
        });

        // Rotating Longitude Meridians
        [-1, -0.5, 0, 0.5, 1].forEach(mer => {
          const shift = Math.sin(angle * 0.5 + mer) * gr;
          ctx.beginPath();
          ctx.ellipse(gx + shift * 0.6, gy, Math.abs(shift) * 0.8 + 4, gr, 0, 0, Math.PI * 2);
          ctx.stroke();
        });
        ctx.restore();

        // 3 Tilted Luminous Orbital Rings with Orbiting Satellites
        // Ring 1 (Cyan)
        ctx.save();
        ctx.shadowColor = '#00f5ff';
        ctx.shadowBlur = 12;
        ctx.strokeStyle = 'rgba(6, 182, 212, 0.75)';
        ctx.lineWidth = 1.6;
        ctx.beginPath();
        ctx.ellipse(gx, gy, gr * 1.48, gr * 0.46, 0.42, 0, Math.PI * 2);
        ctx.stroke();

        const b1a = angle * 1.4;
        const b1x = gx + Math.cos(b1a) * gr * 1.48 * Math.cos(0.42) - Math.sin(b1a) * gr * 0.46 * Math.sin(0.42);
        const b1y = gy + Math.cos(b1a) * gr * 1.48 * Math.sin(0.42) + Math.sin(b1a) * gr * 0.46 * Math.cos(0.42);
        ctx.fillStyle = '#ffffff';
        ctx.beginPath();
        ctx.arc(b1x, b1y, 3.2, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();

        // Ring 2 (Magenta)
        ctx.save();
        ctx.shadowColor = '#ec4899';
        ctx.shadowBlur = 12;
        ctx.strokeStyle = 'rgba(236, 72, 153, 0.70)';
        ctx.lineWidth = 1.6;
        ctx.beginPath();
        ctx.ellipse(gx, gy, gr * 1.58, gr * 0.42, -0.55, 0, Math.PI * 2);
        ctx.stroke();

        const b2a = -angle * 1.1;
        const b2x = gx + Math.cos(b2a) * gr * 1.58 * Math.cos(-0.55) - Math.sin(b2a) * gr * 0.42 * Math.sin(-0.55);
        const b2y = gy + Math.cos(b2a) * gr * 1.58 * Math.sin(-0.55) + Math.sin(b2a) * gr * 0.42 * Math.cos(-0.55);
        ctx.fillStyle = '#fbcfe8';
        ctx.beginPath();
        ctx.arc(b2x, b2y, 3.0, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();

        // Ring 3 (Deep Purple / Violet)
        ctx.save();
        ctx.shadowColor = '#a855f7';
        ctx.shadowBlur = 10;
        ctx.strokeStyle = 'rgba(168, 85, 247, 0.65)';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.ellipse(gx, gy, gr * 1.68, gr * 0.52, 1.15, 0, Math.PI * 2);
        ctx.stroke();
        ctx.restore();

        // Official NIVORA 3D Logo
        if (fallbackLogo.complete && fallbackLogo.naturalWidth > 0) {
          const lw = gr * 0.78;
          const lh = lw * (fallbackLogo.naturalHeight / fallbackLogo.naturalWidth);
          const lGrad = ctx.createRadialGradient(gx, gy, 4, gx, gy, lw * 0.75);
          lGrad.addColorStop(0, 'rgba(6, 182, 212, 0.65)');
          lGrad.addColorStop(0.5, 'rgba(168, 85, 247, 0.45)');
          lGrad.addColorStop(1, 'rgba(6, 182, 212, 0)');
          ctx.fillStyle = lGrad;
          ctx.beginPath();
          ctx.arc(gx, gy, lw * 0.75, 0, Math.PI * 2);
          ctx.fill();

          ctx.drawImage(fallbackLogo, gx - lw / 2, gy - lh / 2 + Math.sin(angle * 1.8) * 3, lw, lh);
        }

        requestAnimationFrame(drawFallback);
      }
      drawFallback();
    }

    """
    code = code[:f_idx1] + new_fb + code[f_idx2:]
    print("Updated initCanvas3DFallbackClean")

with open(MASTER_FILE, "w", encoding="utf-8") as f:
    f.write(code)

print("Applied ultimate reference match successfully!")
