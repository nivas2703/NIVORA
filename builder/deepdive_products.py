# builder/deepdive_products.py

DEEPDIVE_PRODUCTS_HTML = """
        <!-- Product Deep-Dive Explorer Section -->
        <section class="section deepdive-section" id="explore">
            <div class="container">
                <div class="deepdive-header text-center reveal-fade">
                    <span class="section-badge badge-deepdive">PRODUCT DEEP DIVES</span>
                    <h2 class="section-title">Explore the Product Universe</h2>
                    <p class="section-subtitle">
                        Step inside the architecture, problem space, workflows, and technical philosophies powering each NIVORA creation.
                    </p>
                </div>

                <!-- Sticky Tab Selector -->
                <div class="product-tabs-wrapper sticky-tabs">
                    <div class="product-tabs-container" role="tablist" aria-label="NIVORA Products">
                        <button class="tab-button tab-checkra active" role="tab" aria-selected="true" aria-controls="panel-checkra" id="tab-checkra" onclick="switchProductTab('checkra')">
                            <span class="tab-dot"></span>
                            <img src="assets/images/checkra-logo.png" alt="" class="tab-icon">
                            <span class="tab-label">CHECKRA</span>
                            <span class="tab-badge">Live</span>
                        </button>
                        <button class="tab-button tab-homora" role="tab" aria-selected="false" aria-controls="panel-homora" id="tab-homora" onclick="switchProductTab('homora')">
                            <span class="tab-dot"></span>
                            <img src="assets/images/homora-logo.png" alt="" class="tab-icon">
                            <span class="tab-label">HOMORA</span>
                            <span class="tab-badge">Live</span>
                        </button>
                        <button class="tab-button tab-bubora" role="tab" aria-selected="false" aria-controls="panel-bubora" id="tab-bubora" onclick="switchProductTab('bubora')">
                            <span class="tab-dot"></span>
                            <img src="assets/images/bubora-logo.png" alt="" class="tab-icon">
                            <span class="tab-label">BUBORA</span>
                            <span class="tab-badge">Live</span>
                        </button>
                        <button class="tab-button tab-sayora" role="tab" aria-selected="false" aria-controls="panel-sayora" id="tab-sayora" onclick="switchProductTab('sayora')">
                            <span class="tab-dot"></span>
                            <img src="assets/images/sayora-logo.png" alt="" class="tab-icon">
                            <span class="tab-label">SAYORA</span>
                            <span class="tab-badge tab-badge-concept">Concept</span>
                        </button>
                    </div>
                </div>

                <!-- Product Panels Container -->
                <div class="product-panels-viewport">

                    <!-- ========================================== -->
                    <!-- 1. CHECKRA PANEL                           -->
                    <!-- ========================================== -->
                    <div class="product-panel panel-checkra active" id="panel-checkra" role="tabpanel" aria-labelledby="tab-checkra">
                        <!-- 01. Hero & Positioning -->
                        <div class="panel-hero-card">
                            <div class="panel-hero-glow"></div>
                            <div class="panel-hero-content">
                                <div class="panel-brand-header">
                                    <div class="panel-logo-box">
                                        <img src="assets/images/checkra-logo.png" alt="CHECKRA Logo" class="panel-logo">
                                    </div>
                                    <div class="panel-title-group">
                                        <div class="panel-meta-tags">
                                            <span class="tag-category">Writing Integrity &middot; AI &middot; Document Intelligence</span>
                                            <span class="tag-status live-status"><span class="dot"></span> Live Application</span>
                                            <span class="tag-note">Formerly VeriWrite</span>
                                        </div>
                                        <h2 class="panel-main-title">CHECKRA</h2>
                                        <p class="panel-positioning">&ldquo;Your Intelligent Writing Integrity Space&rdquo;</p>
                                    </div>
                                </div>
                                <p class="panel-lead">
                                    An AI-powered writing integrity and source verification platform designed to help students, researchers, educators, professionals, and content creators check, verify, and improve their writing in one connected, evidence-driven workspace.
                                </p>
                                <div class="panel-hero-ctas">
                                    <a href="https://checkra.onrender.com/" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
                                        <span>Launch CHECKRA Web App</span>
                                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                            <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                                            <polyline points="15 3 21 3 21 9"></polyline>
                                            <line x1="10" y1="14" x2="21" y2="3"></line>
                                        </svg>
                                    </a>
                                    <a href="#checkra-workflow" class="btn btn-secondary">
                                        <span>View 3-Level Architecture</span>
                                    </a>
                                </div>
                            </div>
                        </div>

                        <!-- 02. About the Product -->
                        <div class="deep-section">
                            <div class="section-label-bar">
                                <span class="step-num">02</span>
                                <span class="step-title">ABOUT THE PLATFORM</span>
                            </div>
                            <div class="text-columns">
                                <div class="col-lead">
                                    <h3 class="deep-heading">Unified Intelligence Over Fragmented Checkers</h3>
                                    <p>
                                        Modern document review is painfully fragmented. Writers, students, and research teams are forced to shuffle across separate tools for similarity percentages, search engines for source citations, spellcheck extensions for grammar, rewriting bots for tone, and manual formatters for reports.
                                    </p>
                                </div>
                                <div class="col-detail">
                                    <p>
                                        CHECKRA eliminates tool switching by synthesizing similarity detection, web source evidence review, grammar correction, five intelligent rewriting styles, and verifiable report generation into a single intuitive interface. It shifts document evaluation from punitive scoring to transparent writing improvement.
                                    </p>
                                </div>
                            </div>
                        </div>

                        <!-- 03. The Problem It Solves -->
                        <div class="deep-section">
                            <div class="section-label-bar">
                                <span class="step-num">03</span>
                                <span class="step-title">THE PROBLEM IT SOLVES</span>
                            </div>
                            <div class="problems-grid">
                                <div class="problem-item">
                                    <div class="prob-num">01</div>
                                    <h4>Opaque &ldquo;Black Box&rdquo; Scores</h4>
                                    <p>Traditional plagiarism tools output a blunt percentage without transparent proof, triggering false alarms and academic panic over common idioms.</p>
                                </div>
                                <div class="problem-item">
                                    <div class="prob-num">02</div>
                                    <h4>Tool Switching Fatigue</h4>
                                    <p>Using one site for plagiarism, another for grammar, a third for paraphrasing, and a fourth to export reports drains time and creates data fragmentation.</p>
                                </div>
                                <div class="problem-item">
                                    <div class="prob-num">03</div>
                                    <h4>Superficial AI Classifiers</h4>
                                    <p>Crude AI detectors flag original human thoughts as synthetic while missing subtle mosaic plagiarism, paraphrased sources, and semantic duplication.</p>
                                </div>
                            </div>
                        </div>

                        <!-- 04. Key Capabilities (8 Core Capabilities) -->
                        <div class="deep-section">
                            <div class="section-label-bar">
                                <span class="step-num">04</span>
                                <span class="step-title">KEY CAPABILITIES</span>
                            </div>
                            <div class="capabilities-grid">
                                <div class="cap-card">
                                    <div class="cap-icon-box">
                                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                                    </div>
                                    <h4>Multi-Level Similarity Check</h4>
                                    <p>Analyzes documents across three tiered comparison layers: exact string matching, near matching with reordered phrasing, and semantic conceptual similarity.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box">
                                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><path d="M11 8v6"></path><path d="M8 11h6"></path></svg>
                                    </div>
                                    <h4>Web Source Verification</h4>
                                    <p>Conducts live web search passes to locate potential matching source materials, indexing source URLs, match context, and publication relevance.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box">
                                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line></svg>
                                    </div>
                                    <h4>Unified Document Analysis</h4>
                                    <p>Full native ingestion of PDF, DOCX, TXT, HTML, and Markdown formats with layout parsing, chapter segmentation, and clean text extraction.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box">
                                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>
                                    </div>
                                    <h4>AI Evidence Review</h4>
                                    <p>Assists human reviewers in evaluating detected passages, clarifying whether matches represent direct quotation, accidental overlap, or true duplication.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box">
                                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg>
                                    </div>
                                    <h4>Comprehensive Grammar Check</h4>
                                    <p>Identifies grammatical missteps, punctuation anomalies, misspelled terms, weak syntax, and wordiness to heighten clarity and reading fluency.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box">
                                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                                    </div>
                                    <h4>5-Mode Intelligent Rewrite</h4>
                                    <p>Tailors text without distorting intent: Clear &amp; Natural, Academic &amp; Readable, Professional, Concise, and Simple English with side-by-side diffs.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box">
                                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="12" y1="18" x2="12" y2="12"></line><line x1="9" y1="15" x2="15" y2="15"></line></svg>
                                    </div>
                                    <h4>Evidence-Based Reports</h4>
                                    <p>Generates audit-ready structured summaries detailing exact match highlights, source citations, classification metadata, and revision trails.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box">
                                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                                    </div>
                                    <h4>Privacy &amp; Session Security</h4>
                                    <p>Session-based analysis with secure API key handling, non-retention options, and end-to-end data isolation to safeguard intellectual property.</p>
                                </div>
                            </div>
                        </div>

                        <!-- 05. Core Idea / Philosophy -->
                        <div class="deep-section">
                            <div class="quote-callout callout-checkra">
                                <div class="quote-tag">CORE PHILOSOPHY</div>
                                <blockquote>
                                    &ldquo;Don&rsquo;t just check the writing. Understand it, verify it, and improve it.&rdquo;
                                </blockquote>
                                <p class="quote-subtext">
                                    The goal of writing intelligence is not to punish writers with an arbitrary percentage score. It is to equip authors and educators with transparent evidence so they can discern true source lineage, elevate grammar, and refine their own voice.
                                </p>
                            </div>
                        </div>

                        <!-- 06. How It Works (Workflow Rail) -->
                        <div class="deep-section" id="checkra-workflow">
                            <div class="section-label-bar">
                                <span class="step-num">06</span>
                                <span class="step-title">HOW IT WORKS &middot; THE 4-STEP WORKFLOW</span>
                            </div>
                            <div class="workflow-rail">
                                <div class="workflow-step">
                                    <div class="wf-circle">1</div>
                                    <div class="wf-body">
                                        <span class="wf-step-tag">INGESTION</span>
                                        <h5>Input or Upload Document</h5>
                                        <p>Paste draft text directly or upload PDF, DOCX, TXT, HTML, or Markdown files into the sandbox.</p>
                                    </div>
                                </div>
                                <div class="workflow-step">
                                    <div class="wf-circle">2</div>
                                    <div class="wf-body">
                                        <span class="wf-step-tag">SCANNING</span>
                                        <h5>Tri-Level Analysis</h5>
                                        <p>CHECKRA concurrently runs string hashes, near-neighbor matching, and semantic embeddings against open web indexes.</p>
                                    </div>
                                </div>
                                <div class="workflow-step">
                                    <div class="wf-circle">3</div>
                                    <div class="wf-body">
                                        <span class="wf-step-tag">VERIFICATION</span>
                                        <h5>Evidence Review &amp; Grammar</h5>
                                        <p>Inspect highlighted source cards, review AI context classifications, and inspect flagged grammar improvements.</p>
                                    </div>
                                </div>
                                <div class="workflow-step">
                                    <div class="wf-circle">4</div>
                                    <div class="wf-body">
                                        <span class="wf-step-tag">ELEVATION</span>
                                        <h5>Rewrite &amp; Export Report</h5>
                                        <p>Apply calibrated stylistic rewriting to problematic passages and export an evidence report with full citations.</p>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- 07. The Intelligence Approach (3-Level System) -->
                        <div class="deep-section">
                            <div class="section-label-bar">
                                <span class="step-num">07</span>
                                <span class="step-title">3-LEVEL EVIDENCE SYSTEM</span>
                            </div>
                            <div class="levels-container">
                                <div class="level-card">
                                    <div class="level-badge">LEVEL 01</div>
                                    <h4>Exact Matching</h4>
                                    <p>Identifies verbatim string sequences and direct copy-pasted blocks with zero alteration.</p>
                                    <div class="level-meta">Precision: Direct String Match</div>
                                </div>
                                <div class="level-card">
                                    <div class="level-badge">LEVEL 02</div>
                                    <h4>Near Matching</h4>
                                    <p>Detects lightly rearranged phrasing, synonym swaps, inverted sentence clauses, and mosaic modifications.</p>
                                    <div class="level-meta">Precision: Phrasal Permutation</div>
                                </div>
                                <div class="level-card">
                                    <div class="level-badge">LEVEL 03</div>
                                    <h4>Semantic Similarity</h4>
                                    <p>Analyzes deep semantic embeddings to detect whether different wording conveys substantially identical concept structure.</p>
                                    <div class="level-meta">Precision: Conceptual Embedding</div>
                                </div>
                            </div>
                        </div>

                        <!-- 08. Responsible Design & Honest Constraints -->
                        <div class="deep-section">
                            <div class="section-label-bar">
                                <span class="step-num">08</span>
                                <span class="step-title">RESPONSIBLE DESIGN &amp; HUMAN OVERSIGHT</span>
                            </div>
                            <div class="responsible-box">
                                <div class="resp-icon">
                                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                                </div>
                                <div class="resp-content">
                                    <h4>Evidence, Not Automated Accusations</h4>
                                    <p>
                                        CHECKRA is built on the strict principle that automated systems should provide transparent evidence, not definitive human judgments. Similarity percentages are indicator metrics &mdash; not proof of intellectual dishonesty. Human review by educators, editors, and authors remains the indispensable final step.
                                    </p>
                                </div>
                            </div>
                        </div>

                        <!-- 09. Vision & Taglines -->
                        <div class="deep-section">
                            <div class="section-label-bar">
                                <span class="step-num">09</span>
                                <span class="step-title">PRODUCT VISION &amp; IDENTITY</span>
                            </div>
                            <div class="vision-identity-box">
                                <div class="vi-taglines">
                                    <div class="vi-item">
                                        <span class="vi-lbl">PRIMARY TAGLINE</span>
                                        <h3>Your Intelligent Writing Integrity Space.</h3>
                                    </div>
                                    <div class="vi-item">
                                        <span class="vi-lbl">SECONDARY TAGLINE</span>
                                        <p>&ldquo;Don&rsquo;t just check the writing. Understand it, verify it, and improve it.&rdquo;</p>
                                    </div>
                                </div>
                                <div class="vi-statement">
                                    <h5>Five-Year Evolution</h5>
                                    <p>
                                        To become the universal intellectual provenance layer for digital documentation &mdash; bridging AI generation, human scholarship, and authentic creative expression.
                                    </p>
                                </div>
                            </div>
                        </div>

                        <!-- 10. Call to Action & Cross-Product Switcher -->
                        <div class="deep-section panel-footer-nav">
                            <div class="cta-banner cta-checkra">
                                <div>
                                    <h3>Ready to verify and elevate your writing?</h3>
                                    <p>Experience CHECKRA&rsquo;s unified similarity, grammar, and evidence-review suite today.</p>
                                </div>
                                <a href="https://checkra.onrender.com/" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg">
                                    <span>Launch CHECKRA Web App</span>
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                                </a>
                            </div>

                            <div class="cross-nav">
                                <span>Continue Exploring the NIVORA Universe:</span>
                                <div class="cross-links">
                                    <button class="cross-btn" onclick="switchProductTab('homora')">Next: HOMORA (Shared Finance OS) &rarr;</button>
                                    <button class="cross-btn" onclick="switchProductTab('bubora')">BUBORA &rarr;</button>
                                    <button class="cross-btn" onclick="switchProductTab('sayora')">SAYORA &rarr;</button>
                                </div>
                            </div>
                        </div>
                    </div>


                    <!-- ========================================== -->
                    <!-- 2. HOMORA PANEL                            -->
                    <!-- ========================================== -->
                    <div class="product-panel panel-homora" id="panel-homora" role="tabpanel" aria-labelledby="tab-homora">
                        <!-- 01. Hero & Positioning -->
                        <div class="panel-hero-card">
                            <div class="panel-hero-glow glow-homora"></div>
                            <div class="panel-hero-content">
                                <div class="panel-brand-header">
                                    <div class="panel-logo-box">
                                        <img src="assets/images/homora-logo.png" alt="HOMORA Logo" class="panel-logo">
                                    </div>
                                    <div class="panel-title-group">
                                        <div class="panel-meta-tags">
                                            <span class="tag-category">Smart Living &middot; Shared Finance &middot; Automation</span>
                                            <span class="tag-status live-status"><span class="dot"></span> Live Prototype</span>
                                        </div>
                                        <h2 class="panel-main-title">HOMORA</h2>
                                        <p class="panel-positioning">&ldquo;Household Financial Operating System&rdquo;</p>
                                    </div>
                                </div>
                                <p class="panel-lead">
                                    A comprehensive financial and domestic operating system built for flatmates, couples, families, and co-living communities &mdash; turning chaotic shared expenses and awkward money reminders into transparent, harmonious group operations.
                                </p>
                                <div class="panel-hero-ctas">
                                    <a href="https://homora-ai.vercel.app/" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
                                        <span>Visit HOMORA Prototype</span>
                                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                            <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                                            <polyline points="15 3 21 3 21 9"></polyline>
                                            <line x1="10" y1="14" x2="21" y2="3"></line>
                                        </svg>
                                    </a>
                                    <a href="#homora-model" class="btn btn-secondary">
                                        <span>4-Layer Financial Model</span>
                                    </a>
                                </div>
                            </div>
                        </div>

                        <!-- 02. About the Product -->
                        <div class="deep-section">
                            <div class="section-label-bar">
                                <span class="step-num">02</span>
                                <span class="step-title">ABOUT THE PLATFORM</span>
                            </div>
                            <div class="text-columns">
                                <div class="col-lead">
                                    <h3 class="deep-heading">Moving Beyond Basic Split Apps into Full Domestic Operations</h3>
                                    <p>
                                        Shared living creates friction not because people want to fight over money, but because traditional tools only track isolated transactions after the fact. Bill splitting apps fail to manage monthly contribution reserves, recurring utility cycles, shared grocery inventories, or fair emergency buffers.
                                    </p>
                                </div>
                                <div class="col-detail">
                                    <p>
                                        HOMORA introduces a complete domestic operating infrastructure: combining shared finance, real-time contribution pools, automated bill tracking, intelligent grocery planning, household chore assignments, and AI-driven spending optimization into one unified platform.
                                    </p>
                                </div>
                            </div>
                        </div>

                        <!-- 03. The Problem It Solves -->
                        <div class="deep-section">
                            <div class="section-label-bar">
                                <span class="step-num">03</span>
                                <span class="step-title">THE PROBLEM IT SOLVES</span>
                            </div>
                            <div class="problems-grid">
                                <div class="problem-item">
                                    <div class="prob-num">01</div>
                                    <h4>Awkward Financial Tension</h4>
                                    <p>Chasing flatmates for Wi-Fi bills, rent adjustments, or grocery splits damages personal relationships and breeds quiet resentment.</p>
                                </div>
                                <div class="problem-item">
                                    <div class="prob-num">02</div>
                                    <h4>No Collective Budget Visibility</h4>
                                    <p>Homes overspend on double-purchased household goods and surprise utility spikes because no unified monthly budget exists.</p>
                                </div>
                                <div class="problem-item">
                                    <div class="prob-num">03</div>
                                    <h4>Disconnected Domestic Tasks</h4>
                                    <p>Chores, groceries, repairs, and bills live in scattered WhatsApp chats and fridge notes, causing dropped balls and uneven responsibility.</p>
                                </div>
                            </div>
                        </div>

                        <!-- 04. Key Capabilities (14 Capabilities) -->
                        <div class="deep-section">
                            <div class="section-label-bar">
                                <span class="step-num">04</span>
                                <span class="step-title">14 CORE CAPABILITIES</span>
                            </div>
                            <div class="capabilities-grid capabilities-grid-4">
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg></div>
                                    <h4>Shared Finance &amp; Balances</h4>
                                    <p>Transparent real-time balances showing who owes what, who paid in advance, and exact net offsets.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg></div>
                                    <h4>Automated Budgeting</h4>
                                    <p>Target monthly caps for rent, utilities, groceries, and social expenses with automated pace alerts.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line></svg></div>
                                    <h4>Unified Expense Tracking</h4>
                                    <p>Categorized spending logs with receipt attachments, split ratios (equal, percentage, custom shares), and audit trails.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg></div>
                                    <h4>Fair Contribution Splits</h4>
                                    <p>Support for income-weighted, room-size weighted, or usage-calibrated contribution models.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 6v6l4 2"></path></svg></div>
                                    <h4>Community Emergency Pool</h4>
                                    <p>A communal reserve fund tracked inside the home for sudden plumbing repairs, deposits, or unexpected appliance replacements.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
                                    <h4>Claims &amp; Reimbursements</h4>
                                    <p>One-tap expense reimbursement requests with automatic approval rules and clear status timestamps.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg></div>
                                    <h4>Internal Micro-Loans</h4>
                                    <p>Transparent flatmate-to-flatmate internal ledger tracking to advance funds temporarily without awkward bookkeeping.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg></div>
                                    <h4>Smart Groceries Planning</h4>
                                    <p>Synchronized shared pantry lists, staple replenishment alerts, and duplicate purchase prevention.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg></div>
                                    <h4>Bills &amp; Subscriptions</h4>
                                    <p>Recurring calendar for electricity, Wi-Fi, maid services, streaming accounts, and maintenance charges.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 11l3 3L22 4"></path><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path></svg></div>
                                    <h4>Chores &amp; Household Tasks</h4>
                                    <p>Rotational cleaning schedules, trash duty assignments, and chore accountability check-ins.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg></div>
                                    <h4>Social Hub &amp; Memory Wall</h4>
                                    <p>A communal board for house announcements, guest visits, movie night polls, and shared memories.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg></div>
                                    <h4>Financial Insights</h4>
                                    <p>Visual monthly expense trends, waste identification, and historical inflation on utility spend.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg></div>
                                    <h4>Financial Health Score</h4>
                                    <p>An algorithmic hygiene rating reflecting on-time settlements, budget adherence, and reserve health.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg></div>
                                    <h4>HOMORA Intel</h4>
                                    <p>AI assistant analyzing patterns: &ldquo;Grocery expenses rose 18% due to brand substitutions &mdash; suggested alternatives found.&rdquo;</p>
                                </div>
                            </div>
                        </div>

                        <!-- 05. Core Idea / Philosophy -->
                        <div class="deep-section">
                            <div class="quote-callout callout-homora">
                                <div class="quote-tag">CORE PHILOSOPHY</div>
                                <blockquote>
                                    &ldquo;When shared finances are transparent, shared living becomes effortless.&rdquo;
                                </blockquote>
                                <p class="quote-subtext">
                                    Living together should be about mutual companionship and collective comfort &mdash; not ledger disputes, forgotten reimbursements, and tension at the end of the month.
                                </p>
                            </div>
                        </div>

                        <!-- 06. How It Works (Workflow Rail) -->
                        <div class="deep-section">
                            <div class="section-label-bar">
                                <span class="step-num">06</span>
                                <span class="step-title">HOW IT WORKS &middot; THE 4-STEP JOURNEY</span>
                            </div>
                            <div class="workflow-rail">
                                <div class="workflow-step">
                                    <div class="wf-circle">1</div>
                                    <div class="wf-body">
                                        <span class="wf-step-tag">SPACE CREATION</span>
                                        <h5>Form Your Household</h5>
                                        <p>Create a home workspace, invite flatmates or family members with role permissions, and set the currency.</p>
                                    </div>
                                </div>
                                <div class="workflow-step">
                                    <div class="wf-circle">2</div>
                                    <div class="wf-body">
                                        <span class="wf-step-tag">CONFIGURATION</span>
                                        <h5>Define Recurring Rules</h5>
                                        <p>Input fixed bills (rent, Wi-Fi, electricity), set split formulas, and establish the optional emergency pool.</p>
                                    </div>
                                </div>
                                <div class="workflow-step">
                                    <div class="wf-circle">3</div>
                                    <div class="wf-body">
                                        <span class="wf-step-tag">DAILY LIVING</span>
                                        <h5>Log &amp; Collaborate</h5>
                                        <p>Log shared expenses, tick off grocery runs, rotate chores, and watch balances update in real-time.</p>
                                    </div>
                                </div>
                                <div class="workflow-step">
                                    <div class="wf-circle">4</div>
                                    <div class="wf-body">
                                        <span class="wf-step-tag">HARMONY</span>
                                        <h5>Zero-Friction Settlement</h5>
                                        <p>Review monthly health analytics, settle peer balances with simplified debt netting, and keep the home harmonious.</p>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- 07. The 4-Layer Financial Model -->
                        <div class="deep-section" id="homora-model">
                            <div class="section-label-bar">
                                <span class="step-num">07</span>
                                <span class="step-title">4-LAYER FINANCIAL ARCHITECTURE</span>
                            </div>
                            <div class="levels-container levels-4">
                                <div class="level-card">
                                    <div class="level-badge">LAYER 01</div>
                                    <h4>Record</h4>
                                    <p>Comprehensive ledger ingestion: cash, digital transactions, receipts, and recurring utility schedules.</p>
                                </div>
                                <div class="level-card">
                                    <div class="level-badge">LAYER 02</div>
                                    <h4>Allocate</h4>
                                    <p>Dynamic split allocation algorithms handling unequal incomes, absent weeks, and custom member ratios.</p>
                                </div>
                                <div class="level-card">
                                    <div class="level-badge">LAYER 03</div>
                                    <h4>Harmonize</h4>
                                    <p>Debt simplification netting algorithms reducing 10 peer debts down to the minimal necessary transactions.</p>
                                </div>
                                <div class="level-card">
                                    <div class="level-badge">LAYER 04</div>
                                    <h4>Predict</h4>
                                    <p>HOMORA Intel forecast engine modeling seasonal energy bills and suggesting budget buffers.</p>
                                </div>
                            </div>
                        </div>

                        <!-- 08. Responsible Design & Legal Notice -->
                        <div class="deep-section">
                            <div class="section-label-bar">
                                <span class="step-num">08</span>
                                <span class="step-title">RESPONSIBLE DESIGN &amp; HONEST CONSTRAINTS</span>
                            </div>
                            <div class="responsible-box">
                                <div class="resp-icon">
                                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
                                </div>
                                <div class="resp-content">
                                    <h4>Important Regulatory &amp; Financial Clarification</h4>
                                    <p>
                                        <strong>HOMORA is a financial management software tool &mdash; not a bank, NBFC, payment processor, or depository institution.</strong> All internal loans, pools, and balances represent mathematical tracking ledgers maintained by housemates. HOMORA does not hold customer funds, provide credit underwriting, or guarantee debt recovery between individuals.
                                    </p>
                                </div>
                            </div>
                        </div>

                        <!-- 09. Vision & Taglines -->
                        <div class="deep-section">
                            <div class="section-label-bar">
                                <span class="step-num">09</span>
                                <span class="step-title">PRODUCT VISION &amp; IDENTITY</span>
                            </div>
                            <div class="vision-identity-box">
                                <div class="vi-taglines">
                                    <div class="vi-item">
                                        <span class="vi-lbl">PRIMARY TAGLINE</span>
                                        <h3>Household Financial Operating System.</h3>
                                    </div>
                                    <div class="vi-item">
                                        <span class="vi-lbl">SECONDARY TAGLINE</span>
                                        <p>&ldquo;Smart Living &middot; Shared Finance &middot; Effortless Harmony.&rdquo;</p>
                                    </div>
                                </div>
                                <div class="vi-statement">
                                    <h5>Five-Year Outlook</h5>
                                    <p>
                                        To evolve into the premier domestic OS powering modern urban co-living, multi-generational families, and independent households worldwide.
                                    </p>
                                </div>
                            </div>
                        </div>

                        <!-- 10. Call to Action & Cross-Product Switcher -->
                        <div class="deep-section panel-footer-nav">
                            <div class="cta-banner cta-homora">
                                <div>
                                    <h3>Bring financial clarity to your living space</h3>
                                    <p>Test the HOMORA interactive prototype and experience smart shared living.</p>
                                </div>
                                <a href="https://homora-ai.vercel.app/" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg">
                                    <span>Visit HOMORA Prototype</span>
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                                </a>
                            </div>

                            <div class="cross-nav">
                                <span>Continue Exploring the NIVORA Universe:</span>
                                <div class="cross-links">
                                    <button class="cross-btn" onclick="switchProductTab('bubora')">Next: BUBORA (Couples Space) &rarr;</button>
                                    <button class="cross-btn" onclick="switchProductTab('sayora')">SAYORA &rarr;</button>
                                    <button class="cross-btn" onclick="switchProductTab('checkra')">CHECKRA &rarr;</button>
                                </div>
                            </div>
                        </div>
                    </div>


                    <!-- ========================================== -->
                    <!-- 3. BUBORA PANEL                            -->
                    <!-- ========================================== -->
                    <div class="product-panel panel-bubora" id="panel-bubora" role="tabpanel" aria-labelledby="tab-bubora">
                        <!-- 01. Hero & Positioning -->
                        <div class="panel-hero-card">
                            <div class="panel-hero-glow glow-bubora"></div>
                            <div class="panel-hero-content">
                                <div class="panel-brand-header">
                                    <div class="panel-logo-box">
                                        <img src="assets/images/bubora-logo.png" alt="BUBORA Logo" class="panel-logo">
                                    </div>
                                    <div class="panel-title-group">
                                        <div class="panel-meta-tags">
                                            <span class="tag-category">Private Digital Space &middot; Couples &middot; Relationships</span>
                                            <span class="tag-status live-status"><span class="dot"></span> Live Application</span>
                                        </div>
                                        <h2 class="panel-main-title">BUBORA</h2>
                                        <p class="panel-positioning">&ldquo;A Private Digital Home for Two&rdquo;</p>
                                    </div>
                                </div>
                                <p class="panel-lead">
                                    An intimate, distraction-free sanctuary designed exclusively for two people. Free from public social feeds, intrusive algorithms, and advertising noise &mdash; BUBORA provides a dedicated haven to communicate, preserve memories, plan trips, and build a life together.
                                </p>
                                <div class="panel-hero-ctas">
                                    <a href="https://bubora.netlify.app/" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
                                        <span>Visit BUBORA Web App</span>
                                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                            <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                                            <polyline points="15 3 21 3 21 9"></polyline>
                                            <line x1="10" y1="14" x2="21" y2="3"></line>
                                        </svg>
                                    </a>
                                    <a href="#bubora-privacy" class="btn btn-secondary">
                                        <span>Privacy &amp; Encryption Model</span>
                                    </a>
                                </div>
                            </div>
                        </div>

                        <!-- 02. About the Product -->
                        <div class="deep-section">
                            <div class="section-label-bar">
                                <span class="step-num">02</span>
                                <span class="step-title">ABOUT THE PLATFORM</span>
                            </div>
                            <div class="text-columns">
                                <div class="col-lead">
                                    <h3 class="deep-heading">Digital Clutter vs. Relational Intimacy</h3>
                                    <p>
                                        Modern relationships are scattered across a dozen loud, ad-supported apps: WhatsApp for fast chats, Instagram for photos, Google Drive for travel tickets, Notes apps for grocery lists, and split sheets for shared dinners.
                                    </p>
                                </div>
                                <div class="col-detail">
                                    <p>
                                        BUBORA gathers all aspects of shared couple life into one private, beautifully crafted digital room. It is built strictly for two users &mdash; creating an authentic sanctuary where memories don&rsquo;t get buried in group chats and important plans are never lost.
                                    </p>
                                </div>
                            </div>
                        </div>

                        <!-- 03. The Problem It Solves -->
                        <div class="deep-section">
                            <div class="section-label-bar">
                                <span class="step-num">03</span>
                                <span class="step-title">THE PROBLEM IT SOLVES</span>
                            </div>
                            <div class="problems-grid">
                                <div class="problem-item">
                                    <div class="prob-num">01</div>
                                    <h4>Chat Overload &amp; Lost Memories</h4>
                                    <p>Precious milestone photos, romantic notes, and key anniversary memories vanish into infinite chat message histories.</p>
                                </div>
                                <div class="problem-item">
                                    <div class="prob-num">02</div>
                                    <h4>Intrusive Public Feeds</h4>
                                    <p>Mainstream social media platforms are optimized for addiction, vanity metrics, and data monetization &mdash; the exact opposite of healthy intimacy.</p>
                                </div>
                                <div class="problem-item">
                                    <div class="prob-num">03</div>
                                    <h4>Disorganized Future Planning</h4>
                                    <p>Vacation itineraries, bucket list dreams, and joint financial targets are stored across unlinked files, causing disorganization.</p>
                                </div>
                            </div>
                        </div>

                        <!-- 04. Key Capabilities (8 Core Capabilities) -->
                        <div class="deep-section">
                            <div class="section-label-bar">
                                <span class="step-num">04</span>
                                <span class="step-title">8 CORE CAPABILITIES</span>
                            </div>
                            <div class="capabilities-grid">
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg></div>
                                    <h4>Our Chat &amp; Intimate Messaging</h4>
                                    <p>Dedicated private messaging channel with pinned messages, voice notes, reaction stickers, and zero external alerts.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg></div>
                                    <h4>Memories &amp; Photo Timeline</h4>
                                    <p>An interactive chronological timeline capturing first dates, trips, holidays, and milestones in high fidelity.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg></div>
                                    <h4>Shared Calendar &amp; Countdowns</h4>
                                    <p>Synchronized calendar with live countdown timers for anniversaries, flights, reunions, and special evenings.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="3 11 22 2 13 21 11 13 3 11"></polygon></svg></div>
                                    <h4>Plans &amp; Trip Itineraries</h4>
                                    <p>Collaborative travel itineraries with hotel details, flight bookings, packing checklists, and must-see spot pins.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="m4.93 4.93 4.24 4.24"></path><path d="m14.83 9.17 4.24-4.24"></path><path d="m14.83 14.83 4.24 4.24"></path><path d="m9.17 14.83-4.24 4.24"></path></svg></div>
                                    <h4>Goals &amp; Joint Milestones</h4>
                                    <p>Long-term aspirations tracked visually: saving for an apartment, fitness challenges, books to read, or skills to learn together.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg></div>
                                    <h4>Couples Money &amp; Expenses</h4>
                                    <p>Simple joint expense tracking without awkward balance demands &mdash; keeping dining, gifts, and bills clear and harmonious.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg></div>
                                    <h4>Curated Date Ideas</h4>
                                    <p>Random date night generators, surprise activity prompts, and bucket list suggestions tailored for couple fun.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg></div>
                                    <h4>Private Vault</h4>
                                    <p>Secure client-side encrypted vault for sensitive documents, emergency contacts, door codes, and cherished private notes.</p>
                                </div>
                            </div>
                        </div>

                        <!-- 05. Core Idea / Philosophy -->
                        <div class="deep-section">
                            <div class="quote-callout callout-bubora">
                                <div class="quote-tag">CORE PHILOSOPHY</div>
                                <blockquote>
                                    &ldquo;Not every space needs a crowd. Some spaces are sacred for two.&rdquo;
                                </blockquote>
                                <p class="quote-subtext">
                                    In an era where personal lives are commodified by attention algorithms, BUBORA returns to the fundamental beauty of two people sharing moments, secrets, and future dreams in quiet privacy.
                                </p>
                            </div>
                        </div>

                        <!-- 06. How It Works (Workflow Rail) -->
                        <div class="deep-section">
                            <div class="section-label-bar">
                                <span class="step-num">06</span>
                                <span class="step-title">HOW IT WORKS &middot; INITIATION TO DAILY HARMONY</span>
                            </div>
                            <div class="workflow-rail">
                                <div class="workflow-step">
                                    <div class="wf-circle">1</div>
                                    <div class="wf-body">
                                        <span class="wf-step-tag">PAIRING</span>
                                        <h5>Create &amp; Pair Sanctuary</h5>
                                        <p>One partner generates a secure pairing code; the other scans or inputs it to lock the two-person room.</p>
                                    </div>
                                </div>
                                <div class="workflow-step">
                                    <div class="wf-circle">2</div>
                                    <div class="wf-body">
                                        <span class="wf-step-tag">TIMELINE</span>
                                        <h5>Establish Milestones</h5>
                                        <p>Set anniversary dates, upcoming trips, and upload inaugural photos to kickstart the shared memory stream.</p>
                                    </div>
                                </div>
                                <div class="workflow-step">
                                    <div class="wf-circle">3</div>
                                    <div class="wf-body">
                                        <span class="wf-step-tag">CONNECTION</span>
                                        <h5>Daily Interactions</h5>
                                        <p>Drop private messages, leave loving notes, sync schedules, and coordinate groceries or evening plans.</p>
                                    </div>
                                </div>
                                <div class="workflow-step">
                                    <div class="wf-circle">4</div>
                                    <div class="wf-body">
                                        <span class="wf-step-tag">ARCHIVE</span>
                                        <h5>Timeless Living Vault</h5>
                                        <p>Review annual retrospectives and search past moments in an immortal, private digital scrapbook.</p>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- 07. Privacy-First Architecture -->
                        <div class="deep-section" id="bubora-privacy">
                            <div class="section-label-bar">
                                <span class="step-num">07</span>
                                <span class="step-title">PRIVACY-FIRST ARCHITECTURE</span>
                            </div>
                            <div class="levels-container">
                                <div class="level-card">
                                    <div class="level-badge">PRINCIPLE 01</div>
                                    <h4>Zero Surveillance &amp; Ads</h4>
                                    <p>BUBORA contains zero advertising trackers, zero social pixel beacons, and zero data-brokering agreements.</p>
                                </div>
                                <div class="level-card">
                                    <div class="level-badge">PRINCIPLE 02</div>
                                    <h4>Two-Party Enclave</h4>
                                    <p>Access is architecturally restricted to precisely two verified accounts per space &mdash; third-party viewing is impossible.</p>
                                </div>
                                <div class="level-card">
                                    <div class="level-badge">PRINCIPLE 03</div>
                                    <h4>Client-Side Vault Logic</h4>
                                    <p>Sensitive vault entries utilize client-side encryption keys, ensuring intimate details remain strictly between partners.</p>
                                </div>
                            </div>
                        </div>

                        <!-- 08. Responsible Design & Honest Constraints -->
                        <div class="deep-section">
                            <div class="section-label-bar">
                                <span class="step-num">08</span>
                                <span class="step-title">RESPONSIBLE DESIGN ETHICS</span>
                            </div>
                            <div class="responsible-box">
                                <div class="resp-icon">
                                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                                </div>
                                <div class="resp-content">
                                    <h4>No Dopamine Hacks &middot; Respect for Real Life</h4>
                                    <p>
                                        BUBORA deliberately omits infinite scroll feeds, public follower counts, algorithmic rage bait, and engagement-maximizing notifications. The application is designed to support healthy offline romance &mdash; not replace it with screen addiction.
                                    </p>
                                </div>
                            </div>
                        </div>

                        <!-- 09. Vision & Taglines -->
                        <div class="deep-section">
                            <div class="section-label-bar">
                                <span class="step-num">09</span>
                                <span class="step-title">PRODUCT VISION &amp; IDENTITY</span>
                            </div>
                            <div class="vision-identity-box">
                                <div class="vi-taglines">
                                    <div class="vi-item">
                                        <span class="vi-lbl">PRIMARY TAGLINE</span>
                                        <h3>A Private Digital Home for Two.</h3>
                                    </div>
                                    <div class="vi-item">
                                        <span class="vi-lbl">SECONDARY TAGLINE</span>
                                        <p>&ldquo;Not every space needs a crowd. Some spaces are sacred for two.&rdquo;</p>
                                    </div>
                                </div>
                                <div class="vi-statement">
                                    <h5>Five-Year Outlook</h5>
                                    <p>
                                        To establish the global gold standard for intimate digital spaces, protecting couple memories across generations with unyielding privacy.
                                    </p>
                                </div>
                            </div>
                        </div>

                        <!-- 10. Call to Action & Cross-Product Switcher -->
                        <div class="deep-section panel-footer-nav">
                            <div class="cta-banner cta-bubora">
                                <div>
                                    <h3>Build your private couple sanctuary</h3>
                                    <p>Create a space exclusively for you and your partner today.</p>
                                </div>
                                <a href="https://bubora.netlify.app/" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg">
                                    <span>Visit BUBORA Web App</span>
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                                </a>
                            </div>

                            <div class="cross-nav">
                                <span>Continue Exploring the NIVORA Universe:</span>
                                <div class="cross-links">
                                    <button class="cross-btn" onclick="switchProductTab('sayora')">Next: SAYORA (Gig Worker Fund) &rarr;</button>
                                    <button class="cross-btn" onclick="switchProductTab('checkra')">CHECKRA &rarr;</button>
                                    <button class="cross-btn" onclick="switchProductTab('homora')">HOMORA &rarr;</button>
                                </div>
                            </div>
                        </div>
                    </div>


                    <!-- ========================================== -->
                    <!-- 4. SAYORA PANEL                            -->
                    <!-- ========================================== -->
                    <div class="product-panel panel-sayora" id="panel-sayora" role="tabpanel" aria-labelledby="tab-sayora">
                        <!-- 01. Hero & Positioning -->
                        <div class="panel-hero-card">
                            <div class="panel-hero-glow glow-sayora"></div>
                            <div class="panel-hero-content">
                                <div class="panel-brand-header">
                                    <div class="panel-logo-box">
                                        <img src="assets/images/sayora-logo.png" alt="SAYORA Logo" class="panel-logo">
                                    </div>
                                    <div class="panel-title-group">
                                        <div class="panel-meta-tags">
                                            <span class="tag-category">Financial Resilience &middot; Gig Economy &middot; Social Impact</span>
                                            <span class="tag-status status-badge-concept"><span class="dot-concept"></span> Concept &middot; In Development</span>
                                        </div>
                                        <h2 class="panel-main-title">SAYORA</h2>
                                        <p class="panel-positioning">&ldquo;Together for a Safer Tomorrow &middot; Small Steps. Stronger Communities.&rdquo;</p>
                                    </div>
                                </div>
                                <p class="panel-lead">
                                    A community-backed financial safety net and emergency resilience concept engineered for platform delivery executives, drivers, and informal gig workers &mdash; providing transparent micro-savings, peer assistance pools, crisis relief, and welfare scheme discovery.
                                </p>
                                <div class="panel-hero-ctas">
                                    <a href="#sayora-model" class="btn btn-primary">
                                        <span>Explore 4-Level Resilience Model</span>
                                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                            <line x1="5" y1="12" x2="19" y2="12"></line>
                                            <polyline points="12 5 19 12 12 19"></polyline>
                                        </svg>
                                    </a>
                                    <a href="#sayora-disclaimer" class="btn btn-secondary">
                                        <span>R&amp;D Architecture &amp; Ethics</span>
                                    </a>
                                </div>
                            </div>
                        </div>

                        <!-- 02. About the Product -->
                        <div class="deep-section">
                            <div class="section-label-bar">
                                <span class="step-num">02</span>
                                <span class="step-title">ABOUT THE CONCEPT</span>
                            </div>
                            <div class="text-columns">
                                <div class="col-lead">
                                    <h3 class="deep-heading">Bridging the Social Safety Deficit in the On-Demand Economy</h3>
                                    <p>
                                        Millions of gig workers keep our cities moving &mdash; delivering food, driving passengers, and fulfilling logistics. Yet they navigate volatile daily incomes without paid sick leave, accidental downtime cushions, health buffers, or structured emergency safety nets.
                                    </p>
                                </div>
                                <div class="col-detail">
                                    <p>
                                        SAYORA is conceptualized as an empathetic, technology-driven resilience architecture. By blending micro-savings, community mutual aid pools, institutional CSR matching, and localized disaster relief into a single dignified portal, SAYORA aims to protect gig workers from predatory debt spirals.
                                    </p>
                                </div>
                            </div>
                        </div>

                        <!-- 03. The Problem It Solves -->
                        <div class="deep-section">
                            <div class="section-label-bar">
                                <span class="step-num">03</span>
                                <span class="step-title">THE PROBLEM IT SOLVES</span>
                            </div>
                            <div class="problems-grid">
                                <div class="problem-item">
                                    <div class="prob-num">01</div>
                                    <h4>Income Volatility &amp; Shocks</h4>
                                    <p>A single road accident, vehicle breakdown, or severe monsoon spell can wipe out weeks of earnings and force workers into high-interest informal loans.</p>
                                </div>
                                <div class="problem-item">
                                    <div class="prob-num">02</div>
                                    <h4>Institutional Invisibility</h4>
                                    <p>Traditional banks and insurers overlook informal workers due to lacking formal payslips, fixed contracts, or conventional credit scores.</p>
                                </div>
                                <div class="problem-item">
                                    <div class="prob-num">03</div>
                                    <h4>Underutilized Welfare Schemes</h4>
                                    <p>Government subsidies, accident funds, and worker welfare boards exist but go untapped due to bureaucratic literacy barriers and complex paperwork.</p>
                                </div>
                            </div>
                        </div>

                        <!-- 04. Key Capabilities (13 Capabilities) -->
                        <div class="deep-section">
                            <div class="section-label-bar">
                                <span class="step-num">04</span>
                                <span class="step-title">13 CORE CONCEPT CAPABILITIES</span>
                            </div>
                            <div class="capabilities-grid capabilities-grid-4">
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg></div>
                                    <h4>Smart Micro-Savings</h4>
                                    <p>Frictionless round-up savings from daily trip earnings into a protected personal emergency reserve.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>
                                    <h4>Peer Protection Pool</h4>
                                    <p>Decentralized mutual aid fund where tiny voluntary contributions unlock communal emergency assistance.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg></div>
                                    <h4>Community Support Network</h4>
                                    <p>Peer verifiers and fellow workers vouching for incident authenticity and offering roadside solidarity.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg></div>
                                    <h4>Emergency Assistance</h4>
                                    <p>Rapid micro-disbursements for urgent hospital out-of-pocket costs, tire repairs, or immediate medical medicines.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"></path></svg></div>
                                    <h4>Climate &amp; Crisis Relief</h4>
                                    <p>Parametric relief alerts triggered during severe heatwaves, floods, hazardous air quality, or curfews.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg></div>
                                    <h4>Corporate CSR Matching</h4>
                                    <p>Integration channel for enterprise logistics platforms and philanthropic foundations to match worker contributions 1:1.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></div>
                                    <h4>Welfare Scheme Discovery</h4>
                                    <p>Automated matching engine pairing workers with official government social security boards (e.g. e-Shram, PM-JAY).</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg></div>
                                    <h4>Financial Literacy Guides</h4>
                                    <p>Bite-sized vernacular audio and visual guides on debt avoidance, compound interest, tax basics, and budget management.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"></rect><line x1="1" y1="10" x2="23" y2="10"></line></svg></div>
                                    <h4>Essential Money Services</h4>
                                    <p>Affordable low-cost micro-transfers, emergency bill buffering, and zero-penalty credit builder partnerships.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="16" rx="2"></rect><circle cx="9" cy="10" r="2"></circle><line x1="15" y1="8" x2="17" y2="8"></line><line x1="15" y1="12" x2="17" y2="12"></line><line x1="7" y1="16" x2="17" y2="16"></line></svg></div>
                                    <h4>Digital SAYORA ID</h4>
                                    <p>A portable digital identity consolidating work tenure, reliability scores, and safety contributions across gig platforms.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg></div>
                                    <h4>Transparent Impact Analytics</h4>
                                    <p>Publicly auditable blockchain or open-ledger verification showing exactly where every dollar of mutual aid was disbursed.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg></div>
                                    <h4>Ask SAYORA Assistant</h4>
                                    <p>Multilingual voice-first AI assistant answering queries on claims, policy benefits, and emergency nearby hospital clinics.</p>
                                </div>
                                <div class="cap-card">
                                    <div class="cap-icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg></div>
                                    <h4>Security &amp; Data Trust</h4>
                                    <p>Zero sharing of worker data with platform employers, preventing retaliatory deactivations and preserving privacy.</p>
                                </div>
                            </div>
                        </div>

                        <!-- 05. Core Idea / Philosophy -->
                        <div class="deep-section">
                            <div class="quote-callout callout-sayora">
                                <div class="quote-tag">CORE PHILOSOPHY</div>
                                <blockquote>
                                    &ldquo;Those who support our cities deserve a system that supports them.&rdquo;
                                </blockquote>
                                <p class="quote-subtext">
                                    Economic dignity cannot depend on whether a worker has an executive employment contract. Flexible work demands flexible, empathetic, and resilient safety systems.
                                </p>
                            </div>
                        </div>

                        <!-- 06. How It Works (Workflow Rail) -->
                        <div class="deep-section">
                            <div class="section-label-bar">
                                <span class="step-num">06</span>
                                <span class="step-title">HOW IT WORKS &middot; MEMBER &amp; COMMUNITY LIFECYCLE</span>
                            </div>
                            <div class="workflow-rail">
                                <div class="workflow-step">
                                    <div class="wf-circle">1</div>
                                    <div class="wf-body">
                                        <span class="wf-step-tag">ONBOARDING</span>
                                        <h5>Generate SAYORA ID</h5>
                                        <p>Gig worker creates a verified mobile profile, connects preferred micro-saving rules, and joins local city cluster.</p>
                                    </div>
                                </div>
                                <div class="workflow-step">
                                    <div class="wf-circle">2</div>
                                    <div class="wf-body">
                                        <span class="wf-step-tag">ACCUMULATION</span>
                                        <h5>Micro-Stash &amp; CSR Match</h5>
                                        <p>Small daily savings build a personal cushion, automatically augmented by participating CSR foundation pools.</p>
                                    </div>
                                </div>
                                <div class="workflow-step">
                                    <div class="wf-circle">3</div>
                                    <div class="wf-body">
                                        <span class="wf-step-tag">CRISIS RESPONSE</span>
                                        <h5>Instant Verified Claim</h5>
                                        <p>In case of sickness, road accident, or severe weather, member submits a simple photo/audio claim verified by peers.</p>
                                    </div>
                                </div>
                                <div class="workflow-step">
                                    <div class="wf-circle">4</div>
                                    <div class="wf-body">
                                        <span class="wf-step-tag">RESTITUTION</span>
                                        <h5>Immediate Relief Payout</h5>
                                        <p>Emergency assistance disburses within hours directly to the worker's wallet, keeping family finances intact.</p>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- 07. The 4-Level Resilience Model -->
                        <div class="deep-section" id="sayora-model">
                            <div class="section-label-bar">
                                <span class="step-num">07</span>
                                <span class="step-title">4-LEVEL RESILIENCE MODEL</span>
                            </div>
                            <div class="levels-container levels-4">
                                <div class="level-card">
                                    <div class="level-badge">LEVEL 01</div>
                                    <h4>Save</h4>
                                    <p>Individual micro-stashing to build a first-response cushion for personal day-to-day emergencies.</p>
                                </div>
                                <div class="level-card">
                                    <div class="level-badge">LEVEL 02</div>
                                    <h4>Protect</h4>
                                    <p>Community mutual pool that absorbs medium financial shocks through collective risk pooling.</p>
                                </div>
                                <div class="level-card">
                                    <div class="level-badge">LEVEL 03</div>
                                    <h4>Recover</h4>
                                    <p>CSR matching grants and extreme weather parametric payouts for catastrophic life disruptions.</p>
                                </div>
                                <div class="level-card">
                                    <div class="level-badge">LEVEL 04</div>
                                    <h4>Advance</h4>
                                    <p>Welfare scheme discovery, financial literacy, and portable credentialing to enable upward economic mobility.</p>
                                </div>
                            </div>
                        </div>

                        <!-- 08. Responsible Design & Honest Constraints -->
                        <div class="deep-section" id="sayora-disclaimer">
                            <div class="section-label-bar">
                                <span class="step-num">08</span>
                                <span class="step-title">RESPONSIBLE DESIGN &amp; HONEST CONSTRAINTS</span>
                            </div>
                            <div class="responsible-box">
                                <div class="resp-icon">
                                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                                </div>
                                <div class="resp-content">
                                    <h4>Concept Status &middot; Transparent Legal Notice</h4>
                                    <p>
                                        <strong>SAYORA is an architectural concept and R&amp;D initiative within the NIVORA innovation ecosystem.</strong> It is not currently a licensed insurance company, bank, credit union, or registered financial service provider. Full implementation of financial disbursements will be operated in direct partnership with regulated banking institutions, authorized insurance underwriters, and registered non-profit welfare trusts.
                                    </p>
                                </div>
                            </div>
                        </div>

                        <!-- 09. Vision & Taglines -->
                        <div class="deep-section">
                            <div class="section-label-bar">
                                <span class="step-num">09</span>
                                <span class="step-title">PRODUCT VISION &amp; IDENTITY</span>
                            </div>
                            <div class="vision-identity-box">
                                <div class="vi-taglines">
                                    <div class="vi-item">
                                        <span class="vi-lbl">PRIMARY TAGLINE</span>
                                        <h3>Together for a Safer Tomorrow.</h3>
                                    </div>
                                    <div class="vi-item">
                                        <span class="vi-lbl">SECONDARY TAGLINE</span>
                                        <p>&ldquo;Small Steps. Stronger Communities.&rdquo;</p>
                                    </div>
                                </div>
                                <div class="vi-statement">
                                    <h5>Five-Year Outlook</h5>
                                    <p>
                                        To architect a universally accessible safety protocol that can be embedded into gig economy platforms across emerging markets, protecting over 100,000 workers with dignity.
                                    </p>
                                </div>
                            </div>
                        </div>

                        <!-- 10. Call to Action & Cross-Product Switcher -->
                        <div class="deep-section panel-footer-nav">
                            <div class="cta-banner cta-sayora">
                                <div>
                                    <h3>Partner with us to build SAYORA</h3>
                                    <p>We are seeking social impact researchers, CSR partners, and gig worker collectives to bring this vision to life.</p>
                                </div>
                                <a href="#contact" class="btn btn-primary btn-lg">
                                    <span>Get in Touch with NIVORA</span>
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                                </a>
                            </div>

                            <div class="cross-nav">
                                <span>Continue Exploring the NIVORA Universe:</span>
                                <div class="cross-links">
                                    <button class="cross-btn" onclick="switchProductTab('checkra')">Back to: CHECKRA &rarr;</button>
                                    <button class="cross-btn" onclick="switchProductTab('homora')">HOMORA &rarr;</button>
                                    <button class="cross-btn" onclick="switchProductTab('bubora')">BUBORA &rarr;</button>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </section>
"""
