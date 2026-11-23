import re
import sys

filepath = "/Users/bennabathulanivas/Desktop/my projects/NIVORA/builder/assemble_consultancy_universe.py"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Google Fonts in <head>
old_fonts = """  <!-- GOOGLE FONTS: Sora, Space Grotesk, Inter, Instrument Serif, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Space+Grotesk:wght@400;500;600;700;800&family=Sora:wght@400;500;600;700;800&display=swap" rel="stylesheet">"""

new_fonts = """  <!-- GOOGLE FONTS: Plus Jakarta Sans, Inter, JetBrains Mono (Premium & High-Speed) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">"""

if old_fonts in content:
    content = content.replace(old_fonts, new_fonts, 1)
    print("Updated Google Fonts links to Plus Jakarta Sans + Inter + JetBrains Mono")
else:
    print("WARNING: old_fonts not matched")

# 2. Update CSS Font Variables
old_vars = """      --font-display: 'Space Grotesk', -apple-system, sans-serif;
      --font-ui: 'Sora', -apple-system, sans-serif;
      --font-body: 'Inter', -apple-system, sans-serif;
      --font-serif: 'Instrument Serif', Georgia, serif;
      --font-mono: 'JetBrains Mono', monospace;"""

new_vars = """      --font-display: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-ui: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-serif: 'Plus Jakarta Sans', Georgia, serif;
      --font-mono: 'JetBrains Mono', 'SF Mono', Consolas, monospace;"""

if old_vars in content:
    content = content.replace(old_vars, new_vars, 1)
    print("Updated CSS font variables")
else:
    print("WARNING: old_vars not matched")

# 3. Update global resets & box-sizing & component boundaries
old_resets = """    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
      overflow-x: hidden;
      scroll-behavior: smooth;
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: var(--font-body);
      overflow-x: hidden;
      width: 100%;
    }

    body {
      background-color: var(--bg-dark);
      overflow-x: hidden;
      width: 100%;
      min-height: 100vh;
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      position: relative;
    }"""

new_resets = """    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      min-width: 0;
    }

    html {
      scroll-behavior: smooth;
      overflow-x: hidden;
      max-width: 100vw;
      width: 100%;
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: var(--font-body);
    }

    body {
      background-color: var(--bg-dark);
      overflow-x: hidden;
      max-width: 100vw;
      width: 100%;
      min-height: 100vh;
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      position: relative;
    }

    img, svg, video, iframe {
      max-width: 100%;
      height: auto;
    }

    h1, h2, h3, h4, h5, h6, p, a, span, button {
      overflow-wrap: break-word;
      word-break: break-word;
    }

    /* Off-screen Content Visibility Optimization */
    #solutions, #products, #about, #folivio, #insights, #contact, #footer {
      content-visibility: auto;
      contain-intrinsic-size: 1px 750px;
    }"""

if old_resets in content:
    content = content.replace(old_resets, new_resets, 1)
    print("Updated global resets & content-visibility")
else:
    print("WARNING: old_resets not matched")

# 4. Enhance .cosmic-nebula-bg
old_nebula = """    /* Rich Deep Space Milky Way Galaxy Backdrop */
    .cosmic-nebula-bg {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 0;
      pointer-events: none;
      background:
        radial-gradient(ellipse 80% 50% at 50% -10%, rgba(120, 58, 230, 0.22) 0%, transparent 65%),
        radial-gradient(ellipse 65% 45% at 85% 40%, rgba(6, 182, 212, 0.16) 0%, transparent 60%),
        radial-gradient(ellipse 70% 50% at 15% 65%, rgba(168, 85, 247, 0.15) 0%, transparent 60%),
        radial-gradient(ellipse 90% 60% at 50% 110%, rgba(14, 165, 233, 0.12) 0%, transparent 70%),
        radial-gradient(circle at 50% 50%, rgba(15, 23, 42, 0.8) 0%, #020617 75%, #01040a 100%);
    }"""

