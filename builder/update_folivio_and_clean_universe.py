import os
import sys

TARGET_PATH = "/Users/bennabathulanivas/Desktop/my projects/NIVORA/builder/assemble_ultimate_3d_universe.py"

with open(TARGET_PATH, "r", encoding="utf-8") as f:
    code = f.read()

# ==============================================================================
# 1. CSS UPDATES: LOADER, MOBILE DRAWER, PRODUCT BADGES, FOLIVIO SHOWCASE
# ==============================================================================
new_css = """
    /* -------------------------------------------------------------
       UNIVERSE SUBTLE LOADER
       ------------------------------------------------------------- */
    .universe-loader {
      position: fixed;
      inset: 0;
      background: #02040a;
      z-index: 99999;
      display: flex;
      align-items: center;
      justify-content: center;
      pointer-events: none;
      opacity: 1;
      transition: opacity 0.45s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.45s ease;
    }
    .universe-loader.loaded {
      opacity: 0;
      visibility: hidden;
    }
    .loader-inner {
      text-align: center;
    }
    .loader-brand {
      font-family: var(--font-display);
      font-size: 2.0rem;
      font-weight: 800;
      letter-spacing: 0.18em;
      background: linear-gradient(135deg, #a855f7 0%, #38bdf8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 0.5rem;
    }
    .loader-status {
      font-family: var(--font-mono);
      font-size: 0.76rem;
      letter-spacing: 0.16em;
      color: #94a3b8;
      text-transform: uppercase;
      animation: pulseText 1.5s infinite ease-in-out;
    }
    @keyframes pulseText {
      0%, 100% { opacity: 0.6; }
      50% { opacity: 1.0; }
    }

    /* -------------------------------------------------------------
       MOBILE DRAWER MENU & TOGGLE
       ------------------------------------------------------------- */
    .nav-mobile-toggle {
      display: none;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      gap: 5px;
      width: 40px;
      height: 40px;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 50%;
      cursor: pointer;
      padding: 0;
      transition: background 0.2s ease, border-color 0.2s ease;
    }
    .nav-mobile-toggle:hover {
      background: rgba(255, 255, 255, 0.12);
      border-color: rgba(56, 189, 248, 0.4);
    }
    .nav-mobile-toggle .bar {
      width: 17px;
      height: 2px;
      background: #ffffff;
      border-radius: 2px;
      transition: transform 0.3s ease, opacity 0.3s ease;
    }
    .mobile-drawer {
      position: fixed;
      top: 0;
      right: -100%;
      width: min(340px, 86vw);
      height: 100vh;
      background: rgba(2, 6, 23, 0.95);
      backdrop-filter: blur(25px);
      -webkit-backdrop-filter: blur(25px);
      border-left: 1px solid rgba(255, 255, 255, 0.12);
      z-index: 10000;
      display: flex;
      flex-direction: column;
      padding: 2.2rem 1.8rem;
      transition: right 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: -15px 0 50px rgba(0, 0, 0, 0.85);
    }
    .mobile-drawer.open {
      right: 0;
    }
    .drawer-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-bottom: 1.5rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      margin-bottom: 2rem;
    }
    .drawer-brand {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      font-family: var(--font-display);
      font-size: 0.9rem;
      font-weight: 700;
      letter-spacing: 0.12em;
      color: #fff;
    }
    .drawer-close-btn {
      background: none;
      border: none;
      color: #94a3b8;
      font-size: 2.0rem;
      cursor: pointer;
      line-height: 1;
      padding: 0;
      transition: color 0.2s ease;
    }
    .drawer-close-btn:hover {
      color: #ffffff;
    }
    .drawer-links {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 1.35rem;
    }
    .drawer-link {
      font-family: var(--font-ui);
      font-size: 1.2rem;
      font-weight: 500;
      color: #cbd5e1;
      text-decoration: none;
      transition: color 0.2s ease, transform 0.2s ease;
      display: inline-block;
    }
    .drawer-link:hover, .drawer-link.active {
      color: var(--brand-cyan);
      transform: translateX(6px);
    }
    .drawer-footer {
      margin-top: auto;
      padding-top: 1.5rem;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
    }
    .drawer-status {
      display: inline-flex;
      align-items: center;
      gap: 0.55rem;
      font-family: var(--font-mono);
      font-size: 0.75rem;
      color: #38bdf8;
      letter-spacing: 0.12em;
    }

    /* -------------------------------------------------------------
       PRODUCT CARD BADGE: 'A NIVORA PRODUCT'
       ------------------------------------------------------------- */
    .product-branding-tag {
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      font-family: var(--font-mono);
      font-size: 0.68rem;
      font-weight: 600;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.08);
      border: 1px solid rgba(56, 189, 248, 0.24);
      border-radius: 9999px;
      padding: 0.25rem 0.65rem;
      margin-bottom: 0.75rem;
    }
    .product-brand-dot {
      width: 5px;
      height: 5px;
      border-radius: 50%;
      background: #38bdf8;
      box-shadow: 0 0 8px #38bdf8;
    }

    /* -------------------------------------------------------------
       FOLIVIO COMPREHENSIVE SHOWCASE STYLES
       ------------------------------------------------------------- */
    .folivio-section {
      position: relative;
      z-index: 20;
    }
    .folivio-hero-box {
      background: radial-gradient(circle at top left, rgba(56, 189, 248, 0.08) 0%, rgba(168, 85, 247, 0.05) 50%, rgba(2, 6, 23, 0.65) 100%);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: var(--radius-lg);
      padding: clamp(2.2rem, 5vw, 3.8rem);
      margin-bottom: 3.5rem;
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      position: relative;
      overflow: hidden;
    }
    .folivio-hero-box::before {
      content: '';
      position: absolute;
      top: -120px;
      right: -120px;
      width: 320px;
      height: 320px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(168, 85, 247, 0.16) 0%, rgba(0, 0, 0, 0) 70%);
      pointer-events: none;
    }
    .folivio-badge-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.4rem 1.05rem;
      border-radius: 9999px;
      background: rgba(56, 189, 248, 0.08);
      border: 1px solid rgba(56, 189, 248, 0.28);
      font-family: var(--font-mono);
      font-size: 0.74rem;
      font-weight: 600;
      letter-spacing: 0.12em;
      color: #7dd3fc;
      text-transform: uppercase;
      margin-bottom: 1.6rem;
    }
    .folivio-badge-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #38bdf8;
      box-shadow: 0 0 10px #38bdf8;
      animation: dotPulse 2s infinite ease-in-out;
    }
    .folivio-brand-row {
      display: flex;
      align-items: center;
      gap: 2.0rem;
      margin-bottom: 1.6rem;
      flex-wrap: wrap;
    }
    .folivio-logo-badge {
      width: clamp(76px, 8.5vw, 102px);
      height: clamp(76px, 8.5vw, 102px);
      border-radius: var(--radius-md);
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.12);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 0.85rem;
      box-shadow: 0 14px 35px rgba(0, 0, 0, 0.45);
    }
    .folivio-main-logo {
      width: 100%;
      height: 100%;
      object-fit: contain;
    }
    .folivio-title {
      font-family: var(--font-display);
      font-size: clamp(2.4rem, 4.8vw, 4.0rem);
      font-weight: 800;
      letter-spacing: -0.04em;
      line-height: 1.05;
      color: #ffffff;
    }
    .folivio-subtag {
      font-family: var(--font-serif);
      font-style: italic;
      font-size: clamp(1.2rem, 2.2vw, 1.7rem);
      font-weight: 400;
      color: #cbd5e1;
      margin-top: 0.25rem;
    }
    .folivio-pills-row {
      display: flex;
      align-items: center;
      gap: 0.65rem;
      margin-top: 0.65rem;
      font-family: var(--font-mono);
      font-size: 0.78rem;
      font-weight: 600;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: #a855f7;
    }
    .folivio-pill-sep {
      color: rgba(255, 255, 255, 0.3);
    }
    .folivio-manifesto {
      font-size: clamp(1.05rem, 1.4vw, 1.25rem);
      line-height: 1.75;
      color: #e2e8f0;
      max-width: 820px;
      margin-bottom: 2.2rem;
    }
    .folivio-prime-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.65rem;
      padding: 0.9rem 2.0rem;
      border-radius: 9999px;
      background: linear-gradient(135deg, #0284c7 0%, #38bdf8 50%, #a855f7 100%);
      color: #ffffff;
      font-family: var(--font-ui);
      font-size: 0.96rem;
      font-weight: 600;
      text-decoration: none;
      box-shadow: 0 0 25px rgba(56, 189, 248, 0.45);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .folivio-prime-btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 0 35px rgba(56, 189, 248, 0.65);
      color: #ffffff;
    }
    .folivio-sub-head {
      margin-bottom: 2rem;
    }
    .folivio-sub-head h3 {
      font-family: var(--font-display);
      font-size: clamp(1.8rem, 3.2vw, 2.5rem);
      font-weight: 700;
      letter-spacing: -0.03em;
      color: #ffffff;
      margin-top: 0.4rem;
    }
    .folivio-services-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1.6rem;
      margin-bottom: 4rem;
    }
    .folivio-card {
      background: rgba(15, 23, 42, 0.45);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-md);
      padding: 2rem;
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
    }
    .folivio-card:hover {
      transform: translateY(-4px);
      border-color: rgba(56, 189, 248, 0.35);
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.4), 0 0 30px rgba(56, 189, 248, 0.15);
    }
    .folivio-card-num {
      font-family: var(--font-mono);
      font-size: 0.82rem;
      font-weight: 700;
      letter-spacing: 0.15em;
      color: #38bdf8;
      margin-bottom: 0.85rem;
    }
    .folivio-card h4 {
      font-family: var(--font-display);
      font-size: 1.3rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #ffffff;
      margin-bottom: 0.75rem;
    }
    .folivio-card p {
      font-size: 0.94rem;
      line-height: 1.65;
      color: #94a3b8;
    }
    .folivio-benefits-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.5rem;
      margin-bottom: 4rem;
    }
    .folivio-benefit-card {
      background: rgba(2, 6, 23, 0.5);
      border: 1px solid rgba(255, 255, 255, 0.07);
      border-radius: var(--radius-sm);
      padding: 1.6rem 1.8rem;
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
      transition: border-color 0.3s ease;
    }
    .folivio-benefit-card:hover {
      border-color: rgba(168, 85, 247, 0.35);
    }
    .benefit-icon {
      color: #c084fc;
      font-size: 1.1rem;
      line-height: 1;
    }
    .folivio-benefit-card h5 {
      font-family: var(--font-display);
      font-size: 1.12rem;
      font-weight: 600;
      letter-spacing: -0.01em;
      color: #f8fafc;
    }
    .folivio-benefit-card p {
      font-size: 0.9rem;
      line-height: 1.55;
      color: #94a3b8;
    }
    .folivio-process-steps {
      display: grid;
      grid-template-columns: 1fr auto 1fr auto 1fr auto 1fr;
      align-items: center;
      gap: 1rem;
      margin-bottom: 4rem;
    }
    .folivio-step-card {
      background: rgba(15, 23, 42, 0.5);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-md);
      padding: 1.6rem 1.4rem;
      text-align: center;
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
    }
    .step-badge {
      font-family: var(--font-mono);
      font-size: 0.68rem;
      font-weight: 700;
      letter-spacing: 0.16em;
      color: #38bdf8;
      margin-bottom: 0.6rem;
      text-transform: uppercase;
    }
    .folivio-step-card h4 {
      font-family: var(--font-display);
      font-size: 1.25rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #ffffff;
      margin-bottom: 0.5rem;
    }
    .folivio-step-card p {
      font-size: 0.85rem;
      line-height: 1.5;
      color: #94a3b8;
    }
    .folivio-step-arrow {
      color: rgba(255, 255, 255, 0.35);
      font-size: 1.3rem;
      font-weight: 700;
    }
    @media (max-width: 900px) {
      .folivio-process-steps {
        grid-template-columns: 1fr;
      }
      .folivio-step-arrow {
        display: none;
      }
    }
    .folivio-bottom-cta-banner {
      background: linear-gradient(135deg, rgba(30, 27, 75, 0.4) 0%, rgba(15, 23, 42, 0.6) 100%);
      border: 1px solid rgba(168, 85, 247, 0.2);
      border-radius: var(--radius-md);
      padding: 2.2rem 2.8rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 2rem;
      flex-wrap: wrap;
    }
    .folivio-bottom-cta-banner h4 {
      font-family: var(--font-display);
      font-size: 1.35rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 0.4rem;
    }
    .folivio-bottom-cta-banner p {
      font-size: 0.94rem;
      color: #94a3b8;
      max-width: 540px;
    }
    @media (max-width: 860px) {
      .nav-links, .nav-status-pill, .nav-cta-btn {
        display: none !important;
      }
      .nav-mobile-toggle {
        display: flex !important;
      }
    }
"""

