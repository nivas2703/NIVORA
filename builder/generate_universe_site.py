# builder/generate_universe_site.py
# NIVORA — IMMERSIVE UNIVERSE / GALAXY WEBSITE GENERATOR
# Typography System: Space Grotesk (Display) + Inter (Body/UI) + Instrument Serif (Editorial Accent)
import os
import sys

builder_dir = os.path.dirname(os.path.abspath(__file__))
if builder_dir not in sys.path:
    sys.path.append(builder_dir)

def build():
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NIVORA — Turning Ideas Into Intelligent Products</title>
  <meta name="description" content="NIVORA is an immersive technology and innovation universe founded by Nivas Bennabatthula — home to Checkra, Homora, Bubora, and Sayora.">
  <link rel="icon" type="image/png" href="assets/images/nivora-logo.png">

  <!-- GOOGLE FONTS: Space Grotesk (Display), Inter (Body/UI), Instrument Serif (Editorial Accent), JetBrains Mono (Technical/Metadata) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
    /* =========================================================
       NIVORA IMMERSIVE UNIVERSE DESIGN SYSTEM (APPLE + LINEAR + VERCEL)
       ========================================================= */
    :root {{
      --bg-space: #010206;
      --bg-space-deep: #000103;
      --text-main: #f0f3fd;
      --text-secondary: #c0c6d9;
      --text-muted: #848c9e;
      --text-dim: #4f566b;
      --border-subtle: rgba(255, 255, 255, 0.07);
      --border-hover: rgba(255, 255, 255, 0.18);
      --glass-surface: rgba(9, 13, 26, 0.65);
      --glass-surface-dense: rgba(5, 7, 16, 0.94);
      --accent-nivora: #6366f1;
      --accent-glow: rgba(99, 102, 241, 0.28);

      /* Product Themes */
      --color-checkra: #6366f1;
      --glow-checkra: rgba(99, 102, 241, 0.35);
      --color-homora: #06b6d4;
      --glow-homora: rgba(6, 182, 212, 0.35);
      --color-bubora: #ec4899;
      --glow-bubora: rgba(236, 72, 153, 0.35);
      --color-sayora: #10b981;
      --glow-sayora: rgba(16, 185, 129, 0.35);

      /* Typographic System */
      --font-display: 'Space Grotesk', -apple-system, sans-serif;
      --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-editorial: 'Instrument Serif', Georgia, serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html {{
      scroll-behavior: smooth;
      background-color: var(--bg-space);
      color: var(--text-main);
      font-family: var(--font-body);
      font-size: 16px;
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      overflow-x: hidden;
    }}

    body {{
      background-color: var(--bg-space);
      color: var(--text-main);
      min-height: 100vh;
      overflow-x: hidden;
      position: relative;
      font-family: var(--font-body);
    }}

    body.world-open {{
      overflow: hidden !important;
      height: 100vh !important;
    }}

    /* Editorial Serif Accent (Used Sparingly for Cinematic Flair) */
    .editorial-accent {{
      font-family: var(--font-editorial);
      font-style: italic;
      font-weight: 400;
      letter-spacing: -0.01em;
      color: #ffffff;
      display: inline-block;
      padding: 0 1px;
    }}

    /* 3D Universe Starfield Canvas */
    #universeCanvas {{
      position: fixed;
      inset: 0;
      width: 100vw;
      height: 100vh;
      z-index: 0;
      pointer-events: none;
      transition: filter 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s ease;
    }}

    body.world-open #universeCanvas {{
      filter: blur(16px) brightness(0.2);
      transform: scale(1.06);
    }}

    /* Subtle Cosmic Atmospheric Lighting */
    .cosmic-nebula-glow {{
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 1;
      background:
        radial-gradient(circle at 50% 15%, rgba(99, 102, 241, 0.07) 0%, transparent 60%),
        radial-gradient(circle at 85% 65%, rgba(6, 182, 212, 0.05) 0%, transparent 50%),
        radial-gradient(circle at 15% 75%, rgba(236, 72, 153, 0.04) 0%, transparent 50%),
        radial-gradient(circle at 50% 90%, rgba(16, 185, 129, 0.05) 0%, transparent 60%);
      mix-blend-mode: screen;
      opacity: 0.85;
      transition: opacity 0.8s ease;
    }}

    body.world-open .cosmic-nebula-glow {{
      opacity: 0.15;
    }}

    /* =========================================================
       GALACTIC TELEMETRY HUD & NAVIGATION
       ========================================================= */
    .galactic-hud {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      z-index: 100;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 16px 40px;
      background: rgba(1, 2, 6, 0.55);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid var(--border-subtle);
      transition: all 0.35s ease;
    }}

    .hud-brand {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: #fff;
    }}

    .hud-logo-icon {{
      width: 30px;
      height: 30px;
      border-radius: 8px;
      object-fit: contain;
      filter: drop-shadow(0 0 10px rgba(99, 102, 241, 0.35));
      transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .hud-brand:hover .hud-logo-icon {{
      transform: scale(1.08);
    }}

    .hud-brand-text {{
      display: flex;
      flex-direction: column;
    }}

    .hud-brand-name {{
      font-family: var(--font-display);
      font-size: 16px;
      font-weight: 700;
      letter-spacing: 0.06em;
      color: #ffffff;
      line-height: 1.1;
    }}

    .hud-brand-tag {{
      font-family: var(--font-mono);
      font-size: 9px;
      letter-spacing: 0.18em;
      color: var(--text-dim);
      text-transform: uppercase;
      margin-top: 2px;
    }}

    .hud-waypoints {{
      display: flex;
      align-items: center;
      gap: 4px;
      background: rgba(255, 255, 255, 0.025);
      padding: 4px 6px;
      border-radius: 999px;
      border: 1px solid var(--border-subtle);
    }}

    .waypoint-link {{
      font-family: var(--font-body);
      font-size: 12px;
      font-weight: 500;
      color: var(--text-muted);
      text-decoration: none;
      padding: 5px 12px;
      border-radius: 999px;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}

    .waypoint-dot {{
      width: 4px;
      height: 4px;
      border-radius: 50%;
      background: currentColor;
      opacity: 0.5;
    }}

    .waypoint-link:hover {{
      color: #ffffff;
      background: rgba(255, 255, 255, 0.06);
    }}

    .waypoint-link.active {{
      color: #ffffff;
      background: rgba(255, 255, 255, 0.1);
    }}

    .hud-telemetry {{
      display: flex;
      align-items: center;
      gap: 14px;
      font-family: var(--font-mono);
      font-size: 11px;
    }}

    .telemetry-indicator {{
      display: flex;
      align-items: center;
      gap: 7px;
      padding: 4px 11px;
      background: rgba(16, 185, 129, 0.06);
      border: 1px solid rgba(16, 185, 129, 0.2);
      border-radius: 999px;
      color: #34d399;
      font-size: 10px;
      letter-spacing: 0.06em;
    }}

    .pulse-dot {{
      width: 5px;
      height: 5px;
      border-radius: 50%;
      background: #34d399;
      box-shadow: 0 0 8px #34d399;
      animation: hudPulse 2.4s infinite ease-in-out;
    }}

    @keyframes hudPulse {{
      0%, 100% {{ transform: scale(1); opacity: 0.7; }}
      50% {{ transform: scale(1.35); opacity: 1; box-shadow: 0 0 12px #34d399; }}
    }}

    @media (max-width: 820px) {{
      .galactic-hud {{
        padding: 12px 20px;
      }}
      .hud-waypoints {{
        display: none;
      }}
    }}

    /* Main Viewport */
    .universe-viewport {{
      position: relative;
      z-index: 2;
      width: 100%;
    }}

    /* =========================================================
       1. HERO — THE NIVORA UNIVERSE CORE
       ========================================================= */
    .hero-universe {{
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      position: relative;
      padding: 105px 24px 50px;
      text-align: center;
      overflow: hidden;
    }}

    .hero-orbital-stage {{
      position: relative;
      width: 250px;
      height: 250px;
      margin-bottom: 22px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    /* Delicate Orbital Rings */
    .hero-ring {{
      position: absolute;
      border-radius: 50%;
      border: 1px solid rgba(255, 255, 255, 0.06);
      pointer-events: none;
      animation: rotateRing 32s linear infinite;
    }}

    .hero-ring.r1 {{
      width: 210px;
      height: 210px;
      border-color: rgba(99, 102, 241, 0.22);
      animation-duration: 24s;
    }}

    .hero-ring.r2 {{
      width: 250px;
      height: 250px;
      border-color: rgba(6, 182, 212, 0.16);
      animation-duration: 38s;
      animation-direction: reverse;
    }}

    .hero-ring.r3 {{
      width: 290px;
      height: 290px;
      border: 1px dashed rgba(255, 255, 255, 0.05);
      animation-duration: 52s;
    }}

    @keyframes rotateRing {{
      0% {{ transform: rotate(0deg); }}
      100% {{ transform: rotate(360deg); }}
    }}

    /* Floating Central Core */
    .hero-core-presence {{
      position: relative;
      width: 124px;
      height: 124px;
      border-radius: 30px;
      background: radial-gradient(circle at 35% 35%, rgba(99, 102, 241, 0.2), rgba(4, 6, 16, 0.92));
      border: 1px solid rgba(255, 255, 255, 0.12);
      box-shadow: 0 0 50px rgba(99, 102, 241, 0.25), inset 0 1px 1px rgba(255, 255, 255, 0.15);
      display: flex;
      align-items: center;
      justify-content: center;
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      animation: coreFloat 6s ease-in-out infinite alternate;
      z-index: 2;
    }}

    .hero-core-logo {{
      width: 76px;
      height: 76px;
      object-fit: contain;
      filter: drop-shadow(0 0 16px rgba(255, 255, 255, 0.3));
    }}

    @keyframes coreFloat {{
      0% {{ transform: translateY(0px) rotate(0deg); }}
      100% {{ transform: translateY(-10px) rotate(1.5deg); }}
    }}

    .hero-content {{
      max-width: 880px;
      margin: 0 auto;
      z-index: 3;
    }}

    .hero-micro-label {{
      display: inline-flex;
      align-items: center;
      gap: 7px;
      font-family: var(--font-mono);
      font-size: 10px;
      letter-spacing: 0.22em;
      color: #93c5fd;
      background: rgba(99, 102, 241, 0.08);
      border: 1px solid rgba(99, 102, 241, 0.24);
      padding: 5px 14px;
      border-radius: 999px;
      text-transform: uppercase;
      margin-bottom: 16px;
    }}

    .hero-title {{
      font-family: var(--font-display);
      font-size: clamp(52px, 8.5vw, 92px);
      font-weight: 700;
      letter-spacing: -0.04em;
      line-height: 1.0;
      color: #ffffff;
      margin-bottom: 14px;
    }}

    .hero-tagline {{
      font-family: var(--font-display);
      font-size: clamp(21px, 3.2vw, 34px);
      font-weight: 500;
      color: #e2e8f8;
      margin-bottom: 14px;
      letter-spacing: -0.02em;
      line-height: 1.25;
    }}

    .hero-sub {{
      font-family: var(--font-body);
      font-size: clamp(15px, 1.6vw, 17.5px);
      color: var(--text-muted);
      max-width: 640px;
      margin: 0 auto 30px;
      line-height: 1.65;
      font-weight: 400;
    }}

    .hero-actions {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 14px;
      flex-wrap: wrap;
    }}

    /* Buttons (Linear & Vercel Inspired) */
    .btn-universe {{
      font-family: var(--font-body);
      font-size: 13.5px;
      font-weight: 500;
      letter-spacing: 0.01em;
      padding: 13px 26px;
      border-radius: 999px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 9px;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
      border: none;
    }}

    .btn-universe-primary {{
      background: linear-gradient(180deg, #6366f1 0%, #4f46e5 100%);
      color: #ffffff;
      box-shadow: 0 0 24px rgba(99, 102, 241, 0.4), inset 0 1px 1px rgba(255, 255, 255, 0.4);
    }}

    .btn-universe-primary:hover {{
      transform: translateY(-2px);
      box-shadow: 0 0 32px rgba(99, 102, 241, 0.65), inset 0 1px 1px rgba(255, 255, 255, 0.6);
      color: #ffffff;
    }}

    .btn-universe-ghost {{
      background: rgba(255, 255, 255, 0.03);
      color: #cbd5e1;
      border: 1px solid var(--border-subtle);
      backdrop-filter: blur(12px);
    }}

    .btn-universe-ghost:hover {{
      background: rgba(255, 255, 255, 0.08);
      border-color: var(--border-hover);
      color: #ffffff;
      transform: translateY(-2px);
    }}

    .hero-scroll-cue {{
      margin-top: 48px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 9px;
      font-family: var(--font-mono);
      font-size: 10px;
      letter-spacing: 0.2em;
      color: var(--text-dim);
      text-transform: uppercase;
    }}

    .scroll-arrow-anim {{
      width: 18px;
      height: 28px;
      border: 1px solid var(--border-subtle);
      border-radius: 999px;
      display: flex;
      justify-content: center;
      padding-top: 5px;
    }}

    .scroll-arrow-dot {{
      width: 3px;
      height: 5px;
      border-radius: 999px;
      background: #818cf8;
      animation: scrollBounce 2s infinite ease;
    }}

    @keyframes scrollBounce {{
      0% {{ transform: translateY(0); opacity: 0.7; }}
      50% {{ transform: translateY(10px); opacity: 1; }}
      100% {{ transform: translateY(0); opacity: 0.7; }}
    }}

    /* =========================================================
       2. PLANETARY DESTINATIONS (4 CORE PRODUCTS)
       ========================================================= */
    .galaxy-corridor-section {{
      position: relative;
      padding: 60px 24px 110px;
      max-width: 1320px;
      margin: 0 auto;
    }}

    .corridor-header {{
      text-align: center;
      margin-bottom: 64px;
    }}

    .corridor-kicker {{
      font-family: var(--font-mono);
      font-size: 10.5px;
      letter-spacing: 0.22em;
      color: #67e8f9;
      text-transform: uppercase;
      margin-bottom: 12px;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }}

    .corridor-heading {{
      font-family: var(--font-display);
      font-size: clamp(30px, 4.5vw, 52px);
      font-weight: 700;
      color: #ffffff;
      letter-spacing: -0.03em;
      line-height: 1.15;
    }}

    .corridor-desc {{
      font-family: var(--font-body);
      font-size: clamp(14.5px, 1.6vw, 17px);
      color: var(--text-muted);
      max-width: 660px;
      margin: 14px auto 0;
      line-height: 1.65;
    }}

    .destinations-flight-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 28px;
    }}

    @media (max-width: 960px) {{
      .destinations-flight-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    /* Celestial Destination Planet Card */
    .destination-planet-card {{
      position: relative;
      background: var(--glass-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 26px;
      padding: clamp(22px, 3vw, 32px);
      backdrop-filter: blur(28px);
      -webkit-backdrop-filter: blur(28px);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .destination-planet-card:hover {{
      transform: translateY(-6px);
      border-color: var(--border-hover);
    }}

    .destination-planet-card.p-checkra:hover {{
      box-shadow: 0 16px 50px rgba(99, 102, 241, 0.18), 0 0 1px rgba(99, 102, 241, 0.5);
    }}

    .destination-planet-card.p-homora:hover {{
      box-shadow: 0 16px 50px rgba(6, 182, 212, 0.18), 0 0 1px rgba(6, 182, 212, 0.5);
    }}

    .destination-planet-card.p-bubora:hover {{
      box-shadow: 0 16px 50px rgba(236, 72, 153, 0.18), 0 0 1px rgba(236, 72, 153, 0.5);
    }}

    .destination-planet-card.p-sayora:hover {{
      box-shadow: 0 16px 50px rgba(16, 185, 129, 0.18), 0 0 1px rgba(16, 185, 129, 0.5);
    }}

    /* Emblem Stage */
    .planet-emblem-stage {{
      position: relative;
      height: 160px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 22px;
      border-radius: 18px;
      background: radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.02) 0%, rgba(0, 0, 0, 0.45) 100%);
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.04);
    }}

    .planet-emblem-img {{
      max-height: 110px;
      max-width: 78%;
      object-fit: contain;
      filter: drop-shadow(0 0 18px rgba(255, 255, 255, 0.12));
      transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), filter 0.5s ease;
    }}

    .destination-planet-card:hover .planet-emblem-img {{
      transform: scale(1.06);
      filter: drop-shadow(0 0 24px rgba(255, 255, 255, 0.25));
    }}

    .planet-emblem-ring {{
      position: absolute;
      width: 150px;
      height: 150px;
      border-radius: 50%;
      border: 1px solid rgba(255, 255, 255, 0.06);
      pointer-events: none;
      animation: rotateRing 32s linear infinite;
    }}

    /* Metadata */
    .destination-meta-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 10px;
    }}

    .destination-theme-tag {{
      font-family: var(--font-mono);
      font-size: 10.5px;
      letter-spacing: 0.15em;
      text-transform: uppercase;
    }}

    .p-checkra .destination-theme-tag {{ color: #a5b4fc; }}
    .p-homora .destination-theme-tag {{ color: #67e8f9; }}
    .p-bubora .destination-theme-tag {{ color: #f472b6; }}
    .p-sayora .destination-theme-tag {{ color: #6ee7b7; }}

    .destination-status-badge {{
      font-family: var(--font-mono);
      font-size: 10px;
      padding: 3px 9px;
      border-radius: 999px;
      letter-spacing: 0.08em;
    }}

    .status-live {{
      background: rgba(16, 185, 129, 0.08);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.25);
    }}

    .status-concept {{
      background: rgba(99, 102, 241, 0.08);
      color: #a5b4fc;
      border: 1px solid rgba(99, 102, 241, 0.25);
    }}

    .destination-name {{
      font-family: var(--font-display);
      font-size: 26px;
      font-weight: 700;
      color: #ffffff;
      letter-spacing: -0.02em;
      margin-bottom: 6px;
    }}

    .destination-tagline {{
      font-family: var(--font-body);
      font-size: 14px;
      color: var(--text-secondary);
      line-height: 1.55;
      margin-bottom: 18px;
      min-height: 44px;
    }}

    .destination-caps-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 7px;
      margin-bottom: 24px;
    }}

    .cap-tag-pill {{
      font-family: var(--font-mono);
      font-size: 10.5px;
      color: var(--text-muted);
      background: rgba(255, 255, 255, 0.025);
      border: 1px solid rgba(255, 255, 255, 0.05);
      padding: 4px 10px;
      border-radius: 999px;
      letter-spacing: 0.02em;
      transition: all 0.2s ease;
    }}

    .destination-planet-card:hover .cap-tag-pill {{
      background: rgba(255, 255, 255, 0.05);
      color: #f1f5f9;
      border-color: rgba(255, 255, 255, 0.12);
    }}

    .destination-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
      padding-top: 16px;
      border-top: 1px solid rgba(255, 255, 255, 0.05);
    }}

    .btn-explore-concept {{
      font-family: var(--font-body);
      font-size: 13px;
      font-weight: 500;
      padding: 10px 20px;
      border-radius: 999px;
      background: #ffffff;
      color: #010206;
      border: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      cursor: pointer;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .btn-explore-concept:hover {{
      transform: translateY(-2px);
      background: #f1f5f9;
      box-shadow: 0 4px 18px rgba(255, 255, 255, 0.25);
    }}

    .btn-visit-app {{
      font-family: var(--font-body);
      font-size: 12.5px;
      font-weight: 400;
      color: var(--text-muted);
      text-decoration: none;
      padding: 9px 16px;
      border-radius: 999px;
      border: 1px solid var(--border-subtle);
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }}

    .btn-visit-app:hover {{
      color: #ffffff;
      border-color: var(--border-hover);
      background: rgba(255, 255, 255, 0.04);
    }}

    /* =========================================================
       3. DEDICATED PRODUCT PORTFOLIO INTERFACE (FIXED MODAL)
       ========================================================= */
    #universeWorldInterface {{
      position: fixed;
      inset: 0;
      z-index: 9999;
      display: flex;
      flex-direction: column;
      background: var(--glass-surface-dense);
      backdrop-filter: blur(36px);
      -webkit-backdrop-filter: blur(36px);
      opacity: 0;
      pointer-events: none;
      transform: scale(0.95);
      transition: opacity 0.4s cubic-bezier(0.16, 1, 0.3, 1), transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      overflow: hidden;
    }}

    #universeWorldInterface.active {{
      opacity: 1;
      pointer-events: auto;
      transform: scale(1);
    }}

    /* Top Bar */
    .world-top-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 14px 36px;
      background: rgba(1, 2, 6, 0.7);
      border-bottom: 1px solid var(--border-subtle);
      position: sticky;
      top: 0;
      z-index: 10;
      backdrop-filter: blur(20px);
    }}

    .world-top-left {{
      display: flex;
      align-items: center;
      gap: 18px;
    }}

    .btn-return-universe {{
      font-family: var(--font-body);
      font-size: 12.5px;
      font-weight: 500;
      color: #ffffff;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 7px 16px;
      border-radius: 999px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      transition: all 0.2s ease;
    }}

    .btn-return-universe:hover {{
      background: rgba(255, 255, 255, 0.1);
      border-color: rgba(255, 255, 255, 0.25);
      transform: translateX(-2px);
    }}

    .world-brand-subtle {{
      display: flex;
      align-items: center;
      gap: 9px;
      padding-left: 16px;
      border-left: 1px solid var(--border-subtle);
    }}

    .wbs-nivora {{
      font-family: var(--font-mono);
      font-size: 10px;
      letter-spacing: 0.16em;
      color: var(--text-dim);
      text-transform: uppercase;
    }}

    .wbs-product-name {{
      font-family: var(--font-display);
      font-size: 15px;
      font-weight: 700;
      color: #ffffff;
    }}

    .wbs-status-badge {{
      font-family: var(--font-mono);
      font-size: 9.5px;
      padding: 2px 7px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.06);
      color: #cbd5e1;
    }}

    .world-nav-tabs {{
      display: flex;
      align-items: center;
      gap: 4px;
      background: rgba(255, 255, 255, 0.025);
      padding: 3px 5px;
      border-radius: 999px;
      border: 1px solid var(--border-subtle);
    }}

    .world-nav-tab {{
      font-family: var(--font-body);
      font-size: 12px;
      font-weight: 500;
      color: var(--text-muted);
      background: none;
      border: none;
      padding: 5px 12px;
      border-radius: 999px;
      cursor: pointer;
      transition: all 0.2s ease;
    }}

    .world-nav-tab:hover {{
      color: #ffffff;
      background: rgba(255, 255, 255, 0.05);
    }}

    .world-nav-tab.active {{
      color: #ffffff;
      background: rgba(255, 255, 255, 0.1);
    }}

    .world-top-right {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .world-launch-btn {{
      font-family: var(--font-body);
      font-size: 12.5px;
      font-weight: 500;
      background: linear-gradient(180deg, #6366f1 0%, #4f46e5 100%);
      color: #ffffff;
      text-decoration: none;
      padding: 7px 16px;
      border-radius: 999px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 0 16px rgba(99, 102, 241, 0.35);
      transition: all 0.2s ease;
    }}

    .world-launch-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 0 22px rgba(99, 102, 241, 0.55);
      color: #ffffff;
    }}

    .world-close-x {{
      background: none;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      padding: 6px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s ease;
    }}

    .world-close-x:hover {{
      color: #ffffff;
      background: rgba(255, 255, 255, 0.07);
    }}

    /* Scrollable Body inside World */
    .world-scrollable-body {{
      flex: 1;
      overflow-y: auto;
      padding: 36px clamp(20px, 5vw, 72px) 90px;
      scroll-behavior: smooth;
    }}

    .world-product-view {{
      display: none;
      max-width: 1240px;
      margin: 0 auto;
    }}

    .world-product-view.active {{
      display: block;
      animation: fadeInWorld 0.35s ease forwards;
    }}

    @keyframes fadeInWorld {{
      from {{ opacity: 0; transform: translateY(10px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .world-sec {{
      margin-bottom: 50px;
      padding-top: 20px;
    }}

    .world-sec-title {{
      font-family: var(--font-mono);
      font-size: 10px;
      letter-spacing: 0.2em;
      color: #93c5fd;
      text-transform: uppercase;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      margin-bottom: 10px;
    }}

    .world-sec-heading {{
      font-family: var(--font-display);
      font-size: clamp(23px, 3vw, 34px);
      font-weight: 700;
      color: #ffffff;
      letter-spacing: -0.02em;
      margin-bottom: 20px;
    }}

    .world-intro-lead {{
      font-family: var(--font-body);
      font-size: clamp(15.5px, 1.8vw, 19px);
      line-height: 1.65;
      color: #cbd5e1;
      max-width: 960px;
      background: rgba(255, 255, 255, 0.015);
      border: 1px solid var(--border-subtle);
      border-radius: 18px;
      padding: 24px 28px;
      border-left: 3px solid #6366f1;
    }}

    /* Capability Cards */
    .world-grid-4 {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 18px;
    }}

    @media (max-width: 1060px) {{
      .world-grid-4 {{
        grid-template-columns: repeat(2, 1fr);
      }}
    }}

    @media (max-width: 580px) {{
      .world-grid-4 {{
        grid-template-columns: 1fr;
      }}
    }}

    .world-cap-card {{
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border-subtle);
      border-radius: 16px;
      padding: 22px;
      transition: all 0.25s ease;
    }}

    .world-cap-card:hover {{
      background: rgba(255, 255, 255, 0.05);
      border-color: var(--border-hover);
      transform: translateY(-3px);
    }}

    .world-cap-icon {{
      width: 38px;
      height: 38px;
      border-radius: 10px;
      background: rgba(99, 102, 241, 0.1);
      color: #a5b4fc;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 14px;
      border: 1px solid rgba(99, 102, 241, 0.2);
    }}

    .world-cap-card h5 {{
      font-family: var(--font-display);
      font-size: 16px;
      font-weight: 600;
      color: #ffffff;
      margin-bottom: 7px;
    }}

    .world-cap-card p {{
      font-family: var(--font-body);
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    /* Workflow Pipeline */
    .world-workflow-steps {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 15px;
    }}

    @media (max-width: 880px) {{
      .world-workflow-steps {{
        grid-template-columns: 1fr;
      }}
    }}

    .workflow-step-box {{
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border-subtle);
      border-radius: 16px;
      padding: 20px;
    }}

    .step-index-badge {{
      font-family: var(--font-mono);
      font-size: 9.5px;
      letter-spacing: 0.15em;
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.08);
      border: 1px solid rgba(56, 189, 248, 0.2);
      padding: 2px 7px;
      border-radius: 999px;
      display: inline-block;
      margin-bottom: 10px;
    }}

    .workflow-step-box h6 {{
      font-family: var(--font-display);
      font-size: 15px;
      font-weight: 600;
      color: #ffffff;
      margin-bottom: 5px;
    }}

    .workflow-step-box p {{
      font-family: var(--font-body);
      font-size: 12.5px;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    /* Architecture Grid */
    .world-grid-2 {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 18px;
    }}

    @media (max-width: 780px) {{
      .world-grid-2 {{
        grid-template-columns: 1fr;
      }}
    }}

    .arch-card {{
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border-subtle);
      border-radius: 16px;
      padding: 24px;
    }}

    .arch-card h5 {{
      font-family: var(--font-display);
      font-size: 17px;
      font-weight: 600;
      color: #ffffff;
      margin-bottom: 7px;
    }}

    .arch-card p {{
      font-family: var(--font-body);
      font-size: 13.5px;
      color: var(--text-muted);
      line-height: 1.6;
    }}

    /* =========================================================
       4. REST OF THE UNIVERSE (ECOSYSTEM, FOLIVIO, FOUNDER, CONTACT)
       ========================================================= */
    .universe-rest-section {{
      position: relative;
      padding: 80px 24px;
      max-width: 1240px;
      margin: 0 auto;
    }}

    /* Ecosystem */
    .ecosystem-block {{
      background: var(--glass-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 30px;
      padding: clamp(28px, 4.5vw, 56px);
      backdrop-filter: blur(28px);
      margin-bottom: 70px;
    }}

    .eco-header {{
      text-align: center;
      max-width: 760px;
      margin: 0 auto 42px;
    }}

    .eco-pillars-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 18px;
    }}

    @media (max-width: 900px) {{
      .eco-pillars-grid {{
        grid-template-columns: repeat(2, 1fr);
      }}
    }}

    @media (max-width: 540px) {{
      .eco-pillars-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .pillar-card {{
      background: rgba(255, 255, 255, 0.015);
      border: 1px solid var(--border-subtle);
      border-radius: 18px;
      padding: 22px;
      text-align: center;
    }}

    .pillar-badge {{
      font-family: var(--font-mono);
      font-size: 10px;
      letter-spacing: 0.15em;
      padding: 3px 9px;
      border-radius: 999px;
      display: inline-block;
      margin-bottom: 10px;
    }}

    .pillar-card h4 {{
      font-family: var(--font-display);
      font-size: 18px;
      color: #ffffff;
      margin-bottom: 7px;
    }}

    .pillar-card p {{
      font-family: var(--font-body);
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    /* FOLIVIO Section */
    .folivio-satellite-card {{
      background: radial-gradient(circle at 12% 20%, rgba(99, 102, 241, 0.06) 0%, rgba(5, 7, 16, 0.88) 100%);
      border: 1px solid var(--border-subtle);
      border-radius: 30px;
      padding: clamp(28px, 4.5vw, 52px);
      display: grid;
      grid-template-columns: auto 1fr;
      gap: 36px;
      align-items: center;
      margin-bottom: 70px;
    }}

    @media (max-width: 820px) {{
      .folivio-satellite-card {{
        grid-template-columns: 1fr;
        text-align: center;
      }}
      .folivio-logo-box {{
        margin: 0 auto;
      }}
    }}

    .folivio-logo-box {{
      width: 130px;
      height: 130px;
      border-radius: 24px;
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 16px;
    }}

    .folivio-logo-img {{
      width: 100%;
      height: 100%;
      object-fit: contain;
    }}

    .folivio-badge {{
      font-family: var(--font-mono);
      font-size: 10px;
      letter-spacing: 0.2em;
      color: #f472b6;
      text-transform: uppercase;
      margin-bottom: 8px;
    }}

    .folivio-title {{
      font-family: var(--font-display);
      font-size: clamp(26px, 3.2vw, 38px);
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 10px;
    }}

    .folivio-desc {{
      font-family: var(--font-body);
      font-size: 15px;
      color: var(--text-secondary);
      line-height: 1.6;
      max-width: 660px;
      margin-bottom: 22px;
    }}

    /* Founder Section */
    .founder-cosmos-card {{
      background: var(--glass-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 30px;
      padding: clamp(28px, 4.5vw, 56px);
      display: grid;
      grid-template-columns: 300px 1fr;
      gap: 44px;
      align-items: center;
      margin-bottom: 70px;
    }}

    @media (max-width: 860px) {{
      .founder-cosmos-card {{
        grid-template-columns: 1fr;
        text-align: center;
      }}
      .founder-photo-box {{
        margin: 0 auto;
      }}
    }}

    .founder-photo-box {{
      position: relative;
      border-radius: 24px;
      overflow: hidden;
      border: 1px solid var(--border-subtle);
      box-shadow: 0 0 30px rgba(99, 102, 241, 0.16);
    }}

    .founder-photo-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }}

    .founder-kicker {{
      font-family: var(--font-mono);
      font-size: 10.5px;
      letter-spacing: 0.2em;
      color: #93c5fd;
      text-transform: uppercase;
      margin-bottom: 8px;
    }}

    .founder-name {{
      font-family: var(--font-display);
      font-size: clamp(30px, 3.8vw, 44px);
      font-weight: 700;
      color: #ffffff;
      line-height: 1.1;
      margin-bottom: 6px;
    }}

    .founder-role {{
      font-family: var(--font-mono);
      font-size: 12px;
      color: #38bdf8;
      margin-bottom: 18px;
    }}

    .founder-bio {{
      font-family: var(--font-body);
      font-size: 15px;
      color: var(--text-secondary);
      line-height: 1.65;
      margin-bottom: 22px;
    }}

    /* Transmission Console */
    .transmission-console {{
      background: radial-gradient(circle at 50% 0%, rgba(99, 102, 241, 0.1) 0%, rgba(4, 6, 16, 0.95) 100%);
      border: 1px solid var(--border-subtle);
      border-radius: 30px;
      padding: clamp(28px, 4.5vw, 56px);
      max-width: 820px;
      margin: 0 auto 70px;
      text-align: center;
    }}

    .transmission-form {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 14px;
      margin-top: 28px;
      text-align: left;
    }}

    @media (max-width: 620px) {{
      .transmission-form {{
        grid-template-columns: 1fr;
      }}
    }}

    .form-field-full {{
      grid-column: 1 / -1;
    }}

    .form-input {{
      width: 100%;
      background: rgba(255, 255, 255, 0.035);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 13px 16px;
      color: #ffffff;
      font-family: var(--font-body);
      font-size: 13.5px;
      outline: none;
      transition: all 0.2s ease;
    }}

    .form-input:focus {{
      border-color: #6366f1;
      background: rgba(255, 255, 255, 0.06);
      box-shadow: 0 0 14px rgba(99, 102, 241, 0.25);
    }}

    /* Cosmic Footer */
    .cosmic-footer {{
      padding: 44px 24px;
      text-align: center;
      border-top: 1px solid var(--border-subtle);
      font-size: 12.5px;
      color: var(--text-dim);
      font-family: var(--font-mono);
    }}

    .footer-telemetry-row {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 20px;
      flex-wrap: wrap;
      margin-bottom: 14px;
    }}

    .footer-copy {{
      font-family: var(--font-body);
      color: var(--text-muted);
      font-size: 13px;
    }}
  </style>
</head>
<body>

  <!-- BACKGROUND 3D GALAXY CANVAS -->
  <canvas id="universeCanvas"></canvas>
  <div class="cosmic-nebula-glow"></div>

  <!-- GALACTIC HUD & NAVIGATION BAR -->
  <header class="galactic-hud">
    <a href="#" class="hud-brand" aria-label="NIVORA Home">
      <img src="assets/images/nivora-logo.png" alt="NIVORA Core Logo" class="hud-logo-icon">
      <div class="hud-brand-text">
        <span class="hud-brand-name">NIVORA</span>
        <span class="hud-brand-tag">Universe v2.5</span>
      </div>
    </a>

    <nav class="hud-waypoints" aria-label="Universe Flight Navigation">
      <a href="#hero" class="waypoint-link active" onclick="smoothWarpTo('hero')"><span class="waypoint-dot"></span>Core</a>
      <a href="#destinations" class="waypoint-link" onclick="smoothWarpTo('destinations')"><span class="waypoint-dot"></span>Destinations</a>
      <a href="#ecosystem" class="waypoint-link" onclick="smoothWarpTo('ecosystem')"><span class="waypoint-dot"></span>Ecosystem</a>
      <a href="#folivio" class="waypoint-link" onclick="smoothWarpTo('folivio')"><span class="waypoint-dot"></span>FOLIVIO</a>
      <a href="#founder" class="waypoint-link" onclick="smoothWarpTo('founder')"><span class="waypoint-dot"></span>Architect</a>
      <a href="#contact" class="waypoint-link" onclick="smoothWarpTo('contact')"><span class="waypoint-dot"></span>Transmit</a>
    </nav>

    <div class="hud-telemetry">
      <div class="telemetry-indicator">
        <span class="pulse-dot"></span>
        <span id="telemetryStatusText">ORBIT: STABLE</span>
      </div>
    </div>
  </header>

  <!-- MAIN SCROLLABLE UNIVERSE VIEWPORT -->
  <main class="universe-viewport">

    <!-- =========================================================
         1. HERO — ENTER THE NIVORA UNIVERSE
         ========================================================= -->
    <section class="hero-universe" id="hero">
      <div class="hero-orbital-stage">
        <div class="hero-ring r1"></div>
        <div class="hero-ring r2"></div>
        <div class="hero-ring r3"></div>
        <div class="hero-core-presence">
          <img src="assets/images/nivora-logo.png" alt="NIVORA Core Presence" class="hero-core-logo">
        </div>
      </div>

      <div class="hero-content">
        <div class="hero-micro-label">Sector 00 &middot; Innovation Universe</div>
        <h1 class="hero-title">NIVORA</h1>
        <div class="hero-tagline">
          Turning <span class="editorial-accent">Ideas</span> Into Intelligent <span class="editorial-accent">Products</span>.
        </div>
        <p class="hero-sub">
          A technology <span class="editorial-accent">Universe</span> built by Nivas Bennabatthula &mdash; where ambitious concepts transform into resilient, high-craft digital products that solve real human frictions.
        </p>

        <div class="hero-actions">
          <button type="button" class="btn-universe btn-universe-primary" onclick="initiateUniverseWarp()">
            <span>ENTER THE UNIVERSE</span>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
          </button>
          <a href="#destinations" class="btn-universe btn-universe-ghost" onclick="smoothWarpTo('destinations')">
            <span>EXPLORE PRODUCTS</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 8 12 12 14 14"></polyline></svg>
          </a>
        </div>

        <div class="hero-scroll-cue">
          <div class="scroll-arrow-anim">
            <div class="scroll-arrow-dot"></div>
          </div>
          <span>Scroll to Travel Through Space</span>
        </div>
      </div>
    </section>

    <!-- =========================================================
         2. SCROLL = TRAVEL THROUGH SPACE (4 CORE PRODUCT DESTINATIONS)
         ========================================================= -->
    <section class="galaxy-corridor-section" id="destinations">
      <div class="corridor-header">
        <div class="corridor-kicker">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
          <span>Sector 01 &middot; Planetary Destinations</span>
        </div>
        <h2 class="corridor-heading">
          Discover the <span class="editorial-accent">Universe</span> of Products
        </h2>
        <p class="corridor-desc">
          Four distinct celestial worlds engineered to solve fundamental frictions in writing integrity, shared living finance, private relationship spaces, and financial resilience.
        </p>
      </div>

      <div class="destinations-flight-grid">

        <!-- 01. CHECKRA DESTINATION -->
        <article class="destination-planet-card p-checkra" id="dest-checkra">
          <div class="planet-emblem-stage">
            <div class="planet-emblem-ring"></div>
            <img src="assets/images/checkra-emblem.png" alt="CHECKRA Emblem" class="planet-emblem-img">
          </div>

          <div class="destination-info-body">
            <div class="destination-meta-row">
              <span class="destination-theme-tag">Theme &middot; Integrity</span>
              <span class="destination-status-badge status-live">Live Product</span>
            </div>
            <h3 class="destination-name">CHECKRA</h3>
            <p class="destination-tagline">Your Intelligent Writing Integrity Space &mdash; similarity detection, source verification, and AI-driven document intelligence.</p>

            <div class="destination-caps-pills">
              <span class="cap-tag-pill">Similarity Check</span>
              <span class="cap-tag-pill">Source Verification</span>
              <span class="cap-tag-pill">AI Review</span>
              <span class="cap-tag-pill">Grammar Intel</span>
            </div>
          </div>

          <div class="destination-actions">
            <button type="button" class="btn-explore-concept" onclick="zoomIntoWorld('checkra', this)">
              <span>Explore Concept</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </button>
            <a href="https://checkra-xi.vercel.app/" target="_blank" rel="noopener noreferrer" class="btn-visit-app">
              <span>Visit App</span>
              <span class="btn-arrow">↗</span>
            </a>
          </div>
        </article>

        <!-- 02. HOMORA DESTINATION -->
        <article class="destination-planet-card p-homora" id="dest-homora">
          <div class="planet-emblem-stage">
            <div class="planet-emblem-ring"></div>
            <img src="assets/images/homora-logo.png" alt="HOMORA Emblem" class="planet-emblem-img">
          </div>

          <div class="destination-info-body">
            <div class="destination-meta-row">
              <span class="destination-theme-tag">Theme &middot; Harmony</span>
              <span class="destination-status-badge status-live">Active Prototype</span>
            </div>
            <h3 class="destination-name">HOMORA</h3>
            <p class="destination-tagline">AI-Powered Financial Harmony for Shared Living &mdash; smart expense splits, recurring bills, chore tracking, and household intel.</p>

            <div class="destination-caps-pills">
              <span class="cap-tag-pill">Shared Finance</span>
              <span class="cap-tag-pill">Household OS</span>
              <span class="cap-tag-pill">Bill Tracking</span>
              <span class="cap-tag-pill">Expense Intel</span>
            </div>
          </div>

          <div class="destination-actions">
            <button type="button" class="btn-explore-concept" onclick="zoomIntoWorld('homora', this)">
              <span>Explore Concept</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </button>
            <a href="https://homora-ai.vercel.app/" target="_blank" rel="noopener noreferrer" class="btn-visit-app">
              <span>Visit Prototype</span>
              <span class="btn-arrow">↗</span>
            </a>
          </div>
        </article>

        <!-- 03. BUBORA DESTINATION -->
        <article class="destination-planet-card p-bubora" id="dest-bubora">
          <div class="planet-emblem-stage">
            <div class="planet-emblem-ring"></div>
            <img src="assets/images/bubora-logo.png" alt="BUBORA Emblem" class="planet-emblem-img">
          </div>

          <div class="destination-info-body">
            <div class="destination-meta-row">
              <span class="destination-theme-tag">Theme &middot; Connection</span>
              <span class="destination-status-badge status-live">Live Product</span>
            </div>
            <h3 class="destination-name">BUBORA</h3>
            <p class="destination-tagline">A Private Digital Home for Two &mdash; end-to-end encrypted messaging, shared timelines, dream vacations, and relationship milestones.</p>

            <div class="destination-caps-pills">
              <span class="cap-tag-pill">Private Chat</span>
              <span class="cap-tag-pill">Shared Memories</span>
              <span class="cap-tag-pill">Couple Goals</span>
              <span class="cap-tag-pill">Private Vault</span>
            </div>
          </div>

          <div class="destination-actions">
            <button type="button" class="btn-explore-concept" onclick="zoomIntoWorld('bubora', this)">
              <span>Explore Concept</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </button>
            <a href="https://bubora.netlify.app/" target="_blank" rel="noopener noreferrer" class="btn-visit-app">
              <span>Visit App</span>
              <span class="btn-arrow">↗</span>
            </a>
          </div>
        </article>

        <!-- 04. SAYORA DESTINATION -->
        <article class="destination-planet-card p-sayora" id="dest-sayora">
          <div class="planet-emblem-stage">
            <div class="planet-emblem-ring"></div>
            <img src="assets/images/sayora-emblem.png" alt="SAYORA Emblem" class="planet-emblem-img">
          </div>

          <div class="destination-info-body">
            <div class="destination-meta-row">
              <span class="destination-theme-tag">Theme &middot; Resilience</span>
              <span class="destination-status-badge status-concept">Concept &middot; In Dev</span>
            </div>
            <h3 class="destination-name">SAYORA</h3>
            <p class="destination-tagline">Intelligent Financial Resilience Space &mdash; micro-savings, community emergency funds, and dignified financial safety for daily-wage workers.</p>

            <div class="destination-caps-pills">
              <span class="cap-tag-pill">Smart Savings</span>
              <span class="cap-tag-pill">Protection Fund</span>
              <span class="cap-tag-pill">Community Shield</span>
              <span class="cap-tag-pill">SAYORA ID</span>
            </div>
          </div>

          <div class="destination-actions">
            <button type="button" class="btn-explore-concept" onclick="zoomIntoWorld('sayora', this)">
              <span>Explore Concept</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </button>
          </div>
        </article>

      </div>
    </section>

    <!-- =========================================================
         4. REST OF THE UNIVERSE (ECOSYSTEM, FOLIVIO, FOUNDER, TRANSMIT)
         ========================================================= -->
    <div class="universe-rest-section">

      <!-- THE ECOSYSTEM CONSTELLATION -->
      <section class="ecosystem-block" id="ecosystem">
        <div class="eco-header">
          <div class="corridor-kicker">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="2" x2="12" y2="6"></line><line x1="12" y1="18" x2="12" y2="22"></line><line x1="4.93" y1="4.93" x2="7.76" y2="7.76"></line><line x1="16.24" y1="16.24" x2="19.07" y2="19.07"></line><line x1="2" y1="12" x2="6" y2="12"></line><line x1="18" y1="12" x2="22" y2="12"></line></svg>
            <span>The NIVORA Architecture</span>
          </div>
          <h2 class="corridor-heading">
            One <span class="editorial-accent">Universe</span>. Different <span class="editorial-accent">Possibilities</span>.
          </h2>
          <p class="corridor-desc">
            Ideas become products when technology meets purpose. Each product addresses a distinct dimension of human living, connected by shared foundations in privacy, craft, and autonomous intelligence.
          </p>
        </div>

        <div class="eco-pillars-grid">
          <div class="pillar-card">
            <span class="pillar-badge" style="background:rgba(99,102,241,0.1);color:#a5b4fc;border:1px solid rgba(99,102,241,0.25)">01 &middot; INTEGRITY</span>
            <h4>CHECKRA</h4>
            <p>Elevating academic and creative writing through factual similarity detection, citations, and evidence reviews.</p>
          </div>
          <div class="pillar-card">
            <span class="pillar-badge" style="background:rgba(6,182,212,0.1);color:#67e8f9;border:1px solid rgba(6,182,212,0.25)">02 &middot; HARMONY</span>
            <h4>HOMORA</h4>
            <p>Eliminating interpersonal household financial friction through intelligent expense orchestration and automated splits.</p>
          </div>
          <div class="pillar-card">
            <span class="pillar-badge" style="background:rgba(236,72,153,0.1);color:#f472b6;border:1px solid rgba(236,72,153,0.25)">03 &middot; CONNECTION</span>
            <h4>BUBORA</h4>
            <p>Protecting intimacy in the digital age with end-to-end encrypted private sanctuaries for committed partners.</p>
          </div>
          <div class="pillar-card">
            <span class="pillar-badge" style="background:rgba(16,185,129,0.1);color:#6ee7b7;border:1px solid rgba(16,185,129,0.25)">04 &middot; RESILIENCE</span>
            <h4>SAYORA</h4>
            <p>Empowering vulnerable unorganized workers with dignity, micro-savings, and community-backed emergency cushions.</p>
          </div>
        </div>
      </section>

      <!-- FOLIVIO SECTION (DISTINCT FROM PRODUCT UNIVERSE) -->
      <section class="folivio-satellite-card" id="folivio">
        <div class="folivio-logo-box">
          <img src="assets/images/folivio-logo.webp" alt="FOLIVIO" class="folivio-logo-img">
        </div>
        <div class="folivio-copy-content">
          <div class="folivio-badge">Career Branding &middot; Digital Presence</div>
          <h3 class="folivio-title">FOLIVIO</h3>
          <p class="folivio-desc">
            Independent professional career-branding service founded by Nivas &mdash; helping ambitious students, freshers, and professionals turn their projects, certifications, and experience into polished, magnetic digital portfolios.
          </p>
          <div style="display:flex;gap:14px;align-items:center;flex-wrap:wrap;">
            <a href="https://folivio.in" target="_blank" rel="noopener noreferrer" class="btn-universe btn-universe-primary">
              <span>Explore FOLIVIO</span>
              <span class="btn-arrow">↗</span>
            </a>
            <a href="https://www.instagram.com/folivio.ai?utm_source=ig_web_button_share_sheet&rpxt=ZDNlZDc0MzIxNw==" target="_blank" rel="noopener noreferrer" class="btn-universe btn-universe-ghost">
              <span>Instagram @folivio.ai</span>
            </a>
          </div>
        </div>
      </section>

      <!-- FOUNDER & ARCHITECT SECTION -->
      <section class="founder-cosmos-card" id="founder">
        <div class="founder-photo-box">
          <img src="assets/images/founder-nivas.png" alt="Nivas Bennabatthula &mdash; Founder" class="founder-photo-img">
        </div>
        <div class="founder-content-body">
          <div class="founder-kicker">Founder &middot; Product Architect</div>
          <h3 class="founder-name">Nivas<br><span style="color:#818cf8">Bennabatthula</span></h3>
          <div class="founder-role">Founder &middot; Systems Architect &middot; Product Designer</div>
          <p class="founder-bio">
            Nivas is building NIVORA as an integrated <span class="editorial-accent">Innovation</span> sanctuary where high-order software engineering converges with human-first design. Believing that software should feel alive, deeply purposeful, and cinematic, every project in the universe is envisioned, designed, and engineered under an uncompromising standard of craft.
          </p>
          <div style="display:flex;gap:12px;flex-wrap:wrap;">
            <a href="#contact" class="btn-universe btn-universe-primary" onclick="smoothWarpTo('contact')">
              <span>Initiate Transmission</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
            </a>
          </div>
        </div>
      </section>

      <!-- TRANSMISSION CONSOLE (CONTACT) -->
      <section class="transmission-console" id="contact">
        <div class="corridor-kicker">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
          <span>Sector 07 &middot; Deep Space Transmission</span>
        </div>
        <h2 class="corridor-heading">Connect With NIVORA</h2>
        <p class="corridor-desc" style="margin-bottom: 22px;">
          Have a partnership inquiry, technical collaboration, or visionary product idea? Transmit your signal directly to Nivas.
        </p>

        <form class="transmission-form" onsubmit="handleTransmission(event)">
          <div>
            <input type="text" class="form-input" placeholder="Your Name" required>
          </div>
          <div>
            <input type="email" class="form-input" placeholder="Your Email / Signal" required>
          </div>
          <div class="form-field-full">
            <input type="text" class="form-input" placeholder="Subject / Sector of Interest" required>
          </div>
          <div class="form-field-full">
            <textarea class="form-input" rows="4" placeholder="Transmit your message..." required></textarea>
          </div>
          <div class="form-field-full" style="text-align: center; margin-top: 8px;">
            <button type="submit" class="btn-universe btn-universe-primary" id="transmitBtn">
              <span>DISPATCH TRANSMISSION</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
            </button>
            <div id="transmissionToast" style="display:none;margin-top:12px;color:#34d399;font-family:var(--font-mono);font-size:12px;"></div>
          </div>
        </form>
      </section>

    </div>

    <!-- COSMIC TELEMETRY FOOTER -->
    <footer class="cosmic-footer">
      <div class="footer-telemetry-row">
        <span>NIVORA UNIVERSE</span>
        <span>&bull;</span>
        <span>COORDINATES: 17.3850&deg; N, 78.4867&deg; E</span>
        <span>&bull;</span>
        <span>TELEMETRY: ACTIVE</span>
      </div>
      <p class="footer-copy">
        &copy; 2026 NIVORA &middot; Founded &amp; Architected by Nivas Bennabatthula. All rights reserved.
      </p>
    </footer>

  </main>

  <!-- =========================================================
       DEDICATED PRODUCT PORTFOLIO INTERFACE (ZOOM ENVIRONMENT)
       ========================================================= -->
  <div id="universeWorldInterface" role="dialog" aria-modal="true" aria-hidden="true">
    <!-- Top Bar -->
    <header class="world-top-bar">
      <div class="world-top-left">
        <button type="button" class="btn-return-universe" onclick="returnToUniverse()" aria-label="Return to NIVORA Universe (ESC)">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
          <span>Return to Universe</span>
        </button>

        <div class="world-brand-subtle">
          <span class="wbs-nivora">NIVORA &middot;</span>
          <span class="wbs-product-name" id="worldTopProductName">CHECKRA</span>
          <span class="wbs-status-badge" id="worldTopStatusBadge">Live App</span>
        </div>
      </div>

      <nav class="world-nav-tabs" aria-label="Product In-World Navigation">
        <button type="button" class="world-nav-tab active" onclick="scrollWorldSection('overview')">Overview</button>
        <button type="button" class="world-nav-tab" onclick="scrollWorldSection('capabilities')">Capabilities</button>
        <button type="button" class="world-nav-tab" onclick="scrollWorldSection('workflow')">Workflow</button>
        <button type="button" class="world-nav-tab" onclick="scrollWorldSection('architecture')">Architecture</button>
        <button type="button" class="world-nav-tab" onclick="scrollWorldSection('vision')">Vision</button>
      </nav>

      <div class="world-top-right">
        <a href="https://checkra-xi.vercel.app/" target="_blank" rel="noopener noreferrer" class="world-launch-btn" id="worldLaunchLink">
          <span>Launch App</span>
          <span class="btn-arrow">↗</span>
        </a>
        <button type="button" class="world-close-x" onclick="returnToUniverse()" aria-label="Close World (ESC)">
          <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </button>
      </div>
    </header>

    <!-- Scrollable World Body -->
    <div class="world-scrollable-body" id="worldScrollBody">

      <!-- ==================== 1. CHECKRA WORLD ==================== -->
      <div class="world-product-view active" id="view-checkra">
        <div class="world-sec" id="sec-overview-checkra">
          <div class="world-sec-title">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
            <span>Concept Overview &middot; Writing Integrity Space</span>
          </div>
          <h2 class="world-sec-heading">
            Empowering Writing Truth &amp; Source Accuracy
          </h2>
          <p class="world-intro-lead">
            CHECKRA is an AI-powered writing integrity and source verification platform designed to help students, researchers, educators, professionals, and content creators check, verify, and improve their writing in one connected workspace.
          </p>
        </div>

        <div class="world-sec" id="sec-capabilities-checkra">
          <div class="world-sec-title">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="3" width="18" height="18" rx="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line></svg>
            <span>Key Capabilities</span>
          </div>
          <h3 class="world-sec-heading">Engineered for Writing Truth &amp; Elevation</h3>

          <div class="world-grid-4">
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></div>
              <h5>Similarity Check</h5>
              <p>Multi-level comparison analyzing exact matches, near phrasing, and semantic overlap across open web sources.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg></div>
              <h5>Source Verification</h5>
              <p>Indexes live web resources to provide verifiable context, metadata, and direct citations for detected matches.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg></div>
              <h5>Document Analysis</h5>
              <p>Unified native ingestion of PDF, DOCX, TXT, HTML, and Markdown files with preserved layout parsing.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10H12V2z"></path><path d="M12 12 2.1 10.5"></path></svg></div>
              <h5>AI Evidence Review</h5>
              <p>Assists reviewers in evaluating matches, distinguishing valid citations and idioms from true duplication.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg></div>
              <h5>Grammar &amp; Tone Intel</h5>
              <p>Contextual syntactic clarity diagnostics, passive voice alerts, and academic tone calibration.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg></div>
              <h5>Citation Assistance</h5>
              <p>Generates APA, MLA, Chicago, and IEEE citation structures directly from matched online references.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg></div>
              <h5>Evidence Reports</h5>
              <p>Exportable PDF audit trails containing annotated similarity heatmaps and verifiable timestamps.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg></div>
              <h5>Zero Data Ingestion</h5>
              <p>User manuscripts are never used to train public LLM models or stored in unencrypted public indices.</p>
            </div>
          </div>
        </div>

        <div class="world-sec" id="sec-workflow-checkra">
          <div class="world-sec-title">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
            <span>How It Works &middot; 4-Step Pipeline</span>
          </div>
          <h3 class="world-sec-heading">Seamless Document Verification Journey</h3>

          <div class="world-workflow-steps">
            <div class="workflow-step-box">
              <span class="step-index-badge">STEP 01</span>
              <h6>Document Ingestion</h6>
              <p>Upload files or paste text into the protected client sandbox with instant parsing.</p>
            </div>
            <div class="workflow-step-box">
              <span class="step-index-badge">STEP 02</span>
              <h6>Deep Semantic Scan</h6>
              <p>Multi-threaded crawler compares sentence embeddings across billions of indexed sources.</p>
            </div>
            <div class="workflow-step-box">
              <span class="step-index-badge">STEP 03</span>
              <h6>Evidence Review</h6>
              <p>Side-by-side comparison interface distinguishes quoted content from true similarity.</p>
            </div>
            <div class="workflow-step-box">
              <span class="step-index-badge">STEP 04</span>
              <h6>Refinement &amp; Report</h6>
              <p>Apply context rewrites and export an official verification report with timestamp verification.</p>
            </div>
          </div>
        </div>

        <div class="world-sec" id="sec-architecture-checkra">
          <div class="world-sec-title">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg>
            <span>System Architecture</span>
          </div>
          <h3 class="world-sec-heading">Engineered for High-Throughput Accuracy</h3>

          <div class="world-grid-2">
            <div class="arch-card">
              <h5>Hybrid Retrieval Engine</h5>
              <p>Combines exact n-gram matching with dense semantic vector embeddings to detect paraphrased and restructured sentences across languages.</p>
            </div>
            <div class="arch-card">
              <h5>Privacy-First Isolation</h5>
              <p>Client files are processed in ephemeral memory enclaves and permanently expunged upon session termination.</p>
            </div>
          </div>
        </div>

        <div class="world-sec" id="sec-vision-checkra">
          <div class="world-sec-title">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg>
            <span>Future Vision</span>
          </div>
          <h3 class="world-sec-heading">The Standard for Autonomous Content Trust</h3>
          <p style="color:var(--text-muted);line-height:1.7;max-width:860px;font-family:var(--font-body);font-size:14px;">
            CHECKRA is evolving into an omnipresent writing integrity layer &mdash; protecting academic institutions, independent journalists, and research laboratories against synthetic misinformation, unauthorized attribution loss, and automated plagiarism.
          </p>
        </div>
      </div>

      <!-- ==================== 2. HOMORA WORLD ==================== -->
      <div class="world-product-view" id="view-homora">
        <div class="world-sec" id="sec-overview-homora">
          <div class="world-sec-title">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
            <span>Concept Overview &middot; Household Financial OS</span>
          </div>
          <h2 class="world-sec-heading">Financial Harmony for Modern Shared Living</h2>
          <p class="world-intro-lead">
            HOMORA is an AI-powered financial operating system designed for roommates, couples, families, and shared households. It replaces awkward split calculations, forgotten utility bills, and manual spreadsheets with an intuitive, unified ledger that coordinates expenses fairly.
          </p>
        </div>

        <div class="world-sec" id="sec-capabilities-homora">
          <div class="world-sec-title">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="3" width="18" height="18" rx="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line></svg>
            <span>Key Capabilities</span>
          </div>
          <h3 class="world-sec-heading">Orchestrated Household Intelligence</h3>

          <div class="world-grid-4">
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg></div>
              <h5>Smart Expense Splits</h5>
              <p>Dynamic ratio calculation based on room size, utility usage, or custom income-weighted formulas.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg></div>
              <h5>Automated Bill Sync</h5>
              <p>Scans electricity, internet, and rent receipts to allocate dues and notify residents automatically.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg></div>
              <h5>Shared Groceries</h5>
              <p>Collaborative shopping baskets that automatically allocate individual versus shared household staples.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg></div>
              <h5>Member Balances</h5>
              <p>Clear, real-time debt resolution matrices minimizing transfers through simplified triangular settlement.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg></div>
              <h5>HOMORA Intel</h5>
              <p>Machine learning insights predicting month-end utility surges and recommending budget optimizations.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg></div>
              <h5>Chore &amp; Task Harmony</h5>
              <p>Ties financial fairness to shared physical duties like deep cleaning, maintenance, and supplies.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 14 14"></polyline></svg></div>
              <h5>Payment History Audit</h5>
              <p>Immutable digital receipts and payment proof protecting both tenants and landlords.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg></div>
              <h5>Granular Privacy</h5>
              <p>Allows members to keep individual personal transactions confidential while maintaining shared ledger truth.</p>
            </div>
          </div>
        </div>

        <div class="world-sec" id="sec-workflow-homora">
          <div class="world-sec-title">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
            <span>How It Works &middot; 4-Step Pipeline</span>
          </div>
          <h3 class="world-sec-heading">Effortless Home Operating Flow</h3>

          <div class="world-workflow-steps">
            <div class="workflow-step-box">
              <span class="step-index-badge">STEP 01</span>
              <h6>Create Home Space</h6>
              <p>Set up your apartment or house and invite roommates with custom split agreements.</p>
            </div>
            <div class="workflow-step-box">
              <span class="step-index-badge">STEP 02</span>
              <h6>Log Bills &amp; Purchases</h6>
              <p>Snap a photo of any receipt; HOMORA parses items, tax, and totals in seconds.</p>
            </div>
            <div class="workflow-step-box">
              <span class="step-index-badge">STEP 03</span>
              <h6>Intelligent Netting</h6>
              <p>The system calculates optimized balances so residents settle debts with minimal transactions.</p>
            </div>
            <div class="workflow-step-box">
              <span class="step-index-badge">STEP 04</span>
              <h6>Zero-Stress Harmony</h6>
              <p>Enjoy living together with full financial transparency and automated reminders.</p>
            </div>
          </div>
        </div>

        <div class="world-sec" id="sec-architecture-homora">
          <div class="world-sec-title">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg>
            <span>System Architecture</span>
          </div>
          <h3 class="world-sec-heading">Engineered for Frictionless Shared Finance</h3>

          <div class="world-grid-2">
            <div class="arch-card">
              <h5>Real-Time WebSocket Ledger</h5>
              <p>State-synchronized graph ledger propagating transaction updates to all household members instantly across iOS, Android, and Web.</p>
            </div>
            <div class="arch-card">
              <h5>OCR &amp; Categorization Pipeline</h5>
              <p>Computer vision engine extracting line-item details from multi-vendor receipts with 99.4% accuracy.</p>
            </div>
          </div>
        </div>

        <div class="world-sec" id="sec-vision-homora">
          <div class="world-sec-title">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg>
            <span>Future Vision</span>
          </div>
          <h3 class="world-sec-heading">The Standard for Modern Co-Living Operations</h3>
          <p style="color:var(--text-muted);line-height:1.7;max-width:860px;font-family:var(--font-body);font-size:14px;">
            HOMORA is evolving into a full smart home OS connecting utility smart meters, automated banking rails, and collective residential sustainability incentives.
          </p>
        </div>
      </div>

      <!-- ==================== 3. BUBORA WORLD ==================== -->
      <div class="world-product-view" id="view-bubora">
        <div class="world-sec" id="sec-overview-bubora">
          <div class="world-sec-title">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
            <span>Concept Overview &middot; Digital Home for Two</span>
          </div>
          <h2 class="world-sec-heading">A Private, Dedicated Space for Couples</h2>
          <p class="world-intro-lead">
            BUBORA is an intimate, private digital sanctuary created exclusively for two partners. Free from social media feeds, advertisements, and public surveillance, BUBORA combines private encrypted communication, shared memories, collaborative travel planning, and relationship milestones.
          </p>
        </div>

        <div class="world-sec" id="sec-capabilities-bubora">
          <div class="world-sec-title">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="3" width="18" height="18" rx="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line></svg>
            <span>Key Capabilities</span>
          </div>
          <h3 class="world-sec-heading">Designed Exclusively for Two Hearts</h3>

          <div class="world-grid-4">
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg></div>
              <h5>Encrypted Duo Chat</h5>
              <p>End-to-end encrypted messaging with voice notes, photo drops, and playful micro-reactions.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg></div>
              <h5>Timeline of Memories</h5>
              <p>Chronological gallery of your shared journey, anniversaries, trips, and cherished photographs.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg></div>
              <h5>Shared Calendar</h5>
              <p>Synchronized scheduling for date nights, anniversaries, flights, and doctor appointments.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg></div>
              <h5>Trips &amp; Adventures</h5>
              <p>Collaborative vacation planning with interactive pin maps, packing lists, and itinerary cards.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle></svg></div>
              <h5>Shared Goals</h5>
              <p>Track joint dreams like saving for a home, adopting a pet, or learning a new language together.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg></div>
              <h5>Couple Finances</h5>
              <p>Transparent joint budget for dinners, gifts, and weekend escapes without awkward debt tallying.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></div>
              <h5>Couple Games &amp; Quizzes</h5>
              <p>Fun daily connection prompts and relationship quizzes to discover new facets of each other.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg></div>
              <h5>The Private Vault</h5>
              <p>Biometrically locked storage for intimate photos, passports, medical notes, and love letters.</p>
            </div>
          </div>
        </div>

        <div class="world-sec" id="sec-workflow-bubora">
          <div class="world-sec-title">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
            <span>How It Works &middot; 4-Step Pipeline</span>
          </div>
          <h3 class="world-sec-heading">Connecting Your Sanctuary</h3>

          <div class="world-workflow-steps">
            <div class="workflow-step-box">
              <span class="step-index-badge">STEP 01</span>
              <h6>Invite Your Partner</h6>
              <p>Generate a unique encrypted pair code that links only your two devices forever.</p>
            </div>
            <div class="workflow-step-box">
              <span class="step-index-badge">STEP 02</span>
              <h6>Build Your Space</h6>
              <p>Personalize your home screen with custom nicknames, relationship dates, and themes.</p>
            </div>
            <div class="workflow-step-box">
              <span class="step-index-badge">STEP 03</span>
              <h6>Share Everyday Life</h6>
              <p>Post status widgets, send heartbeats, coordinate plans, and save photos in your timeline.</p>
            </div>
            <div class="workflow-step-box">
              <span class="step-index-badge">STEP 04</span>
              <h6>Cherish Milestones</h6>
              <p>Watch your memories compound over months and years into an irreplaceable couple keepsake.</p>
            </div>
          </div>
        </div>

        <div class="world-sec" id="sec-architecture-bubora">
          <div class="world-sec-title">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg>
            <span>System Architecture</span>
          </div>
          <h3 class="world-sec-heading">Engineered for Unbreakable Trust &amp; Privacy</h3>

          <div class="world-grid-2">
            <div class="arch-card">
              <h5>Peer-to-Peer Encryption</h5>
              <p>Messages and photos are encrypted with keys that exist solely on your partner's phone and yours. Zero server access.</p>
            </div>
            <div class="arch-card">
              <h5>Ad-Free Sanctuary</h5>
              <p>Zero tracking SDKs, zero data mining, and zero external ad networks. A pristine private home.</p>
            </div>
          </div>
        </div>

        <div class="world-sec" id="sec-vision-bubora">
          <div class="world-sec-title">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg>
            <span>Future Vision</span>
          </div>
          <h3 class="world-sec-heading">The Lifelong Memory Vault for Modern Relationships</h3>
          <p style="color:var(--text-muted);line-height:1.7;max-width:860px;font-family:var(--font-body);font-size:14px;">
            BUBORA envisions a digital sanctuary that couples cherish across decades &mdash; holding letters, vows, voice recordings, and precious moments safely preserved forever.
          </p>
        </div>
      </div>

      <!-- ==================== 4. SAYORA WORLD ==================== -->
      <div class="world-product-view" id="view-sayora">
        <div class="world-sec" id="sec-overview-sayora">
          <div class="world-sec-title">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
            <span>Concept Overview &middot; Financial Resilience Space</span>
          </div>
          <h2 class="world-sec-heading">Financial Dignity &amp; Resilience for Workers &amp; Communities</h2>
          <p class="world-intro-lead">
            SAYORA is a financial resilience platform designed for informal workers, gig economy contributors, and vulnerable urban communities. Combining automated micro-savings, community emergency funds, and dignified crisis protection, SAYORA builds safety nets where traditional banking fails.
          </p>
        </div>

        <div class="world-sec" id="sec-capabilities-sayora">
          <div class="world-sec-title">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="3" width="18" height="18" rx="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line></svg>
            <span>Key Capabilities</span>
          </div>
          <h3 class="world-sec-heading">Engineered for Community Security</h3>

          <div class="world-grid-4">
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg></div>
              <h5>Micro-Savings Protocol</h5>
              <p>Rounds up small daily wages and automatically locks tiny reserves into interest-bearing, high-safety vaults.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>
              <h5>Community Shield Pool</h5>
              <p>Peer-guaranteed safety pools offering zero-predatory-interest emergency liquidity during health crises.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg></div>
              <h5>SAYORA Digital Identity</h5>
              <p>Portable, privacy-preserving reputation credential allowing informal workers to prove reliability without credit scores.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 14 14"></polyline></svg></div>
              <h5>Crisis Assistance Alert</h5>
              <p>Instant SOS trigger routing emergency funds within minutes upon verified accidents or illness.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg></div>
              <h5>CSR Matching Rails</h5>
              <p>Channels corporate social responsibility funding directly into worker emergency pools with transparent impact audits.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M8 14s1.5 2 4 2 4-2 4-2"></path><line x1="9" y1="9" x2="9.01" y2="9"></line><line x1="15" y1="9" x2="15.01" y2="9"></line></svg></div>
              <h5>Audio-First Literacy</h5>
              <p>Vernacular voice lessons breaking down compound growth, emergency planning, and scam avoidance.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg></div>
              <h5>Weather &amp; Monsoons Cover</h5>
              <p>Parametric relief payouts triggered automatically during extreme climate events or floods that halt daily wages.</p>
            </div>
            <div class="world-cap-card">
              <div class="world-cap-icon"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg></div>
              <h5>Zero-Fee Architecture</h5>
              <p>Community pools operate with 0% predatory interest and transparent peer governance.</p>
            </div>
          </div>
        </div>

        <div class="world-sec" id="sec-workflow-sayora">
          <div class="world-sec-title">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
            <span>How It Works &middot; 4-Step Pipeline</span>
          </div>
          <h3 class="world-sec-heading">Resilience in Action</h3>

          <div class="world-workflow-steps">
            <div class="workflow-step-box">
              <span class="step-index-badge">STEP 01</span>
              <h6>Register SAYORA ID</h6>
              <p>Create a verified, low-bandwidth account using simple phone-number verification.</p>
            </div>
            <div class="workflow-step-box">
              <span class="step-index-badge">STEP 02</span>
              <h6>Daily Roundups</h6>
              <p>Small change from UPI and digital earnings is swept into a locked emergency buffer.</p>
            </div>
            <div class="workflow-step-box">
              <span class="step-index-badge">STEP 03</span>
              <h6>Community Backing</h6>
              <p>Join a local guild of trusted workers who vouch for and protect one another.</p>
            </div>
            <div class="workflow-step-box">
              <span class="step-index-badge">STEP 04</span>
              <h6>Instant Emergency Relief</h6>
              <p>Request immediate disbursal in crises with zero collateral and dignity intact.</p>
            </div>
          </div>
        </div>

        <div class="world-sec" id="sec-architecture-sayora">
          <div class="world-sec-title">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg>
            <span>System Architecture</span>
          </div>
          <h3 class="world-sec-heading">Engineered for Last-Mile Financial Inclusion</h3>

          <div class="world-grid-2">
            <div class="arch-card">
              <h5>Ultra-Lightweight PWA</h5>
              <p>Engineered to operate seamlessly on sub-$50 Android phones with 2G/3G connectivity and offline-first caching.</p>
            </div>
            <div class="arch-card">
              <h5>Parametric Smart Contracts</h5>
              <p>Transparent public ledger ensuring community funds cannot be misappropriated or seized by predatory lenders.</p>
            </div>
          </div>
        </div>

        <div class="world-sec" id="sec-vision-sayora">
          <div class="world-sec-title">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg>
            <span>Future Vision</span>
          </div>
          <h3 class="world-sec-heading">Universal Safety Net for Every Hardworking Citizen</h3>
          <p style="color:var(--text-muted);line-height:1.7;max-width:860px;font-family:var(--font-body);font-size:14px;">
            SAYORA aims to scale into a self-sustaining societal safety infrastructure &mdash; demonstrating that when technology empowers community solidarity, millions of informal families break the cycle of predatory debt forever.
          </p>
        </div>
      </div>

    </div>
  </div>

  <!-- =========================================================
       CANVAS GALAXY SIMULATION & IMMERSIVE INTERACTION ENGINE
       ========================================================= -->
  <script>
    /* -------------------------------------------------------------
       1. 3D GALAXY / STARFIELD SIMULATION
       ------------------------------------------------------------- */
    (function initUniverseStarfield() {{
      const canvas = document.getElementById('universeCanvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');

      let width = canvas.width = window.innerWidth;
      let height = canvas.height = window.innerHeight;

      const isMobile = width < 768;
      const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

      const numStars = prefersReducedMotion ? 120 : (isMobile ? 220 : 480);
      const stars = [];

      let scrollSpeed = 0;
      let lastScrollY = window.scrollY;

      let mouseX = 0;
      let mouseY = 0;
      let targetMouseX = 0;
      let targetMouseY = 0;

      const starColors = [
        '#ffffff', '#ffffff', '#ffffff',
        '#a5b4fc', '#818cf8', '#67e8f9',
        '#f472b6', '#6ee7b7'
      ];

      function initStars() {{
        stars.length = 0;
        for (let i = 0; i < numStars; i++) {{
          stars.push({{
            x: (Math.random() - 0.5) * 2200,
            y: (Math.random() - 0.5) * 1600,
            z: Math.random() * 2000 + 1,
            size: Math.random() * 1.6 + 0.5,
            color: starColors[Math.floor(Math.random() * starColors.length)],
            alpha: Math.random() * 0.65 + 0.35
          }});
        }}
      }}

      initStars();

      window.addEventListener('resize', () => {{
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
        initStars();
      }});

      window.addEventListener('mousemove', (e) => {{
        targetMouseX = (e.clientX - width / 2) * 0.12;
        targetMouseY = (e.clientY - height / 2) * 0.12;
      }});

      window.addEventListener('scroll', () => {{
        const currentScrollY = window.scrollY;
        const delta = currentScrollY - lastScrollY;
        lastScrollY = currentScrollY;

        scrollSpeed = Math.min(Math.abs(delta) * 0.75, 40);
        updateHUDTelemetry(currentScrollY);
      }}, {{ passive: true }});

      function render() {{
        ctx.fillStyle = '#010206';
        ctx.fillRect(0, 0, width, height);

        mouseX += (targetMouseX - mouseX) * 0.05;
        mouseY += (targetMouseY - mouseY) * 0.05;

        scrollSpeed *= 0.92;
        if (scrollSpeed < 0.05) scrollSpeed = 0;

        const fov = 340;
        const cx = width / 2 + mouseX;
        const cy = height / 2 + mouseY;

        const baseSpeed = prefersReducedMotion ? 0.2 : 0.7;
        const currentSpeed = baseSpeed + scrollSpeed;

        for (let i = 0; i < stars.length; i++) {{
          const s = stars[i];

          s.z -= currentSpeed;
          if (s.z <= 2) {{
            s.z = 2000;
            s.x = (Math.random() - 0.5) * 2200;
            s.y = (Math.random() - 0.5) * 1600;
          }}

          const k = fov / s.z;
          const px = s.x * k + cx;
          const py = s.y * k + cy;

          if (px < -50 || px > width + 50 || py < -50 || py > height + 50) {{
            continue;
          }}

          const rad = Math.max(0.4, (1 - s.z / 2000) * s.size * 1.8);

          if (scrollSpeed > 2 && !prefersReducedMotion) {{
            const prevZ = s.z + currentSpeed * 2.2;
            const prevK = fov / prevZ;
            const prevPx = s.x * prevK + cx;
            const prevPy = s.y * prevK + cy;

            ctx.beginPath();
            ctx.moveTo(prevPx, prevPy);
            ctx.lineTo(px, py);
            ctx.strokeStyle = s.color;
            ctx.lineWidth = rad * 0.75;
            ctx.globalAlpha = Math.min(1, s.alpha * (1 - s.z / 2000) * 1.3);
            ctx.stroke();
          }} else {{
            ctx.beginPath();
            ctx.arc(px, py, rad, 0, Math.PI * 2);
            ctx.fillStyle = s.color;
            ctx.globalAlpha = Math.min(1, s.alpha * (1 - s.z / 2000));
            ctx.fill();
          }}
        }}

        ctx.globalAlpha = 1;
        requestAnimationFrame(render);
      }}

      render();
    }})();

    /* -------------------------------------------------------------
       2. TELEMETRY & HUD UPDATE ON SCROLL
       ------------------------------------------------------------- */
    function updateHUDTelemetry(scrollY) {{
      const text = document.getElementById('telemetryStatusText');
      if (!text) return;

      const destSec = document.getElementById('destinations');
      const ecoSec = document.getElementById('ecosystem');
      const folSec = document.getElementById('folivio');
      const fndSec = document.getElementById('founder');
      const conSec = document.getElementById('contact');

      if (conSec && scrollY >= conSec.offsetTop - 300) {{
        text.innerText = 'SECTOR: TRANSMIT';
      }} else if (fndSec && scrollY >= fndSec.offsetTop - 300) {{
        text.innerText = 'SECTOR: ARCHITECT';
      }} else if (folSec && scrollY >= folSec.offsetTop - 300) {{
        text.innerText = 'SECTOR: FOLIVIO';
      }} else if (ecoSec && scrollY >= ecoSec.offsetTop - 300) {{
        text.innerText = 'SECTOR: ECOSYSTEM';
      }} else if (destSec && scrollY >= destSec.offsetTop - 300) {{
        text.innerText = 'SECTOR: DESTINATIONS';
      }} else {{
        text.innerText = 'ORBIT: CORE STABLE';
      }}
    }}

    function smoothWarpTo(sectionId) {{
      const el = document.getElementById(sectionId);
      if (el) {{
        el.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
      }}
    }}

    function initiateUniverseWarp() {{
      smoothWarpTo('destinations');
    }}

    /* -------------------------------------------------------------
       3. PRODUCT ZOOM TRANSITION & WORLD PORTFOLIO INTERFACE
       ------------------------------------------------------------- */
    const worldMeta = {{
      'checkra': {{
        name: 'CHECKRA',
        badge: 'Live Product',
        url: 'https://checkra-xi.vercel.app/'
      }},
      'homora': {{
        name: 'HOMORA',
        badge: 'Active Prototype',
        url: 'https://homora-ai.vercel.app/'
      }},
      'bubora': {{
        name: 'BUBORA',
        badge: 'Live Product',
        url: 'https://bubora.netlify.app/'
      }},
      'sayora': {{
        name: 'SAYORA',
        badge: 'Concept &middot; In Dev',
        url: ''
      }}
    }};

    function zoomIntoWorld(productId, triggerBtn) {{
      const overlay = document.getElementById('universeWorldInterface');
      if (!overlay) return;

      const info = worldMeta[productId] || {{ name: productId.toUpperCase(), badge: 'Product', url: '' }};
      document.getElementById('worldTopProductName').innerText = info.name;
      document.getElementById('worldTopStatusBadge').innerHTML = info.badge;

      const launchBtn = document.getElementById('worldLaunchLink');
      if (info.url) {{
        launchBtn.style.display = 'inline-flex';
        launchBtn.href = info.url;
      }} else {{
        launchBtn.style.display = 'none';
      }}

      document.querySelectorAll('.world-product-view').forEach(view => {{
        view.classList.remove('active');
      }});
      const targetView = document.getElementById('view-' + productId);
      if (targetView) {{
        targetView.classList.add('active');
      }}

      const scrollBody = document.getElementById('worldScrollBody');
      if (scrollBody) scrollBody.scrollTop = 0;

      document.body.classList.add('world-open');
      overlay.classList.add('active');
      overlay.setAttribute('aria-hidden', 'false');
    }}

    function returnToUniverse() {{
      const overlay = document.getElementById('universeWorldInterface');
      if (!overlay) return;

      overlay.classList.remove('active');
      overlay.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('world-open');
    }}

    function scrollWorldSection(secKey) {{
      const activeView = document.querySelector('.world-product-view.active');
      if (!activeView) return;

      const prodId = activeView.id.replace('view-', '');
      const targetSec = document.getElementById('sec-' + secKey + '-' + prodId);
      if (targetSec) {{
        targetSec.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
      }}

      document.querySelectorAll('.world-nav-tab').forEach(tab => tab.classList.remove('active'));
      const clickedTab = event && event.target;
      if (clickedTab) clickedTab.classList.add('active');
    }}

    window.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') {{
        returnToUniverse();
      }}
    }});

    // Click backdrop to close
    document.getElementById('universeWorldInterface')?.addEventListener('click', (e) => {{
      if (e.target.id === 'universeWorldInterface') {{
        returnToUniverse();
      }}
    }});

    /* -------------------------------------------------------------
       4. TRANSMISSION CONSOLE DISPATCH HANDLER
       ------------------------------------------------------------- */
    function handleTransmission(e) {{
      e.preventDefault();
      const btn = document.getElementById('transmitBtn');
      const toast = document.getElementById('transmissionToast');
      if (!btn) return;

      const origText = btn.innerHTML;
      btn.innerHTML = '<span>DISPATCHING SIGNAL...</span>';
      btn.disabled = true;

      setTimeout(() => {{
        btn.innerHTML = '<span>TRANSMISSION CONFIRMED ✓</span>';
        if (toast) {{
          toast.style.display = 'block';
          toast.innerText = 'Signal received. Nivas and the NIVORA core team will respond promptly.';
        }}
        e.target.reset();

        setTimeout(() => {{
          btn.innerHTML = origText;
          btn.disabled = false;
          setTimeout(() => {{
            if (toast) toast.style.display = 'none';
          }}, 5000);
        }}, 3000);
      }}, 850);
    }}
  </script>
</body>
</html>
"""

    desktop_path = "/Users/bennabathulanivas/Desktop/my projects/NIVORA/index.html"
    downloads_path = "/Users/bennabathulanivas/Downloads/NIVORA/index.html"

    with open(desktop_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {len(html)} bytes to {desktop_path}")

    with open(downloads_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {len(html)} bytes to {downloads_path}")

if __name__ == '__main__':
    build()
