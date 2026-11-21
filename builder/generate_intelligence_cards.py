# builder/generate_intelligence_cards.py
import re

POPUP_CSS = """
    /* =========================================================
       NIVORA PRODUCT INTELLIGENCE CARD (CONCEPT POPUP SYSTEM)
       ========================================================= */
    :root {
      --card-accent: #21d9ff;
      --card-glow: rgba(33, 217, 255, 0.22);
      --card-badge-bg: rgba(33, 217, 255, 0.12);
      --card-badge-border: rgba(33, 217, 255, 0.35);
    }

    /* Product Specific Themes */
    .theme-checkra {
      --card-accent: #21d9ff;
      --card-glow: rgba(33, 217, 255, 0.22);
      --card-badge-bg: rgba(33, 217, 255, 0.12);
      --card-badge-border: rgba(33, 217, 255, 0.35);
    }
    .theme-homora {
      --card-accent: #21d9ff;
      --card-glow: rgba(33, 217, 255, 0.22);
      --card-badge-bg: rgba(33, 217, 255, 0.12);
      --card-badge-border: rgba(33, 217, 255, 0.35);
    }
    .theme-bubora {
      --card-accent: #ec6dff;
      --card-glow: rgba(236, 109, 255, 0.22);
      --card-badge-bg: rgba(236, 109, 255, 0.12);
      --card-badge-border: rgba(236, 109, 255, 0.35);
    }
    .theme-sayora {
      --card-accent: #24d8a7;
      --card-glow: rgba(36, 216, 167, 0.24);
      --card-badge-bg: rgba(36, 216, 167, 0.12);
      --card-badge-border: rgba(36, 216, 167, 0.35);
    }

    /* Body Scroll Lock */
    body.modal-scroll-locked {
      position: fixed;
      left: 0;
      right: 0;
      width: 100%;
      overflow: hidden;
      touch-action: none;
    }

    /* Fixed Popup Overlay */
    .concept-modal-overlay {
      position: fixed;
      inset: 0;
      z-index: 10000;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: clamp(14px, 3vw, 32px);
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
      transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.3s ease;
    }

    .concept-modal-overlay.active {
      opacity: 1;
      visibility: visible;
      pointer-events: auto;
    }

    /* Dimmed Glass Backdrop */
    .concept-modal-backdrop {
      position: absolute;
      inset: 0;
      background: rgba(4, 5, 12, 0.82);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
    }

    /* Centered Product Intelligence Card Window */
    .concept-modal-window {
      position: relative;
      z-index: 2;
      width: min(92vw, 980px);
      max-height: min(88vh, 860px);
      display: flex;
      flex-direction: column;
      border-radius: 24px;
      border: 1px solid rgba(255, 255, 255, 0.13);
      background: linear-gradient(165deg, rgba(16, 18, 38, 0.96), rgba(6, 7, 16, 0.99));
      box-shadow: 0 35px 100px rgba(0, 0, 0, 0.85), 0 0 70px var(--card-glow);
      overflow: hidden;
      transform: scale(0.96) translateY(12px);
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease, border-color 0.3s ease;
    }

    .concept-modal-overlay.active .concept-modal-window {
      transform: scale(1) translateY(0);
    }

    /* Sticky Popup Header */
    .popup-header {
      flex-shrink: 0;
      padding: 18px 28px 16px;
      background: rgba(12, 14, 28, 0.92);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      position: relative;
      z-index: 5;
    }

    /* Small NIVORA Top Branding Row */
    .popup-brand-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 14px;
    }

    .popup-nivora-brand {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      padding: 3px 10px 3px 6px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      font-size: 10px;
      font-weight: 800;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: #c4c6dc;
    }

    .popup-nivora-mark {
      width: 15px;
      height: 15px;
      object-fit: contain;
    }

    .popup-close-btn {
      width: 36px;
      height: 36px;
      border-radius: 10px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #c5c7dc;
      display: grid;
      place-items: center;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .popup-close-btn:hover {
      background: rgba(255, 255, 255, 0.15);
      color: #ffffff;
      border-color: rgba(255, 255, 255, 0.3);
      transform: scale(1.06);
    }

    /* Product Identity Bar */
    .popup-identity {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .popup-logo-box {
      width: 52px;
      height: 52px;
      border-radius: 14px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 6px;
      display: grid;
      place-items: center;
      flex-shrink: 0;
    }

    .popup-logo-img {
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      filter: drop-shadow(0 4px 10px rgba(0, 0, 0, 0.5));
    }

    .popup-title-group {
      min-width: 0;
      flex: 1;
    }

    .popup-name-row {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .popup-product-name {
      font-size: 20px;
      font-weight: 850;
      letter-spacing: -0.02em;
      color: #ffffff;
    }

    .popup-status-badge {
      font-size: 9.5px;
      font-weight: 800;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      padding: 3px 8px;
      border-radius: 999px;
      background: var(--card-badge-bg);
      border: 1px solid var(--card-badge-border);
      color: var(--card-accent);
    }

    .popup-tagline {
      font-size: 13px;
      font-weight: 600;
      color: var(--card-accent);
      margin-top: 2px;
    }

    /* Scrollable Popup Body */
    .popup-body {
      flex: 1;
      overflow-y: auto;
      overflow-x: hidden;
      padding: 24px 28px 28px;
      scroll-behavior: smooth;
      -webkit-overflow-scrolling: touch;
    }

    .popup-body::-webkit-scrollbar {
      width: 6px;
    }
    .popup-body::-webkit-scrollbar-track {
      background: transparent;
    }
    .popup-body::-webkit-scrollbar-thumb {
      background: rgba(255, 255, 255, 0.14);
      border-radius: 999px;
    }
    .popup-body::-webkit-scrollbar-thumb:hover {
      background: rgba(255, 255, 255, 0.25);
    }

    /* Product Views inside Popup */
    .popup-product-view {
      display: none;
    }
    .popup-product-view.active {
      display: block;
      animation: popupViewFade 0.28s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @keyframes popupViewFade {
      from { opacity: 0; transform: translateY(8px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Concise About Section */
    .popup-about-block {
      margin-bottom: 24px;
    }

    .popup-section-kicker {
      font-size: 10px;
      font-weight: 850;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: var(--card-accent);
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .popup-about-desc {
      font-size: 14.5px;
      line-height: 1.7;
      color: #e0e2f2;
      font-weight: 500;
    }

    /* Capabilities Grid (Compact Cards) */
    .popup-capabilities-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      margin-bottom: 24px;
    }

    .popup-cap-card {
      padding: 15px 14px;
      border-radius: 13px;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.07);
      transition: all 0.22s ease;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .popup-cap-card:hover {
      background: rgba(255, 255, 255, 0.06);
      border-color: rgba(255, 255, 255, 0.18);
      transform: translateY(-2px);
    }

    .pcc-icon {
      width: 30px;
      height: 30px;
      border-radius: 8px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.09);
      display: grid;
      place-items: center;
      color: var(--card-accent);
      flex-shrink: 0;
    }

    .popup-cap-card h5 {
      font-size: 13px;
      font-weight: 750;
      color: #ffffff;
      letter-spacing: -0.01em;
    }

    .popup-cap-card p {
      font-size: 11.5px;
      line-height: 1.55;
      color: #9ba0b6;
    }

    /* Core Idea & Vision Highlight Box */
    .popup-vision-banner {
      padding: 20px 22px;
      border-radius: 15px;
      background: radial-gradient(circle at 50% 50%, var(--card-glow), transparent 70%), rgba(255, 255, 255, 0.025);
      border: 1px solid rgba(255, 255, 255, 0.10);
      margin-bottom: 24px;
      position: relative;
    }

    .pvb-quote {
      font-size: 16px;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: #ffffff;
      line-height: 1.45;
      margin-bottom: 8px;
    }

    .pvb-desc {
      font-size: 12px;
      color: #9ea3ba;
      line-height: 1.6;
    }

    /* Fixed Popup Bottom Action Bar */
    .popup-footer-bar {
      padding-top: 18px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      flex-wrap: wrap;
    }

    .pfb-left {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .pfb-nav-label {
      font-size: 11px;
      color: #84889e;
      font-weight: 600;
    }

    .pfb-switch-btn {
      padding: 6px 11px;
      border-radius: 8px;
      font-size: 11px;
      font-weight: 700;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: #c4c6dc;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .pfb-switch-btn:hover {
      background: rgba(255, 255, 255, 0.09);
      color: #ffffff;
      border-color: rgba(255, 255, 255, 0.2);
    }

    .pfb-right {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .pfb-cta-btn {
      padding: 9px 18px;
      font-size: 13px;
      font-weight: 750;
      border-radius: 10px;
    }

    /* Responsive Adaptation */
    @media (max-width: 900px) {
      .popup-capabilities-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    @media (max-width: 600px) {
      .concept-modal-overlay {
        padding: 10px;
      }
      .concept-modal-window {
        width: 100%;
        max-height: 94dvh;
        border-radius: 18px;
      }
      .popup-header {
        padding: 14px 18px;
      }
      .popup-body {
        padding: 18px 18px 22px;
      }
      .popup-capabilities-grid {
        grid-template-columns: 1fr;
      }
      .popup-footer-bar {
        flex-direction: column;
        align-items: stretch;
        gap: 12px;
      }
      .pfb-left {
        justify-content: center;
        flex-wrap: wrap;
      }
      .pfb-right {
        justify-content: stretch;
      }
      .pfb-cta-btn {
        width: 100%;
        justify-content: center;
      }
    }
"""