# Insert new CSS right before </style>
assert "</style>" in code, "</style> tag not found"
code = code.replace("</style>", new_css + "\n  </style>", 1)

# ==============================================================================
# 2. HTML: UNIVERSE LOADER & MOBILE DRAWER
# ==============================================================================
# Loader at start of <body>
loader_html = """
  <!-- SUBTLE UNIVERSE INITIALIZATION LOADER -->
  <div id="universeLoader" class="universe-loader">
    <div class="loader-inner">
      <div class="loader-brand">NIVORA</div>
      <div class="loader-status">Initializing Universe...</div>
    </div>
  </div>
"""
assert "<body>" in code, "<body> tag not found"
code = code.replace("<body>", "<body>" + loader_html, 1)

# Mobile toggle inside nav-right-actions
nav_toggle_html = """
        <!-- Mobile Menu Toggle -->
        <button type="button" class="nav-mobile-toggle" id="mobileMenuToggle" aria-label="Toggle Navigation Menu">
          <span class="bar"></span>
          <span class="bar"></span>
        </button>
      </div>"""

assert '<span>Explore Universe &rarr;</span>\n        </button>\n      </div>' in code, "nav-cta-btn end not found"
code = code.replace('<span>Explore Universe &rarr;</span>\n        </button>\n      </div>', '<span>Explore Universe &rarr;</span>\n        </button>' + nav_toggle_html, 1)

