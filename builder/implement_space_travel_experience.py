#!/usr/bin/env python3
"""
implement_space_travel_experience.py
Transforms NIVORA into a living 3D space-travel universe:
1. Global persistent WebGL space environment behind ALL sections (Home -> Products -> About -> Portfolio -> Vision -> FOLIVIO -> Contact).
2. Real depth-based Starfield + Hyperspace Motion Streak / Warp system:
   - 3,600 line segments (7,200 vertices) that dynamically travel toward the viewer on scroll DOWN.
   - Streaks elongate into cinematic light trails during fast scrolling.
   - Star field reverses naturally on scroll UP.
   - Smooth exponential damping deceleration when scrolling stops.
3. Virtual Camera Scroll Travel Model:
   - Full 6-stage 3D camera trajectory through 1,650 units of space (Z: +270 -> -1380).
   - Core -> Product Constellation -> The Builder -> Creation Field -> Future Horizon -> Transmission Point.
4. Spatial destination environments:
   - Product Constellation ambient aura (Z: -200).
   - The Builder (Nivas) golden-cyan holographic halo + 450 floating embers (Z: -530).
   - Creation Field project constellation nodes (Z: -840).
   - Contact Transmission beacon & calm cosmic float (Z: -1480).
5. Cinematic Button Interactions:
   - 'Enter the Universe': 1.35s hyper-drive warp surge.
   - 'Explore Products': controlled flight to product constellation.
6. Preserves 100% of existing content, logos, typography, modals, and design language.
"""

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MASTER_BUILDER = os.path.join(SCRIPT_DIR, "assemble_ultimate_3d_universe.py")

