import re
import sys

filepath = "/Users/bennabathulanivas/Desktop/my projects/NIVORA/builder/assemble_consultancy_universe.py"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Brochure Modal CSS
brochure_css = """
    /* -------------------------------------------------------------
       BROCHURE MODAL VIEWER SYSTEM
       ------------------------------------------------------------- */
    #brochureModalOverlay {
      position: fixed;
      inset: 0;
      background: rgba(3, 5, 12, 0.88);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      z-index: 99999;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
      opacity: 0;
      transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    #brochureModalOverlay.open {
      display: flex;
      opacity: 1;
    }

    .brochure-modal-container {
      background: #090d1a;
      border: 1px solid rgba(255, 255, 255, 0.14);
      border-radius: 18px;
      width: 100%;
      max-width: 1100px;
      height: 90vh;
      max-height: 960px;
      display: flex;
      flex-direction: column;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8), 0 0 40px rgba(56, 189, 248, 0.15);
      overflow: hidden;
      transform: scale(0.96) translateY(12px);
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    #brochureModalOverlay.open .brochure-modal-container {
      transform: scale(1) translateY(0);
    }

    .brochure-modal-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 1.0rem 1.5rem;
      background: rgba(13, 19, 36, 0.85);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      flex-shrink: 0;
      gap: 1.0rem;
    }

    .brochure-header-left {
      display: flex;
      flex-direction: column;
      min-width: 0;
    }

    .brochure-kicker-tag {
      font-family: var(--font-mono);
      font-size: 0.68rem;
      font-weight: 600;
      letter-spacing: 0.12em;
      color: #38bdf8;
      text-transform: uppercase;
      margin-bottom: 0.2rem;
    }

    .brochure-modal-title {
      font-family: var(--font-display);
      font-size: 1.2rem;
      font-weight: 700;
      color: #ffffff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .brochure-header-actions {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      flex-shrink: 0;
    }

    .btn-bm-download {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.55rem 1.15rem;
      background: linear-gradient(135deg, #a855f7 0%, #38bdf8 100%);
      color: #ffffff;
      font-family: var(--font-ui);
      font-size: 0.82rem;
      font-weight: 600;
      border-radius: var(--radius-pill);
      text-decoration: none;
      transition: all 0.2s ease;
      box-shadow: 0 4px 14px rgba(56, 189, 248, 0.3);
    }

    .btn-bm-download:hover {
      box-shadow: 0 6px 20px rgba(56, 189, 248, 0.5);
      transform: translateY(-1px);
    }

    .btn-bm-tab {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.55rem 0.95rem;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.14);
      color: #cbd5e1;
      font-family: var(--font-ui);
      font-size: 0.8rem;
      font-weight: 500;
      border-radius: var(--radius-pill);
      text-decoration: none;
      transition: all 0.2s ease;
    }

    .btn-bm-tab:hover {
      background: rgba(255, 255, 255, 0.12);
      color: #ffffff;
    }

    .btn-bm-close {
      width: 36px;
      height: 36px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 50%;
      color: #cbd5e1;
      font-size: 1.35rem;
      line-height: 1;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .btn-bm-close:hover {
      background: rgba(239, 68, 68, 0.2);
      border-color: rgba(239, 68, 68, 0.5);
      color: #ffffff;
    }

    .brochure-modal-viewport {
      flex: 1;
      background: #050811;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }

    .brochure-pdf-frame {
      width: 100%;
      height: 100%;
      border: none;
      background: #0b0f19;
    }

    .brochure-modal-footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.85rem 1.5rem;
      background: rgba(13, 19, 36, 0.9);
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      flex-shrink: 0;
      gap: 1.0rem;
    }

    .brochure-footer-text {
      font-size: 0.84rem;
      color: #94a3b8;
    }

    .btn-bm-enquire {
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      padding: 0.5rem 1.1rem;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-radius: var(--radius-pill);
      color: #38bdf8;
      font-family: var(--font-ui);
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .btn-bm-enquire:hover {
      background: rgba(56, 189, 248, 0.15);
      border-color: rgba(56, 189, 248, 0.7);
      color: #ffffff;
    }

    @media (max-width: 768px) {
      #brochureModalOverlay {
        padding: 0.5rem;
      }
      .brochure-modal-container {
        height: 94vh;
        border-radius: 14px;
      }
      .brochure-modal-header {
        padding: 0.75rem 1.0rem;
      }
      .brochure-modal-title {
        font-size: 1.05rem;
      }
      .brochure-header-actions {
        gap: 0.4rem;
      }
      .btn-bm-tab {
        display: none;
      }
      .brochure-modal-footer {
        flex-direction: column;
        align-items: stretch;
        gap: 0.6rem;
        padding: 0.75rem 1.0rem;
        text-align: center;
      }
      .btn-bm-enquire {
        justify-content: center;
      }
    }
"""

