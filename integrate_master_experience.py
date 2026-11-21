# integrate_master_experience.py
import re

def build_integration():
    with open('/tmp/original_head.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Read the new CSS from css_styles.py
    with open('/Users/bennabathulanivas/Desktop/my projects/NIVORA/builder/css_styles.py', 'r', encoding='utf-8') as f:
        css_full = f.read()

    start_css_pos = 29041 - 70
    end_css_pos = css_full.find('/* =========================================================\n       ABOUT SECTION: LIFE CYCLE PIPELINE')
    extra_css = css_full[start_css_pos:end_css_pos]

    # Additional polish for buttons & dropdown
    additional_css = """
    /* Integration Enhancements */
    .world-btn-explore {
      padding: 9px 15px;
      font-size: 12px;
      font-weight: 700;
      border-radius: 9px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.16);
      color: #ffffff;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: var(--transition-smooth);
    }
    .world-btn-explore:hover {
      background: rgba(255, 255, 255, 0.16);
      border-color: rgba(255, 255, 255, 0.32);
      transform: translateY(-2px);
    }
    .tab-badge {
      font-size: 9px;
      padding: 2px 7px;
      border-radius: 999px;
      font-weight: 800;
      background: rgba(255, 255, 255, 0.1);
      color: #fff;
    }
    .tab-badge.concept {
      background: rgba(36, 216, 167, 0.18);
      color: var(--emerald);
      border: 1px solid rgba(36, 216, 167, 0.35);
    }
    .satellite {
      cursor: pointer;
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease;
    }
    .satellite:hover {
      transform: scale(1.1);
      box-shadow: 0 0 30px rgba(157, 92, 255, 0.4);
    }
    """

    full_extra_css = extra_css + additional_css

    # Inject CSS before </style>
    style_close = "</style>"
    if style_close in html:
        html = html.replace(style_close, full_extra_css + "\n  " + style_close, 1)

    # 2. Update navigation in topbar: Add Products Dropdown or deep dive anchors
    navlinks_old = """      <div class="navlinks">
        <a href="#home" class="active">Home</a>
        <a href="#products">Products</a>
        <a href="#about">About</a>
        <a href="#portfolio">Portfolio</a>
        <a href="#vision">Vision</a>
        <a href="#contact">Contact</a>
        <a href="#products" class="btn nav-cta">Explore Products</a>
      </div>"""

    navlinks_new = """      <div class="navlinks">
        <a href="#home" class="active">Home</a>
        <a href="#products">Products</a>
        <a href="#universe-philosophy">Universe</a>
        <a href="#explore">Deep Dives</a>
        <a href="#about">About</a>
        <a href="#portfolio">Portfolio</a>
        <a href="#vision">Vision</a>
        <a href="#contact">Contact</a>
        <a href="#explore" class="btn nav-cta">Explore Products</a>
      </div>"""

    html = html.replace(navlinks_old, navlinks_new)

    # 3. Add onclick to hero satellites
    html = html.replace('class="satellite s-checkra"', 'class="satellite s-checkra" onclick="openProductDeepDive(\'checkra\')" title="Explore CHECKRA"')
    html = html.replace('class="satellite s-homora"', 'class="satellite s-homora" onclick="openProductDeepDive(\'homora\')" title="Explore HOMORA"')
    html = html.replace('class="satellite s-bubora"', 'class="satellite s-bubora" onclick="openProductDeepDive(\'bubora\')" title="Explore BUBORA"')
    html = html.replace('class="satellite s-sayora"', 'class="satellite s-sayora" onclick="openProductDeepDive(\'sayora\')" title="Explore SAYORA"')

    # 4. Add "Explore Details ↓" buttons to the 4 product cards in #products
    # CHECKRA card footer
    checkra_old = """              <div class="world-footer">
                <a class="world-link" href="https://checkra.onrender.com/" target="_blank" rel="noopener noreferrer">
                  Visit CHECKRA <span class="btn-arrow">↗</span>
                </a>
                <span style="font-size:11px;color:#8f92a9;">Official Website</span>
              </div>"""

    checkra_new = """              <div class="world-footer">
                <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap;">
                  <a class="world-link" href="https://checkra.onrender.com/" target="_blank" rel="noopener noreferrer">
                    Visit CHECKRA <span class="btn-arrow">↗</span>
                  </a>
                  <button class="world-btn-explore" onclick="openProductDeepDive('checkra')">
                    Explore Details <span class="btn-arrow">↓</span>
                  </button>
                </div>
                <span style="font-size:11px;color:#8f92a9;">Live App</span>
              </div>"""

    html = html.replace(checkra_old, checkra_new)

    # HOMORA card footer
    homora_old = """              <div class="world-footer">
                <a class="world-link" href="https://homora-ai.vercel.app/" target="_blank" rel="noopener noreferrer">
                  Visit HOMORA <span class="btn-arrow">↗</span>
                </a>
                <span style="font-size:11px;color:#8f92a9;">Official Website</span>
              </div>"""

    homora_new = """              <div class="world-footer">
                <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap;">
                  <a class="world-link" href="https://homora-ai.vercel.app/" target="_blank" rel="noopener noreferrer">
                    Visit HOMORA <span class="btn-arrow">↗</span>
                  </a>
                  <button class="world-btn-explore" onclick="openProductDeepDive('homora')">
                    Explore Details <span class="btn-arrow">↓</span>
                  </button>
                </div>
                <span style="font-size:11px;color:#8f92a9;">Live Prototype</span>
              </div>"""

    html = html.replace(homora_old, homora_new)

    # BUBORA card footer
    bubora_old = """              <div class="world-footer">
                <a class="world-link" href="https://bubora.netlify.app/" target="_blank" rel="noopener noreferrer">
                  Visit BUBORA <span class="btn-arrow">↗</span>
                </a>
                <span style="font-size:11px;color:#8f92a9;">Official Website</span>
              </div>"""

    bubora_new = """              <div class="world-footer">
                <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap;">
                  <a class="world-link" href="https://bubora.netlify.app/" target="_blank" rel="noopener noreferrer">
                    Visit BUBORA <span class="btn-arrow">↗</span>
                  </a>
                  <button class="world-btn-explore" onclick="openProductDeepDive('bubora')">
                    Explore Details <span class="btn-arrow">↓</span>
                  </button>
                </div>
                <span style="font-size:11px;color:#8f92a9;">Live App</span>
              </div>"""

    html = html.replace(bubora_old, bubora_new)

    # SAYORA card footer
    sayora_old = """              <div class="world-footer">
                <span class="btn secondary" style="cursor:default;opacity:0.6;font-size:13px;padding:9px 18px;">
                  Concept Preview
                </span>
                <span style="font-size:11px;color:#8f92a9;">Social Impact Fund</span>
              </div>"""

    sayora_new = """              <div class="world-footer">
                <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap;">
                  <button class="world-btn-explore" onclick="openProductDeepDive('sayora')">
                    Explore Concept Details <span class="btn-arrow">↓</span>
                  </button>
                </div>
                <span style="font-size:11px;color:#8f92a9;">In Development</span>
              </div>"""

    html = html.replace(sayora_old, sayora_new)

    # 5. Build the Universe Philosophy and Product Deep-Dive Sections HTML
    universe_and_explore_html = """
    <!-- =========================================================
         SECTION: ONE UNIVERSE. DIFFERENT POSSIBILITIES.
         ========================================================= -->
    <section class="section" id="universe-philosophy">
      <div class="section-divider"></div>
      <div class="container">
        <div class="section-head reveal">
          <div>
            <div class="kicker">02 · The NIVORA Architecture</div>
            <h2>One Universe.<br><span class="grad">Different Possibilities.</span></h2>
          </div>
          <p>
            NIVORA products are not disconnected experiments. They are deliberate interventions across four foundational human spheres — unified by human-centered engineering, data sovereignty, and meticulous craft.
          </p>
        </div>

        <div class="universe-philosophy-card reveal">
          <div class="upc-lead">
            <p>
              From the intellectual integrity of academic writing, to domestic financial harmony, intimate relational spaces, and the economic resilience of gig workers — NIVORA transforms ambitious concepts into intelligent realities.
            </p>
          </div>

          <!-- 4-Pillar Spectrum Conduit -->
          <div class="universe-conduit-line">
            <div class="ucl-item t-checkra" onclick="openProductDeepDive('checkra')">
              <div class="ucl-theme">INTEGRITY</div>
              <b>CHECKRA</b>
              <p>Truth in written intelligence and creative thought.</p>
            </div>
            <div class="ucl-item t-homora" onclick="openProductDeepDive('homora')">
              <div class="ucl-theme">HARMONY</div>
              <b>HOMORA</b>
              <p>Clarity, trust, and equitability in collective living.</p>
            </div>
            <div class="ucl-item t-bubora" onclick="openProductDeepDive('bubora')">
              <div class="ucl-theme">CONNECTION</div>
              <b>BUBORA</b>
              <p>Intimacy, privacy, and shared emotional memory.</p>
            </div>
            <div class="ucl-item t-sayora" onclick="openProductDeepDive('sayora')">
              <div class="ucl-theme">RESILIENCE</div>
              <b>SAYORA</b>
              <p>Security, solidarity, and dignified worker protection.</p>
            </div>
          </div>

          <div class="upc-quote-footer">
            <b>&ldquo;Ideas become products when technology meets purpose.&rdquo;</b>
            <span style="font-size:13px;color:#8f92a9;">The Core NIVORA Innovation Philosophy · Nivas Bennabatthula</span>
          </div>
        </div>
      </div>
    </section>

    <!-- =========================================================
         SECTION: PRODUCT DEEP DIVE EXPLORER (#explore)
         ========================================================= -->
    <section class="section" id="explore">
      <div class="section-divider"></div>
      <div class="container">
        <div class="section-head reveal">
          <div>
            <div class="kicker">03 · Product Deep Dives</div>
            <h2>Explore the<br><span class="grad">Universe Worlds.</span></h2>
          </div>
          <p>
            Inspect the underlying problem space, workflows, architecture models, and ethical design principles of each NIVORA creation.
          </p>
        </div>

        <!-- Sticky Product Tabs -->
        <div class="product-tabs-wrapper">
          <button class="product-tab-btn tab-checkra active" id="tab-checkra" onclick="openProductDeepDive('checkra', event)">
            <img src="assets/images/checkra-logo.png" alt="CHECKRA">
            <span>CHECKRA</span>
            <span class="tab-badge">Live App</span>
          </button>
          <button class="product-tab-btn tab-homora" id="tab-homora" onclick="openProductDeepDive('homora', event)">
            <img src="assets/images/homora-logo.png" alt="HOMORA">
            <span>HOMORA</span>
            <span class="tab-badge">Active Prototype</span>
          </button>
          <button class="product-tab-btn tab-bubora" id="tab-bubora" onclick="openProductDeepDive('bubora', event)">
            <img src="assets/images/bubora-logo.png" alt="BUBORA">
            <span>BUBORA</span>
            <span class="tab-badge">Live App</span>
          </button>
          <button class="product-tab-btn tab-sayora" id="tab-sayora" onclick="openProductDeepDive('sayora', event)">
            <img src="assets/images/sayora-logo.png" alt="SAYORA">
            <span>SAYORA</span>
            <span class="tab-badge concept">Concept</span>
          </button>
        </div>

        <!-- 1. CHECKRA PANEL -->
        <div class="product-panel checkra-theme active" id="panel-checkra">
          <div class="detail-card-container">
            <!-- 01 Hero Header -->
            <div class="detail-header-block">
              <div class="dhb-logo-wrap">
                <img src="assets/images/checkra-logo.png" alt="CHECKRA Logo">
              </div>
              <div class="dhb-info-block">
                <div class="dhb-meta-row">
                  <span class="dhb-category">Writing Integrity · AI · Document Intelligence</span>
                  <span class="status-badge live">Live Application</span>
                  <span class="legacy-tag">Formerly VeriWrite</span>
                </div>
                <h3>CHECKRA</h3>
                <div class="dhb-positioning">&ldquo;Your Intelligent Writing Integrity Space&rdquo;</div>
                <p class="dhb-desc">
                  An AI-powered writing integrity and source verification platform designed to help students, researchers, educators, professionals, and content creators check, verify, and improve their writing in one connected workspace.
                </p>
                <div class="dhb-actions">
                  <a class="btn primary" href="https://checkra.onrender.com/" target="_blank" rel="noopener noreferrer">
                    Launch CHECKRA Web App <span class="btn-arrow">↗</span>
                  </a>
                  <button class="world-btn-explore" onclick="document.getElementById('checkra-levels').scrollIntoView({behavior:'smooth'})">
                    View 3-Level Evidence Model ↓
                  </button>
                </div>
              </div>
            </div>

            <!-- 02 About & 03 The Problem -->
            <div class="about-problem-grid">
              <div class="narrative-card">
                <div class="nc-kicker">02 · ABOUT THE PRODUCT</div>
                <h4>Unified Workspace Over Fragmented Checkers</h4>
                <p>
                  Instead of using separate tools for similarity checking, source verification, grammar correction, rewriting, and report generation, CHECKRA brings these capabilities together into one intelligent platform for analyzing and improving written content.
                </p>
              </div>
              <div class="narrative-card problem-highlight">
                <div class="nc-kicker">03 · THE REAL-WORLD PROBLEM</div>
                <h4>Opaque Scores &amp; Disconnected Tools</h4>
                <p>
                  Traditional similarity tools reduce analysis to a single blunt percentage without transparent proof. Authors suffer from tool-switching fatigue, false AI-generation accusations, and inability to trace exact source evidence.
                </p>
              </div>
            </div>

            <!-- 05 Core Idea Quote -->
            <div class="core-idea-banner">
              <div class="nc-kicker">05 · CORE PHILOSOPHY</div>
              <blockquote>&ldquo;Don&rsquo;t just check the writing. Understand it, verify it, and improve it.&rdquo;</blockquote>
              <p>
                CHECKRA takes a broader approach by combining Similarity Analysis + Source Verification + AI Evidence Review + Grammar Improvement + Intelligent Rewriting into one platform — providing transparent evidence that users can review and understand themselves.
              </p>
            </div>

            <!-- 04 Key Capabilities (8 capabilities) -->
            <div class="capabilities-section-title">
              <h4>04 · Key Capabilities</h4>
              <p>Eight intelligent modules engineered for comprehensive writing fidelity and elevation.</p>
            </div>
            <div class="capabilities-deep-grid">
              <div class="cap-deep-card">
                <b>Multi-Level Similarity Check</b>
                <p>Analyzes documents across three comparison tiers: exact matching, near matching with rearranged wording, and deep semantic similarity.</p>
              </div>
              <div class="cap-deep-card">
                <b>Web Source Verification</b>
                <p>Searches and indexes open web sources to pinpoint matching content and provide transparent source context and URL citations.</p>
              </div>
              <div class="cap-deep-card">
                <b>Unified Multi-Format Ingestion</b>
                <p>Native parsing and text extraction for PDF, DOCX, TXT, HTML, and Markdown files through a unified document analysis pipeline.</p>
              </div>
              <div class="cap-deep-card">
                <b>AI Evidence Review</b>
                <p>Assists human reviewers in evaluating matches, distinguishing quotes from accidental phrasing and intentional duplication.</p>
              </div>
              <div class="cap-deep-card">
                <b>Comprehensive Grammar Check</b>
                <p>Detects grammar, spelling, punctuation, and writing-quality issues with clean suggestions to heighten prose clarity.</p>
              </div>
              <div class="cap-deep-card">
                <b>5-Mode Intelligent Rewrite</b>
                <p>Rewriting modes: Clear &amp; Natural, Academic &amp; Readable, Professional, Concise, and Simple English with diff views.</p>
              </div>
              <div class="cap-deep-card">
                <b>Evidence-Based Reports</b>
                <p>Generates structured exportable reports containing similarity findings, matched excerpts, source info, and verification details.</p>
              </div>
              <div class="cap-deep-card">
                <b>Privacy &amp; Session Security</b>
                <p>Privacy-focused session processing, secure API-key handling, and zero permanent text storage to protect intellectual property.</p>
              </div>
            </div>

            <!-- 06 How It Works -->
            <div class="workflow-card-block">
              <h4>06 · How It Works · The 4-Step Pipeline</h4>
              <p>From draft upload to verified evidence report.</p>
              <div class="workflow-rail">
                <div class="wf-step">
                  <div class="wf-num">STEP 01</div>
                  <b>Ingest Document</b>
                  <p style="font-size:11px;color:#8f92a9;margin-top:4px;">Upload PDF, DOCX, TXT or paste draft.</p>
                </div>
                <div class="wf-step">
                  <div class="wf-num">STEP 02</div>
                  <b>Multi-Level Scan</b>
                  <p style="font-size:11px;color:#8f92a9;margin-top:4px;">Exact, near, and semantic similarity extraction.</p>
                </div>
                <div class="wf-step">
                  <div class="wf-num">STEP 03</div>
                  <b>Evidence &amp; Grammar</b>
                  <p style="font-size:11px;color:#8f92a9;margin-top:4px;">Examine source links, AI flags, and syntax issues.</p>
                </div>
                <div class="wf-step">
                  <div class="wf-num">STEP 04</div>
                  <b>Refine &amp; Export</b>
                  <p style="font-size:11px;color:#8f92a9;margin-top:4px;">Apply stylistic rewrites and export audit report.</p>
                </div>
              </div>
            </div>

            <!-- 07 3-Level Evidence Model -->
            <div class="ecosystem-visual-block" id="checkra-levels">
              <h4>07 · The 3-Level Evidence-Based Approach</h4>
              <p>Transparent evidence classification instead of an opaque black-box percentage.</p>
              <div class="eco-pill-stream">
                <div class="eco-stream-tag">
                  LEVEL 01: Exact Matching <span>Direct verbatim string sequences</span>
                </div>
                <div class="eco-stream-tag">
                  LEVEL 02: Near Matching <span>Rearranged, substituted, or mosaic phrasing</span>
                </div>
                <div class="eco-stream-tag">
                  LEVEL 03: Semantic Similarity <span>Different wording conveying identical concept</span>
                </div>
              </div>
            </div>

            <!-- 08 Responsible Design Ethics -->
            <div class="responsible-design-card">
              <span class="rdc-tag">08 · RESPONSIBLE DESIGN ETHICS</span>
              <h4>Evidence Over Automated Accusations</h4>
              <p>
                CHECKRA is built on the core principle that software should illuminate evidence, not make definitive punitive accusations. Similarity scores are indicators to guide human educators, editors, and authors — not unilateral verdicts.
              </p>
            </div>

            <!-- 09 Vision & Taglines -->
            <div class="vision-tagline-block">
              <div class="vtb-left">
                <h4>09 · PRODUCT VISION</h4>
                <p>To establish the universal open standard for intellectual provenance and writing elevation across academia and digital publishing.</p>
              </div>
              <div class="vtb-right">
                <div class="vtb-primary-tagline">Your Intelligent Writing Integrity Space.</div>
                <div class="vtb-secondary-tagline">&ldquo;Don&rsquo;t just check the writing. Understand it, verify it, and improve it.&rdquo;</div>
              </div>
            </div>

            <!-- 10 Cross-Navigation -->
            <div class="cross-nav-footer">
              <span style="font-size:13px;color:#8f92a9;">Continue Exploring the NIVORA Ecosystem:</span>
              <div class="cross-nav-links">
                <button class="cross-nav-btn" onclick="openProductDeepDive('homora')">Next: HOMORA (Shared Finance OS) →</button>
                <button class="cross-nav-btn" onclick="openProductDeepDive('bubora')">BUBORA →</button>
                <button class="cross-nav-btn" onclick="openProductDeepDive('sayora')">SAYORA →</button>
              </div>
            </div>
          </div>
        </div>

        <!-- 2. HOMORA PANEL -->
        <div class="product-panel homora-theme" id="panel-homora">
          <div class="detail-card-container">
            <!-- 01 Hero Header -->
            <div class="detail-header-block">
              <div class="dhb-logo-wrap">
                <img src="assets/images/homora-logo.png" alt="HOMORA Logo">
              </div>
              <div class="dhb-info-block">
                <div class="dhb-meta-row">
                  <span class="dhb-category">Smart Living · Shared Finance · Automation</span>
                  <span class="status-badge live">Active Prototype</span>
                </div>
                <h3>HOMORA</h3>
                <div class="dhb-positioning">&ldquo;Household Financial Operating System&rdquo;</div>
                <p class="dhb-desc">
                  A comprehensive financial and domestic operating system built for flatmates, couples, families, and co-living communities — turning chaotic shared expenses and awkward money reminders into transparent, harmonious group operations.
                </p>
                <div class="dhb-actions">
                  <a class="btn primary" href="https://homora-ai.vercel.app/" target="_blank" rel="noopener noreferrer">
                    Visit HOMORA Prototype <span class="btn-arrow">↗</span>
                  </a>
                  <button class="world-btn-explore" onclick="document.getElementById('homora-model').scrollIntoView({behavior:'smooth'})">
                    4-Layer Financial Model ↓
                  </button>
                </div>
              </div>
            </div>

            <!-- 02 About & 03 The Problem -->
            <div class="about-problem-grid">
              <div class="narrative-card">
                <div class="nc-kicker">02 · ABOUT THE PRODUCT</div>
                <h4>Moving Beyond Basic Expense Splitters</h4>
                <p>
                  HOMORA is not just a bill-splitting calculator. It provides a complete domestic operating infrastructure: uniting real-time shared balances, emergency pools, chore scheduling, grocery inventories, and AI spending intelligence into one platform.
                </p>
              </div>
              <div class="narrative-card problem-highlight">
                <div class="nc-kicker">03 · THE REAL-WORLD PROBLEM</div>
                <h4>Awkward Tension &amp; Domestic Friction</h4>
                <p>
                  Chasing housemates for bills damages relationships. Without a unified ledger, households overspend on groceries, miss utility payments, and suffer from unequal chore and financial burdens.
                </p>
              </div>
            </div>

            <!-- 05 Core Idea Quote -->
            <div class="core-idea-banner">
              <div class="nc-kicker">05 · CORE PHILOSOPHY</div>
              <blockquote>&ldquo;When shared finances are transparent, shared living becomes effortless.&rdquo;</blockquote>
              <p>
                Living together should be about mutual companionship and collective comfort — not ledger disputes, forgotten reimbursements, and anxiety at the end of every month.
              </p>
            </div>

            <!-- 04 Key Capabilities (14 capabilities) -->
            <div class="capabilities-section-title">
              <h4>04 · 14 Core Capabilities</h4>
              <p>Full-stack domestic financial operating system for modern co-living.</p>
            </div>
            <div class="capabilities-deep-grid">
              <div class="cap-deep-card">
                <b>Shared Finance &amp; Balances</b>
                <p>Real-time group ledger tracking who paid, who owes, and automatic net balance simplifications.</p>
              </div>
              <div class="cap-deep-card">
                <b>Automated Budgeting</b>
                <p>Monthly spending caps for rent, utilities, food, and social funds with automated velocity warnings.</p>
              </div>
              <div class="cap-deep-card">
                <b>Unified Expense Tracking</b>
                <p>Categorized spending logs with receipt attachments and flexible split ratios (equal, percentage, custom).</p>
              </div>
              <div class="cap-deep-card">
                <b>Fair Contribution Splits</b>
                <p>Income-weighted, room-size weighted, or usage-calibrated contribution models for true equitability.</p>
              </div>
              <div class="cap-deep-card">
                <b>Community Emergency Pool</b>
                <p>A communal reserve fund tracked inside the home for sudden appliance fixes, repairs, or unexpected bills.</p>
              </div>
              <div class="cap-deep-card">
                <b>Claims &amp; Reimbursements</b>
                <p>One-tap expense reimbursement requests with instant approval rules and audit timestamps.</p>
              </div>
              <div class="cap-deep-card">
                <b>Internal Micro-Loans</b>
                <p>Transparent flatmate-to-flatmate internal ledger tracking to advance funds without awkwardness.</p>
              </div>
              <div class="cap-deep-card">
                <b>Smart Grocery Planning</b>
                <p>Synchronized shared pantry lists, staple replenishment alerts, and duplicate purchase prevention.</p>
              </div>
              <div class="cap-deep-card">
                <b>Bills &amp; Subscriptions</b>
                <p>Shared recurring calendar for electricity, Wi-Fi, maid services, streaming accounts, and rent.</p>
              </div>
              <div class="cap-deep-card">
                <b>Chores &amp; Household Tasks</b>
                <p>Rotational cleaning schedules, trash duty assignments, and accountability check-ins.</p>
              </div>
              <div class="cap-deep-card">
                <b>Social Hub &amp; Memory Wall</b>
                <p>A communal home notice board for house announcements, guest visits, movie night polls, and photos.</p>
              </div>
              <div class="cap-deep-card">
                <b>Household Financial Insights</b>
                <p>Visual monthly expense trends, waste identification, and historical inflation on utility spend.</p>
              </div>
              <div class="cap-deep-card">
                <b>Financial Health Scorecard</b>
                <p>An algorithmic hygiene rating reflecting on-time settlements, budget adherence, and reserve health.</p>
              </div>
              <div class="cap-deep-card">
                <b>HOMORA Intel Assistant</b>
                <p>AI assistant analyzing patterns: &ldquo;Grocery expenses rose 18% due to brand substitutions — alternatives found.&rdquo;</p>
              </div>
            </div>

            <!-- 06 How It Works -->
            <div class="workflow-card-block">
              <h4>06 · How It Works · 4-Step Harmony Journey</h4>
              <p>Setup once, collaborate effortlessly daily, settle without friction monthly.</p>
              <div class="workflow-rail">
                <div class="wf-step">
                  <div class="wf-num">STEP 01</div>
                  <b>Create Space</b>
                  <p style="font-size:11px;color:#8f92a9;margin-top:4px;">Invite flatmates and configure home roles.</p>
                </div>
                <div class="wf-step">
                  <div class="wf-num">STEP 02</div>
                  <b>Set Rules &amp; Bills</b>
                  <p style="font-size:11px;color:#8f92a9;margin-top:4px;">Define split ratios, recurring utilities, and emergency buffer.</p>
                </div>
                <div class="wf-step">
                  <div class="wf-num">STEP 03</div>
                  <b>Live &amp; Log</b>
                  <p style="font-size:11px;color:#8f92a9;margin-top:4px;">Log grocery runs, complete chores, and update balances.</p>
                </div>
                <div class="wf-step">
                  <div class="wf-num">STEP 04</div>
                  <b>Net Settlement</b>
                  <p style="font-size:11px;color:#8f92a9;margin-top:4px;">Settle balances with mathematically simplified transfers.</p>
                </div>
              </div>
            </div>

            <!-- 07 4-Layer Financial Model -->
            <div class="ecosystem-visual-block" id="homora-model">
              <h4>07 · The 4-Layer Financial Architecture</h4>
              <p>How HOMORA structures domestic capital flow.</p>
              <div class="eco-pill-stream">
                <div class="eco-stream-tag">LAYER 01: Record <span>Ledger ingestion of all payments, bills, and receipts</span></div>
                <div class="eco-stream-tag">LAYER 02: Allocate <span>Equitable rule-based distribution across housemates</span></div>
                <div class="eco-stream-tag">LAYER 03: Harmonize <span>Debt simplification netting to minimize transactions</span></div>
                <div class="eco-stream-tag">LAYER 04: Predict <span>HOMORA Intel forecast engine for utility &amp; food spend</span></div>
              </div>
            </div>

            <!-- 08 Responsible Design Ethics -->
            <div class="responsible-design-card">
              <span class="rdc-tag">08 · RESPONSIBLE DESIGN &amp; LEGAL CLARITY</span>
              <h4>Non-Bank &amp; Non-Depository Software Architecture</h4>
              <p>
                <strong>HOMORA is a financial management software tool — not a bank, NBFC, payment processor, or depository institution.</strong> All internal loans, pools, and balances represent mathematical accounting ledgers maintained by housemates. HOMORA does not hold customer funds or underwrite credit.
              </p>
            </div>

            <!-- 09 Vision & Taglines -->
            <div class="vision-tagline-block">
              <div class="vtb-left">
                <h4>09 · PRODUCT VISION</h4>
                <p>To power millions of harmonious shared households, urban apartments, and co-living communities worldwide.</p>
              </div>
              <div class="vtb-right">
                <div class="vtb-primary-tagline">Household Financial Operating System.</div>
                <div class="vtb-secondary-tagline">&ldquo;Smart Living · Shared Finance · Effortless Harmony.&rdquo;</div>
              </div>
            </div>

            <!-- 10 Cross-Navigation -->
            <div class="cross-nav-footer">
              <span style="font-size:13px;color:#8f92a9;">Continue Exploring the NIVORA Ecosystem:</span>
              <div class="cross-nav-links">
                <button class="cross-nav-btn" onclick="openProductDeepDive('bubora')">Next: BUBORA (Couples Space) →</button>
                <button class="cross-nav-btn" onclick="openProductDeepDive('sayora')">SAYORA →</button>
                <button class="cross-nav-btn" onclick="openProductDeepDive('checkra')">CHECKRA →</button>
              </div>
            </div>
          </div>
        </div>

        <!-- 3. BUBORA PANEL -->
        <div class="product-panel bubora-theme" id="panel-bubora">
          <div class="detail-card-container">
            <!-- 01 Hero Header -->
            <div class="detail-header-block">
              <div class="dhb-logo-wrap">
                <img src="assets/images/bubora-logo.png" alt="BUBORA Logo">
              </div>
              <div class="dhb-info-block">
                <div class="dhb-meta-row">
                  <span class="dhb-category">Private Digital Space · Couples · Relationships</span>
                  <span class="status-badge live">Live Application</span>
                </div>
                <h3>BUBORA</h3>
                <div class="dhb-positioning">&ldquo;A Private Digital Home for Two&rdquo;</div>
                <p class="dhb-desc">
                  An intimate, distraction-free sanctuary designed exclusively for couples. Free from public social feeds, intrusive algorithms, and advertising noise — BUBORA provides a dedicated haven to communicate, preserve memories, plan trips, and build a life together.
                </p>
                <div class="dhb-actions">
                  <a class="btn primary" href="https://bubora.netlify.app/" target="_blank" rel="noopener noreferrer">
                    Visit BUBORA Web App <span class="btn-arrow">↗</span>
                  </a>
                  <button class="world-btn-explore" onclick="document.getElementById('bubora-privacy').scrollIntoView({behavior:'smooth'})">
                    Privacy Principles ↓
                  </button>
                </div>
              </div>
            </div>

            <!-- 02 About & 03 The Problem -->
            <div class="about-problem-grid">
              <div class="narrative-card">
                <div class="nc-kicker">02 · ABOUT THE PRODUCT</div>
                <h4>A Sanctuary Designed for Precisely Two</h4>
                <p>
                  Modern couple lives are fragmented across messaging apps, photo clouds, note apps, and travel sites. BUBORA consolidates intimacy into one protected, beautifully crafted digital room where sacred memories are never buried under group chats.
                </p>
              </div>
              <div class="narrative-card problem-highlight">
                <div class="nc-kicker">03 · THE REAL-WORLD PROBLEM</div>
                <h4>Feed Addiction vs Relational Depth</h4>
                <p>
                  Mainstream social media platforms are optimized for algorithmic outrage, public performance, and data mining — the exact opposite of private, vulnerable, and meaningful emotional bonding.
                </p>
              </div>
            </div>

            <!-- 05 Core Idea Quote -->
            <div class="core-idea-banner">
              <div class="nc-kicker">05 · CORE PHILOSOPHY</div>
              <blockquote>&ldquo;Not every space needs a crowd. Some spaces are sacred for two.&rdquo;</blockquote>
              <p>
                In a world of noisy group chats and viral attention algorithms, BUBORA returns to the fundamental beauty of two people sharing moments, secrets, and future dreams in complete privacy.
              </p>
            </div>

            <!-- 04 Key Capabilities (8 capabilities) -->
            <div class="capabilities-section-title">
              <h4>04 · 8 Core Capabilities</h4>
              <p>Everything two partners need to nurture and preserve their shared journey.</p>
            </div>
            <div class="capabilities-deep-grid">
              <div class="cap-deep-card">
                <b>Our Chat &amp; Intimate Messaging</b>
                <p>Dedicated private messaging channel with pinned memories, voice notes, stickers, and zero external alerts.</p>
              </div>
              <div class="cap-deep-card">
                <b>Memories &amp; Photo Timeline</b>
                <p>An interactive chronological timeline capturing first dates, trips, holidays, and milestones in high fidelity.</p>
              </div>
              <div class="cap-deep-card">
                <b>Shared Calendar &amp; Countdowns</b>
                <p>Synchronized calendar with live countdown timers for anniversaries, flights, reunions, and date nights.</p>
              </div>
              <div class="cap-deep-card">
                <b>Plans &amp; Trip Itineraries</b>
                <p>Collaborative travel itineraries with hotel details, flight bookings, packing checklists, and must-see spot pins.</p>
              </div>
              <div class="cap-deep-card">
                <b>Goals &amp; Joint Milestones</b>
                <p>Long-term aspirations tracked visually: saving for an apartment, fitness challenges, books, or skills to learn together.</p>
              </div>
              <div class="cap-deep-card">
                <b>Couples Money &amp; Shared Expenses</b>
                <p>Simple joint expense tracking without awkward balance demands — keeping dining, gifts, and bills harmonious.</p>
              </div>
              <div class="cap-deep-card">
                <b>Curated Activities &amp; Date Ideas</b>
                <p>Date night generators, surprise activity prompts, and bucket list suggestions tailored for couple fun.</p>
              </div>
              <div class="cap-deep-card">
                <b>Private Vault</b>
                <p>Secure client-side encrypted vault for sensitive documents, emergency contacts, door codes, and cherished letters.</p>
              </div>
            </div>

            <!-- 06 How It Works -->
            <div class="workflow-card-block">
              <h4>06 · How It Works · Initiation to Daily Harmony</h4>
              <p>Simple pairing to a permanent private sanctuary.</p>
              <div class="workflow-rail">
                <div class="wf-step">
                  <div class="wf-num">STEP 01</div>
                  <b>Pair Sanctuary</b>
                  <p style="font-size:11px;color:#8f92a9;margin-top:4px;">Generate private pairing code to lock space for two.</p>
                </div>
                <div class="wf-step">
                  <div class="wf-num">STEP 02</div>
                  <b>Anchor Milestones</b>
                  <p style="font-size:11px;color:#8f92a9;margin-top:4px;">Set anniversary dates, upcoming trips, and first photos.</p>
                </div>
                <div class="wf-step">
                  <div class="wf-num">STEP 03</div>
                  <b>Daily Living</b>
                  <p style="font-size:11px;color:#8f92a9;margin-top:4px;">Send love notes, sync schedules, and coordinate plans.</p>
                </div>
                <div class="wf-step">
                  <div class="wf-num">STEP 04</div>
                  <b>Living Scrapbook</b>
                  <p style="font-size:11px;color:#8f92a9;margin-top:4px;">Review annual retrospectives in an immortal memory vault.</p>
                </div>
              </div>
            </div>

            <!-- 07 Privacy Architecture -->
            <div class="ecosystem-visual-block" id="bubora-privacy">
              <h4>07 · Privacy-First Architecture</h4>
              <p>Built with absolute data dignity at its core.</p>
              <div class="eco-pill-stream">
                <div class="eco-stream-tag">PRINCIPLE 01: Zero Surveillance <span>No ad trackers, marketing pixels, or data brokering</span></div>
                <div class="eco-stream-tag">PRINCIPLE 02: Two-Party Enclave <span>Strictly 2 accounts per space; 3rd party viewing impossible</span></div>
                <div class="eco-stream-tag">PRINCIPLE 03: Client-Side Vault <span>Private documents encrypted client-side</span></div>
              </div>
            </div>

            <!-- 08 Responsible Design Ethics -->
            <div class="responsible-design-card">
              <span class="rdc-tag">08 · RESPONSIBLE DESIGN ETHICS</span>
              <h4>No Dopamine Exploitation · Real-Life Connection</h4>
              <p>
                BUBORA omits infinite feeds, likes, algorithmic notifications, and attention hacks. The software exists to nourish offline romance, real presence, and genuine affection — not to trap users in digital loops.
              </p>
            </div>

            <!-- 09 Vision & Taglines -->
            <div class="vision-tagline-block">
              <div class="vtb-left">
                <h4>09 · PRODUCT VISION</h4>
                <p>To establish the global benchmark for intimate digital enclaves, safeguarding memories for couples worldwide.</p>
              </div>
              <div class="vtb-right">
                <div class="vtb-primary-tagline">A Private Digital Home for Two.</div>
                <div class="vtb-secondary-tagline">&ldquo;Not every space needs a crowd. Some spaces are sacred for two.&rdquo;</div>
              </div>
            </div>

            <!-- 10 Cross-Navigation -->
            <div class="cross-nav-footer">
              <span style="font-size:13px;color:#8f92a9;">Continue Exploring the NIVORA Ecosystem:</span>
              <div class="cross-nav-links">
                <button class="cross-nav-btn" onclick="openProductDeepDive('sayora')">Next: SAYORA (Gig Worker Fund) →</button>
                <button class="cross-nav-btn" onclick="openProductDeepDive('checkra')">CHECKRA →</button>
                <button class="cross-nav-btn" onclick="openProductDeepDive('homora')">HOMORA →</button>
              </div>
            </div>
          </div>
        </div>

        <!-- 4. SAYORA PANEL -->
        <div class="product-panel sayora-theme" id="panel-sayora">
          <div class="detail-card-container">
            <!-- 01 Hero Header -->
            <div class="detail-header-block">
              <div class="dhb-logo-wrap">
                <img src="assets/images/sayora-logo.png" alt="SAYORA Logo">
              </div>
              <div class="dhb-info-block">
                <div class="dhb-meta-row">
                  <span class="dhb-category">Financial Resilience · Gig Economy · Social Impact</span>
                  <span class="status-badge concept">Concept · In Development</span>
                </div>
                <h3>SAYORA</h3>
                <div class="dhb-positioning">&ldquo;Together for a Safer Tomorrow · Small Steps. Stronger Communities.&rdquo;</div>
                <p class="dhb-desc">
                  A community-backed financial safety net and emergency resilience concept engineered for platform delivery executives, drivers, and informal gig workers — providing transparent micro-savings, peer assistance pools, crisis relief, and welfare scheme discovery.
                </p>
                <div class="dhb-actions">
                  <button class="world-btn-explore" onclick="document.getElementById('sayora-model').scrollIntoView({behavior:'smooth'})">
                    4-Level Resilience Model ↓
                  </button>
                  <a class="btn secondary" href="#contact">
                    Partner With SAYORA R&amp;D <span class="btn-arrow">→</span>
                  </a>
                </div>
              </div>
            </div>

            <!-- 02 About & 03 The Problem -->
            <div class="about-problem-grid">
              <div class="narrative-card">
                <div class="nc-kicker">02 · ABOUT THE CONCEPT</div>
                <h4>Bridging the Gig Safety Deficit</h4>
                <p>
                  Millions of delivery partners and drivers power modern cities but operate without safety nets, paid sick leave, or health cushions. SAYORA explores mutual-aid micro-savings pools, CSR matching grants, and parametric extreme weather relief into one dignified safety architecture.
                </p>
              </div>
              <div class="narrative-card problem-highlight">
                <div class="nc-kicker">03 · THE REAL-WORLD PROBLEM</div>
                <h4>Income Shocks &amp; Predatory Debt</h4>
                <p>
                  A single bike accident, hospital visit, or flood week can destroy informal workers' livelihood, forcing them into high-interest informal loans. Complex paperwork also blocks them from government welfare schemes.
                </p>
              </div>
            </div>

            <!-- 05 Core Idea Quote -->
            <div class="core-idea-banner">
              <div class="nc-kicker">05 · CORE PHILOSOPHY</div>
              <blockquote>&ldquo;Those who support our cities deserve a system that supports them.&rdquo;</blockquote>
              <p>
                Economic security should not belong only to salaried executives. Flexible labor demands flexible, empathetic, and resilient safety systems.
              </p>
            </div>

            <!-- 04 Key Capabilities (13 capabilities) -->
            <div class="capabilities-section-title">
              <h4>04 · 13 Core Concept Capabilities</h4>
              <p>Architectural pillars designed for informal worker dignity and resilience.</p>
            </div>
            <div class="capabilities-deep-grid">
              <div class="cap-deep-card">
                <b>Smart Micro-Savings</b>
                <p>Frictionless round-up savings from daily trip earnings into a personal emergency reserve.</p>
              </div>
              <div class="cap-deep-card">
                <b>Peer Protection Pool</b>
                <p>Community mutual aid fund where tiny voluntary contributions unlock communal emergency assistance.</p>
              </div>
              <div class="cap-deep-card">
                <b>Community Support Network</b>
                <p>Peer verifiers and fellow workers vouching for incident authenticity and offering roadside solidarity.</p>
              </div>
              <div class="cap-deep-card">
                <b>Emergency Assistance</b>
                <p>Rapid micro-disbursements for urgent hospital out-of-pocket costs, medicines, or tire repairs.</p>
              </div>
              <div class="cap-deep-card">
                <b>Climate &amp; Crisis Relief</b>
                <p>Parametric relief alerts triggered during severe heatwaves, floods, hazardous air quality, or curfews.</p>
              </div>
              <div class="cap-deep-card">
                <b>Corporate CSR Matching</b>
                <p>Channel for logistics platforms and philanthropic foundations to match worker contributions 1:1.</p>
              </div>
              <div class="cap-deep-card">
                <b>Welfare Scheme Discovery</b>
                <p>Automated matching engine pairing workers with official government social security boards (e-Shram, PM-JAY).</p>
              </div>
              <div class="cap-deep-card">
                <b>Financial Literacy Guides</b>
                <p>Vernacular audio and visual guides on debt avoidance, compound interest, tax basics, and budget management.</p>
              </div>
              <div class="cap-deep-card">
                <b>Essential Money Services</b>
                <p>Affordable low-cost micro-transfers, emergency bill buffering, and zero-penalty credit builder partnerships.</p>
              </div>
              <div class="cap-deep-card">
                <b>Digital SAYORA ID</b>
                <p>A portable digital identity consolidating work tenure, reliability scores, and safety contributions.</p>
              </div>
              <div class="cap-deep-card">
                <b>Transparent Impact Analytics</b>
                <p>Publicly auditable open-ledger verification showing exactly where every dollar of mutual aid was disbursed.</p>
              </div>
              <div class="cap-deep-card">
                <b>Ask SAYORA Assistant</b>
                <p>Multilingual voice-first AI assistant answering queries on claims, benefits, and emergency clinic locations.</p>
              </div>
              <div class="cap-deep-card">
                <b>Security &amp; Data Trust</b>
                <p>Zero sharing of worker data with platform employers, preventing retaliatory deactivations and preserving privacy.</p>
              </div>
            </div>

            <!-- 06 How It Works -->
            <div class="workflow-card-block">
              <h4>06 · How It Works · Member &amp; Community Flow</h4>
              <p>Simple lifecycle designed for mobile-first, on-the-road workers.</p>
              <div class="workflow-rail">
                <div class="wf-step">
                  <div class="wf-num">STEP 01</div>
                  <b>Generate ID</b>
                  <p style="font-size:11px;color:#8f92a9;margin-top:4px;">Create portable profile and link micro-stash rules.</p>
                </div>
                <div class="wf-step">
                  <div class="wf-num">STEP 02</div>
                  <b>Micro-Stash &amp; Match</b>
                  <p style="font-size:11px;color:#8f92a9;margin-top:4px;">Daily savings build buffer, augmented by CSR grants.</p>
                </div>
                <div class="wf-step">
                  <div class="wf-num">STEP 03</div>
                  <b>Incident Claim</b>
                  <p style="font-size:11px;color:#8f92a9;margin-top:4px;">Submit verified photo/audio claim in case of accident or storm.</p>
                </div>
                <div class="wf-step">
                  <div class="wf-num">STEP 04</div>
                  <b>Relief Payout</b>
                  <p style="font-size:11px;color:#8f92a9;margin-top:4px;">Immediate assistance disburses directly to worker's wallet.</p>
                </div>
              </div>
            </div>

            <!-- 07 4-Level Resilience Model -->
            <div class="ecosystem-visual-block" id="sayora-model">
              <h4>07 · 4-Level Resilience Architecture</h4>
              <p>Systematic layers of protection.</p>
              <div class="eco-pill-stream">
                <div class="eco-stream-tag">LEVEL 01: Save <span>Individual micro-savings for personal day-to-day emergencies</span></div>
                <div class="eco-stream-tag">LEVEL 02: Protect <span>Mutual aid pool absorbing medium financial shocks collectively</span></div>
                <div class="eco-stream-tag">LEVEL 03: Recover <span>CSR matching grants and extreme weather parametric relief</span></div>
                <div class="eco-stream-tag">LEVEL 04: Advance <span>Welfare scheme discovery, literacy, and portable credentialing</span></div>
              </div>
            </div>

            <!-- 08 Responsible Design Ethics -->
            <div class="responsible-design-card">
              <span class="rdc-tag">08 · RESPONSIBLE DESIGN &amp; HONEST CONSTRAINTS</span>
              <h4>Concept Status · Transparent Regulatory Clarity</h4>
              <p>
                <strong>SAYORA is an architectural concept and R&amp;D initiative within the NIVORA innovation ecosystem.</strong> It is not currently a licensed insurance company, bank, credit union, or registered financial service provider. Full implementation will be operated in direct partnership with regulated banking institutions, authorized insurance underwriters, and registered non-profit welfare trusts.
              </p>
            </div>

            <!-- 09 Vision & Taglines -->
            <div class="vision-tagline-block">
              <div class="vtb-left">
                <h4>09 · PRODUCT VISION</h4>
                <p>To architect an open resilience protocol embedded across emerging market gig platforms, protecting over 100,000 workers with dignity.</p>
              </div>
              <div class="vtb-right">
                <div class="vtb-primary-tagline">Together for a Safer Tomorrow.</div>
                <div class="vtb-secondary-tagline">&ldquo;Small Steps. Stronger Communities.&rdquo;</div>
              </div>
            </div>

            <!-- 10 Cross-Navigation -->
            <div class="cross-nav-footer">
              <span style="font-size:13px;color:#8f92a9;">Continue Exploring the NIVORA Ecosystem:</span>
              <div class="cross-nav-links">
                <button class="cross-nav-btn" onclick="openProductDeepDive('checkra')">Back to: CHECKRA →</button>
                <button class="cross-nav-btn" onclick="openProductDeepDive('homora')">HOMORA →</button>
                <button class="cross-nav-btn" onclick="openProductDeepDive('bubora')">BUBORA →</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
"""

    # Inject the Universe Philosophy and Product Deep-Dive sections right after </section> of #products
    products_close = '    </section>\n\n    <!-- ABOUT SECTION -->'
    if products_close in html:
        html = html.replace(products_close, '    </section>\n\n' + universe_and_explore_html + '\n\n    <!-- ABOUT SECTION -->', 1)
    else:
        # fallback search
        prod_end = html.find('id="about"')
        if prod_end != -1:
            sec_before = html.rfind('</section>', 0, prod_end)
            if sec_before != -1:
                html = html[:sec_before+10] + '\n\n' + universe_and_explore_html + '\n\n' + html[sec_before+10:]

    # 6. Add the JavaScript function openProductDeepDive and Hash Handler to the <script> block
    js_code = """
    // -------------------------------------------------------------
    // Product Deep-Dive Tab Switcher & Hash Routing
    // -------------------------------------------------------------
    function openProductDeepDive(productKey, event) {
      if (event && event.preventDefault) {
        event.preventDefault();
      }
      var validTabs = ['checkra', 'homora', 'bubora', 'sayora'];
      if (validTabs.indexOf(productKey) === -1) return;

      // Update Tab Buttons
      validTabs.forEach(function(k) {
        var btn = document.getElementById('tab-' + k);
        var panel = document.getElementById('panel-' + k);
        if (btn) {
          if (k === productKey) {
            btn.classList.add('active');
          } else {
            btn.classList.remove('active');
          }
        }
        if (panel) {
          if (k === productKey) {
            panel.classList.add('active');
          } else {
            panel.classList.remove('active');
          }
        }
      });

      // Smooth scroll to #explore section
      var exploreSection = document.getElementById('explore');
      if (exploreSection) {
        var navHeight = 80;
        var topPos = exploreSection.getBoundingClientRect().top + window.pageYOffset - navHeight;
        window.scrollTo({
          top: topPos,
          behavior: 'smooth'
        });
      }

      // Update URL hash without causing instant jump
      if (window.history && window.history.pushState) {
        window.history.pushState(null, null, '#' + productKey);
      } else {
        window.location.hash = '#' + productKey;
      }
    }

    // Auto-detect hash on load or hashchange
    function checkHashRoute() {
      var hash = window.location.hash.replace('#', '').toLowerCase();
      if (['checkra', 'homora', 'bubora', 'sayora'].indexOf(hash) !== -1) {
        openProductDeepDive(hash);
      }
    }
    window.addEventListener('hashchange', checkHashRoute);
    window.addEventListener('DOMContentLoaded', checkHashRoute);
"""

    script_close = "</script>"
    if script_close in html:
        html = html.replace(script_close, js_code + "\n  " + script_close, 1)

    # Write output to Desktop & Downloads
    desktop_file = "/Users/bennabathulanivas/Desktop/my projects/NIVORA/index.html"
    downloads_file = "/Users/bennabathulanivas/Downloads/NIVORA/index.html"

    with open(desktop_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully integrated master experience into {desktop_file} ({len(html)} chars)")

    with open(downloads_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully integrated master experience into {downloads_file} ({len(html)} chars)")

if __name__ == "__main__":
    build_integration()