new_nebula = """    /* Rich Deep Space Milky Way Galaxy Backdrop & Cosmic Nebulae */
    .cosmic-nebula-bg {
      position: fixed;
      inset: 0;
      width: 100%;
      height: 100%;
      z-index: 0;
      pointer-events: none;
      background:
        radial-gradient(ellipse 75% 55% at 50% -5%, rgba(124, 58, 237, 0.28) 0%, transparent 60%),
        radial-gradient(ellipse 60% 45% at 88% 32%, rgba(6, 182, 212, 0.20) 0%, transparent 55%),
        radial-gradient(ellipse 65% 50% at 12% 58%, rgba(168, 85, 247, 0.22) 0%, transparent 58%),
        radial-gradient(ellipse 85% 65% at 65% 85%, rgba(14, 165, 233, 0.16) 0%, transparent 65%),
        radial-gradient(circle at 50% 50%, rgba(11, 16, 32, 0.92) 0%, #030611 65%, #010307 100%);
    }

    .cosmic-nebula-bg::after {
      content: '';
      position: absolute;
      inset: 0;
      background:
        radial-gradient(1.5px 1.5px at 15% 25%, rgba(255, 255, 255, 0.4) 0%, transparent 100%),
        radial-gradient(1px 1px at 35% 65%, rgba(56, 189, 248, 0.45) 0%, transparent 100%),
        radial-gradient(1.5px 1.5px at 75% 15%, rgba(168, 85, 247, 0.4) 0%, transparent 100%),
        radial-gradient(1px 1px at 85% 75%, rgba(255, 255, 255, 0.35) 0%, transparent 100%),
        radial-gradient(ellipse 90% 80% at 50% 50%, transparent 50%, rgba(1, 3, 7, 0.6) 100%);
      opacity: 0.85;
      pointer-events: none;
    }"""

if old_nebula in content:
    content = content.replace(old_nebula, new_nebula, 1)
    print("Enhanced .cosmic-nebula-bg graphics")
else:
    print("WARNING: old_nebula not matched")

# 5. Fix .products-grid, .solutions-grid, .insights-grid minmax limits
content = content.replace(
    'grid-template-columns: repeat(auto-fit, minmax(520px, 1fr));',
    'grid-template-columns: repeat(auto-fit, minmax(min(100%, 460px), 1fr));'
)
content = content.replace(
    'grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));',
    'grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr));'
)
content = content.replace(
    'grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));',
    'grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr));'
)
print("Updated grid minmax rules for products, solutions, and insights")

# 6. Replace and expand Responsive Media Queries
old_media_section_start = "    /* -------------------------------------------------------------\n       RESPONSIVE MEDIA QUERIES (DESKTOP, LAPTOP, TABLET, MOBILE)\n       ------------------------------------------------------------- */"
old_media_end_marker = "    /* -------------------------------------------------------------\n       BROCHURE MODAL VIEWER SYSTEM"

new_responsive_queries = """    /* -------------------------------------------------------------
       RESPONSIVE MEDIA QUERIES (DESKTOP, LAPTOP, TABLET, MOBILE)
       ------------------------------------------------------------- */
    @media (max-width: 1200px) {
      .footer-grid {
        grid-template-columns: repeat(3, 1fr);
        gap: 2.5rem;
      }
      .journey-steps-grid {
        grid-template-columns: repeat(3, 1fr);
      }
    }

    @media (max-width: 1024px) {
      .products-grid {
        grid-template-columns: 1fr;
      }
      .contact-grid {
        grid-template-columns: 1fr;
        gap: 3.0rem;
      }
      .founder-card {
        grid-template-columns: 1fr;
        text-align: center;
        gap: 2.5rem;
      }
      .founder-img-col {
        margin: 0 auto;
      }
      .services-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 1.15rem;
      }
      .solutions-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 1.25rem;
      }
    }

    @media (max-width: 860px) {
      .hero-metrics {
        grid-template-columns: repeat(2, 1fr);
        gap: 0.85rem;
      }
      .nav-links, .nav-status-pill, .nav-cta-btn {
        display: none !important;
      }
      .nav-mobile-toggle {
        display: flex !important;
      }
      .footer-grid {
        grid-template-columns: repeat(2, 1fr);
      }
      .folivio-process-steps {
        grid-template-columns: 1fr;
      }
      .folivio-step-arrow {
        display: none;
      }
      .journey-steps-grid {
        grid-template-columns: 1fr;
      }
      .solutions-grid {
        grid-template-columns: 1fr;
        gap: 1.25rem;
      }
      .founder-card {
        padding: 2.0rem 1.4rem;
      }
      .folivio-hero-card {
        padding: 2.0rem 1.4rem;
      }
    }

    @media (max-width: 768px) {
      /* Concept & Brochure Modals on Tablet/Mobile */
      .modal-container {
        width: 95vw;
        max-height: 92vh;
        border-radius: 14px;
        margin: auto;
      }
      .modal-top-bar {
        padding: 0.85rem 1.1rem;
      }
      .modal-scroll-body {
        padding: 1.35rem 1.1rem;
      }
      .modal-product-branding {
        flex-direction: column;
        align-items: flex-start;
        gap: 0.75rem;
      }
      .modal-product-branding img {
        width: 52px !important;
        height: 52px !important;
      }
      .modal-caps-grid {
        grid-template-columns: 1fr;
        gap: 0.75rem;
      }
      .modal-specs-grid {
        grid-template-columns: 1fr;
      }
      .modal-steps-flow {
        grid-template-columns: 1fr;
      }
    }

    @media (max-width: 640px) {
      .container {
        padding: 0 1.15rem;
      }
      .section {
        padding: 4.5rem 0 3.5rem;
      }
      .section-divider {
        margin-bottom: 3.5rem;
      }
      .form-row {
        grid-template-columns: 1fr;
      }
      .footer-grid {
        grid-template-columns: 1fr;
        gap: 2.0rem;
      }
      .hero-metrics {
        grid-template-columns: 1fr;
        gap: 0.75rem;
      }
      .folivio-brand-row {
        flex-direction: column;
        align-items: flex-start;
      }
      .services-grid {
        grid-template-columns: 1fr;
        gap: 0.95rem;
      }
      .service-card {
        padding: 1.35rem 1.15rem;
      }
      .solutions-grid {
        grid-template-columns: 1fr;
        gap: 1.15rem;
      }
      .solution-card {
        padding: 1.6rem 1.25rem;
      }
      .world-card {
        padding: 1.6rem 1.25rem;
      }
      .pillars-grid {
        grid-template-columns: 1fr;
      }
      .folivio-services-grid {
        grid-template-columns: 1fr;
      }
      .folivio-benefits-grid {
        grid-template-columns: 1fr;
      }
      .insights-grid {
        grid-template-columns: 1fr;
      }
      .contact-form {
        padding: 1.8rem 1.25rem;
      }
      .service-actions-row, .solution-actions-row {
        flex-direction: column;
        gap: 0.55rem;
      }
      .service-brochure-btn, .solution-brochure-btn {
        width: 100%;
        justify-content: center;
      }
      .hero-title .hero-welcome {
        font-size: 2.1rem;
      }
      .hero-tagline {
        font-size: 1.25rem;
      }
      .hero-desc {
        font-size: 0.92rem;
      }
    }"""