POPUP_HTML = """
  <!-- =========================================================
       NIVORA PRODUCT INTELLIGENCE CARD (CONCEPT POPUP)
       ========================================================= -->
  <div id="conceptModalOverlay" class="concept-modal-overlay" role="dialog" aria-modal="true" aria-hidden="true">
    <div class="concept-modal-backdrop" onclick="closeConceptModal()"></div>

    <div class="concept-modal-window" id="conceptModalWindow">
      <!-- STICKY HEADER -->
      <header class="popup-header">
        <div class="popup-brand-row">
          <div class="popup-nivora-brand">
            <img src="assets/images/nivora-logo.png" alt="NIVORA" class="popup-nivora-mark">
            <span>NIVORA UNIVERSE</span>
          </div>
          <button type="button" class="popup-close-btn" id="modalCloseBtn" onclick="closeConceptModal()" aria-label="Close product concept card (ESC)">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>
        </div>

        <div class="popup-identity">
          <div class="popup-logo-box">
            <img id="popupLogo-checkra" class="popup-logo-img" src="assets/images/checkra-logo.png" alt="CHECKRA Logo">
            <img id="popupLogo-homora" class="popup-logo-img" src="assets/images/homora-logo.png" alt="HOMORA Logo" style="display:none;">
            <img id="popupLogo-bubora" class="popup-logo-img" src="assets/images/bubora-logo.png" alt="BUBORA Logo" style="display:none;">
            <img id="popupLogo-sayora" class="popup-logo-img" src="assets/images/sayora-logo.png" alt="SAYORA Logo" style="display:none;">
          </div>
          <div class="popup-title-group">
            <div class="popup-name-row">
              <span id="popupProductName" class="popup-product-name">CHECKRA</span>
              <span id="popupStatusBadge" class="popup-status-badge">Live App</span>
            </div>
            <div id="popupTagline" class="popup-tagline">Writing Integrity &amp; Plagiarism Intelligence</div>
          </div>
        </div>
      </header>

      <!-- SCROLLABLE CONTENT BODY -->
      <div class="popup-body" id="conceptModalBody">

        <!-- =========================================================
             1. CHECKRA INTELLIGENCE CARD
             ========================================================= -->
        <div class="popup-product-view active" id="modal-view-checkra">
          <div class="popup-about-block">
            <div class="popup-section-kicker">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
              <span>ABOUT CHECKRA</span>
            </div>
            <p class="popup-about-desc">
              CHECKRA is an AI-powered writing integrity and source verification platform designed to help students, researchers, educators, and professionals check, verify, and improve their written work in one connected workspace. Rather than punitive scores, CHECKRA provides transparent evidence to understand and elevate writing.
            </p>
          </div>

          <!-- Capabilities Grid (6 Core Cards) -->
          <div class="popup-capabilities-grid">
            <div class="popup-cap-card">
              <div class="pcc-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
              </div>
              <h5>Similarity Check</h5>
              <p>Multi-level detection covering exact verbatim, near phrasing, and deep semantic matching.</p>
            </div>

            <div class="popup-cap-card">
              <div class="pcc-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
              </div>
              <h5>Source Verification</h5>
              <p>Indexes open web resources with direct citation links and transparent context.</p>
            </div>

            <div class="popup-cap-card">
              <div class="pcc-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line></svg>
              </div>
              <h5>Document Analysis</h5>
              <p>Unified ingestion of PDF, DOCX, TXT, HTML, and Markdown with chapter parsing.</p>
            </div>

            <div class="popup-cap-card">
              <div class="pcc-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg>
              </div>
              <h5>Grammar &amp; Rewrite</h5>
              <p>Identifies grammar flaws and provides 5 tailored rewriting styles with clear diffs.</p>
            </div>

            <div class="popup-cap-card">
              <div class="pcc-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><line x1="12" y1="18" x2="12" y2="12"></line><line x1="9" y1="15" x2="15" y2="15"></line></svg>
              </div>
              <h5>Evidence Reports</h5>
              <p>Structured audit summaries with matched excerpts, classification, and source URLs.</p>
            </div>

            <div class="popup-cap-card">
              <div class="pcc-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
              </div>
              <h5>Privacy &amp; Security</h5>
              <p>Session-based processing with zero permanent text retention to safeguard intellectual property.</p>
            </div>
          </div>

          <!-- Core Idea & Vision -->
          <div class="popup-vision-banner">
            <div class="popup-section-kicker">
              <span>CORE IDEA &amp; VISION</span>
            </div>
            <div class="pvb-quote">&ldquo;Don&rsquo;t just check the writing. Understand it, verify it, and improve it.&rdquo;</div>
            <p class="pvb-desc">CHECKRA aims to become a trusted intelligent writing companion — helping people create original, credible, and well-written content through transparent evidence-based analysis.</p>
          </div>

          <!-- Bottom Footer -->
          <div class="popup-footer-bar">
            <div class="pfb-left">
              <span class="pfb-nav-label">Switch:</span>
              <button type="button" class="pfb-switch-btn" onclick="openConceptModal('homora')">HOMORA →</button>
              <button type="button" class="pfb-switch-btn" onclick="openConceptModal('bubora')">BUBORA →</button>
              <button type="button" class="pfb-switch-btn" onclick="openConceptModal('sayora')">SAYORA →</button>
            </div>
            <div class="pfb-right">
              <a class="btn primary pfb-cta-btn" href="https://checkra-xi.vercel.app/" target="_blank" rel="noopener noreferrer">
                <span>Visit CHECKRA App</span>
                <span class="btn-arrow">↗</span>
              </a>
            </div>
          </div>
        </div>


        <!-- =========================================================
             2. HOMORA INTELLIGENCE CARD
             ========================================================= -->
        <div class="popup-product-view" id="modal-view-homora">
          <div class="popup-about-block">
            <div class="popup-section-kicker">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
              <span>ABOUT HOMORA</span>
            </div>
            <p class="popup-about-desc">
              HOMORA is an intelligent household finance platform designed to help roommates, shared households, couples, and co-living communities manage money, expenses, bills, responsibilities, and financial decisions in one connected ecosystem — turning awkward money conversations into transparent domestic harmony.
            </p>
          </div>

          <!-- Capabilities Grid (6 Core Cards) -->
          <div class="popup-capabilities-grid">
            <div class="popup-cap-card">
              <div class="pcc-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
              </div>
              <h5>Shared Balances</h5>
              <p>Transparent real-time balances with automated debt simplification netting.</p>
            </div>

            <div class="popup-cap-card">
              <div class="pcc-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
              </div>
              <h5>Automated Budgeting</h5>
              <p>Target monthly caps for rent, utilities, food, and social buffers with pace alerts.</p>
            </div>

            <div class="popup-cap-card">
              <div class="pcc-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 14 14"></polyline></svg>
              </div>
              <h5>Fair Contribution Splits</h5>
              <p>Support for equal, percentage, room-size, or income-weighted split calculations.</p>
            </div>

            <div class="popup-cap-card">
              <div class="pcc-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
              </div>
              <h5>Emergency Pool &amp; Claims</h5>
              <p>A communal household buffer for sudden repairs with one-tap reimbursement claims.</p>
            </div>

            <div class="popup-cap-card">
              <div class="pcc-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>
              </div>
              <h5>Groceries &amp; Chores</h5>
              <p>Synchronized pantry replenishment lists and rotational household cleaning duties.</p>
            </div>

            <div class="popup-cap-card">
              <div class="pcc-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10H12V2z"></path><path d="M12 12 2.1 10.5"></path></svg>
              </div>
              <h5>HOMORA Intel Copilot</h5>
              <p>AI copilot surfacing category spend trends and proactive waste reduction suggestions.</p>
            </div>
          </div>

          <!-- Core Idea & Vision -->
          <div class="popup-vision-banner">
            <div class="popup-section-kicker">
              <span>CORE IDEA &amp; VISION</span>
            </div>
            <div class="pvb-quote">&ldquo;Shared Living. Shared Responsibility. Smarter Money.&rdquo;</div>
            <p class="pvb-desc">HOMORA aims to make shared living financially transparent, organized, intelligent, and stress-free — functioning as a complete Household Financial Operating System.</p>
          </div>

          <!-- Bottom Footer -->
          <div class="popup-footer-bar">
            <div class="pfb-left">
              <span class="pfb-nav-label">Switch:</span>
              <button type="button" class="pfb-switch-btn" onclick="openConceptModal('checkra')">CHECKRA →</button>
              <button type="button" class="pfb-switch-btn" onclick="openConceptModal('bubora')">BUBORA →</button>
              <button type="button" class="pfb-switch-btn" onclick="openConceptModal('sayora')">SAYORA →</button>
            </div>
            <div class="pfb-right">
              <a class="btn primary pfb-cta-btn" href="https://homora-ai.vercel.app/" target="_blank" rel="noopener noreferrer">
                <span>Visit HOMORA Prototype</span>
                <span class="btn-arrow">↗</span>
              </a>
            </div>
          </div>
        </div>


        <!-- =========================================================
             3. BUBORA INTELLIGENCE CARD
             ========================================================= -->
        <div class="popup-product-view" id="modal-view-bubora">
          <div class="popup-about-block">
            <div class="popup-section-kicker">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
              <span>ABOUT BUBORA</span>
            </div>
            <p class="popup-about-desc">
              BUBORA is a private digital space designed exclusively for two people to build, organize, and preserve their life together in one secure sanctuary. Free from public social feeds, intrusive algorithms, and advertising noise, BUBORA gives couple life a dedicated, intimate home.
            </p>
          </div>

          <!-- Capabilities Grid (6 Core Cards) -->
          <div class="popup-capabilities-grid">
            <div class="popup-cap-card">
              <div class="pcc-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
              </div>
              <h5>Our Chat</h5>
              <p>Dedicated private messaging channel with pinned memories, voice notes, and zero external alerts.</p>
            </div>

            <div class="popup-cap-card">
              <div class="pcc-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
              </div>
              <h5>Memories Timeline</h5>
              <p>An interactive chronological timeline capturing first dates, trips, holidays, and milestones.</p>
            </div>

            <div class="popup-cap-card">
              <div class="pcc-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
              </div>
              <h5>Shared Calendar</h5>
              <p>Synchronized calendar with live countdown timers for anniversaries, flights, and date nights.</p>
            </div>

            <div class="popup-cap-card">
              <div class="pcc-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="3 11 22 2 13 21 11 13 3 11"></polygon></svg>
              </div>
              <h5>Plans &amp; Trips</h5>
              <p>Collaborative travel itineraries with hotel details, flight bookings, and packing checklists.</p>
            </div>

            <div class="popup-cap-card">
              <div class="pcc-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
              </div>
              <h5>Our Money</h5>
              <p>Gentle joint expense tracking without awkward balance demands — keeping finances harmonious.</p>
            </div>

            <div class="popup-cap-card">
              <div class="pcc-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
              </div>
              <h5>Private Vault</h5>
              <p>Encrypted vault for private notes, door codes, passports, and cherished letters.</p>
            </div>
          </div>

          <!-- Core Idea & Vision -->
          <div class="popup-vision-banner">
            <div class="popup-section-kicker">
              <span>CORE IDEA &amp; VISION</span>
            </div>
            <div class="pvb-quote">&ldquo;A relationship has many little moments. Bubora gives those moments one little world.&rdquo;</div>
            <p class="pvb-desc">BUBORA aims to become a complete digital companion for couples — helping them communicate better, remember more, plan together, and build their future side by side with uncompromised privacy.</p>
          </div>

          <!-- Bottom Footer -->
          <div class="popup-footer-bar">
            <div class="pfb-left">
              <span class="pfb-nav-label">Switch:</span>
              <button type="button" class="pfb-switch-btn" onclick="openConceptModal('checkra')">CHECKRA →</button>
              <button type="button" class="pfb-switch-btn" onclick="openConceptModal('homora')">HOMORA →</button>
              <button type="button" class="pfb-switch-btn" onclick="openConceptModal('sayora')">SAYORA →</button>
            </div>
            <div class="pfb-right">
              <a class="btn primary pfb-cta-btn" href="https://bubora.netlify.app/" target="_blank" rel="noopener noreferrer">
                <span>Visit BUBORA App</span>
                <span class="btn-arrow">↗</span>
              </a>
            </div>
          </div>
        </div>


        <!-- =========================================================
             4. SAYORA INTELLIGENCE CARD
             ========================================================= -->
        <div class="popup-product-view" id="modal-view-sayora">
          <div class="popup-about-block">
            <div class="popup-section-kicker">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
              <span>ABOUT SAYORA</span>
            </div>
            <p class="popup-about-desc">
              SAYORA is a social-impact fintech and financial resilience platform designed to help informal workers, gig workers, daily-wage earners, street vendors, drivers, and communities save, contribute, access emergency support, and build a safer financial future with dignity.
            </p>
          </div>

          <!-- Capabilities Grid (6 Core Cards) -->
          <div class="popup-capabilities-grid">
            <div class="popup-cap-card">
              <div class="pcc-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
              </div>
              <h5>Smart Micro-Savings</h5>
              <p>Frictionless daily micro-roundups into an individual protected emergency cushion.</p>
            </div>

            <div class="popup-cap-card">
              <div class="pcc-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
              </div>
              <h5>Financial Protection</h5>
              <p>Mutual aid pool absorbing shocks from vehicle breakdowns and sudden hospital bills.</p>
            </div>

            <div class="popup-cap-card">
              <div class="pcc-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"></path></svg>
              </div>
              <h5>Climate &amp; Crisis Relief</h5>
              <p>Parametric relief alerts during severe heatwaves, monsoons, floods, and curfews.</p>
            </div>

            <div class="popup-cap-card">
              <div class="pcc-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
              </div>
              <h5>CSR Matching Grants</h5>
              <p>Integration channel for platforms and philanthropic foundations to match savings 1:1.</p>
            </div>

            <div class="popup-cap-card">
              <div class="pcc-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
              </div>
              <h5>Welfare Schemes Match</h5>
              <p>Automated discovery pairing workers with official government social security boards.</p>
            </div>

            <div class="popup-cap-card">
              <div class="pcc-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="16" rx="2"></rect><circle cx="9" cy="10" r="2"></circle><line x1="15" y1="8" x2="17" y2="8"></line><line x1="15" y1="12" x2="17" y2="12"></line><line x1="7" y1="16" x2="17" y2="16"></line></svg>
              </div>
              <h5>Digital SAYORA ID</h5>
              <p>Portable digital credential consolidating work tenure and safety ratings.</p>
            </div>
          </div>

          <!-- Core Idea & Vision -->
          <div class="popup-vision-banner">
            <div class="popup-section-kicker">
              <span>CORE IDEA &amp; VISION</span>
            </div>
            <div class="pvb-quote">&ldquo;Small Steps. Stronger Communities.&rdquo;</div>
            <p class="pvb-desc">SAYORA aims to become a trusted financial resilience companion for gig workers and communities — helping people build savings, prepare for emergencies, and create a safer tomorrow.</p>
          </div>

          <!-- Bottom Footer -->
          <div class="popup-footer-bar">
            <div class="pfb-left">
              <span class="pfb-nav-label">Switch:</span>
              <button type="button" class="pfb-switch-btn" onclick="openConceptModal('checkra')">CHECKRA →</button>
              <button type="button" class="pfb-switch-btn" onclick="openConceptModal('homora')">HOMORA →</button>
              <button type="button" class="pfb-switch-btn" onclick="openConceptModal('bubora')">BUBORA →</button>
            </div>
            <div class="pfb-right">
              <a class="btn primary pfb-cta-btn" href="#contact" onclick="closeConceptModal(); document.getElementById('contact').scrollIntoView({behavior:'smooth'})">
                <span>Connect With R&amp;D</span>
                <span class="btn-arrow">→</span>
              </a>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
"""