with open(MASTER_BUILDER, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update CSS: Remove opaque background from .section and make universe persistent behind all content
old_section_css = r"""    .section {
      position: relative;
      padding: 7rem 4%;
      z-index: 10;
      background: linear-gradient(180deg, rgba(2, 4, 10, 0.75) 0%, rgba(2, 4, 10, 0.90) 100%);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
    }"""

new_section_css = r"""    /* GLOBAL PERSISTENT UNIVERSE: ALL SECTIONS ARE TRANSPARENT OVER 3D WEBGL */
    .section {
      position: relative;
      padding: 8rem 4%;
      z-index: 10;
      background: transparent;
      pointer-events: auto;
      transition: opacity 0.5s ease, transform 0.5s ease;
    }

    /* Spatial Destination Header Kicker */
    .destination-kicker {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.32rem 0.9rem;
      border-radius: 9999px;
      background: rgba(6, 182, 212, 0.08);
      border: 1px solid rgba(6, 182, 212, 0.28);
      font-family: var(--font-mono);
      font-size: 0.7rem;
      font-weight: 600;
      letter-spacing: 0.16em;
      color: var(--brand-cyan);
      text-transform: uppercase;
      margin-bottom: 0.85rem;
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
    }
    .dest-pulse-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #06b6d4;
      box-shadow: 0 0 8px #06b6d4;
      animation: dotPulse 2s infinite ease-in-out;
    }"""

if old_section_css in code:
    code = code.replace(old_section_css, new_section_css)
    print("Replaced section CSS with persistent global transparency")
else:
    print("Old section CSS target not found")

# 2. Update CTA button click handlers in HTML
old_ctas = r"""          <div class="hero-actions">
            <button type="button" class="btn-enter-universe" onclick="triggerCinematicCameraZoom()">
              <span>Enter the Universe &rarr;</span>
            </button>
            <a class="btn-explore-products" href="#products">
              <span class="play-icon-circle">&#9658;</span>
              <span>Explore Products</span>
            </a>
          </div>"""

new_ctas = r"""          <div class="hero-actions">
            <button type="button" class="btn-enter-universe" onclick="triggerEnterUniverseSequence()" id="btnEnterUniverse">
              <span>Enter the Universe &rarr;</span>
            </button>
            <button type="button" class="btn-explore-products" onclick="triggerExploreProductsFlight()" id="btnExploreProducts">
              <span class="play-icon-circle">&#9658;</span>
              <span>Explore Products</span>
            </button>
          </div>"""

if old_ctas in code:
    code = code.replace(old_ctas, new_ctas)
    print("Updated hero CTAs with space-travel trigger handlers")
else:
    print("Old hero CTAs target not found")

# 3. Add Destination badges to sections in HTML
code = code.replace(
    '<section class="section" id="products">\n      <div class="container">\n        <div class="section-head">',
    '<section class="section" id="products">\n      <div class="container">\n        <div class="section-head">\n          <div><div class="destination-kicker"><span class="dest-pulse-dot"></span>DESTINATION: PRODUCT CONSTELLATION</div>'
)
code = code.replace(
    '<section class="section" id="about">\n      <div class="container">\n        <div class="section-head">',
    '<section class="section" id="about">\n      <div class="container">\n        <div class="section-head">\n          <div><div class="destination-kicker"><span class="dest-pulse-dot"></span>DESTINATION: THE BUILDER</div>'
)
code = code.replace(
    '<section class="section" id="portfolio">\n      <div class="container">\n        <div class="section-head">',
    '<section class="section" id="portfolio">\n      <div class="container">\n        <div class="section-head">\n          <div><div class="destination-kicker"><span class="dest-pulse-dot"></span>DESTINATION: CREATION FIELD</div>'
)
code = code.replace(
    '<section class="section" id="vision">\n      <div class="container">\n        <div class="section-head">',
    '<section class="section" id="vision">\n      <div class="container">\n        <div class="section-head">\n          <div><div class="destination-kicker"><span class="dest-pulse-dot"></span>DESTINATION: THE FUTURE HORIZON</div>'
)
code = code.replace(
    '<section class="section" id="folivio">\n      <div class="container">\n        <div class="section-head">',
    '<section class="section" id="folivio">\n      <div class="container">\n        <div class="section-head">\n          <div><div class="destination-kicker"><span class="dest-pulse-dot"></span>DESTINATION: CAREER CONSTELLATION</div>'
)
code = code.replace(
    '<section class="section" id="contact">\n      <div class="container">\n        <div class="section-head">',
    '<section class="section" id="contact">\n      <div class="container">\n        <div class="section-head">\n          <div><div class="destination-kicker"><span class="dest-pulse-dot"></span>DESTINATION: TRANSMISSION</div>'
)
print("Added destination kickers across all sections")

# 4. Update Three.js Engine Variables
three_vars_target = r"""    const canvas = document.getElementById('webglUniverseCanvas');
    let renderer, scene, camera;
    let milkyWayGroup, galacticBulge, spiralArmStars;
    let distantStarField, brightBeaconsGroup, distantGalaxiesGroup;
    let globeGroup, globeMesh, logoSprite, atmosphereMesh, globeHaloSprite;
    let orbitalRings = [], ringParticles = [];
    let accretionGroup, accretionDisk, accretionParticles, energyBeam;
    let blPlanetMesh, blPlanetAtmos, brPlanetMesh, brPlanetAtmos, trGalaxyGroup;
    let nebulaPuffs = [];"""

three_vars_replacement = r"""    const canvas = document.getElementById('webglUniverseCanvas');
    let renderer, scene, camera;
    let milkyWayGroup, galacticBulge, spiralArmStars;
    let distantStarField, brightBeaconsGroup, distantGalaxiesGroup;
    let globeGroup, globeMesh, logoSprite, atmosphereMesh, globeHaloSprite;
    let orbitalRings = [], ringParticles = [];
    let accretionGroup, accretionDisk, accretionParticles, energyBeam;
    let blPlanetMesh, blPlanetAtmos, brPlanetMesh, brPlanetAtmos, trGalaxyGroup;
    let nebulaPuffs = [];

    // SPACE-TRAVEL & HYPERSPACE WARP SYSTEM (REAL DEPTH + STREAKS)
    let warpLinesMesh, warpLinesGeo;
    const WARP_STAR_COUNT = 3600;
    const warpStarPositions = new Float32Array(WARP_STAR_COUNT * 6);
    const warpStarColors = new Float32Array(WARP_STAR_COUNT * 6);
    const warpStarData = [];
    let rawScrollVelocity = 0;
    let smoothedScrollVelocity = 0;
    let lastScrollPosition = 0;
    let isUserScrolling = false;
    let scrollTimeoutId = null;

    // SPATIAL DESTINATION OBJECTS
    let builderSpatialHalo, builderEmbersPoints;
    let portfolioConstellationGroup;
    let transmissionBeaconGroup;"""

if three_vars_target in code:
    code = code.replace(three_vars_target, three_vars_replacement)
    print("Updated Three.js variables with Space Travel & Warp systems")
else:
    print("Three.js variables target not found")

# 5. In initUniverse3D, add buildWarpStarfield and buildSpatialDestinations
init_uni_target = r"""        // Build 3D Cinematic Universe
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

init_uni_replacement = r"""        // Build 3D Cinematic Universe
        buildDistantStarfield();
        buildWarpStarfield();
        buildProceduralMilkyWay();
        buildGalacticBulge();
        buildSubtleCosmicNebula();
        buildBrightStellarBeacons();
        buildCelestialForeAndBackground();
        buildNivoraGlobeCore();
        buildGalacticAccretionPlatform();
        buildOrbitalRings3D();
        build3DProductWorlds();
        buildSpatialDestinations();"""

if init_uni_target in code:
    code = code.replace(init_uni_target, init_uni_replacement)
    print("Updated initUniverse3D function calls")
else:
    print("initUniverse3D target not found")

# 6. Add buildWarpStarfield and buildSpatialDestinations functions
warp_functions = r"""    /* -------------------------------------------------------------
       2B. DYNAMIC HYPERSPACE WARP STARFIELD (MOTION TRAILS & REAL DEPTH)
       ------------------------------------------------------------- */
    function buildWarpStarfield() {
      const palette = [
        { r: 1.0, g: 1.0, b: 1.0 },       // Diamond white (70%)
        { r: 0.82, g: 0.90, b: 1.0 },      // Celestial soft blue (15%)
        { r: 0.22, g: 0.74, b: 0.97 },     // Electric cyan (7%)
        { r: 0.75, g: 0.52, b: 0.98 },     // Cosmic violet (5%)
        { r: 0.96, g: 0.45, b: 0.72 }      // Magenta energy (3%)
      ];

      for (let i = 0; i < WARP_STAR_COUNT; i++) {
        const angle = Math.random() * Math.PI * 2;
        const radius = 20 + Math.pow(Math.random(), 0.85) * 540;
        const x = Math.cos(angle) * radius;
        const y = Math.sin(angle) * radius;
        const z = (Math.random() - 0.5) * 2200 - 500;
        const baseSpeed = 0.25 + Math.random() * 0.45;

        const rand = Math.random();
        let col = palette[0];
        if (rand > 0.97) col = palette[4];
        else if (rand > 0.92) col = palette[3];
        else if (rand > 0.85) col = palette[2];
        else if (rand > 0.70) col = palette[1];

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
      scene.add(warpLinesMesh);
    }

    /* -------------------------------------------------------------
       2C. 3D SPATIAL DESTINATION STRUCTURES (ABOUT, PORTFOLIO, CONTACT)
       ------------------------------------------------------------- */
    function buildSpatialDestinations() {
      // 1. THE BUILDER DESTINATION (Z = -530)
      // Holographic aura halo ring positioned behind founder card
      const bHaloGeo = new THREE.RingGeometry(24, 38, 48);
      const bHaloMat = new THREE.MeshBasicMaterial({
        color: 0x06b6d4,
        transparent: true,
        opacity: 0.35,
        side: THREE.DoubleSide,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });
      builderSpatialHalo = new THREE.Mesh(bHaloGeo, bHaloMat);
      builderSpatialHalo.position.set(24, 6, -530);
      scene.add(builderSpatialHalo);

      // 450 Shimmering Golden & Cyan Floating Embers
      const emberCount = 450;
      const emberPos = new Float32Array(emberCount * 3);
      const emberCol = new Float32Array(emberCount * 3);
      for (let i = 0; i < emberCount; i++) {
        const a = Math.random() * Math.PI * 2;
        const r = 5 + Math.pow(Math.random(), 1.2) * 45;
        emberPos[i * 3] = 24 + Math.cos(a) * r;
        emberPos[i * 3 + 1] = 6 + Math.sin(a) * r;
        emberPos[i * 3 + 2] = -530 + (Math.random() - 0.5) * 25;

        if (Math.random() > 0.4) {
          emberCol[i * 3] = 0.98; emberCol[i * 3 + 1] = 0.75; emberCol[i * 3 + 2] = 0.25; // Gold
        } else {
          emberCol[i * 3] = 0.12; emberCol[i * 3 + 1] = 0.78; emberCol[i * 3 + 2] = 0.95; // Cyan
        }
      }
      const emberGeo = new THREE.BufferGeometry();
      emberGeo.setAttribute('position', new THREE.BufferAttribute(emberPos, 3));
      emberGeo.setAttribute('color', new THREE.BufferAttribute(emberCol, 3));
      builderEmbersPoints = new THREE.Points(emberGeo, new THREE.PointsMaterial({
        size: 2.2,
        vertexColors: true,
        map: createSoftPointTexture(),
        transparent: true,
        opacity: 0.75,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      }));
      scene.add(builderEmbersPoints);

      // 2. CREATION FIELD DESTINATION (Z = -840)
      // 6 Glowing Constellation Nodes floating in space
      portfolioConstellationGroup = new THREE.Group();
      portfolioConstellationGroup.position.set(0, 8, -840);
      const nodeCoords = [
        [-38, 22, -20], [35, 18, -40], [-25, -18, -15],
        [32, -22, -35], [0, 26, -55], [0, -28, -25]
      ];
      nodeCoords.forEach((nc) => {
        const nMesh = new THREE.Mesh(
          new THREE.SphereGeometry(1.4, 12, 12),
          new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.9 })
        );
        nMesh.position.set(nc[0], nc[1], nc[2]);
        const nHalo = new THREE.Sprite(new THREE.SpriteMaterial({
          map: createSoftPointTexture(),
          color: 0x8b5cf6,
          transparent: true,
          opacity: 0.65,
          blending: THREE.AdditiveBlending
        }));
        nHalo.scale.set(7.5, 7.5, 1);
        nMesh.add(nHalo);
        portfolioConstellationGroup.add(nMesh);
      });
      scene.add(portfolioConstellationGroup);

      // 3. THE TRANSMISSION DESTINATION (Z = -1480)
      // Edge of Universe: Central radiant transmission beacon
      transmissionBeaconGroup = new THREE.Group();
      transmissionBeaconGroup.position.set(0, 10, -1480);

      const beaconRings = [
        { r: 8, col: 0xffffff, op: 0.95 },
        { r: 22, col: 0x06b6d4, op: 0.75 },
        { r: 42, col: 0xa855f7, op: 0.55 },
        { r: 68, col: 0xec4899, op: 0.35 }
      ];
      beaconRings.forEach(br => {
        const ringLine = new THREE.Line(
          new THREE.BufferGeometry().setFromPoints(new THREE.EllipseCurve(0, 0, br.r, br.r, 0, Math.PI * 2).getPoints(80)),
          new THREE.LineBasicMaterial({ color: br.col, transparent: true, opacity: br.op, blending: THREE.AdditiveBlending })
        );
        transmissionBeaconGroup.add(ringLine);
      });

      // Central Pillar Beam
      const tBeam = new THREE.Mesh(
        new THREE.CylinderGeometry(0.8, 3.2, 50, 16, 1, true),
        new THREE.MeshBasicMaterial({ color: 0x06b6d4, transparent: true, opacity: 0.65, blending: THREE.AdditiveBlending, side: THREE.DoubleSide })
      );
      transmissionBeaconGroup.add(tBeam);
      scene.add(transmissionBeaconGroup);
    }