# Insert brochure CSS before RESPONSIVE MEDIA QUERIES
target_css_insert = "    /* -------------------------------------------------------------\n       RESPONSIVE MEDIA QUERIES"
if target_css_insert in content:
    content = content.replace(target_css_insert, brochure_css + "\n" + target_css_insert, 1)
    print("Inserted brochure CSS")
else:
    print("ERROR: target_css_insert not found")
    sys.exit(1)

# Update responsive services-grid in @media (max-width: 1024px)
old_1024 = """      .services-grid {
        grid-template-columns: 1fr;
      }"""
new_1024 = """      .services-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 1.15rem;
      }"""
if old_1024 in content:
    content = content.replace(old_1024, new_1024, 1)
    print("Updated 1024px services-grid")
else:
    print("WARNING: old_1024 not found")

# Update responsive in @media (max-width: 640px)
old_640_service = """      .service-card {
        padding: 1.8rem 1.4rem;
      }"""
new_640_service = """      .services-grid {
        grid-template-columns: 1fr;
        gap: 1.0rem;
      }
      .service-card {
        padding: 1.35rem 1.15rem;
      }"""
if old_640_service in content:
    content = content.replace(old_640_service, new_640_service, 1)
    print("Updated 640px service-card & services-grid")
else:
    print("WARNING: old_640_service not found")

# 2. Replace Services Section HTML with Compact Small Cards
old_services_pattern = r'<div class="services-grid">.*?<!-- SERVICE 1: ACCOUNTING & BOOKKEEPING -->.*?<\/div>\s*<\/div>\s*<\/section>\s*<!-- =========================================================\s*SECTION 02: BUSINESS SOLUTIONS'

