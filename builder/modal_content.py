# builder/modal_content.py
# Pre-rendered HTML panels for CHECKRA, HOMORA, BUBORA, SAYORA

MODAL_HTML = """
  <!-- =========================================================
       PREMIUM PRODUCT CONCEPT MODAL OVERLAY
       ========================================================= -->
  <div id="conceptModalOverlay" class="concept-modal-overlay" role="dialog" aria-modal="true" aria-hidden="true">
    <div class="concept-modal-backdrop" onclick="closeConceptModal()"></div>

    <div class="concept-modal-window" id="conceptModalWindow">
      <!-- FIXED STICKY MODAL HEADER -->
      <header class="concept-modal-header" id="modalHeader">
        <div class="cmh-left">
          <div class="cmh-logo-wrap">
            <img id="cmhLogo-checkra" class="cmh-logo-img" src="assets/images/checkra-logo.png" alt="CHECKRA Logo">
            <img id="cmhLogo-homora" class="cmh-logo-img" src="assets/images/homora-logo.png" alt="HOMORA Logo" style="display:none;">
            <img id="cmhLogo-bubora" class="cmh-logo-img" src="assets/images/bubora-logo.png" alt="BUBORA Logo" style="display:none;">
            <img id="cmhLogo-sayora" class="cmh-logo-img" src="assets/images/sayora-logo.png" alt="SAYORA Logo" style="display:none;">
          </div>
          <div class="cmh-title-group">
            <div class="cmh-meta">
              <span id="cmhName" class="cmh-name">CHECKRA</span>
              <span id="cmhBadge" class="cmh-status-badge">Live App</span>
            </div>
            <div id="cmhTagline" class="cmh-tagline">Your Intelligent Writing Integrity Space</div>
          </div>
        </div>

        <nav class="cmh-nav" aria-label="Modal navigation">
          <button type="button" class="cmh-nav-link active" onclick="scrollModalTo('sec-overview')">Overview</button>
          <button type="button" class="cmh-nav-link" onclick="scrollModalTo('sec-capabilities')">Capabilities</button>
          <button type="button" class="cmh-nav-link" onclick="scrollModalTo('sec-architecture')">Architecture</button>
          <button type="button" class="cmh-nav-link" onclick="scrollModalTo('sec-workflow')">Workflow</button>
          <button type="button" class="cmh-nav-link" onclick="scrollModalTo('sec-vision')">Vision</button>
        </nav>

        <div class="cmh-actions">
          <a id="cmhLaunchBtn" class="btn primary cmh-launch-btn" href="https://checkra-xi.vercel.app/" target="_blank" rel="noopener noreferrer">
            <span>Launch App</span>
            <span class="btn-arrow">↗</span>
          </a>
          <button type="button" class="concept-modal-close" id="modalCloseBtn" onclick="closeConceptModal()" aria-label="Close product concept modal (ESC)">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>
        </div>
      </header>

      <!-- SCROLLABLE CONTENT BODY -->
      <div class="concept-modal-body" id="conceptModalBody">

        <!-- =========================================================
             1. CHECKRA CONCEPT PANEL
             ========================================================= -->
        <div class="modal-product-panel active" id="modal-panel-checkra">
          <!-- Overview -->
          <div class="modal-sec" id="sec-overview-checkra">
            <div class="modal-sec-title">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
              <span>CONCEPT OVERVIEW · WRITING INTEGRITY SPACE</span>
            </div>
            <p class="modal-intro-lead">
              CHECKRA is an AI-powered writing integrity and source verification platform designed to help students, researchers, educators, professionals, and content creators check, verify, and improve their writing in one connected workspace.
            </p>
          </div>

          <!-- Capability Grid (8 Cards) -->
          <div class="modal-sec" id="sec-capabilities-checkra">
            <div class="modal-sec-title">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="3" width="18" height="18" rx="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line></svg>
              <span>KEY CAPABILITIES</span>
            </div>
            <h3 class="modal-sec-heading">Engineered for Writing Truth &amp; Elevation</h3>

            <div class="modal-grid-4">
              <div class="modal-cap-card">
                <div class="mcc-icon">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                </div>
                <h5>Similarity Check</h5>
                <p>Multi-level comparison analyzing exact matches, near phrasing, and semantic overlap across open sources.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
                </div>
                <h5>Source Verification</h5>
                <p>Indexes live web resources to provide verifiable context and direct citations for detected matches.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
                </div>
                <h5>Document Analysis</h5>
                <p>Unified native ingestion of PDF, DOCX, TXT, HTML, and Markdown files with preserved layout parsing.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10H12V2z"></path><path d="M12 12 2.1 10.5"></path></svg>
                </div>
                <h5>AI Evidence Review</h5>
                <p>Assists reviewers in evaluating matches, distinguishing valid citations from true duplication.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg>
                </div>
                <h5>Grammar Check</h5>
                <p>Identifies grammatical anomalies, typos, punctuation missteps, and wordiness to heighten clarity.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                </div>
                <h5>AI Rewrite</h5>
                <p>Calibrated rewrite modes: Clear &amp; Natural, Academic &amp; Readable, Professional, Concise, Simple English.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><line x1="12" y1="18" x2="12" y2="12"></line><line x1="9" y1="15" x2="15" y2="15"></line></svg>
                </div>
                <h5>Evidence-Based Reports</h5>
                <p>Generates structured audit summaries detailing matched passages, source info, and revision trails.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                </div>
                <h5>Privacy &amp; Security</h5>
                <p>Session-based processing, zero permanent text storage, and secure handling to safeguard IP.</p>
              </div>
            </div>
          </div>

          <!-- Core Idea Banner -->
          <div class="modal-core-idea">
            <blockquote>&ldquo;Don&rsquo;t just check the writing. Understand it, verify it, and improve it.&rdquo;</blockquote>
            <p>
              Traditional similarity tools reduce analysis to a single punitive percentage. CHECKRA takes a transparent approach combining Similarity Analysis + Source Verification + AI Evidence Review + Grammar Improvement + Intelligent Rewriting into one cohesive workspace.
            </p>
          </div>

          <!-- Analysis Layers (3 Connected Levels) -->
          <div class="modal-sec" id="sec-architecture-checkra">
            <div class="modal-sec-title">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
              <span>3-STEP ANALYSIS LAYERS</span>
            </div>
            <h3 class="modal-sec-heading">Evidence-Based Detection Architecture</h3>

            <div class="modal-arch-rail levels-3">
              <div class="modal-arch-step">
                <div class="mas-tag">LAYER 01</div>
                <b>Exact Matching</b>
                <p>Identifies directly matching verbatim sequences and unquoted copy-pasted passages with byte precision.</p>
              </div>
              <div class="modal-arch-step">
                <div class="mas-tag">LAYER 02</div>
                <b>Near Matching</b>
                <p>Detects similar passages where wording has been modified, synonym-swapped, or rearranged.</p>
              </div>
              <div class="modal-arch-step">
                <div class="mas-tag">LAYER 03</div>
                <b>Semantic Similarity</b>
                <p>Analyzes deep semantic embeddings to evaluate whether different wording conveys substantially identical concepts.</p>
              </div>
            </div>
          </div>

          <!-- Responsible Integrity -->
          <div class="modal-sec">
            <div class="modal-sec-title">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
              <span>RESPONSIBLE INTEGRITY STATUS CARDS</span>
            </div>
            <div class="modal-grid-4">
              <div class="modal-cap-card">
                <h5>Web Sources Retrieved</h5>
                <p>Transparent count of indexed materials reviewed across the public web for context.</p>
              </div>
              <div class="modal-cap-card">
                <h5>Topically Related Sources</h5>
                <p>Documents addressing the same subject matter without sharing direct text matches.</p>
              </div>
              <div class="modal-cap-card">
                <h5>Possible Matching Sources</h5>
                <p>Passages showing structural or near-matching patterns highlighted for reviewer evaluation.</p>
              </div>
              <div class="modal-cap-card">
                <h5>Verified Matching Sources</h5>
                <p>Confirmed verbatim overlap accompanied by direct URLs, timestamps, and excerpt diffs.</p>
              </div>
            </div>

            <div class="modal-responsible-notice">
              <div class="mrn-kicker">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                <span>RESPONSIBLE DESIGN ETHICS</span>
              </div>
              <h5>Transparent Evidence Over Unsupported Accusations</h5>
              <p>CHECKRA focuses on providing transparent, auditable evidence that writers and educators can review themselves, rather than outputting opaque black-box verdicts.</p>
            </div>
          </div>

          <!-- Workflow -->
          <div class="modal-sec" id="sec-workflow-checkra">
            <div class="modal-sec-title">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
              <span>7-STAGE WORKFLOW</span>
            </div>
            <h3 class="modal-sec-heading">The Writing Integrity Pipeline</h3>

            <div class="modal-workflow-rail">
              <div class="modal-wf-step"><div class="mwf-num">01</div><b>Upload</b></div>
              <div class="modal-wf-step"><div class="mwf-num">02</div><b>Analyze</b></div>
              <div class="modal-wf-step"><div class="mwf-num">03</div><b>Find Evidence</b></div>
              <div class="modal-wf-step"><div class="mwf-num">04</div><b>Verify</b></div>
              <div class="modal-wf-step"><div class="mwf-num">05</div><b>Review</b></div>
              <div class="modal-wf-step"><div class="mwf-num">06</div><b>Improve</b></div>
              <div class="modal-wf-step"><div class="mwf-num">07</div><b>Report</b></div>
            </div>
          </div>

          <!-- Vision -->
          <div class="modal-sec" id="sec-vision-checkra">
            <div class="modal-vision-box">
              <div class="mv-left">
                <h4>PRODUCT VISION</h4>
                <p>CHECKRA aims to become a trusted intelligent writing companion — helping people create original, credible, clear, and well-written content through evidence-based analysis and AI-powered assistance.</p>
              </div>
              <div class="mv-right">
                <div class="mv-tagline-primary">Check. Verify. Improve.</div>
                <div class="mv-tagline-secondary">Your Intelligent Writing Integrity Space</div>
              </div>
            </div>
          </div>

          <!-- Modal Footer Cross Nav -->
          <div class="modal-footer-nav">
            <span style="font-size:12.5px;color:#8f92a9;">Switch Product Concept:</span>
            <div class="mfn-links">
              <button type="button" class="mfn-btn" onclick="openConceptModal('homora')">HOMORA (Shared Finance OS) →</button>
              <button type="button" class="mfn-btn" onclick="openConceptModal('bubora')">BUBORA (Couples) →</button>
              <button type="button" class="mfn-btn" onclick="openConceptModal('sayora')">SAYORA (Resilience) →</button>
            </div>
          </div>
        </div>


        <!-- =========================================================
             2. HOMORA CONCEPT PANEL
             ========================================================= -->
        <div class="modal-product-panel" id="modal-panel-homora">
          <!-- Overview -->
          <div class="modal-sec" id="sec-overview-homora">
            <div class="modal-sec-title">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
              <span>CONCEPT OVERVIEW · HOUSEHOLD FINANCIAL OPERATING SYSTEM</span>
            </div>
            <p class="modal-intro-lead">
              HOMORA is an intelligent household finance platform designed to help roommates, shared households, couples, families, and co-living communities manage money, expenses, bills, responsibilities, and financial decisions in one connected ecosystem.
            </p>
          </div>

          <!-- Core Idea Banner & Solved Questions -->
          <div class="modal-core-idea">
            <blockquote>&ldquo;Shared Living. Shared Responsibility. Smarter Money.&rdquo;</blockquote>
            <p>Eliminating awkward money reminders and domestic tension through unified transparency.</p>
            <div class="modal-chip-row">
              <span class="modal-chip">Who paid?</span>
              <span class="modal-chip">Who owes?</span>
              <span class="modal-chip">Where did the money go?</span>
              <span class="modal-chip">Did everyone contribute?</span>
              <span class="modal-chip">What bills are pending?</span>
              <span class="modal-chip">Can we afford this?</span>
            </div>
          </div>

          <!-- Capability Grid (15 Cards) -->
          <div class="modal-sec" id="sec-capabilities-homora">
            <div class="modal-sec-title">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="3" width="18" height="18" rx="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line></svg>
              <span>15 CORE CAPABILITIES</span>
            </div>
            <h3 class="modal-sec-heading">Complete Domestic Operating Architecture</h3>

            <div class="modal-grid-5">
              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg></div>
                <h5>Shared Finance</h5>
                <p>Transparent group balances with simplified peer-to-peer debt netting.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg></div>
                <h5>Household Budgeting</h5>
                <p>Monthly target caps for rent, utilities, food, and social buffers.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line></svg></div>
                <h5>Expense Tracking</h5>
                <p>Categorized spending logs with receipts and customizable split shares.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 14 14"></polyline></svg></div>
                <h5>Contribution Mgmt</h5>
                <p>Equal, percentage, room-size, or income-weighted split calculations.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg></div>
                <h5>Financial Pool</h5>
                <p>A communal household emergency reserve for shared appliance fixes.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></div>
                <h5>Emergency Claims</h5>
                <p>One-tap expense reimbursement requests with instant status trails.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg></div>
                <h5>Internal Loans</h5>
                <p>Transparent roommate-to-roommate internal ledger tracking with zero awkwardness.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg></div>
                <h5>Smart Groceries</h5>
                <p>Synchronized shared pantry lists and duplicate purchase prevention.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg></div>
                <h5>Bills &amp; Subscriptions</h5>
                <p>Recurring utility reminders for Wi-Fi, electricity, rent, and maid services.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 11 12 14 22 4"></polyline><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path></svg></div>
                <h5>Tasks &amp; Chores</h5>
                <p>Rotational cleaning duties, trash assignments, and accountability tracking.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg></div>
                <h5>Community Hub</h5>
                <p>Home message board for visitor announcements, polls, and shared moments.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg></div>
                <h5>Insights &amp; Reports</h5>
                <p>Visual monthly expense trends and utility spend inflation analysis.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg></div>
                <h5>Financial Health</h5>
                <p>Algorithmic hygiene rating reflecting budget adherence and reserve stability.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10H12V2z"></path><path d="M12 12 2.1 10.5"></path></svg></div>
                <h5>HOMORA Intel</h5>
                <p>AI copilot surfacing actionable cost-saving domestic insights.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg></div>
                <h5>Trust &amp; Transparency</h5>
                <p>Auditable shared ledger visible to all members with immutable revision records.</p>
              </div>
            </div>
          </div>

          <!-- Financial Architecture (4 Levels) -->
          <div class="modal-sec" id="sec-architecture-homora">
            <div class="modal-sec-title">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
              <span>4-LEVEL FINANCIAL ARCHITECTURE</span>
            </div>
            <h3 class="modal-sec-heading">Capital Flow &amp; Intelligence Tiers</h3>

            <div class="modal-arch-rail">
              <div class="modal-arch-step">
                <div class="mas-tag">LEVEL 01</div>
                <b>Personal Contribution</b>
                <p>Savings responsibility, payments, expenses, claims, and settlements.</p>
              </div>
              <div class="modal-arch-step">
                <div class="mas-tag">LEVEL 02</div>
                <b>Household Pool</b>
                <p>Inflows, outflows, current pool, reserves, and liquid buffers.</p>
              </div>
              <div class="modal-arch-step">
                <div class="mas-tag">LEVEL 03</div>
                <b>Household Operations</b>
                <p>Groceries, bills, subscriptions, chores, and house announcements.</p>
              </div>
              <div class="modal-arch-step">
                <div class="mas-tag">LEVEL 04</div>
                <b>Intelligence</b>
                <p>Spending analysis, budget recommendations, trends, and financial health.</p>
              </div>
            </div>
          </div>

          <!-- Connected Ecosystem Diagram -->
          <div class="modal-sec">
            <div class="modal-sec-title">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line></svg>
              <span>CONNECTED ECOSYSTEM DIAGRAM</span>
            </div>
            <div class="modal-network-diagram">
              <div class="mnd-nodes">
                <span class="mnd-node">Members</span>
                <span class="mnd-arrow">↓</span>
                <span class="mnd-node">Money</span>
                <span class="mnd-arrow">↓</span>
                <span class="mnd-node">Expenses</span>
                <span class="mnd-arrow">↓</span>
                <span class="mnd-node">Bills</span>
                <span class="mnd-arrow">↓</span>
                <span class="mnd-node">Groceries</span>
                <span class="mnd-arrow">↓</span>
                <span class="mnd-node">Tasks</span>
                <span class="mnd-arrow">↓</span>
                <span class="mnd-node">Communication</span>
                <span class="mnd-arrow">↓</span>
                <span class="mnd-node">Intelligence</span>
              </div>
            </div>
          </div>

          <!-- HOMORA Intel AI Section -->
          <div class="modal-sec" id="sec-workflow-homora">
            <div class="modal-sec-title">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
              <span>HOMORA INTEL · HOUSEHOLD COPILOT</span>
            </div>
            <h3 class="modal-sec-heading">Proactive Financial Decision Support</h3>
            <div class="modal-grid-3">
              <div class="modal-cap-card">
                <h5>&ldquo;How much did we spend this month?&rdquo;</h5>
                <p>Instant category breakdowns comparing current pace to historical median run-rates.</p>
              </div>
              <div class="modal-cap-card">
                <h5>&ldquo;Which category uses most of our budget?&rdquo;</h5>
                <p>Pinpoints runaway electricity spikes or food delivery habits with itemized diffs.</p>
              </div>
              <div class="modal-cap-card">
                <h5>&ldquo;Are we under budget? Can we afford this?&rdquo;</h5>
                <p>Simulates proposed shared purchases against upcoming rent and utility deadlines.</p>
              </div>
            </div>

            <!-- Responsible Design Notice -->
            <div class="modal-responsible-notice">
              <div class="mrn-kicker">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                <span>LEGAL &amp; ARCHITECTURAL CLARITY</span>
              </div>
              <h5>Financial Management Tool · Not a Depository Bank</h5>
              <p>HOMORA is a household financial management software system — not a bank, NBFC, or insurer. All internal loans, pools, and balances represent mathematical tracking ledgers maintained by housemates.</p>
            </div>
          </div>

          <!-- Vision -->
          <div class="modal-sec" id="sec-vision-homora">
            <div class="modal-vision-box">
              <div class="mv-left">
                <h4>PRODUCT VISION</h4>
                <p>Make shared living financially transparent, organized, intelligent, and stress-free.</p>
              </div>
              <div class="mv-right">
                <div class="mv-tagline-primary">HOMORA is a Household Financial OS.</div>
                <div class="mv-tagline-secondary">AI-Powered Financial Harmony for Shared Living</div>
              </div>
            </div>
          </div>

          <!-- Modal Footer Cross Nav -->
          <div class="modal-footer-nav">
            <span style="font-size:12.5px;color:#8f92a9;">Switch Product Concept:</span>
            <div class="mfn-links">
              <button type="button" class="mfn-btn" onclick="openConceptModal('bubora')">BUBORA (Couples Space) →</button>
              <button type="button" class="mfn-btn" onclick="openConceptModal('sayora')">SAYORA (Gig Worker Fund) →</button>
              <button type="button" class="mfn-btn" onclick="openConceptModal('checkra')">CHECKRA (Integrity) →</button>
            </div>
          </div>
        </div>


        <!-- =========================================================
             3. BUBORA CONCEPT PANEL
             ========================================================= -->
        <div class="modal-product-panel" id="modal-panel-bubora">
          <!-- Overview -->
          <div class="modal-sec" id="sec-overview-bubora">
            <div class="modal-sec-title">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
              <span>CONCEPT OVERVIEW · PRIVATE DIGITAL SANCTUARY</span>
            </div>
            <p class="modal-intro-lead">
              BUBORA is a private digital space designed exclusively for two people to build, organize, and preserve their life together in one secure place.
            </p>
          </div>

          <!-- Core Idea Banner -->
          <div class="modal-core-idea">
            <blockquote>&ldquo;A relationship has many little moments. Bubora gives those moments one little world.&rdquo;</blockquote>
            <p>
              In an era where personal moments are scattered across noisy, ad-supported apps, BUBORA returns to the sacred beauty of two people sharing intimacy, memories, and future plans in complete privacy.
            </p>
          </div>

          <!-- Feature Grid (8 Cards) -->
          <div class="modal-sec" id="sec-capabilities-bubora">
            <div class="modal-sec-title">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="3" width="18" height="18" rx="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line></svg>
              <span>8 ELEGANT FEATURE WORLDS</span>
            </div>
            <h3 class="modal-sec-heading">Built Exclusively for Two</h3>

            <div class="modal-grid-4">
              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg></div>
                <h5>Our Chat</h5>
                <p>Dedicated private messaging channel with pinned memories, voice notes, and zero external alerts.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg></div>
                <h5>Memories</h5>
                <p>An interactive chronological timeline capturing first dates, trips, holidays, and milestones.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg></div>
                <h5>Our Calendar</h5>
                <p>Shared calendar with live countdown timers for anniversaries, trips, and special evenings.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="3 11 22 2 13 21 11 13 3 11"></polygon></svg></div>
                <h5>Plans &amp; Trips</h5>
                <p>Collaborative travel itineraries with hotel details, flight bookings, packing checklists, and spot pins.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="m4.93 4.93 4.24 4.24"></path><path d="m14.83 9.17 4.24-4.24"></path></svg></div>
                <h5>Our Goals</h5>
                <p>Visual long-term milestones: saving for an apartment, fitness challenges, and joint dreams.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg></div>
                <h5>Our Money</h5>
                <p>Gentle shared expense tracking without awkward balance demands — keeping finances clear.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg></div>
                <h5>Activities</h5>
                <p>Curated date night generators, surprise activity prompts, and shared bucket list items.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg></div>
                <h5>Private Vault</h5>
                <p>Encrypted vault for private notes, door codes, passports, and cherished letters.</p>
              </div>
            </div>
          </div>

          <!-- Connected Life Diagram -->
          <div class="modal-sec" id="sec-architecture-bubora">
            <div class="modal-sec-title">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 14 14"></polyline></svg>
              <span>CONNECTED LIFE ECOSYSTEM</span>
            </div>
            <div class="modal-network-diagram">
              <div class="mnd-nodes">
                <span class="mnd-node">Connection</span>
                <span class="mnd-arrow">✦</span>
                <span class="mnd-node">Memories</span>
                <span class="mnd-arrow">✦</span>
                <span class="mnd-node">Planning</span>
                <span class="mnd-arrow">✦</span>
                <span class="mnd-node" style="border-color:var(--modal-accent);color:#fff;">BUBORA</span>
                <span class="mnd-arrow">✦</span>
                <span class="mnd-node">Finance</span>
                <span class="mnd-arrow">✦</span>
                <span class="mnd-node">Activities</span>
                <span class="mnd-arrow">✦</span>
                <span class="mnd-node">Privacy</span>
              </div>
            </div>

            <!-- Privacy by Design Card -->
            <div class="modal-responsible-notice" style="border-color:rgba(236,109,255,0.25);">
              <div class="mrn-kicker" style="color:#ec6dff;">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                <span>PRIVACY BY DESIGN ETHICS</span>
              </div>
              <h5>Strict Couple Data Isolation</h5>
              <p>Designed around client-side encryption concepts, separate storage of sensitive records, controlled metadata, zero advertising trackers, and an impenetrable two-party enclave.</p>
            </div>
          </div>

          <!-- Journey -->
          <div class="modal-sec" id="sec-workflow-bubora">
            <div class="modal-sec-title">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
              <span>THE COUPLE JOURNEY</span>
            </div>
            <h3 class="modal-sec-heading">From First Connection to Lifelong Archive</h3>

            <div class="modal-workflow-rail">
              <div class="modal-wf-step"><div class="mwf-num">01</div><b>Connect</b></div>
              <div class="modal-wf-step"><div class="mwf-num">02</div><b>Remember</b></div>
              <div class="modal-wf-step"><div class="mwf-num">03</div><b>Plan</b></div>
              <div class="modal-wf-step"><div class="mwf-num">04</div><b>Experience</b></div>
              <div class="modal-wf-step"><div class="mwf-num">05</div><b>Manage</b></div>
              <div class="modal-wf-step"><div class="mwf-num">06</div><b>Grow Together</b></div>
            </div>
          </div>

          <!-- Vision -->
          <div class="modal-sec" id="sec-vision-bubora">
            <div class="modal-vision-box">
              <div class="mv-left">
                <h4>PRODUCT VISION</h4>
                <p>Bubora aims to become a complete digital companion for couples — helping them communicate better, remember more, plan together, manage money responsibly, and build their future side by side.</p>
              </div>
              <div class="mv-right">
                <div class="mv-tagline-primary">Your Little World of Us.</div>
                <div class="mv-tagline-secondary">A Private Digital Home for Two</div>
              </div>
            </div>
          </div>

          <!-- Modal Footer Cross Nav -->
          <div class="modal-footer-nav">
            <span style="font-size:12.5px;color:#8f92a9;">Switch Product Concept:</span>
            <div class="mfn-links">
              <button type="button" class="mfn-btn" onclick="openConceptModal('sayora')">SAYORA (Gig Worker Fund) →</button>
              <button type="button" class="mfn-btn" onclick="openConceptModal('checkra')">CHECKRA (Integrity) →</button>
              <button type="button" class="mfn-btn" onclick="openConceptModal('homora')">HOMORA (Shared Finance) →</button>
            </div>
          </div>
        </div>


        <!-- =========================================================
             4. SAYORA CONCEPT PANEL
             ========================================================= -->
        <div class="modal-product-panel" id="modal-panel-sayora">
          <!-- Overview -->
          <div class="modal-sec" id="sec-overview-sayora">
            <div class="modal-sec-title">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
              <span>CONCEPT OVERVIEW · FINANCIAL RESILIENCE &amp; SOCIAL IMPACT</span>
            </div>
            <p class="modal-intro-lead">
              SAYORA is a social-impact fintech and financial resilience platform designed to help informal workers, gig workers, daily-wage earners, street vendors, drivers, and communities save, contribute, access support, manage money, and build a safer financial future.
            </p>
          </div>

          <!-- Core Idea Banner & Lifecycle -->
          <div class="modal-core-idea">
            <blockquote>&ldquo;Small Steps. Stronger Communities.&rdquo;</blockquote>
            <p>Dignified mutual protection for the backbone of modern cities.</p>
            <div class="modal-chip-row">
              <span class="modal-chip">Save</span>
              <span class="modal-chip">Contribute</span>
              <span class="modal-chip">Connect</span>
              <span class="modal-chip">Protect</span>
              <span class="modal-chip">Learn</span>
              <span class="modal-chip">Recover</span>
              <span class="modal-chip">Grow</span>
            </div>
          </div>

          <!-- Capability Grid (13 Cards) -->
          <div class="modal-sec" id="sec-capabilities-sayora">
            <div class="modal-sec-title">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="3" width="18" height="18" rx="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line></svg>
              <span>13 CORE RESILIENCE CAPABILITIES</span>
            </div>
            <h3 class="modal-sec-heading">Empowering Informal &amp; Gig Economy Workers</h3>

            <div class="modal-grid-4">
              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg></div>
                <h5>Smart Savings &amp; Goals</h5>
                <p>Daily micro-roundups into an individual protected emergency fund.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>
                <h5>Financial Protection</h5>
                <p>Mutual aid pool absorbing shocks from accidents and sudden hospital bills.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle></svg></div>
                <h5>Community Support</h5>
                <p>Peer verifiers and fellow workers vouching for incident legitimacy.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg></div>
                <h5>Emergency Assistance</h5>
                <p>Rapid micro-disbursements for immediate medicine and vehicle repairs.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"></path></svg></div>
                <h5>Climate &amp; Crisis</h5>
                <p>Parametric relief during severe heatwaves, monsoons, and curfews.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg></div>
                <h5>CSR &amp; Corporate</h5>
                <p>Integration channel for platforms and foundations to match savings 1:1.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></div>
                <h5>Benefits &amp; Schemes</h5>
                <p>Matching engine pairing workers with official welfare schemes (e-Shram, PM-JAY).</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg></div>
                <h5>Financial Literacy</h5>
                <p>Vernacular audio and visual guides on debt avoidance and budgeting.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="4" width="22" height="16" rx="2"></rect><line x1="1" y1="10" x2="23" y2="10"></line></svg></div>
                <h5>Money &amp; Services</h5>
                <p>Zero-penalty micro-transfers and emergency bill buffering partnerships.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="16" rx="2"></rect><circle cx="9" cy="10" r="2"></circle><line x1="15" y1="8" x2="17" y2="8"></line></svg></div>
                <h5>Digital SAYORA ID</h5>
                <p>Portable digital credential consolidating work tenure and reliability ratings.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg></div>
                <h5>Impact &amp; Analytics</h5>
                <p>Open-ledger reporting detailing exactly where assistance funds were deployed.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg></div>
                <h5>Ask SAYORA AI</h5>
                <p>Multilingual voice assistant answering scheme, claim, and hospital questions.</p>
              </div>

              <div class="modal-cap-card">
                <div class="mcc-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg></div>
                <h5>Security &amp; Trust</h5>
                <p>Zero data sharing with gig platform employers, preventing retaliation.</p>
              </div>
            </div>
          </div>

          <!-- Resilience Architecture (4 Levels) -->
          <div class="modal-sec" id="sec-architecture-sayora">
            <div class="modal-sec-title">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
              <span>4-LEVEL RESILIENCE ARCHITECTURE</span>
            </div>
            <h3 class="modal-sec-heading">Multi-Tiered Safety Architecture</h3>

            <div class="modal-arch-rail">
              <div class="modal-arch-step">
                <div class="mas-tag">TIER 01</div>
                <b>Personal Resilience</b>
                <p>Savings, emergency funds, goals, literacy, and personal money management.</p>
              </div>
              <div class="modal-arch-step">
                <div class="mas-tag">TIER 02</div>
                <b>Community Resilience</b>
                <p>Member contributions, peer verification, and collective safety initiatives.</p>
              </div>
              <div class="modal-arch-step">
                <div class="mas-tag">TIER 03</div>
                <b>CSR &amp; Partner Support</b>
                <p>CSR matching programs, corporate campaigns, and institutional partner grants.</p>
              </div>
              <div class="modal-arch-step">
                <div class="mas-tag">TIER 04</div>
                <b>Crisis Response</b>
                <p>Incident identification, assistance requests, capacity tracking, and funding gaps.</p>
              </div>
            </div>

            <!-- Responsible Design Notice -->
            <div class="modal-responsible-notice" style="border-color:rgba(36,216,167,0.25);">
              <div class="mrn-kicker" style="color:#24d8a7;">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                <span>RESPONSIBLE DESIGN &amp; HONEST CONSTRAINTS</span>
              </div>
              <h5>Financial Resilience Platform · Not a Licensed Bank or Insurer</h5>
              <p>SAYORA is designed as a financial resilience and social-impact platform, not as a replacement for a bank, insurer, NBFC, or government authority. Full deployment will operate in formal partnership with regulated banking and non-profit welfare trusts.</p>
            </div>
          </div>

          <!-- Ecosystem Network -->
          <div class="modal-sec">
            <div class="modal-sec-title">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line></svg>
              <span>ECOSYSTEM NETWORK</span>
            </div>
            <div class="modal-network-diagram">
              <div class="mnd-nodes">
                <span class="mnd-node">Members</span>
                <span class="mnd-arrow">↕</span>
                <span class="mnd-node">Communities</span>
                <span class="mnd-arrow">↕</span>
                <span class="mnd-node" style="border-color:var(--modal-accent);color:#fff;">SAYORA Core</span>
                <span class="mnd-arrow">↙ ↓ ↘</span>
                <span class="mnd-node">CSR Orgs</span>
                <span class="mnd-node">Partners</span>
                <span class="mnd-node">Admin</span>
              </div>
            </div>
          </div>

          <!-- Journey -->
          <div class="modal-sec" id="sec-workflow-sayora">
            <div class="modal-sec-title">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
              <span>THE RESILIENCE LIFECYCLE</span>
            </div>
            <h3 class="modal-sec-heading">Step-by-Step Empowerment</h3>

            <div class="modal-workflow-rail">
              <div class="modal-wf-step"><div class="mwf-num">01</div><b>Join</b></div>
              <div class="modal-wf-step"><div class="mwf-num">02</div><b>Verify</b></div>
              <div class="modal-wf-step"><div class="mwf-num">03</div><b>SAYORA ID</b></div>
              <div class="modal-wf-step"><div class="mwf-num">04</div><b>Save</b></div>
              <div class="modal-wf-step"><div class="mwf-num">05</div><b>Contribute</b></div>
              <div class="modal-wf-step"><div class="mwf-num">06</div><b>Learn</b></div>
              <div class="modal-wf-step"><div class="mwf-num">07</div><b>Resilience</b></div>
              <div class="modal-wf-step"><div class="mwf-num">08</div><b>Benefits</b></div>
              <div class="modal-wf-step"><div class="mwf-num">09</div><b>Support</b></div>
              <div class="modal-wf-step"><div class="mwf-num">10</div><b>Impact</b></div>
            </div>
          </div>

          <!-- Vision -->
          <div class="modal-sec" id="sec-vision-sayora">
            <div class="modal-vision-box">
              <div class="mv-left">
                <h4>PRODUCT VISION</h4>
                <p>SAYORA aims to become a trusted financial resilience companion for workers and communities — helping people build savings, access relevant support, improve financial knowledge, prepare for emergencies, and create a safer financial future together.</p>
              </div>
              <div class="mv-right">
                <div class="mv-tagline-primary">Together for a Safer Tomorrow.</div>
                <div class="mv-tagline-secondary">Small Steps. Stronger Communities.</div>
              </div>
            </div>
          </div>

          <!-- Modal Footer Cross Nav -->
          <div class="modal-footer-nav">
            <span style="font-size:12.5px;color:#8f92a9;">Switch Product Concept:</span>
            <div class="mfn-links">
              <button type="button" class="mfn-btn" onclick="openConceptModal('checkra')">CHECKRA (Integrity) →</button>
              <button type="button" class="mfn-btn" onclick="openConceptModal('homora')">HOMORA (Shared Finance) →</button>
              <button type="button" class="mfn-btn" onclick="openConceptModal('bubora')">BUBORA (Couples) →</button>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
"""