POPUP_JS = """
    // -------------------------------------------------------------
    // NIVORA Product Intelligence Card (Concept Popup Controller)
    // -------------------------------------------------------------
    var currentModalKey = null;
    var savedPageScrollY = 0;
    var lastModalFocusTrigger = null;

    var productPopupConfig = {
      checkra: {
        name: "CHECKRA",
        tagline: "Writing Integrity & Plagiarism Intelligence",
        badge: "Live App",
        isConcept: false,
        themeClass: "theme-checkra"
      },
      homora: {
        name: "HOMORA",
        tagline: "AI-Powered Financial Harmony for Shared Living",
        badge: "Active Prototype",
        isConcept: false,
        themeClass: "theme-homora"
      },
      bubora: {
        name: "BUBORA",
        tagline: "A Private Digital Home for Two",
        badge: "Live App",
        isConcept: false,
        themeClass: "theme-bubora"
      },
      sayora: {
        name: "SAYORA",
        tagline: "Financial Resilience for Workers & Communities",
        badge: "Concept · In Development",
        isConcept: true,
        themeClass: "theme-sayora"
      }
    };

    function openConceptModal(productKey, triggerEl) {
      if (!productPopupConfig[productKey]) return;
      currentModalKey = productKey;
      var conf = productPopupConfig[productKey];

      // Save scroll position and trigger element
      if (!document.body.classList.contains('modal-scroll-locked')) {
        savedPageScrollY = window.pageYOffset || document.documentElement.scrollTop;
      }
      if (triggerEl) {
        lastModalFocusTrigger = triggerEl;
      }

      // Lock body scroll precisely without visual jumping
      document.body.style.top = '-' + savedPageScrollY + 'px';
      document.body.classList.add('modal-scroll-locked');

      // Update Header Data
      var modalWindow = document.getElementById('conceptModalWindow');
      var popupProductName = document.getElementById('popupProductName');
      var popupStatusBadge = document.getElementById('popupStatusBadge');
      var popupTagline = document.getElementById('popupTagline');

      if (modalWindow) {
        modalWindow.className = 'concept-modal-window ' + conf.themeClass;
      }
      if (popupProductName) popupProductName.textContent = conf.name;
      if (popupTagline) popupTagline.textContent = conf.tagline;
      if (popupStatusBadge) {
        popupStatusBadge.textContent = conf.badge;
      }

      // Toggle Logos
      ['checkra', 'homora', 'bubora', 'sayora'].forEach(function(k) {
        var logoImg = document.getElementById('popupLogo-' + k);
        if (logoImg) {
          logoImg.style.display = (k === productKey) ? 'block' : 'none';
        }
      });

      // Toggle Product Views
      ['checkra', 'homora', 'bubora', 'sayora'].forEach(function(k) {
        var view = document.getElementById('modal-view-' + k);
        if (view) {
          if (k === productKey) {
            view.classList.add('active');
          } else {
            view.classList.remove('active');
          }
        }
      });

      // Reset modal body scroll to top
      var modalBody = document.getElementById('conceptModalBody');
      if (modalBody) {
        modalBody.scrollTop = 0;
      }

      // Show Overlay
      var overlay = document.getElementById('conceptModalOverlay');
      if (overlay) {
        overlay.classList.add('active');
        overlay.setAttribute('aria-hidden', 'false');
      }

      // Move focus to modal close button for accessibility
      setTimeout(function() {
        var closeBtn = document.getElementById('modalCloseBtn');
        if (closeBtn) closeBtn.focus();
      }, 100);
    }

    function closeConceptModal() {
      var overlay = document.getElementById('conceptModalOverlay');
      if (overlay) {
        overlay.classList.remove('active');
        overlay.setAttribute('aria-hidden', 'true');
      }

      // Restore body scroll position seamlessly
      document.body.classList.remove('modal-scroll-locked');
      document.body.style.top = '';
      window.scrollTo(0, savedPageScrollY);

      // Return keyboard focus to trigger
      if (lastModalFocusTrigger && lastModalFocusTrigger.focus) {
        lastModalFocusTrigger.focus();
      }
    }

    // ESC key listener to close modal
    window.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' || e.key === 'Esc') {
        var overlay = document.getElementById('conceptModalOverlay');
        if (overlay && overlay.classList.contains('active')) {
          closeConceptModal();
        }
      }
    });
"""