new_services_html = """<div class="services-grid">
          <!-- SERVICE 1: ACCOUNTING & BOOKKEEPING -->
          <article class="service-card" onclick="openBrochureModal('accounting')" title="Click to explore and view brochure">
            <div class="service-header">
              <div class="service-kicker">01 &middot; Core Records</div>
              <h3 class="service-title">Accounting &amp; Bookkeeping</h3>
            </div>
            <p class="service-desc">
              Accurate, organized and management-ready financial records with structured ledger maintenance, bank reconciliation and reporting support.
            </p>
            <div class="service-card-bottom">
              <button type="button" class="btn-service-explore" onclick="event.stopPropagation(); openBrochureModal('accounting')">
                <span>Explore &amp; Brochure</span>
                <span class="explore-arrow">&rarr;</span>
              </button>
            </div>
          </article>

          <!-- SERVICE 2: INCOME TAX SERVICES -->
          <article class="service-card" onclick="openBrochureModal('income-tax')" title="Click to explore and view brochure">
            <div class="service-header">
              <div class="service-kicker">02 &middot; Direct Tax</div>
              <h3 class="service-title">Income Tax Services</h3>
            </div>
            <p class="service-desc">
              Practical income-tax compliance, advance tax computation, and planning support for individuals, professionals and businesses.
            </p>
            <div class="service-card-bottom">
              <button type="button" class="btn-service-explore" onclick="event.stopPropagation(); openBrochureModal('income-tax')">
                <span>Explore &amp; Brochure</span>
                <span class="explore-arrow">&rarr;</span>
              </button>
            </div>
          </article>

          <!-- SERVICE 3: GST SERVICES -->
          <article class="service-card" onclick="openBrochureModal('gst')" title="Click to explore and view brochure">
            <div class="service-header">
              <div class="service-kicker">03 &middot; Indirect Tax</div>
              <h3 class="service-title">GST Services</h3>
            </div>
            <p class="service-desc">
              End-to-end GST compliance support from registration, return preparation (GSTR-1, 3B, 9) to reconciliation and refund documentation.
            </p>
            <div class="service-card-bottom">
              <button type="button" class="btn-service-explore" onclick="event.stopPropagation(); openBrochureModal('gst')">
                <span>Explore &amp; Brochure</span>
                <span class="explore-arrow">&rarr;</span>
              </button>
            </div>
          </article>

          <!-- SERVICE 4: PAYROLL & LABOUR COMPLIANCE -->
          <article class="service-card" onclick="openBrochureModal('payroll')" title="Click to explore and view brochure">
            <div class="service-header">
              <div class="service-kicker">04 &middot; Human Capital</div>
              <h3 class="service-title">Payroll &amp; Labour Compliance</h3>
            </div>
            <p class="service-desc">
              Structured salary processing, payslip management, PF/ESI/PT statutory filings, and employee documentation for growing teams.
            </p>
            <div class="service-card-bottom">
              <button type="button" class="btn-service-explore" onclick="event.stopPropagation(); openBrochureModal('payroll')">
                <span>Explore &amp; Brochure</span>
                <span class="explore-arrow">&rarr;</span>
              </button>
            </div>
          </article>

          <!-- SERVICE 5: FINANCIAL ADVISORY -->
          <article class="service-card" onclick="openBrochureModal('advisory')" title="Click to explore and view brochure">
            <div class="service-header">
              <div class="service-kicker">05 &middot; Strategic Advisory</div>
              <h3 class="service-title">Financial Advisory</h3>
            </div>
            <p class="service-desc">
              Executive financial planning, cash flow forecasting, working capital review, bankable project reports and CMA data preparation.
            </p>
            <div class="service-card-bottom">
              <button type="button" class="btn-service-explore" onclick="event.stopPropagation(); openBrochureModal('advisory')">
                <span>Explore &amp; Brochure</span>
                <span class="explore-arrow">&rarr;</span>
              </button>
            </div>
          </article>

          <!-- SERVICE 6: BUSINESS REGISTRATIONS & LICENSING -->
          <article class="service-card" onclick="openBrochureModal('registration')" title="Click to explore and view brochure">
            <div class="service-header">
              <div class="service-kicker">06 &middot; Entity Setup</div>
              <h3 class="service-title">Business Registrations &amp; Licensing</h3>
            </div>
            <p class="service-desc">
              Entity incorporation, MSME / Udyam, FSSAI, IEC, and regulatory documentation setup for entrepreneurs launching ventures.
            </p>
            <div class="service-card-bottom">
              <button type="button" class="btn-service-explore" onclick="event.stopPropagation(); openBrochureModal('registration')">
                <span>Explore &amp; Brochure</span>
                <span class="explore-arrow">&rarr;</span>
              </button>
            </div>
          </article>

          <!-- SERVICE 7: DATA ENTRY & PROCESS MANAGEMENT -->
          <article class="service-card" onclick="openBrochureModal('data-process')" title="Click to explore and view brochure">
            <div class="service-header">
              <div class="service-kicker">07 &middot; Operational Support</div>
              <h3 class="service-title">Data Entry &amp; Process Management</h3>
            </div>
            <p class="service-desc">
              High-accuracy back-office operations, invoice data entry, document digitization, spreadsheet modelling and data scrubbing.
            </p>
            <div class="service-card-bottom">
              <button type="button" class="btn-service-explore" onclick="event.stopPropagation(); openBrochureModal('data-process')">
                <span>Explore &amp; Brochure</span>
                <span class="explore-arrow">&rarr;</span>
              </button>
            </div>
          </article>

          <!-- SERVICE 8: DIGITAL & TECHNOLOGY SOLUTIONS -->
          <article class="service-card" onclick="openBrochureModal('technology')" title="Click to explore and view brochure">
            <div class="service-header">
              <div class="service-kicker">08 &middot; Technology Vertical</div>
              <h3 class="service-title">Digital &amp; Technology Solutions</h3>
            </div>
            <p class="service-desc">
              Custom web applications, AI automation tools, business process digitization and BI analytics dashboards engineered for agility.
            </p>
            <div class="service-card-bottom">
              <button type="button" class="btn-service-explore" onclick="event.stopPropagation(); openBrochureModal('technology')">
                <span>Explore &amp; Brochure</span>
                <span class="explore-arrow">&rarr;</span>
              </button>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- =========================================================
         SECTION 02: BUSINESS SOLUTIONS"""

