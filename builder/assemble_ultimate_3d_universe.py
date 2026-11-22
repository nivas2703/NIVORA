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
    /* PURE DEEP SPACE AMBIENCE — 100% PROCEDURAL (ZERO STATIC IMAGES) */
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

    /* 3D PRODUCT WORLD HOVER HUD PILL */
    .product-world-tooltip {
      position: fixed;
      top: 0;
      left: 0;
      z-index: 150;
      pointer-events: none;
      display: none;
      align-items: center;
      gap: 0.75rem;
      padding: 0.5rem 1.15rem;
      background: rgba(8, 12, 28, 0.88);
      border: 1px solid rgba(6, 182, 212, 0.45);
      box-shadow: 0 12px 35px -10px rgba(0, 0, 0, 0.9), 0 0 25px rgba(6, 182, 212, 0.35);
      border-radius: 9999px;
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      transform: translate(-50%, -135%);
      transition: opacity 0.2s ease, transform 0.2s ease;
      white-space: nowrap;
    }
    .pwt-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #06b6d4;
      box-shadow: 0 0 10px #06b6d4;
    }
    .pwt-text {
      display: flex;
      flex-direction: column;
      gap: 0.1rem;
    }
    .pwt-name {
      font-family: var(--font-display);
      font-size: 0.82rem;
      font-weight: 700;
      letter-spacing: 0.06em;
      color: #ffffff;
    }
    .pwt-tagline {
      font-family: var(--font-body);
      font-size: 0.66rem;
      color: #94a3b8;
    }
    .pwt-hint {
      font-family: var(--font-mono);
      font-size: 0.62rem;
      color: #38bdf8;
      padding-left: 0.5rem;
      border-left: 1px solid rgba(255, 255, 255, 0.15);
      letter-spacing: 0.05em;
    }

    /* Initial state for cinematic intro */
    .hero-content {
      transition: opacity 0.3s ease, transform 0.3s ease;
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
       HERO COMPOSITION — EXACT CENTERED UNIVERSE & TYPOGRAPHY
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
      pointer-events: none; /* UI inside is enabled selectively */
      text-align: center;
    }

    .hero-container {
      width: 100%;
      max-width: 860px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      position: relative;
      z-index: 10;
      pointer-events: auto;
    }

    /* Centered Official NIVORA Logo Stage */
    .hero-center-logo-stage {
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 1.6rem;
      cursor: pointer;
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 25;
    }

    .hero-center-logo-stage:hover {
      transform: scale(1.05);
    }

    .hero-logo-glow-disc {
      position: absolute;
      width: 280px;
      height: 280px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(6, 182, 212, 0.32) 0%, rgba(168, 85, 247, 0.22) 40%, rgba(2, 6, 23, 0) 70%);
      filter: blur(30px);
      pointer-events: none;
      animation: logoAuraPulse 4s ease-in-out infinite alternate;
    }

    @keyframes logoAuraPulse {
      0% { transform: scale(0.92); opacity: 0.65; }
      100% { transform: scale(1.1); opacity: 0.95; }
    }

    .hero-center-logo-img {
      position: relative;
      z-index: 2;
      width: clamp(175px, 17vw, 235px);
      height: auto;
      object-fit: contain;
      filter: drop-shadow(0 0 25px rgba(6, 182, 212, 0.65))
              drop-shadow(0 0 55px rgba(168, 85, 247, 0.5));
      animation: logoFloatGently 5s ease-in-out infinite alternate;
    }

    @keyframes logoFloatGently {
      0% { transform: translateY(0px); }
      100% { transform: translateY(-7px); }
    }

    /* Centered Hero Content */
    .hero-content {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      width: 100%;
      max-width: 820px;
      pointer-events: auto;
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
      margin: 0 auto 1.25rem;
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
      text-align: center;
      margin-bottom: 0.95rem;
    }

    .hero-welcome {
      font-family: var(--font-display);
      font-size: clamp(2.2rem, 3.8vw, 3.5rem);
      font-weight: 700;
      letter-spacing: -0.03em;
      color: #ffffff;
      display: block;
      margin-bottom: 0.15rem;
      text-shadow: 0 4px 24px rgba(0, 0, 0, 0.95), 0 0 35px rgba(168, 85, 247, 0.35);
    }

    .hero-brand {
      display: inline-block;
      font-size: clamp(3.8rem, 7.5vw, 6.2rem);
      font-weight: 800;
      letter-spacing: -0.04em;
      line-height: 1.0;
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
      font-size: clamp(1.25rem, 2.2vw, 1.85rem);
      font-weight: 500;
      color: #f1f5f9;
      line-height: 1.3;
      text-align: center;
      max-width: 760px;
      margin: 0 auto 1.25rem;
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
      border-radius: 9999px;
    }
    .accent-ideas::after {
      background: #a855f7;
      box-shadow: 0 0 10px rgba(168, 85, 247, 0.9);
    }
    .accent-products::after {
      background: #ec4899;
      box-shadow: 0 0 10px rgba(236, 72, 153, 0.9);
    }

    /* Description (Exact 600-720px width) */
    .hero-copy {
      font-size: clamp(0.98rem, 1.2vw, 1.08rem);
      line-height: 1.7;
      color: #cbd5e1;
      text-align: center;
      max-width: 660px;
      margin: 0 auto 1.85rem;
    }

    .hero-copy strong {
      color: #ffffff;
      font-weight: 600;
    }

    /* Action Buttons */
    .hero-actions {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 1.25rem;
      margin: 0 auto 2.2rem;
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

    /* Metrics Grid (Centered) */
    .hero-metrics {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 2.8rem;
      padding-top: 1.4rem;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      max-width: 580px;
      margin: 0 auto;
      width: 100%;
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
      text-align: left;
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
    /* GLOBAL PERSISTENT UNIVERSE: ALL SECTIONS ARE TRANSPARENT OVER 3D WEBGL */
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

  <!-- 3D PRODUCT WORLD HOVER HUD PILL -->
  <div id="productWorldTooltip" class="product-world-tooltip">
    <div class="pwt-dot" id="pwtDot"></div>
    <div class="pwt-text">
      <span class="pwt-name" id="pwtName">CHECKRA</span>
      <span class="pwt-tagline" id="pwtTagline">Writing Integrity Space</span>
    </div>
    <span class="pwt-hint">Explore World &nearr;</span>
  </div>

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
        <!-- 1. EXACT CENTERED OFFICIAL NIVORA LOGO -->
        <div class="hero-center-logo-stage" onclick="triggerCinematicCameraZoom()">
          <div class="hero-logo-glow-disc"></div>
          <img src="assets/images/nivora-logo.png" alt="NIVORA" class="hero-center-logo-img" id="heroCenterLogo">
        </div>

        <!-- 2. EXACT CENTERED HERO TYPOGRAPHY & ACTIONS (BELOW LOGO) -->
        <div class="hero-content">
          <div class="hero-badge">
            <span class="dot"></span>
            <span>A NIVAS BENNABATTHULA INITIATIVE</span>
          </div>

          <h1 class="hero-title">
            <span class="hero-welcome">Welcome to</span>
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

          <!-- Hero Metrics (Centered) -->
          <div class="hero-metrics">
            <div class="metric-card">
              <div class="metric-icon-wrap m-purple">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
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
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
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
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M18.178 8c5.096 0 5.096 8 0 8-3.084 0-4.321-2.91-6.178-5.334C10.143 8.244 8.906 8 5.822 8 0.726 8 0.726 16 5.822 16c3.084 0 4.321-2.91 6.178-5.334C13.857 13.09 15.094 16 18.178 16z"></path>
                </svg>
              </div>
              <div class="metric-info">
                <strong>&infin;</strong>
                <span>Digital Possibilities</span>
              </div>
            </div>
          </div>
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
       2. THREE.JS FULL 3D CINEMATIC UNIVERSE ENGINE
          (PROCEDURAL MILKY WAY + ORBITAL PRODUCT WORLDS + CAMERA TRAVEL)
       ------------------------------------------------------------- */
    const canvas = document.getElementById('webglUniverseCanvas');
    let renderer, scene, camera;
    let milkyWayGroup, galacticBulge, spiralArmStars;
    let distantStarField, brightBeaconsGroup, distantGalaxiesGroup;
    let globeGroup, globeHaloSprite;
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
    let transmissionBeaconGroup;

    // 3D Product Worlds
    let productWorldsGroup;
    let productWorlds = [];
    let productHitTargets = [];
    let hoveredProduct = null;
    const raycaster = new THREE.Raycaster();
    const mouseRay = new THREE.Vector2(-999, -999);
    const tooltipEl = document.getElementById('productWorldTooltip');
    const pwtNameEl = document.getElementById('pwtName');
    const pwtTaglineEl = document.getElementById('pwtTagline');
    const pwtDotEl = document.getElementById('pwtDot');

    let isWebGLEnabled = false;
    let isZoomingTransition = false;
    let warpSpeedFactor = 1.0;
    let mouse = { x: 0, y: 0, targetX: 0, targetY: 0 };
    let clock = new THREE.Clock();

    // Base Camera Coordinates (Exact Centered Universe Composition)
    const baseCamX = 0;
    const baseCamY = 16;
    const baseCamZ = 260;
    const globeCenterX = 0.0;
    const globeCenterY = 36.0;
    const globeCenterZ = 0.0;

    let currentCamPos = new THREE.Vector3(baseCamX, baseCamY, baseCamZ);
    let currentLookAt = new THREE.Vector3(0, 18, 0);
    let targetScrollP = 0;

    // 4 Product Worlds Configuration
    const productConfigs = [
      {
        id: 'checkra',
        name: 'CHECKRA',
        tagline: 'Writing Integrity & Plagiarism Intelligence',
        color: 0x8b5cf6,
        glowColor: '#8b5cf6',
        emblem: 'assets/images/checkra-emblem.png',
        radius: 46,
        speed: 0.0016,
        inclinationX: 0.35,
        inclinationY: 0.12,
        inclinationZ: 0.18,
        sphereSize: 2.5,
        startProgress: 0.18
      },
      {
        id: 'homora',
        name: 'HOMORA',
        tagline: 'Smart Living & Shared Finance',
        color: 0x06b6d4,
        glowColor: '#06b6d4',
        emblem: 'assets/images/homora-logo.png',
        radius: 72,
        speed: 0.0012,
        inclinationX: -0.42,
        inclinationY: 0.32,
        inclinationZ: -0.22,
        sphereSize: 2.8,
        startProgress: 0.44
      },
      {
        id: 'bubora',
        name: 'BUBORA',
        tagline: 'Intimate Digital Sanctuary for Two',
        color: 0xec4899,
        glowColor: '#ec4899',
        emblem: 'assets/images/bubora-logo.png',
        radius: 100,
        speed: -0.0009,
        inclinationX: 0.48,
        inclinationY: -0.28,
        inclinationZ: 0.35,
        sphereSize: 2.6,
        startProgress: 0.68
      },
      {
        id: 'sayora',
        name: 'SAYORA',
        tagline: 'Social Impact & Financial Shield',
        color: 0x10b981,
        glowColor: '#10b981',
        emblem: 'assets/images/sayora-emblem.png',
        radius: 130,
        speed: 0.0007,
        inclinationX: -0.28,
        inclinationY: 0.45,
        inclinationZ: 0.12,
        sphereSize: 3.0,
        startProgress: 0.88
      }
    ];

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
        renderer.setClearColor(0x02040a, 0);
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 1.25;

        scene = new THREE.Scene();
        camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 4000);
        camera.position.set(baseCamX, baseCamY, baseCamZ);
        camera.lookAt(0, 18, 0);

        // Build 3D Cinematic Universe (Clean Procedural Milky Way & Centered Core Halo)
        buildDistantStarfield();
        buildWarpStarfield();
        buildProceduralMilkyWay();
        buildGalacticBulge();
        buildSubtleCosmicNebula();
        buildBrightStellarBeacons();
        buildNivoraGlobeCore();
        build3DProductWorlds();
        buildSpatialDestinations();

        setupInteractivity();
        isWebGLEnabled = true;
        animateUniverseCinematic();
        runCinematicIntro();
      } catch (e) {
        console.warn("WebGL notice, running high-performance 2D canvas fallback:", e);
        initCanvas3DFallbackClean();
      }
    }

    /* -------------------------------------------------------------
       3. PROCEDURAL MILKY WAY SPIRAL ARMS (42,000 GPU PARTICLES)
       ------------------------------------------------------------- */
    function buildProceduralMilkyWay() {
      milkyWayGroup = new THREE.Group();
      milkyWayGroup.position.set(globeCenterX, globeCenterY, globeCenterZ);
      milkyWayGroup.rotation.set(0.82, 0.22, -0.15); // Majestic cinematic 3D tilt

      const starCount = 42000;
      const positions = new Float32Array(starCount * 3);
      const colors = new Float32Array(starCount * 3);

      const armAngles = [0.45, 0.45 + Math.PI, 1.85, 1.85 + Math.PI];
      const armWeights = [0.38, 0.38, 0.12, 0.12];
      const rMin = 22;
      const rMax = 260;

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

        // Mathematical logarithmic spiral
        const spiralAngle = baseAngle + 2.25 * Math.log(r / rMin) + 0.22 * (r / rMax);

        // Radial and vertical Gaussian dispersion
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

        // Color Grading: soft white, electric cyan, indigo, violet, magenta
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
    }

    /* -------------------------------------------------------------
       4. GALACTIC BULGE (7,500 CORE PARTICLES)
       ------------------------------------------------------------- */
    function buildGalacticBulge() {
      const bulgeCount = 7500;
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
        size: 1.7,
        sizeAttenuation: true,
        vertexColors: true,
        map: createSoftPointTexture(),
        transparent: true,
        opacity: 0.88,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });

      galacticBulge = new THREE.Points(bulgeGeo, bulgeMat);
      milkyWayGroup.add(galacticBulge);
    }

    /* -------------------------------------------------------------
       5. 4 ORBITAL PRODUCT WORLDS (CHECKRA, HOMORA, BUBORA, SAYORA)
       ------------------------------------------------------------- */
    function build3DProductWorlds() {
      productWorldsGroup = new THREE.Group();
      productWorldsGroup.visible = false;
      scene.add(productWorldsGroup);

      const texLoader = new THREE.TextureLoader();

      productConfigs.forEach((cfg) => {
        // 1. Orbital Path Line
        const curve = new THREE.EllipseCurve(
          0, 0,
          cfg.radius, cfg.radius * 0.92,
          0, 2 * Math.PI, false, 0
        );
        const curvePoints = curve.getPoints(120);
        const pathGeo = new THREE.BufferGeometry().setFromPoints(curvePoints);
        const pathLine = new THREE.Line(pathGeo, new THREE.LineBasicMaterial({
          color: cfg.color,
          transparent: true,
          opacity: 0.22,
          blending: THREE.AdditiveBlending
        }));
        pathLine.position.set(globeCenterX, globeCenterY, globeCenterZ);
        pathLine.rotation.set(cfg.inclinationX, cfg.inclinationY, cfg.inclinationZ);
        productWorldsGroup.add(pathLine);

        // 2. World Container Group
        const worldGroup = new THREE.Group();

        // 3. Central Planetary Sphere
        const planetGeo = new THREE.SphereGeometry(cfg.sphereSize, 24, 24);
        const planetMat = new THREE.MeshBasicMaterial({
          color: cfg.color,
          transparent: true,
          opacity: 0.9
        });
        const planetMesh = new THREE.Mesh(planetGeo, planetMat);
        worldGroup.add(planetMesh);

        // 4. Atmospheric Glow Shell
        const haloMat = new THREE.SpriteMaterial({
          map: createSoftPointTexture(),
          color: cfg.color,
          transparent: true,
          opacity: 0.7,
          blending: THREE.AdditiveBlending
        });
        const haloSprite = new THREE.Sprite(haloMat);
        haloSprite.scale.set(cfg.sphereSize * 5.0, cfg.sphereSize * 5.0, 1);
        worldGroup.add(haloSprite);

        // 5. Billboard Emblem Sprite
        texLoader.load(cfg.emblem, (tex) => {
          tex.minFilter = THREE.LinearFilter;
          tex.magFilter = THREE.LinearFilter;
          const emblemMat = new THREE.SpriteMaterial({
            map: tex,
            transparent: true,
            opacity: 0.95,
            depthTest: false
          });
          const emblemSprite = new THREE.Sprite(emblemMat);
          emblemSprite.scale.set(8.5, 8.5, 1);
          emblemSprite.position.set(0, cfg.sphereSize * 2.2, 0);
          emblemSprite.renderOrder = 30;
          worldGroup.add(emblemSprite);
        });

        // 6. Orbiting Photon Moon
        const moon = new THREE.Mesh(
          new THREE.SphereGeometry(0.5, 12, 12),
          new THREE.MeshBasicMaterial({ color: 0xffffff })
        );
        worldGroup.add(moon);

        // 7. Raycast Hit Proxy Sphere (Invisible)
        const hitGeo = new THREE.SphereGeometry(cfg.sphereSize * 3.2, 12, 12);
        const hitMat = new THREE.MeshBasicMaterial({ visible: false });
        const hitMesh = new THREE.Mesh(hitGeo, hitMat);
        hitMesh.userData = {
          isProductWorld: true,
          id: cfg.id,
          name: cfg.name,
          tagline: cfg.tagline,
          color: cfg.glowColor,
          group: worldGroup,
          pathLine: pathLine
        };
        worldGroup.add(hitMesh);
        productHitTargets.push(hitMesh);

        productWorldsGroup.add(worldGroup);

        productWorlds.push({
          config: cfg,
          group: worldGroup,
          curve: curve,
          moon: moon,
          pathLine: pathLine,
          progress: cfg.startProgress,
          speed: cfg.speed
        });
      });
    }

    /* -------------------------------------------------------------
       6. PROCEDURAL NEBULA CLOUDS & STELLAR STARFIELDS
       ------------------------------------------------------------- */
    function buildSubtleCosmicNebula() {
      const texNavy = createProceduralNebulaTexture('#0a0e27', '#030514');
      const texViolet = createProceduralNebulaTexture('#1e123d', '#070414');
      const texCyan = createProceduralNebulaTexture('#083344', '#020b14');

      for (let i = 0; i < 32; i++) {
        const tex = (i % 3 === 0) ? texCyan : (i % 3 === 1 ? texViolet : texNavy);
        const mat = new THREE.SpriteMaterial({
          map: tex,
          transparent: true,
          opacity: 0.035 + Math.random() * 0.035,
          blending: THREE.AdditiveBlending,
          depthWrite: false
        });
        const sprite = new THREE.Sprite(mat);

        const r = 30 + Math.pow(Math.random(), 1.3) * 180;
        const a = Math.random() * Math.PI * 2;
        sprite.position.set(
          globeCenterX + Math.cos(a) * r,
          globeCenterY + (Math.random() - 0.5) * 45,
          globeCenterZ + Math.sin(a) * r - 20
        );
        const s = 150 + Math.random() * 220;
        sprite.scale.set(s, s, 1);
        scene.add(sprite);
        nebulaPuffs.push({ sprite, baseScale: s, seed: Math.random() * 10 });
      }
    }

    /* -------------------------------------------------------------
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
      builderSpatialHalo.visible = false;
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
      builderEmbersPoints.visible = false;
      scene.add(builderEmbersPoints);

      // 2. CREATION FIELD DESTINATION (Z = -840)
      // 6 Glowing Constellation Nodes floating in space
      portfolioConstellationGroup = new THREE.Group();
      portfolioConstellationGroup.position.set(0, 8, -840);
      portfolioConstellationGroup.visible = false;
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
      transmissionBeaconGroup.visible = false;

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

    function buildDistantStarfield() {
      const count = 14000;
      const pos = new Float32Array(count * 3);
      const col = new Float32Array(count * 3);

      for (let i = 0; i < count; i++) {
        pos[i * 3] = (Math.random() - 0.5) * 1600;
        pos[i * 3 + 1] = (Math.random() - 0.5) * 1000;
        pos[i * 3 + 2] = -400 - Math.random() * 1100;

        const isCyan = Math.random() < 0.08;
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
        size: 1.1,
        sizeAttenuation: true,
        vertexColors: true,
        map: createSoftPointTexture(),
        transparent: true,
        opacity: 0.65,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });

      distantStarField = new THREE.Points(geo, mat);
      scene.add(distantStarField);
    }

    function buildBrightStellarBeacons() {
      brightBeaconsGroup = new THREE.Group();
      const count = 160;
      const starTex = createDiffractionStarTexture();

      for (let i = 0; i < count; i++) {
        const mat = new THREE.SpriteMaterial({
          map: starTex,
          transparent: true,
          opacity: 0.5 + Math.random() * 0.35,
          blending: THREE.AdditiveBlending,
          depthWrite: false
        });
        const sprite = new THREE.Sprite(mat);

        let x = (Math.random() - 0.5) * 850;
        let y = (Math.random() - 0.5) * 550;
        let z = (Math.random() - 0.5) * 450 - 50;

        if (x < -10 && y > -40 && y < 50) x -= 90;

        sprite.position.set(x, y, z);
        const s = 3.5 + Math.random() * 6.0;
        sprite.scale.set(s, s, 1);
        brightBeaconsGroup.add(sprite);
      }
      scene.add(brightBeaconsGroup);
    }

    /* -------------------------------------------------------------
       7. NIVORA UNIVERSE CORE — AURA & SUBTLE ORBITAL HALO
       ------------------------------------------------------------- */
    function buildNivoraGlobeCore() {
      globeGroup = new THREE.Group();
      globeGroup.position.set(globeCenterX, globeCenterY, globeCenterZ);

      // 1. Radiant Atmospheric Corona Sprite (Centered behind official logo)
      const haloMat = new THREE.SpriteMaterial({
        map: createCoronaHaloTexture(),
        transparent: true,
        opacity: 0.65,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });
      globeHaloSprite = new THREE.Sprite(haloMat);
      globeHaloSprite.scale.set(72, 72, 1);
      globeHaloSprite.position.set(0, 0, -10);
      globeHaloSprite.renderOrder = 10;
      globeGroup.add(globeHaloSprite);

      // 2. 2,200 Subtle Orbital Quantum Particles (Delicate cosmic halo orbiting r = 22 to 32)
      const haloPointCount = 2200;
      const haloPos = new Float32Array(haloPointCount * 3);
      const haloCol = new Float32Array(haloPointCount * 3);

      for (let i = 0; i < haloPointCount; i++) {
        const r = 22.0 + Math.random() * 9.0;
        const theta = Math.random() * Math.PI * 2;
        const phi = (Math.random() - 0.5) * 0.75;

        haloPos[i * 3] = r * Math.cos(phi) * Math.cos(theta);
        haloPos[i * 3 + 1] = r * Math.sin(phi) + (Math.random() - 0.5) * 2.2;
        haloPos[i * 3 + 2] = r * Math.cos(phi) * Math.sin(theta);

        const t = (r - 22.0) / 9.0;
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
        map: createSoftPointTexture(),
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
       10. TEXTURE GENERATORS
       ------------------------------------------------------------- */
    function createSoftPointTexture() {
      const c = document.createElement('canvas');
      c.width = 64; c.height = 64;
      const ctx = c.getContext('2d');
      const grad = ctx.createRadialGradient(32, 32, 0, 32, 32, 32);
      grad.addColorStop(0, 'rgba(255, 255, 255, 1)');
      grad.addColorStop(0.25, 'rgba(255, 255, 255, 0.75)');
      grad.addColorStop(0.65, 'rgba(6, 182, 212, 0.25)');
      grad.addColorStop(1, 'rgba(6, 182, 212, 0)');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, 64, 64);
      return new THREE.CanvasTexture(c);
    }

    function createDiffractionStarTexture() {
      const c = document.createElement('canvas');
      c.width = 128; c.height = 128;
      const ctx = c.getContext('2d');

      const grad = ctx.createRadialGradient(64, 64, 0, 64, 64, 64);
      grad.addColorStop(0, 'rgba(255, 255, 255, 1)');
      grad.addColorStop(0.15, 'rgba(224, 242, 254, 0.8)');
      grad.addColorStop(0.5, 'rgba(139, 92, 246, 0.2)');
      grad.addColorStop(1, 'rgba(6, 182, 212, 0)');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, 128, 128);

      ctx.lineWidth = 1.0;
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.45)';
      ctx.beginPath();
      ctx.moveTo(64, 20); ctx.lineTo(64, 108);
      ctx.moveTo(20, 64); ctx.lineTo(108, 64);
      ctx.stroke();

      return new THREE.CanvasTexture(c);
    }

    function createProceduralNebulaTexture(c1, c2) {
      const c = document.createElement('canvas');
      c.width = 256; c.height = 256;
      const ctx = c.getContext('2d');
      const grad = ctx.createRadialGradient(128, 128, 0, 128, 128, 128);
      grad.addColorStop(0, c1);
      grad.addColorStop(0.5, c2);
      grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, 256, 256);
      return new THREE.CanvasTexture(c);
    }

    function createOceanPlanetTexture() {
      const c = document.createElement('canvas');
      c.width = 1024; c.height = 512;
      const ctx = c.getContext('2d');
      const bg = ctx.createLinearGradient(0, 0, 1024, 512);
      bg.addColorStop(0, '#030c24');
      bg.addColorStop(0.5, '#051838');
      bg.addColorStop(1, '#072b5c');
      ctx.fillStyle = bg;
      ctx.fillRect(0, 0, 1024, 512);

      ctx.fillStyle = 'rgba(56, 189, 248, 0.14)';
      for (let i = 0; i < 35; i++) {
        const x = Math.random() * 1024;
        const y = Math.random() * 512;
        const r = 35 + Math.random() * 85;
        ctx.beginPath();
        ctx.arc(x, y, r, 0, Math.PI * 2);
        ctx.fill();
      }
      return new THREE.CanvasTexture(c);
    }

    function createShadowedPlanetTexture(c1, c2) {
      const c = document.createElement('canvas');
      c.width = 512; c.height = 256;
      const ctx = c.getContext('2d');
      const grad = ctx.createLinearGradient(0, 0, 512, 256);
      grad.addColorStop(0, c1);
      grad.addColorStop(0.5, c2);
      grad.addColorStop(1, '#020108');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, 512, 256);
      return new THREE.CanvasTexture(c);
    }

    function createCoronaHaloTexture() {
      const c = document.createElement('canvas');
      c.width = 256; c.height = 256;
      const ctx = c.getContext('2d');
      const grad = ctx.createRadialGradient(128, 128, 10, 128, 128, 128);
      grad.addColorStop(0, 'rgba(6, 182, 212, 0.45)');
      grad.addColorStop(0.35, 'rgba(168, 85, 247, 0.35)');
      grad.addColorStop(0.70, 'rgba(59, 130, 246, 0.18)');
      grad.addColorStop(1, 'rgba(2, 6, 23, 0)');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, 256, 256);
      return new THREE.CanvasTexture(c);
    }

    function createDigitalWorldTextureCinematic() {
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

    function setupInteractivity() {
      window.addEventListener('mousemove', (e) => {
        mouse.targetX = (e.clientX / window.innerWidth - 0.5) * 1.2;
        mouse.targetY = -(e.clientY / window.innerHeight - 0.5) * 1.0;

        mouseRay.x = (e.clientX / window.innerWidth) * 2 - 1;
        mouseRay.y = -(e.clientY / window.innerHeight) * 2 + 1;

        if (tooltipEl && hoveredProduct) {
          tooltipEl.style.left = e.clientX + 'px';
          tooltipEl.style.top = e.clientY + 'px';
        }
      }, { passive: true });

      canvas.addEventListener('click', () => {
        if (hoveredProduct && hoveredProduct.userData && hoveredProduct.userData.id) {
          openConceptModal(hoveredProduct.userData.id);
        }
      });
    }

    /* -------------------------------------------------------------
       12. CINEMATIC CAMERA SCROLL TRAJECTORY (ZOOM OUT JOURNEY)
       ------------------------------------------------------------- */
    function getCameraTrajectory(p) {
      // 6-STAGE SPACE-TRAVEL FLIGHT PATH (Z: +260 -> -1420)
      if (p <= 0.12) {
        // Stage 1: HERO -> Forward warp acceleration past the Core into the galaxy
        const t = p / 0.12;
        const ease = t * t * (3 - 2 * t);
        return {
          pos: new THREE.Vector3(
            0,
            baseCamY + (8 - baseCamY) * ease,
            baseCamZ + (-40 - baseCamZ) * ease   // 260 -> -40 (Flies straight past Core into deep cosmos!)
          ),
          look: new THREE.Vector3(
            0,
            currentLookAt.y + (8 - currentLookAt.y) * ease,
            0 + (-180 - 0) * ease
          )
        };
      } else if (p <= 0.36) {
        // Stage 2: PRODUCT CONSTELLATION DESTINATION (Z: -40 -> -240)
        const t = (p - 0.12) / 0.24;
        const ease = t * t * (3 - 2 * t);
        return {
          pos: new THREE.Vector3(
            0,
            8,
            -40 + (-240 - -40) * ease
          ),
          look: new THREE.Vector3(
            0,
            8,
            -180 + (-420 - -180) * ease
          )
        };
      } else if (p <= 0.58) {
        // Stage 3: THE BUILDER (NIVAS) ARRIVAL (Z: -240 -> -540)
        const t = (p - 0.36) / 0.22;
        const ease = t * t * (3 - 2 * t);
        return {
          pos: new THREE.Vector3(
            0 + (-12 - 0) * ease,
            8 + (6 - 8) * ease,
            -240 + (-540 - -240) * ease
          ),
          look: new THREE.Vector3(
            0 + (-8 - 0) * ease,
            8 + (6 - 8) * ease,
            -420 + (-740 - -420) * ease
          )
        };
      } else if (p <= 0.76) {
        // Stage 4: PORTFOLIO ARCHIVES ARRIVAL (Z: -540 -> -840)
        const t = (p - 0.58) / 0.18;
        const ease = t * t * (3 - 2 * t);
        return {
          pos: new THREE.Vector3(
            -12 + (6 - -12) * ease,
            6 + (10 - 6) * ease,
            -540 + (-840 - -540) * ease
          ),
          look: new THREE.Vector3(
            -8 + (2 - -8) * ease,
            6 + (8 - 6) * ease,
            -740 + (-1060 - -740) * ease
          )
        };
      } else if (p <= 0.88) {
        // Stage 5: ECOSYSTEM PHILOSOPHY & VISION (Z: -840 -> -1120)
        const t = (p - 0.76) / 0.12;
        const ease = t * t * (3 - 2 * t);
        return {
          pos: new THREE.Vector3(
            6 + (-2 - 6) * ease,
            10 + (8 - 10) * ease,
            -840 + (-1120 - -840) * ease
          ),
          look: new THREE.Vector3(
            2 + (0 - 2) * ease,
            8 + (8 - 8) * ease,
            -1060 + (-1320 - -1060) * ease
          )
        };
      } else {
        // Stage 6: TRANSMISSION TERMINAL (Z: -1120 -> -1420)
        const t = (p - 0.88) / 0.12;
        const ease = t * t * (3 - 2 * t);
        return {
          pos: new THREE.Vector3(
            -2 + (0 - -2) * ease,
            8 + (4 - 8) * ease,
            -1120 + (-1420 - -1120) * ease
          ),
          look: new THREE.Vector3(
            0,
            8 + (4 - 8) * ease,
            -1320 + (-1600 - -1320) * ease
          )
        };
      }
    }

    function animateUniverseCinematic() {
      requestAnimationFrame(animateUniverseCinematic);

      const elapsed = clock.getElapsedTime();

      // Smooth mouse spring damping
      mouse.x += (mouse.targetX - mouse.x) * 0.04;
      mouse.y += (mouse.targetY - mouse.y) * 0.04;

      if (!isZoomingTransition) {
        const targetTrajectory = getCameraTrajectory(targetScrollP);
        currentCamPos.lerp(targetTrajectory.pos, 0.055);
        currentLookAt.lerp(targetTrajectory.look, 0.055);

        // Hyperspace cosmic turbulence during high-speed travel
        const warpShake = Math.min(0.35, Math.abs(smoothedScrollVelocity) * 0.012);
        const shakeX = (Math.random() - 0.5) * warpShake;
        const shakeY = (Math.random() - 0.5) * warpShake;

        camera.position.set(
          currentCamPos.x + mouse.x * 4.0 + shakeX,
          currentCamPos.y + mouse.y * 3.0 + shakeY,
          currentCamPos.z
        );
        camera.lookAt(
          currentLookAt.x + mouse.x * 1.5,
          currentLookAt.y + mouse.y * 1.0,
          currentLookAt.z
        );
      }

      // Milky Way organic slow rotation
      if (milkyWayGroup) {
        milkyWayGroup.rotation.z += 0.00035 * warpSpeedFactor;
      }

      // Atmospheric nebula breathing
      nebulaPuffs.forEach(np => {
        const pulse = 1.0 + 0.06 * Math.sin(elapsed * 0.5 + np.seed);
        np.sprite.scale.set(np.baseScale * pulse, np.baseScale * pulse, 1);
      });

      // Smooth exponential velocity damping
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

      // Core Universe Halo rotation & visibility
      if (globeGroup) {
        globeGroup.rotation.y += 0.0012 * effectiveWarpFactor;
        globeGroup.visible = (camera.position.z > 30);
      }

      // Animate Spatial Destinations & Toggle Visibility based on scroll journey
      if (builderSpatialHalo) {
        builderSpatialHalo.visible = (targetScrollP > 0.35 && targetScrollP < 0.72);
        if (builderSpatialHalo.visible) builderSpatialHalo.rotation.z += 0.0015;
      }
      if (builderEmbersPoints) {
        builderEmbersPoints.visible = (targetScrollP > 0.35 && targetScrollP < 0.72);
        if (builderEmbersPoints.visible) builderEmbersPoints.rotation.z -= 0.0008;
      }
      if (portfolioConstellationGroup) {
        portfolioConstellationGroup.visible = (targetScrollP > 0.55 && targetScrollP < 0.88);
        if (portfolioConstellationGroup.visible) portfolioConstellationGroup.rotation.y = Math.sin(elapsed * 0.3) * 0.06;
      }
      if (transmissionBeaconGroup) {
        transmissionBeaconGroup.visible = (targetScrollP > 0.75);
        if (transmissionBeaconGroup.visible) {
          const pulse = 1.0 + 0.08 * Math.sin(elapsed * 2.5);
          transmissionBeaconGroup.children.forEach((c, idx) => {
            if (c.geometry && c.geometry.type === 'CylinderGeometry') {
              c.scale.set(pulse, 1, pulse);
            } else {
              c.rotation.z += 0.001 * (idx % 2 === 0 ? 1 : -1);
            }
          });
        }
      }

      // 4 Orbital Product Worlds Animation (Dynamic Spatial Journey)
      // Constellation center travels from Core (Z: 0) to Products Destination (Z: -210)
      const cP = Math.min(1, Math.max(0, (targetScrollP - 0.05) / 0.25));
      const cEase = cP * cP * (3 - 2 * cP);
      const constCenterX = globeCenterX + (0 - globeCenterX) * cEase;
      const constCenterY = globeCenterY + (8 - globeCenterY) * cEase;
      const constCenterZ = globeCenterZ + (-210 - globeCenterZ) * cEase;
      const orbitScale = 1.0 + 0.45 * cEase; // Expands outward as user arrives at Products!

      if (productWorldsGroup) productWorldsGroup.visible = (targetScrollP > 0.08 && targetScrollP < 0.55);
      productWorlds.forEach((pw) => {
        if (pw.pathLine) {
          pw.pathLine.position.set(constCenterX, constCenterY, constCenterZ);
          pw.pathLine.scale.set(orbitScale, orbitScale, orbitScale);
        }
        pw.progress = (pw.progress + pw.speed * effectiveWarpFactor + 1) % 1;
        const pt = pw.curve.getPoint(pw.progress);
        const v = new THREE.Vector3(pt.x * orbitScale, pt.y * orbitScale, 0);
        v.applyEuler(new THREE.Euler(pw.config.inclinationX, pw.config.inclinationY, pw.config.inclinationZ));
        pw.group.position.set(constCenterX + v.x, constCenterY + v.y, constCenterZ + v.z);

        // Micro photon moon orbiting the planet
        if (pw.moon) {
          const mAngle = elapsed * 3.0 + pw.config.startProgress * 10;
          const mR = pw.config.sphereSize * 1.8;
          pw.moon.position.set(Math.cos(mAngle) * mR, Math.sin(mAngle * 0.8) * 0.8, Math.sin(mAngle) * mR);
        }
      });

      // Core halo breathing
      if (globeHaloSprite) {
        const hPulse = 1.0 + 0.05 * Math.sin(elapsed * 2.0);
        globeHaloSprite.scale.set(72 * hPulse, 72 * hPulse, 1);
      }

      // Distant galaxies rotation
      if (distantGalaxiesGroup) {
        distantGalaxiesGroup.children.forEach((g) => {
          g.rotation.z += 0.00015;
        });
      }

      // Raycasting Hover Detection
      if (!isZoomingTransition && camera && productHitTargets.length > 0) {
        raycaster.setFromCamera(mouseRay, camera);
        const intersects = raycaster.intersectObjects(productHitTargets);

        if (intersects.length > 0) {
          const hit = intersects[0].object;
          if (hoveredProduct !== hit) {
            if (hoveredProduct && hoveredProduct.userData && hoveredProduct.userData.group) {
              hoveredProduct.userData.group.scale.set(1, 1, 1);
              if (hoveredProduct.userData.pathLine) hoveredProduct.userData.pathLine.material.opacity = 0.22;
            }
            hoveredProduct = hit;
            if (hit.userData && hit.userData.group) {
              hit.userData.group.scale.set(1.25, 1.25, 1.25);
              if (hit.userData.pathLine) hit.userData.pathLine.material.opacity = 0.65;
            }
            canvas.style.cursor = 'pointer';
            if (tooltipEl) {
              pwtNameEl.innerText = hit.userData.name;
              pwtTaglineEl.innerText = hit.userData.tagline;
              pwtDotEl.style.background = hit.userData.color;
              pwtDotEl.style.boxShadow = `0 0 10px ${hit.userData.color}`;
              tooltipEl.style.display = 'flex';
              tooltipEl.style.opacity = '1';
            }
          }
        } else {
          if (hoveredProduct) {
            if (hoveredProduct.userData && hoveredProduct.userData.group) {
              hoveredProduct.userData.group.scale.set(1, 1, 1);
              if (hoveredProduct.userData.pathLine) hoveredProduct.userData.pathLine.material.opacity = 0.22;
            }
            hoveredProduct = null;
            canvas.style.cursor = 'default';
            if (tooltipEl) {
              tooltipEl.style.opacity = '0';
              setTimeout(() => { if (!hoveredProduct) tooltipEl.style.display = 'none'; }, 200);
            }
          }
        }
      }

      renderer.render(scene, camera);
    }

    window.addEventListener('resize', () => {
      if (!isWebGLEnabled || !renderer) return;
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    });

    /* -------------------------------------------------------------
       13B. REAL-TIME SPACE-TRAVEL SCROLL & VELOCITY CONTROLLER
       ------------------------------------------------------------- */
    let lastTrackedScrollY = window.scrollY || 0;
    let lastTrackedTime = performance.now();

    function updateActiveNavLink(p) {
      const navLinks = document.querySelectorAll('.nav-links .nav-link');
      if (!navLinks.length) return;
      let activeId = '#hero';
      if (p >= 0.92) activeId = '#contact';
      else if (p >= 0.86) activeId = '#folivio';
      else if (p >= 0.76) activeId = '#vision';
      else if (p >= 0.58) activeId = '#portfolio';
      else if (p >= 0.38) activeId = '#about';
      else if (p >= 0.15) activeId = '#products';

      navLinks.forEach(link => {
        if (link.getAttribute('href') === activeId) {
          link.classList.add('active');
        } else {
          link.classList.remove('active');
        }
      });
    }

    function handleScrollTravelUpdate(scrollY, maxScroll, velocity) {
      if (maxScroll <= 0) {
        targetScrollP = 0;
      } else {
        targetScrollP = Math.min(1.0, Math.max(0.0, scrollY / maxScroll));
      }

      if (typeof velocity === 'number' && !isNaN(velocity)) {
        rawScrollVelocity = Math.max(-55, Math.min(55, velocity * 0.85));
      }

      // 1. Dynamic Hero Perspective Exit during space travel
      const heroContent = document.querySelector('.hero-content');
      const heroIndicator = document.querySelector('.hero-scroll-indicator');
      if (heroContent) {
        const heroAlpha = Math.max(0, 1.0 - targetScrollP * 6.5);
        heroContent.style.opacity = heroAlpha;
        heroContent.style.transform = `translate3d(0, ${-targetScrollP * 140}px, 0) scale(${1.0 + targetScrollP * 0.12})`;
        heroContent.style.pointerEvents = targetScrollP > 0.08 ? 'none' : 'auto';
      }
      if (heroIndicator) {
        heroIndicator.style.opacity = Math.max(0, 1.0 - targetScrollP * 16.0);
        heroIndicator.style.pointerEvents = targetScrollP > 0.03 ? 'none' : 'auto';
      }

      updateActiveNavLink(targetScrollP);
    }

    // Lenis Smooth Scroll binding
    if (lenis) {
      lenis.on('scroll', (e) => {
        const limit = e.limit || (document.documentElement.scrollHeight - window.innerHeight);
        handleScrollTravelUpdate(e.scroll, limit, e.velocity);
      });
    }

    // Native scroll event listener (fallback and instant sync)
    window.addEventListener('scroll', () => {
      const scrollY = window.scrollY || window.pageYOffset || 0;
      const maxScroll = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
      const now = performance.now();
      const dt = Math.max(8, now - lastTrackedTime);
      const dy = scrollY - lastTrackedScrollY;
      const calcVel = (dy / dt) * 16.0;

      handleScrollTravelUpdate(scrollY, maxScroll, calcVel);
      lastTrackedScrollY = scrollY;
      lastTrackedTime = now;
    }, { passive: true });

    // Smooth navigation clicks to space destinations
    document.querySelectorAll('.nav-links a, .nav-brand').forEach(anchor => {
      anchor.addEventListener('click', (e) => {
        const href = anchor.getAttribute('href');
        if (href && href.startsWith('#')) {
          const target = document.querySelector(href);
          if (target) {
            e.preventDefault();
            if (lenis) {
              lenis.scrollTo(target, { duration: 1.5 });
            } else {
              target.scrollIntoView({ behavior: 'smooth' });
            }
          }
        }
      });
    });

    /* -------------------------------------------------------------
       14. CINEMATIC INTRO SEQUENCE (UNDER 3 SECONDS)
       ------------------------------------------------------------- */
    function runCinematicIntro() {
      const heroContent = document.querySelector('.hero-content');
      if (heroContent) {
        heroContent.style.opacity = '1';
        heroContent.style.transform = 'translateY(0)';
      }
      canvas.style.opacity = '1';
    }

    /* -------------------------------------------------------------
       15. INTERACTIVE SPACE-TRAVEL FLIGHT SEQUENCES
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
            if (lenis) {
              lenis.scrollTo(target, { duration: 1.5 });
            } else {
              target.scrollIntoView({ behavior: 'smooth' });
            }
          }
        }
      }
      requestAnimationFrame(warpStep);
    }

    function triggerExploreProductsFlight() {
      if (isZoomingTransition) return;
      isZoomingTransition = true;

      // Accelerated camera travel towards product constellation
      rawScrollVelocity = 28;

      const targetElem = document.getElementById('products');
      if (targetElem) {
        if (lenis) {
          lenis.scrollTo(targetElem, { duration: 1.5 });
        } else {
          targetElem.scrollIntoView({ behavior: 'smooth' });
        }
      }

      setTimeout(() => {
        isZoomingTransition = false;
      }, 1200);
    }

    function triggerCinematicCameraZoom() {
      triggerEnterUniverseSequence();
    }

    /* -------------------------------------------------------------
       16. HIGH-PERFORMANCE 2D PROCEDURAL CANVAS FALLBACK
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