# Check where responsive media queries are
# Note: brochure CSS was added either before or after responsive queries
# Let's inspect the exact lines around @media (max-width: 1200px)
media_pattern = r'    /\* -------------------------------------------------------------\s*RESPONSIVE MEDIA QUERIES.*?@media \(max-width: 640px\) \{.*?\n    \}'
match = re.search(media_pattern, content, re.DOTALL)
if match:
    content = content[:match.start()] + new_responsive_queries + content[match.end():]
    print("Replaced responsive media queries with comprehensive boundary enforcement")
else:
    print("WARNING: media_pattern not matched")

# 7. Update Three.js SoftPointTexture & BeaconTexture
old_soft_texture = """      grad.addColorStop(0, 'rgba(255, 255, 255, 1)');
      grad.addColorStop(0.22, 'rgba(235, 245, 255, 0.85)');
      grad.addColorStop(0.60, 'rgba(6, 182, 212, 0.28)');
      grad.addColorStop(1, 'rgba(6, 182, 212, 0)');"""

new_soft_texture = """      grad.addColorStop(0, 'rgba(255, 255, 255, 1)');
      grad.addColorStop(0.25, 'rgba(235, 248, 255, 0.92)');
      grad.addColorStop(0.55, 'rgba(56, 189, 248, 0.38)');
      grad.addColorStop(0.85, 'rgba(168, 85, 247, 0.12)');
      grad.addColorStop(1, 'rgba(0, 0, 0, 0)');"""

if old_soft_texture in content:
    content = content.replace(old_soft_texture, new_soft_texture, 1)
    print("Updated getSoftPointTexture gradient")
else:
    print("WARNING: old_soft_texture not found")

old_beacon_texture = """      ctx.lineWidth = 1.2;
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)';
      ctx.beginPath();
      ctx.moveTo(64, 18); ctx.lineTo(64, 110);
      ctx.moveTo(18, 64); ctx.lineTo(110, 64);
      ctx.stroke();"""

new_beacon_texture = """      ctx.lineWidth = 1.0;
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.65)';
      ctx.beginPath();
      ctx.moveTo(64, 10); ctx.lineTo(64, 118);
      ctx.moveTo(10, 64); ctx.lineTo(118, 64);
      ctx.stroke();

      ctx.lineWidth = 0.5;
      ctx.strokeStyle = 'rgba(56, 189, 248, 0.4)';
      ctx.beginPath();
      ctx.moveTo(28, 28); ctx.lineTo(100, 100);
      ctx.moveTo(28, 100); ctx.lineTo(100, 28);
      ctx.stroke();"""