# Mobile drawer right after </header>
drawer_html = """
    <!-- MOBILE NAVIGATION DRAWER -->
    <div class="mobile-drawer" id="mobileDrawer">
      <div class="drawer-header">
        <div class="drawer-brand">
          <img src="assets/images/nivora-logo.png" alt="NIVORA" style="width:26px;height:auto;">
          <span>NIVORA UNIVERSE</span>
        </div>
        <button type="button" class="drawer-close-btn" id="mobileDrawerClose">&times;</button>
      </div>
      <ul class="drawer-links">
        <li><a href="#hero" class="drawer-link">Home</a></li>
        <li><a href="#products" class="drawer-link">Products</a></li>
        <li><a href="#about" class="drawer-link">About</a></li>
        <li><a href="#portfolio" class="drawer-link">Portfolio</a></li>
        <li><a href="#vision" class="drawer-link">Vision</a></li>
        <li><a href="#folivio" class="drawer-link">FOLIVIO</a></li>
        <li><a href="#contact" class="drawer-link">Contact</a></li>
      </ul>
      <div class="drawer-footer">
        <div class="drawer-status">
          <span class="status-dot-pulse"></span>
          <span>STATUS: ONLINE</span>
        </div>
      </div>
    </div>
"""
assert "</header>" in code, "</header> not found"
code = code.replace("</header>", "</header>" + drawer_html, 1)

