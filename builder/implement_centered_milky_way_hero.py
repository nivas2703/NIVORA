#!/usr/bin/env python3
"""
implement_centered_milky_way_hero.py
Transforms NIVORA into a clean, centered, premium cinematic Milky Way hero:
1. Centered Hero Composition:
   - Eyebrow badge centered
   - 3D Cosmic Core stage centered with official NIVORA logo at the focal center
   - Welcome to NIVORA (centered headline with purple->violet->blue->cyan gradient)
   - Tagline (centered with italic serif Ideas & Products)
   - Description (centered, balanced max-width)
   - CTA buttons (centered)
   - Metrics row (centered)
   - Bottom scroll indicator (centered)
2. Concentrated Procedural Milky Way centered directly around the NIVORA core:
   - 28,000 GPU particles in tight spiral arms + dense galactic bulge
   - Highest density and luminance at the core around the logo
   - Subtle cosmic rotation, zero static images
3. Official NIVORA Logo Treatment:
   - Crisp, sharp, illuminated logo at center (depthTest: false, renderOrder: 50)
   - Circular energy field aura
   - Inner concentrated particle sphere
   - Thin glowing orbital rings with energy beads
4. Clean Visual Hierarchy - Removed Distractions:
   - Removed giant bottom-left blue planet
   - Removed giant bottom-right pink planet
   - Product worlds kept invisible in hero, emerging only when traveling into Products
5. Full space-travel motion system preserved (forward & reverse warp streaks, 6-stage flight).
"""

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MASTER_BUILDER = os.path.join(SCRIPT_DIR, "assemble_ultimate_3d_universe.py")