def generate():
    # Read the clean baseline
    with open('/tmp/original_head.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Ensure updated CHECKRA link
    html = html.replace('https://checkra.onrender.com/', 'https://checkra-xi.vercel.app/')

    # 1. Update Hero Satellites with onclick
    html = html.replace('class="satellite s-checkra"', 'class="satellite s-checkra" onclick="openConceptModal(\'checkra\', this)" title="Explore CHECKRA Concept"')
    html = html.replace('class="satellite s-homora"', 'class="satellite s-homora" onclick="openConceptModal(\'homora\', this)" title="Explore HOMORA Concept"')
    html = html.replace('class="satellite s-bubora"', 'class="satellite s-bubora" onclick="openConceptModal(\'bubora\', this)" title="Explore BUBORA Concept"')
    html = html.replace('class="satellite s-sayora"', 'class="satellite s-sayora" onclick="openConceptModal(\'sayora\', this)" title="Explore SAYORA Concept"')

    # 2. Update Product cards in #products to have the concise cards + Explore Concept button
    clean_products_grid = """        <div class="worlds-grid">
          <!-- CHECKRA CARD -->
          <article class="world-card w-checkra reveal">
            <div class="world-media">
              <img src="assets/images/checkra-logo.png" alt="CHECKRA logo" loading="lazy">
            </div>
            <div class="world-body">
              <div class="world-top">
                <div class="world-name-group">
                  <h3>CHECKRA</h3>
                  <span class="legacy-tag">Formerly VeriWrite</span>
                </div>
                <span class="status-badge live">Live App</span>
              </div>
              <div class="world-positioning">Writing Integrity &amp; Plagiarism Intelligence</div>
              <div class="capabilities-list">
                <span class="cap-pill">Similarity</span>
                <span class="cap-pill">Verification</span>
                <span class="cap-pill">AI Review</span>
              </div>
              <div class="world-footer">
                <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap;">
                  <button type="button" class="btn primary" onclick="openConceptModal('checkra', this)">
                    Explore Concept <span class="btn-arrow">→</span>
                  </button>
                  <a class="world-link" href="https://checkra-xi.vercel.app/" target="_blank" rel="noopener noreferrer">
                    Visit App <span class="btn-arrow">↗</span>
                  </a>
                </div>
                <span style="font-size:11px;color:#8f92a9;">Writing Intelligence Space</span>
              </div>
            </div>
          </article>

          <!-- HOMORA CARD -->
          <article class="world-card w-homora reveal">
            <div class="world-media">
              <img src="assets/images/homora-logo.png" alt="HOMORA logo" loading="lazy">
            </div>
            <div class="world-body">
              <div class="world-top">
                <div class="world-name-group">
                  <h3>HOMORA</h3>
                </div>
                <span class="status-badge live">Active Prototype</span>
              </div>
              <div class="world-positioning">AI-Powered Financial Harmony for Shared Living</div>
              <div class="capabilities-list">
                <span class="cap-pill">Shared Finance</span>
                <span class="cap-pill">Household Intelligence</span>
                <span class="cap-pill">Budgeting</span>
              </div>
              <div class="world-footer">
                <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap;">
                  <button type="button" class="btn primary" onclick="openConceptModal('homora', this)">
                    Explore Concept <span class="btn-arrow">→</span>
                  </button>
                  <a class="world-link" href="https://homora-ai.vercel.app/" target="_blank" rel="noopener noreferrer">
                    Visit Prototype <span class="btn-arrow">↗</span>
                  </a>
                </div>
                <span style="font-size:11px;color:#8f92a9;">Household Financial OS</span>
              </div>
            </div>
          </article>

          <!-- BUBORA CARD -->
          <article class="world-card w-bubora reveal">
            <div class="world-media">
              <img src="assets/images/bubora-logo.png" alt="BUBORA logo" loading="lazy">
            </div>
            <div class="world-body">
              <div class="world-top">
                <div class="world-name-group">
                  <h3>BUBORA</h3>
                </div>
                <span class="status-badge live">Live App</span>
              </div>
              <div class="world-positioning">A Digital Space for Couples</div>
              <div class="capabilities-list">
                <span class="cap-pill">Memories</span>
                <span class="cap-pill">Connection</span>
                <span class="cap-pill">Planning</span>
              </div>
              <div class="world-footer">
                <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap;">
                  <button type="button" class="btn primary" onclick="openConceptModal('bubora', this)">
                    Explore Concept <span class="btn-arrow">→</span>
                  </button>
                  <a class="world-link" href="https://bubora.netlify.app/" target="_blank" rel="noopener noreferrer">
                    Visit App <span class="btn-arrow">↗</span>
                  </a>
                </div>
                <span style="font-size:11px;color:#8f92a9;">Private Digital Home for Two</span>
              </div>
            </div>
          </article>

          <!-- SAYORA CARD -->
          <article class="world-card w-sayora reveal">
            <div class="world-media">
              <img src="assets/images/sayora-logo.png" alt="SAYORA logo" loading="lazy">
            </div>
            <div class="world-body">
              <div class="world-top">
                <div class="world-name-group">
                  <h3>SAYORA</h3>
                </div>
                <span class="status-badge concept">Concept · In Development</span>
              </div>
              <div class="world-positioning">Financial Resilience for Workers &amp; Communities</div>
              <div class="capabilities-list">
                <span class="cap-pill">Savings</span>
                <span class="cap-pill">Protection</span>
                <span class="cap-pill">Community Support</span>
              </div>
              <div class="world-footer">
                <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap;">
                  <button type="button" class="btn primary" onclick="openConceptModal('sayora', this)">
                    Explore Concept <span class="btn-arrow">→</span>
                  </button>
                </div>
                <span style="font-size:11px;color:#8f92a9;">Social Impact Fund</span>
              </div>
            </div>
          </article>
        </div>"""

    start_grid = html.find('<div class="worlds-grid">')
    end_grid = html.find('</section>', start_grid)
    html = html[:start_grid] + clean_products_grid + '\n      </div>\n    </section>' + html[end_grid+10:]

    # 3. Inject CSS before </style>
    style_close = "</style>"
    if style_close in html:
        html = html.replace(style_close, POPUP_CSS + "\n  " + style_close, 1)

    # 4. Inject Modal HTML right before </body>
    body_close = "</body>"
    if body_close in html:
        html = html.replace(body_close, POPUP_HTML + "\n" + body_close, 1)

    # 5. Inject Modal JS right before </script>
    script_close = "</script>"
    if script_close in html:
        html = html.replace(script_close, POPUP_JS + "\n  " + script_close, 1)

    # Save to Desktop and Downloads
    desktop_file = "/Users/bennabathulanivas/Desktop/my projects/NIVORA/index.html"
    downloads_file = "/Users/bennabathulanivas/Downloads/NIVORA/index.html"

    with open(desktop_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated clean concept intelligence popup system: {len(html)} chars written to {desktop_file}")

    with open(downloads_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated clean concept intelligence popup system: {len(html)} chars written to {downloads_file}")

if __name__ == '__main__':
    generate()