"""

# Insert warp_functions right before buildDistantStarfield
dist_star_hook = r"""    function buildDistantStarfield() {"""
if dist_star_hook in code:
    code = code.replace(dist_star_hook, warp_functions + dist_star_hook)
    print("Added buildWarpStarfield and buildSpatialDestinations functions")
else:
    print("buildDistantStarfield hook not found")

# 7. Update getCameraTrajectory with full 6-stage forward flight path across 1,650 units of space
old_cam_traj = r"""    function getCameraTrajectory(p) {
      if (p < 0.25) {
        // 0.0 to 0.25: Hero -> Zoom out & reveal product orbits
        const t = p / 0.25;
        const ease = t * t * (3 - 2 * t);
        return {
          pos: new THREE.Vector3(
            baseCamX + (15 - baseCamX) * ease,
            baseCamY + (18 - baseCamY) * ease,
            baseCamZ + (410 - baseCamZ) * ease
          ),
          look: new THREE.Vector3(
            30 + (50 - 30) * ease,
            5,
            0
          )
        };
      } else if (p < 0.55) {
        // 0.25 to 0.55: Revealing product worlds & constellation (#products)
        const t = (p - 0.25) / 0.30;
        const ease = t * t * (3 - 2 * t);
        return {
          pos: new THREE.Vector3(
            15 + (38 - 15) * ease,
            18 + (40 - 18) * ease,
            410 + (530 - 410) * ease
          ),
          look: new THREE.Vector3(
            50 + (66 - 50) * ease,
            5,
            0
          )
        };
      } else if (p < 0.80) {
        // 0.55 to 0.80: Architecture Lifecycle & Meet the Builder (#about, #portfolio)
        const t = (p - 0.55) / 0.25;
        const ease = t * t * (3 - 2 * t);
        return {
          pos: new THREE.Vector3(
            38 + (-8 - 38) * ease,
            40 + (58 - 40) * ease,
            530 + (640 - 530) * ease
          ),
          look: new THREE.Vector3(
            66 + (50 - 66) * ease,
            5 + (8 - 5) * ease,
            -15 * ease
          )
        };
      } else {
        // 0.80 to 1.0: Panoramic wide galaxy overview (#vision, #folivio, #contact)
        const t = (p - 0.80) / 0.20;
        const ease = t * t * (3 - 2 * t);
        return {
          pos: new THREE.Vector3(
            -8 + (-15 - -8) * ease,
            58 + (76 - 58) * ease,
            640 + (760 - 640) * ease
          ),
          look: new THREE.Vector3(
            50 + (35 - 50) * ease,
            8 + (12 - 8) * ease,
            -15 + (-30 - -15) * ease
          )
        };
      }
    }"""

new_cam_traj = r"""    function getCameraTrajectory(p) {
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
        };
      } else if (p <= 0.38) {
        // Stage 2: PRODUCT CONSTELLATION ARRIVAL (Z: -190)
        const t = (p - 0.16) / 0.22;
        const ease = t * t * (3 - 2 * t);
        return {
          pos: new THREE.Vector3(
            12 + (-4 - 12) * ease,
            8 + (10 - 8) * ease,
            110 + (-190 - 110) * ease  // Dives into Product Constellation!
          ),
          look: new THREE.Vector3(
            28 + (0 - 28) * ease,
            6 + (10 - 6) * ease,
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
            -190 + (-520 - -190) * ease // Arrives at Founder's Domain!
          ),
          look: new THREE.Vector3(
            0 + (-6 - 0) * ease,
            10 + (6 - 10) * ease,
            -350 + (-680 - -350) * ease
          )
        };
      } else if (p <= 0.76) {
        // Stage 4: CREATION FIELD (PORTFOLIO) (Z: -840)
        const t = (p - 0.58) / 0.18;
        const ease = t * t * (3 - 2 * t);
        return {
          pos: new THREE.Vector3(
            -14 + (10 - -14) * ease,
            6 + (12 - 6) * ease,
            -520 + (-840 - -520) * ease // Glides across Portfolio field!
          ),
          look: new THREE.Vector3(
            -6 + (4 - -6) * ease,
            6 + (10 - 6) * ease,
            -680 + (-1020 - -680) * ease
          )
        };
      } else if (p <= 0.90) {
        // Stage 5: THE FUTURE HORIZON (VISION & FOLIVIO) (Z: -1140)
        const t = (p - 0.76) / 0.14;
        const ease = t * t * (3 - 2 * t);
        return {
          pos: new THREE.Vector3(
            10 + (0 - 10) * ease,
            12 + (20 - 12) * ease,
            -840 + (-1140 - -840) * ease // Expansive universe view!
          ),
          look: new THREE.Vector3(
            4 + (0 - 4) * ease,
            10 + (14 - 10) * ease,
            -1020 + (-1320 - -1020) * ease
          )
        };
      } else {
        // Stage 6: THE TRANSMISSION (CONTACT) (Z: -1380)
        const t = (p - 0.90) / 0.10;
        const ease = t * t * (3 - 2 * t);
        return {
          pos: new THREE.Vector3(
            0,
            20 + (10 - 20) * ease,
            -1140 + (-1380 - -1140) * ease // Edge of universe calm!
          ),
          look: new THREE.Vector3(
            0,
            10,
            -1550
          )
        };
      }
    }"""

if old_cam_traj in code:
    code = code.replace(old_cam_traj, new_cam_traj)
    print("Replaced getCameraTrajectory with 6-stage forward space travel")
else:
    print("old_cam_traj target not found")

# 8. Update Scroll Listener: Add real-time instantaneous velocity tracking with inertia
old_scroll_listener = r"""    window.addEventListener('scroll', () => {
      if (isZoomingTransition || !isWebGLEnabled) return;
      const scrollY = window.scrollY;
      const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
      targetScrollP = Math.max(0, Math.min(1, scrollY / (maxScroll || 1)));

      // Subtle Hero UI Fade as user scrolls past hero
      const heroContentEl = document.querySelector('.hero-content');
      if (heroContentEl) {
        const heroH = window.innerHeight;
        const fadeP = Math.max(0, Math.min(1, 1 - (scrollY / (heroH * 0.7))));
        heroContentEl.style.opacity = fadeP.toString();
        heroContentEl.style.transform = `translateY(${-scrollY * 0.25}px)`;
      }
    }, { passive: true });"""

new_scroll_listener = r"""    window.addEventListener('scroll', () => {
      if (isZoomingTransition || !isWebGLEnabled) return;
      const scrollY = window.scrollY;
      const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
      targetScrollP = Math.max(0, Math.min(1, scrollY / (maxScroll || 1)));

      // Real-time instantaneous scroll velocity & direction calculation
      const deltaY = scrollY - lastScrollPosition;
      lastScrollPosition = scrollY;
      rawScrollVelocity = deltaY;
      isUserScrolling = true;

      if (scrollTimeoutId) clearTimeout(scrollTimeoutId);
      scrollTimeoutId = setTimeout(() => {
        isUserScrolling = false;
        rawScrollVelocity = 0;
      }, 120);

      // Hero UI Depth Zoom Out as user leaves hero
      const heroContentEl = document.querySelector('.hero-content');
      if (heroContentEl) {
        const heroH = window.innerHeight;
        const fadeP = Math.max(0, Math.min(1, 1 - (scrollY / (heroH * 0.65))));
        heroContentEl.style.opacity = fadeP.toString();
        heroContentEl.style.transform = `scale(${1 - (1 - fadeP) * 0.08}) translateY(${-scrollY * 0.2}px)`;
      }
    }, { passive: true });"""

if old_scroll_listener in code:
    code = code.replace(old_scroll_listener, new_scroll_listener)
    print("Updated scroll listener with instantaneous velocity tracking")
else:
    print("old_scroll_listener target not found")

# 9. Update Animation Loop in animateUniverseCinematic:
# Include dynamic warp streak update, destination animations, and velocity damping
old_anim_loop = r"""      // Globe axial rotation & logo floating
      if (globeMesh) globeMesh.rotation.y += 0.0014 * warpSpeedFactor;
      if (logoSprite) {
        logoSprite.position.y = Math.sin(elapsed * 1.5) * 0.5;
      }

      // Foreground & background celestial rotation
      if (blPlanetMesh) blPlanetMesh.rotation.y += 0.0003;
      if (brPlanetMesh) brPlanetMesh.rotation.y += 0.0004;
      if (trGalaxyGroup) trGalaxyGroup.rotation.z += 0.0012;
      if (accretionGroup) accretionGroup.rotation.z += 0.0032 * warpSpeedFactor;"""

new_anim_loop = r"""      // Smooth exponential velocity damping
      smoothedScrollVelocity += (rawScrollVelocity - smoothedScrollVelocity) * 0.12;
      rawScrollVelocity *= 0.88;

      // Check prefers-reduced-motion
      const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      const effectiveWarpFactor = prefersReducedMotion ? 0.2 : warpSpeedFactor;

      // DYNAMIC HYPERSPACE WARP STARFIELD UPDATE (MOTION STREAKS & DEPTH TRAVEL)
      if (warpLinesGeo && warpLinesMesh) {
        // Forward speed proportional to scroll velocity + subtle cosmic drift
        const travelSpeed = ((0.32 + Math.abs(smoothedScrollVelocity) * 1.6) * Math.sign(smoothedScrollVelocity || 1)) * effectiveWarpFactor;
        // Motion trail length: stretches into light trails on fast scroll!
        const trailLength = Math.max(0.4, Math.min(30.0, Math.abs(smoothedScrollVelocity) * 2.2));

        const posAttr = warpLinesGeo.attributes.position;
        const colAttr = warpLinesGeo.attributes.color;
        const camZ = camera.position.z;
        const boundFront = camZ + 70;
        const boundBack = camZ - 1300;
        const depthSpan = boundFront - boundBack;

        for (let i = 0; i < WARP_STAR_COUNT; i++) {
          const s = warpStarData[i];
          s.z += travelSpeed * s.baseSpeed;

          // Boundary wrapping (supports forward & reverse travel!)
          if (travelSpeed > 0 && s.z > boundFront) {
            s.z -= depthSpan;
          } else if (travelSpeed < 0 && s.z < boundBack) {
            s.z += depthSpan;
          }

          const idx6 = i * 6;
          // Head vertex
          posAttr.array[idx6] = s.x;
          posAttr.array[idx6 + 1] = s.y;
          posAttr.array[idx6 + 2] = s.z;

          // Tail vertex: stretches backward when moving forward; stretches forward when reversing!
          posAttr.array[idx6 + 3] = s.x;
          posAttr.array[idx6 + 4] = s.y;
          posAttr.array[idx6 + 5] = s.z - Math.sign(travelSpeed) * trailLength;

          // Tail luminosity boost during fast travel
          const boost = Math.min(1.0, Math.abs(smoothedScrollVelocity) * 0.07);
          colAttr.array[idx6 + 3] = s.r * (0.25 + boost * 0.7);
          colAttr.array[idx6 + 4] = s.g * (0.25 + boost * 0.7);
          colAttr.array[idx6 + 5] = s.b * (0.25 + boost * 0.7);
        }

        posAttr.needsUpdate = true;
        colAttr.needsUpdate = true;
      }

      // Globe axial rotation & logo floating
      if (globeMesh) globeMesh.rotation.y += 0.0014 * effectiveWarpFactor;
      if (logoSprite) {
        logoSprite.position.y = Math.sin(elapsed * 1.5) * 0.5;
      }

      // Foreground & background celestial rotation
      if (blPlanetMesh) blPlanetMesh.rotation.y += 0.0003;
      if (brPlanetMesh) brPlanetMesh.rotation.y += 0.0004;
      if (trGalaxyGroup) trGalaxyGroup.rotation.z += 0.0012;
      if (accretionGroup) accretionGroup.rotation.z += 0.0032 * effectiveWarpFactor;

      // Animate Spatial Destinations
      if (builderSpatialHalo) {
        builderSpatialHalo.rotation.z += 0.0015;
      }
      if (builderEmbersPoints) {
        builderEmbersPoints.rotation.z -= 0.0008;
      }
      if (portfolioConstellationGroup) {
        portfolioConstellationGroup.rotation.y = Math.sin(elapsed * 0.3) * 0.06;
      }
      if (transmissionBeaconGroup) {
        const pulse = 1.0 + 0.08 * Math.sin(elapsed * 2.5);
        transmissionBeaconGroup.children.forEach((c, idx) => {
          if (c.geometry && c.geometry.type === 'CylinderGeometry') {
            c.scale.set(pulse, 1, pulse);
          } else {
            c.rotation.z += 0.001 * (idx % 2 === 0 ? 1 : -1);
          }
        });
      }"""

if old_anim_loop in code:
    code = code.replace(old_anim_loop, new_anim_loop)
    print("Updated animation loop with dynamic warp stars and destination animations")
else:
    print("old_anim_loop target not found")

# 10. Replace triggerCinematicCameraZoom with triggerEnterUniverseSequence and triggerExploreProductsFlight
old_zoom_func = r"""    /* -------------------------------------------------------------
       15. HYPERSPACE CAMERA WARP DIVE
       ------------------------------------------------------------- */
    function triggerCinematicCameraZoom() {
      if (isZoomingTransition) return;
      isZoomingTransition = true;

      const flash = document.getElementById('cosmicWarpFlash');
      const startX = camera.position.x;
      const startY = camera.position.y;
      const startZ = camera.position.z;

      const targetX = globeCenterX;
      const targetY = globeCenterY;
      const targetZ = 12;

      const duration = 1200;
      const startTime = performance.now();

      function step(now) {
        const elapsed = now - startTime;
        const p = Math.min(elapsed / duration, 1);
        const ease = p < 0.5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2;

        camera.position.x = startX + (targetX - startX) * ease;
        camera.position.y = startY + (targetY - startY) * ease;
        camera.position.z = startZ + (targetZ - startZ) * ease;

        camera.lookAt(targetX, targetY, 0);

        if (p > 0.4 && p < 0.8 && flash) {
          flash.style.opacity = '0.35';
        } else if (flash) {
          flash.style.opacity = '0';
        }

        if (p < 1) {
          requestAnimationFrame(step);
        } else {
          isZoomingTransition = false;
          if (flash) flash.style.opacity = '0';
          const productsEl = document.getElementById('products');
          if (productsEl) {
            productsEl.scrollIntoView({ behavior: 'smooth' });
          }
        }
      }

      requestAnimationFrame(step);
    }"""

new_zoom_func = r"""    /* -------------------------------------------------------------
       15. INTERACTIVE SPACE-TRAVEL SEQUENCES
       ------------------------------------------------------------- */
    function triggerEnterUniverseSequence() {
      if (isZoomingTransition) return;
      isZoomingTransition = true;

      const heroContent = document.querySelector('.hero-content');
      if (heroContent) {
        heroContent.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
        heroContent.style.opacity = '0.4';
        heroContent.style.transform = 'scale(0.96)';
      }

      const startZ = camera.position.z;
      const startTime = performance.now();
      const duration = 1350; // 1.35s cinematic hyper-drive entry

      function warpStep(now) {
        const elapsed = now - startTime;
        const p = Math.min(elapsed / duration, 1);

        if (p < 0.25) {
          // Camera pulls back slightly
          const sub = p / 0.25;
          camera.position.z = startZ + 24 * Math.sin(sub * Math.PI * 0.5);
          rawScrollVelocity = -6; // slight reverse motion
        } else if (p < 0.85) {
          // Hyperspace forward surge into the universe!
          const sub = (p - 0.25) / 0.60;
          const ease = sub * sub * (3 - 2 * sub);
          camera.position.z = (startZ + 24) - 200 * ease;
          rawScrollVelocity = 32 * Math.sin(sub * Math.PI); // Star streaks accelerate!
        } else {
          // Decelerate and settle
          const sub = (p - 0.85) / 0.15;
          camera.position.z = (startZ - 176) + 176 * sub;
          rawScrollVelocity *= 0.85;
        }

        if (p < 1) {
          requestAnimationFrame(warpStep);
        } else {
          if (heroContent) {
            heroContent.style.opacity = '1';
            heroContent.style.transform = 'scale(1)';
          }
          isZoomingTransition = false;
          // Smooth glide down to products
          const target = document.getElementById('products');
          if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
          }
        }
      }
      requestAnimationFrame(warpStep);
    }

    function triggerExploreProductsFlight() {
      if (isZoomingTransition) return;
      isZoomingTransition = true;

      // Accelerated camera travel towards product constellation
      rawScrollVelocity = 24;

      const targetElem = document.getElementById('products');
      if (targetElem) {
        targetElem.scrollIntoView({ behavior: 'smooth' });
      }

      setTimeout(() => {
        isZoomingTransition = false;
      }, 1200);
    }

    function triggerCinematicCameraZoom() {
      triggerEnterUniverseSequence();
    }"""

if old_zoom_func in code:
    code = code.replace(old_zoom_func, new_zoom_func)
    print("Replaced zoom functions with interactive space-travel flight controls")
else:
    print("old_zoom_func target not found")

with open(MASTER_BUILDER, "w", encoding="utf-8") as f:
    f.write(code)

print("Saved updated assemble_ultimate_3d_universe.py successfully!")
