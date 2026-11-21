# builder/assemble_cinematic_globe_hero.py
# NIVORA — PREMIUM CINEMATIC 3D GLOBE HERO MASTER BUILDER
import os
import sys

builder_dir = os.path.dirname(os.path.abspath(__file__))
if builder_dir not in sys.path:
    sys.path.append(builder_dir)

def generate_globe_hero_html():
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NIVORA — Turning Ideas Into Intelligent Products</title>
  <meta name="description" content="NIVORA is the technology and innovation universe built by Nivas Bennabatthula — home to Checkra, Homora, Bubora, and Sayora.">
  <link rel="icon" type="image/png" href="assets/images/nivora-logo.png">

  <!-- GOOGLE FONTS: Sora, Space Grotesk, Inter, Instrument Serif, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Space+Grotesk:wght@400;500;600;700;800&family=Sora:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <!-- THREE.JS, GSAP & LENIS CDNS -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://unpkg.com/lenis@1.1.18/dist/lenis.min.js"></script>

  <style>
    /* =========================================================
       NIVORA CINEMATIC 3D UNIVERSE DESIGN SYSTEM
       ========================================================= */
    :root {
      --bg-space-base: #010206;
      --bg-space-deep: #000103;
      
      --text-main: #f8faff;
      --text-secondary: #b8c0d9;
      --text-muted: #707a96;
      --text-dim: #454d63;

      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-hover: rgba(255, 255, 255, 0.25);
      
      --glass-surface: rgba(10, 15, 34, 0.65);
      --glass-surface-dense: rgba(6, 8, 20, 0.94);
      --glass-surface-elevated: rgba(14, 20, 44, 0.78);

      /* NIVORA Brand Palette: Violet -> Purple -> Blue -> Cyan -> Magenta */
      --color-violet: #8b5cf6;
      --color-purple: #a855f7;
      --color-blue: #4f7cff;
      --color-cyan: #22d3ee;
      --color-magenta: #ec4899;
      --color-emerald: #10b981;

      /* Product Identity Colors & Glows */
      --color-checkra: #8b5cf6;
      --glow-checkra: rgba(139, 92, 246, 0.45);
      --color-homora: #06b6d4;
      --glow-homora: rgba(6, 182, 212, 0.45);
      --color-bubora: #ec4899;
      --glow-bubora: rgba(236, 72, 153, 0.45);
      --color-sayora: #10b981;
      --glow-sayora: rgba(16, 185, 129, 0.45);

      /* Typographic System */
      --font-display: 'Sora', 'Space Grotesk', -apple-system, sans-serif;
      --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-editorial: 'Instrument Serif', Georgia, serif;
      --font-mono: 'JetBrains Mono', monospace;
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html.lenis, html.lenis body {
      height: auto;
    }

    .lenis.lenis-smooth {
      scroll-behavior: auto !important;
    }

    .lenis.lenis-smooth [data-lenis-prevent] {
      overscroll-behavior: contain;
    }

    .lenis.lenis-stopped {
      overflow: hidden;
    }

    html {
      background: #010206;
      color: var(--text-main);
      font-family: var(--font-body);
      font-size: 16px;
      line-height: 1.6;
      overflow-x: hidden;
    }

    body {
      background: #010206;
      min-height: 100vh;
      overflow-x: hidden;
      position: relative;
      cursor: default;
    }

    body.world-open {
      overflow: hidden;
    }

    a {
      color: inherit;
      text-decoration: none;
      transition: all 0.25s ease;
    }

    img {
      max-width: 100%;
      height: auto;
      display: block;
    }

    button {
      font-family: inherit;
      border: none;
      outline: none;
      cursor: pointer;
      background: none;
    }

    /* =========================================================
       CINEMATIC MULTI-LAYER COSMIC ENVIRONMENT
       ========================================================= */
    #webglCanvas {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 0;
    }

    /* Layer 2: Rich Nebula Clouds Background */
    .cosmic-nebulae-container {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 1;
      overflow: hidden;
      opacity: 0.85;
      transition: transform 0.2s ease-out;
    }

    /* Deep Navy Atmospheric Wash */
    .nebula-wash {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: radial-gradient(ellipse at 50% 10%, #0c1236 0%, #06091d 45%, #010208 85%, #000103 100%);
    }

    /* Vibrant Purple & Electric Blue Nebula Behind Globe */
    .nebula-globe-aura {
      position: absolute;
      top: 15%;
      right: 5%;
      width: 750px;
      height: 750px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(139, 92, 246, 0.45) 0%, rgba(79, 124, 255, 0.3) 35%, rgba(34, 211, 238, 0.15) 55%, transparent 75%);
      filter: blur(120px);
      animation: nebulaPulse 12s ease-in-out infinite alternate;
    }

    /* Subtle Magenta / Violet Cloud on Left */
    .nebula-left-cloud {
      position: absolute;
      top: 30%;
      left: -10%;
      width: 600px;
      height: 600px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(236, 72, 153, 0.2) 0%, rgba(139, 92, 246, 0.18) 40%, transparent 70%);
      filter: blur(140px);
      animation: nebulaPulse 14s ease-in-out infinite alternate-reverse;
    }

    @keyframes nebulaPulse {
      0% { transform: scale(0.92) translate(0, 0); opacity: 0.8; }
      100% { transform: scale(1.1) translate(20px, -15px); opacity: 1; }
    }

    /* Fine Celestial Grid Overlay */
    .cosmic-grid-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 1;
      background-image: 
        linear-gradient(to right, rgba(255, 255, 255, 0.012) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.012) 1px, transparent 1px);
      background-size: 100px 100px;
    }

    /* =========================================================
       PLANETARY FOREGROUND (BOTTOM EDGES FOR CINEMATIC SCALE)
       ========================================================= */
    .foreground-planet-left {
      position: absolute;
      bottom: -320px;
      left: -200px;
      width: 580px;
      height: 580px;
      border-radius: 50%;
      background: radial-gradient(circle at 75% 25%, #080f2d 0%, #030614 60%, #010208 95%);
      box-shadow: 
        inset -10px -10px 40px rgba(0, 0, 0, 0.95),
        inset 15px 15px 50px rgba(34, 211, 238, 0.28),
        0 0 80px rgba(79, 124, 255, 0.25);
      border-top: 1.5px solid rgba(34, 211, 238, 0.35);
      pointer-events: none;
      z-index: 2;
      opacity: 0.75;
      transform: rotate(-15deg);
    }

    .foreground-planet-right {
      position: absolute;
      bottom: -360px;
      right: -220px;
      width: 640px;
      height: 640px;
      border-radius: 50%;
      background: radial-gradient(circle at 25% 25%, #120b29 0%, #050312 60%, #010208 95%);
      box-shadow: 
        inset 10px 10px 40px rgba(0, 0, 0, 0.95),
        inset -15px -15px 50px rgba(236, 72, 153, 0.25),
        0 0 90px rgba(139, 92, 246, 0.28);
      border-top: 1.5px solid rgba(236, 72, 153, 0.35);
      pointer-events: none;
      z-index: 2;
      opacity: 0.7;
      transform: rotate(20deg);
    }

    /* Container */
    .container {
      width: 100%;
      max-width: 1320px;
      margin: 0 auto;
      padding: 0 2.5rem;
      position: relative;
      z-index: 3;
    }

    /* =========================================================
       CUSTOM DESKTOP 3D CURSOR
       ========================================================= */
    .custom-cursor-ring {
      position: fixed;
      top: 0;
      left: 0;
      width: 32px;
      height: 32px;
      border: 1.5px solid rgba(139, 92, 246, 0.65);
      border-radius: 50%;
      pointer-events: none;
      transform: translate(-50%, -50%);
      transition: width 0.3s cubic-bezier(0.16, 1, 0.3, 1),
                  height 0.3s cubic-bezier(0.16, 1, 0.3, 1),
                  border-color 0.3s ease,
                  background-color 0.3s ease;
      z-index: 99999;
      box-shadow: 0 0 16px rgba(139, 92, 246, 0.25);
    }

    .custom-cursor-dot {
      position: fixed;
      top: 0;
      left: 0;
      width: 5px;
      height: 5px;
      background: #22d3ee;
      border-radius: 50%;
      pointer-events: none;
      transform: translate(-50%, -50%);
      z-index: 100000;
      box-shadow: 0 0 8px #22d3ee;
    }

    .custom-cursor-ring.cursor-hover {
      width: 56px;
      height: 56px;
      border-color: rgba(34, 211, 238, 0.9);
      background: rgba(34, 211, 238, 0.08);
      box-shadow: 0 0 28px rgba(34, 211, 238, 0.4);
    }

    @media (hover: none) or (pointer: coarse) {
      .custom-cursor-ring, .custom-cursor-dot {
        display: none !important;
      }
    }

    /* =========================================================
       NAVIGATION BAR (FLOATING LUXURY CONTROL CAPSULE)
       ========================================================= */
    .site-nav {
      position: fixed;
      top: 1.5rem;
      left: 50%;
      transform: translateX(-50%);
      width: calc(100% - 4rem);
      max-width: 1260px;
      height: 66px;
      background: rgba(6, 9, 24, 0.7);
      backdrop-filter: blur(28px) saturate(190%);
      -webkit-backdrop-filter: blur(28px) saturate(190%);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 9999px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 1.65rem;
      z-index: 1000;
      box-shadow: 
        0 20px 50px -15px rgba(0, 0, 0, 0.8),
        0 0 35px rgba(139, 92, 246, 0.15),
        inset 0 1px 1px rgba(255, 255, 255, 0.2);
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .site-nav.scrolled {
      background: rgba(4, 6, 18, 0.88);
      border-color: rgba(255, 255, 255, 0.18);
      box-shadow: 
        0 25px 60px -12px rgba(0, 0, 0, 0.95),
        0 0 45px rgba(139, 92, 246, 0.25);
    }

    .nav-brand {
      display: flex;
      align-items: center;
      gap: 0.9rem;
      text-decoration: none;
    }

    .nav-brand-logo {
      width: 34px;
      height: 34px;
      object-fit: contain;
      filter: drop-shadow(0 0 14px rgba(99, 102, 241, 0.7));
    }

    .nav-brand-text {
      display: flex;
      flex-direction: column;
    }

    .nav-brand-title {
      font-family: var(--font-display);
      font-size: 1.1rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: #fff;
    }

    .nav-brand-tag {
      font-family: var(--font-mono);
      font-size: 0.62rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--color-cyan);
    }

    .nav-links {
      display: flex;
      align-items: center;
      gap: 1.6rem;
    }

    .nav-item {
      font-size: 0.875rem;
      font-weight: 500;
      color: var(--text-secondary);
      position: relative;
      padding: 0.4rem 0.85rem;
      border-radius: 9999px;
      transition: all 0.25s ease;
    }

    .nav-item:hover {
      color: #ffffff;
    }

    .nav-item.active {
      color: #ffffff;
      background: rgba(139, 92, 246, 0.2);
      border: 1px solid rgba(139, 92, 246, 0.4);
      box-shadow: 0 0 16px rgba(139, 92, 246, 0.3);
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 1.25rem;
    }

    .nav-telemetry {
      font-family: var(--font-mono);
      font-size: 0.72rem;
      letter-spacing: 0.14em;
      color: var(--color-cyan);
      display: flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.35rem 0.85rem;
      background: rgba(34, 211, 238, 0.08);
      border: 1px solid rgba(34, 211, 238, 0.22);
      border-radius: 9999px;
    }

    .pulse-dot {
      width: 6px;
      height: 6px;
      background: #10b981;
      border-radius: 50%;
      box-shadow: 0 0 10px #10b981;
      animation: pulseDotAnim 2s infinite;
    }

    @keyframes pulseDotAnim {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(0.85); }
    }

    .btn-nav-explore {
      font-family: var(--font-display);
      font-size: 0.825rem;
      font-weight: 700;
      padding: 0.6rem 1.35rem;
      border-radius: 9999px;
      background: linear-gradient(135deg, #8b5cf6 0%, #4f7cff 50%, #22d3ee 100%);
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 0.45rem;
      border: 1px solid rgba(255, 255, 255, 0.25);
      box-shadow: 
        0 8px 25px -4px rgba(139, 92, 246, 0.6),
        0 0 16px rgba(34, 211, 238, 0.35);
      transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .btn-nav-explore:hover {
      transform: translateY(-1px) scale(1.02);
      box-shadow: 
        0 12px 30px -4px rgba(139, 92, 246, 0.85),
        0 0 25px rgba(34, 211, 238, 0.55);
      border-color: rgba(255, 255, 255, 0.5);
    }

    /* =========================================================
       HERO SECTION — 3D DIGITAL UNIVERSE
       ========================================================= */
    .hero {
      min-height: 100vh;
      display: flex;
      align-items: center;
      padding-top: 8rem;
      padding-bottom: 6rem;
      position: relative;
      z-index: 3;
      overflow: visible;
    }

    .hero-grid {
      display: grid;
      grid-template-columns: 1.05fr 0.95fr;
      align-items: center;
      gap: 3rem;
      position: relative;
    }

    .hero-left {
      position: relative;
      z-index: 4;
    }

    /* Badge: Glass pill with violet border & cyan dot */
    .hero-badge-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
      font-family: var(--font-mono);
      font-size: 0.74rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--color-cyan);
      padding: 0.45rem 1.1rem;
      background: rgba(139, 92, 246, 0.1);
      border: 1px solid rgba(139, 92, 246, 0.35);
      border-radius: 9999px;
      margin-bottom: 1.85rem;
      box-shadow: 0 0 20px rgba(139, 92, 246, 0.2);
    }

    .badge-pulse-cyan {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--color-cyan);
      box-shadow: 0 0 10px var(--color-cyan);
      display: inline-block;
    }

    /* Main Headline */
    .hero-title {
      font-family: var(--font-display);
      font-size: clamp(3.6rem, 6.5vw, 6rem);
      font-weight: 800;
      line-height: 1.04;
      letter-spacing: -0.045em;
      margin-bottom: 1.35rem;
    }

    .hero-sub-lead {
      color: #ffffff;
      display: block;
      font-weight: 700;
      letter-spacing: -0.03em;
    }

    /* Animated Brand Gradient: Violet -> Purple -> Blue -> Cyan */
    .grad-nivora {
      background: linear-gradient(135deg, #8b5cf6 0%, #a855f7 30%, #4f7cff 65%, #22d3ee 100%);
      background-size: 300% 300%;
      animation: brandGradFlow 8s ease-in-out infinite;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      display: inline-block;
      filter: drop-shadow(0 0 35px rgba(139, 92, 246, 0.4));
    }

    @keyframes brandGradFlow {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }

    /* Tagline with Editorial Luxury Accent */
    .hero-tagline-wrap {
      font-family: var(--font-body);
      font-size: clamp(1.25rem, 2.1vw, 1.7rem);
      font-weight: 500;
      color: var(--text-secondary);
      margin-bottom: 1.65rem;
      line-height: 1.45;
    }

    .editorial-accent {
      font-family: var(--font-editorial);
      font-style: italic;
      font-weight: 400;
      font-size: 1.2em;
      color: #ffffff;
      letter-spacing: 0.01em;
      position: relative;
      display: inline-block;
    }

    /* Luminous Magenta/Purple Underline beneath Ideas and Products */
    .editorial-accent::after {
      content: '';
      position: absolute;
      bottom: 2px;
      left: 0;
      right: 0;
      height: 2px;
      background: linear-gradient(90deg, #ec4899 0%, #a855f7 100%);
      box-shadow: 0 0 12px rgba(236, 72, 153, 0.7);
      border-radius: 9999px;
    }

    .hero-copy {
      font-size: 1.12rem;
      line-height: 1.7;
      color: var(--text-secondary);
      max-width: 560px;
      margin-bottom: 2.75rem;
    }

    .hero-copy strong {
      color: #ffffff;
      font-weight: 600;
    }

    /* Hero CTA Actions */
    .hero-actions {
      display: flex;
      align-items: center;
      gap: 1.35rem;
      margin-bottom: 3.5rem;
      flex-wrap: wrap;
    }

    .btn-enter-universe {
      font-family: var(--font-display);
      font-size: 1rem;
      font-weight: 700;
      padding: 0.95rem 2.2rem;
      border-radius: 9999px;
      background: linear-gradient(135deg, #8b5cf6 0%, #a855f7 40%, #22d3ee 100%);
      background-size: 200% 200%;
      animation: btnGradShift 6s ease-in-out infinite alternate;
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.35);
      box-shadow: 
        0 14px 35px -6px rgba(139, 92, 246, 0.65),
        0 0 28px rgba(34, 211, 238, 0.35),
        inset 0 1px 2px rgba(255, 255, 255, 0.6);
      display: inline-flex;
      align-items: center;
      gap: 0.65rem;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @keyframes btnGradShift {
      0% { background-position: 0% 50%; }
      100% { background-position: 100% 50%; }
    }

    .btn-enter-universe:hover {
      transform: translateY(-2px) scale(1.02);
      box-shadow: 
        0 18px 45px -6px rgba(139, 92, 246, 0.85),
        0 0 40px rgba(34, 211, 238, 0.6);
      border-color: rgba(255, 255, 255, 0.6);
    }

    .btn-explore-products {
      font-family: var(--font-body);
      font-size: 0.95rem;
      font-weight: 600;
      padding: 0.9rem 1.85rem;
      border-radius: 9999px;
      background: rgba(14, 20, 48, 0.6);
      color: var(--text-main);
      border: 1px solid rgba(139, 92, 246, 0.35);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      display: inline-flex;
      align-items: center;
      gap: 0.75rem;
      transition: all 0.28s ease;
    }

    .btn-explore-products:hover {
      background: rgba(20, 30, 70, 0.8);
      border-color: rgba(34, 211, 238, 0.6);
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5), 0 0 20px rgba(34, 211, 238, 0.3);
      transform: translateY(-2px);
    }

    .play-icon-circle {
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: rgba(139, 92, 246, 0.25);
      border: 1px solid rgba(139, 92, 246, 0.5);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 0.65rem;
      color: var(--color-cyan);
    }

    /* Hero Metrics with Elegant Icons */
    .hero-metrics {
      display: flex;
      align-items: center;
      gap: 3.5rem;
      padding-top: 2.25rem;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
    }

    .metric-card {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .metric-icon-wrap {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: rgba(14, 20, 48, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.1);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--color-cyan);
      box-shadow: 0 6px 18px rgba(0, 0, 0, 0.6);
    }

    .metric-icon-wrap.m-purple {
      color: var(--color-purple);
      border-color: rgba(168, 85, 247, 0.3);
      background: rgba(168, 85, 247, 0.08);
    }
    .metric-icon-wrap.m-cyan {
      color: var(--color-cyan);
      border-color: rgba(34, 211, 238, 0.3);
      background: rgba(34, 211, 238, 0.08);
    }
    .metric-icon-wrap.m-magenta {
      color: var(--color-magenta);
      border-color: rgba(236, 72, 153, 0.3);
      background: rgba(236, 72, 153, 0.08);
    }

    .metric-info strong {
      font-family: var(--font-display);
      font-size: 2.2rem;
      font-weight: 800;
      line-height: 1;
      color: #ffffff;
      display: block;
    }

    .metric-info span {
      font-size: 0.825rem;
      color: var(--text-muted);
      letter-spacing: 0.02em;
    }

    /* =========================================================
       HERO RIGHT: 3D DIGITAL PLANET / NIVORA GLOBE STAGE
       ========================================================= */
    .hero-art-stage {
      position: relative;
      width: 100%;
      height: 640px;
      display: flex;
      align-items: center;
      justify-content: center;
      perspective: 1400px;
      z-index: 4;
    }

    /* Interactive 3D Parallax Container */
    .globe-pivot-container {
      position: relative;
      width: 480px;
      height: 480px;
      display: flex;
      align-items: center;
      justify-content: center;
      transform-style: preserve-3d;
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* Galaxy Energy Platform Beneath Globe */
    .galaxy-platform-wrap {
      position: absolute;
      bottom: -60px;
      left: 50%;
      transform: translateX(-50%) rotateX(75deg);
      width: 480px;
      height: 480px;
      border-radius: 50%;
      pointer-events: none;
      z-index: 1;
    }

    .galaxy-platform-vortex {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      background: conic-gradient(from 0deg, rgba(139, 92, 246, 0.7), rgba(34, 211, 238, 0.6), rgba(236, 72, 153, 0.6), rgba(79, 124, 255, 0.7), rgba(139, 92, 246, 0.7));
      filter: blur(12px);
      box-shadow: 
        0 0 60px rgba(34, 211, 238, 0.5),
        0 0 100px rgba(139, 92, 246, 0.5),
        inset 0 0 40px rgba(255, 255, 255, 0.8);
      animation: spinVortex 20s linear infinite;
      opacity: 0.85;
    }

    @keyframes spinVortex {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }

    /* Vertical Light Pillar Connecting Galaxy Platform to Globe */
    .galaxy-energy-beam {
      position: absolute;
      bottom: 60px;
      left: 50%;
      transform: translateX(-50%);
      width: 140px;
      height: 180px;
      background: linear-gradient(to top, rgba(34, 211, 238, 0.45) 0%, rgba(139, 92, 246, 0.25) 50%, transparent 100%);
      filter: blur(20px);
      pointer-events: none;
      z-index: 2;
      animation: beamPulse 4s ease-in-out infinite alternate;
    }

    @keyframes beamPulse {
      0% { opacity: 0.6; transform: translateX(-50%) scaleX(0.85); }
      100% { opacity: 1; transform: translateX(-50%) scaleX(1.15); }
    }

    /* Central 3D Globe Body */
    .nivora-globe-core {
      position: relative;
      width: 380px;
      height: 380px;
      border-radius: 50%;
      background: radial-gradient(circle at 35% 30%, #151b42 0%, #070c26 55%, #020412 100%);
      box-shadow: 
        inset 0 0 60px rgba(34, 211, 238, 0.45),
        inset -20px -20px 80px rgba(0, 0, 0, 0.95),
        inset 15px 15px 50px rgba(255, 255, 255, 0.35),
        0 0 70px rgba(34, 211, 238, 0.45),
        0 0 130px rgba(139, 92, 246, 0.4),
        0 0 190px rgba(236, 72, 153, 0.25);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 5;
      cursor: pointer;
      overflow: hidden;
      animation: globeFloat 6s ease-in-out infinite alternate;
    }

    @keyframes globeFloat {
      0% { transform: translateY(0px) rotate(0deg); }
      100% { transform: translateY(-12px) rotate(1deg); }
    }

    /* Digital Latitude / Longitude Mesh on Globe Surface */
    .globe-digital-mesh {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      border-radius: 50%;
      background-image: 
        radial-gradient(circle at 50% 50%, transparent 60%, rgba(34, 211, 238, 0.25) 100%),
        repeating-linear-gradient(0deg, transparent, transparent 18px, rgba(34, 211, 238, 0.15) 19px, transparent 20px),
        repeating-linear-gradient(90deg, transparent, transparent 18px, rgba(139, 92, 246, 0.15) 19px, transparent 20px);
      background-size: 100% 100%, 100% 100%, 100% 100%;
      opacity: 0.8;
      animation: rotateGlobeMesh 40s linear infinite;
      pointer-events: none;
    }

    @keyframes rotateGlobeMesh {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }

    /* Glowing Digital Data Points on Globe */
    .globe-data-points {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      border-radius: 50%;
      background: radial-gradient(circle at 40% 40%, rgba(255,255,255,0.9) 1px, transparent 2px),
                  radial-gradient(circle at 65% 25%, rgba(34,211,238,0.9) 1.5px, transparent 3px),
                  radial-gradient(circle at 25% 65%, rgba(139,92,246,0.9) 1.5px, transparent 3px),
                  radial-gradient(circle at 75% 70%, rgba(236,72,153,0.9) 1.5px, transparent 3px);
      background-size: 70px 70px;
      opacity: 0.65;
      pointer-events: none;
    }

    /* Official Floating NIVORA Logo inside Core */
    .globe-center-logo {
      width: 130px;
      height: 130px;
      object-fit: contain;
      filter: 
        drop-shadow(0 0 25px rgba(139, 92, 246, 0.85))
        drop-shadow(0 0 45px rgba(34, 211, 238, 0.65));
      position: relative;
      z-index: 10;
      animation: logoBreathing 4s ease-in-out infinite alternate;
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @keyframes logoBreathing {
      0% { transform: scale(0.96) translateY(0); filter: drop-shadow(0 0 20px rgba(139, 92, 246, 0.7)); }
      100% { transform: scale(1.04) translateY(-4px); filter: drop-shadow(0 0 35px rgba(34, 211, 238, 0.9)); }
    }

    .nivora-globe-core:hover .globe-center-logo {
      transform: scale(1.12);
    }

    /* Thin 3D Orbital Rings (4 Tilted Rings) */
    .globe-orbital-ring {
      position: absolute;
      top: 50%;
      left: 50%;
      border-radius: 50%;
      pointer-events: none;
      transform-style: preserve-3d;
    }

    /* Ring 1: Cyan (Passes front-left to back-right) */
    .ring-1 {
      width: 470px;
      height: 470px;
      margin-top: -235px;
      margin-left: -235px;
      border: 1.5px solid rgba(34, 211, 238, 0.5);
      box-shadow: 0 0 16px rgba(34, 211, 238, 0.4);
      transform: rotateX(68deg) rotateY(15deg);
      animation: spinRing1 35s linear infinite;
      z-index: 6;
    }

    /* Ring 2: Electric Blue */
    .ring-2 {
      width: 530px;
      height: 530px;
      margin-top: -265px;
      margin-left: -265px;
      border: 1.5px dashed rgba(79, 124, 255, 0.45);
      box-shadow: 0 0 20px rgba(79, 124, 255, 0.35);
      transform: rotateX(55deg) rotateY(-25deg);
      animation: spinRing2 45s linear infinite reverse;
      z-index: 4;
    }

    /* Ring 3: Violet */
    .ring-3 {
      width: 590px;
      height: 590px;
      margin-top: -295px;
      margin-left: -295px;
      border: 1.5px solid rgba(139, 92, 246, 0.4);
      box-shadow: 0 0 22px rgba(139, 92, 246, 0.3);
      transform: rotateX(75deg) rotateY(42deg);
      animation: spinRing3 55s linear infinite;
      z-index: 6;
    }

    /* Ring 4: Magenta */
    .ring-4 {
      width: 650px;
      height: 650px;
      margin-top: -325px;
      margin-left: -325px;
      border: 1.5px dashed rgba(236, 72, 153, 0.35);
      box-shadow: 0 0 25px rgba(236, 72, 153, 0.25);
      transform: rotateX(62deg) rotateY(-40deg);
      animation: spinRing4 65s linear infinite reverse;
      z-index: 4;
    }

    @keyframes spinRing1 { from { transform: rotateX(68deg) rotateY(15deg) rotateZ(0deg); } to { transform: rotateX(68deg) rotateY(15deg) rotateZ(360deg); } }
    @keyframes spinRing2 { from { transform: rotateX(55deg) rotateY(-25deg) rotateZ(0deg); } to { transform: rotateX(55deg) rotateY(-25deg) rotateZ(360deg); } }
    @keyframes spinRing3 { from { transform: rotateX(75deg) rotateY(42deg) rotateZ(0deg); } to { transform: rotateX(75deg) rotateY(42deg) rotateZ(360deg); } }
    @keyframes spinRing4 { from { transform: rotateX(62deg) rotateY(-40deg) rotateZ(0deg); } to { transform: rotateX(62deg) rotateY(-40deg) rotateZ(360deg); } }

    /* =========================================================
       SCROLL INDICATOR (FUTURISTIC BOTTOM CENTER HUD)
       ========================================================= */
    .hero-scroll-indicator {
      position: absolute;
      bottom: 2rem;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.5rem;
      z-index: 10;
      color: var(--text-muted);
      cursor: pointer;
      transition: color 0.25s ease;
    }

    .hero-scroll-indicator:hover {
      color: var(--color-cyan);
    }

    .scroll-mouse-icon {
      width: 20px;
      height: 32px;
      border: 1.5px solid rgba(255, 255, 255, 0.25);
      border-radius: 9999px;
      position: relative;
    }

    .scroll-mouse-wheel {
      position: absolute;
      top: 6px;
      left: 50%;
      transform: translateX(-50%);
      width: 3px;
      height: 6px;
      background: var(--color-cyan);
      border-radius: 9999px;
      box-shadow: 0 0 8px var(--color-cyan);
      animation: mouseWheelAnim 2s infinite;
    }

    @keyframes mouseWheelAnim {
      0% { top: 6px; opacity: 1; }
      100% { top: 18px; opacity: 0; }
    }

    .scroll-hud-text {
      font-family: var(--font-mono);
      font-size: 0.65rem;
      letter-spacing: 0.2em;
      text-transform: uppercase;
    }

    .scroll-arrow-bounce {
      font-size: 0.85rem;
      animation: arrowBounce 1.8s infinite;
    }

    @keyframes arrowBounce {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(5px); }
    }

    /* Common Section Styles */
    .section {
      padding: 7.5rem 0;
      position: relative;
      z-index: 3;
    }

    .section-divider {
      position: absolute;
      top: 0;
      left: 5%;
      right: 5%;
      height: 1px;
      background: linear-gradient(90deg, transparent 0%, rgba(255, 255, 255, 0.12) 30%, rgba(139, 92, 246, 0.28) 50%, rgba(34, 211, 238, 0.28) 70%, transparent 100%);
    }

    .section-head {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      gap: 2.5rem;
      margin-bottom: 4.5rem;
      position: relative;
    }

    .kicker {
      font-family: var(--font-mono);
      font-size: 0.76rem;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: var(--color-cyan);
      margin-bottom: 0.85rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .kicker::before {
      content: '//';
      color: var(--color-violet);
      font-weight: 600;
    }

    .section-head h2 {
      font-family: var(--font-display);
      font-size: clamp(2.4rem, 4.2vw, 3.8rem);
      font-weight: 700;
      line-height: 1.1;
      letter-spacing: -0.035em;
      color: var(--text-main);
    }

    .section-head p {
      max-width: 540px;
      color: var(--text-secondary);
      font-size: 1.05rem;
      line-height: 1.65;
    }

    .grad-accent {
      background: linear-gradient(135deg, #22d3ee 0%, #4f7cff 60%, #8b5cf6 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      display: inline-block;
    }

    /* Products Grid */
    .products-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 2.25rem;
    }

    .world-card {
      background: rgba(8, 12, 28, 0.65);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid rgba(255, 255, 255, 0.09);
      border-radius: 28px;
      padding: 2.25rem;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 20px 50px -15px rgba(0, 0, 0, 0.7);
      transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1),
                  border-color 0.35s ease,
                  box-shadow 0.35s ease,
                  background 0.35s ease;
      transform-style: preserve-3d;
    }

    .card-watermark {
      position: absolute;
      top: -10%;
      right: -8%;
      width: 280px;
      height: 280px;
      opacity: 0.05;
      pointer-events: none;
      filter: blur(1px);
      transition: opacity 0.4s ease, transform 0.4s ease;
      z-index: 0;
    }

    .world-card:hover .card-watermark {
      opacity: 0.09;
      transform: scale(1.06) rotate(4deg);
    }

    .world-card:hover {
      background: rgba(12, 18, 42, 0.8);
      transform: translateY(-8px);
    }

    .world-card.card-checkra:hover {
      border-color: rgba(139, 92, 246, 0.6);
      box-shadow: 0 28px 65px -15px rgba(0, 0, 0, 0.85), 0 0 45px rgba(139, 92, 246, 0.28);
    }
    .world-card.card-homora:hover {
      border-color: rgba(6, 182, 212, 0.6);
      box-shadow: 0 28px 65px -15px rgba(0, 0, 0, 0.85), 0 0 45px rgba(6, 182, 212, 0.28);
    }
    .world-card.card-bubora:hover {
      border-color: rgba(236, 72, 153, 0.6);
      box-shadow: 0 28px 65px -15px rgba(0, 0, 0, 0.85), 0 0 45px rgba(236, 72, 153, 0.28);
    }
    .world-card.card-sayora:hover {
      border-color: rgba(16, 185, 129, 0.6);
      box-shadow: 0 28px 65px -15px rgba(0, 0, 0, 0.85), 0 0 45px rgba(16, 185, 129, 0.28);
    }

    .world-art-wrap {
      width: 100%;
      height: 200px;
      border-radius: 20px;
      background: rgba(4, 6, 16, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.06);
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 2rem;
      position: relative;
      overflow: hidden;
    }

    .world-art-wrap img {
      max-height: 120px;
      max-width: 80%;
      object-fit: contain;
      filter: drop-shadow(0 0 25px rgba(0, 0, 0, 0.7));
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      z-index: 1;
    }

    .world-card:hover .world-art-wrap img {
      transform: scale(1.05);
    }

    .card-checkra .world-art-wrap img {
      mix-blend-mode: screen;
      filter: drop-shadow(0 0 25px rgba(139, 92, 246, 0.6));
    }
    .card-homora .world-art-wrap img {
      mix-blend-mode: screen;
      filter: drop-shadow(0 0 25px rgba(6, 182, 212, 0.6));
    }
    .card-watermark {
      mix-blend-mode: screen;
    }

    .world-header {
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      margin-bottom: 0.65rem;
      position: relative;
      z-index: 1;
    }

    .world-header h3 {
      font-family: var(--font-display);
      font-size: 1.85rem;
      font-weight: 700;
      letter-spacing: -0.03em;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 0.65rem;
    }

    .formerly-tag {
      font-family: var(--font-mono);
      font-size: 0.65rem;
      letter-spacing: 0.12em;
      color: var(--text-dim);
      font-weight: 400;
      background: rgba(255, 255, 255, 0.05);
      padding: 0.2rem 0.55rem;
      border-radius: 6px;
    }

    .status-badge {
      font-family: var(--font-mono);
      font-size: 0.68rem;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      padding: 0.3rem 0.75rem;
      border-radius: 9999px;
      font-weight: 600;
    }

    .badge-live {
      background: rgba(16, 185, 129, 0.12);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.3);
    }

    .badge-dev {
      background: rgba(6, 182, 212, 0.12);
      color: #38bdf8;
      border: 1px solid rgba(6, 182, 212, 0.3);
    }

    .world-tagline {
      font-family: var(--font-body);
      font-size: 1.02rem;
      font-weight: 500;
      color: var(--color-cyan);
      margin-bottom: 1.15rem;
      position: relative;
      z-index: 1;
    }

    .world-desc {
      color: var(--text-secondary);
      font-size: 0.95rem;
      line-height: 1.65;
      margin-bottom: 1.65rem;
      position: relative;
      z-index: 1;
    }

    .world-capabilities {
      display: flex;
      flex-wrap: wrap;
      gap: 0.55rem;
      margin-bottom: 2rem;
      position: relative;
      z-index: 1;
    }

    .cap-pill {
      font-family: var(--font-mono);
      font-size: 0.72rem;
      letter-spacing: 0.06em;
      color: var(--text-secondary);
      padding: 0.3rem 0.75rem;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 8px;
    }

    .world-actions {
      display: flex;
      align-items: center;
      gap: 1rem;
      margin-top: auto;
      padding-top: 1.25rem;
      border-top: 1px solid rgba(255, 255, 255, 0.07);
      position: relative;
      z-index: 1;
    }

    .btn-concept {
      font-family: var(--font-body);
      font-size: 0.875rem;
      font-weight: 600;
      padding: 0.65rem 1.35rem;
      border-radius: 9999px;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.16);
      color: #ffffff;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.25s ease;
    }

    .btn-concept:hover {
      background: rgba(255, 255, 255, 0.12);
      border-color: rgba(255, 255, 255, 0.35);
      transform: translateY(-1px);
    }

    .world-link {
      font-size: 0.85rem;
      font-weight: 500;
      color: var(--text-secondary);
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      margin-left: auto;
      transition: color 0.2s ease;
    }

    .world-link:hover {
      color: #ffffff;
    }

    /* Lifecycle Pipeline */
    .pipeline-wrapper {
      background: rgba(8, 12, 28, 0.6);
      backdrop-filter: blur(20px);
      border: 1px solid rgba(255, 255, 255, 0.09);
      border-radius: 32px;
      padding: 3rem 2.5rem;
      margin-bottom: 3.5rem;
      position: relative;
      overflow: hidden;
      box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.8);
    }

    .pipeline-header {
      text-align: center;
      max-width: 680px;
      margin: 0 auto 3.5rem;
    }

    .pipeline-header h3 {
      font-family: var(--font-display);
      font-size: 2rem;
      font-weight: 700;
      letter-spacing: -0.03em;
      color: #ffffff;
      margin-bottom: 0.65rem;
    }

    .pipeline-header p {
      color: var(--text-secondary);
      font-size: 1rem;
    }

    .pipeline-pathway {
      position: relative;
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 1.5rem;
      z-index: 2;
    }

    .pathway-circuit-line {
      position: absolute;
      top: 42px;
      left: 10%;
      right: 10%;
      height: 2px;
      background: linear-gradient(90deg, #8b5cf6 0%, #4f7cff 25%, #22d3ee 50%, #ec4899 75%, #10b981 100%);
      z-index: 0;
      opacity: 0.55;
    }

    .pathway-laser-pulse {
      position: absolute;
      top: -2px;
      left: 0;
      width: 60px;
      height: 6px;
      border-radius: 9999px;
      background: #ffffff;
      box-shadow: 0 0 16px #22d3ee, 0 0 25px #8b5cf6;
      animation: moveLaser 6s ease-in-out infinite;
    }

    @keyframes moveLaser {
      0% { left: 0%; opacity: 0; }
      10% { opacity: 1; }
      90% { opacity: 1; }
      100% { left: 100%; opacity: 0; }
    }

    .pipe-step-node {
      background: rgba(6, 8, 20, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 20px;
      padding: 1.85rem 1.25rem;
      display: flex;
      flex-direction: column;
      position: relative;
      z-index: 1;
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.6);
    }

    .pipe-step-node:hover {
      transform: translateY(-8px);
      border-color: rgba(34, 211, 238, 0.6);
      background: rgba(12, 18, 42, 0.95);
      box-shadow: 0 20px 45px -10px rgba(0, 0, 0, 0.8), 0 0 35px rgba(34, 211, 238, 0.25);
    }

    .pipe-node-badge {
      font-family: var(--font-mono);
      font-size: 0.68rem;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--color-cyan);
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .pipe-node-badge::before {
      content: '';
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--color-cyan);
      box-shadow: 0 0 8px var(--color-cyan);
    }

    .pipe-step-node b {
      font-family: var(--font-display);
      font-size: 1.35rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 0.75rem;
      display: block;
    }

    .pipe-step-node p {
      font-size: 0.875rem;
      line-height: 1.6;
      color: var(--text-secondary);
    }

    /* Methodology 3 Pillars */
    .methodology-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 2rem;
    }

    .meth-card {
      background: rgba(8, 12, 28, 0.55);
      backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 24px;
      padding: 2.25rem;
      transition: all 0.3s ease;
      position: relative;
    }

    .meth-card:hover {
      background: rgba(12, 18, 42, 0.75);
      border-color: rgba(255, 255, 255, 0.2);
      transform: translateY(-5px);
    }

    .meth-card h3 {
      font-family: var(--font-display);
      font-size: 1.35rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 0.85rem;
    }

    .meth-card p {
      font-size: 0.95rem;
      line-height: 1.65;
      color: var(--text-secondary);
    }

    /* Founder Section */
    .portfolio-grid {
      display: grid;
      grid-template-columns: 0.9fr 1.1fr;
      align-items: center;
      gap: 4rem;
    }

    .founder-image-wrapper {
      position: relative;
      border-radius: 32px;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.14);
      background: rgba(6, 8, 20, 0.85);
      box-shadow: 0 30px 70px -15px rgba(0, 0, 0, 0.9), 0 0 40px rgba(139, 92, 246, 0.25);
    }

    .founder-halo {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 320px;
      height: 320px;
      background: radial-gradient(circle, rgba(139, 92, 246, 0.45) 0%, rgba(6, 182, 212, 0.25) 50%, transparent 70%);
      filter: blur(50px);
      z-index: 0;
      pointer-events: none;
    }

    .founder-image-wrapper img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      position: relative;
      z-index: 1;
      filter: contrast(1.05);
      transition: transform 0.5s ease;
    }

    .founder-image-wrapper:hover img {
      transform: scale(1.03);
    }

    .corner-bracket {
      position: absolute;
      width: 12px;
      height: 12px;
      pointer-events: none;
      z-index: 2;
    }
    .bracket-tl { top: 12px; left: 12px; border-top: 2px solid var(--color-cyan); border-left: 2px solid var(--color-cyan); }
    .bracket-tr { top: 12px; right: 12px; border-top: 2px solid var(--color-cyan); border-right: 2px solid var(--color-cyan); }
    .bracket-bl { bottom: 12px; left: 12px; border-bottom: 2px solid var(--color-cyan); border-left: 2px solid var(--color-cyan); }
    .bracket-br { bottom: 12px; right: 12px; border-bottom: 2px solid var(--color-cyan); border-right: 2px solid var(--color-cyan); }

    .founder-content { position: relative; }
    .founder-eyebrow {
      font-family: var(--font-mono);
      font-size: 0.74rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--color-cyan);
      margin-bottom: 0.65rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .founder-name {
      font-family: var(--font-display);
      font-size: clamp(2.5rem, 4.5vw, 3.8rem);
      font-weight: 800;
      line-height: 1.05;
      letter-spacing: -0.04em;
      color: #ffffff;
      margin-bottom: 0.5rem;
    }

    .founder-titles {
      font-family: var(--font-mono);
      font-size: 0.85rem;
      letter-spacing: 0.08em;
      color: var(--color-cyan);
      margin-bottom: 1.75rem;
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
    }

    .founder-bio {
      font-size: 1.05rem;
      line-height: 1.7;
      color: var(--text-secondary);
      margin-bottom: 2rem;
    }

    .founder-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 0.65rem;
      margin-bottom: 2.25rem;
    }

    .fpill {
      font-family: var(--font-mono);
      font-size: 0.76rem;
      letter-spacing: 0.08em;
      color: var(--text-main);
      padding: 0.4rem 0.9rem;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 9999px;
    }

    .founder-quote {
      border-left: 2px solid var(--color-violet);
      padding-left: 1.5rem;
      font-style: italic;
      color: var(--text-secondary);
      font-size: 1.02rem;
      line-height: 1.6;
      margin-bottom: 2.25rem;
    }

    /* Philosophy Constellation */
    .central-thesis-wrap {
      text-align: center;
      margin-bottom: 4rem;
    }

    .central-thesis-banner {
      font-family: var(--font-display);
      font-size: clamp(1.8rem, 3.4vw, 2.75rem);
      font-weight: 700;
      line-height: 1.25;
      letter-spacing: -0.03em;
      color: #ffffff;
      max-width: 880px;
      margin: 0 auto 1.25rem;
    }

    .central-thesis-sub {
      font-family: var(--font-mono);
      font-size: 0.85rem;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: var(--color-cyan);
    }

    .philosophy-constellation {
      background: rgba(8, 12, 28, 0.65);
      backdrop-filter: blur(24px);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 36px;
      padding: 3.5rem 2.5rem;
      margin-bottom: 3.5rem;
      position: relative;
      overflow: hidden;
      box-shadow: 0 30px 70px -15px rgba(0, 0, 0, 0.85);
    }

    .constellation-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.75rem;
      position: relative;
      z-index: 2;
    }

    .constellation-node {
      background: rgba(6, 8, 20, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 22px;
      padding: 2rem 1.5rem;
      display: flex;
      flex-direction: column;
      position: relative;
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .node-theme-tag {
      font-family: var(--font-mono);
      font-size: 0.7rem;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      padding: 0.25rem 0.65rem;
      border-radius: 9999px;
      display: inline-block;
      width: fit-content;
      margin-bottom: 1rem;
      font-weight: 600;
    }

    .node-checkra { border-color: rgba(139, 92, 246, 0.25); }
    .node-checkra .node-theme-tag {
      background: rgba(139, 92, 246, 0.15);
      color: #c4b5fd;
      border: 1px solid rgba(139, 92, 246, 0.35);
    }
    .node-checkra:hover {
      border-color: var(--color-checkra);
      box-shadow: 0 20px 45px -10px rgba(0, 0, 0, 0.8), 0 0 35px var(--glow-checkra);
      transform: translateY(-8px);
    }

    .node-homora { border-color: rgba(6, 182, 212, 0.25); }
    .node-homora .node-theme-tag {
      background: rgba(6, 182, 212, 0.15);
      color: #67e8f9;
      border: 1px solid rgba(6, 182, 212, 0.35);
    }
    .node-homora:hover {
      border-color: var(--color-homora);
      box-shadow: 0 20px 45px -10px rgba(0, 0, 0, 0.8), 0 0 35px var(--glow-homora);
      transform: translateY(-8px);
    }

    .node-bubora { border-color: rgba(236, 72, 153, 0.25); }
    .node-bubora .node-theme-tag {
      background: rgba(236, 72, 153, 0.15);
      color: #f472b6;
      border: 1px solid rgba(236, 72, 153, 0.35);
    }
    .node-bubora:hover {
      border-color: var(--color-bubora);
      box-shadow: 0 20px 45px -10px rgba(0, 0, 0, 0.8), 0 0 35px var(--glow-bubora);
      transform: translateY(-8px);
    }

    .node-sayora { border-color: rgba(16, 185, 129, 0.25); }
    .node-sayora .node-theme-tag {
      background: rgba(16, 185, 129, 0.15);
      color: #6ee7b7;
      border: 1px solid rgba(16, 185, 129, 0.35);
    }
    .node-sayora:hover {
      border-color: var(--color-sayora);
      box-shadow: 0 20px 45px -10px rgba(0, 0, 0, 0.8), 0 0 35px var(--glow-sayora);
      transform: translateY(-8px);
    }

    .constellation-node h4 {
      font-family: var(--font-display);
      font-size: 1.5rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 0.65rem;
    }

    .constellation-node p {
      font-size: 0.9rem;
      line-height: 1.6;
      color: var(--text-secondary);
    }

    /* 4 Ecosystem Pillars */
    .ecosystem-pillars-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.75rem;
    }

    .eco-pillar-card {
      background: rgba(8, 12, 28, 0.5);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 20px;
      padding: 1.85rem;
      transition: all 0.3s ease;
    }

    .eco-pillar-card:hover {
      background: rgba(12, 18, 42, 0.7);
      border-color: rgba(255, 255, 255, 0.2);
      transform: translateY(-4px);
    }

    .eco-pillar-card h4 {
      font-family: var(--font-display);
      font-size: 1.2rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 0.75rem;
    }

    .eco-pillar-card p {
      font-size: 0.875rem;
      line-height: 1.6;
      color: var(--text-secondary);
    }

    /* FOLIVIO Section */
    .folivio-banner {
      background: rgba(8, 12, 32, 0.65);
      backdrop-filter: blur(20px);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 32px;
      padding: 3.5rem;
      display: grid;
      grid-template-columns: 200px 1fr;
      gap: 3.5rem;
      align-items: center;
      margin-bottom: 3rem;
      box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.8), 0 0 40px rgba(6, 182, 212, 0.15);
    }

    .folivio-logo-wrap {
      width: 180px;
      height: 180px;
      border-radius: 28px;
      background: rgba(4, 6, 16, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.12);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
      box-shadow: 0 20px 45px -10px rgba(0, 0, 0, 0.8);
    }

    .folivio-logo-wrap img {
      width: 100%;
      height: 100%;
      object-fit: contain;
    }

    .folivio-content h3 {
      font-family: var(--font-display);
      font-size: 2.4rem;
      font-weight: 800;
      letter-spacing: -0.03em;
      color: #ffffff;
      margin-bottom: 0.4rem;
    }

    .folivio-tagline {
      font-family: var(--font-body);
      font-size: 1.15rem;
      font-weight: 500;
      color: var(--text-secondary);
      margin-bottom: 1.25rem;
    }

    .folivio-tagline b {
      color: var(--color-cyan);
    }

    .folivio-desc {
      font-size: 1.05rem;
      line-height: 1.68;
      color: var(--text-secondary);
      margin-bottom: 2rem;
      max-width: 720px;
    }

    .folivio-services-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.75rem;
    }

    .folivio-service-card {
      background: rgba(8, 12, 28, 0.55);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 20px;
      padding: 1.85rem;
      transition: all 0.3s ease;
    }

    .folivio-service-card:hover {
      background: rgba(12, 18, 42, 0.8);
      border-color: rgba(6, 182, 212, 0.4);
      transform: translateY(-4px);
    }

    .folivio-service-card h4 {
      font-family: var(--font-display);
      font-size: 1.15rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 0.65rem;
    }

    .folivio-service-card p {
      font-size: 0.875rem;
      line-height: 1.6;
      color: var(--text-secondary);
    }

    /* Contact Section */
    .contact-wrapper {
      display: grid;
      grid-template-columns: 0.9fr 1.1fr;
      gap: 3.5rem;
      background: rgba(8, 12, 28, 0.65);
      backdrop-filter: blur(24px);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 36px;
      padding: 3.5rem;
      box-shadow: 0 30px 80px -20px rgba(0, 0, 0, 0.9), 0 0 50px rgba(139, 92, 246, 0.2);
      position: relative;
      overflow: hidden;
    }

    .contact-info-panel h3 {
      font-family: var(--font-display);
      font-size: 2.2rem;
      font-weight: 700;
      letter-spacing: -0.03em;
      color: #ffffff;
      margin-bottom: 0.85rem;
    }

    .contact-info-panel p {
      color: var(--text-secondary);
      font-size: 1.05rem;
      line-height: 1.68;
      margin-bottom: 2.25rem;
    }

    .contact-card-link {
      display: flex;
      align-items: center;
      gap: 1.15rem;
      padding: 1.25rem 1.5rem;
      background: rgba(6, 8, 20, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 18px;
      text-decoration: none;
      margin-bottom: 2rem;
      transition: all 0.25s ease;
    }

    .contact-card-link:hover {
      background: rgba(12, 18, 42, 0.9);
      border-color: rgba(34, 211, 238, 0.5);
      transform: translateY(-2px);
    }

    .ccl-icon {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: rgba(34, 211, 238, 0.1);
      border: 1px solid rgba(34, 211, 238, 0.25);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--color-cyan);
    }

    .ccl-icon svg { width: 22px; height: 22px; fill: currentColor; }
    .ccl-text b { font-family: var(--font-display); font-size: 1rem; color: #ffffff; display: block; }
    .ccl-text span { font-size: 0.825rem; color: var(--text-secondary); }

    .folivio-redirect-notice {
      padding: 1.25rem;
      border-radius: 16px;
      background: rgba(6, 182, 212, 0.06);
      border: 1px solid rgba(6, 182, 212, 0.2);
      font-size: 0.875rem;
      color: var(--text-secondary);
      line-height: 1.6;
    }

    .folivio-redirect-notice strong {
      color: var(--color-cyan);
      display: block;
      margin-bottom: 0.35rem;
    }

    .folivio-redirect-notice a {
      color: #ffffff;
      text-decoration: underline;
      font-weight: 600;
    }

    .form-group { margin-bottom: 1.5rem; }
    .form-group label {
      display: block;
      font-family: var(--font-mono);
      font-size: 0.76rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--text-secondary);
      margin-bottom: 0.6rem;
    }

    .form-control {
      width: 100%;
      padding: 0.95rem 1.25rem;
      background: rgba(6, 8, 20, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 14px;
      color: #ffffff;
      font-family: var(--font-body);
      font-size: 0.95rem;
      outline: none;
      transition: all 0.25s ease;
    }

    .form-control:focus {
      border-color: var(--color-cyan);
      box-shadow: 0 0 20px rgba(34, 211, 238, 0.25);
      background: rgba(10, 15, 34, 0.9);
    }

    textarea.form-control { resize: vertical; min-height: 130px; }

    .btn-submit {
      width: 100%;
      font-size: 1rem;
      font-weight: 600;
      padding: 1rem;
      border-radius: 14px;
      background: linear-gradient(135deg, #8b5cf6 0%, #4f7cff 50%, #22d3ee 100%);
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.25);
      box-shadow: 0 12px 30px -8px rgba(139, 92, 246, 0.6);
      transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .btn-submit:hover {
      transform: translateY(-2px);
      box-shadow: 0 16px 40px -8px rgba(139, 92, 246, 0.85);
      border-color: rgba(255, 255, 255, 0.45);
    }

    .form-toast {
      display: none;
      margin-top: 1.25rem;
      padding: 0.85rem 1.25rem;
      background: rgba(16, 185, 129, 0.12);
      border: 1px solid rgba(16, 185, 129, 0.35);
      border-radius: 12px;
      color: #34d399;
      font-size: 0.875rem;
      text-align: center;
    }

    /* Footer */
    .site-footer {
      padding: 5rem 0 3rem;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      position: relative;
      background: rgba(2, 3, 8, 0.85);
      z-index: 3;
    }

    .footer-grid {
      display: grid;
      grid-template-columns: 1.5fr 1fr 1fr 1fr;
      gap: 3.5rem;
      margin-bottom: 4rem;
    }

    .footer-brand p {
      color: var(--text-muted);
      font-size: 0.9rem;
      line-height: 1.6;
      max-width: 320px;
      margin-top: 1rem;
    }

    .footer-col h4 {
      font-family: var(--font-display);
      font-size: 0.95rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 1.25rem;
      letter-spacing: -0.01em;
    }

    .footer-col ul { list-style: none; }
    .footer-col li { margin-bottom: 0.75rem; }
    .footer-col a { color: var(--text-secondary); font-size: 0.875rem; transition: color 0.2s ease; }
    .footer-col a:hover { color: #ffffff; }

    .footer-bottom {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 2rem;
      border-top: 1px solid rgba(255, 255, 255, 0.06);
      font-size: 0.825rem;
      color: var(--text-muted);
    }

    /* Concept Modal */
    #conceptModalOverlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(2, 4, 12, 0.88);
      backdrop-filter: blur(28px) saturate(180%);
      -webkit-backdrop-filter: blur(28px) saturate(180%);
      z-index: 10000;
      display: flex;
      flex-direction: column;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }

    #conceptModalOverlay.active { opacity: 1; pointer-events: auto; }

    .modal-top-bar {
      height: 72px;
      background: rgba(6, 9, 22, 0.85);
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 2rem;
      flex-shrink: 0;
      z-index: 10;
    }

    .modal-top-left { display: flex; align-items: center; gap: 1.5rem; }
    .btn-return-modal {
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-secondary);
      padding: 0.55rem 1.15rem;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 9999px;
      transition: all 0.25s ease;
    }

    .btn-return-modal:hover { background: rgba(255, 255, 255, 0.12); color: #ffffff; border-color: rgba(255, 255, 255, 0.3); }

    .modal-brand-subtle { display: flex; align-items: center; gap: 0.65rem; font-family: var(--font-display); font-size: 1rem; color: #ffffff; }
    .mbs-nivora { color: var(--text-muted); font-weight: 500; }
    .mbs-product-name { font-weight: 700; color: #ffffff; }
    .mbs-status-badge {
      font-family: var(--font-mono);
      font-size: 0.65rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      padding: 0.2rem 0.55rem;
      background: rgba(34, 211, 238, 0.12);
      color: var(--color-cyan);
      border: 1px solid rgba(34, 211, 238, 0.3);
      border-radius: 9999px;
    }

    .modal-nav-tabs {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      background: rgba(255, 255, 255, 0.04);
      padding: 0.3rem;
      border-radius: 9999px;
      border: 1px solid rgba(255, 255, 255, 0.08);
    }

    .modal-nav-tab {
      font-size: 0.825rem;
      font-weight: 500;
      color: var(--text-secondary);
      padding: 0.4rem 0.95rem;
      border-radius: 9999px;
      transition: all 0.2s ease;
    }

    .modal-nav-tab:hover { color: #ffffff; }
    .modal-nav-tab.active { background: rgba(255, 255, 255, 0.12); color: #ffffff; }

    .modal-top-right { display: flex; align-items: center; gap: 1.25rem; }
    .modal-launch-btn {
      font-size: 0.85rem;
      font-weight: 600;
      padding: 0.55rem 1.25rem;
      border-radius: 9999px;
      background: linear-gradient(135deg, #8b5cf6, #4f7cff);
      color: #ffffff;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      box-shadow: 0 6px 18px rgba(139, 92, 246, 0.4);
    }

    .modal-launch-btn:hover { transform: translateY(-1px); box-shadow: 0 10px 24px rgba(139, 92, 246, 0.6); }

    .modal-close-x {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: var(--text-secondary);
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s ease;
    }

    .modal-close-x:hover { background: rgba(255, 255, 255, 0.15); color: #ffffff; transform: scale(1.05); }

    .modal-scrollable-body { flex: 1; overflow-y: auto; padding: 3rem 2rem 5rem; }
    .modal-product-view { display: none; max-width: 1140px; margin: 0 auto; }
    .modal-product-view.active { display: block; animation: modalFadeIn 0.35s cubic-bezier(0.16, 1, 0.3, 1); }

    @keyframes modalFadeIn {
      from { opacity: 0; transform: translateY(12px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .modal-hero-sec { margin-bottom: 4rem; }
    .modal-product-branding {
      display: flex;
      align-items: center;
      gap: 1.5rem;
      margin-bottom: 1.25rem;
    }
    .modal-brand-emblem-icon {
      width: 72px;
      height: 72px;
      object-fit: contain;
      border-radius: 18px;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 10px;
      mix-blend-mode: screen;
      filter: drop-shadow(0 0 20px rgba(139, 92, 246, 0.5));
      flex-shrink: 0;
    }
    @media (max-width: 640px) {
      .modal-product-branding {
        flex-direction: column;
        align-items: flex-start;
        gap: 1rem;
      }
    }
    .modal-kicker {
      font-family: var(--font-mono);
      font-size: 0.76rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--color-cyan);
      margin-bottom: 0.75rem;
    }

    .modal-hero-sec h2 {
      font-family: var(--font-display);
      font-size: clamp(2.4rem, 4vw, 3.4rem);
      font-weight: 700;
      letter-spacing: -0.03em;
      color: #ffffff;
      margin-bottom: 1.5rem;
    }

    .modal-lead-box {
      background: rgba(8, 12, 28, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-left: 3px solid var(--color-violet);
      border-radius: 20px;
      padding: 2rem 2.25rem;
      font-size: 1.15rem;
      line-height: 1.7;
      color: var(--text-main);
      box-shadow: 0 16px 40px -10px rgba(0, 0, 0, 0.6);
    }

    .modal-section-title {
      font-family: var(--font-display);
      font-size: 2rem;
      font-weight: 700;
      letter-spacing: -0.03em;
      color: #ffffff;
      margin-bottom: 2rem;
    }

    .modal-caps-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.5rem;
      margin-bottom: 4.5rem;
    }

    .modal-cap-card {
      background: rgba(8, 12, 28, 0.55);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 18px;
      padding: 1.65rem;
      transition: all 0.25s ease;
    }

    .modal-cap-card:hover {
      background: rgba(12, 18, 42, 0.8);
      border-color: rgba(255, 255, 255, 0.2);
      transform: translateY(-4px);
    }

    .modal-cap-icon {
      width: 40px;
      height: 40px;
      border-radius: 10px;
      background: rgba(139, 92, 246, 0.12);
      border: 1px solid rgba(139, 92, 246, 0.25);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--color-violet);
      margin-bottom: 1.15rem;
    }

    .modal-cap-card h4 {
      font-family: var(--font-display);
      font-size: 1.05rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 0.5rem;
    }

    .modal-cap-card p {
      font-size: 0.85rem;
      line-height: 1.55;
      color: var(--text-secondary);
    }

    /* Responsive Design */
    @media (max-width: 1024px) {
      .hero-grid { grid-template-columns: 1fr; gap: 4rem; text-align: center; }
      .hero-copy { margin-left: auto; margin-right: auto; }
      .hero-actions { justify-content: center; }
      .hero-metrics { justify-content: center; }
      .products-grid { grid-template-columns: 1fr; }
      .portfolio-grid { grid-template-columns: 1fr; gap: 3rem; }
      .constellation-grid { grid-template-columns: repeat(2, 1fr); }
      .ecosystem-pillars-grid { grid-template-columns: repeat(2, 1fr); }
      .folivio-banner { grid-template-columns: 1fr; text-align: center; justify-items: center; }
      .folivio-services-grid { grid-template-columns: repeat(2, 1fr); }
      .contact-wrapper { grid-template-columns: 1fr; }
      .footer-grid { grid-template-columns: repeat(2, 1fr); }
      .pipeline-pathway { grid-template-columns: 1fr; gap: 1rem; }
      .pathway-circuit-line { display: none; }
      .modal-caps-grid { grid-template-columns: repeat(2, 1fr); }
    }

    @media (max-width: 640px) {
      .site-nav { width: calc(100% - 1.5rem); padding: 0 1rem; }
      .nav-links { display: none; }
      .hero-metrics { flex-direction: column; gap: 1.5rem; }
      .constellation-grid { grid-template-columns: 1fr; }
      .ecosystem-pillars-grid { grid-template-columns: 1fr; }
      .folivio-services-grid { grid-template-columns: 1fr; }
      .footer-grid { grid-template-columns: 1fr; }
      .methodology-grid { grid-template-columns: 1fr; }
      .modal-caps-grid { grid-template-columns: 1fr; }
      .modal-nav-tabs { display: none; }
      .nivora-globe-core { width: 300px; height: 300px; }
      .ring-1, .ring-2, .ring-3, .ring-4 { transform: scale(0.7); }
    }
  </style>
</head>
<body>

  <!-- CUSTOM DESKTOP 3D CURSOR -->
  <div class="custom-cursor-ring" id="cursorRing"></div>
  <div class="custom-cursor-dot" id="cursorDot"></div>

  <!-- THREE.JS WEBGL CANVAS (REAL 3D STARFIELD) -->
  <canvas id="webglCanvas"></canvas>

  <!-- LAYER 2: RICH COSMIC NEBULAE ENVIRONMENT -->
  <div class="cosmic-nebulae-container" id="cosmicNebulae">
    <div class="nebula-wash"></div>
    <div class="nebula-globe-aura"></div>
    <div class="nebula-left-cloud"></div>
  </div>

  <!-- CELESTIAL GRID OVERLAY -->
  <div class="cosmic-grid-overlay"></div>

  <!-- PLANETARY FOREGROUND (BOTTOM EDGES FOR SCALE) -->
  <div class="foreground-planet-left"></div>
  <div class="foreground-planet-right"></div>

  <!-- NAVIGATION BAR (FLOATING CONTROL CAPSULE) -->
  <header class="site-nav" id="mainNav">
    <a href="#hero" class="nav-brand" aria-label="NIVORA Home">
      <img src="assets/images/nivora-logo.png" alt="NIVORA Core Logo" class="nav-brand-logo">
      <div class="nav-brand-text">
        <span class="nav-brand-title">NIVORA</span>
        <span class="nav-brand-tag">DIGITAL UNIVERSE</span>
      </div>
    </a>

    <nav class="nav-links" aria-label="Main Navigation">
      <a href="#hero" class="nav-item active">Home</a>
      <a href="#products" class="nav-item">Products</a>
      <a href="#about" class="nav-item">About</a>
      <a href="#portfolio" class="nav-item">Portfolio</a>
      <a href="#vision" class="nav-item">Vision</a>
      <a href="#folivio" class="nav-item">FOLIVIO</a>
      <a href="#contact" class="nav-item">Contact</a>
    </nav>

    <div class="nav-actions">
      <div class="nav-telemetry">
        <span class="pulse-dot"></span>
        <span id="navTelemetryText">STATUS: ONLINE</span>
      </div>
      <button type="button" class="btn-nav-explore" onclick="enterUniverseZoom()">
        <span>Explore Universe</span>
        <span class="btn-arrow">→</span>
      </button>
    </div>
  </header>

  <!-- MAIN SCROLLABLE CONTENT -->
  <main>

    <!-- =========================================================
         HERO — CINEMATIC 3D DIGITAL PLANET & UNIVERSE
         ========================================================= -->
    <section class="hero" id="hero">
      <div class="container hero-grid">
        <!-- LEFT HERO CONTENT -->
        <div class="hero-left">
          <div class="hero-badge-pill">
            <span class="badge-pulse-cyan"></span>
            <span>A NIVAS BENNABATTHULA INITIATIVE</span>
          </div>
          
          <h1 class="hero-title">
            <span class="hero-sub-lead">Welcome to</span>
            <span class="grad-nivora">NIVORA.</span>
          </h1>

          <div class="hero-tagline-wrap">
            Turning <em class="editorial-accent">Ideas</em> Into Intelligent <em class="editorial-accent">Products</em>.
          </div>

          <p class="hero-copy">
            NIVORA is the <strong>technology and innovation universe built by Nivas Bennabatthula</strong> &mdash; where ambitious ideas become intelligent products, meaningful experiences and new digital possibilities.
          </p>

          <div class="hero-actions">
            <button type="button" class="btn-enter-universe" onclick="enterUniverseZoom()">
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
          </div>
        </div>

        <!-- RIGHT HERO CONTENT: 3D DIGITAL PLANET & GALAXY PLATFORM -->
        <div class="hero-art-stage" id="heroArtStage">
          <div class="globe-pivot-container" id="globePivot">
            <!-- Galaxy Platform Beneath Globe -->
            <div class="galaxy-platform-wrap">
              <div class="galaxy-platform-vortex"></div>
            </div>

            <!-- Vertical Energy Beam -->
            <div class="galaxy-energy-beam"></div>

            <!-- Central Futuristic Globe / Digital Planet -->
            <div class="nivora-globe-core" onclick="enterUniverseZoom()" title="Click to Enter the NIVORA Universe">
              <div class="globe-digital-mesh"></div>
              <div class="globe-data-points"></div>
              <img src="assets/images/nivora-logo.png" alt="Official NIVORA Core Logo" class="globe-center-logo">
            </div>

            <!-- 4 Thin 3D Orbital Rings with Independent Rotation -->
            <div class="globe-orbital-ring ring-1"></div>
            <div class="globe-orbital-ring ring-2"></div>
            <div class="globe-orbital-ring ring-3"></div>
            <div class="globe-orbital-ring ring-4"></div>
          </div>
        </div>
      </div>

      <!-- SCROLL INDICATOR (HUD FOOTER) -->
      <div class="hero-scroll-indicator" onclick="enterUniverseZoom()">
        <div class="scroll-mouse-icon">
          <div class="scroll-mouse-wheel"></div>
        </div>
        <span class="scroll-hud-text">SCROLL TO EXPLORE THE UNIVERSE</span>
        <span class="scroll-arrow-bounce">&darr;</span>
      </div>
    </section>

    <!-- =========================================================
       SECTION 01: PRODUCTS WITH A PURPOSE (#products)
       THE PRODUCT CONSTELLATION
       ========================================================= -->
    <section class="section" id="products">
      <div class="section-divider"></div>
      <div class="container">
        <div class="section-head">
          <div>
            <div class="kicker">01 &middot; The Product Constellation</div>
            <h2>Products with<br><span class="grad-accent">a Purpose.</span></h2>
          </div>
          <p>
            Inside the NIVORA ecosystem, ideas transform into focused digital worlds. Each product addresses real human frictions with high-grade engineering, AI intelligence, and deliberate craftsmanship.
          </p>
        </div>

        <div class="products-grid">
          <!-- CARD 1: CHECKRA -->
          <article class="world-card card-checkra">
            <img src="assets/images/checkra-emblem.png" alt="" class="card-watermark">
            <div class="world-art-wrap">
              <img src="assets/images/checkra-logo.png" alt="CHECKRA logo" loading="lazy">
            </div>

            <div class="world-header">
              <h3>CHECKRA <span class="formerly-tag">Formerly VeriWrite</span></h3>
              <span class="status-badge badge-live">Live App</span>
            </div>

            <div class="world-tagline">
              Writing Integrity &amp; <em class="editorial-accent">Plagiarism Intelligence</em>
            </div>

            <p class="world-desc">
              Advanced verification engine designed to check, verify, and elevate written work through multi-layer plagiarism detection, source authenticity signals, and AI-assisted integrity scoring.
            </p>

            <div class="world-capabilities">
              <span class="cap-pill">Multi-Source Cross-Check</span>
              <span class="cap-pill">Citation Lineage</span>
              <span class="cap-pill">Originality Telemetry</span>
              <span class="cap-pill">Context-Aware Match</span>
            </div>

            <div class="world-actions">
              <button type="button" class="btn-concept" onclick="openConceptModal('checkra')">
                <span>Explore Concept</span>
                <span class="btn-arrow">&rarr;</span>
              </button>
              <a class="world-link" href="https://checkra-xi.vercel.app/" target="_blank" rel="noopener noreferrer">
                <span>Launch App</span>
                <span>&nearr;</span>
              </a>
            </div>
          </article>

          <!-- CARD 2: HOMORA -->
          <article class="world-card card-homora">
            <img src="assets/images/homora-logo.png" alt="" class="card-watermark">
            <div class="world-art-wrap">
              <img src="assets/images/homora-logo.png" alt="HOMORA logo" loading="lazy">
            </div>

            <div class="world-header">
              <h3>HOMORA</h3>
              <span class="status-badge badge-dev">Active Prototype</span>
            </div>

            <div class="world-tagline">
              Smart Living &amp; <em class="editorial-accent">Shared Finance</em>
            </div>

            <p class="world-desc">
              AI-powered financial harmony platform for shared households, roommates, and co-living spaces &mdash; effortlessly coordinating contributions, expenses, and home management.
            </p>

            <div class="world-capabilities">
              <span class="cap-pill">FairShare Split Engine</span>
              <span class="cap-pill">Automated Ledger</span>
              <span class="cap-pill">Household Chores Sync</span>
              <span class="cap-pill">Dispute-Free Accounting</span>
            </div>

            <div class="world-actions">
              <button type="button" class="btn-concept" onclick="openConceptModal('homora')">
                <span>Explore Concept</span>
                <span class="btn-arrow">&rarr;</span>
              </button>
              <a class="world-link" href="https://homora-ai.vercel.app/" target="_blank" rel="noopener noreferrer">
                <span>Launch App</span>
                <span>&nearr;</span>
              </a>
            </div>
          </article>

          <!-- CARD 3: BUBORA -->
          <article class="world-card card-bubora">
            <img src="assets/images/bubora-logo.png" alt="" class="card-watermark">
            <div class="world-art-wrap">
              <img src="assets/images/bubora-logo.png" alt="BUBORA logo" loading="lazy">
            </div>

            <div class="world-header">
              <h3>BUBORA</h3>
              <span class="status-badge badge-live">Live App</span>
            </div>

            <div class="world-tagline">
              A Private Digital Space for <em class="editorial-accent">Couples</em>
            </div>

            <p class="world-desc">
              An intimate digital sanctuary engineered for two &mdash; uniting private messaging, shared memories, collaborative bucket lists, and relationship milestones away from social media noise.
            </p>

            <div class="world-capabilities">
              <span class="cap-pill">Encrypted Dual-Vault</span>
              <span class="cap-pill">Shared TimeCapsule</span>
              <span class="cap-pill">Mood Resonance</span>
              <span class="cap-pill">Zero Third-Party Ads</span>
            </div>

            <div class="world-actions">
              <button type="button" class="btn-concept" onclick="openConceptModal('bubora')">
                <span>Explore Concept</span>
                <span class="btn-arrow">&rarr;</span>
              </button>
              <a class="world-link" href="https://bubora.netlify.app/" target="_blank" rel="noopener noreferrer">
                <span>Launch App</span>
                <span>&nearr;</span>
              </a>
            </div>
          </article>

          <!-- CARD 4: SAYORA -->
          <article class="world-card card-sayora">
            <img src="assets/images/sayora-emblem.png" alt="" class="card-watermark">
            <div class="world-art-wrap">
              <img src="assets/images/sayora-logo.png" alt="SAYORA logo" loading="lazy">
            </div>

            <div class="world-header">
              <h3>SAYORA</h3>
              <span class="status-badge badge-dev">Concept &middot; In Dev</span>
            </div>

            <div class="world-tagline">
              Financial Resilience for <em class="editorial-accent">Workers &amp; Communities</em>
            </div>

            <p class="world-desc">
              Social impact fintech initiative architected to shield informal laborers and delivery gig workers against income shocks, health emergencies, and catastrophic disruptions.
            </p>

            <div class="world-capabilities">
              <span class="cap-pill">Micro-Safety Pools</span>
              <span class="cap-pill">Parametric Payouts</span>
              <span class="cap-pill">Emergency Buffer OS</span>
              <span class="cap-pill">Community Shield</span>
            </div>

            <div class="world-actions">
              <button type="button" class="btn-concept" onclick="openConceptModal('sayora')">
                <span>Explore Concept</span>
                <span class="btn-arrow">&rarr;</span>
              </button>
              <span class="world-link" style="color:var(--text-muted); cursor:not-allowed;">
                <span>In Development</span>
              </span>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- =========================================================
       SECTION 02: METHODOLOGY & CRAFT (#about)
       LIFECYCLE PIPELINE PATHWAY + 3 PILLARS
       ========================================================= -->
    <section class="section" id="about">
      <div class="section-divider"></div>
      <div class="container">
        <div class="section-head">
          <div>
            <div class="kicker">02 &middot; Methodology &amp; Craft</div>
            <h2>Building What<br><span class="grad-accent">Comes Next.</span></h2>
          </div>
          <p>
            NIVORA is an independent, founder-led ecosystem where ideas move with purpose from theoretical notebooks into scalable, production-grade products that solve real human frictions.
          </p>
        </div>

        <div class="pipeline-wrapper">
          <div class="pipeline-header">
            <h3>The NIVORA Lifecycle Pipeline</h3>
            <p>From initial spark to lasting social footprint &mdash; every product in the universe traverses five deliberate stages of creation.</p>
          </div>

          <div class="pipeline-pathway">
            <div class="pathway-circuit-line">
              <div class="pathway-laser-pulse"></div>
            </div>

            <div class="pipe-step-node">
              <div class="pipe-node-badge">STAGE 01</div>
              <b>Idea</b>
              <p>Identifying unaddressed frictions in finance, writing integrity, relationships, and modern labor markets.</p>
            </div>

            <div class="pipe-step-node">
              <div class="pipe-node-badge">STAGE 02</div>
              <b>Design</b>
              <p>Crafting high-fidelity, cinematic digital interfaces rooted in intuitive glassmorphism and clear visual hierarchy.</p>
            </div>

            <div class="pipe-step-node">
              <div class="pipe-node-badge">STAGE 03</div>
              <b>Build</b>
              <p>Architecting resilient software systems using modern web frameworks, AI models, and clean engineering paradigms.</p>
            </div>

            <div class="pipe-step-node">
              <div class="pipe-node-badge">STAGE 04</div>
              <b>Refine</b>
              <p>Refining functional prototypes into cohesive, standalone digital universes with distinct brand identities.</p>
            </div>

            <div class="pipe-step-node">
              <div class="pipe-node-badge">STAGE 05</div>
              <b>Impact</b>
              <p>Deploying solutions that protect integrity, empower households, strengthen relationships, and shield communities.</p>
            </div>
          </div>
        </div>

        <div class="methodology-grid">
          <div class="meth-card">
            <h3>Practical Technology</h3>
            <p>Technology is built to solve actual, measurable human problems &mdash; not to chase temporary tech hype or produce discardable features.</p>
          </div>
          <div class="meth-card">
            <h3>AI &amp; Intelligence</h3>
            <p>Integrating modern machine learning and contextual reasoning into everyday workflows &mdash; making verification, financial tracking, and connection effortless.</p>
          </div>
          <div class="meth-card">
            <h3>Deliberate Craftsmanship</h3>
            <p>Every layout, animation, database schema, and micro-interaction is executed with obsessive care for durability, speed, and aesthetic refinement.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- =========================================================
       SECTION 03: THE ARCHITECT (#portfolio)
       ========================================================= -->
    <section class="section" id="portfolio">
      <div class="section-divider"></div>
      <div class="container">
        <div class="section-head">
          <div>
            <div class="kicker">03 &middot; The Architect</div>
            <h2>Meet the<br><span class="grad-accent">Builder.</span></h2>
          </div>
          <p>
            NIVORA is founder-led. The vision, architectural direction, design language, and execution are driven directly by Nivas Bennabatthula.
          </p>
        </div>

        <div class="portfolio-grid">
          <div class="founder-image-wrapper">
            <div class="founder-halo"></div>
            <div class="corner-bracket bracket-tl"></div>
            <div class="corner-bracket bracket-tr"></div>
            <div class="corner-bracket bracket-bl"></div>
            <div class="corner-bracket bracket-br"></div>
            <img src="assets/images/founder-nivas.png" alt="Nivas Bennabatthula &mdash; Founder &amp; Architect of NIVORA">
          </div>

          <div class="founder-content">
            <div class="founder-eyebrow">// FOUNDER &middot; PRODUCT BUILDER</div>
            <h3 class="founder-name">Nivas <span class="grad-nivora">Bennabatthula</span></h3>
            <div class="founder-titles">
              <span>Founder &amp; Architect</span> &bull; 
              <span>Product Builder</span> &bull; 
              <span>Finance &amp; Tech Enthusiast</span>
            </div>

            <p class="founder-bio">
              Nivas is building NIVORA as a sanctuary where ambitious ideas transcend notes and prototypes to become tangible, intelligent software. Driven by a deep curiosity at the intersection of quantitative finance, intuitive interface design, and artificial intelligence, he crafts products from first principles &mdash; obsessive about craft, execution, and lasting purpose.
            </p>

            <div class="founder-pills">
              <span class="fpill">Autonomous Systems</span>
              <span class="fpill">Product Strategy</span>
              <span class="fpill">Full-Stack Architecture</span>
              <span class="fpill">AI Integrations</span>
              <span class="fpill">Design Systems</span>
              <span class="fpill">Fintech Mechanisms</span>
            </div>

            <div class="founder-quote">
              &ldquo;True innovation is never about adding noise to an already loud world. It is about distilling complex human challenges into products so elegant and natural they feel inevitable.&rdquo;
            </div>

            <a class="btn-enter-universe" href="https://nivas2703.vercel.app/" target="_blank" rel="noopener noreferrer">
              <span>Visit Official Founder Portfolio</span>
              <span>&nearr;</span>
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- =========================================================
       SECTION 04: ECOSYSTEM PHILOSOPHY & ARCHITECTURE (#vision)
       ========================================================= -->
    <section class="section" id="vision">
      <div class="section-divider"></div>
      <div class="container">
        <div class="section-head">
          <div>
            <div class="kicker">04 &middot; Ecosystem Philosophy &amp; Architecture</div>
            <h2>One Universe.<br><span class="grad-accent">Different Possibilities.</span></h2>
          </div>
          <p>
            A multi-dimensional ecosystem uniting distinct product worlds under a singular technological thesis: purposeful intelligence and immaculate execution.
          </p>
        </div>

        <div class="central-thesis-wrap">
          <div class="central-thesis-banner">
            &ldquo;Ideas become products when <span class="grad-nivora">technology meets purpose.</span>&rdquo;
          </div>
          <div class="central-thesis-sub">// THE CORE OPERATING THESIS OF NIVORA</div>
        </div>

        <div class="philosophy-constellation">
          <div class="constellation-grid">
            <div class="constellation-node node-checkra">
              <span class="node-theme-tag">INTEGRITY</span>
              <h4>CHECKRA</h4>
              <p>Writing Integrity &amp; AI Plagiarism Intelligence &mdash; safeguarding truth and authenticity across scholarly and creative content.</p>
            </div>
            <div class="constellation-node node-homora">
              <span class="node-theme-tag">HARMONY</span>
              <h4>HOMORA</h4>
              <p>Shared Living &amp; Financial OS &mdash; automating collaborative household contributions and removing domestic friction.</p>
            </div>
            <div class="constellation-node node-bubora">
              <span class="node-theme-tag">CONNECTION</span>
              <h4>BUBORA</h4>
              <p>Couples Private Digital Sanctuary &mdash; preserving intimacy, shared memories, and emotional resonance in an ad-free space.</p>
            </div>
            <div class="constellation-node node-sayora">
              <span class="node-theme-tag">RESILIENCE</span>
              <h4>SAYORA</h4>
              <p>Worker Resilience &amp; Social Protection &mdash; architecting community micro-safety buffers for vulnerable gig workforces.</p>
            </div>
          </div>
        </div>

        <div class="ecosystem-pillars-grid">
          <div class="eco-pillar-card">
            <h4>Autonomous Utility</h4>
            <p>Every product operates with deep functional autonomy, reducing human friction through intelligent automation.</p>
          </div>
          <div class="eco-pillar-card">
            <h4>Human-First Privacy</h4>
            <p>Zero intrusive tracking, zero data monetization. Products are engineered as private digital sanctuaries.</p>
          </div>
          <div class="eco-pillar-card">
            <h4>Cross-Product Synergy</h4>
            <p>Unified design philosophy, shared design systems, and consistent architectural principles across all creations.</p>
          </div>
          <div class="eco-pillar-card">
            <h4>Founder-Driven Velocity</h4>
            <p>Direct architectural oversight by Nivas ensures uncompromised quality and rapid innovation cadence.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- =========================================================
       SECTION 05: FOLIVIO (#folivio)
       CAREER BRANDING · DIGITAL PRESENCE
       ========================================================= -->
    <section class="section" id="folivio">
      <div class="section-divider"></div>
      <div class="container">
        <div class="section-head">
          <div>
            <div class="kicker">05 &middot; Beyond NIVORA</div>
            <h2>Build your<br><span class="grad-accent">Career Presence.</span></h2>
          </div>
          <p>
            FOLIVIO is an independent professional career-branding service founded by Nivas &mdash; helping students, freshers, and professionals turn their education, skills, projects, certifications, and experience into polished career profiles.
          </p>
        </div>

        <div class="folivio-banner">
          <div class="folivio-logo-wrap">
            <img src="assets/images/folivio-logo.webp" alt="FOLIVIO Official Brand Logo" loading="lazy">
          </div>
          <div class="folivio-content">
            <h3>FOLIVIO</h3>
            <div class="folivio-tagline">Build. <b>Showcase.</b> Grow.</div>
            <p class="folivio-desc">
              Professional career branding for ambitious individuals who want their work, credentials, and digital footprint to look as formidable online as they are on paper.
            </p>
            <a class="btn-enter-universe" href="https://www.instagram.com/folivio.ai?utm_source=ig_web_button_share_sheet&rpxt=ZDNlZDc0MzIxNw==" target="_blank" rel="noopener noreferrer">
              <span>Connect on Instagram</span>
              <span>&nearr;</span>
            </a>
          </div>
        </div>

        <div class="folivio-services-grid">
          <div class="folivio-service-card">
            <h4>Professional Resumes</h4>
            <p>Clean, ATS-friendly resume architectures that communicate impact, precision, and verified competence to hiring leads.</p>
          </div>
          <div class="folivio-service-card">
            <h4>Personal Portfolios</h4>
            <p>High-conversion project showcases that turn coursework, engineering builds, and internships into compelling proof-of-work.</p>
          </div>
          <div class="folivio-service-card">
            <h4>LinkedIn Makeovers</h4>
            <p>Optimized headlines, strategic summaries, and structured experience blocks that attract recruiters and founders.</p>
          </div>
          <div class="folivio-service-card">
            <h4>Portfolio Websites</h4>
            <p>Bespoke, cinematic personal web presences that stand out in competitive software and technology applicant pools.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- =========================================================
       SECTION 06: CONTACT (#contact)
       ========================================================= -->
    <section class="section" id="contact">
      <div class="section-divider"></div>
      <div class="container">
        <div class="section-head">
          <div>
            <div class="kicker">06 &middot; Collaboration &amp; Inquiries</div>
            <h2>Have an Idea?<br><span class="grad-accent">Let's Build It.</span></h2>
          </div>
          <p>
            NIVORA is always exploring new ideas, products, and possibilities. Whether you are interested in a product collaboration, technology discussion, or ecosystem partnership, let us connect.
          </p>
        </div>

        <div class="contact-wrapper">
          <div class="contact-info-panel">
            <h3>Enter the Universe.</h3>
            <p>
              Connect directly with Nivas Bennabatthula regarding NIVORA initiatives, product development, or new technology ventures.
            </p>

            <div class="contact-methods">
              <a class="contact-card-link" href="https://nivas2703.vercel.app/" target="_blank" rel="noopener noreferrer">
                <div class="ccl-icon">
                  <svg viewBox="0 0 24 24">
                    <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/>
                  </svg>
                </div>
                <div class="ccl-text">
                  <b>Official Founder Website</b>
                  <span>Explore Nivas's projects &amp; profile</span>
                </div>
              </a>
            </div>

            <div class="folivio-redirect-notice">
              <strong>Looking for Career Branding?</strong>
              For resumes, portfolios, and LinkedIn profile makeovers, please reach out directly through the official <a href="https://www.instagram.com/folivio.ai?utm_source=ig_web_button_share_sheet&rpxt=ZDNlZDc0MzIxNw==" target="_blank" rel="noopener noreferrer">FOLIVIO Instagram</a>.
            </div>
          </div>

          <div class="contact-form-panel">
            <form id="nivoraContactForm" onsubmit="handleContactSubmit(event)">
              <div class="form-group">
                <label for="contactName">Your Name</label>
                <input type="text" id="contactName" class="form-control" placeholder="e.g. Alex Morgan" required>
              </div>

              <div class="form-group">
                <label for="contactEmail">Email Address</label>
                <input type="email" id="contactEmail" class="form-control" placeholder="alex@example.com" required>
              </div>

              <div class="form-group">
                <label for="contactSubject">Area of Interest</label>
                <select id="contactSubject" class="form-control">
                  <option value="Product Collaboration">Product Collaboration</option>
                  <option value="CHECKRA Discussion">CHECKRA Writing Integrity</option>
                  <option value="HOMORA Shared Finance">HOMORA Shared Living OS</option>
                  <option value="BUBORA Platform">BUBORA Private Space</option>
                  <option value="SAYORA Social Impact">SAYORA Financial Shield</option>
                  <option value="Technology & Architecture">Technology &amp; Architecture</option>
                  <option value="Other Inquiries">General / Other Inquiry</option>
                </select>
              </div>

              <div class="form-group">
                <label for="contactMessage">Message / Idea Description</label>
                <textarea id="contactMessage" class="form-control" placeholder="Tell us about your project, idea, or how we might collaborate..." required></textarea>
              </div>

              <button type="submit" class="btn-submit" id="contactSubmitBtn">
                <span>Start a Conversation &rarr;</span>
              </button>

              <div class="form-toast" id="contactToast"></div>
            </form>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- =========================================================
       FOOTER
       ========================================================= -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="nav-brand">
            <img src="assets/images/nivora-logo.png" alt="NIVORA Logo" class="nav-brand-logo">
            <div class="nav-brand-text">
              <span class="nav-brand-title">NIVORA</span>
              <span class="nav-brand-tag">DIGITAL UNIVERSE</span>
            </div>
          </div>
          <p>Turning ideas into intelligent products. An independent technology universe architected and engineered by Nivas Bennabatthula.</p>
        </div>

        <div class="footer-col">
          <h4>Ecosystem</h4>
          <ul>
            <li><a href="https://checkra-xi.vercel.app/" target="_blank" rel="noopener noreferrer">CHECKRA</a></li>
            <li><a href="https://homora-ai.vercel.app/" target="_blank" rel="noopener noreferrer">HOMORA</a></li>
            <li><a href="https://bubora.netlify.app/" target="_blank" rel="noopener noreferrer">BUBORA</a></li>
            <li><a href="#products">SAYORA</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Navigation</h4>
          <ul>
            <li><a href="#hero">Universe Core</a></li>
            <li><a href="#products">Product Constellation</a></li>
            <li><a href="#about">Methodology &amp; Craft</a></li>
            <li><a href="#portfolio">The Architect</a></li>
            <li><a href="#vision">Ecosystem Architecture</a></li>
            <li><a href="#folivio">FOLIVIO</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Initiatives</h4>
          <ul>
            <li><a href="https://nivas2703.vercel.app/" target="_blank" rel="noopener noreferrer">Nivas Bennabatthula</a></li>
            <li><a href="https://www.instagram.com/folivio.ai?utm_source=ig_web_button_share_sheet&rpxt=ZDNlZDc0MzIxNw==" target="_blank" rel="noopener noreferrer">FOLIVIO Career Branding</a></li>
            <li><a href="#contact">Collaboration &amp; Contact</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 NIVORA &mdash; Built with deliberate craft by Nivas Bennabatthula. All rights reserved.</div>
        <div>ONE BUILDER &bull; MULTIPLE IDEAS &bull; DIFFERENT WORLDS &bull; ONE VISION</div>
      </div>
    </div>
  </footer>

  <!-- =========================================================
       PREMIUM FIXED PRODUCT CONCEPT MODAL SYSTEM
       ========================================================= -->
  <div id="conceptModalOverlay" role="dialog" aria-modal="true" aria-hidden="true" data-lenis-prevent>
    <header class="modal-top-bar">
      <div class="modal-top-left">
        <button type="button" class="btn-return-modal" onclick="closeConceptModal()" aria-label="Return to NIVORA Universe (ESC)">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
          <span>Return to Universe</span>
        </button>

        <div class="modal-brand-subtle">
          <span class="mbs-nivora">NIVORA &middot;</span>
          <span class="mbs-product-name" id="modalTopProductName">CHECKRA</span>
          <span class="mbs-status-badge" id="modalTopStatusBadge">Live App</span>
        </div>
      </div>

      <nav class="modal-nav-tabs" aria-label="Modal In-World Navigation">
        <button type="button" class="modal-nav-tab active" onclick="scrollModalSec('overview')">Overview</button>
        <button type="button" class="modal-nav-tab" onclick="scrollModalSec('capabilities')">Capabilities</button>
        <button type="button" class="modal-nav-tab" onclick="scrollModalSec('workflow')">Workflow</button>
        <button type="button" class="modal-nav-tab" onclick="scrollModalSec('architecture')">Architecture</button>
        <button type="button" class="modal-nav-tab" onclick="scrollModalSec('vision')">Vision</button>
      </nav>

      <div class="modal-top-right">
        <a href="https://checkra-xi.vercel.app/" target="_blank" rel="noopener noreferrer" class="modal-launch-btn" id="modalLaunchBtn">
          <span>Launch App</span>
          <span class="btn-arrow">&nearr;</span>
        </a>
        <button type="button" class="modal-close-x" onclick="closeConceptModal()" aria-label="Close Modal (ESC)">
          <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </button>
      </div>
    </header>

    <div class="modal-scrollable-body" id="modalScrollBody" data-lenis-prevent>
      <!-- 1. CHECKRA MODAL VIEW -->
      <div class="modal-product-view active" id="modal-view-checkra">
        <div class="modal-hero-sec" id="msec-checkra-overview">
          <div class="modal-product-branding">
            <img src="assets/images/checkra-emblem.png" alt="CHECKRA Emblem" class="modal-brand-emblem-icon">
            <div class="modal-brand-text-col">
              <div class="modal-kicker">// CONCEPT OVERVIEW &middot; WRITING INTEGRITY SPACE</div>
              <h2>Empowering Writing Truth &amp; Source Accuracy</h2>
            </div>
          </div>
          <div class="modal-lead-box">
            CHECKRA is an AI-powered writing integrity and source verification platform designed to help students, researchers, educators, professionals, and content creators check, verify, and improve their writing in one connected workspace.
          </div>
        </div>

        <div id="msec-checkra-capabilities">
          <h3 class="modal-section-title">Engineered for Writing Truth &amp; Elevation</h3>
          <div class="modal-caps-grid">
            <div class="modal-cap-card">
              <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></div>
              <h4>Similarity Check</h4>
              <p>Multi-level comparison analyzing exact matches, near phrasing, and semantic overlap across open web sources.</p>
            </div>
            <div class="modal-cap-card">
              <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg></div>
              <h4>Source Verification</h4>
              <p>Indexes live web resources to provide verifiable context, metadata, and direct citations for detected matches.</p>
            </div>
            <div class="modal-cap-card">
              <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg></div>
              <h4>Document Analysis</h4>
              <p>Unified native ingestion of PDF, DOCX, TXT, HTML, and Markdown files with preserved layout parsing.</p>
            </div>
            <div class="modal-cap-card">
              <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg></div>
              <h4>AI Evidence Review</h4>
              <p>Assists reviewers in evaluating matches, distinguishing valid citations and idioms from true duplication.</p>
            </div>
          </div>
        </div>

        <div id="msec-checkra-workflow">
          <h3 class="modal-section-title">Workflow Architecture</h3>
          <div class="modal-caps-grid">
            <div class="modal-cap-card">
              <div class="modal-cap-icon">01</div>
              <h4>Native Ingestion</h4>
              <p>Upload documents or paste rich text into the secure client sandbox with instant word and token parsing.</p>
            </div>
            <div class="modal-cap-card">
              <div class="modal-cap-icon">02</div>
              <h4>Multi-Vector Scan</h4>
              <p>The core engine triggers parallel n-gram shingles, web crawling indexes, and embedding distance checks.</p>
            </div>
            <div class="modal-cap-card">
              <div class="modal-cap-icon">03</div>
              <h4>Integrity Telemetry</h4>
              <p>Visual split-pane telemetry displays side-by-side matching snippets, source domain validity, and trust score.</p>
            </div>
            <div class="modal-cap-card">
              <div class="modal-cap-icon">04</div>
              <h4>Export &amp; Improve</h4>
              <p>Generate shareable audit reports with highlighted improvements, citation suggestions, and verification badges.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- 2. HOMORA MODAL VIEW -->
      <div class="modal-product-view" id="modal-view-homora">
        <div class="modal-hero-sec" id="msec-homora-overview">
          <div class="modal-product-branding">
            <img src="assets/images/homora-logo.png" alt="HOMORA Emblem" class="modal-brand-emblem-icon" style="filter: drop-shadow(0 0 20px rgba(6, 182, 212, 0.5));">
            <div class="modal-brand-text-col">
              <div class="modal-kicker">// CONCEPT OVERVIEW &middot; SHARED LIVING OS</div>
              <h2>Smart Living &amp; Financial Harmony for Households</h2>
            </div>
          </div>
          <div class="modal-lead-box">
            HOMORA is an AI-powered financial harmony platform for shared households, roommates, and co-living spaces &mdash; effortlessly coordinating contributions, expenses, and domestic agreements without confrontation.
          </div>
        </div>

        <div id="msec-homora-capabilities">
          <h3 class="modal-section-title">Core Operating Capabilities</h3>
          <div class="modal-caps-grid">
            <div class="modal-cap-card">
              <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg></div>
              <h4>FairShare Split Engine</h4>
              <p>Custom split models (income-weighted, room-size based, or custom ratio) calculate equitable monthly balances.</p>
            </div>
            <div class="modal-cap-card">
              <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="5" width="20" height="14" rx="2"></rect><line x1="2" y1="10" x2="22" y2="10"></line></svg></div>
              <h4>Automated Ledger</h4>
              <p>Real-time shared expenditure tracker with multi-currency conversion, receipt OCR, and instant debt simplification.</p>
            </div>
            <div class="modal-cap-card">
              <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg></div>
              <h4>Household Chore Sync</h4>
              <p>Rotational cleaning and supply schedules balanced with financial contributions for transparent equity.</p>
            </div>
            <div class="modal-cap-card">
              <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg></div>
              <h4>Dispute-Free Mediation</h4>
              <p>Automated gentle nudges and neutral notifications eliminate interpersonal friction over money and bills.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- 3. BUBORA MODAL VIEW -->
      <div class="modal-product-view" id="modal-view-bubora">
        <div class="modal-hero-sec" id="msec-bubora-overview">
          <div class="modal-product-branding">
            <img src="assets/images/bubora-logo.png" alt="BUBORA Emblem" class="modal-brand-emblem-icon" style="filter: drop-shadow(0 0 20px rgba(236, 72, 153, 0.5));">
            <div class="modal-brand-text-col">
              <div class="modal-kicker">// CONCEPT OVERVIEW &middot; COUPLES PRIVATE SPACE</div>
              <h2>An Intimate Digital Sanctuary for Two</h2>
            </div>
          </div>
          <div class="modal-lead-box">
            BUBORA is an intimate digital sanctuary engineered exclusively for two &mdash; uniting private messaging, shared memory vaults, collaborative bucket lists, and relationship milestones away from public social feeds and noise.
          </div>
        </div>

        <div id="msec-bubora-capabilities">
          <h3 class="modal-section-title">Sanctuary Features</h3>
          <div class="modal-caps-grid">
            <div class="modal-cap-card">
              <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg></div>
              <h4>Encrypted Dual-Vault</h4>
              <p>Zero-knowledge encrypted repository for private photographs, voice notes, letters, and relationship artifacts.</p>
            </div>
            <div class="modal-cap-card">
              <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg></div>
              <h4>Shared TimeCapsule</h4>
              <p>Chronological relationship roadmap documenting milestones, anniversary countdowns, and future travel dreams.</p>
            </div>
            <div class="modal-cap-card">
              <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg></div>
              <h4>Mood Resonance</h4>
              <p>Subtle emotional check-ins that let partners express their feelings, support needs, and appreciation quietly.</p>
            </div>
            <div class="modal-cap-card">
              <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></div>
              <h4>Zero Advertisements</h4>
              <p>Strictly ad-free, private environment without social algorithms, surveillance metrics, or external audience pressure.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- 4. SAYORA MODAL VIEW -->
      <div class="modal-product-view" id="modal-view-sayora">
        <div class="modal-hero-sec" id="msec-sayora-overview">
          <div class="modal-product-branding">
            <img src="assets/images/sayora-emblem.png" alt="SAYORA Emblem" class="modal-brand-emblem-icon" style="filter: drop-shadow(0 0 20px rgba(16, 185, 129, 0.5));">
            <div class="modal-brand-text-col">
              <div class="modal-kicker">// CONCEPT OVERVIEW &middot; SOCIAL IMPACT &amp; FINANCIAL SHIELD</div>
              <h2>Financial Resilience for Workers &amp; Communities</h2>
            </div>
          </div>
          <div class="modal-lead-box">
            SAYORA is a social impact fintech initiative architected to shield informal laborers, gig delivery workers, and daily wage earners against sudden income shocks, health emergencies, and catastrophic climate disruptions.
          </div>
        </div>

        <div id="msec-sayora-capabilities">
          <h3 class="modal-section-title">Resilience Mechanisms</h3>
          <div class="modal-caps-grid">
            <div class="modal-cap-card">
              <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>
              <h4>Micro-Safety Pools</h4>
              <p>Decentralized peer safety buffers that pool minute daily contributions into high-resilience community lifelines.</p>
            </div>
            <div class="modal-cap-card">
              <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg></div>
              <h4>Parametric Payouts</h4>
              <p>Automated claim triggers linked to adverse weather events, extreme heat index, or verified mobility platform outages.</p>
            </div>
            <div class="modal-cap-card">
              <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"></rect><line x1="1" y1="10" x2="23" y2="10"></line></svg></div>
              <h4>Emergency Buffer OS</h4>
              <p>Zero-predatory-interest micro-drawdown facilities designed to stave off local loan shark cycles during emergencies.</p>
            </div>
            <div class="modal-cap-card">
              <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg></div>
              <h4>Community Shield Network</h4>
              <p>Grassroots mutual aid coordination linking worker federations, community centers, and non-profit micro-funds.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- =========================================================
       THREE.JS + GSAP + LENIS 3D UNIVERSE ENGINE
       ========================================================= -->
  <script>
    /* -------------------------------------------------------------
       1. LENIS SMOOTH SCROLL INITIALIZATION
       ------------------------------------------------------------- */
    let lenis;
    try {
      lenis = new Lenis({
        duration: 1.2,
        easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
        orientation: 'vertical',
        gestureOrientation: 'vertical',
        smoothWheel: true,
        wheelMultiplier: 1.0,
        touchMultiplier: 2.0,
      });

      function raf(time) {
        lenis.raf(time);
        requestAnimationFrame(raf);
      }
      requestAnimationFrame(raf);
    } catch(err) {
      console.warn('Lenis smooth scroll fallback:', err);
    }

    /* -------------------------------------------------------------
       2. THREE.JS 3D STARFIELD & COSMIC ENGINE
       ------------------------------------------------------------- */
    let scene, camera, renderer;
    let starParticles, particleGeo;
    let mouseX = 0, mouseY = 0;
    let targetMouseX = 0, targetMouseY = 0;
    let isZooming = false;
    let scrollProgress = 0;
    let canvas2DFallbackActive = false;
    let fallbackStars = [];
    let fallbackSpeed = 0.8;

    function initCanvas3DUniverse() {
      canvas2DFallbackActive = true;
      const canvas = document.getElementById('webglCanvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      if (!ctx) return;

      let width = canvas.width = window.innerWidth;
      let height = canvas.height = window.innerHeight;

      const numStars = window.innerWidth < 768 ? 240 : 650;
      fallbackStars = [];
      const colors = ['#ffffff', '#ffffff', '#c7d2fe', '#8b5cf6', '#22d3ee', '#ec4899', '#10b981'];

      for (let i = 0; i < numStars; i++) {
        fallbackStars.push({
          x: (Math.random() - 0.5) * 2600,
          y: (Math.random() - 0.5) * 1900,
          z: Math.random() * 2200 + 1,
          size: Math.random() * 2.2 + 0.6,
          color: colors[Math.floor(Math.random() * colors.length)],
          alpha: Math.random() * 0.65 + 0.35
        });
      }

      window.addEventListener('resize', () => {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
      });

      function renderCanvas3D() {
        if (!canvas2DFallbackActive) return;
        requestAnimationFrame(renderCanvas3D);

        ctx.fillStyle = '#010206';
        ctx.fillRect(0, 0, width, height);

        mouseX += (targetMouseX - mouseX) * 0.05;
        mouseY += (targetMouseY - mouseY) * 0.05;

        const fov = 350;
        const cx = width / 2 + mouseX * 45;
        const cy = height / 2 + mouseY * 35;

        for (let i = 0; i < fallbackStars.length; i++) {
          const s = fallbackStars[i];
          s.z -= fallbackSpeed;
          if (s.z <= 2) {
            s.z = 2200;
            s.x = (Math.random() - 0.5) * 2600;
            s.y = (Math.random() - 0.5) * 1900;
          }

          const k = fov / s.z;
          const px = s.x * k + cx;
          const py = s.y * k + cy;

          if (px < -60 || px > width + 60 || py < -60 || py > height + 60) continue;

          const rad = Math.max(0.4, (1 - s.z / 2200) * s.size * 1.8);

          if (fallbackSpeed > 2) {
            const prevZ = s.z + fallbackSpeed * 2.5;
            const prevK = fov / prevZ;
            const prevPx = s.x * prevK + cx;
            const prevPy = s.y * prevK + cy;

            ctx.beginPath();
            ctx.moveTo(prevPx, prevPy);
            ctx.lineTo(px, py);
            ctx.strokeStyle = s.color;
            ctx.lineWidth = rad * 0.85;
            ctx.globalAlpha = Math.min(1, s.alpha * (1 - s.z / 2200) * 1.4);
            ctx.stroke();
          } else {
            ctx.beginPath();
            ctx.arc(px, py, rad, 0, Math.PI * 2);
            ctx.fillStyle = s.color;
            ctx.globalAlpha = Math.min(1, s.alpha * (1 - s.z / 2200));
            ctx.fill();
          }
        }
      }
      renderCanvas3D();
    }

    function initThreeUniverse() {
      const canvas = document.getElementById('webglCanvas');
      if (!canvas || !window.THREE) {
        initCanvas3DUniverse();
        return;
      }

      const width = window.innerWidth;
      const height = window.innerHeight;

      scene = new THREE.Scene();
      camera = new THREE.PerspectiveCamera(60, width / height, 0.1, 4000);
      camera.position.set(0, 0, 600);

      try {
        renderer = new THREE.WebGLRenderer({
          canvas: canvas,
          antialias: true,
          alpha: true,
          powerPreference: 'default'
        });
      } catch (e1) {
        try {
          renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true });
        } catch (e2) {
          console.warn('WebGL renderer unavailable, falling back to 3D Canvas:', e2);
          initCanvas3DUniverse();
          return;
        }
      }

      if (renderer) {
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        renderer.setSize(width, height);
      }

      // Starfield BufferGeometry
      const particleCount = window.innerWidth < 768 ? 1400 : 3000;
      particleGeo = new THREE.BufferGeometry();
      const positions = new Float32Array(particleCount * 3);
      const colors = new Float32Array(particleCount * 3);

      const palette = [
        new THREE.Color('#ffffff'),
        new THREE.Color('#e0e7ff'),
        new THREE.Color('#8b5cf6'),
        new THREE.Color('#22d3ee'),
        new THREE.Color('#4f7cff'),
        new THREE.Color('#ec4899')
      ];

      for (let i = 0; i < particleCount; i++) {
        positions[i * 3] = (Math.random() - 0.5) * 2800;
        positions[i * 3 + 1] = (Math.random() - 0.5) * 2200;
        positions[i * 3 + 2] = (Math.random() - 0.5) * 3600 - 400;

        const col = palette[Math.floor(Math.random() * palette.length)];
        colors[i * 3] = col.r;
        colors[i * 3 + 1] = col.g;
        colors[i * 3 + 2] = col.b;
      }

      particleGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
      particleGeo.setAttribute('color', new THREE.BufferAttribute(colors, 3));

      // Circular texture
      const canvasTexture = document.createElement('canvas');
      canvasTexture.width = 32;
      canvasTexture.height = 32;
      const ctx = canvasTexture.getContext('2d');
      const grad = ctx.createRadialGradient(16, 16, 0, 16, 16, 16);
      grad.addColorStop(0, 'rgba(255,255,255,1)');
      grad.addColorStop(0.3, 'rgba(255,255,255,0.7)');
      grad.addColorStop(1, 'rgba(255,255,255,0)');
      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.arc(16, 16, 16, 0, Math.PI * 2);
      ctx.fill();

      const particleTex = new THREE.CanvasTexture(canvasTexture);

      const particleMat = new THREE.PointsMaterial({
        size: 3.4,
        vertexColors: true,
        map: particleTex,
        transparent: true,
        opacity: 0.82,
        depthWrite: false,
        blending: THREE.AdditiveBlending
      });

      starParticles = new THREE.Points(particleGeo, particleMat);
      scene.add(starParticles);

      window.addEventListener('resize', () => {
        if (!camera || !renderer) return;
        const w = window.innerWidth;
        const h = window.innerHeight;
        camera.aspect = w / h;
        camera.updateProjectionMatrix();
        renderer.setSize(w, h);
      });
    }

    // Mouse movement listener
    window.addEventListener('mousemove', (e) => {
      targetMouseX = (e.clientX - window.innerWidth / 2) / (window.innerWidth / 2);
      targetMouseY = (e.clientY - window.innerHeight / 2) / (window.innerHeight / 2);

      // Parallax for 3D globe and background nebulae
      const globePivot = document.getElementById('globePivot');
      if (globePivot) {
        globePivot.style.transform = `perspective(1200px) rotateX(${-targetMouseY * 8}deg) rotateY(${targetMouseX * 8}deg)`;
      }

      const nebulae = document.getElementById('cosmicNebulae');
      if (nebulae) {
        nebulae.style.transform = `translate(${-targetMouseX * 18}px, ${-targetMouseY * 18}px)`;
      }
    });

    // Scroll listener for camera journey
    window.addEventListener('scroll', () => {
      const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
      scrollProgress = maxScroll > 0 ? window.scrollY / maxScroll : 0;
      updateTelemetryOnScroll(window.scrollY);
    }, { passive: true });

    /* -------------------------------------------------------------
       3. THE BIG ZOOM — CINEMATIC GSAP CAMERA WARP
       ------------------------------------------------------------- */
    function enterUniverseZoom() {
      if (isZooming) return;
      isZooming = true;

      const globePivot = document.getElementById('globePivot');

      if (window.gsap) {
        const tl = gsap.timeline({
          onComplete: () => {
            isZooming = false;
            if (globePivot) gsap.set(globePivot, { clearProps: 'transform,opacity' });
          }
        });

        if (camera) {
          tl.to(camera.position, {
            z: -380,
            x: targetMouseX * 40,
            y: targetMouseY * 30,
            duration: 1.6,
            ease: 'power3.inOut'
          }, 0);
        }

        if (canvas2DFallbackActive) {
          tl.to({ speed: 0.8 }, {
            speed: 24,
            duration: 0.8,
            ease: 'power2.in',
            onUpdate: function() { fallbackSpeed = this.targets()[0].speed; }
          }, 0)
          .to({ speed: 24 }, {
            speed: 0.8,
            duration: 0.8,
            ease: 'power2.out',
            onUpdate: function() { fallbackSpeed = this.targets()[0].speed; }
          }, 0.8);
        }

        if (globePivot) {
          tl.to(globePivot, {
            scale: 3.2,
            opacity: 0,
            duration: 1.3,
            ease: 'power2.in'
          }, 0);
        }
      }

      if (lenis) {
        lenis.scrollTo('#products', { duration: 1.8, easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)) });
      } else {
        const prod = document.getElementById('products');
        if (prod) prod.scrollIntoView({ behavior: 'smooth' });
      }
    }

    /* -------------------------------------------------------------
       4. ANIMATION RENDER LOOP (60 FPS TARGET)
       ------------------------------------------------------------- */
    function animateUniverse(time) {
      requestAnimationFrame(animateUniverse);

      mouseX += (targetMouseX - mouseX) * 0.05;
      mouseY += (targetMouseY - mouseY) * 0.05;

      if (camera && !isZooming) {
        const targetZ = 600 - scrollProgress * 3000;
        camera.position.z += (targetZ - camera.position.z) * 0.08;

        const targetCamX = mouseX * 65;
        const targetCamY = -mouseY * 45;
        camera.position.x += (targetCamX - camera.position.x) * 0.06;
        camera.position.y += (targetCamY - camera.position.y) * 0.06;
        camera.lookAt(0, 0, camera.position.z - 400);
      }

      if (renderer && scene && camera) {
        renderer.render(scene, camera);
      }
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', () => {
        initThreeUniverse();
        requestAnimationFrame(animateUniverse);
      });
    } else {
      initThreeUniverse();
      requestAnimationFrame(animateUniverse);
    }

    /* -------------------------------------------------------------
       5. CUSTOM DESKTOP 3D CURSOR ENGINE
       ------------------------------------------------------------- */
    (function initCustomCursor() {
      const ring = document.getElementById('cursorRing');
      const dot = document.getElementById('cursorDot');
      if (!ring || !dot) return;

      let mouseX = -100;
      let mouseY = -100;
      let ringX = -100;
      let ringY = -100;

      window.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
        dot.style.left = mouseX + 'px';
        dot.style.top = mouseY + 'px';
      });

      function loopCursor() {
        ringX += (mouseX - ringX) * 0.16;
        ringY += (mouseY - ringY) * 0.16;
        ring.style.left = ringX + 'px';
        ring.style.top = ringY + 'px';
        requestAnimationFrame(loopCursor);
      }
      loopCursor();

      const hoverTargets = document.querySelectorAll('a, button, .world-card, .pipe-step-node, .constellation-node, .nivora-globe-core, .hero-scroll-indicator');
      hoverTargets.forEach(el => {
        el.addEventListener('mouseenter', () => ring.classList.add('cursor-hover'));
        el.addEventListener('mouseleave', () => ring.classList.remove('cursor-hover'));
      });
    })();

    /* -------------------------------------------------------------
       6. CARD 3D TILT ENGINE
       ------------------------------------------------------------- */
    (function initCardTilt() {
      document.querySelectorAll('.world-card').forEach(card => {
        card.addEventListener('mousemove', (e) => {
          const rect = card.getBoundingClientRect();
          const x = (e.clientX - rect.left - rect.width / 2) / (rect.width / 2);
          const y = (e.clientY - rect.top - rect.height / 2) / (rect.height / 2);
          card.style.transform = `perspective(1000px) translateY(-10px) rotateX(${-y * 4}deg) rotateY(${x * 4}deg)`;
        });
        card.addEventListener('mouseleave', () => {
          card.style.transform = 'perspective(1000px) translateY(0px) rotateX(0deg) rotateY(0deg)';
        });
      });
    })();

    /* -------------------------------------------------------------
       7. TELEMETRY & HUD UPDATE
       ------------------------------------------------------------- */
    function updateTelemetryOnScroll(scrollY) {
      const text = document.getElementById('navTelemetryText');
      const nav = document.getElementById('mainNav');
      if (nav) {
        if (scrollY > 50) nav.classList.add('scrolled');
        else nav.classList.remove('scrolled');
      }

      if (!text) return;

      const proSec = document.getElementById('products');
      const abtSec = document.getElementById('about');
      const porSec = document.getElementById('portfolio');
      const visSec = document.getElementById('vision');
      const folSec = document.getElementById('folivio');
      const conSec = document.getElementById('contact');

      if (conSec && scrollY >= conSec.offsetTop - 300) {
        text.innerText = 'SECTOR: TRANSMIT';
      } else if (folSec && scrollY >= folSec.offsetTop - 300) {
        text.innerText = 'SECTOR: FOLIVIO';
      } else if (visSec && scrollY >= visSec.offsetTop - 300) {
        text.innerText = 'SECTOR: ECOSYSTEM';
      } else if (porSec && scrollY >= porSec.offsetTop - 300) {
        text.innerText = 'SECTOR: ARCHITECT';
      } else if (abtSec && scrollY >= abtSec.offsetTop - 300) {
        text.innerText = 'SECTOR: CRAFT';
      } else if (proSec && scrollY >= proSec.offsetTop - 300) {
        text.innerText = 'SECTOR: CONSTELLATION';
      } else {
        text.innerText = 'STATUS: ONLINE';
      }
    }

    /* -------------------------------------------------------------
       8. PRODUCT CONCEPT MODAL CONTROLLER
       ------------------------------------------------------------- */
    const productMeta = {
      'checkra': {
        name: 'CHECKRA',
        badge: 'Live App',
        url: 'https://checkra-xi.vercel.app/'
      },
      'homora': {
        name: 'HOMORA',
        badge: 'Active Prototype',
        url: 'https://homora-ai.vercel.app/'
      },
      'bubora': {
        name: 'BUBORA',
        badge: 'Live App',
        url: 'https://bubora.netlify.app/'
      },
      'sayora': {
        name: 'SAYORA',
        badge: 'Concept · In Dev',
        url: ''
      }
    };

    function openConceptModal(productId) {
      const overlay = document.getElementById('conceptModalOverlay');
      if (!overlay) return;

      if (lenis) lenis.stop();

      const info = productMeta[productId] || { name: productId.toUpperCase(), badge: 'Product', url: '' };
      document.getElementById('modalTopProductName').innerText = info.name;
      document.getElementById('modalTopStatusBadge').innerText = info.badge;

      const launchBtn = document.getElementById('modalLaunchBtn');
      if (info.url) {
        launchBtn.style.display = 'inline-flex';
        launchBtn.href = info.url;
      } else {
        launchBtn.style.display = 'none';
      }

      document.querySelectorAll('.modal-product-view').forEach(view => {
        view.classList.remove('active');
      });
      const targetView = document.getElementById('modal-view-' + productId);
      if (targetView) {
        targetView.classList.add('active');
      }

      const scrollBody = document.getElementById('modalScrollBody');
      if (scrollBody) scrollBody.scrollTop = 0;

      document.body.classList.add('world-open');
      overlay.classList.add('active');
      overlay.setAttribute('aria-hidden', 'false');
    }

    function closeConceptModal() {
      const overlay = document.getElementById('conceptModalOverlay');
      if (!overlay) return;

      overlay.classList.remove('active');
      overlay.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('world-open');

      if (lenis) lenis.start();
    }

    function scrollModalSec(secId) {
      const activeView = document.querySelector('.modal-product-view.active');
      if (!activeView) return;

      const prodId = activeView.id.replace('modal-view-', '');
      const targetEl = document.getElementById('msec-' + prodId + '-' + secId);
      if (targetEl) {
        targetEl.scrollIntoView({ behavior: 'smooth' });
      }

      document.querySelectorAll('.modal-nav-tab').forEach(t => t.classList.remove('active'));
      const clickedTab = event?.target;
      if (clickedTab) clickedTab.classList.add('active');
    }

    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeConceptModal();
      }
    });

    document.getElementById('conceptModalOverlay')?.addEventListener('click', (e) => {
      if (e.target.id === 'conceptModalOverlay') {
        closeConceptModal();
      }
    });

    /* -------------------------------------------------------------
       9. CONTACT FORM TRANSMISSION HANDLER
       ------------------------------------------------------------- */
    function handleContactSubmit(e) {
      e.preventDefault();
      const btn = document.getElementById('contactSubmitBtn');
      const toast = document.getElementById('contactToast');
      const origText = btn.innerHTML;

      btn.innerHTML = '<span>Transmitting...</span>';
      btn.disabled = true;

      setTimeout(() => {
        btn.innerHTML = '<span>Transmitted Successfully ✓</span>';
        if (toast) {
          toast.style.display = 'inline-block';
          toast.innerText = 'Thank you. Your message has been dispatched directly to Nivas.';
        }
        e.target.reset();

        setTimeout(() => {
          btn.innerHTML = origText;
          btn.disabled = false;
          setTimeout(() => {
            if (toast) toast.style.display = 'none';
          }, 5000);
        }, 3000);
      }, 750);
    }
  </script>
</body>
</html>
"""

def build():
    html = generate_globe_hero_html()
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