# ==============================================================================
# 3. HTML: PRODUCT BADGE 'A NIVORA PRODUCT' ON CHECKRA, HOMORA, BUBORA, SAYORA
# ==============================================================================
prod_tag = """
            <div class="product-branding-tag">
              <span class="product-brand-dot"></span>
              <span>A NIVORA Product</span>
            </div>"""

for c_target in ['<h3>CHECKRA', '<h3>HOMORA', '<h3>BUBORA', '<h3>SAYORA']:
    assert c_target in code, f"{c_target} not found"
    code = code.replace(c_target, prod_tag + '\n            ' + c_target, 1)

# ==============================================================================
# 4. HTML: EXPANDED FOLIVIO SHOWCASE SECTION
# ==============================================================================
old_folivio = """    <!-- =========================================================
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
    </section>"""

new_folivio = """    <!-- =========================================================
       SECTION 05: FOLIVIO SHOWCASE (#folivio)
       ========================================================= -->
    <section class="section folivio-section" id="folivio">
      <div class="section-divider"></div>
      <div class="container">
        <!-- 1. FOLIVIO HERO & STRATEGIC POSITIONING -->
        <div class="folivio-hero-box">
          <div class="folivio-badge-pill">
            <span class="folivio-badge-dot"></span>
            <span>A Professional Service by Nivas Bennabatthula</span>
          </div>

          <div class="folivio-brand-row">
            <div class="folivio-logo-badge">
              <img src="assets/images/folivio-logo.webp" alt="FOLIVIO Studio Logo" class="folivio-main-logo">
            </div>
            <div class="folivio-headings">
              <h2 class="folivio-title">FOLIVIO</h2>
              <div class="folivio-subtag">Build. Showcase. Grow.</div>
              <div class="folivio-pills-row">
                <span>Career Branding</span>
                <span class="folivio-pill-sep">&middot;</span>
                <span>Digital Presence</span>
              </div>
            </div>
          </div>

          <p class="folivio-manifesto">
            FOLIVIO helps students, freshers and professionals turn their education, skills, projects, certifications and experience into a polished professional identity that is ready to be seen, shared and remembered.
          </p>

          <div class="folivio-cta-wrap">
            <a href="https://www.instagram.com/folivio.ai?utm_source=ig_web_button_share_sheet&rpxt=ZDNlZDc0MzIxNw==" target="_blank" rel="noopener noreferrer" class="folivio-prime-btn">
              <span>Connect with FOLIVIO &rarr;</span>
            </a>
          </div>
        </div>

        <!-- 2. FOLIVIO 4-CARD SERVICE GRID -->
        <div class="folivio-sub-head">
          <div class="kicker">// 01 &middot; Career Branding Services</div>
          <h3>Tailored Services for Every Professional</h3>
        </div>

        <div class="folivio-services-grid">
          <!-- Service 01 -->
          <div class="folivio-card">
            <div class="folivio-card-num">01 &mdash; RESUMES</div>
            <h4>Professional Resumes</h4>
            <p>Create polished, role-focused resumes designed to present education, skills, projects, certifications and experience clearly.</p>
          </div>
          <!-- Service 02 -->
          <div class="folivio-card">
            <div class="folivio-card-num">02 &mdash; PORTFOLIOS</div>
            <h4>Personal Portfolios</h4>
            <p>Build modern personal portfolio websites that showcase your work, projects, achievements and professional story.</p>
          </div>
          <!-- Service 03 -->
          <div class="folivio-card">
            <div class="folivio-card-num">03 &mdash; LINKEDIN</div>
            <h4>LinkedIn Makeovers</h4>
            <p>Improve your LinkedIn presence with stronger positioning, profile content, project presentation and professional branding.</p>
          </div>
          <!-- Service 04 -->
          <div class="folivio-card">
            <div class="folivio-card-num">04 &mdash; WEBSITES</div>
            <h4>Portfolio Websites</h4>
            <p>Create a dedicated personal website that gives recruiters, clients and collaborators one place to understand your professional profile.</p>
          </div>
        </div>

        <!-- 3. FOLIVIO BENEFITS (Why FOLIVIO?) -->
        <div class="folivio-sub-head">
          <div class="kicker">// 02 &middot; Strategic Benefits</div>
          <h3>Why FOLIVIO?</h3>
        </div>

        <div class="folivio-benefits-grid">
          <div class="folivio-benefit-card">
            <div class="benefit-icon">✦</div>
            <h5>Stronger First Impression</h5>
            <p>Present yourself professionally from the first interaction.</p>
          </div>
          <div class="folivio-benefit-card">
            <div class="benefit-icon">✦</div>
            <h5>Clear Professional Identity</h5>
            <p>Turn scattered education, skills and experiences into one coherent career story.</p>
          </div>
          <div class="folivio-benefit-card">
            <div class="benefit-icon">✦</div>
            <h5>Better Project Visibility</h5>
            <p>Showcase projects and achievements instead of simply listing them.</p>
          </div>
          <div class="folivio-benefit-card">
            <div class="benefit-icon">✦</div>
            <h5>Recruiter-Friendly Presentation</h5>
            <p>Make important information easier to discover and understand.</p>
          </div>
          <div class="folivio-benefit-card">
            <div class="benefit-icon">✦</div>
            <h5>Consistent Personal Brand</h5>
            <p>Maintain a professional identity across your resume, LinkedIn and portfolio.</p>
          </div>
          <div class="folivio-benefit-card">
            <div class="benefit-icon">✦</div>
            <h5>Ready to Showcase</h5>
            <p>Create digital assets that can be shared with recruiters, employers, clients and collaborators.</p>
          </div>
        </div>

        <!-- 4. FOLIVIO PROCESS (DISCOVER -> DEFINE -> DESIGN -> SHOWCASE) -->
        <div class="folivio-sub-head">
          <div class="kicker">// 03 &middot; The Methodology</div>
          <h3>The FOLIVIO Process</h3>
        </div>

        <div class="folivio-process-steps">
          <div class="folivio-step-card">
            <div class="step-badge">01 &middot; DISCOVER</div>
            <h4>Discover</h4>
            <p>Understand your background, goals, skills and experience.</p>
          </div>
          <div class="folivio-step-arrow">&rarr;</div>
          <div class="folivio-step-card">
            <div class="step-badge">02 &middot; DEFINE</div>
            <h4>Define</h4>
            <p>Build a clear professional positioning.</p>
          </div>
          <div class="folivio-step-arrow">&rarr;</div>
          <div class="folivio-step-card">
            <div class="step-badge">03 &middot; DESIGN</div>
            <h4>Design</h4>
            <p>Create the required career assets.</p>
          </div>
          <div class="folivio-step-arrow">&rarr;</div>
          <div class="folivio-step-card">
            <div class="step-badge">04 &middot; SHOWCASE</div>
            <h4>Showcase</h4>
            <p>Present everything through a polished digital presence.</p>
          </div>
        </div>

        <!-- 5. BOTTOM CONNECT BANNER -->
        <div class="folivio-bottom-cta-banner">
          <div>
            <h4>Ready to Build Your Professional Brand?</h4>
            <p>Connect with FOLIVIO on Instagram for bespoke resume engineering, portfolio design, and career branding guidance.</p>
          </div>
          <a href="https://www.instagram.com/folivio.ai?utm_source=ig_web_button_share_sheet&rpxt=ZDNlZDc0MzIxNw==" target="_blank" rel="noopener noreferrer" class="folivio-prime-btn">
            <span>Connect with FOLIVIO &rarr;</span>
          </a>
        </div>
      </div>
    </section>"""