MODAL_JS = """
    // -------------------------------------------------------------
    // Premium Concept Modal Controller & Scroll Lock
    // -------------------------------------------------------------
    var currentModalKey = null;
    var savedPageScrollY = 0;
    var lastModalFocusTrigger = null;

    var productModalConfig = {
      checkra: {
        name: "CHECKRA",
        tagline: "Your Intelligent Writing Integrity Space",
        badge: "Live App",
        isConcept: false,
        themeClass: "theme-checkra",
        logo: "assets/images/checkra-logo.png",
        launchUrl: "https://checkra-xi.vercel.app/",
        launchText: "Launch App"
      },
      homora: {
        name: "HOMORA",
        tagline: "AI-Powered Financial Harmony for Shared Living",
        badge: "Active Prototype",
        isConcept: false,
        themeClass: "theme-homora",
        logo: "assets/images/homora-logo.png",
        launchUrl: "https://homora-ai.vercel.app/",
        launchText: "Visit Prototype"
      },
      bubora: {
        name: "BUBORA",
        tagline: "Your Little World of Us",
        badge: "Live App",
        isConcept: false,
        themeClass: "theme-bubora",
        logo: "assets/images/bubora-logo.png",
        launchUrl: "https://bubora.netlify.app/",
        launchText: "Visit App"
      },
      sayora: {
        name: "SAYORA",
        tagline: "Your Intelligent Financial Resilience Space",
        badge: "Concept · In Development",
        isConcept: true,
        themeClass: "theme-sayora",
        logo: "assets/images/sayora-logo.png",
        launchUrl: "#contact",
        launchText: "Partner With R&D"
      }
    };

    function openConceptModal(productKey, triggerEl) {
      if (!productModalConfig[productKey]) return;
      currentModalKey = productKey;
      var conf = productModalConfig[productKey];

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
      var cmhLogo = document.getElementById('cmhLogo');
      var cmhName = document.getElementById('cmhName');
      var cmhBadge = document.getElementById('cmhBadge');
      var cmhTagline = document.getElementById('cmhTagline');
      var cmhLaunchBtn = document.getElementById('cmhLaunchBtn');

      if (modalWindow) {
        modalWindow.className = 'concept-modal-window ' + conf.themeClass;
      }
      ['checkra', 'homora', 'bubora', 'sayora'].forEach(function(k) {
        var logoImg = document.getElementById('cmhLogo-' + k);
        if (logoImg) {
          logoImg.style.display = (k === productKey) ? 'block' : 'none';
        }
      });
      if (cmhName) cmhName.textContent = conf.name;
      if (cmhTagline) cmhTagline.textContent = conf.tagline;
      if (cmhBadge) {
        cmhBadge.textContent = conf.badge;
        if (conf.isConcept) {
          cmhBadge.className = 'cmh-status-badge concept';
        } else {
          cmhBadge.className = 'cmh-status-badge';
        }
      }
      if (cmhLaunchBtn) {
        cmhLaunchBtn.href = conf.launchUrl;
        cmhLaunchBtn.innerHTML = '<span>' + conf.launchText + '</span> <span class="btn-arrow">↗</span>';
        if (conf.launchUrl === '#contact') {
          cmhLaunchBtn.removeAttribute('target');
          cmhLaunchBtn.onclick = function() {
            closeConceptModal();
            setTimeout(function() {
              var contact = document.getElementById('contact');
              if (contact) contact.scrollIntoView({ behavior: 'smooth' });
            }, 350);
          };
        } else {
          cmhLaunchBtn.setAttribute('target', '_blank');
          cmhLaunchBtn.onclick = null;
        }
      }

      // Toggle Panels
      ['checkra', 'homora', 'bubora', 'sayora'].forEach(function(k) {
        var panel = document.getElementById('modal-panel-' + k);
        if (panel) {
          if (k === productKey) {
            panel.classList.add('active');
          } else {
            panel.classList.remove('active');
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

    // Scroll smoothly within modal content area
    function scrollModalTo(sectionIdPrefix) {
      if (!currentModalKey) return;
      var targetId = sectionIdPrefix + '-' + currentModalKey;
      var el = document.getElementById(targetId);
      var modalBody = document.getElementById('conceptModalBody');
      if (el && modalBody) {
        var top = el.offsetTop - 20;
        modalBody.scrollTo({
          top: top,
          behavior: 'smooth'
        });
      }

      // Update nav link active state
      var links = document.querySelectorAll('.cmh-nav-link');
      links.forEach(function(link) {
        if (link.getAttribute('onclick').indexOf(sectionIdPrefix) !== -1) {
          link.classList.add('active');
        } else {
          link.classList.remove('active');
        }
      });
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
