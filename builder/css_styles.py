# builder/css_styles.py

CSS_CONTENT = """
    /* =========================================================
       NIVORA CORE DESIGN SYSTEM — CINEMATIC LUXURY & PRECISION
       ========================================================= */
    :root {
      --bg: #04050b;
      --bg-alt: #080914;
      --surface: rgba(14, 15, 30, 0.72);
      --surface-hover: rgba(22, 24, 46, 0.85);
      --border: rgba(255, 255, 255, 0.10);
      --border-focus: rgba(168, 102, 255, 0.45);
      --text: #f7f7ff;
      --text-muted: #9fa2b8;
      --text-dim: #71748a;
      
      --purple: #9d5cff;
      --purple-glow: rgba(157, 92, 255, 0.28);
      --cyan: #21d9ff;
      --cyan-glow: rgba(33, 217, 255, 0.24);
      --blue: #4b8cff;
      --pink: #ec6dff;
      --emerald: #24d8a7;
      
      --font-stack: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      --radius-sm: 10px;
      --radius-md: 16px;
      --radius-lg: 24px;
      --radius-xl: 32px;
      --shadow-ambient: 0 30px 90px rgba(0, 0, 0, 0.48);
      --transition-smooth: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
      background: var(--bg);
      color-scheme: dark;
    }

    body {
      font-family: var(--font-stack);
      background-color: var(--bg);
      background-image: 
        radial-gradient(ellipse 70% 55% at 68% 8%, rgba(138, 73, 255, 0.18), transparent 60%),
        radial-gradient(ellipse 55% 45% at 18% 32%, rgba(28, 209, 255, 0.08), transparent 60%),
        radial-gradient(ellipse 65% 50% at 82% 70%, rgba(95, 60, 255, 0.10), transparent 65%),
        radial-gradient(ellipse 50% 40% at 20% 90%, rgba(36, 216, 167, 0.06), transparent 60%);
      color: var(--text);
      overflow-x: hidden;
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    /* Ambient Subtle Grid */
    body::before {
      content: "";
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: -3;
      background-image:
        linear-gradient(rgba(140, 110, 255, 0.025) 1px, transparent 1px),
        linear-gradient(90deg, rgba(140, 110, 255, 0.025) 1px, transparent 1px);
      background-size: 72px 72px;
      mask-image: radial-gradient(circle at 50% 40%, black 30%, transparent 85%);
      -webkit-mask-image: radial-gradient(circle at 50% 40%, black 30%, transparent 85%);
    }

    /* Cinematic Film Grain */
    .noise {
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 99;
      opacity: 0.025;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 180 180' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.7'/%3E%3C/svg%3E");
    }

    /* Interactive Background Stars Canvas */
    #stars {
      position: fixed;
      inset: 0;
      width: 100%;
      height: 100%;
      z-index: -4;
      pointer-events: none;
      opacity: 0.85;
    }

    /* Interactive Radial Cursor Glow */
    .cursor-glow {
      position: fixed;
      width: 380px;
      height: 380px;
      border-radius: 50%;
      pointer-events: none;
      z-index: -2;
      transform: translate(-50%, -50%);
      background: radial-gradient(circle, rgba(140, 85, 255, 0.08), transparent 70%);
      filter: blur(12px);
      transition: opacity 0.5s ease;
    }

    /* Scroll progress indicator */
    .scroll-progress {
      position: fixed;
      left: 0;
      top: 0;
      width: 0%;
      height: 2.5px;
      z-index: 100;
      background: linear-gradient(90deg, #9d5cff, #ec6dff 40%, #21d9ff 85%, #24d8a7);
      box-shadow: 0 0 16px rgba(157, 92, 255, 0.8);
    }

    /* Common typography and layout */
    a {
      color: inherit;
      text-decoration: none;
      outline: none;
    }

    a:focus-visible, button:focus-visible, input:focus-visible, textarea:focus-visible, select:focus-visible {
      outline: 2px solid var(--purple);
      outline-offset: 3px;
    }

    button {
      background: none;
      border: 0;
      font-family: inherit;
      cursor: pointer;
      color: inherit;
    }

    .container {
      width: min(1240px, 92vw);
      margin-inline: auto;
    }

    .section {
      padding: 120px 0;
      position: relative;
    }

    .section-divider {
      position: absolute;
      top: 0;
      left: 50%;
      transform: translateX(-50%);
      width: min(980px, 80vw);
      height: 1px;
      background: linear-gradient(90deg, transparent, rgba(160, 100, 255, 0.16), rgba(33, 217, 255, 0.12), transparent);
      pointer-events: none;
    }

    .section-head {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      gap: 36px;
      margin-bottom: 56px;
    }

    .kicker {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: var(--purple);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .kicker::before {
      content: "";
      display: inline-block;
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--purple);
      box-shadow: 0 0 10px var(--purple);
    }

    .section h2 {
      font-size: clamp(34px, 4.4vw, 56px);
      line-height: 1.05;
      letter-spacing: -0.04em;
      font-weight: 850;
    }

    .section-head p {
      max-width: 460px;
      color: var(--text-muted);
      font-size: 14px;
      line-height: 1.75;
    }

    .grad {
      background: linear-gradient(105deg, #ffffff 0%, #e2d7ff 32%, #a567ff 65%, #35ddff 100%);
      -webkit-background-clip: text;
      background-clip: text;
      -webkit-text-fill-color: transparent;
      color: transparent;
      display: inline-block;
    }

    /* Buttons */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      padding: 13px 22px;
      border-radius: var(--radius-md);
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.02em;
      transition: var(--transition-smooth);
      position: relative;
      overflow: hidden;
      cursor: pointer;
      border: 1px solid rgba(255, 255, 255, 0.12);
      white-space: nowrap;
    }

    .btn::after {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(110deg, transparent 25%, rgba(255, 255, 255, 0.22) 50%, transparent 75%);
      transform: translateX(-120%);
      transition: transform 0.65s ease;
      pointer-events: none;
    }

    .btn:hover::after {
      transform: translateX(120%);
    }

    .btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 14px 34px rgba(0, 0, 0, 0.35);
    }

    .btn.primary {
      background: linear-gradient(105deg, #9a4dff, #cf62ff 48%, #21d9ff);
      color: #ffffff;
      border: 0;
      box-shadow: 0 12px 36px rgba(154, 77, 255, 0.30), 0 0 24px rgba(33, 217, 255, 0.15);
    }

    .btn.primary:hover {
      box-shadow: 0 16px 44px rgba(154, 77, 255, 0.42), 0 0 30px rgba(33, 217, 255, 0.22);
    }

    .btn.secondary {
      background: rgba(255, 255, 255, 0.04);
      color: var(--text);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
    }

    .btn.secondary:hover {
      background: rgba(255, 255, 255, 0.08);
      border-color: rgba(255, 255, 255, 0.22);
    }

    .btn-arrow {
      transition: transform 0.25s ease;
    }

    .btn:hover .btn-arrow {
      transform: translateX(4px);
    }

    /* =========================================================
       NAVIGATION BAR WITH DROPDOWN
       ========================================================= */
    .topbar {
      position: fixed;
      top: 18px;
      left: 50%;
      transform: translateX(-50%);
      width: min(1180px, calc(100vw - 24px));
      max-width: 100%;
      box-sizing: border-box;
      z-index: 50;
      border: 1px solid rgba(190, 145, 255, 0.18);
      background: rgba(8, 9, 20, 0.76);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border-radius: 22px;
      box-shadow: 0 18px 60px rgba(0, 0, 0, 0.38), inset 0 1px 0 rgba(255, 255, 255, 0.08);
      transition: var(--transition-smooth);
    }

    .nav {
      height: 68px;
      padding: 0 12px 0 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
      font-weight: 850;
      letter-spacing: 0.10em;
    }

    .brand img {
      width: 40px;
      height: 40px;
      object-fit: contain;
      filter: drop-shadow(0 0 14px rgba(157, 92, 255, 0.65));
      transition: transform 0.3s ease;
    }

    .brand:hover img {
      transform: scale(1.06);
    }

    .brand-text span {
      font-size: 17px;
      font-weight: 850;
      color: #ffffff;
      letter-spacing: 0.08em;
    }

    .brand-text small {
      display: block;
      color: var(--text-dim);
      font-size: 8.5px;
      letter-spacing: 0.22em;
      margin-top: -2px;
      font-weight: 700;
      text-transform: uppercase;
    }

    .navlinks {
      display: flex;
      align-items: center;
      gap: 3px;
    }

    .navlinks a, .navlinks .nav-dropdown-trigger {
      font-size: 13px;
      font-weight: 600;
      color: #c4c6db;
      padding: 10px 13px;
      border-radius: 12px;
      transition: var(--transition-smooth);
      display: inline-flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
    }

    .navlinks a:hover, .navlinks a.active, .navlinks .nav-dropdown:hover .nav-dropdown-trigger {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.08);
    }

    .nav-dropdown {
      position: relative;
    }

    .nav-dropdown-menu {
      position: absolute;
      top: calc(100% + 8px);
      left: 50%;
      transform: translateX(-50%) translateY(8px);
      min-width: 240px;
      background: rgba(8, 9, 22, 0.96);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: var(--radius-md);
      padding: 8px;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.6), 0 0 30px rgba(157, 92, 255, 0.12);
      opacity: 0;
      pointer-events: none;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 100;
    }

    .nav-dropdown:hover .nav-dropdown-menu,
    .nav-dropdown:focus-within .nav-dropdown-menu {
      opacity: 1;
      pointer-events: auto;
      transform: translateX(-50%) translateY(0);
    }

    .nav-dropdown-item {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 9px 12px;
      border-radius: 10px;
      color: #c4c6db !important;
      font-size: 12.5px;
      font-weight: 600;
      transition: var(--transition-smooth);
    }

    .nav-dropdown-item:hover {
      color: #ffffff !important;
      background: rgba(255, 255, 255, 0.08);
    }

    .nav-dropdown-item img {
      width: 24px;
      height: 24px;
      object-fit: contain;
    }

    .nav-dropdown-item span small {
      display: block;
      color: var(--text-dim);
      font-size: 10px;
      font-weight: 500;
      margin-top: 1px;
    }

    .nav-cta {
      padding: 10px 18px !important;
      color: #ffffff !important;
      border: 1px solid rgba(190, 120, 255, 0.5) !important;
      background: linear-gradient(100deg, rgba(157, 92, 255, 0.32), rgba(33, 217, 255, 0.18)) !important;
      box-shadow: 0 0 20px rgba(157, 92, 255, 0.20);
      margin-left: 6px;
    }

    .nav-cta:hover {
      background: linear-gradient(100deg, rgba(157, 92, 255, 0.50), rgba(33, 217, 255, 0.30)) !important;
      border-color: rgba(200, 140, 255, 0.75) !important;
      box-shadow: 0 0 30px rgba(157, 92, 255, 0.35);
    }

    .menu-toggle {
      display: none;
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.10);
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 5px;
      cursor: pointer;
      z-index: 60;
    }

    .menu-toggle span {
      display: block;
      width: 20px;
      height: 2px;
      background: #ffffff;
      border-radius: 2px;
      transition: var(--transition-smooth);
    }

    .menu-toggle.open span:nth-child(1) {
      transform: translateY(7px) rotate(45deg);
    }
    .menu-toggle.open span:nth-child(2) {
      opacity: 0;
      transform: scaleX(0);
    }
    .menu-toggle.open span:nth-child(3) {
      transform: translateY(-7px) rotate(-45deg);
    }

    /* Mobile Drawer */
    .mobile-drawer {
      position: fixed;
      inset: 0;
      background: rgba(5, 6, 15, 0.98);
      backdrop-filter: blur(28px);
      -webkit-backdrop-filter: blur(28px);
      z-index: 55;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      gap: 16px;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.35s ease, transform 0.35s ease;
      transform: translateY(-10px);
      overflow-y: auto;
      padding: 40px 20px;
    }

    .mobile-drawer.open {
      opacity: 1;
      pointer-events: auto;
      transform: translateY(0);
    }

    .mobile-drawer a {
      font-size: 18px;
      font-weight: 700;
      color: #c4c6db;
      padding: 6px 20px;
      border-radius: 14px;
      transition: var(--transition-smooth);
    }

    .mobile-drawer a:hover, .mobile-drawer a.active {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.08);
    }

    .mobile-product-sublinks {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      justify-content: center;
      margin: 4px 0 10px;
    }

    .mobile-product-sublinks a {
      font-size: 13px !important;
      padding: 6px 12px !important;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
    }

    /* =========================================================
       HERO SECTION
       ========================================================= */
    .hero {
      min-height: 100vh;
      display: grid;
      align-items: center;
      padding: 160px 0 90px;
      position: relative;
      isolation: isolate;
      overflow: hidden;
    }

    .hero-glow-orbit {
      position: absolute;
      width: 720px;
      height: 720px;
      right: -120px;
      top: 50%;
      transform: translateY(-50%);
      border-radius: 50%;
      background: radial-gradient(circle, rgba(138, 73, 255, 0.16) 0%, rgba(33, 217, 255, 0.06) 40%, transparent 70%);
      filter: blur(24px);
      pointer-events: none;
      z-index: -1;
    }

    .hero-grid {
      display: grid;
      grid-template-columns: 1.05fr 0.95fr;
      gap: 36px;
      align-items: center;
    }

    .eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      border: 1px solid rgba(190, 126, 255, 0.35);
      background: linear-gradient(90deg, rgba(140, 70, 255, 0.16), rgba(33, 217, 255, 0.08));
      padding: 8px 16px;
      border-radius: 999px;
      color: #e5d7ff;
      font-size: 11px;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      font-weight: 650;
      box-shadow: 0 0 25px rgba(157, 92, 255, 0.14);
    }

    .eyebrow i {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--purple);
      box-shadow: 0 0 12px var(--purple);
    }

    .hero h1 {
      font-size: clamp(54px, 6.8vw, 92px);
      line-height: 0.94;
      letter-spacing: -0.055em;
      margin: 24px 0 16px;
      font-weight: 850;
      color: #ffffff;
      text-wrap: balance;
    }

    .hero-tagline-badge {
      display: inline-block;
      font-size: clamp(16px, 2vw, 21px);
      font-weight: 750;
      letter-spacing: -0.01em;
      color: #dcd7ff;
      margin-bottom: 20px;
    }

    .hero-tagline-badge span {
      color: var(--cyan);
    }

    .hero-copy {
      max-width: 620px;
      color: var(--text-muted);
      font-size: 16px;
      line-height: 1.8;
    }

    .hero-copy strong {
      color: #ffffff;
      font-weight: 650;
    }

    .hero-actions {
      display: flex;
      gap: 14px;
      flex-wrap: wrap;
      margin-top: 34px;
    }

    .hero-meta {
      display: flex;
      gap: 34px;
      margin-top: 44px;
      padding-top: 28px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      color: var(--text-dim);
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.16em;
      font-weight: 600;
    }

    .hero-meta > div {
      position: relative;
    }

    .hero-meta strong {
      display: block;
      font-size: 24px;
      letter-spacing: 0;
      text-transform: none;
      margin-bottom: 2px;
      font-weight: 850;
      background: linear-gradient(100deg, #ffffff, #cfbbfb, #43ddff);
      -webkit-background-clip: text;
      background-clip: text;
      -webkit-text-fill-color: transparent;
      color: transparent;
    }

    /* Hero Art: Planetary Central Universe */
    .hero-art {
      position: relative;
      min-height: 600px;
      display: grid;
      place-items: center;
      transform-style: preserve-3d;
    }

    .hero-art::before {
      content: "";
      position: absolute;
      width: 580px;
      height: 580px;
      border-radius: 50%;
      border: 1px solid rgba(157, 92, 255, 0.16);
      box-shadow: 0 0 100px rgba(138, 73, 255, 0.12), inset 0 0 100px rgba(33, 217, 255, 0.05);
      animation: spinSlow 36s linear infinite;
    }

    .hero-art::after {
      content: "";
      position: absolute;
      width: 440px;
      height: 440px;
      border-radius: 50%;
      border: 1px dashed rgba(33, 217, 255, 0.20);
      animation: spinReverse 24s linear infinite;
    }

    .orbit {
      position: absolute;
      border: 1px solid rgba(157, 92, 255, 0.15);
      border-radius: 50%;
      transform: rotateX(68deg);
      box-shadow: 0 0 70px rgba(138, 73, 255, 0.08);
    }
    .orbit.o1 { width: 560px; height: 560px; }
    .orbit.o2 { width: 420px; height: 420px; }
    .orbit.o3 { width: 300px; height: 300px; }

    .core {
      width: 350px;
      height: 350px;
      border-radius: 50%;
      display: grid;
      place-items: center;
      position: relative;
      background: radial-gradient(circle at 50% 30%, rgba(65, 48, 120, 0.90), rgba(7, 8, 20, 0.98) 65%);
      border: 1px solid rgba(255, 255, 255, 0.16);
      box-shadow:
        inset 0 0 90px rgba(157, 92, 255, 0.24),
        inset 0 0 35px rgba(33, 217, 255, 0.10),
        0 0 90px rgba(138, 73, 255, 0.25),
        0 25px 80px rgba(0, 0, 0, 0.6);
      animation: floatSmooth 6s ease-in-out infinite;
      z-index: 3;
    }

    .core::before {
      content: "";
      position: absolute;
      inset: -2px;
      border-radius: 50%;
      padding: 2px;
      background: conic-gradient(from 20deg, transparent, #9d5cff, #21d9ff, transparent 70%);
      -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
      -webkit-mask-composite: xor;
      mask-composite: exclude;
      animation: spinSlow 9s linear infinite;
    }

    .core img {
      width: 240px;
      height: 240px;
      object-fit: contain;
      filter: drop-shadow(0 0 28px rgba(157, 92, 255, 0.65)) drop-shadow(0 0 50px rgba(33, 217, 255, 0.20));
      z-index: 2;
    }

    .core-label {
      position: absolute;
      bottom: 28px;
      text-align: center;
      z-index: 3;
    }

    .core-label b {
      display: block;
      font-size: 19px;
      letter-spacing: 0.24em;
      color: #ffffff;
      text-shadow: 0 0 20px rgba(168, 102, 255, 0.4);
    }

    .core-label span {
      font-size: 9px;
      color: #9ea1b8;
      letter-spacing: 0.20em;
      text-transform: uppercase;
    }

    .satellite {
      position: absolute;
      width: 104px;
      height: 104px;
      border-radius: 26px;
      background: linear-gradient(145deg, rgba(20, 20, 42, 0.88), rgba(7, 8, 18, 0.92));
      border: 1px solid rgba(255, 255, 255, 0.16);
      display: grid;
      place-items: center;
      box-shadow: 0 18px 45px rgba(0, 0, 0, 0.5), 0 0 30px rgba(157, 92, 255, 0.18);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      animation: floatSmooth 5.2s ease-in-out infinite;
      z-index: 4;
      transition: transform 0.3s ease, border-color 0.3s ease;
    }

    .satellite:hover {
      transform: scale(1.08) translateY(-4px) !important;
      border-color: rgba(190, 140, 255, 0.5);
    }

    .satellite img {
      max-width: 82px;
      max-height: 82px;
      object-fit: contain;
      border-radius: 18px;
      filter: drop-shadow(0 0 12px rgba(157, 92, 255, 0.3));
    }

    .satellite::after {
      position: absolute;
      bottom: -22px;
      left: 50%;
      transform: translateX(-50%);
      font-size: 8.5px;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #9da1ba;
      white-space: nowrap;
      font-weight: 700;
    }

    .s-checkra { top: 38px; right: 50px; }
    .s-checkra::after { content: "CHECKRA"; }

    .s-homora { bottom: 75px; left: 35px; animation-delay: -1.8s; }
    .s-homora::after { content: "HOMORA"; }

    .s-bubora { top: 190px; left: 10px; animation-delay: -3.2s; }
    .s-bubora::after { content: "BUBORA"; }

    .s-sayora { bottom: 65px; right: 30px; animation-delay: -2.4s; }
    .s-sayora::after { content: "SAYORA"; }

    .hero-star {
      position: absolute;
      color: #ffffff;
      font-size: 22px;
      text-shadow: 0 0 20px #c178ff;
      animation: pulseStar 2.8s ease-in-out infinite;
      pointer-events: none;
    }
    .hero-star.a { top: 60px; left: 55px; }
    .hero-star.b { right: 18px; bottom: 130px; font-size: 15px; animation-delay: 1.2s; }

    /* =========================================================
       PRODUCT UNIVERSE OVERVIEW SECTION (#products)
       ========================================================= */
    .worlds-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 26px;
    }

    .world-card {
      min-height: 540px;
      border: 1px solid rgba(255, 255, 255, 0.11);
      border-radius: var(--radius-xl);
      overflow: hidden;
      position: relative;
      background: #080913;
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease, box-shadow 0.4s ease;
      box-shadow: 0 24px 70px rgba(0, 0, 0, 0.32);
      display: flex;
      flex-direction: column;
    }

    .world-card:hover {
      transform: translateY(-8px);
      border-color: rgba(255, 255, 255, 0.24);
      box-shadow: 0 32px 90px rgba(0, 0, 0, 0.48);
    }

    .world-card::before {
      content: "";
      position: absolute;
      inset: 0;
      border-radius: inherit;
      padding: 1px;
      background: linear-gradient(135deg, rgba(255, 255, 255, 0.16), transparent 30%, rgba(157, 92, 255, 0.18), transparent 70%, rgba(33, 217, 255, 0.14));
      -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
      -webkit-mask-composite: xor;
      mask-composite: exclude;
      pointer-events: none;
    }

    .world-media {
      height: 270px;
      position: relative;
      overflow: hidden;
      display: grid;
      place-items: center;
      padding: 24px;
    }

    .world-media::after {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, transparent 40%, rgba(8, 9, 19, 0.70) 80%, rgba(8, 9, 19, 0.98) 100%);
      pointer-events: none;
    }

    .world-media img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      object-position: center;
      transition: transform 0.7s cubic-bezier(0.16, 1, 0.3, 1), filter 0.7s ease;
      filter: drop-shadow(0 16px 36px rgba(0, 0, 0, 0.5));
      position: relative;
      z-index: 1;
    }

    .world-card:hover .world-media img {
      transform: scale(1.05);
    }

    .w-checkra .world-media {
      background:
        radial-gradient(circle at 50% 40%, rgba(165, 85, 255, 0.24), transparent 45%),
        linear-gradient(145deg, #090714, #120921 55%, #070712);
    }
    .w-checkra {
      box-shadow: inset 0 -100px 160px rgba(157, 92, 255, 0.08), 0 24px 70px rgba(0, 0, 0, 0.32);
    }

    .w-homora .world-media {
      background:
        radial-gradient(circle at 50% 40%, rgba(28, 209, 255, 0.22), transparent 45%),
        linear-gradient(145deg, #041018, #071c26 55%, #050b12);
    }
    .w-homora {
      box-shadow: inset 0 -100px 160px rgba(33, 217, 255, 0.08), 0 24px 70px rgba(0, 0, 0, 0.32);
    }

    .w-bubora .world-media {
      background:
        radial-gradient(circle at 50% 40%, rgba(240, 108, 255, 0.22), transparent 45%),
        linear-gradient(145deg, #120713, #1e0b20 55%, #090712);
    }
    .w-bubora {
      box-shadow: inset 0 -100px 160px rgba(236, 109, 255, 0.08), 0 24px 70px rgba(0, 0, 0, 0.32);
    }

    .w-sayora .world-media {
      background:
        radial-gradient(circle at 50% 40%, rgba(36, 216, 167, 0.22), transparent 45%),
        linear-gradient(145deg, #041312, #072224 55%, #050d12);
    }
    .w-sayora {
      box-shadow: inset 0 -100px 160px rgba(36, 216, 167, 0.08), 0 24px 70px rgba(0, 0, 0, 0.32);
    }

    .world-body {
      padding: 0 32px 32px;
      margin-top: -24px;
      position: relative;
      z-index: 2;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }

    .world-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 6px;
    }

    .world-name-group {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .world h3 {
      font-size: 28px;
      letter-spacing: -0.035em;
      font-weight: 850;
      color: #ffffff;
    }

    .status-badge {
      font-size: 8.5px;
      text-transform: uppercase;
      letter-spacing: 0.16em;
      padding: 6px 10px;
      border-radius: 999px;
      font-weight: 700;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #d6d7e6;
    }

    .status-badge.live {
      border-color: rgba(36, 216, 167, 0.35);
      color: #8affd4;
      background: rgba(36, 216, 167, 0.08);
    }

    .status-badge.concept {
      border-color: rgba(33, 217, 255, 0.35);
      color: #8ee9ff;
      background: rgba(33, 217, 255, 0.08);
    }

    .status-badge.dev {
      border-color: rgba(180, 115, 255, 0.35);
      color: #d8b4ff;
      background: rgba(180, 115, 255, 0.08);
    }

    .legacy-tag {
      font-size: 8.5px;
      color: #9295aa;
      font-weight: 600;
      letter-spacing: 0.08em;
      padding: 4px 8px;
      border-radius: 6px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.06);
    }

    .world-category-tag {
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: #8f92a9;
      margin-bottom: 4px;
    }

    .world-positioning {
      color: var(--purple);
      font-size: 13.5px;
      font-weight: 750;
      letter-spacing: 0.01em;
      margin-bottom: 12px;
    }

    .w-homora .world-positioning { color: var(--cyan); }
    .w-bubora .world-positioning { color: var(--pink); }
    .w-sayora .world-positioning { color: var(--emerald); }

    .world p {
      color: var(--text-muted);
      font-size: 13px;
      line-height: 1.7;
      margin-bottom: 20px;
    }

    .capabilities-list {
      display: flex;
      flex-wrap: wrap;
      gap: 7px;
      margin-bottom: 24px;
      margin-top: auto;
    }

    .cap-pill {
      font-size: 10px;
      color: #b0b3c6;
      background: rgba(255, 255, 255, 0.035);
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 5px 9px;
      border-radius: 8px;
      font-weight: 500;
    }

    .world-footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      padding-top: 18px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      flex-wrap: wrap;
    }

    .world-link {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 13px;
      font-weight: 750;
      letter-spacing: 0.02em;
      color: #ffffff;
      transition: color 0.25s ease;
      cursor: pointer;
    }

    .world-link:hover {
      color: var(--purple);
    }

    .w-homora .world-link:hover { color: var(--cyan); }
    .w-bubora .world-link:hover { color: var(--pink); }
    .w-sayora .world-link:hover { color: var(--emerald); }

    /* =========================================================
       SECTION: ONE UNIVERSE. DIFFERENT POSSIBILITIES.
       ========================================================= */
    .universe-philosophy-card {
      padding: 56px 44px;
      border-radius: var(--radius-xl);
      border: 1px solid rgba(255, 255, 255, 0.12);
      background: linear-gradient(145deg, rgba(16, 17, 36, 0.85), rgba(7, 8, 17, 0.94));
      box-shadow: var(--shadow-ambient);
      position: relative;
      overflow: hidden;
    }

    .universe-philosophy-card::before {
      content: "";
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at 50% 10%, rgba(157, 92, 255, 0.12), transparent 45%),
                  radial-gradient(circle at 10% 80%, rgba(33, 217, 255, 0.08), transparent 35%);
      pointer-events: none;
    }

    .upc-lead {
      max-width: 800px;
      margin: 0 auto 36px;
      text-align: center;
      position: relative;
      z-index: 1;
    }

    .upc-lead p {
      color: #c5c7dc;
      font-size: 16px;
      line-height: 1.85;
    }

    .universe-conduit-line {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin: 36px 0;
      position: relative;
      z-index: 1;
    }

    .ucl-item {
      padding: 24px 20px;
      border-radius: var(--radius-md);
      background: rgba(255, 255, 255, 0.035);
      border: 1px solid rgba(255, 255, 255, 0.09);
      text-align: center;
      transition: var(--transition-smooth);
      position: relative;
      cursor: pointer;
    }

    .ucl-item:hover {
      transform: translateY(-5px);
      border-color: rgba(255, 255, 255, 0.25);
      background: rgba(255, 255, 255, 0.07);
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.4);
    }

    .ucl-theme {
      font-size: 11px;
      font-weight: 850;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      margin-bottom: 8px;
    }

    .ucl-item.t-checkra .ucl-theme { color: var(--purple); }
    .ucl-item.t-homora .ucl-theme { color: var(--cyan); }
    .ucl-item.t-bubora .ucl-theme { color: var(--pink); }
    .ucl-item.t-sayora .ucl-theme { color: var(--emerald); }

    .ucl-item b {
      display: block;
      font-size: 18px;
      color: #ffffff;
      margin-bottom: 8px;
      letter-spacing: 0.02em;
    }

    .ucl-item p {
      color: var(--text-muted);
      font-size: 12px;
      line-height: 1.6;
    }

    .upc-quote-footer {
      text-align: center;
      padding-top: 32px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      position: relative;
      z-index: 1;
    }

    .upc-quote-footer b {
      font-size: clamp(20px, 2.5vw, 28px);
      letter-spacing: -0.02em;
      color: #ffffff;
      display: block;
      margin-bottom: 4px;
    }

    /* =========================================================
       COMPREHENSIVE PRODUCT DEEP DIVE EXPLORER (#explore)
       ========================================================= */
    .product-tabs-wrapper {
      position: sticky;
      top: 92px;
      z-index: 35;
      margin-bottom: 44px;
      padding: 6px;
      background: rgba(10, 11, 24, 0.85);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border: 1px solid rgba(255, 255, 255, 0.14);
      border-radius: 20px;
      display: flex;
      gap: 6px;
      box-shadow: 0 16px 50px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.08);
    }

    .product-tab-btn {
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      padding: 13px 18px;
      border-radius: 14px;
      font-size: 13.5px;
      font-weight: 750;
      letter-spacing: 0.02em;
      color: var(--text-muted);
      border: 1px solid transparent;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
      background: transparent;
      white-space: nowrap;
    }

    .product-tab-btn:hover {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.05);
    }

    .product-tab-btn img {
      width: 24px;
      height: 24px;
      object-fit: contain;
      filter: drop-shadow(0 0 8px rgba(157, 92, 255, 0.3));
    }

    .product-tab-btn.active {
      color: #ffffff;
      background: linear-gradient(135deg, rgba(255, 255, 255, 0.12), rgba(255, 255, 255, 0.04));
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.15);
    }

    .product-tab-btn.tab-checkra.active {
      border-color: rgba(157, 92, 255, 0.55);
      box-shadow: 0 0 25px rgba(157, 92, 255, 0.25);
    }
    .product-tab-btn.tab-homora.active {
      border-color: rgba(33, 217, 255, 0.55);
      box-shadow: 0 0 25px rgba(33, 217, 255, 0.25);
    }
    .product-tab-btn.tab-bubora.active {
      border-color: rgba(236, 109, 255, 0.55);
      box-shadow: 0 0 25px rgba(236, 109, 255, 0.25);
    }
    .product-tab-btn.tab-sayora.active {
      border-color: rgba(36, 216, 167, 0.55);
      box-shadow: 0 0 25px rgba(36, 216, 167, 0.25);
    }

    .product-panel {
      display: none;
      animation: fadeInPanel 0.45s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    .product-panel.active {
      display: block;
    }

    @keyframes fadeInPanel {
      from { opacity: 0; transform: translateY(18px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* 10-Step Deep Dive Content Components */
    .detail-card-container {
      background: linear-gradient(145deg, rgba(14, 15, 32, 0.88), rgba(7, 8, 17, 0.96));
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: var(--radius-xl);
      padding: 50px 44px;
      box-shadow: var(--shadow-ambient);
      position: relative;
      overflow: hidden;
    }

    .detail-header-block {
      display: grid;
      grid-template-columns: 1fr 1.25fr;
      gap: 36px;
      align-items: center;
      padding-bottom: 44px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.09);
      margin-bottom: 44px;
    }

    .dhb-logo-wrap {
      width: 100%;
      height: 280px;
      border-radius: var(--radius-lg);
      display: grid;
      place-items: center;
      padding: 24px;
      position: relative;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.10);
    }

    .dhb-logo-wrap img {
      max-width: 90%;
      max-height: 90%;
      object-fit: contain;
      filter: drop-shadow(0 16px 36px rgba(0, 0, 0, 0.6));
    }

    .checkra-theme .dhb-logo-wrap {
      background: radial-gradient(circle at 50% 40%, rgba(157, 92, 255, 0.22), transparent 50%), #0a0718;
    }
    .homora-theme .dhb-logo-wrap {
      background: radial-gradient(circle at 50% 40%, rgba(33, 217, 255, 0.22), transparent 50%), #05111c;
    }
    .bubora-theme .dhb-logo-wrap {
      background: radial-gradient(circle at 50% 40%, rgba(236, 109, 255, 0.22), transparent 50%), #150918;
    }
    .sayora-theme .dhb-logo-wrap {
      background: radial-gradient(circle at 50% 40%, rgba(36, 216, 167, 0.22), transparent 50%), #061517;
    }

    .dhb-info-block .dhb-meta-row {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 12px;
      flex-wrap: wrap;
    }

    .dhb-category {
      font-size: 11px;
      font-weight: 750;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #9da1b8;
    }

    .dhb-info-block h3 {
      font-size: clamp(34px, 4vw, 52px);
      line-height: 1.02;
      letter-spacing: -0.04em;
      font-weight: 850;
      color: #ffffff;
      margin-bottom: 10px;
    }

    .dhb-positioning {
      font-size: 17px;
      font-weight: 750;
      letter-spacing: -0.01em;
      margin-bottom: 18px;
    }

    .checkra-theme .dhb-positioning { color: var(--purple); }
    .homora-theme .dhb-positioning { color: var(--cyan); }
    .bubora-theme .dhb-positioning { color: var(--pink); }
    .sayora-theme .dhb-positioning { color: var(--emerald); }

    .dhb-desc {
      color: var(--text-muted);
      font-size: 14.5px;
      line-height: 1.8;
      margin-bottom: 26px;
    }

    .dhb-actions {
      display: flex;
      gap: 14px;
      flex-wrap: wrap;
    }

    /* Problem & About 2-Column Split */
    .about-problem-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      margin-bottom: 44px;
    }

    .narrative-card {
      padding: 34px 30px;
      border-radius: var(--radius-lg);
      background: rgba(255, 255, 255, 0.028);
      border: 1px solid rgba(255, 255, 255, 0.08);
      position: relative;
    }

    .narrative-card .nc-kicker {
      font-size: 10.5px;
      font-weight: 800;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #9295ac;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .narrative-card h4 {
      font-size: 22px;
      letter-spacing: -0.03em;
      color: #ffffff;
      margin-bottom: 14px;
      line-height: 1.25;
    }

    .narrative-card p {
      color: var(--text-muted);
      font-size: 13.5px;
      line-height: 1.75;
    }

    .narrative-card.problem-highlight {
      border-color: rgba(255, 120, 150, 0.22);
      background: radial-gradient(circle at 100% 0%, rgba(255, 80, 120, 0.06), transparent 50%), rgba(255, 255, 255, 0.025);
    }

    /* Core Statement Banner */
    .core-idea-banner {
      padding: 40px 36px;
      border-radius: var(--radius-lg);
      text-align: center;
      margin-bottom: 48px;
      position: relative;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.12);
    }

    .checkra-theme .core-idea-banner {
      background: radial-gradient(circle at 50% 50%, rgba(157, 92, 255, 0.14), transparent 60%), rgba(16, 12, 34, 0.85);
      border-color: rgba(157, 92, 255, 0.3);
    }
    .homora-theme .core-idea-banner {
      background: radial-gradient(circle at 50% 50%, rgba(33, 217, 255, 0.14), transparent 60%), rgba(8, 18, 34, 0.85);
      border-color: rgba(33, 217, 255, 0.3);
    }
    .bubora-theme .core-idea-banner {
      background: radial-gradient(circle at 50% 50%, rgba(236, 109, 255, 0.14), transparent 60%), rgba(24, 10, 26, 0.85);
      border-color: rgba(236, 109, 255, 0.3);
    }
    .sayora-theme .core-idea-banner {
      background: radial-gradient(circle at 50% 50%, rgba(36, 216, 167, 0.14), transparent 60%), rgba(6, 20, 22, 0.85);
      border-color: rgba(36, 216, 167, 0.3);
    }

    .core-idea-banner blockquote {
      font-size: clamp(22px, 2.6vw, 34px);
      font-weight: 850;
      letter-spacing: -0.03em;
      line-height: 1.25;
      color: #ffffff;
      margin-bottom: 12px;
    }

    .core-idea-banner p {
      max-width: 720px;
      margin: 0 auto;
      color: var(--text-muted);
      font-size: 14px;
      line-height: 1.7;
    }

    /* Capabilities Grid */
    .capabilities-section-title {
      margin-bottom: 24px;
    }
    .capabilities-section-title h4 {
      font-size: 24px;
      letter-spacing: -0.03em;
      color: #ffffff;
      margin-bottom: 6px;
    }
    .capabilities-section-title p {
      color: var(--text-muted);
      font-size: 13.5px;
    }

    .capabilities-deep-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      margin-bottom: 48px;
    }

    .cap-deep-card {
      padding: 24px 22px;
      border-radius: var(--radius-md);
      background: rgba(255, 255, 255, 0.028);
      border: 1px solid rgba(255, 255, 255, 0.08);
      transition: var(--transition-smooth);
    }

    .cap-deep-card:hover {
      transform: translateY(-4px);
      background: rgba(255, 255, 255, 0.055);
      border-color: rgba(255, 255, 255, 0.2);
    }

    .cap-deep-card b {
      display: block;
      font-size: 15px;
      color: #ffffff;
      margin-bottom: 8px;
      letter-spacing: -0.01em;
    }

    .cap-deep-card p {
      color: var(--text-muted);
      font-size: 12px;
      line-height: 1.65;
    }

    /* Workflow Journey Rail */
    .workflow-card-block {
      padding: 34px 30px;
      border-radius: var(--radius-lg);
      background: rgba(255, 255, 255, 0.025);
      border: 1px solid rgba(255, 255, 255, 0.09);
      margin-bottom: 48px;
    }

    .workflow-card-block h4 {
      font-size: 20px;
      color: #ffffff;
      margin-bottom: 8px;
      letter-spacing: -0.02em;
    }

    .workflow-card-block p {
      color: var(--text-muted);
      font-size: 13px;
      margin-bottom: 24px;
    }

    .workflow-rail {
      display: flex;
      gap: 10px;
      overflow-x: auto;
      padding-bottom: 12px;
    }

    .wf-step {
      flex: 1;
      min-width: 140px;
      padding: 16px 14px;
      border-radius: 12px;
      background: rgba(255, 255, 255, 0.035);
      border: 1px solid rgba(255, 255, 255, 0.08);
      text-align: center;
      position: relative;
    }

    .wf-num {
      font-size: 9.5px;
      font-weight: 850;
      letter-spacing: 0.16em;
      margin-bottom: 6px;
    }

    .checkra-theme .wf-num { color: var(--purple); }
    .homora-theme .wf-num { color: var(--cyan); }
    .bubora-theme .wf-num { color: var(--pink); }
    .sayora-theme .wf-num { color: var(--emerald); }

    .wf-step b {
      font-size: 13px;
      color: #ffffff;
      display: block;
    }

    /* Intelligence & Ecosystem Model */
    .ecosystem-visual-block {
      padding: 34px 30px;
      border-radius: var(--radius-lg);
      background: linear-gradient(145deg, rgba(255, 255, 255, 0.04), rgba(255, 255, 255, 0.015));
      border: 1px solid rgba(255, 255, 255, 0.10);
      margin-bottom: 48px;
    }

    .ecosystem-visual-block h4 {
      font-size: 20px;
      color: #ffffff;
      margin-bottom: 8px;
    }

    .ecosystem-visual-block p {
      color: var(--text-muted);
      font-size: 13px;
      margin-bottom: 22px;
    }

    .eco-pill-stream {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      justify-content: center;
      margin: 18px 0;
    }

    .eco-stream-tag {
      padding: 10px 18px;
      border-radius: 999px;
      font-size: 12.5px;
      font-weight: 700;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .eco-stream-tag span {
      color: var(--text-dim);
    }

    /* Responsible Design Card */
    .responsible-design-card {
      padding: 32px 30px;
      border-radius: var(--radius-lg);
      border: 1px solid rgba(255, 255, 255, 0.12);
      background: rgba(255, 255, 255, 0.02);
      margin-bottom: 48px;
      position: relative;
    }

    .responsible-design-card .rdc-tag {
      font-size: 10px;
      font-weight: 800;
      letter-spacing: 0.20em;
      text-transform: uppercase;
      color: #ffa07a;
      margin-bottom: 10px;
      display: inline-block;
    }

    .responsible-design-card h4 {
      font-size: 20px;
      color: #ffffff;
      margin-bottom: 10px;
    }

    .responsible-design-card p {
      color: var(--text-muted);
      font-size: 13px;
      line-height: 1.75;
    }

    /* Vision & Taglines */
    .vision-tagline-block {
      display: grid;
      grid-template-columns: 1.2fr 0.8fr;
      gap: 26px;
      padding: 36px 32px;
      border-radius: var(--radius-lg);
      background: rgba(255, 255, 255, 0.035);
      border: 1px solid rgba(255, 255, 255, 0.10);
      align-items: center;
      margin-bottom: 44px;
    }

    .vtb-left h4 {
      font-size: 11px;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--purple);
      margin-bottom: 10px;
      font-weight: 800;
    }

    .vtb-left p {
      color: #ffffff;
      font-size: 16px;
      line-height: 1.7;
      font-weight: 600;
    }

    .vtb-right {
      text-align: right;
      padding-left: 20px;
      border-left: 1px solid rgba(255, 255, 255, 0.08);
    }

    .vtb-primary-tagline {
      font-size: 20px;
      font-weight: 850;
      color: #ffffff;
      letter-spacing: -0.02em;
      margin-bottom: 6px;
    }

    .vtb-secondary-tagline {
      font-size: 13px;
      color: var(--text-dim);
      font-weight: 600;
    }

    /* Cross-Navigation Footer */
    .cross-nav-footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      padding-top: 28px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      flex-wrap: wrap;
    }

    .cross-nav-links {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }

    .cross-nav-btn {
      padding: 9px 15px;
      border-radius: 10px;
      font-size: 12px;
      font-weight: 700;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: #c4c6dc;
      cursor: pointer;
      transition: var(--transition-smooth);
    }

    .cross-nav-btn:hover {
      background: rgba(255, 255, 255, 0.08);
      color: #ffffff;
      border-color: rgba(255, 255, 255, 0.2);
    }

    /* =========================================================
       ABOUT SECTION: LIFE CYCLE PIPELINE
       ========================================================= */
    .about-ecosystem {
      margin-top: 36px;
    }

    .pipeline-wrapper {
      position: relative;
      border: 1px solid rgba(255, 255, 255, 0.11);
      border-radius: var(--radius-xl);
      background: linear-gradient(145deg, rgba(16, 17, 36, 0.85), rgba(7, 8, 17, 0.94));
      padding: 48px 36px;
      box-shadow: var(--shadow-ambient);
      overflow: hidden;
    }

    .pipeline-wrapper::before {
      content: "";
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at 50% 20%, rgba(157, 92, 255, 0.10), transparent 50%),
                  radial-gradient(circle at 10% 80%, rgba(33, 217, 255, 0.07), transparent 40%);
      pointer-events: none;
    }

    .pipeline-header {
      text-align: center;
      max-width: 680px;
      margin: 0 auto 46px;
      position: relative;
      z-index: 1;
    }

    .pipeline-header h3 {
      font-size: 26px;
      letter-spacing: -0.03em;
      margin-bottom: 12px;
      color: #ffffff;
    }

    .pipeline-header p {
      color: var(--text-muted);
      font-size: 14px;
      line-height: 1.7;
    }

    .pipeline-steps {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 14px;
      position: relative;
      z-index: 1;
    }

    .pipe-step {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-md);
      padding: 24px 18px;
      transition: var(--transition-smooth);
      position: relative;
    }

    .pipe-step:hover {
      transform: translateY(-4px);
      background: rgba(255, 255, 255, 0.06);
      border-color: rgba(168, 102, 255, 0.35);
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.3);
    }

    .pipe-number {
      font-size: 10px;
      font-weight: 800;
      letter-spacing: 0.16em;
      color: var(--purple);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .pipe-step:nth-child(2) .pipe-number { color: #cf62ff; }
    .pipe-step:nth-child(3) .pipe-number { color: #4b8cff; }
    .pipe-step:nth-child(4) .pipe-number { color: #21d9ff; }
    .pipe-step:nth-child(5) .pipe-number { color: #24d8a7; }

    .pipe-step b {
      display: block;
      font-size: 17px;
      color: #ffffff;
      margin-bottom: 8px;
      letter-spacing: -0.02em;
    }

    .pipe-step p {
      color: var(--text-muted);
      font-size: 12px;
      line-height: 1.6;
    }

    /* Principles & Focus Pillars */
    .principles-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 18px;
      margin-top: 24px;
    }

    .principle-card {
      padding: 28px 24px;
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-lg);
      background: rgba(255, 255, 255, 0.025);
      transition: var(--transition-smooth);
    }

    .principle-card:hover {
      border-color: rgba(255, 255, 255, 0.18);
      background: rgba(255, 255, 255, 0.045);
      transform: translateY(-3px);
    }

    .principle-card .p-tag {
      font-size: 9.5px;
      font-weight: 750;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--cyan);
      margin-bottom: 10px;
    }

    .principle-card h4 {
      font-size: 16px;
      color: #ffffff;
      margin-bottom: 8px;
      letter-spacing: -0.02em;
    }

    .principle-card p {
      color: var(--text-muted);
      font-size: 12.5px;
      line-height: 1.65;
    }

    /* =========================================================
       FOUNDER & PORTFOLIO SECTION (#portfolio)
       ========================================================= */
    .founder-card {
      display: grid;
      grid-template-columns: 0.85fr 1.15fr;
      min-height: 560px;
      border-radius: var(--radius-xl);
      overflow: hidden;
      border: 1px solid rgba(190, 140, 255, 0.18);
      background: linear-gradient(115deg, #101020, #0a0a13 55%, #181230);
      box-shadow: 0 35px 110px rgba(0, 0, 0, 0.46), 0 0 55px rgba(138, 73, 255, 0.08);
      position: relative;
    }

    .founder-photo {
      position: relative;
      min-height: 560px;
      overflow: hidden;
    }

    .founder-photo img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center top;
      filter: saturate(0.96) contrast(1.02);
      transition: transform 0.7s ease, filter 0.7s ease;
    }

    .founder-card:hover .founder-photo img {
      transform: scale(1.03);
      filter: saturate(1.05) contrast(1.04);
    }

    .founder-photo::after {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(90deg, transparent 60%, #101020 100%),
                  linear-gradient(0deg, #101020 0%, transparent 35%);
      pointer-events: none;
    }

    .founder-content {
      padding: 60px 56px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      position: relative;
      z-index: 1;
    }

    .founder-kicker {
      color: var(--purple);
      font-size: 10px;
      text-transform: uppercase;
      letter-spacing: 0.22em;
      margin-bottom: 12px;
      font-weight: 750;
    }

    .founder-content h3 {
      font-size: clamp(38px, 4.2vw, 58px);
      line-height: 0.98;
      letter-spacing: -0.05em;
      margin-bottom: 14px;
      font-weight: 850;
    }

    .founder-role {
      color: #ded6ff;
      font-size: 15px;
      font-weight: 650;
      margin-bottom: 22px;
    }

    .founder-content p {
      color: var(--text-muted);
      max-width: 540px;
      font-size: 14.5px;
      line-height: 1.8;
      margin-bottom: 24px;
    }

    .founder-pills {
      display: flex;
      gap: 9px;
      flex-wrap: wrap;
      margin-bottom: 34px;
    }

    .founder-pill {
      font-size: 11px;
      font-weight: 600;
      color: #cfd2e5;
      border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 7px 14px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.04);
    }

    /* =========================================================
       VISION & ECOSYSTEM SECTION (#vision)
       ========================================================= */
    .vision-panel {
      position: relative;
      border: 1px solid rgba(255, 255, 255, 0.11);
      border-radius: var(--radius-xl);
      overflow: hidden;
      background: linear-gradient(145deg, rgba(17, 18, 38, 0.88), rgba(6, 7, 16, 0.95));
      box-shadow: var(--shadow-ambient);
      padding: 56px 40px;
    }

    .vision-panel::before {
      content: "";
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at 50% 50%, rgba(138, 73, 255, 0.12), transparent 45%),
                  radial-gradient(circle at 80% 80%, rgba(33, 217, 255, 0.08), transparent 35%);
      pointer-events: none;
    }

    .vision-quote {
      text-align: center;
      max-width: 660px;
      margin: 0 auto 50px;
      position: relative;
      z-index: 1;
    }

    .vision-quote .quote-phrase {
      font-size: clamp(24px, 3.2vw, 38px);
      font-weight: 850;
      letter-spacing: -0.035em;
      line-height: 1.2;
      color: #ffffff;
      margin-bottom: 12px;
    }

    .vision-quote .quote-sub {
      color: var(--text-dim);
      font-size: 11px;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      font-weight: 700;
    }

    .ecosystem-diagram {
      position: relative;
      z-index: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 36px;
    }

    .hub-nivora {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 24px 38px;
      border-radius: 28px;
      background: radial-gradient(circle, rgba(140, 75, 255, 0.22), rgba(12, 13, 28, 0.95) 75%);
      border: 1px solid rgba(190, 140, 255, 0.35);
      box-shadow: 0 0 70px rgba(157, 92, 255, 0.30), inset 0 1px 0 rgba(255, 255, 255, 0.25);
      text-align: center;
    }

    .hub-nivora img {
      width: 64px;
      height: 64px;
      object-fit: contain;
      filter: drop-shadow(0 0 16px rgba(157, 92, 255, 0.6));
      margin-bottom: 10px;
    }

    .hub-nivora b {
      font-size: 20px;
      letter-spacing: 0.16em;
      color: #ffffff;
    }

    .hub-nivora span {
      font-size: 10px;
      color: #afb2cb;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      margin-top: 2px;
    }

    .conduit-down {
      width: 2px;
      height: 38px;
      background: linear-gradient(180deg, var(--purple), rgba(33, 217, 255, 0.8));
      box-shadow: 0 0 12px var(--purple);
    }

    .worlds-orbit-row {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      width: 100%;
    }

    .orbit-node {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      padding: 22px 16px;
      border-radius: var(--radius-md);
      background: rgba(255, 255, 255, 0.035);
      border: 1px solid rgba(255, 255, 255, 0.09);
      transition: var(--transition-smooth);
    }

    .orbit-node:hover {
      transform: translateY(-5px);
      border-color: rgba(255, 255, 255, 0.22);
      background: rgba(255, 255, 255, 0.06);
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.35);
    }

    .orbit-node img {
      width: 58px;
      height: 48px;
      object-fit: contain;
      margin-bottom: 12px;
      filter: drop-shadow(0 0 12px rgba(157, 92, 255, 0.3));
    }

    .orbit-node b {
      font-size: 14px;
      letter-spacing: 0.04em;
      color: #ffffff;
      margin-bottom: 4px;
    }

    .orbit-node span {
      font-size: 9.5px;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.12em;
    }

    .separate-stream-divider {
      width: 100%;
      display: flex;
      align-items: center;
      gap: 18px;
      margin-top: 14px;
    }

    .separate-stream-divider span {
      font-size: 10.5px;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #7b809a;
      white-space: nowrap;
      font-weight: 700;
    }

    .separate-stream-divider::before,
    .separate-stream-divider::after {
      content: "";
      flex-grow: 1;
      height: 1px;
      background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.10), transparent);
    }

    .stream-folivio-node {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
      width: 100%;
      padding: 22px 28px;
      border-radius: 20px;
      border: 1px dashed rgba(60, 180, 255, 0.35);
      background: linear-gradient(145deg, rgba(16, 25, 48, 0.65), rgba(8, 12, 26, 0.75));
      transition: var(--transition-smooth);
    }

    .stream-folivio-node:hover {
      border-color: rgba(60, 180, 255, 0.65);
      box-shadow: 0 16px 45px rgba(33, 217, 255, 0.12);
      transform: translateY(-2px);
    }

    .sfn-left {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .sfn-left img {
      width: 48px;
      height: 48px;
      object-fit: contain;
    }

    .sfn-info b {
      font-size: 15px;
      color: #ffffff;
      letter-spacing: 0.04em;
    }

    .sfn-info span {
      display: block;
      font-size: 11px;
      color: #8ecfff;
      margin-top: 2px;
    }

    .sfn-tag {
      font-size: 9px;
      font-weight: 750;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      padding: 6px 12px;
      border-radius: 999px;
      background: rgba(33, 217, 255, 0.12);
      border: 1px solid rgba(33, 217, 255, 0.3);
      color: #bbf0ff;
    }

    /* =========================================================
       FOLIVIO SECTION (#folivio)
       ========================================================= */
    .folivio-premium {
      display: grid;
      grid-template-columns: 0.92fr 1.08fr;
      gap: 22px;
      position: relative;
      z-index: 1;
    }

    .folivio-identity,
    .folivio-services {
      position: relative;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: var(--radius-xl);
      background: linear-gradient(145deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.015)), rgba(7, 8, 18, 0.85);
      box-shadow: 0 30px 100px rgba(0, 0, 0, 0.38), inset 0 1px 0 rgba(255, 255, 255, 0.06);
    }

    .folivio-identity {
      padding: 38px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .folivio-identity::before {
      content: "";
      position: absolute;
      width: 440px;
      height: 440px;
      left: -160px;
      top: -160px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(33, 217, 255, 0.16), rgba(157, 92, 255, 0.10) 40%, transparent 70%);
      filter: blur(16px);
      pointer-events: none;
    }

    .folivio-logo-wrap {
      width: 100%;
      height: 250px;
      border-radius: 24px;
      display: grid;
      place-items: center;
      background: radial-gradient(circle at 50% 45%, rgba(65, 175, 255, 0.12), transparent 55%),
                  linear-gradient(145deg, rgba(255, 255, 255, 0.07), rgba(255, 255, 255, 0.02));
      border: 1px solid rgba(255, 255, 255, 0.09);
      overflow: hidden;
    }

    .folivio-logo-wrap img {
      width: 230px;
      height: 230px;
      object-fit: contain;
      filter: drop-shadow(0 16px 36px rgba(50, 140, 255, 0.20));
      transition: transform 0.5s ease;
    }

    .folivio-identity:hover .folivio-logo-wrap img {
      transform: scale(1.05) rotate(-1deg);
    }

    .folivio-brand-copy {
      position: relative;
      z-index: 2;
      margin-top: 24px;
    }

    .folivio-overline {
      color: #8cc9ff;
      font-size: 9.5px;
      font-weight: 750;
      letter-spacing: 0.20em;
      text-transform: uppercase;
      margin-bottom: 6px;
    }

    .folivio-brand-copy h3 {
      font-size: 48px;
      line-height: 0.95;
      letter-spacing: -0.06em;
      margin-bottom: 8px;
      background: linear-gradient(105deg, #ffffff 10%, #d8e7ff 35%, #4fc9ff 68%, #9b62ff 100%);
      -webkit-background-clip: text;
      background-clip: text;
      -webkit-text-fill-color: transparent;
      color: transparent;
    }

    .folivio-tagline {
      font-size: 17px;
      font-weight: 750;
      color: #e5e8f8;
      letter-spacing: 0.01em;
      margin-bottom: 12px;
    }

    .folivio-tagline span { color: var(--purple); }
    .folivio-tagline b { color: var(--cyan); }

    .folivio-brand-copy p {
      color: var(--text-muted);
      font-size: 13px;
      line-height: 1.7;
      margin-bottom: 22px;
    }

    .folivio-cta-group {
      display: flex;
      align-items: center;
      gap: 14px;
      flex-wrap: wrap;
    }

    .folivio-handle {
      font-size: 11px;
      color: #8a8fa8;
      letter-spacing: 0.04em;
    }

    .folivio-services {
      padding: 40px;
      background: radial-gradient(circle at 90% 10%, rgba(33, 217, 255, 0.08), transparent 35%),
                  radial-gradient(circle at 10% 90%, rgba(157, 92, 255, 0.08), transparent 38%),
                  rgba(7, 8, 18, 0.88);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .service-intro h4 {
      font-size: 30px;
      letter-spacing: -0.04em;
      line-height: 1.1;
      margin: 8px 0 10px;
      color: #ffffff;
    }

    .service-intro h4 em {
      font-style: normal;
      color: var(--cyan);
    }

    .service-intro p {
      color: var(--text-muted);
      font-size: 12.5px;
      line-height: 1.7;
    }

    .services-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin: 26px 0;
    }

    .service-box {
      padding: 20px;
      border-radius: var(--radius-md);
      border: 1px solid rgba(255, 255, 255, 0.08);
      background: rgba(255, 255, 255, 0.025);
      position: relative;
      transition: var(--transition-smooth);
    }

    .service-box:hover {
      transform: translateY(-3px);
      background: rgba(255, 255, 255, 0.05);
      border-color: rgba(116, 205, 255, 0.3);
    }

    .service-box-num {
      position: absolute;
      top: 14px;
      right: 14px;
      font-size: 9px;
      color: #60647c;
      letter-spacing: 0.14em;
      font-weight: 750;
    }

    .service-box-icon {
      width: 36px;
      height: 36px;
      border-radius: 10px;
      display: grid;
      place-items: center;
      background: linear-gradient(145deg, rgba(33, 217, 255, 0.20), rgba(157, 92, 255, 0.20));
      border: 1px solid rgba(131, 201, 255, 0.22);
      color: #dcefff;
      font-size: 10px;
      font-weight: 850;
      margin-bottom: 12px;
    }

    .service-box b {
      display: block;
      font-size: 14px;
      color: #ffffff;
      margin-bottom: 5px;
    }

    .service-box span {
      display: block;
      font-size: 11px;
      color: var(--text-muted);
      line-height: 1.55;
    }

    .folivio-footer-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      padding-top: 20px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
    }

    .folivio-footer-bar strong {
      font-size: 13px;
      color: #ffffff;
    }

    .folivio-footer-bar span {
      color: var(--text-dim);
      font-size: 12px;
    }

    /* =========================================================
       CONTACT SECTION (#contact)
       ========================================================= */
    .contact-wrapper {
      display: grid;
      grid-template-columns: 1fr 1.15fr;
      gap: 36px;
      align-items: start;
    }

    .contact-info-panel {
      padding: 40px;
      border-radius: var(--radius-xl);
      border: 1px solid rgba(255, 255, 255, 0.10);
      background: linear-gradient(145deg, rgba(16, 17, 34, 0.85), rgba(7, 8, 17, 0.94));
      box-shadow: var(--shadow-ambient);
    }

    .contact-info-panel h3 {
      font-size: 32px;
      letter-spacing: -0.04em;
      margin-bottom: 14px;
      color: #ffffff;
      line-height: 1.1;
    }

    .contact-info-panel p {
      color: var(--text-muted);
      font-size: 14px;
      line-height: 1.75;
      margin-bottom: 30px;
    }

    .contact-methods {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .contact-card-link {
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 16px 20px;
      border-radius: var(--radius-md);
      background: rgba(255, 255, 255, 0.035);
      border: 1px solid rgba(255, 255, 255, 0.08);
      transition: var(--transition-smooth);
    }

    .contact-card-link:hover {
      background: rgba(255, 255, 255, 0.06);
      border-color: rgba(168, 102, 255, 0.4);
      transform: translateX(4px);
    }

    .ccl-icon {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      display: grid;
      place-items: center;
      background: linear-gradient(145deg, rgba(157, 92, 255, 0.25), rgba(33, 217, 255, 0.15));
      border: 1px solid rgba(255, 255, 255, 0.14);
      color: #ffffff;
    }

    .ccl-icon svg {
      width: 22px;
      height: 22px;
      fill: currentColor;
    }

    .ccl-text b {
      display: block;
      font-size: 14px;
      color: #ffffff;
    }

    .ccl-text span {
      display: block;
      font-size: 12px;
      color: var(--text-dim);
    }

    .folivio-redirect-notice {
      margin-top: 28px;
      padding: 16px 20px;
      border-radius: var(--radius-md);
      border: 1px solid rgba(33, 217, 255, 0.22);
      background: rgba(33, 217, 255, 0.04);
      font-size: 12px;
      color: #bcefff;
      line-height: 1.6;
    }

    .folivio-redirect-notice strong {
      display: block;
      color: #ffffff;
      margin-bottom: 4px;
    }

    .folivio-redirect-notice a {
      color: var(--cyan);
      font-weight: 700;
      text-decoration: underline;
    }

    /* Contact Form */
    .contact-form-panel {
      padding: 40px;
      border-radius: var(--radius-xl);
      border: 1px solid rgba(255, 255, 255, 0.10);
      background: linear-gradient(145deg, rgba(20, 21, 42, 0.75), rgba(8, 9, 20, 0.90));
      box-shadow: var(--shadow-ambient);
    }

    .form-group {
      margin-bottom: 20px;
    }

    .form-group label {
      display: block;
      font-size: 12px;
      font-weight: 650;
      color: #c5c7dc;
      margin-bottom: 8px;
      letter-spacing: 0.02em;
    }

    .form-control {
      width: 100%;
      padding: 13px 16px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: var(--radius-sm);
      color: #ffffff;
      font-family: inherit;
      font-size: 14px;
      transition: var(--transition-smooth);
    }

    .form-control:focus {
      background: rgba(255, 255, 255, 0.07);
      border-color: var(--purple);
      box-shadow: 0 0 20px rgba(157, 92, 255, 0.22);
    }

    textarea.form-control {
      resize: vertical;
      min-height: 120px;
    }

    .form-submit-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      margin-top: 26px;
    }

    .form-status-msg {
      font-size: 12px;
      color: #87ffce;
      opacity: 0;
      transition: opacity 0.3s ease;
    }

    .form-status-msg.visible {
      opacity: 1;
    }

    /* =========================================================
       FOOTER SECTION
       ========================================================= */
    footer {
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding: 80px 0 45px;
      position: relative;
      overflow: hidden;
      background: #030408;
    }

    footer::before {
      content: "NIVORA";
      position: absolute;
      left: 50%;
      bottom: -60px;
      transform: translateX(-50%);
      font-size: clamp(80px, 18vw, 240px);
      font-weight: 950;
      letter-spacing: -0.07em;
      color: rgba(255, 255, 255, 0.018);
      pointer-events: none;
      user-select: none;
    }

    .footer-grid {
      display: grid;
      grid-template-columns: 1.5fr 1fr 1fr 1fr;
      gap: 36px;
      position: relative;
      z-index: 1;
    }

    .footer-brand-col img {
      width: 44px;
      height: 44px;
      object-fit: contain;
      filter: drop-shadow(0 0 12px rgba(157, 92, 255, 0.5));
      margin-bottom: 12px;
    }

    .footer-brand-col h4 {
      font-size: 20px;
      font-weight: 850;
      letter-spacing: 0.08em;
      color: #ffffff;
      margin-bottom: 6px;
    }

    .footer-brand-col p {
      color: var(--text-dim);
      font-size: 12px;
      line-height: 1.7;
      max-width: 290px;
    }

    .footer-col h5 {
      font-size: 10px;
      text-transform: uppercase;
      letter-spacing: 0.20em;
      color: #afb1c5;
      margin-bottom: 16px;
      font-weight: 750;
    }

    .footer-col a {
      display: block;
      color: var(--text-dim);
      font-size: 12.5px;
      margin-bottom: 10px;
      transition: color 0.2s ease, transform 0.2s ease;
    }

    .footer-col a:hover {
      color: #ffffff;
      transform: translateX(2px);
    }

    .footer-bottom {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      margin-top: 60px;
      padding-top: 24px;
      border-top: 1px solid rgba(255, 255, 255, 0.06);
      color: #63667c;
      font-size: 11.5px;
      position: relative;
      z-index: 1;
    }

    .footer-bottom a {
      color: #8f92ab;
      font-weight: 600;
    }

    .footer-bottom a:hover {
      color: #ffffff;
    }

    /* Scroll Reveal Animation */
    .reveal {
      opacity: 1;
      transform: none;
      transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @media (prefers-reduced-motion: no-preference) {
      .js-ready .reveal:not(.show) {
        opacity: 0;
        transform: translateY(28px);
      }
      .js-ready .reveal.show {
        opacity: 1;
        transform: none;
      }
    }

    @keyframes spinSlow { to { transform: rotate(360deg); } }
    @keyframes spinReverse { to { transform: rotate(-360deg); } }
    @keyframes floatSmooth { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-12px); } }
    @keyframes pulseStar { 0%, 100% { opacity: 0.35; transform: scale(0.9); } 50% { opacity: 1; transform: scale(1.15); } }

    /* =========================================================
       RESPONSIVE DESIGN BREAKPOINTS
       ========================================================= */
    @media (max-width: 1024px) {
      .hero-grid { grid-template-columns: 1fr; gap: 48px; }
      .hero-art { min-height: 520px; order: -1; }
      .worlds-grid { grid-template-columns: 1fr; }
      .universe-conduit-line { grid-template-columns: 1fr 1fr; }
      .capabilities-deep-grid { grid-template-columns: 1fr 1fr; }
      .detail-header-block { grid-template-columns: 1fr; }
      .about-problem-grid { grid-template-columns: 1fr; }
      .vision-tagline-block { grid-template-columns: 1fr; }
      .vtb-right { text-align: left; padding-left: 0; border-left: none; border-top: 1px solid rgba(255, 255, 255, 0.08); padding-top: 20px; }
      .founder-card { grid-template-columns: 1fr; }
      .founder-photo { min-height: 420px; }
      .founder-content { padding: 44px 34px; }
      .folivio-premium { grid-template-columns: 1fr; }
      .pipeline-steps { grid-template-columns: 1fr 1fr; }
      .principles-grid { grid-template-columns: 1fr 1fr; }
      .worlds-orbit-row { grid-template-columns: 1fr 1fr; }
      .contact-wrapper { grid-template-columns: 1fr; }
      .footer-grid { grid-template-columns: 1fr 1fr; gap: 32px; }
    }

    @media (max-width: 900px) {
      .navlinks { display: none; }
      .menu-toggle { display: flex; }
      .hero { padding-top: 130px; }
      .hero h1 { font-size: clamp(48px, 9vw, 68px); }
      .product-tabs-wrapper { top: 80px; overflow-x: auto; padding: 4px; }
      .product-tab-btn { padding: 10px 14px; font-size: 12px; }
    }

    @media (max-width: 640px) {
      .topbar { top: 10px; border-radius: 18px; width: calc(100vw - 20px); }
      .nav { height: 58px; padding: 0 10px 0 12px; }
      .brand { gap: 8px; min-width: 0; flex-shrink: 1; }
      .brand img { width: 32px; height: 32px; flex-shrink: 0; }
      .brand-text { min-width: 0; overflow: hidden; }
      .brand-text span { font-size: 14.5px; white-space: nowrap; }
      .brand-text small { font-size: 7.5px; letter-spacing: 0.16em; }
      .hero { padding-top: 110px; }
      .hero h1 { font-size: 42px; }
      .hero-art { min-height: 400px; }
      .core { width: 240px; height: 240px; }
      .core img { width: 160px; height: 160px; }
      .hero-art::before { width: 360px; height: 360px; }
      .hero-art::after { width: 270px; height: 270px; }
      .satellite { width: 78px; height: 78px; border-radius: 20px; }
      .satellite img { max-width: 60px; max-height: 60px; }
      .s-checkra { top: 15px; right: 8px; }
      .s-homora { bottom: 15px; left: 8px; }
      .s-bubora { top: 125px; left: 0px; }
      .s-sayora { bottom: 15px; right: 8px; }
      .section { padding: 80px 0; }
      .section-head { flex-direction: column; align-items: flex-start; gap: 14px; margin-bottom: 38px; }
      .universe-philosophy-card { padding: 36px 20px; }
      .universe-conduit-line { grid-template-columns: 1fr; }
      .product-tabs-wrapper { flex-wrap: nowrap; -webkit-overflow-scrolling: touch; }
      .product-tab-btn { min-width: 140px; }
      .detail-card-container { padding: 30px 20px; }
      .dhb-logo-wrap { height: 220px; }
      .capabilities-deep-grid { grid-template-columns: 1fr; }
      .workflow-card-block { padding: 24px 18px; }
      .ecosystem-visual-block { padding: 24px 18px; }
      .pipeline-wrapper { padding: 30px 20px; }
      .pipeline-steps { grid-template-columns: 1fr; }
      .principles-grid { grid-template-columns: 1fr; }
      .worlds-orbit-row { grid-template-columns: 1fr; }
      .stream-folivio-node { flex-direction: column; align-items: flex-start; gap: 16px; }
      .folivio-identity { padding: 26px 20px; }
      .folivio-services { padding: 28px 20px; }
      .services-grid { grid-template-columns: 1fr; }
      .folivio-footer-bar { flex-direction: column; align-items: flex-start; }
      .contact-info-panel, .contact-form-panel { padding: 28px 20px; }
      .footer-grid { grid-template-columns: 1fr; }
      .footer-bottom { flex-direction: column; align-items: flex-start; gap: 10px; }
    }

    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }
    }
"""
