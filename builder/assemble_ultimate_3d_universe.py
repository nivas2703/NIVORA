# builder/assemble_ultimate_3d_universe.py
# NIVORA — THE 3D UNIVERSE IS THE HERO (MASTER ARCHITECTURAL GENERATOR)
import os
import sys

def build_ultimate_universe_html():
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
       NIVORA ULTIMATE 3D UNIVERSE DESIGN SYSTEM
       ========================================================= */
    :root {
      --bg-space-base: #010206;
      --bg-space-deep: #000103;
      
      --text-main: #f8faff;
      --text-secondary: #b8c0d9;
      --text-muted: #707a96;

      --brand-violet: #8b5cf6;
      --brand-purple: #a855f7;
      --brand-magenta: #d946ef;
      --brand-blue: #3b82f6;
      --brand-cyan: #06b6d4;
      --brand-glow-cyan: rgba(6, 182, 212, 0.45);
      --brand-glow-violet: rgba(139, 92, 246, 0.45);

      --font-display: 'Space Grotesk', -apple-system, sans-serif;
      --font-ui: 'Inter', -apple-system, sans-serif;
      --font-serif: 'Instrument Serif', Georgia, serif;
      --font-mono: 'JetBrains Mono', monospace;

      --color-checkra: #8b5cf6;
      --glow-checkra: rgba(139, 92, 246, 0.45);
      --color-homora: #06b6d4;
      --glow-homora: rgba(6, 182, 212, 0.45);
      --color-bubora: #ec4899;
      --glow-bubora: rgba(236, 72, 153, 0.45);
      --color-sayora: #10b981;
      --glow-sayora: rgba(16, 185, 129, 0.45);

      --color-primary: #8b5cf6;
      --color-cyan: #06b6d4;
      --color-purple: #a855f7;
      --color-magenta: #ec4899;
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      background-color: var(--bg-space-base);
      color: var(--text-main);
      font-family: var(--font-ui);
      scroll-behavior: auto;
      overflow-x: hidden;
    }

    body {
      background-color: var(--bg-space-base);
      color: var(--text-main);
      overflow-x: hidden;
      min-height: 100vh;
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    a {
      color: inherit;
      text-decoration: none;
    }

    /* =========================================================
       FIXED FULL-SCREEN 3D UNIVERSE CANVAS
       ========================================================= */
    #webglUniverseCanvas {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 1;
      pointer-events: none;
      display: block;
    }

    /* High-res Ambient Cosmic Background Layer behind WebGL */
    .cosmic-ambient-backdrop {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 0;
      pointer-events: none;
      background: url('assets/images/cinematic-universe-hero.jpg') center center / cover no-repeat,
                  radial-gradient(circle at 75% 45%, rgba(20, 24, 60, 0.5) 0%, rgba(10, 12, 30, 0.4) 40%, rgba(1, 2, 6, 0.95) 85%),
                  var(--bg-space-base);
      overflow: hidden;
    }

    /* Ambient Nebular Clouds */
    .cosmic-nebula-topleft {
      position: absolute;
      top: -10%;
      left: -8%;
      width: 55vw;
      height: 55vh;
      background: radial-gradient(ellipse at center, rgba(168, 85, 247, 0.28) 0%, rgba(147, 51, 234, 0.15) 45%, transparent 70%);
      filter: blur(50px);
      pointer-events: none;
      animation: nebulaPulse 12s ease-in-out infinite alternate;
    }

    .cosmic-nebula-rightcore {
      position: absolute;
      top: 15%;
      right: 5%;
      width: 50vw;
      height: 65vh;
      background: radial-gradient(circle at 60% 50%, rgba(6, 182, 212, 0.18) 0%, rgba(139, 92, 246, 0.22) 40%, rgba(217, 70, 239, 0.12) 65%, transparent 80%);
      filter: blur(60px);
      pointer-events: none;
      animation: nebulaPulse 14s ease-in-out infinite alternate-reverse;
    }

    .cosmic-nebula-bottommid {
      position: absolute;
      bottom: -15%;
      left: 30%;
      width: 45vw;
      height: 45vh;
      background: radial-gradient(ellipse at center, rgba(192, 38, 211, 0.22) 0%, rgba(88, 28, 135, 0.12) 50%, transparent 75%);
      filter: blur(55px);
      pointer-events: none;
    }

    @keyframes nebulaPulse {
      0% { transform: scale(1) translate(0, 0); opacity: 0.85; }
      50% { transform: scale(1.08) translate(10px, -8px); opacity: 1; }
      100% { transform: scale(0.96) translate(-10px, 8px); opacity: 0.8; }
    }

    /* =========================================================
       LUXURY FLOATING GLASS CAPSULE NAVIGATION
       ========================================================= */
    .top-nav {
      position: fixed;
      top: 1.5rem;
      left: 50%;
      transform: translateX(-50%);
      z-index: 100;
      width: 92%;
      max-width: 1240px;
    }

    .nav-capsule {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.5rem 1.25rem;
      background: rgba(4, 6, 18, 0.55);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 9999px;
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.7);
      transition: all 0.3s ease;
    }

    .nav-brand {
      display: flex;
      align-items: center;
      gap: 0.85rem;
      text-decoration: none;
    }

    .nav-logo-icon {
      width: 32px;
      height: 32px;
      object-fit: contain;
      filter: drop-shadow(0 0 12px rgba(6, 182, 212, 0.7));
      transition: transform 0.3s ease;
    }

    .nav-brand:hover .nav-logo-icon {
      transform: scale(1.08) rotate(5deg);
    }

    .nav-brand-text {
      display: flex;
      flex-direction: column;
      line-height: 1.15;
    }

    .brand-title {
      font-family: var(--font-display);
      font-size: 1.05rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      color: #ffffff;
    }

    .brand-subtitle {
      font-family: var(--font-mono);
      font-size: 0.58rem;
      letter-spacing: 0.18em;
      color: var(--brand-cyan);
      text-transform: uppercase;
    }

    .nav-links {
      display: flex;
      align-items: center;
      gap: 0.4rem;
      list-style: none;
    }

    .nav-link {
      padding: 0.45rem 1.05rem;
      font-size: 0.86rem;
      font-weight: 500;
      color: var(--text-secondary);
      border-radius: 9999px;
      transition: all 0.25s ease;
      position: relative;
    }

    .nav-link:hover {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.08);
    }

    .nav-link.active {
      color: #ffffff;
      background: linear-gradient(135deg, rgba(139, 92, 246, 0.45) 0%, rgba(6, 182, 212, 0.35) 100%);
      border: 1px solid rgba(255, 255, 255, 0.2);
      box-shadow: 0 0 20px rgba(139, 92, 246, 0.5);
    }

    .nav-right-actions {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .nav-status-pill {
      display: flex;
      align-items: center;
      gap: 0.45rem;
      padding: 0.35rem 0.85rem;
      background: rgba(6, 182, 212, 0.08);
      border: 1px solid rgba(6, 182, 212, 0.3);
      border-radius: 9999px;
      font-family: var(--font-mono);
      font-size: 0.68rem;
      font-weight: 600;
      letter-spacing: 0.12em;
      color: var(--brand-cyan);
    }

    .status-dot-pulse {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 10px #10b981;
      animation: dotPulse 2s ease-in-out infinite;
    }

    @keyframes dotPulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(0.8); }
    }

    .nav-cta-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.55rem 1.25rem;
      background: linear-gradient(135deg, #a855f7 0%, #3b82f6 50%, #06b6d4 100%);
      color: #ffffff;
      font-family: var(--font-ui);
      font-size: 0.84rem;
      font-weight: 600;
      border-radius: 9999px;
      border: 1px solid rgba(255, 255, 255, 0.25);
      box-shadow: 0 10px 25px -5px rgba(139, 92, 246, 0.6), 0 0 20px rgba(6, 182, 212, 0.4);
      cursor: pointer;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .nav-cta-btn:hover {
      transform: translateY(-2px) scale(1.03);
      box-shadow: 0 14px 30px -5px rgba(139, 92, 246, 0.8), 0 0 30px rgba(6, 182, 212, 0.6);
    }

    /* =========================================================
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
    }

    /* Founder Badge Pill */
    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.55rem;
      padding: 0.42rem 1.1rem;
      border-radius: 9999px;
      background: rgba(139, 92, 246, 0.12);
      border: 1px solid rgba(139, 92, 246, 0.4);
      box-shadow: 0 0 25px rgba(139, 92, 246, 0.35);
      margin-bottom: 1.2rem;
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
    }

    .hero-badge .dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--brand-cyan);
      box-shadow: 0 0 10px var(--brand-cyan);
      animation: dotPulse 2s infinite ease-in-out;
    }

    .hero-badge span {
      font-family: var(--font-mono);
      font-size: 0.72rem;
      font-weight: 600;
      letter-spacing: 0.16em;
      color: #d8b4fe;
      text-transform: uppercase;
    }

    /* Main Typography */
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
    }

    .editorial-accent {
      font-family: var(--font-serif);
      font-style: italic;
      font-size: 1.15em;
      font-weight: 400;
      color: #ffffff;
      position: relative;
      display: inline-block;
      padding: 0 0.1em;
    }

    .editorial-accent::after {
      content: '';
      position: absolute;
      left: 0.05em;
      right: 0.05em;
      bottom: -2px;
      height: 2px;
      background: linear-gradient(90deg, #ec4899, #a855f7, #06b6d4);
      border-radius: 9999px;
      box-shadow: 0 0 10px rgba(236, 72, 153, 0.8);
    }

    /* Description */
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
    }

    .btn-enter-universe {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.65rem;
      padding: 0.85rem 1.95rem;
      background: linear-gradient(135deg, #9333ea 0%, #3b82f6 50%, #06b6d4 100%);
      color: #ffffff;
      font-family: var(--font-ui);
      font-size: 0.95rem;
      font-weight: 600;
      border-radius: 9999px;
      border: 1px solid rgba(255, 255, 255, 0.2);
      box-shadow: 0 10px 25px -5px rgba(147, 51, 234, 0.45);
      cursor: pointer;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }

    .btn-enter-universe::before {
      content: '';
      position: absolute;
      top: -50%;
      left: -50%;
      width: 200%;
      height: 200%;
      background: radial-gradient(circle, rgba(255, 255, 255, 0.3) 0%, transparent 60%);
      opacity: 0;
      transition: opacity 0.3s ease;
      pointer-events: none;
    }

    .btn-enter-universe:hover {
      transform: translateY(-3px) scale(1.03);
      box-shadow: 0 22px 45px -8px rgba(168, 85, 247, 0.9),
                  0 0 50px rgba(6, 182, 212, 0.75);
    }

    .btn-enter-universe:hover::before {
      opacity: 1;
    }

    .btn-explore-products {
      display: inline-flex;
      align-items: center;
      gap: 0.65rem;
      padding: 0.85rem 1.65rem;
      background: rgba(10, 14, 32, 0.5);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 9999px;
      color: #ffffff;
      font-family: var(--font-ui);
      font-size: 0.92rem;
      font-weight: 600;
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      box-shadow: 0 8px 20px -6px rgba(0, 0, 0, 0.5);
      transition: all 0.25s ease;
      text-decoration: none;
    }

    .btn-explore-products:hover {
      background: rgba(255, 255, 255, 0.08);
      border-color: rgba(6, 182, 212, 0.5);
      transform: translateY(-2px);
      box-shadow: 0 16px 35px -8px rgba(0, 0, 0, 0.7), 0 0 30px rgba(6, 182, 212, 0.4);
    }

    .play-icon-circle {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      background: rgba(6, 182, 212, 0.2);
      border: 1px solid rgba(6, 182, 212, 0.4);
      font-size: 0.65rem;
      color: var(--brand-cyan);
    }

    /* Metrics Grid */
    .hero-metrics {
      display: flex;
      align-items: center;
      gap: 1.75rem;
      padding-top: 1.15rem;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      max-width: 480px;
    }

    .metric-card {
      display: flex;
      align-items: center;
      gap: 0.9rem;
    }

    .metric-icon-wrap {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 32px;
      height: 32px;
      border-radius: 8px;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
      flex-shrink: 0;
    }

    .metric-icon-wrap.m-purple { color: #c084fc; }
    .metric-icon-wrap.m-cyan { color: #67e8f9; }
    .metric-icon-wrap.m-magenta { color: #f472b6; }

    .metric-info {
      display: flex;
      flex-direction: column;
    }

    .metric-info strong {
      font-family: var(--font-display);
      font-size: 1.45rem;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.1;
    }

    .metric-info span {
      font-size: 0.76rem;
      color: var(--text-muted);
      letter-spacing: 0.02em;
    }

    /* Right Hero Click Target Area for Three.js Globe */
    .hero-art-stage {
      position: relative;
      width: 100%;
      height: 600px;
      display: flex;
      align-items: center;
      justify-content: center;
      pointer-events: auto; /* Allow clicking on 3D globe to trigger zoom */
      cursor: pointer;
    }

    /* Invisible click capture proxy for 3D globe */
    .globe-click-proxy {
      width: 440px;
      height: 440px;
      border-radius: 50%;
      position: relative;
      cursor: pointer;
    }

    /* HUD Bottom Scroll Indicator */
    .hero-scroll-indicator {
      position: absolute;
      bottom: 1.2rem;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.5rem;
      cursor: pointer;
      z-index: 25;
      pointer-events: auto;
      transition: opacity 0.3s ease;
    }

    .scroll-mouse-icon {
      width: 22px;
      height: 36px;
      border-radius: 9999px;
      border: 2px solid rgba(255, 255, 255, 0.35);
      position: relative;
      display: flex;
      justify-content: center;
    }

    .scroll-mouse-wheel {
      width: 3px;
      height: 7px;
      background: var(--brand-cyan);
      border-radius: 2px;
      margin-top: 6px;
      box-shadow: 0 0 8px var(--brand-cyan);
      animation: wheelBounce 2s cubic-bezier(0.65, 0, 0.35, 1) infinite;
    }

    @keyframes wheelBounce {
      0% { transform: translateY(0); opacity: 1; }
      100% { transform: translateY(12px); opacity: 0; }
    }

    .scroll-hud-text {
      font-family: var(--font-mono);
      font-size: 0.65rem;
      font-weight: 600;
      letter-spacing: 0.22em;
      color: #94a3b8;
      text-transform: uppercase;
    }

    .scroll-arrow-bounce {
      color: var(--brand-cyan);
      font-size: 0.9rem;
      animation: arrowBounce 1.8s ease-in-out infinite;
    }

    @keyframes arrowBounce {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(5px); }
    }

    /* Cosmic Warp Fullscreen Transition Flash */
    #cosmicWarpFlash {
      position: fixed;
      inset: 0;
      background: radial-gradient(circle at 65% 50%, rgba(168, 85, 247, 0.98) 0%, rgba(6, 182, 212, 0.9) 40%, rgba(1, 2, 6, 1) 100%);
      opacity: 0;
      pointer-events: none;
      z-index: 9999;
      transition: opacity 0.35s ease;
    }

    /* =========================================================
       SUBSEQUENT SECTIONS STYLING (PRESERVED CONTENT)
       ========================================================= */
    .section {
      position: relative;
      padding: 7rem 4%;
      z-index: 10;
      background: transparent;
    }

    .section-divider {
      height: 1px;
      width: 100%;
      max-width: 1280px;
      margin: 0 auto 5rem;
      background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.12), transparent);
    }

    .container {
      width: 100%;
      max-width: 1280px;
      margin: 0 auto;
    }

    .section-head {
      margin-bottom: 4rem;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      gap: 2rem;
      flex-wrap: wrap;
    }

    .kicker {
      font-family: var(--font-mono);
      font-size: 0.78rem;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: var(--brand-cyan);
      margin-bottom: 0.75rem;
    }

    .section-head h2 {
      font-family: var(--font-display);
      font-size: clamp(2.4rem, 4.2vw, 3.8rem);
      font-weight: 700;
      line-height: 1.08;
      letter-spacing: -0.03em;
      color: #ffffff;
    }

    .grad-accent {
      background: linear-gradient(135deg, #a855f7 0%, #06b6d4 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .section-intro-text {
      max-width: 520px;
      font-size: 1.05rem;
      color: var(--text-secondary);
      line-height: 1.7;
    }

    /* Products 2x2 Grid */
    .products-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 2.5rem;
    }

    .world-card {
      background: rgba(8, 12, 28, 0.65);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 28px;
      padding: 2.8rem;
      position: relative;
      overflow: hidden;
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1),
                  border-color 0.4s ease,
                  box-shadow 0.4s ease,
                  background 0.4s ease;
    }

    .world-card:hover {
      transform: translateY(-8px);
      background: rgba(12, 18, 40, 0.75);
    }

    .card-watermark {
      position: absolute;
      top: -10%;
      right: -8%;
      width: 280px;
      height: 280px;
      object-fit: contain;
      pointer-events: none;
      opacity: 0.04;
      filter: blur(1px);
      transition: opacity 0.4s ease, transform 0.4s ease;
      z-index: 0;
      mix-blend-mode: screen;
    }

    .world-card:hover .card-watermark {
      opacity: 0.09;
      transform: scale(1.06) rotate(4deg);
    }

    .world-card.card-checkra:hover {
      border-color: rgba(139, 92, 246, 0.6);
      box-shadow: 0 28px 65px -15px rgba(0, 0, 0, 0.85), 0 0 45px rgba(139, 92, 246, 0.3);
    }
    .world-card.card-homora:hover {
      border-color: rgba(6, 182, 212, 0.6);
      box-shadow: 0 28px 65px -15px rgba(0, 0, 0, 0.85), 0 0 45px rgba(6, 182, 212, 0.3);
    }
    .world-card.card-bubora:hover {
      border-color: rgba(236, 72, 153, 0.6);
      box-shadow: 0 28px 65px -15px rgba(0, 0, 0, 0.85), 0 0 45px rgba(236, 72, 153, 0.3);
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

    .card-checkra .world-art-wrap img {
      max-height: 130px;
      max-width: 85%;
      object-fit: contain;
      filter: drop-shadow(0 0 25px rgba(139, 92, 246, 0.6));
    }
    .card-homora .world-art-wrap img {
      mix-blend-mode: screen;
      filter: drop-shadow(0 0 25px rgba(6, 182, 212, 0.6));
    }

    .world-card:hover .world-art-wrap img {
      transform: scale(1.05);
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
      color: #ffffff;
      letter-spacing: -0.02em;
    }

    .formerly-tag {
      font-family: var(--font-mono);
      font-size: 0.72rem;
      font-weight: 500;
      color: #94a3b8;
      margin-left: 0.5rem;
    }

    .status-badge {
      font-family: var(--font-mono);
      font-size: 0.68rem;
      font-weight: 600;
      padding: 0.28rem 0.75rem;
      border-radius: 9999px;
      letter-spacing: 0.1em;
      text-transform: uppercase;
    }

    .badge-live {
      background: rgba(16, 185, 129, 0.12);
      border: 1px solid rgba(16, 185, 129, 0.35);
      color: #34d399;
      box-shadow: 0 0 15px rgba(16, 185, 129, 0.2);
    }

    .badge-proto {
      background: rgba(6, 182, 212, 0.12);
      border: 1px solid rgba(6, 182, 212, 0.35);
      color: #38bdf8;
      box-shadow: 0 0 15px rgba(6, 182, 212, 0.2);
    }

    .badge-dev {
      background: rgba(236, 72, 153, 0.12);
      border: 1px solid rgba(236, 72, 153, 0.35);
      color: #f472b6;
      box-shadow: 0 0 15px rgba(236, 72, 153, 0.2);
    }

    .badge-concept {
      background: rgba(139, 92, 246, 0.12);
      border: 1px solid rgba(139, 92, 246, 0.35);
      color: #c084fc;
      box-shadow: 0 0 15px rgba(139, 92, 246, 0.2);
    }

    .world-tagline {
      font-size: 1.05rem;
      font-weight: 500;
      color: var(--brand-cyan);
      margin-bottom: 1.1rem;
      position: relative;
      z-index: 1;
    }

    .world-desc {
      font-size: 0.96rem;
      line-height: 1.7;
      color: var(--text-secondary);
      margin-bottom: 1.8rem;
      position: relative;
      z-index: 1;
    }

    .capabilities-list {
      list-style: none;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.75rem 1rem;
      margin-bottom: 2.2rem;
      position: relative;
      z-index: 1;
    }

    .capabilities-list li {
      font-size: 0.85rem;
      color: var(--text-secondary);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .capabilities-list li::before {
      content: '◆';
      font-size: 0.5rem;
      color: var(--brand-cyan);
    }

    .world-actions {
      display: flex;
      align-items: center;
      gap: 1rem;
      position: relative;
      z-index: 1;
    }

    .btn-concept {
      padding: 0.7rem 1.4rem;
      border-radius: 9999px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.14);
      color: #ffffff;
      font-size: 0.88rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.25s ease;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
    }

    .btn-concept:hover {
      background: rgba(255, 255, 255, 0.12);
      border-color: rgba(255, 255, 255, 0.3);
      transform: translateY(-2px);
    }

    .world-link {
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--brand-cyan);
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      transition: gap 0.2s ease, color 0.2s ease;
    }

    .world-link:hover {
      color: #ffffff;
      gap: 0.55rem;
    }

    /* Lifecycle & Philosophy Section */
    .lifecycle-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 2rem;
    }

    .stage-card {
      background: rgba(8, 12, 28, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 22px;
      padding: 2.2rem;
      position: relative;
      backdrop-filter: blur(18px);
      -webkit-backdrop-filter: blur(18px);
      transition: all 0.3s ease;
    }

    .stage-card:hover {
      border-color: rgba(139, 92, 246, 0.4);
      transform: translateY(-5px);
      box-shadow: 0 15px 35px -10px rgba(0, 0, 0, 0.7), 0 0 25px rgba(139, 92, 246, 0.15);
    }

    .stage-number {
      font-family: var(--font-mono);
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--brand-cyan);
      margin-bottom: 1rem;
    }

    .stage-card h3 {
      font-family: var(--font-display);
      font-size: 1.45rem;
      font-weight: 700;
      margin-bottom: 0.75rem;
      color: #ffffff;
    }

    .stage-card p {
      font-size: 0.92rem;
      line-height: 1.65;
      color: var(--text-secondary);
    }

    /* Founder / Architect Section */
    .founder-card {
      display: grid;
      grid-template-columns: 0.85fr 1.15fr;
      gap: 4rem;
      align-items: center;
      background: rgba(8, 12, 28, 0.65);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 32px;
      padding: 4rem;
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
    }

    .founder-image-wrap {
      width: 100%;
      border-radius: 24px;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.12);
      box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.9), 0 0 45px rgba(139, 92, 246, 0.2);
    }

    .founder-image-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.5s ease;
    }

    .founder-card:hover .founder-image-wrap img {
      transform: scale(1.03);
    }

    .founder-info h3 {
      font-family: var(--font-display);
      font-size: 2.4rem;
      font-weight: 700;
      margin-bottom: 0.5rem;
      color: #ffffff;
    }

    .founder-title {
      font-size: 1.05rem;
      color: var(--brand-cyan);
      font-weight: 500;
      margin-bottom: 1.8rem;
    }

    .founder-bio {
      font-size: 1.02rem;
      line-height: 1.75;
      color: var(--text-secondary);
      margin-bottom: 2.2rem;
    }

    .founder-links {
      display: flex;
      align-items: center;
      gap: 1.5rem;
    }

    .founder-links a {
      font-size: 0.92rem;
      font-weight: 600;
      color: #ffffff;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.65rem 1.4rem;
      border-radius: 9999px;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
      transition: all 0.25s ease;
    }

    .founder-links a:hover {
      background: rgba(255, 255, 255, 0.15);
      border-color: rgba(255, 255, 255, 0.3);
      transform: translateY(-2px);
    }

    /* Ecosystem Constellation Section */
    .constellation-wrap {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.8rem;
    }

    .constellation-node {
      background: rgba(8, 12, 28, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 20px;
      padding: 2.2rem 1.8rem;
      text-align: center;
      backdrop-filter: blur(18px);
      -webkit-backdrop-filter: blur(18px);
      transition: all 0.3s ease;
    }

    .constellation-node:hover {
      transform: translateY(-6px);
    }

    .node-checkra:hover { border-color: var(--color-checkra); box-shadow: 0 15px 35px -10px rgba(0,0,0,0.8), 0 0 30px var(--glow-checkra); }
    .node-homora:hover { border-color: var(--color-homora); box-shadow: 0 15px 35px -10px rgba(0,0,0,0.8), 0 0 30px var(--glow-homora); }
    .node-bubora:hover { border-color: var(--color-bubora); box-shadow: 0 15px 35px -10px rgba(0,0,0,0.8), 0 0 30px var(--glow-bubora); }
    .node-sayora:hover { border-color: var(--color-sayora); box-shadow: 0 15px 35px -10px rgba(0,0,0,0.8), 0 0 30px var(--glow-sayora); }

    .node-theme-tag {
      font-family: var(--font-mono);
      font-size: 0.68rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      margin-bottom: 0.85rem;
    }

    .constellation-node h4 {
      font-family: var(--font-display);
      font-size: 1.4rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 0.5rem;
    }

    .constellation-node p {
      font-size: 0.86rem;
      color: var(--text-secondary);
      line-height: 1.55;
    }

    /* FOLIVIO Section */
    .folivio-banner {
      background: linear-gradient(135deg, rgba(20, 16, 42, 0.75) 0%, rgba(12, 10, 26, 0.85) 100%);
      border: 1px solid rgba(139, 92, 246, 0.25);
      border-radius: 32px;
      padding: 3.8rem;
      display: grid;
      grid-template-columns: 1.2fr 0.8fr;
      gap: 3rem;
      align-items: center;
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
    }

    .folivio-info h3 {
      font-family: var(--font-display);
      font-size: 2.2rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 1rem;
    }

    .folivio-info p {
      font-size: 1.02rem;
      color: var(--text-secondary);
      line-height: 1.7;
      margin-bottom: 2rem;
    }

    .folivio-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.8rem 1.8rem;
      background: linear-gradient(135deg, #a855f7 0%, #ec4899 100%);
      color: #ffffff;
      font-weight: 600;
      border-radius: 9999px;
      box-shadow: 0 10px 25px -5px rgba(168, 85, 247, 0.5);
      transition: all 0.3s ease;
    }

    .folivio-btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 15px 30px -5px rgba(168, 85, 247, 0.7);
    }

    .folivio-logo-box {
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .folivio-logo-box img {
      max-width: 220px;
      filter: drop-shadow(0 0 30px rgba(168, 85, 247, 0.4));
    }

    /* Contact Section */
    .contact-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 4rem;
      align-items: flex-start;
    }

    .contact-info h3 {
      font-family: var(--font-display);
      font-size: 2.2rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 1rem;
    }

    .contact-info p {
      font-size: 1.05rem;
      color: var(--text-secondary);
      line-height: 1.7;
      margin-bottom: 2.5rem;
    }

    .contact-channels {
      display: flex;
      flex-direction: column;
      gap: 1.2rem;
    }

    .channel-item {
      display: flex;
      align-items: center;
      gap: 1rem;
      color: var(--text-secondary);
      font-size: 0.96rem;
    }

    .channel-icon {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.1);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--brand-cyan);
    }

    .contact-form {
      background: rgba(8, 12, 28, 0.65);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 28px;
      padding: 3rem;
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
    }

    .form-group {
      margin-bottom: 1.6rem;
    }

    .form-group label {
      display: block;
      font-size: 0.85rem;
      font-weight: 600;
      color: #94a3b8;
      margin-bottom: 0.5rem;
    }

    .form-group input,
    .form-group textarea {
      width: 100%;
      padding: 0.85rem 1.2rem;
      background: rgba(4, 6, 16, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 14px;
      color: #ffffff;
      font-family: inherit;
      font-size: 0.95rem;
      transition: all 0.25s ease;
      outline: none;
    }

    .form-group input:focus,
    .form-group textarea:focus {
      border-color: var(--brand-cyan);
      box-shadow: 0 0 20px rgba(6, 182, 212, 0.25);
    }

    .form-submit-btn {
      width: 100%;
      padding: 1rem;
      background: linear-gradient(135deg, #a855f7 0%, #3b82f6 50%, #06b6d4 100%);
      color: #ffffff;
      font-weight: 600;
      font-size: 1rem;
      border-radius: 14px;
      border: 1px solid rgba(255, 255, 255, 0.2);
      cursor: pointer;
      box-shadow: 0 10px 25px -5px rgba(139, 92, 246, 0.5);
      transition: all 0.3s ease;
    }

    .form-submit-btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 15px 35px -5px rgba(139, 92, 246, 0.7);
    }

    /* Footer */
    footer {
      position: relative;
      padding: 4rem 4% 3rem;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      z-index: 10;
      background: rgba(1, 2, 6, 0.8);
      backdrop-filter: blur(20px);
    }

    .footer-content {
      max-width: 1280px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 2rem;
    }

    .footer-copy {
      font-size: 0.86rem;
      color: var(--text-muted);
    }

    .footer-links {
      display: flex;
      align-items: center;
      gap: 2rem;
      list-style: none;
    }

    .footer-links a {
      font-size: 0.86rem;
      color: var(--text-secondary);
      transition: color 0.2s ease;
    }

    .footer-links a:hover {
      color: #ffffff;
    }

    /* =========================================================
       CONCEPT MODAL POPUP SYSTEM (FULL PRESERVED)
       ========================================================= */
    #conceptModalOverlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 1, 4, 0.88);
      backdrop-filter: blur(32px) saturate(180%);
      -webkit-backdrop-filter: blur(32px) saturate(180%);
      z-index: 1000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 2.5rem 1.5rem;
      opacity: 0;
      transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    #conceptModalOverlay.open {
      display: flex;
      opacity: 1;
    }

    .modal-container {
      width: 100%;
      max-width: 960px;
      max-height: 88vh;
      background: rgba(8, 12, 28, 0.88);
      border: 1px solid rgba(255, 255, 255, 0.14);
      border-radius: 32px;
      box-shadow: 0 35px 80px -20px rgba(0, 0, 0, 0.9), 0 0 60px rgba(139, 92, 246, 0.25);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      position: relative;
      animation: modalSlideUp 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @keyframes modalSlideUp {
      from { transform: translateY(30px) scale(0.97); opacity: 0; }
      to { transform: translateY(0) scale(1); opacity: 1; }
    }

    .modal-top-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 1.25rem 2rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      background: rgba(12, 16, 36, 0.6);
      flex-shrink: 0;
      gap: 1rem;
    }

    .modal-top-left {
      display: flex;
      align-items: center;
      gap: 1.25rem;
    }

    .btn-return-modal {
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      padding: 0.45rem 1rem;
      border-radius: 9999px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #ffffff;
      font-size: 0.82rem;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .btn-return-modal:hover {
      background: rgba(255, 255, 255, 0.12);
    }

    .modal-brand-subtle {
      display: flex;
      align-items: center;
      gap: 0.45rem;
      font-family: var(--font-display);
      font-weight: 700;
      font-size: 1.05rem;
      letter-spacing: 0.05em;
    }

    .mbs-nivora { color: #94a3b8; }
    .mbs-product-name { color: #ffffff; }

    .mbs-status-badge {
      font-family: var(--font-mono);
      font-size: 0.64rem;
      font-weight: 600;
      padding: 0.2rem 0.6rem;
      border-radius: 9999px;
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.35);
      color: #34d399;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }

    .modal-nav-tabs {
      display: flex;
      align-items: center;
      gap: 0.35rem;
    }

    .modal-nav-tab {
      padding: 0.4rem 0.9rem;
      border-radius: 9999px;
      background: transparent;
      border: none;
      color: var(--text-secondary);
      font-size: 0.82rem;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .modal-nav-tab:hover {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.06);
    }

    .modal-nav-tab.active {
      color: #ffffff;
      background: rgba(139, 92, 246, 0.25);
      border: 1px solid rgba(139, 92, 246, 0.45);
    }

    .modal-top-right {
      display: flex;
      align-items: center;
      gap: 0.85rem;
    }

    .modal-launch-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      padding: 0.48rem 1.15rem;
      border-radius: 9999px;
      background: linear-gradient(135deg, #a855f7, #3b82f6);
      color: #ffffff;
      font-size: 0.82rem;
      font-weight: 600;
      border: 1px solid rgba(255, 255, 255, 0.2);
      box-shadow: 0 6px 18px rgba(139, 92, 246, 0.4);
      transition: all 0.25s ease;
    }

    .modal-launch-btn:hover {
      transform: translateY(-1px);
      box-shadow: 0 10px 24px rgba(139, 92, 246, 0.6);
    }

    .modal-close-x {
      width: 34px;
      height: 34px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #94a3b8;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .modal-close-x:hover {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.15);
    }

    .modal-scrollable-body {
      padding: 3rem 3rem 4rem;
      overflow-y: auto;
      scroll-behavior: smooth;
    }

    .modal-product-view {
      display: none;
      animation: modalFadeIn 0.3s ease;
    }

    .modal-product-view.active {
      display: block;
    }

    @keyframes modalFadeIn {
      from { opacity: 0; transform: translateY(12px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .modal-hero-sec { margin-bottom: 3.5rem; }

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
      padding: 8px;
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
      color: var(--brand-cyan);
      margin-bottom: 0.75rem;
    }

    .modal-hero-sec h2 {
      font-family: var(--font-display);
      font-size: clamp(2.2rem, 3.8vw, 3.2rem);
      font-weight: 700;
      letter-spacing: -0.03em;
      color: #ffffff;
      line-height: 1.15;
    }

    .modal-lead-box {
      margin-top: 1.5rem;
      padding: 1.8rem;
      border-radius: 20px;
      background: rgba(255, 255, 255, 0.03);
      border-left: 3px solid var(--brand-cyan);
      font-size: 1.05rem;
      line-height: 1.75;
      color: #e2e8f0;
    }

    .modal-section-title {
      font-family: var(--font-display);
      font-size: 1.6rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 1.8rem;
    }

    .modal-caps-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1.5rem;
      margin-bottom: 3.5rem;
    }

    .modal-cap-card {
      padding: 1.8rem;
      border-radius: 20px;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
      transition: all 0.25s ease;
    }

    .modal-cap-card:hover {
      background: rgba(255, 255, 255, 0.06);
      border-color: rgba(255, 255, 255, 0.18);
      transform: translateY(-3px);
    }

    .modal-cap-icon {
      width: 42px;
      height: 42px;
      border-radius: 12px;
      background: rgba(139, 92, 246, 0.15);
      border: 1px solid rgba(139, 92, 246, 0.35);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--brand-cyan);
      margin-bottom: 1.1rem;
    }

    .modal-cap-card h4 {
      font-family: var(--font-display);
      font-size: 1.18rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 0.5rem;
    }

    .modal-cap-card p {
      font-size: 0.9rem;
      line-height: 1.6;
      color: var(--text-secondary);
    }

    .modal-flow-box {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.2rem;
      margin-bottom: 3.5rem;
    }

    .flow-step-box {
      padding: 1.5rem;
      border-radius: 18px;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
    }

    .flow-num {
      font-family: var(--font-mono);
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--brand-cyan);
      margin-bottom: 0.6rem;
    }

    .flow-step-box h5 {
      font-family: var(--font-display);
      font-size: 1.05rem;
      font-weight: 600;
      color: #ffffff;
      margin-bottom: 0.4rem;
    }

    .flow-step-box p {
      font-size: 0.84rem;
      line-height: 1.5;
      color: var(--text-secondary);
    }

    .modal-arch-box {
      padding: 2.2rem;
      border-radius: 22px;
      background: rgba(4, 6, 16, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.1);
      margin-bottom: 3.5rem;
    }

    .arch-specs-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.5rem;
      margin-top: 1.5rem;
    }

    .arch-spec-item {
      padding: 1.2rem;
      background: rgba(255, 255, 255, 0.02);
      border-radius: 14px;
      border: 1px solid rgba(255, 255, 255, 0.06);
    }

    .arch-spec-item strong {
      display: block;
      font-family: var(--font-mono);
      font-size: 0.74rem;
      color: var(--brand-cyan);
      margin-bottom: 0.4rem;
      text-transform: uppercase;
    }

    .arch-spec-item span {
      font-size: 0.92rem;
      color: #ffffff;
      font-weight: 500;
    }

    .modal-vision-box {
      padding: 2.5rem;
      border-radius: 24px;
      background: linear-gradient(135deg, rgba(20, 16, 42, 0.7) 0%, rgba(10, 14, 30, 0.85) 100%);
      border: 1px solid rgba(139, 92, 246, 0.3);
      position: relative;
    }

    .modal-vision-box h4 {
      font-family: var(--font-display);
      font-size: 1.4rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 0.75rem;
    }

    .modal-vision-box p {
      font-size: 1rem;
      line-height: 1.7;
      color: var(--text-secondary);
      margin-bottom: 1.5rem;
    }

    /* Responsive */
    @media (max-width: 1024px) {
      .hero-container {
        grid-template-columns: 1fr;
        gap: 2rem;
        padding-top: 2rem;
      }
      .hero-content {
        max-width: 100%;
        text-align: center;
      }
      .hero-copy {
        margin-left: auto;
        margin-right: auto;
      }
      .hero-actions {
        justify-content: center;
      }
      .hero-metrics {
        justify-content: center;
      }
      .hero-art-stage {
        height: 480px;
      }
      .products-grid {
        grid-template-columns: 1fr;
      }
      .lifecycle-grid,
      .constellation-wrap {
        grid-template-columns: repeat(2, 1fr);
      }
      .founder-card,
      .folivio-banner,
      .contact-grid {
        grid-template-columns: 1fr;
        gap: 2.5rem;
      }
      .modal-caps-grid {
        grid-template-columns: 1fr;
      }
      .modal-flow-box {
        grid-template-columns: repeat(2, 1fr);
      }
      .arch-specs-grid {
        grid-template-columns: 1fr;
      }
    }

    @media (max-width: 768px) {
      .nav-links, .nav-status-pill {
        display: none;
      }
      .hero-metrics {
        flex-direction: column;
        gap: 1.25rem;
        align-items: center;
      }
      .lifecycle-grid,
      .constellation-wrap {
        grid-template-columns: 1fr;
      }
      .modal-top-bar {
        flex-direction: column;
        align-items: stretch;
      }
      .modal-nav-tabs {
        overflow-x: auto;
        padding-bottom: 0.5rem;
      }
      .modal-scrollable-body {
        padding: 1.5rem;
      }
    }
  </style>
</head>

<body>
  <!-- FIXED FULL-SCREEN 3D UNIVERSE CANVAS -->
  <canvas id="webglUniverseCanvas"></canvas>

  <!-- AMBIENT COSMIC BACKGROUND LAYER (BEHIND WEBGL) -->
  <div class="cosmic-ambient-backdrop">
    <div class="cosmic-nebula-topleft"></div>
    <div class="cosmic-nebula-rightcore"></div>
    <div class="cosmic-nebula-bottommid"></div>
  </div>

  <!-- FULLSCREEN COSMIC WARP FLASH -->
  <div id="cosmicWarpFlash"></div>

  <!-- =========================================================
       LUXURY FLOATING GLASS CAPSULE NAVIGATION
       ========================================================= -->
  <header class="top-nav">
    <nav class="nav-capsule" aria-label="NIVORA Universe Navigation">
      <a href="#hero" class="nav-brand">
        <img src="assets/images/nivora-logo.png" alt="NIVORA Logo" class="nav-logo-icon">
        <div class="nav-brand-text">
          <span class="brand-title">NIVORA</span>
          <span class="brand-subtitle">DIGITAL UNIVERSE</span>
        </div>
      </a>

      <ul class="nav-links">
        <li><a href="#hero" class="nav-link active">Home</a></li>
        <li><a href="#products" class="nav-link">Products</a></li>
        <li><a href="#about" class="nav-link">About</a></li>
        <li><a href="#portfolio" class="nav-link">Portfolio</a></li>
        <li><a href="#vision" class="nav-link">Vision</a></li>
        <li><a href="#folivio" class="nav-link">FOLIVIO</a></li>
        <li><a href="#contact" class="nav-link">Contact</a></li>
      </ul>

      <div class="nav-right-actions">
        <div class="nav-status-pill">
          <span class="status-dot-pulse"></span>
          <span>STATUS: ONLINE</span>
        </div>
        <button type="button" class="nav-cta-btn" onclick="triggerCinematicCameraZoom()">
          <span>Explore Universe &rarr;</span>
        </button>
      </div>
    </nav>
  </header>

  <!-- =========================================================
       HERO SECTION — THE 3D UNIVERSE IS THE HERO
       ========================================================= -->
  <main>
    <section class="hero" id="hero">
      <div class="hero-container">
        <!-- LEFT HERO CONTENT: BRANDING, TYPOGRAPHY, CTAS -->
        <div class="hero-content">
          <div class="hero-badge">
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
            <div class="kicker">// 01 &middot; The Product Constellation</div>
            <h2>Products with<br><span class="grad-accent">a Purpose.</span></h2>
          </div>
          <p class="section-intro-text">
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

            <ul class="capabilities-list">
              <li>Similarity &amp; Plagiarism Detection</li>
              <li>Source URL &amp; Citation Indexing</li>
              <li>Multi-Format Document Parsing</li>
              <li>Contextual Integrity Feedback</li>
            </ul>

            <div class="world-actions">
              <button type="button" class="btn-concept" onclick="openConceptModal('checkra')">
                <span>Explore Concept</span>
                <span class="btn-arrow">&rarr;</span>
              </button>
              <a class="world-link" href="https://checkra-xi.vercel.app/" target="_blank" rel="noopener noreferrer">
                <span>Launch App</span>
                <span class="btn-arrow">&nearr;</span>
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
              <span class="status-badge badge-proto">Active Prototype</span>
            </div>

            <div class="world-tagline">
              Smart Living &amp; <em class="editorial-accent">Shared Finance</em>
            </div>

            <p class="world-desc">
              AI-powered financial harmony platform for shared households, roommates, and co-living spaces &mdash; coordinating contributions, recurring expenses, and agreements without friction.
            </p>

            <ul class="capabilities-list">
              <li>Fair Bill &amp; Chore Splitting</li>
              <li>Voice-Enabled Expense Capture</li>
              <li>Smart Group Spending Insights</li>
              <li>Household Agreement Vault</li>
            </ul>

            <div class="world-actions">
              <button type="button" class="btn-concept" onclick="openConceptModal('homora')">
                <span>Explore Concept</span>
                <span class="btn-arrow">&rarr;</span>
              </button>
              <a class="world-link" href="https://homora.vercel.app" target="_blank" rel="noopener noreferrer">
                <span>Explore Prototype</span>
                <span class="btn-arrow">&nearr;</span>
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
              <span class="status-badge badge-dev">In Development</span>
            </div>

            <div class="world-tagline">
              Intimate Digital Sanctuary <em class="editorial-accent">for Two</em>
            </div>

            <p class="world-desc">
              A private digital haven engineered exclusively for two &mdash; uniting shared messaging, memory vaults, collaborative bucket lists, and relationship milestones away from public feeds.
            </p>

            <ul class="capabilities-list">
              <li>End-to-End Encrypted Intimacy</li>
              <li>Shared Milestone Calendar</li>
              <li>Curated Memory &amp; Photo Vault</li>
              <li>Ambient Presence &amp; Haptics</li>
            </ul>

            <div class="world-actions">
              <button type="button" class="btn-concept" onclick="openConceptModal('bubora')">
                <span>Explore Concept</span>
                <span class="btn-arrow">&rarr;</span>
              </button>
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
              <span class="status-badge badge-concept">Conceptual Stage</span>
            </div>

            <div class="world-tagline">
              Social Impact &amp; <em class="editorial-accent">Financial Shield</em>
            </div>

            <p class="world-desc">
              Fintech initiative architected to shield informal laborers, gig delivery workers, and daily wage earners against sudden income shocks, health emergencies, and climate disruptions.
            </p>

            <ul class="capabilities-list">
              <li>Micro-Income Stabilization</li>
              <li>Community Mutual-Aid Pools</li>
              <li>Weather-Indexed Disruption Cover</li>
              <li>Vernacular Audio-First Interface</li>
            </ul>

            <div class="world-actions">
              <button type="button" class="btn-concept" onclick="openConceptModal('sayora')">
                <span>Explore Concept</span>
                <span class="btn-arrow">&rarr;</span>
              </button>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- =========================================================
       SECTION 02: ABOUT & LIFECYCLE (#about)
       ========================================================= -->
    <section class="section" id="about">
      <div class="section-divider"></div>
      <div class="container">
        <div class="section-head">
          <div>
            <div class="kicker">// 02 &middot; Product Lifecycle &amp; Philosophy</div>
            <h2>Ideas to Products.<br><span class="grad-accent">The 4-Stage Arc.</span></h2>
          </div>
          <p class="section-intro-text">
            NIVORA operates on a disciplined lifecycle. No product ships as a half-conceived experiment &mdash; each transitions deliberately from philosophical insight into production reality.
          </p>
        </div>

        <div class="lifecycle-grid">
          <div class="stage-card">
            <div class="stage-number">PHASE // 01</div>
            <h3>Philosophy</h3>
            <p>Identifying deep systemic frictions in human workflow, shared living, communication, and economic security before writing code.</p>
          </div>
          <div class="stage-card">
            <div class="stage-number">PHASE // 02</div>
            <h3>Architecture</h3>
            <p>Designing modern, scalable technical foundations: resilient cloud backends, secure client apps, and targeted AI model integrations.</p>
          </div>
          <div class="stage-card">
            <div class="stage-number">PHASE // 03</div>
            <h3>Experience</h3>
            <p>Refining every micro-interaction, typography scale, motion curve, and cognitive load until the interface feels instinctive and calm.</p>
          </div>
          <div class="stage-card">
            <div class="stage-number">PHASE // 04</div>
            <h3>Production</h3>
            <p>Deploying resilient, monitored cloud systems delivering dependable utility, real data privacy, and measurable daily impact.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- =========================================================
       SECTION 03: ARCHITECT & FOUNDER (#portfolio)
       ========================================================= -->
    <section class="section" id="portfolio">
      <div class="section-divider"></div>
      <div class="container">
        <div class="founder-card">
          <div class="founder-image-wrap">
            <img src="assets/images/founder-nivas.png" alt="Nivas Bennabatthula — Founder &amp; Architect of NIVORA">
          </div>
          <div class="founder-info">
            <div class="kicker">// THE ARCHITECT</div>
            <h3>Nivas Bennabatthula</h3>
            <div class="founder-title">Founder, Product Architect &amp; Full-Stack Builder</div>
            <p class="founder-bio">
              Driven by the conviction that modern technology should elevate human dignity, Nivas conceives, architects, and builds every product within the NIVORA universe. Balancing rigorous engineering with empathetic user research, he turns complex distributed systems and modern AI into calm, reliable products.
            </p>
            <div class="founder-links">
              <a href="https://nivas-portfolio.vercel.app/" target="_blank" rel="noopener noreferrer">
                <span>Personal Portfolio</span>
                <span class="btn-arrow">&nearr;</span>
              </a>
              <a href="https://www.linkedin.com/in/bennabathulanivas/" target="_blank" rel="noopener noreferrer">
                <span>LinkedIn</span>
                <span class="btn-arrow">&nearr;</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =========================================================
       SECTION 04: ECOSYSTEM UNIVERSE (#vision)
       ========================================================= -->
    <section class="section" id="vision">
      <div class="section-divider"></div>
      <div class="container">
        <div class="section-head">
          <div>
            <div class="kicker">// 04 &middot; Ecosystem Constellation</div>
            <h2>One Connected Vision.<br><span class="grad-accent">Distinct Digital Realms.</span></h2>
          </div>
          <p class="section-intro-text">
            While each product addresses a dedicated domain, all four share NIVORA's foundational standards: clean privacy architecture, human-centric design, and intelligent AI assistance.
          </p>
        </div>

        <div class="constellation-wrap">
          <div class="constellation-node node-checkra">
            <div class="node-theme-tag" style="color: var(--color-checkra);">Integrity Realm</div>
            <h4>CHECKRA</h4>
            <p>Verification Intelligence for writers, educators, and scholars.</p>
          </div>

          <div class="constellation-node node-homora">
            <div class="node-theme-tag" style="color: var(--color-homora);">Domestic Harmony</div>
            <h4>HOMORA</h4>
            <p>Smart living &amp; shared financial OS for co-living households.</p>
          </div>

          <div class="constellation-node node-bubora">
            <div class="node-theme-tag" style="color: var(--color-bubora);">Intimate Sanctuary</div>
            <h4>BUBORA</h4>
            <p>Private digital haven engineered exclusively for two.</p>
          </div>

          <div class="constellation-node node-sayora">
            <div class="node-theme-tag" style="color: var(--color-sayora);">Social Resilience</div>
            <h4>SAYORA</h4>
            <p>Financial shield &amp; micro-safety nets for vulnerable workers.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- =========================================================
       SECTION 05: FOLIVIO PARTNERSHIP (#folivio)
       ========================================================= -->
    <section class="section" id="folivio">
      <div class="section-divider"></div>
      <div class="container">
        <div class="folivio-banner">
          <div class="folivio-info">
            <div class="kicker">// DESIGN ALLIANCE</div>
            <h3>FOLIVIO &times; NIVORA</h3>
            <p>
              FOLIVIO serves as the dedicated visual identity, brand strategy, and design engineering arm across the NIVORA ecosystem &mdash; ensuring each product balances cutting-edge AI architecture with world-class editorial aesthetic.
            </p>
            <a href="https://www.instagram.com/folivio.in/" target="_blank" rel="noopener noreferrer" class="folivio-btn">
              <span>Explore @folivio.in on Instagram</span>
              <span class="btn-arrow">&nearr;</span>
            </a>
          </div>
          <div class="folivio-logo-box">
            <img src="assets/images/folivio-logo.webp" alt="FOLIVIO Studio Logo">
          </div>
        </div>
      </div>
    </section>

    <!-- =========================================================
       SECTION 06: CONTACT & TRANSMISSION (#contact)
       ========================================================= -->
    <section class="section" id="contact">
      <div class="section-divider"></div>
      <div class="container">
        <div class="contact-grid">
          <div class="contact-info">
            <div class="kicker">// DIRECT DISPATCH</div>
            <h2>Let's Shape the<br><span class="grad-accent">Next Possibility.</span></h2>
            <p>
              Whether you are an ambitious engineer, potential collaborator, product partner, or investor &mdash; open a direct channel into the NIVORA universe.
            </p>
            <div class="contact-channels">
              <div class="channel-item">
                <div class="channel-icon">@</div>
                <div>
                  <strong>Primary Transmission</strong><br>
                  <span>nivasbennabathula@gmail.com</span>
                </div>
              </div>
              <div class="channel-item">
                <div class="channel-icon">&infin;</div>
                <div>
                  <strong>Headquarters</strong><br>
                  <span>NIVORA Innovation Lab &middot; India</span>
                </div>
              </div>
            </div>
          </div>

          <form class="contact-form" onsubmit="handleContactSubmit(event)">
            <div class="form-group">
              <label for="cName">Your Name / Organization</label>
              <input type="text" id="cName" required placeholder="e.g. Elena Rostova">
            </div>
            <div class="form-group">
              <label for="cEmail">Your Electronic Address</label>
              <input type="email" id="cEmail" required placeholder="name@domain.com">
            </div>
            <div class="form-group">
              <label for="cMsg">Transmission Intent / Message</label>
              <textarea id="cMsg" rows="4" required placeholder="Describe your inquiry, collaboration idea, or question..."></textarea>
            </div>
            <button type="submit" class="form-submit-btn" id="contactSubmitBtn">
              <span>Transmit Message &rarr;</span>
            </button>
            <div id="contactToast" style="display:none;margin-top:1rem;color:#34d399;font-size:0.9rem;text-align:center;"></div>
          </form>
        </div>
      </div>
    </section>
  </main>

  <!-- =========================================================
       GLOBAL FOOTER
       ========================================================= -->
  <footer>
    <div class="footer-content">
      <div class="footer-copy">
        &copy; <span id="currentYear">2026</span> NIVORA &middot; Built &amp; Architected by Nivas Bennabatthula. All rights reserved.
      </div>
      <ul class="footer-links">
        <li><a href="#hero">Home</a></li>
        <li><a href="#products">Products</a></li>
        <li><a href="#portfolio">Founder</a></li>
        <li><a href="https://checkra-xi.vercel.app/" target="_blank" rel="noopener noreferrer">CHECKRA</a></li>
        <li><a href="https://homora.vercel.app" target="_blank" rel="noopener noreferrer">HOMORA</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </div>
  </footer>

  <!-- =========================================================
       CONCEPT MODAL POPUP SYSTEM (FULL PRESERVED)
       ========================================================= -->
  <div id="conceptModalOverlay" role="dialog" aria-modal="true" aria-hidden="true" data-lenis-prevent>
    <div class="modal-container">
      <header class="modal-top-bar">
        <div class="modal-top-left">
          <button type="button" class="btn-return-modal" onclick="closeConceptModal()" aria-label="Return to NIVORA Universe (ESC)">
            <span>&larr; Return to Universe</span>
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
            &times;
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
                <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1 4-10z"></path></svg></div>
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
            <h3 class="modal-section-title">The Four-Step Verification Loop</h3>
            <div class="modal-flow-box">
              <div class="flow-step-box">
                <div class="flow-num">01 / UPLOAD</div>
                <h5>Document Ingestion</h5>
                <p>Drag-and-drop or paste raw text. The ingestion parser cleans markup and extracts tokens.</p>
              </div>
              <div class="flow-step-box">
                <div class="flow-num">02 / INDEX</div>
                <h5>Deep Web Indexing</h5>
                <p>Embeddings run against multi-source knowledge indices and academic publications.</p>
              </div>
              <div class="flow-step-box">
                <div class="flow-num">03 / SCORE</div>
                <h5>Integrity Scoring</h5>
                <p>Algorithmic calculation separates common boilerplate idioms from non-attributed passages.</p>
              </div>
              <div class="flow-step-box">
                <div class="flow-num">04 / ELEVATE</div>
                <h5>Citation Elevation</h5>
                <p>Exportable reports generate properly formatted references and authentic attribution paths.</p>
              </div>
            </div>
          </div>

          <div id="msec-checkra-architecture">
            <h3 class="modal-section-title">Technical Architecture</h3>
            <div class="modal-arch-box">
              <p style="color: var(--text-secondary); line-height: 1.7;">
                Engineered with a high-throughput microservices pipeline. Text extraction utilizes serverless edge workers, while similarity hashing leverages vector databases and locality-sensitive hashing (LSH).
              </p>
              <div class="arch-specs-grid">
                <div class="arch-spec-item">
                  <strong>Processing Engine</strong>
                  <span>Edge-Distributed Node &amp; WebAssembly</span>
                </div>
                <div class="arch-spec-item">
                  <strong>Vector Index</strong>
                  <span>High-Dimensional Embedding Index</span>
                </div>
                <div class="arch-spec-item">
                  <strong>Privacy Architecture</strong>
                  <span>Zero-Retention Workspace Guarantee</span>
                </div>
              </div>
            </div>
          </div>

          <div id="msec-checkra-vision">
            <div class="modal-vision-box">
              <h4>The Future of Human Attribution</h4>
              <p>
                In an era where synthetic AI content floods the open web, authentic human writing must be protected and provably verifiable. CHECKRA serves as the trusted standard for scholarly integrity.
              </p>
              <a href="https://checkra-xi.vercel.app/" target="_blank" rel="noopener noreferrer" class="modal-launch-btn">
                <span>Experience CHECKRA Live &nearr;</span>
              </a>
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
                <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="5" width="20" height="14" rx="2"></rect><line x1="2" y1="10" x2="22" y2="10"></line></svg></div>
                <h4>Fair Cost Allocation</h4>
                <p>Weight bills by income, room square footage, occupancy duration, or custom agreements.</p>
              </div>
              <div class="modal-cap-card">
                <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg></div>
                <h4>Voice-First Receipt Intake</h4>
                <p>Speak naturally: "Bought groceries for $62, split between Alex and me." Natural language parses it instantly.</p>
              </div>
              <div class="modal-cap-card">
                <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg></div>
                <h4>Chore Rotation &amp; Escrow</h4>
                <p>Equitable distribution of domestic chores with automated reminders and friendly nudge mechanics.</p>
              </div>
              <div class="modal-cap-card">
                <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg></div>
                <h4>Living Agreement Vault</h4>
                <p>Immutable digital home charter covering guests, quiet hours, and shared pantry rules.</p>
              </div>
            </div>
          </div>

          <div id="msec-homora-vision">
            <div class="modal-vision-box">
              <h4>Eliminating Domestic Friction</h4>
              <p>
                Shared living shouldn't strain human friendships. HOMORA replaces awkward payment reminders with automated, transparent, and fair household operations.
              </p>
              <a href="https://homora.vercel.app" target="_blank" rel="noopener noreferrer" class="modal-launch-btn">
                <span>Explore Prototype &nearr;</span>
              </a>
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
                <h4>Pair-Locked Encryption</h4>
                <p>Zero third-party tracking. Only you and your partner hold the asymmetric cryptographic keys.</p>
              </div>
              <div class="modal-cap-card">
                <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg></div>
                <h4>Shared Memory Timelines</h4>
                <p>High-resolution chronological photo and audio scrapbooks celebrating milestones and small days alike.</p>
              </div>
              <div class="modal-cap-card">
                <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></div>
                <h4>Dream &amp; Bucket Lists</h4>
                <p>Collaborative travel itineraries, movie lists, and aspirational goals with synchronized checkmarks.</p>
              </div>
              <div class="modal-cap-card">
                <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 14 14"></polyline></svg></div>
                <h4>Milestone Heartbeat</h4>
                <p>Intelligent countdowns for anniversaries, travels, and quiet moments that matter exclusively to you.</p>
              </div>
            </div>
          </div>

          <div id="msec-bubora-vision">
            <div class="modal-vision-box">
              <h4>Reclaiming Intimacy from the Feed</h4>
              <p>
                Human love shouldn't compete with viral algorithms or public social pressure. BUBORA offers an unpolluted digital room just for two souls.
              </p>
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
            <h3 class="modal-section-title">The Safety Net Architecture</h3>
            <div class="modal-caps-grid">
              <div class="modal-cap-card">
                <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>
                <h4>Micro-Income Shield</h4>
                <p>Automated micro-hedging against severe monsoons, extreme heatwaves, or local work stoppages.</p>
              </div>
              <div class="modal-cap-card">
                <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8"></path><line x1="12" y1="2" x2="12" y2="4"></line><line x1="12" y1="20" x2="12" y2="22"></line></svg></div>
                <h4>Community Mutual Pools</h4>
                <p>Decentralized peer-to-peer solidarity reserves providing instant zero-interest emergency relief.</p>
              </div>
              <div class="modal-cap-card">
                <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg></div>
                <h4>Parametric Health Triggers</h4>
                <p>Instant automatic payouts triggered directly by verified hospital admission records without bureaucracy.</p>
              </div>
              <div class="modal-cap-card">
                <div class="modal-cap-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg></div>
                <h4>Vernacular Audio-First UX</h4>
                <p>Multilingual voice prompts ensuring equal dignity and accessibility for non-literate gig workers.</p>
              </div>
            </div>
          </div>

          <div id="msec-sayora-vision">
            <div class="modal-vision-box">
              <h4>Dignity for the Invisible Backbone</h4>
              <p>
                The gig workforce drives modern global cities yet bears all existential risks alone. SAYORA builds a collective technological shield around every hardworking hand.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- =========================================================
       THREE.JS WEBGL + 3D PROJECTION UNIVERSE ENGINE
       ========================================================= -->
  <script>
    /* -------------------------------------------------------------
       1. GLOBAL STATE & LENIS SMOOTH SCROLLING
       ------------------------------------------------------------- */
    let lenis = null;
    try {
      if (typeof Lenis !== 'undefined') {
        lenis = new Lenis({
          duration: 1.2,
          easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
          smoothWheel: true,
          touchMultiplier: 1.5,
          infinite: false
        });
        function raf(time) {
          lenis.raf(time);
          requestAnimationFrame(raf);
        }
        requestAnimationFrame(raf);
      }
    } catch (err) {
      console.warn("Lenis init notice:", err);
    }

    // Dynamic Year
    document.getElementById('currentYear').innerText = new Date().getFullYear();

    /* -------------------------------------------------------------
       2. THREE.JS 3D UNIVERSE ENGINE (CLEAN, MINIMAL, PREMIUM)
       ------------------------------------------------------------- */
    const canvas = document.getElementById('webglUniverseCanvas');
    let renderer, scene, camera;
    let globeGroup, globeMesh, logoSprite, atmosphereMesh;
    let orbitalRings = [], ringParticles = [];
    let galaxyDisk, galaxyEnergyBeam;
    let starLayer1, starLayer2, starLayer3;
    let isWebGLEnabled = false;
    let isZoomingTransition = false;
    let warpSpeedFactor = 1.0;
    let mouse = { x: 0, y: 0, targetX: 0, targetY: 0 };
    let clock = new THREE.Clock();

    // Base Camera Coordinates (Globe on Right, UI on Left)
    const baseCamX = -30;
    const baseCamY = 2;
    const baseCamZ = 260;
    const globeCenterX = 66;
    const globeCenterY = 5;
    const globeCenterZ = 0;

    function initUniverse3D() {
      try {
        renderer = new THREE.WebGLRenderer({
          canvas: canvas,
          antialias: true,
          alpha: true,
          powerPreference: 'high-performance'
        });
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setClearColor(0x000000, 0); // 100% transparent clear
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 1.15;

        scene = new THREE.Scene();
        camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 2000);
        camera.position.set(baseCamX, baseCamY, baseCamZ);
        camera.lookAt(globeCenterX * 0.45, globeCenterY, 0);

        buildStarfieldsClean();
        buildNivoraGlobeClean();
        buildOrbitalRingsClean();
        buildGalaxyAccretionDiskClean();

        isWebGLEnabled = true;
        animateUniverseClean();
      } catch (e) {
        console.warn("WebGL notice, fallback active:", e);
        initCanvas3DFallbackClean();
      }
    }

    /* -------------------------------------------------------------
       3. STARFIELDS (CLEAN, SPARSE, 90% SOFT WHITE, ZERO CLUTTER)
       ------------------------------------------------------------- */
    function buildStarfieldsClean() {
      const starTex = createGlowPointTexture();

      // Layer 1: Background Stars (650 tiny, faint stars)
      const count1 = 650;
      const pos1 = new Float32Array(count1 * 3);
      const col1 = new Float32Array(count1 * 3);
      for (let i = 0; i < count1; i++) {
        pos1[i * 3] = (Math.random() - 0.5) * 1400;
        pos1[i * 3 + 1] = (Math.random() - 0.5) * 900;
        pos1[i * 3 + 2] = -350 - Math.random() * 400;

        // 90% soft white, 10% soft cosmic blue
        const shade = 0.5 + Math.random() * 0.35;
        col1[i * 3] = shade * 0.95;
        col1[i * 3 + 1] = shade * 0.98;
        col1[i * 3 + 2] = shade;
      }
      const geo1 = new THREE.BufferGeometry();
      geo1.setAttribute('position', new THREE.BufferAttribute(pos1, 3));
      geo1.setAttribute('color', new THREE.BufferAttribute(col1, 3));
      starLayer1 = new THREE.Points(geo1, new THREE.PointsMaterial({
        size: 1.5,
        vertexColors: true,
        map: starTex,
        transparent: true,
        opacity: 0.6,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      }));
      scene.add(starLayer1);

      // Layer 2: Midground Stars (220 small stars, subtle twinkle)
      const count2 = 220;
      const pos2 = new Float32Array(count2 * 3);
      const col2 = new Float32Array(count2 * 3);
      for (let i = 0; i < count2; i++) {
        let x = (Math.random() - 0.5) * 900;
        let y = (Math.random() - 0.5) * 650;
        // Avoid clustering right in front of text (x: -120 to 10, y: -40 to 60)
        if (x > -120 && x < 10 && y > -40 && y < 60) x -= 140;

        pos2[i * 3] = x;
        pos2[i * 3 + 1] = y;
        pos2[i * 3 + 2] = -100 + Math.random() * 150;

        const rand = Math.random();
        if (rand < 0.1) {
          col2[i * 3] = 0.65; col2[i * 3 + 1] = 0.35; col2[i * 3 + 2] = 0.95; // Violet
        } else if (rand < 0.2) {
          col2[i * 3] = 0.05; col2[i * 3 + 1] = 0.85; col2[i * 3 + 2] = 0.95; // Cyan
        } else {
          col2[i * 3] = 0.92; col2[i * 3 + 1] = 0.95; col2[i * 3 + 2] = 1.0; // Crisp white
        }
      }
      const geo2 = new THREE.BufferGeometry();
      geo2.setAttribute('position', new THREE.BufferAttribute(pos2, 3));
      geo2.setAttribute('color', new THREE.BufferAttribute(col2, 3));
      starLayer2 = new THREE.Points(geo2, new THREE.PointsMaterial({
        size: 2.2,
        vertexColors: true,
        map: starTex,
        transparent: true,
        opacity: 0.75,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      }));
      scene.add(starLayer2);

      // Layer 3: Foreground Floating Cosmic Motifs (ONLY 24 gentle motes)
      const count3 = 24;
      const pos3 = new Float32Array(count3 * 3);
      const col3 = new Float32Array(count3 * 3);
      for (let i = 0; i < count3; i++) {
        pos3[i * 3] = (Math.random() - 0.5) * 550;
        pos3[i * 3 + 1] = (Math.random() - 0.5) * 380;
        pos3[i * 3 + 2] = 80 + Math.random() * 140;

        col3[i * 3] = 0.9; col3[i * 3 + 1] = 0.95; col3[i * 3 + 2] = 1.0;
      }
      const geo3 = new THREE.BufferGeometry();
      geo3.setAttribute('position', new THREE.BufferAttribute(pos3, 3));
      geo3.setAttribute('color', new THREE.BufferAttribute(col3, 3));
      starLayer3 = new THREE.Points(geo3, new THREE.PointsMaterial({
        size: 3.5,
        vertexColors: true,
        map: starTex,
        transparent: true,
        opacity: 0.8,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      }));
      scene.add(starLayer3);
    }

    /* -------------------------------------------------------------
       4. CENTRAL 3D NIVORA GLOBE (CLEAN SILHOUETTE, 35% VP HEIGHT)
       ------------------------------------------------------------- */
    function buildNivoraGlobeClean() {
      globeGroup = new THREE.Group();
      globeGroup.position.set(globeCenterX, globeCenterY, globeCenterZ);

      // 35% viewport height scale (radius = 24.5)
      const globeRadius = 24.5;

      // Digital Continents & Tech Grid Texture
      const cyberTex = createDigitalWorldTextureClean();

      const sphereGeo = new THREE.SphereGeometry(globeRadius, 48, 48);
      const sphereMat = new THREE.MeshBasicMaterial({
        map: cyberTex,
        transparent: true,
        opacity: 0.75,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });
      globeMesh = new THREE.Mesh(sphereGeo, sphereMat);
      globeGroup.add(globeMesh);

      // Soft Cyan/Violet Atmospheric Shell
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
          blending: THREE.NormalBlending
        });
        logoSprite = new THREE.Sprite(logoMat);
        logoSprite.scale.set(16, 16, 1);
        globeGroup.add(logoSprite);

        // Subtle soft backing glow
        const auraMat = new THREE.SpriteMaterial({
          map: createGlowPointTexture(),
          color: 0x06b6d4,
          transparent: true,
          opacity: 0.45,
          blending: THREE.AdditiveBlending
        });
        const auraSprite = new THREE.Sprite(auraMat);
        auraSprite.scale.set(20, 20, 1);
        globeGroup.add(auraSprite);
      });

      scene.add(globeGroup);
    }

    /* -------------------------------------------------------------
       5. 3 ELEGANT ORBITAL RINGS & 1-2 PARTICLES PER ORBIT
       ------------------------------------------------------------- */
    function buildOrbitalRingsClean() {
      // Exactly 3 rings with different angles (horizontal, diagonal, vertical-diagonal)
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

        // Exactly 1 to 2 particles per ring (small, elegant, slow)
        const particleCount = rIdx === 1 ? 2 : 1;
        for (let p = 0; p < particleCount; p++) {
          const bead = new THREE.Mesh(
            new THREE.SphereGeometry(0.9, 12, 12),
            new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.9 })
          );
          const halo = new THREE.Sprite(new THREE.SpriteMaterial({
            map: createGlowPointTexture(),
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
       6. THIN, SOFT, ELEGANT GALAXY ACCRETION DISK
       ------------------------------------------------------------- */
    function buildGalaxyAccretionDiskClean() {
      // 1,100 soft particles (thinner, wider, soft cosmic platform)
      const dPoints = 1100;
      const dPos = new Float32Array(dPoints * 3);
      const dCol = new Float32Array(dPoints * 3);

      for (let i = 0; i < dPoints; i++) {
        const radius = 8 + Math.pow(Math.random(), 1.3) * 54;
        const angle = Math.random() * Math.PI * 2;
        const spiralOffset = radius * 0.06;
        const theta = angle + spiralOffset;

        dPos[i * 3] = Math.cos(theta) * radius;
        dPos[i * 3 + 1] = (Math.random() - 0.5) * 1.8;
        dPos[i * 3 + 2] = Math.sin(theta) * radius;

        // Dark center -> violet outer glow -> cyan highlights -> subtle magenta
        const p = radius / 62;
        if (p < 0.25) {
          dCol[i * 3] = 0.9; dCol[i * 3 + 1] = 0.95; dCol[i * 3 + 2] = 1.0;
        } else if (p < 0.6) {
          dCol[i * 3] = 0.55; dCol[i * 3 + 1] = 0.2; dCol[i * 3 + 2] = 0.85; // Violet
        } else if (p < 0.8) {
          dCol[i * 3] = 0.85; dCol[i * 3 + 1] = 0.2; dCol[i * 3 + 2] = 0.75; // Magenta
        } else {
          dCol[i * 3] = 0.05; dCol[i * 3 + 1] = 0.7; dCol[i * 3 + 2] = 0.9; // Cyan
        }
      }

      const dGeo = new THREE.BufferGeometry();
      dGeo.setAttribute('position', new THREE.BufferAttribute(dPos, 3));
      dGeo.setAttribute('color', new THREE.BufferAttribute(dCol, 3));
      galaxyDisk = new THREE.Points(dGeo, new THREE.PointsMaterial({
        size: 2.0,
        vertexColors: true,
        map: createGlowPointTexture(),
        transparent: true,
        opacity: 0.65,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      }));
      galaxyDisk.position.set(globeCenterX, globeCenterY - 35, globeCenterZ);
      galaxyDisk.rotation.set(Math.PI / 2.3, 0, 0.1);
      scene.add(galaxyDisk);

      // Subtle Vertical Energy Beam
      const beamGeo = new THREE.CylinderGeometry(1.2, 3.2, 18, 24, 1, true);
      galaxyEnergyBeam = new THREE.Mesh(beamGeo, new THREE.MeshBasicMaterial({
        color: 0x06b6d4,
        transparent: true,
        opacity: 0.35,
        blending: THREE.AdditiveBlending,
        side: THREE.DoubleSide,
        depthWrite: false
      }));
      galaxyEnergyBeam.position.set(globeCenterX, globeCenterY - 22, globeCenterZ);
      scene.add(galaxyEnergyBeam);
    }

    /* -------------------------------------------------------------
       7. CLEAN TEXTURES
       ------------------------------------------------------------- */
    function createGlowPointTexture() {
      const c = document.createElement('canvas');
      c.width = 64; c.height = 64;
      const ctx = c.getContext('2d');
      const grad = ctx.createRadialGradient(32, 32, 0, 32, 32, 32);
      grad.addColorStop(0, 'rgba(255, 255, 255, 1)');
      grad.addColorStop(0.3, 'rgba(255, 255, 255, 0.7)');
      grad.addColorStop(0.7, 'rgba(6, 182, 212, 0.25)');
      grad.addColorStop(1, 'rgba(6, 182, 212, 0)');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, 64, 64);
      return new THREE.CanvasTexture(c);
    }

    function createDigitalWorldTextureClean() {
      const c = document.createElement('canvas');
      c.width = 1024; c.height = 512;
      const ctx = c.getContext('2d');

      // Transparent/dark cyber base
      ctx.fillStyle = 'rgba(2, 6, 20, 0.4)';
      ctx.fillRect(0, 0, 1024, 512);

      // Fine Longitude / Latitude Tech Lines
      ctx.strokeStyle = 'rgba(6, 182, 212, 0.18)';
      ctx.lineWidth = 0.8;
      for (let x = 0; x < 1024; x += 64) {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, 512); ctx.stroke();
      }
      for (let y = 0; y < 512; y += 48) {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(1024, y); ctx.stroke();
      }

      // Subtle continental nodes
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
    }

    /* -------------------------------------------------------------
       8. SUBTLE MOUSE PARALLAX & CONTINUOUS ANIMATION LOOP
       ------------------------------------------------------------- */
    window.addEventListener('mousemove', (e) => {
      // Subtle: 2-3% displacement only
      mouse.targetX = (e.clientX / window.innerWidth - 0.5) * 1.2;
      mouse.targetY = -(e.clientY / window.innerHeight - 0.5) * 1.0;
    }, { passive: true });

    function animateUniverseClean() {
      requestAnimationFrame(animateUniverseClean);

      const elapsed = clock.getElapsedTime();

      // Smooth mouse damping
      mouse.x += (mouse.targetX - mouse.x) * 0.04;
      mouse.y += (mouse.targetY - mouse.y) * 0.04;

      if (!isZoomingTransition) {
        // Subtle camera parallax
        camera.position.x = baseCamX + mouse.x * 3.5;
        camera.position.y = baseCamY + mouse.y * 2.5;
        camera.lookAt(globeCenterX * 0.45 + mouse.x * 1.2, globeCenterY + mouse.y * 0.8, 0);
      }

      // Globe axial rotation
      if (globeMesh) globeMesh.rotation.y += 0.0014 * warpSpeedFactor;

      // Logo gentle bobbing
      if (logoSprite) {
        logoSprite.position.y = Math.sin(elapsed * 1.5) * 0.5;
      }

      // Orbital particles
      ringParticles.forEach((p) => {
        p.progress = (p.progress + p.speed * warpSpeedFactor + 1) % 1;
        const pt = p.curve.getPoint(p.progress);
        const v = new THREE.Vector3(pt.x, pt.y, 0);
        v.applyEuler(new THREE.Euler(p.rotX, p.rotY, p.rotZ));
        p.mesh.position.copy(v);
      });

      // Galaxy disk rotation
      if (galaxyDisk) galaxyDisk.rotation.z += 0.002 * warpSpeedFactor;

      // Energy beam pulsing
      if (galaxyEnergyBeam) {
        const pulse = 1 + 0.05 * Math.sin(elapsed * 3);
        galaxyEnergyBeam.scale.set(pulse, 1, pulse);
      }

      // Gentle star drift
      if (starLayer1) starLayer1.rotation.y += 0.0001 * warpSpeedFactor;

      renderer.render(scene, camera);
    }

    window.addEventListener('resize', () => {
      if (!isWebGLEnabled || !renderer) return;
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    });

    /* -------------------------------------------------------------
       9. SMOOTH 3D CAMERA ZOOM (SCROLL & BUTTON)
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
        camera.lookAt(globeCenterX, globeCenterY, 0);

        warpSpeedFactor = 1 + ease * 4;

        if (p > 0.75 && p < 0.95) {
          if (flash) flash.style.opacity = String((p - 0.75) / 0.2);
        } else if (p >= 0.95) {
          if (flash) flash.style.opacity = '1';
        }

        if (p < 1) {
          requestAnimationFrame(step);
        } else {
          const prodSec = document.getElementById('products');
          if (prodSec) prodSec.scrollIntoView({ behavior: 'instant' });

          setTimeout(() => {
            if (flash) flash.style.opacity = '0';
            setTimeout(() => {
              isZoomingTransition = false;
              warpSpeedFactor = 1.0;
              camera.position.set(baseCamX, baseCamY, baseCamZ);
              camera.lookAt(globeCenterX * 0.45, globeCenterY, 0);
            }, 350);
          }, 150);
        }
      }
      requestAnimationFrame(step);
    }

    window.addEventListener('scroll', () => {
      if (isZoomingTransition || !isWebGLEnabled) return;
      const scrollY = window.scrollY;
      const heroH = window.innerHeight;
      if (scrollY < heroH * 1.5) {
        const p = Math.min(scrollY / (heroH * 0.95), 1);
        camera.position.x = baseCamX + (globeCenterX - baseCamX) * (p * 0.55);
        camera.position.z = baseCamZ - (p * 150);
        camera.lookAt(globeCenterX * 0.45 + (globeCenterX * 0.45 * p), globeCenterY, 0);
      }
    }, { passive: true });

    /* -------------------------------------------------------------
       10. CLEAN CANVAS 3D FALLBACK
       ------------------------------------------------------------- */
    function initCanvas3DFallbackClean() {
      const ctx = canvas.getContext('2d');
      let w = canvas.width = window.innerWidth;
      let h = canvas.height = window.innerHeight;

      const fallbackLogo = new Image();
      fallbackLogo.src = 'assets/images/nivora-logo.png';

      window.addEventListener('resize', () => {
        w = canvas.width = window.innerWidth;
        h = canvas.height = window.innerHeight;
      });

      // 180 clean stars
      const stars = [];
      for (let i = 0; i < 180; i++) {
        stars.push({
          x: (Math.random() - 0.5) * w * 2,
          y: (Math.random() - 0.5) * h * 2,
          z: Math.random() * 1000 + 50,
          size: Math.random() * 1.5 + 0.8
        });
      }

      let angle = 0;
      function drawFallback() {
        ctx.clearRect(0, 0, w, h);
        angle += 0.01;

        // Subtle 3D stars
        ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
        stars.forEach(s => {
          s.z -= 0.5;
          if (s.z <= 0) s.z = 1000;
          const k = 300 / s.z;
          const px = s.x * k + w / 2;
          const py = s.y * k + h / 2;
          if (px >= 0 && px <= w && py >= 0 && py <= h) {
            ctx.beginPath();
            ctx.arc(px, py, s.size * k * 0.7, 0, Math.PI * 2);
            ctx.fill();
          }
        });

        // 3D Luminous Globe & Rings on Right Side
        const gx = w * 0.72;
        const gy = h * 0.48;
        const gr = Math.min(w, h) * 0.17;

        // Soft Atmospheric Glow
        const atmosGrad = ctx.createRadialGradient(gx, gy, gr * 0.2, gx, gy, gr * 1.15);
        atmosGrad.addColorStop(0, 'rgba(168, 85, 247, 0.35)');
        atmosGrad.addColorStop(0.6, 'rgba(6, 182, 212, 0.22)');
        atmosGrad.addColorStop(0.9, 'rgba(6, 182, 212, 0.08)');
        atmosGrad.addColorStop(1, 'rgba(6, 182, 212, 0)');
        ctx.fillStyle = atmosGrad;
        ctx.beginPath();
        ctx.arc(gx, gy, gr * 1.15, 0, Math.PI * 2);
        ctx.fill();

        // 3 Thin Orbital Rings
        ctx.lineWidth = 1.2;
        ctx.strokeStyle = 'rgba(168, 85, 247, 0.45)';
        ctx.beginPath();
        ctx.ellipse(gx, gy, gr * 1.35, gr * 0.42, 0.45, 0, Math.PI * 2);
        ctx.stroke();

        ctx.strokeStyle = 'rgba(6, 182, 212, 0.45)';
        ctx.beginPath();
        ctx.ellipse(gx, gy, gr * 1.45, gr * 0.32, -0.60, 0, Math.PI * 2);
        ctx.stroke();

        // 1 travelling photon bead
        const b1Angle = angle * 1.2;
        const b1x = gx + Math.cos(b1Angle) * gr * 1.35 * Math.cos(0.45) - Math.sin(b1Angle) * gr * 0.42 * Math.sin(0.45);
        const b1y = gy + Math.cos(b1Angle) * gr * 1.35 * Math.sin(0.45) + Math.sin(b1Angle) * gr * 0.42 * Math.cos(0.45);
        ctx.fillStyle = '#67e8f9';
        ctx.beginPath();
        ctx.arc(b1x, b1y, 2.8, 0, Math.PI * 2);
        ctx.fill();

        // Crisp Suspended NIVORA Logo in Center
        if (fallbackLogo.complete && fallbackLogo.naturalWidth > 0) {
          const lw = gr * 0.75;
          const lh = lw * (fallbackLogo.naturalHeight / fallbackLogo.naturalWidth);
          ctx.drawImage(fallbackLogo, gx - lw / 2, gy - lh / 2, lw, lh);
        }

        requestAnimationFrame(drawFallback);
      }
      drawFallback();
    }

    window.addEventListener('DOMContentLoaded', () => {
      initUniverse3D();
    });

    /* -------------------------------------------------------------
       13. CONCEPT MODAL POPUP ENGINE
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
        url: 'https://homora.vercel.app'
      },
      'bubora': {
        name: 'BUBORA',
        badge: 'In Development',
        url: ''
      },
      'sayora': {
        name: 'SAYORA',
        badge: 'Conceptual Stage',
        url: ''
      }
    };

    function openConceptModal(prodId) {
      const overlay = document.getElementById('conceptModalOverlay');
      const prodName = document.getElementById('modalTopProductName');
      const prodBadge = document.getElementById('modalTopStatusBadge');
      const launchBtn = document.getElementById('modalLaunchBtn');
      const views = document.querySelectorAll('.modal-product-view');

      views.forEach(v => v.classList.remove('active'));
      const activeView = document.getElementById('modal-view-' + prodId);
      if (activeView) activeView.classList.add('active');

      const meta = productMeta[prodId];
      if (meta) {
        if (prodName) prodName.innerText = meta.name;
        if (prodBadge) prodBadge.innerText = meta.badge;
        if (launchBtn) {
          if (meta.url) {
            launchBtn.style.display = 'inline-flex';
            launchBtn.href = meta.url;
          } else {
            launchBtn.style.display = 'none';
          }
        }
      }

      if (overlay) {
        overlay.classList.add('open');
        overlay.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
      }

      const scrollBody = document.getElementById('modalScrollBody');
      if (scrollBody) scrollBody.scrollTop = 0;
    }

    function closeConceptModal() {
      const overlay = document.getElementById('conceptModalOverlay');
      if (overlay) {
        overlay.classList.remove('open');
        overlay.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
      }
    }

    function scrollModalSec(secId) {
      const activeView = document.querySelector('.modal-product-view.active');
      if (!activeView) return;
      const targetSec = activeView.querySelector('[id*="-' + secId + '"]');
      if (targetSec) {
        targetSec.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
      const tabs = document.querySelectorAll('.modal-nav-tab');
      tabs.forEach(t => t.classList.remove('active'));
      const clicked = event?.target;
      if (clicked) clicked.classList.add('active');
    }

    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeConceptModal();
    });

    document.getElementById('conceptModalOverlay')?.addEventListener('click', (e) => {
      if (e.target.id === 'conceptModalOverlay') closeConceptModal();
    });

    /* -------------------------------------------------------------
       14. CONTACT FORM TRANSMISSION HANDLER
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

def generate():
    html = build_ultimate_universe_html()
    desktop_path = "/Users/bennabathulanivas/Desktop/my projects/NIVORA/index.html"
    downloads_path = "/Users/bennabathulanivas/Downloads/NIVORA/index.html"

    with open(desktop_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {len(html)} bytes to {desktop_path}")

    with open(downloads_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {len(html)} bytes to {downloads_path}")

if __name__ == '__main__':
    generate()