assert old_folivio in code, "old_folivio section not found"
code = code.replace(old_folivio, new_folivio, 1)

# ==============================================================================
# 5. THREE.JS ENGINE & PERFORMANCE:
#    - REMOVE UNEXPLAINED SHAPES (build3DProductWorlds & buildSpatialDestinations)
#    - LIMIT DPR (Math.min(window.devicePixelRatio, 1.75))
#    - ADAPTIVE PARTICLE QUALITY
#    - TAB VISIBILITY PAUSE
# ==============================================================================

# Update initUniverseEngineCinematic declarations and setup
old_engine_init = """        scene = new THREE.Scene();
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
        buildSpatialDestinations();"""

new_engine_init = """        // Adaptive device performance scaling (High-performance desktop vs medium/mobile)
        const isMobileDevice = (window.innerWidth < 768) || ('ontouchstart' in window);
        const cpuCores = navigator.hardwareConcurrency || 4;
        const isLowPower = isMobileDevice || (cpuCores <= 4);
        const particleScale = isLowPower ? (isMobileDevice ? 0.45 : 0.65) : 1.0;

        // Limit Device Pixel Ratio to optimize GPU fill-rate (Target: 60 FPS)
        const maxDpr = isMobileDevice ? 1.5 : 1.75;
        renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, maxDpr));
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setClearColor(0x02040a, 0);
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 1.25;

        scene = new THREE.Scene();
        camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 4000);
        camera.position.set(baseCamX, baseCamY, baseCamZ);
        camera.lookAt(0, 18, 0);

        // Build 3D Cinematic Universe (Pure Milky Way, Stars & Atmospheric Glow - No Unexplained Shapes)
        buildDistantStarfield(particleScale);
        buildWarpStarfield(particleScale);
        buildProceduralMilkyWay(particleScale);
        buildGalacticBulge(particleScale);
        buildSubtleCosmicNebula();
        buildBrightStellarBeacons();
        buildNivoraGlobeCore();

        // Dismiss Universe Loader smoothly
        const loaderEl = document.getElementById('universeLoader');
        if (loaderEl) {
          setTimeout(() => loaderEl.classList.add('loaded'), 200);
        }"""