if old_beacon_texture in content:
    content = content.replace(old_beacon_texture, new_beacon_texture, 1)
    print("Updated getBeaconTexture diffraction rays")
else:
    print("WARNING: old_beacon_texture not found")

# 8. Update Three.js Distant Starfield & Nebula Corridor
old_distant = """        pos[i * 3] = (Math.random() - 0.5) * 1600;
        pos[i * 3 + 1] = (Math.random() - 0.5) * 1000;
        pos[i * 3 + 2] = -400 - Math.random() * 1100;

        const isCyan = Math.random() < 0.08;
        if (isCyan) {
          col[i * 3] = 0.5; col[i * 3 + 1] = 0.85; col[i * 3 + 2] = 1.0;
        } else {
          const shade = 0.45 + Math.random() * 0.5;
          col[i * 3] = shade; col[i * 3 + 1] = shade; col[i * 3 + 2] = shade * 1.05;
        }"""

new_distant = """        pos[i * 3] = (Math.random() - 0.5) * 1800;
        pos[i * 3 + 1] = (Math.random() - 0.5) * 1200;
        pos[i * 3 + 2] = 350 - Math.random() * 2200;

        const starRand = Math.random();
        if (starRand < 0.12) {
          col[i * 3] = 0.45; col[i * 3 + 1] = 0.82; col[i * 3 + 2] = 1.0; // Cyan
        } else if (starRand < 0.20) {
          col[i * 3] = 0.85; col[i * 3 + 1] = 0.60; col[i * 3 + 2] = 1.0; // Violet
        } else if (starRand < 0.28) {
          col[i * 3] = 1.0; col[i * 3 + 1] = 0.92; col[i * 3 + 2] = 0.75; // Gold
        } else {
          const shade = 0.55 + Math.random() * 0.45;
          col[i * 3] = shade; col[i * 3 + 1] = shade; col[i * 3 + 2] = shade * 1.05;
        }"""

if old_distant in content:
    content = content.replace(old_distant, new_distant, 1)
    print("Updated buildDistantStarfield corridor across full travel path")
else:
    print("WARNING: old_distant not found")

# 9. Update buildSubtleCosmicNebula to distribute puffs along entire journey
old_nebula_loop = """      for (let i = 0; i < 12; i++) {
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
      }"""

new_nebula_loop = """      for (let i = 0; i < 16; i++) {
        const pCfg = puffs[i % puffs.length];
        const tex = createProceduralNebulaTexture(pCfg.color1, pCfg.color2);
        const mat = new THREE.SpriteMaterial({
          map: tex,
          transparent: true,
          opacity: 0.32,
          blending: THREE.AdditiveBlending,
          depthWrite: false
        });
        const sprite = new THREE.Sprite(mat);

        const zPos = 180 - i * 110 + (Math.random() - 0.5) * 60;
        const angle = (i * 0.9) + Math.random() * 0.5;
        const radius = 60 + Math.random() * 140;
        sprite.position.set(
          Math.cos(angle) * radius,
          18 + Math.sin(angle) * 0.6 * radius + (Math.random() - 0.5) * 40,
          zPos
        );
        const s = 180 + Math.random() * 220;
        sprite.scale.set(s, s, 1);
        scene.add(sprite);
        nebulaPuffs.push({ sprite, baseScale: s, baseOpacity: mat.opacity, seed: Math.random() * 10 });
      }"""

if old_nebula_loop in content:
    content = content.replace(old_nebula_loop, new_nebula_loop, 1)
    print("Updated buildSubtleCosmicNebula corridor across full travel path")
else:
    print("WARNING: old_nebula_loop not found")

# 10. Update PerformanceEngine pixel ratio cap for High Tier
old_tier_high = """        } else {
          this.tier = 'HIGH';
          this.particleScale = 1.0;"""

new_tier_high = """        } else {
          this.tier = 'HIGH';
          this.particleScale = 1.0;
          this.pixelRatio = Math.min(window.devicePixelRatio || 1, 1.25);"""

if old_tier_high in content:
    content = content.replace(old_tier_high, new_tier_high, 1)
    print("Capped HIGH tier pixel ratio to 1.25 for lightning performance")
else:
    print("WARNING: old_tier_high not found")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Upgrade script applied successfully to assemble_consultancy_universe.py!")