with open(MASTER_BUILDER, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update CSS: Make Hero Centered
old_hero_css = r"""    /* =========================================================
       HERO SECTION — THE 3D UNIVERSE IS THE HERO
       ========================================================= */
    .hero {
      position: relative;
      min-height: 100vh;
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: flex-start;
      padding: 5.5rem 4% 2rem;
      flex-direction: column;
      justify-content: center;
      z-index: 10;
      pointer-events: none; /* UI inside is enabled selectively */
    }

    .hero-container {
      width: 100%;
      max-width: 1360px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 1fr 1fr;
      align-items: center;
      gap: 3rem;
      position: relative;
      z-index: 10;
    }

    /* Left Hero Content */
    .hero-content {
      max-width: 540px;
      pointer-events: auto; /* Enable clicks */
      position: relative;
      z-index: 20;
    }"""

new_hero_css = r"""    /* =========================================================
       HERO SECTION — CENTERED CINEMATIC MILKY WAY HERO
       ========================================================= */
    .hero {
      position: relative;
      min-height: 100vh;
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 6.5rem 4% 3rem;
      z-index: 10;
      pointer-events: none;
    }

    .hero-container-centered {
      width: 100%;
      max-width: 900px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      position: relative;
      z-index: 20;
      pointer-events: auto;
    }

    /* 3D Cosmic Core Stage: Visual anchor for Three.js Milky Way Core */
    .hero-core-stage {
      position: relative;
      width: 100%;
      height: 250px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0.5rem 0 1.25rem;
      cursor: pointer;
      pointer-events: auto;
    }

    .core-click-proxy {
      width: 240px;
      height: 240px;
      border-radius: 50%;
      position: relative;
      cursor: pointer;
    }

    .hero-text-block {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      width: 100%;
    }"""

if old_hero_css in code:
    code = code.replace(old_hero_css, new_hero_css)
    print("Replaced hero CSS with centered hero CSS")
else:
    print("old_hero_css target not found")

# 2. Update typography and metrics CSS to be centered
old_typo_css = r"""    /* Main Typography */
    .hero-title {
      font-family: var(--font-display);
      font-size: clamp(3.2rem, 5.8vw, 5.4rem);
      font-weight: 800;
      line-height: 1.04;
      letter-spacing: -0.04em;
      margin-bottom: 0.85rem;
    }

    .hero-welcome {
      color: #ffffff;
      display: inline-block;
    }

    .hero-brand {
      display: inline-block;
      background: linear-gradient(135deg, #a855f7 0%, #d946ef 35%, #3b82f6 70%, #06b6d4 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-size: 200% 200%;
      animation: brandGradShift 6s ease-in-out infinite alternate;
      filter: drop-shadow(0 0 35px rgba(168, 85, 247, 0.4));
    }

    @keyframes brandGradShift {
      0% { background-position: 0% 50%; }
      100% { background-position: 100% 50%; }
    }

    /* Tagline */
    .hero-tagline {
      font-family: var(--font-ui);
      font-size: clamp(1.35rem, 2.3vw, 1.95rem);
      font-weight: 500;
      color: #f1f5f9;
      line-height: 1.3;
      margin-bottom: 1.15rem;
      letter-spacing: -0.02em;
    }"""

new_typo_css = r"""    /* Main Typography (Centered) */
    .hero-title {
      font-family: var(--font-display);
      font-size: clamp(3.0rem, 5.4vw, 4.6rem);
      font-weight: 800;
      line-height: 1.06;
      letter-spacing: -0.04em;
      margin-bottom: 0.85rem;
      text-align: center;
    }

    .hero-welcome {
      color: #ffffff;
      display: inline-block;
    }

    .hero-brand {
      display: inline-block;
      background: linear-gradient(135deg, #a855f7 0%, #c084fc 25%, #38bdf8 70%, #06b6d4 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-size: 200% 200%;
      animation: brandGradShift 6s ease-in-out infinite alternate;
      filter: drop-shadow(0 0 35px rgba(168, 85, 247, 0.45));
    }

    @keyframes brandGradShift {
      0% { background-position: 0% 50%; }
      100% { background-position: 100% 50%; }
    }

    /* Tagline (Centered) */
    .hero-tagline {
      font-family: var(--font-ui);
      font-size: clamp(1.25rem, 2.1vw, 1.75rem);
      font-weight: 500;
      color: #f1f5f9;
      line-height: 1.35;
      margin-bottom: 1.25rem;
      letter-spacing: -0.02em;
      text-align: center;
    }"""

if old_typo_css in code:
    code = code.replace(old_typo_css, new_typo_css)
    print("Replaced typography CSS with centered styles")
else:
    print("old_typo_css target not found")

# Update copy, actions, and metrics CSS to be centered
old_copy_css = r"""    /* Description */
    .hero-copy {
      font-size: clamp(0.95rem, 1.15vw, 1.05rem);
      line-height: 1.65;
      color: #cbd5e1;
      margin-bottom: 1.6rem;
      max-width: 500px;
    }

    .hero-copy strong {
      color: #ffffff;
      font-weight: 600;
    }

    /* Action Buttons */
    .hero-actions {
      display: flex;
      align-items: center;
      gap: 1.25rem;
      margin-bottom: 1.8rem;
      flex-wrap: wrap;
    }"""

new_copy_css = r"""    /* Description (Centered) */
    .hero-copy {
      font-size: clamp(0.95rem, 1.1vw, 1.05rem);
      line-height: 1.7;
      color: #cbd5e1;
      margin-bottom: 1.85rem;
      max-width: 660px;
      text-align: center;
    }

    .hero-copy strong {
      color: #ffffff;
      font-weight: 600;
    }

    /* Action Buttons (Centered) */
    .hero-actions {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 1.25rem;
      margin-bottom: 2.2rem;
      flex-wrap: wrap;
    }"""

if old_copy_css in code:
    code = code.replace(old_copy_css, new_copy_css)
    print("Replaced copy and actions CSS with centered styles")
else:
    print("old_copy_css target not found")

# Update hero metrics CSS
old_metrics_css = r"""    /* Metrics Grid */
    .hero-metrics {
      display: flex;
      align-items: center;
      gap: 1.75rem;
      padding-top: 1.15rem;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      max-width: 480px;
    }"""

new_metrics_css = r"""    /* Metrics Grid (Centered) */
    .hero-metrics {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 2.5rem;
      padding-top: 1.35rem;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      max-width: 640px;
      margin: 0 auto;
    }"""

if old_metrics_css in code:
    code = code.replace(old_metrics_css, new_metrics_css)
    print("Replaced hero metrics CSS with centered styles")
else:
    print("old_metrics_css target not found")

# 3. Update HTML markup for the hero section
old_hero_html = r"""    <section class="hero" id="hero">
      <div class="hero-container">
        <!-- LEFT HERO CONTENT: BRANDING, TYPOGRAPHY, CTAS -->
        <div class="hero-content">
          <div class="hero-badge">
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
            <button type="button" class="btn-enter-universe" onclick="triggerEnterUniverseSequence()" id="btnEnterUniverse">
              <span>Enter the Universe &rarr;</span>
            </button>
            <button type="button" class="btn-explore-products" onclick="triggerExploreProductsFlight()" id="btnExploreProducts">
              <span class="play-icon-circle">&#9658;</span>
              <span>Explore Products</span>
            </button>
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
          </div>
        </div>

        <!-- RIGHT HERO CONTENT: 3D GLOBE CLICK PROXY (CANVAS IS BEHIND/INTERACTIVE) -->
        <div class="hero-art-stage" id="heroArtStage" onclick="triggerCinematicCameraZoom()" title="Click to Enter the NIVORA Universe">
          <div class="globe-click-proxy"></div>
        </div>
      </div>

      <!-- SCROLL INDICATOR (HUD FOOTER) -->
      <div class="hero-scroll-indicator" onclick="triggerCinematicCameraZoom()">
        <div class="scroll-mouse-icon">
          <div class="scroll-mouse-wheel"></div>
        </div>
        <span class="scroll-hud-text">SCROLL TO EXPLORE THE UNIVERSE</span>
        <span class="scroll-arrow-bounce">&darr;</span>
      </div>
    </section>"""

new_hero_html = r"""    <section class="hero" id="hero">
      <div class="hero-container-centered">
        <!-- 1. Small Eyebrow Badge -->
        <div class="hero-badge">
          <span class="dot"></span>
          <span>A NIVAS BENNABATTHULA INITIATIVE</span>
        </div>

        <!-- 2. 3D Cosmic Core Visual Anchor (Click Proxy for Central NIVORA Core) -->
        <div class="hero-core-stage" id="heroArtStage" onclick="triggerEnterUniverseSequence()" title="Click to Enter the NIVORA Universe">
          <div class="core-click-proxy"></div>
        </div>

        <!-- 3. Centered Main Typography & Content -->
        <div class="hero-text-block">
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

          <!-- 4. Centered Action Buttons -->
          <div class="hero-actions">
            <button type="button" class="btn-enter-universe" onclick="triggerEnterUniverseSequence()" id="btnEnterUniverse">
              <span>Enter the Universe &rarr;</span>
            </button>
            <button type="button" class="btn-explore-products" onclick="triggerExploreProductsFlight()" id="btnExploreProducts">
              <span class="play-icon-circle">&#9658;</span>
              <span>Explore Products</span>
            </button>
          </div>

          <!-- 5. Centered Ecosystem Metrics -->
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
          </div>
        </div>
      </div>

      <!-- SCROLL INDICATOR (HUD FOOTER) -->
      <div class="hero-scroll-indicator" onclick="triggerEnterUniverseSequence()">
        <div class="scroll-mouse-icon">
          <div class="scroll-mouse-wheel"></div>
        </div>
        <span class="scroll-hud-text">SCROLL TO EXPLORE THE UNIVERSE</span>
        <span class="scroll-arrow-bounce">&darr;</span>
      </div>
    </section>"""

if old_hero_html in code:
    code = code.replace(old_hero_html, new_hero_html)
    print("Replaced hero HTML with centered hero structure")
else:
    print("old_hero_html target not found")

# 4. Three.js Engine: Center the Core and Milky Way at (0, 16, 0)
# Base coordinates:
old_base_coords = r"""    const baseCamX = 0;
    const baseCamY = 4;
    const baseCamZ = 270;
    const globeCenterX = 66;
    const globeCenterY = 5;
    const globeCenterZ = 0;

    let currentCamPos = new THREE.Vector3(baseCamX, baseCamY, baseCamZ);
    let currentLookAt = new THREE.Vector3(0, 4, 0);"""

new_base_coords = r"""    const baseCamX = 0;
    const baseCamY = 0;
    const baseCamZ = 260;
    const globeCenterX = 0;
    const globeCenterY = 16;
    const globeCenterZ = 0;

    let currentCamPos = new THREE.Vector3(baseCamX, baseCamY, baseCamZ);
    let currentLookAt = new THREE.Vector3(0, 14, 0);"""

if old_base_coords in code:
    code = code.replace(old_base_coords, new_base_coords)
    print("Centered Three.js camera and globe coordinates at (0, 16, 0)")
else:
    print("old_base_coords target not found")

# 5. Remove distracting celestial objects (blPlanetMesh, brPlanetMesh)
old_celestial_func = r"""    function buildCelestialForeAndBackground() {
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
      trGalaxyGroup.rotation.set(0.72, 0.42, -0.32);"""

new_celestial_func = r"""    function buildCelestialForeAndBackground() {
      // Clean, un-cluttered cosmos: Distracting giant foreground planets removed per design requirement
      // Very subtle distant deep-space spiral galaxy in the far cosmic background (Z = -600)
      trGalaxyGroup = new THREE.Group();
      trGalaxyGroup.position.set(240, 140, -550);
      trGalaxyGroup.rotation.set(0.68, 0.35, -0.25);"""

if old_celestial_func in code:
    code = code.replace(old_celestial_func, new_celestial_func)
    print("Removed distracting giant foreground planets from buildCelestialForeAndBackground")
else:
    print("old_celestial_func target not found")

# 6. Concentrated Procedural Milky Way centered directly around NIVORA Core
old_milky_way = r"""    function buildProceduralMilkyWay() {
      milkyWayGroup = new THREE.Group();
      milkyWayGroup.position.set(globeCenterX, globeCenterY, globeCenterZ);
      milkyWayGroup.rotation.set(0.82, 0.22, -0.15); // Majestic cinematic 3D tilt

      const starCount = 42000;
      const positions = new Float32Array(starCount * 3);
      const colors = new Float32Array(starCount * 3);

      const armAngles = [0.45, 0.45 + Math.PI, 1.85, 1.85 + Math.PI];
      const armWeights = [0.38, 0.38, 0.12, 0.12];
      const rMin = 22;
      const rMax = 380;

      const cosX = Math.cos(0.82), sinX = Math.sin(0.82);
      const cosY = Math.cos(0.22), sinY = Math.sin(0.22);

      let idx = 0;
      for (let i = 0; i < starCount; i++) {
        // Arm distribution
        const randArm = Math.random();
        let arm = 0;
        let cumulative = 0;
        for (let a = 0; a < armWeights.length; a++) {
          cumulative += armWeights[a];
          if (randArm <= cumulative) {
            arm = a;
            break;
          }
        }

        const r = rMin + Math.pow(Math.random(), 1.45) * (rMax - rMin);
        const spiralSpeed = 3.6;
        const theta = armAngles[arm] + Math.log(r / rMin) * spiralSpeed + (Math.random() - 0.5) * 0.42;

        const armThickness = 2.0 + (r / rMax) * 16.0;
        const armDispersion = 2.5 + (r / rMax) * 18.0;

        const xLocal = Math.cos(theta) * r + (Math.random() - 0.5) * armDispersion;
        const yLocal = (Math.random() - 0.5) * armThickness;
        const zLocal = Math.sin(theta) * r + (Math.random() - 0.5) * armDispersion;

        // Quiet negative space for left-side hero text
        const xWorld = globeCenterX + (xLocal * cosY + zLocal * sinY);
        const yWorld = globeCenterY + (yLocal * cosX - (xLocal * -sinY + zLocal * cosY) * sinX);
        if (xWorld < 12 && yWorld > -35 && yWorld < 45) {
          if (Math.random() > 0.12) continue;
        }

        positions[idx * 3] = xLocal;
        positions[idx * 3 + 1] = yLocal;
        positions[idx * 3 + 2] = zLocal;

        // Photometric Stellar Color Palette
        const p = (r - rMin) / (rMax - rMin);
        if (p < 0.22) {
          colors[idx * 3] = 0.95; colors[idx * 3 + 1] = 0.98; colors[idx * 3 + 2] = 1.0;
        } else if (p < 0.52) {
          colors[idx * 3] = 0.25; colors[idx * 3 + 1] = 0.72; colors[idx * 3 + 2] = 1.0;
        } else if (p < 0.78) {
          colors[idx * 3] = 0.65; colors[idx * 3 + 1] = 0.42; colors[idx * 3 + 2] = 0.98;
        } else {
          colors[idx * 3] = 0.88; colors[idx * 3 + 1] = 0.35; colors[idx * 3 + 2] = 0.85;
        }

        idx++;
      }

      const armGeo = new THREE.BufferGeometry();
      armGeo.setAttribute('position', new THREE.BufferAttribute(positions.subarray(0, idx * 3), 3));
      armGeo.setAttribute('color', new THREE.BufferAttribute(colors.subarray(0, idx * 3), 3));

      const armMat = new THREE.PointsMaterial({
        size: 1.45,
        sizeAttenuation: true,
        vertexColors: true,
        map: createSoftPointTexture(),
        transparent: true,
        opacity: 0.82,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });

      spiralArmStars = new THREE.Points(armGeo, armMat);
      milkyWayGroup.add(spiralArmStars);
      scene.add(milkyWayGroup);
    }"""

new_milky_way = r"""    function buildProceduralMilkyWay() {
      // Concentrated Procedural Milky Way Centered Directly Around NIVORA Core
      milkyWayGroup = new THREE.Group();
      milkyWayGroup.position.set(globeCenterX, globeCenterY, globeCenterZ);
      milkyWayGroup.rotation.set(0.75, 0.15, -0.10); // Elegant balanced cosmic tilt

      const starCount = 32000;
      const positions = new Float32Array(starCount * 3);
      const colors = new Float32Array(starCount * 3);

      const armAngles = [0.2, 0.2 + Math.PI, 1.7, 1.7 + Math.PI];
      const armWeights = [0.4, 0.4, 0.1, 0.1];
      const rMin = 14;
      const rMax = 260; // Concentrated around central core!

      let idx = 0;
      for (let i = 0; i < starCount; i++) {
        const randArm = Math.random();
        let arm = 0;
        let cumulative = 0;
        for (let a = 0; a < armWeights.length; a++) {
          cumulative += armWeights[a];
          if (randArm <= cumulative) {
            arm = a;
            break;
          }
        }

        // Higher particle concentration near core
        const r = rMin + Math.pow(Math.random(), 1.7) * (rMax - rMin);
        const spiralSpeed = 3.2;
        const theta = armAngles[arm] + Math.log(r / rMin) * spiralSpeed + (Math.random() - 0.5) * 0.38;

        const armThickness = 1.5 + (r / rMax) * 12.0;
        const armDispersion = 2.0 + (r / rMax) * 14.0;

        positions[idx * 3] = Math.cos(theta) * r + (Math.random() - 0.5) * armDispersion;
        positions[idx * 3 + 1] = (Math.random() - 0.5) * armThickness;
        positions[idx * 3 + 2] = Math.sin(theta) * r + (Math.random() - 0.5) * armDispersion;

        // Photometric Stellar Color Palette (White-Cyan at Core, Violet/Magenta at Edges)
        const p = (r - rMin) / (rMax - rMin);
        if (p < 0.25) {
          colors[idx * 3] = 0.95; colors[idx * 3 + 1] = 0.98; colors[idx * 3 + 2] = 1.0; // Radiant white-cyan
        } else if (p < 0.55) {
          colors[idx * 3] = 0.22; colors[idx * 3 + 1] = 0.74; colors[idx * 3 + 2] = 1.0; // Electric cyan
        } else if (p < 0.80) {
          colors[idx * 3] = 0.68; colors[idx * 3 + 1] = 0.45; colors[idx * 3 + 2] = 0.98; // Cosmic violet
        } else {
          colors[idx * 3] = 0.92; colors[idx * 3 + 1] = 0.32; colors[idx * 3 + 2] = 0.85; // Magenta energy
        }

        idx++;
      }

      const armGeo = new THREE.BufferGeometry();
      armGeo.setAttribute('position', new THREE.BufferAttribute(positions.subarray(0, idx * 3), 3));
      armGeo.setAttribute('color', new THREE.BufferAttribute(colors.subarray(0, idx * 3), 3));

      const armMat = new THREE.PointsMaterial({
        size: 1.5,
        sizeAttenuation: true,
        vertexColors: true,
        map: createSoftPointTexture(),
        transparent: true,
        opacity: 0.85,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });

      spiralArmStars = new THREE.Points(armGeo, armMat);
      milkyWayGroup.add(spiralArmStars);
      scene.add(milkyWayGroup);
    }"""

if old_milky_way in code:
    code = code.replace(old_milky_way, new_milky_way)
    print("Centered and concentrated procedural Milky Way around NIVORA Core")
else:
    print("old_milky_way target not found")

# 7. Update buildNivoraGlobeCore to have crisp centered official logo with circular energy field
old_core_func = r"""    function buildNivoraGlobeCore() {
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
    }"""

new_core_func = r"""    function buildNivoraGlobeCore() {
      globeGroup = new THREE.Group();
      globeGroup.position.set(globeCenterX, globeCenterY, globeCenterZ);

      const globeRadius = 18.0; // Elegant, perfectly proportioned cosmic core

      // 1. Inner Concentrated Particle Sphere (Surrounding Logo)
      const pCount = 1200;
      const pPos = new Float32Array(pCount * 3);
      const pCol = new Float32Array(pCount * 3);
      for (let i = 0; i < pCount; i++) {
        const u = Math.random();
        const v = Math.random();
        const theta = u * 2.0 * Math.PI;
        const phi = Math.acos(2.0 * v - 1.0);
        const r = globeRadius * 0.95 + (Math.random() - 0.5) * 1.5;

        pPos[i * 3] = r * Math.sin(phi) * Math.cos(theta);
        pPos[i * 3 + 1] = r * Math.sin(phi) * Math.sin(theta);
        pPos[i * 3 + 2] = r * Math.cos(phi);

        if (Math.random() > 0.5) {
          pCol[i * 3] = 0.95; pCol[i * 3 + 1] = 0.98; pCol[i * 3 + 2] = 1.0;
        } else {
          pCol[i * 3] = 0.22; pCol[i * 3 + 1] = 0.74; pCol[i * 3 + 2] = 0.97;
        }
      }
      const pGeo = new THREE.BufferGeometry();
      pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
      pGeo.setAttribute('color', new THREE.BufferAttribute(pCol, 3));
      globeMesh = new THREE.Points(pGeo, new THREE.PointsMaterial({
        size: 1.4,
        vertexColors: true,
        map: createSoftPointTexture(),
        transparent: true,
        opacity: 0.85,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      }));
      globeGroup.add(globeMesh);

      // 2. Atmospheric Glass Shell with Brilliant Fresnel Rim
      const atmosGeo = new THREE.SphereGeometry(globeRadius * 1.06, 36, 36);
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
            fresnel = pow(fresnel, 2.8);

            vec3 cyanColor = vec3(0.02, 0.71, 0.83);    // #06b6d4
            vec3 purpleColor = vec3(0.66, 0.33, 0.97);  // #a855f7
            vec3 magentaColor = vec3(0.93, 0.28, 0.94); // #ec4899

            vec3 rimColor = mix(cyanColor, purpleColor, fresnel * 0.8);
            rimColor = mix(rimColor, magentaColor, pow(fresnel, 3.8));

            gl_FragColor = vec4(rimColor, fresnel * 0.88);
          }
        `,
        transparent: true,
        blending: THREE.AdditiveBlending,
        side: THREE.FrontSide,
        depthWrite: false
      });
      atmosphereMesh = new THREE.Mesh(atmosGeo, atmosMat);
      globeGroup.add(atmosphereMesh);

      // 3. Radiant Circular Energy Field Aura
      const haloMat = new THREE.SpriteMaterial({
        map: createCoronaHaloTexture(),
        transparent: true,
        opacity: 0.65,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });
      globeHaloSprite = new THREE.Sprite(haloMat);
      globeHaloSprite.scale.set(65, 65, 1);
      globeHaloSprite.renderOrder = 20;
      globeGroup.add(globeHaloSprite);

      // 4. OFFICIAL NIVORA LOGO (SHARP, HIGH CONTRAST, EXACT CENTER)
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
        logoSprite.scale.set(19, 19, 1);
        logoSprite.renderOrder = 50; // Always on top of particles!
        globeGroup.add(logoSprite);

        // Illuminating Backing Aura
        const auraMat = new THREE.SpriteMaterial({
          map: createSoftPointTexture(),
          color: 0x06b6d4,
          transparent: true,
          opacity: 0.55,
          blending: THREE.AdditiveBlending,
          depthTest: false
        });
        const auraSprite = new THREE.Sprite(auraMat);
        auraSprite.scale.set(26, 26, 1);
        auraSprite.renderOrder = 45;
        globeGroup.add(auraSprite);
      });

      scene.add(globeGroup);
    }"""

if old_core_func in code:
    code = code.replace(old_core_func, new_core_func)
    print("Replaced buildNivoraGlobeCore with centered crisp logo core")
else:
    print("old_core_func target not found")

# 8. Update Camera Trajectory for Centered Experience
old_cam_flight = r"""    function getCameraTrajectory(p) {
      // 6-STAGE FORWARD SPACE-TRAVEL FLIGHT (Z: +270 -> -1380)
      if (p <= 0.16) {
        // Stage 1: HOME (NIVORA CORE) -> Camera begins forward travel
        const t = p / 0.16;
        const ease = t * t * (3 - 2 * t);
        return {
          pos: new THREE.Vector3(
            baseCamX + (12 - baseCamX) * ease,
            baseCamY + (8 - baseCamY) * ease,
            baseCamZ + (110 - baseCamZ) * ease   // 270 -> 110 (Forward travel!)
          ),
          look: new THREE.Vector3(
            0 + (28 - 0) * ease,
            4 + (6 - 4) * ease,
            0 + (-120 - 0) * ease
          )
        };"""

new_cam_flight = r"""    function getCameraTrajectory(p) {
      // 6-STAGE CENTERED FORWARD SPACE-TRAVEL FLIGHT (Z: +260 -> -1380)
      if (p <= 0.16) {
        // Stage 1: HOME (NIVORA CORE) -> Camera moves forward directly through central core
        const t = p / 0.16;
        const ease = t * t * (3 - 2 * t);
        return {
          pos: new THREE.Vector3(
            0,
            0 + (4 - 0) * ease,
            baseCamZ + (110 - baseCamZ) * ease   // 260 -> 110 (Forward travel!)
          ),
          look: new THREE.Vector3(
            0,
            14 + (10 - 14) * ease,
            0 + (-120 - 0) * ease
          )
        };"""

if old_cam_flight in code:
    code = code.replace(old_cam_flight, new_cam_flight)
    print("Updated camera flight stage 1 for centered composition")
else:
    print("old_cam_flight target not found")

# 9. In animateUniverseCinematic, keep product worlds invisible during hero ($p < 0.16$)
old_pw_vis = r"""      // 4 Orbital Product Worlds Animation (Dynamic Spatial Journey)"""
new_pw_vis = r"""      // Products constellation visibility (only visible when traveling to Products)
      if (productWorldsGroup) {
        productWorldsGroup.visible = (targetScrollP > 0.14);
      }

      // 4 Orbital Product Worlds Animation (Dynamic Spatial Journey)"""

if old_pw_vis in code:
    code = code.replace(old_pw_vis, new_pw_vis)
    print("Set productWorldsGroup to emerge only when traveling toward Products")
else:
    print("old_pw_vis target not found")

# Save updated master builder
with open(MASTER_BUILDER, "w", encoding="utf-8") as f:
    f.write(code)

print("Saved updated assemble_ultimate_3d_universe.py successfully!")