assert old_engine_init in code, "old_engine_init not found"
code = code.replace(old_engine_init, new_engine_init, 1)

# Remove build3DProductWorlds function definition
b_prod_start = "    function build3DProductWorlds() {"
b_prod_end = "    function buildSubtleCosmicNebula() {"
assert b_prod_start in code, "b_prod_start not found"
assert b_prod_end in code, "b_prod_end not found"
s_idx = code.find(b_prod_start)
e_idx = code.find(b_prod_end)
code = code[:s_idx] + b_prod_end + code[e_idx + len(b_prod_end):]

# Remove buildSpatialDestinations function definition
b_spat_start = "    function buildSpatialDestinations() {"
b_spat_end = "    function buildDistantStarfield("
# Note: buildDistantStarfield currently has no args, let's find it:
if "    function buildDistantStarfield(" not in code:
    b_spat_end = "    function buildDistantStarfield() {"
assert b_spat_start in code, "b_spat_start not found"
assert b_spat_end in code, "b_spat_end not found"
s_idx2 = code.find(b_spat_start)
e_idx2 = code.find(b_spat_end)
code = code[:s_idx2] + code[e_idx2:]

# Update buildProceduralMilkyWay with scale parameter
old_mw_head = """    function buildProceduralMilkyWay() {
      milkyWayGroup = new THREE.Group();
      milkyWayGroup.position.set(globeCenterX, globeCenterY, globeCenterZ);
      milkyWayGroup.rotation.set(0.82, 0.22, -0.15); // Majestic cinematic 3D tilt

      const starCount = 42000;"""