match = re.search(old_services_pattern, content, re.DOTALL)
if match:
    content = content[:match.start()] + new_services_html + content[match.end():]
    print("Replaced services section with compact small cards")
else:
    print("ERROR: old_services_pattern not matched")
    sys.exit(1)

# Also update Solutions brochure buttons to use openBrochureModal
content = content.replace(
    'class="solution-brochure-btn" title="View & Download Solutions For Startups Brochure (PDF)">',
    'class="solution-brochure-btn" onclick="openBrochureModal(\'startups\'); return false;" title="View & Download Solutions For Startups Brochure (PDF)">'
)
content = content.replace(
    'class="solution-brochure-btn" title="View & Download Solutions For SMEs Brochure (PDF)">',
    'class="solution-brochure-btn" onclick="openBrochureModal(\'smes\'); return false;" title="View & Download Solutions For SMEs Brochure (PDF)">'
)
content = content.replace(
    'class="solution-brochure-btn" title="View & Download Solutions For Entrepreneurs Brochure (PDF)">',
    'class="solution-brochure-btn" onclick="openBrochureModal(\'entrepreneurs\'); return false;" title="View & Download Solutions For Entrepreneurs Brochure (PDF)">'
)
content = content.replace(
    'class="solution-brochure-btn" title="View & Download Solutions For Professionals Brochure (PDF)">',
    'class="solution-brochure-btn" onclick="openBrochureModal(\'professionals\'); return false;" title="View & Download Solutions For Professionals Brochure (PDF)">'
)
print("Updated solutions brochure onclick handlers")

# 3. Add Brochure Modal HTML before conceptModalOverlay
brochure_modal_html = """  <!-- =========================================================
       BROCHURE VIEWER MODAL SYSTEM (FULL INTERACTIVE & DOWNLOAD)
       ========================================================= -->
  <div id="brochureModalOverlay" role="dialog" aria-modal="true" aria-hidden="true">
    <div class="brochure-modal-container">
      <div class="brochure-modal-header">
        <div class="brochure-header-left">
          <div class="brochure-kicker-tag" id="bmKicker">// OFFICIAL SERVICE BROCHURE</div>
          <h3 class="brochure-modal-title" id="bmTitle">Service Brochure</h3>
        </div>
        <div class="brochure-header-actions">
          <a id="bmDownloadBtn" href="#" download="" class="btn-bm-download" title="Download Full PDF Brochure">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
            <span>Download PDF</span>
          </a>
          <a id="bmOpenTabBtn" href="#" target="_blank" rel="noopener noreferrer" class="btn-bm-tab" title="Open PDF in dedicated browser tab">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
            <span>Open in Tab</span>
          </a>
          <button type="button" class="btn-bm-close" onclick="closeBrochureModal()" aria-label="Close Brochure Modal">&times;</button>
        </div>
      </div>
      <div class="brochure-modal-viewport">
        <iframe id="brochureIframe" class="brochure-pdf-frame" src="about:blank" title="Official NIVORA Brochure Viewer"></iframe>
      </div>
      <div class="brochure-modal-footer">
        <span class="brochure-footer-text">Looking for tailored advisory or implementation for your business?</span>
        <button type="button" class="btn-bm-enquire" id="bmEnquireBtn" onclick="handleBrochureEnquire()">
          <span>Book Consultation for this Service</span>
          <span>&rarr;</span>
        </button>
      </div>
    </div>
  </div>\n\n"""