new_mw_head = """    function buildProceduralMilkyWay(scale = 1.0) {
      milkyWayGroup = new THREE.Group();
      milkyWayGroup.position.set(globeCenterX, globeCenterY, globeCenterZ);
      milkyWayGroup.rotation.set(0.82, 0.22, -0.15); // Majestic cinematic 3D tilt

      const starCount = Math.floor(42000 * scale);"""

assert old_mw_head in code, "old_mw_head not found"
code = code.replace(old_mw_head, new_mw_head, 1)

# Update buildGalacticBulge with scale parameter
old_bulge_head = """    function buildGalacticBulge() {
      const bulgeCount = 7500;"""

new_bulge_head = """    function buildGalacticBulge(scale = 1.0) {
      const bulgeCount = Math.floor(7500 * scale);"""

assert old_bulge_head in code, "old_bulge_head not found"
code = code.replace(old_bulge_head, new_bulge_head, 1)

# Update buildDistantStarfield with scale parameter
old_dist_head = """    function buildDistantStarfield() {
      const count = 14000;"""

new_dist_head = """    function buildDistantStarfield(scale = 1.0) {
      const count = Math.floor(14000 * scale);"""

assert old_dist_head in code, "old_dist_head not found"
code = code.replace(old_dist_head, new_dist_head, 1)