target_modal_insert = '  <!-- =========================================================\n       CONCEPT MODAL POPUP SYSTEM'
if target_modal_insert in content:
    content = content.replace(target_modal_insert, brochure_modal_html + target_modal_insert, 1)
    print("Inserted brochure modal HTML")
else:
    print("ERROR: target_modal_insert not found")
    sys.exit(1)

# 4. Add JavaScript for Brochure Modal & ESC Key Handling
brochure_js = """    /* -------------------------------------------------------------
       BROCHURE VIEWER MODAL SYSTEM (FULL INTERACTIVE & DOWNLOAD)
       ------------------------------------------------------------- */
    const BROCHURE_DATA = {
      'accounting': {
        title: 'Accounting & Bookkeeping Services',
        kicker: '01 · CORE RECORDS PRACTICE',
        pdf: 'brochures/accounting-and-bookkeeping.pdf',
        downloadName: 'NIVORA - Accounting & Bookkeeping Brochure.pdf',
        serviceName: 'Accounting & Bookkeeping'
      },
      'income-tax': {
        title: 'Income Tax Services',
        kicker: '02 · DIRECT TAX PRACTICE',
        pdf: 'brochures/income-tax-services.pdf',
        downloadName: 'NIVORA - Income Tax Services Brochure.pdf',
        serviceName: 'Income Tax'
      },
      'gst': {
        title: 'GST Compliance & Advisory Services',
        kicker: '03 · INDIRECT TAX PRACTICE',
        pdf: 'brochures/gst-services.pdf',
        downloadName: 'NIVORA - GST Services Brochure.pdf',
        serviceName: 'GST'
      },
      'payroll': {
        title: 'Payroll & Labour Compliance Services',
        kicker: '04 · HUMAN CAPITAL PRACTICE',
        pdf: 'brochures/payroll-and-labour-compliance.pdf',
        downloadName: 'NIVORA - Payroll & Labour Compliance Brochure.pdf',
        serviceName: 'Payroll'
      },
      'advisory': {
        title: 'Financial Advisory & Planning',
        kicker: '05 · STRATEGIC ADVISORY PRACTICE',
        pdf: 'brochures/financial-advisory.pdf',
        downloadName: 'NIVORA - Financial Advisory Brochure.pdf',
        serviceName: 'Financial Advisory'
      },
      'registration': {
        title: 'Business Registrations & Licensing',
        kicker: '06 · ENTITY SETUP PRACTICE',
        pdf: 'brochures/business-registrations-and-licensing.pdf',
        downloadName: 'NIVORA - Business Registrations & Licensing Brochure.pdf',
        serviceName: 'Business Registration'
      },
      'data-process': {
        title: 'Data Entry & Process Management',
        kicker: '07 · OPERATIONAL SUPPORT PRACTICE',
        pdf: 'brochures/data-entry-and-process-management.pdf',
        downloadName: 'NIVORA - Data Entry & Process Management Brochure.pdf',
        serviceName: 'Data & Process Support'
      },
      'technology': {
        title: 'Digital & Technology Solutions',
        kicker: '08 · TECHNOLOGY VERTICAL',
        pdf: 'brochures/digital-and-technology-solutions.pdf',
        downloadName: 'NIVORA - Digital & Technology Solutions Brochure.pdf',
        serviceName: 'Technology Solutions'
      },
      'startups': {
        title: 'Solutions For Startups Package',
        kicker: 'VENTURE · ARCHITECTURE',
        pdf: 'brochures/solutions-for-startups.pdf',
        downloadName: 'NIVORA - Solutions For Startups Package.pdf',
        serviceName: 'General Business Consultation'
      },
      'smes': {
        title: 'Solutions For SMEs Package',
        kicker: 'SCALE · RELIABILITY',
        pdf: 'brochures/solutions-for-smes.pdf',
        downloadName: 'NIVORA - Solutions For SMEs Package.pdf',
        serviceName: 'General Business Consultation'
      },
      'entrepreneurs': {
        title: 'Solutions For Entrepreneurs Package',
        kicker: 'VISION · EXECUTE',
        pdf: 'brochures/solutions-for-entrepreneurs.pdf',
        downloadName: 'NIVORA - Solutions For Entrepreneurs Package.pdf',
        serviceName: 'General Business Consultation'
      },
      'professionals': {
        title: 'Solutions For Professionals Package',
        kicker: 'PRACTICE · ELEVATE',
        pdf: 'brochures/solutions-for-professionals.pdf',
        downloadName: 'NIVORA - Solutions For Professionals Package.pdf',
        serviceName: 'General Business Consultation'
      }
    };

    let currentBrochureService = '';

    function openBrochureModal(key) {
      const data = BROCHURE_DATA[key];
      if (!data) return;

      currentBrochureService = data.serviceName;

      const overlay = document.getElementById('brochureModalOverlay');
      const titleEl = document.getElementById('bmTitle');
      const kickerEl = document.getElementById('bmKicker');
      const dlBtn = document.getElementById('bmDownloadBtn');
      const tabBtn = document.getElementById('bmOpenTabBtn');
      const iframe = document.getElementById('brochureIframe');

      if (titleEl) titleEl.textContent = data.title;
      if (kickerEl) kickerEl.textContent = '// ' + data.kicker;
      if (dlBtn) {
        dlBtn.href = data.pdf;
        dlBtn.setAttribute('download', data.downloadName);
      }
      if (tabBtn) {
        tabBtn.href = data.pdf;
      }
      if (iframe) {
        iframe.src = data.pdf + '#toolbar=1&navpanes=0';
      }

      if (overlay) {
        overlay.classList.add('open');
        overlay.setAttribute('aria-hidden', 'false');
      }
      document.body.style.overflow = 'hidden';
    }

    function closeBrochureModal() {
      const overlay = document.getElementById('brochureModalOverlay');
      if (overlay) {
        overlay.classList.remove('open');
        overlay.setAttribute('aria-hidden', 'true');
      }
      const iframe = document.getElementById('brochureIframe');
      if (iframe) iframe.src = 'about:blank';
      document.body.style.overflow = '';
    }

    function handleBrochureEnquire() {
      const serviceToSelect = currentBrochureService || 'General Business Consultation';
      closeBrochureModal();
      setTimeout(() => {
        selectConsultationService(serviceToSelect);
      }, 200);
    }

    const bmOverlayEl = document.getElementById('brochureModalOverlay');
    if (bmOverlayEl) {
      bmOverlayEl.addEventListener('click', (e) => {
        if (e.target === bmOverlayEl) closeBrochureModal();
      });
    }
"""

old_escape = """    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeConceptModal();
    });"""

new_escape = """    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeConceptModal();
        closeBrochureModal();
      }
    });"""

if old_escape in content:
    content = content.replace(old_escape, new_escape, 1)
    print("Updated ESC key listener")
else:
    print("WARNING: old_escape not found")

target_js_insert = "    /* -------------------------------------------------------------\n       CONSULTATION FORM SUBMISSION"
if target_js_insert in content:
    content = content.replace(target_js_insert, brochure_js + "\n" + target_js_insert, 1)
    print("Inserted brochure JavaScript")
else:
    print("ERROR: target_js_insert not found")
    sys.exit(1)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Updated assemble_consultancy_universe.py successfully!")