# Update buildWarpStarfield with scale parameter
old_warp_head = """    function buildWarpStarfield() {
      const palette = [
        { r: 1.0, g: 1.0, b: 1.0 },       // Diamond white (70%)
        { r: 0.82, g: 0.90, b: 1.0 },      // Celestial soft blue (15%)
        { r: 0.22, g: 0.74, b: 0.97 },     // Electric cyan (7%)
        { r: 0.75, g: 0.52, b: 0.98 },     // Cosmic violet (5%)
        { r: 0.96, g: 0.45, b: 0.72 }      // Magenta energy (3%)
      ];

      for (let i = 0; i < WARP_STAR_COUNT; i++) {"""

new_warp_head = """    function buildWarpStarfield(scale = 1.0) {
      const palette = [
        { r: 1.0, g: 1.0, b: 1.0 },       // Diamond white (70%)
        { r: 0.82, g: 0.90, b: 1.0 },      // Celestial soft blue (15%)
        { r: 0.22, g: 0.74, b: 0.97 },     // Electric cyan (7%)
        { r: 0.75, g: 0.52, b: 0.98 },     // Cosmic violet (5%)
        { r: 0.96, g: 0.45, b: 0.72 }      // Magenta energy (3%)
      ];

      const activeWarpCount = Math.floor(WARP_STAR_COUNT * scale);
      for (let i = 0; i < activeWarpCount; i++) {"""

assert old_warp_head in code, "old_warp_head not found"
code = code.replace(old_warp_head, new_warp_head, 1)

# Update animateUniverseCinematic with tab visibility check and clean shapes
old_anim_head = """    function animateUniverseCinematic() {
      requestAnimationFrame(animateUniverseCinematic);

      const elapsed = clock.getElapsedTime();"""

new_anim_head = """    let isTabVisible = true;
    document.addEventListener('visibilitychange', () => {
      isTabVisible = (document.visibilityState === 'visible');
      if (isTabVisible && clock) {
        clock.getDelta(); // prevent delta jumps
      }
    });

    function animateUniverseCinematic() {
      requestAnimationFrame(animateUniverseCinematic);
      if (!isTabVisible) return; // Pause expensive rendering when tab is hidden

      const elapsed = clock.getElapsedTime();"""

assert old_anim_head in code, "old_anim_head not found"
code = code.replace(old_anim_head, new_anim_head, 1)

# Clean up animateUniverseCinematic spatial destinations and product worlds updates
old_anim_tail = """      // Animate Spatial Destinations & Toggle Visibility based on scroll journey
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
      });"""

new_anim_tail = """      // Deep space Milky Way and starfield continuously accompany camera flight"""

assert old_anim_tail in code, "old_anim_tail not found"
code = code.replace(old_anim_tail, new_anim_tail, 1)

# Add Mobile Drawer wiring in setupInteractivity or at init
drawer_js = """
      // Setup Mobile Navigation Drawer
      const toggleBtn = document.getElementById('mobileMenuToggle');
      const drawer = document.getElementById('mobileDrawer');
      const closeBtn = document.getElementById('mobileDrawerClose');
      if (toggleBtn && drawer) {
        toggleBtn.addEventListener('click', (e) => {
          e.stopPropagation();
          drawer.classList.toggle('open');
        });
        if (closeBtn) {
          closeBtn.addEventListener('click', () => drawer.classList.remove('open'));
        }
        drawer.querySelectorAll('.drawer-link').forEach(link => {
          link.addEventListener('click', () => drawer.classList.remove('open'));
        });
        document.addEventListener('click', (e) => {
          if (drawer.classList.contains('open') && !drawer.contains(e.target) && !toggleBtn.contains(e.target)) {
            drawer.classList.remove('open');
          }
        });
      }
"""
assert "setupInteractivity();" in code, "setupInteractivity() call not found"
code = code.replace("setupInteractivity();", "setupInteractivity();\n" + drawer_js, 1)

with open(TARGET_PATH, "w", encoding="utf-8") as f:
    f.write(code)

print("SUCCESS: assemble_ultimate_3d_universe.py updated with all enhancements!")
