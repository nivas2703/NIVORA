# builder/nav_hero_cards.py

NAV_HERO_CARDS_HTML = """
    <!-- Top Navigation -->
    <header class="nivora-nav" id="main-nav">
        <div class="nav-container">
            <a href="#hero" class="brand-link" aria-label="NIVORA Home">
                <img src="assets/images/nivora-logo.png" alt="NIVORA Logo" class="brand-mark">
                <span class="brand-text">NIVORA</span>
            </a>

            <nav class="desktop-menu" aria-label="Main Navigation">
                <a href="#hero" class="nav-item">Home</a>
                
                <!-- Products with Dropdown -->
                <div class="nav-dropdown-wrapper">
                    <a href="#products" class="nav-item dropdown-toggle">
                        Products
                        <svg class="dropdown-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="6 9 12 15 18 9"></polyline>
                        </svg>
                    </a>
                    <div class="nav-dropdown-menu">
                        <a href="#checkra" class="dropdown-item" onclick="switchProductTab('checkra')">
                            <span class="dropdown-dot dot-checkra"></span>
                            <div class="dropdown-info">
                                <span class="dropdown-title">CHECKRA</span>
                                <span class="dropdown-desc">Writing Integrity & Plagiarism Intelligence</span>
                            </div>
                        </a>
                        <a href="#homora" class="dropdown-item" onclick="switchProductTab('homora')">
                            <span class="dropdown-dot dot-homora"></span>
                            <div class="dropdown-info">
                                <span class="dropdown-title">HOMORA</span>
                                <span class="dropdown-desc">Smart Living & Shared Finance OS</span>
                            </div>
                        </a>
                        <a href="#bubora" class="dropdown-item" onclick="switchProductTab('bubora')">
                            <span class="dropdown-dot dot-bubora"></span>
                            <div class="dropdown-info">
                                <span class="dropdown-title">BUBORA</span>
                                <span class="dropdown-desc">Private Digital Home for Two</span>
                            </div>
                        </a>
                        <a href="#sayora" class="dropdown-item" onclick="switchProductTab('sayora')">
                            <span class="dropdown-dot dot-sayora"></span>
                            <div class="dropdown-info">
                                <span class="dropdown-title">SAYORA</span>
                                <span class="dropdown-desc">Gig Worker Financial Resilience Fund</span>
                            </div>
                        </a>
                        <div class="dropdown-divider"></div>
                        <a href="#explore" class="dropdown-item dropdown-footer-link">
                            Explore All Deep Dives &rarr;
                        </a>
                    </div>
                </div>

                <a href="#about" class="nav-item">About</a>
                <a href="#portfolio" class="nav-item">Founder</a>
                <a href="#folivio" class="nav-item">FOLIVIO</a>
                <a href="#vision" class="nav-item">Vision</a>
                <a href="#contact" class="nav-item">Contact</a>
            </nav>

            <div class="nav-actions">
                <a href="#explore" class="btn btn-primary nav-cta">
                    <span>Explore Products</span>
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <line x1="5" y1="12" x2="19" y2="12"></line>
                        <polyline points="12 5 19 12 12 19"></polyline>
                    </svg>
                </a>
                <button class="mobile-toggle" id="mobile-toggle" aria-label="Toggle navigation menu">
                    <span class="toggle-bar"></span>
                    <span class="toggle-bar"></span>
                    <span class="toggle-bar"></span>
                </button>
            </div>
        </div>

        <!-- Mobile Drawer -->
        <div class="mobile-drawer" id="mobile-drawer">
            <div class="mobile-drawer-inner">
                <a href="#hero" class="mobile-nav-item">Home</a>
                <a href="#products" class="mobile-nav-item">Product Universe</a>
                <div class="mobile-sublinks">
                    <a href="#checkra" class="mobile-sublink" onclick="switchProductTab('checkra')">&bull; CHECKRA</a>
                    <a href="#homora" class="mobile-sublink" onclick="switchProductTab('homora')">&bull; HOMORA</a>
                    <a href="#bubora" class="mobile-sublink" onclick="switchProductTab('bubora')">&bull; BUBORA</a>
                    <a href="#sayora" class="mobile-sublink" onclick="switchProductTab('sayora')">&bull; SAYORA</a>
                </div>
                <a href="#about" class="mobile-nav-item">About NIVORA</a>
                <a href="#portfolio" class="mobile-nav-item">Founder</a>
                <a href="#folivio" class="mobile-nav-item">FOLIVIO</a>
                <a href="#vision" class="mobile-nav-item">Ecosystem Vision</a>
                <a href="#contact" class="mobile-nav-item">Contact</a>
                <div class="mobile-cta-box">
                    <a href="#explore" class="btn btn-primary btn-block">Explore Product Worlds</a>
                </div>
            </div>
        </div>
    </header>

    <!-- Main Content Container -->
    <main id="content">

        <!-- Hero Section -->
        <section class="hero-section" id="hero">
            <div class="hero-ambient-glow"></div>
            <div class="hero-ambient-glow-2"></div>
            <div class="container hero-container">
                <div class="hero-badge reveal-fade">
                    <span class="pulse-indicator"></span>
                    <span class="badge-text">INNOVATION &middot; TECHNOLOGY &middot; PURPOSE</span>
                </div>

                <h1 class="hero-title reveal-fade">
                    Welcome to <span class="gradient-text glow-hero">NIVORA.</span>
                </h1>

                <p class="hero-tagline reveal-fade">
                    Turning Ideas Into Intelligent Products.
                </p>

                <p class="hero-description reveal-fade">
                    NIVORA is the technology and innovation universe built by <strong>Nivas Bennabatthula</strong> &mdash; where ambitious ideas become intelligent products, meaningful experiences and new digital possibilities.
                </p>

                <div class="hero-buttons reveal-fade">
                    <a href="#explore" class="btn btn-primary btn-lg">
                        <span>Explore Products</span>
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="5" y1="12" x2="19" y2="12"></line>
                            <polyline points="12 5 19 12 12 19"></polyline>
                        </svg>
                    </a>
                    <a href="#portfolio" class="btn btn-secondary btn-lg">
                        <span>Meet the Founder</span>
                    </a>
                </div>

                <!-- Floating Product Identities Visual Orbit -->
                <div class="hero-orbital-visual reveal-scale">
                    <div class="orbit-center">
                        <div class="orbit-core-glow"></div>
                        <img src="assets/images/nivora-logo.png" alt="NIVORA Core" class="orbit-core-logo">
                        <span class="orbit-core-label">NIVORA ECOSYSTEM</span>
                    </div>

                    <div class="orbit-satellites">
                        <a href="#checkra" class="satellite-pill sat-checkra" onclick="switchProductTab('checkra')">
                            <img src="assets/images/checkra-logo.png" alt="CHECKRA" class="sat-logo">
                            <div class="sat-text">
                                <span class="sat-name">CHECKRA</span>
                                <span class="sat-role">Writing Integrity</span>
                            </div>
                        </a>
                        <a href="#homora" class="satellite-pill sat-homora" onclick="switchProductTab('homora')">
                            <img src="assets/images/homora-logo.png" alt="HOMORA" class="sat-logo">
                            <div class="sat-text">
                                <span class="sat-name">HOMORA</span>
                                <span class="sat-role">Shared Finance OS</span>
                            </div>
                        </a>
                        <a href="#bubora" class="satellite-pill sat-bubora" onclick="switchProductTab('bubora')">
                            <img src="assets/images/bubora-logo.png" alt="BUBORA" class="sat-logo">
                            <div class="sat-text">
                                <span class="sat-name">BUBORA</span>
                                <span class="sat-role">Digital Home for Two</span>
                            </div>
                        </a>
                        <a href="#sayora" class="satellite-pill sat-sayora" onclick="switchProductTab('sayora')">
                            <img src="assets/images/sayora-logo.png" alt="SAYORA" class="sat-logo">
                            <div class="sat-text">
                                <span class="sat-name">SAYORA</span>
                                <span class="sat-role">Financial Resilience</span>
                            </div>
                        </a>
                    </div>
                </div>

                <div class="hero-scroll-indicator">
                    <a href="#products" aria-label="Scroll to Products">
                        <span class="scroll-mouse">
                            <span class="scroll-wheel"></span>
                        </span>
                        <span class="scroll-text">Explore the Universe</span>
                    </a>
                </div>
            </div>
        </section>

        <!-- Product Universe Section (Overview Grid) -->
        <section class="section products-section" id="products">
            <div class="container">
                <div class="section-header text-center reveal-fade">
                    <span class="section-badge">THE PRODUCT WORLDS</span>
                    <h2 class="section-title">Engineered with Purpose. Driven by Intelligence.</h2>
                    <p class="section-subtitle">
                        Inside NIVORA, every product is a distinct world tackling a core human and technological challenge &mdash; from academic truth and collective living to shared intimacy and gig-worker resilience.
                    </p>
                </div>

                <div class="products-grid">
                    <!-- CHECKRA Card -->
                    <div class="product-card card-checkra reveal-fade" data-tilt>
                        <div class="card-ambient-glow"></div>
                        <div class="card-header">
                            <div class="product-logo-wrapper">
                                <img src="assets/images/checkra-logo.png" alt="CHECKRA Logo" class="product-logo">
                            </div>
                            <div class="product-status-badge status-live">
                                <span class="status-dot"></span> Live Application
                            </div>
                        </div>
                        <div class="card-body">
                            <span class="product-category">Writing Integrity &middot; AI &middot; Document Intelligence</span>
                            <h3 class="product-name">CHECKRA</h3>
                            <p class="product-positioning">&ldquo;Your Intelligent Writing Integrity Space&rdquo;</p>
                            <p class="product-description">
                                An intelligent writing integrity and source verification platform combining multi-level similarity detection, web source evidence review, comprehensive grammar correction, and responsible AI rewriting into a unified workspace.
                            </p>
                            <div class="product-features-pills">
                                <span class="feat-pill">Multi-Level Similarity</span>
                                <span class="feat-pill">Source Evidence</span>
                                <span class="feat-pill">Grammar &amp; Rewrite</span>
                                <span class="feat-pill">Structured Reports</span>
                            </div>
                        </div>
                        <div class="card-footer">
                            <a href="#checkra" class="btn btn-card-primary" onclick="switchProductTab('checkra')">
                                <span>Explore Product &rarr;</span>
                            </a>
                            <a href="https://checkra.onrender.com/" target="_blank" rel="noopener noreferrer" class="btn btn-card-outline" title="Open CHECKRA Live Web App">
                                <span>Visit App</span>
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                                    <polyline points="15 3 21 3 21 9"></polyline>
                                    <line x1="10" y1="14" x2="21" y2="3"></line>
                                </svg>
                            </a>
                        </div>
                    </div>

                    <!-- HOMORA Card -->
                    <div class="product-card card-homora reveal-fade" data-tilt>
                        <div class="card-ambient-glow"></div>
                        <div class="card-header">
                            <div class="product-logo-wrapper">
                                <img src="assets/images/homora-logo.png" alt="HOMORA Logo" class="product-logo">
                            </div>
                            <div class="product-status-badge status-live">
                                <span class="status-dot"></span> Live Prototype
                            </div>
                        </div>
                        <div class="card-body">
                            <span class="product-category">Smart Living &middot; Shared Finance &middot; Automation</span>
                            <h3 class="product-name">HOMORA</h3>
                            <p class="product-positioning">&ldquo;Household Financial Operating System&rdquo;</p>
                            <p class="product-description">
                                A comprehensive financial operating system for shared living. Replaces messy chat threads and awkward money conversations with transparent expense tracking, automated shared budgeting, grocery planning, chore coordination, and internal liquidity pools.
                            </p>
                            <div class="product-features-pills">
                                <span class="feat-pill">Shared Balances</span>
                                <span class="feat-pill">Internal Pools</span>
                                <span class="feat-pill">Smart Groceries</span>
                                <span class="feat-pill">HOMORA Intel</span>
                            </div>
                        </div>
                        <div class="card-footer">
                            <a href="#homora" class="btn btn-card-primary" onclick="switchProductTab('homora')">
                                <span>Explore Product &rarr;</span>
                            </a>
                            <a href="https://homora-ai.vercel.app/" target="_blank" rel="noopener noreferrer" class="btn btn-card-outline" title="Open HOMORA Live Web App">
                                <span>Visit App</span>
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                                    <polyline points="15 3 21 3 21 9"></polyline>
                                    <line x1="10" y1="14" x2="21" y2="3"></line>
                                </svg>
                            </a>
                        </div>
                    </div>

                    <!-- BUBORA Card -->
                    <div class="product-card card-bubora reveal-fade" data-tilt>
                        <div class="card-ambient-glow"></div>
                        <div class="card-header">
                            <div class="product-logo-wrapper">
                                <img src="assets/images/bubora-logo.png" alt="BUBORA Logo" class="product-logo">
                            </div>
                            <div class="product-status-badge status-live">
                                <span class="status-dot"></span> Live Application
                            </div>
                        </div>
                        <div class="card-body">
                            <span class="product-category">Private Digital Space &middot; Couples &middot; Relationships</span>
                            <h3 class="product-name">BUBORA</h3>
                            <p class="product-positioning">&ldquo;A Private Digital Home for Two&rdquo;</p>
                            <p class="product-description">
                                An intimate, distraction-free digital space created exclusively for couples. Replaces public social media noise and fragmented apps with dedicated encrypted messaging, shared memory timeline, countdowns, trip planning, joint goals, and private vaults.
                            </p>
                            <div class="product-features-pills">
                                <span class="feat-pill">Encrypted Chat</span>
                                <span class="feat-pill">Memory Timeline</span>
                                <span class="feat-pill">Trip Planning</span>
                                <span class="feat-pill">Private Vault</span>
                            </div>
                        </div>
                        <div class="card-footer">
                            <a href="#bubora" class="btn btn-card-primary" onclick="switchProductTab('bubora')">
                                <span>Explore Product &rarr;</span>
                            </a>
                            <a href="https://bubora.netlify.app/" target="_blank" rel="noopener noreferrer" class="btn btn-card-outline" title="Open BUBORA Live Web App">
                                <span>Visit App</span>
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                                    <polyline points="15 3 21 3 21 9"></polyline>
                                    <line x1="10" y1="14" x2="21" y2="3"></line>
                                </svg>
                            </a>
                        </div>
                    </div>

                    <!-- SAYORA Card -->
                    <div class="product-card card-sayora reveal-fade" data-tilt>
                        <div class="card-ambient-glow"></div>
                        <div class="card-header">
                            <div class="product-logo-wrapper">
                                <img src="assets/images/sayora-logo.png" alt="SAYORA Logo" class="product-logo">
                            </div>
                            <div class="product-status-badge status-concept">
                                <span class="status-dot-concept"></span> Concept &middot; In Development
                            </div>
                        </div>
                        <div class="card-body">
                            <span class="product-category">Financial Resilience &middot; Gig Economy &middot; Social Impact</span>
                            <h3 class="product-name">SAYORA</h3>
                            <p class="product-positioning">&ldquo;Together for a Safer Tomorrow&rdquo;</p>
                            <p class="product-description">
                                A community-backed financial safety net and emergency resilience concept engineered for platform and gig workers. Combines micro-savings, peer assistance pools, crisis relief, scheme discovery, and transparent impact analytics into a dignified safety architecture.
                            </p>
                            <div class="product-features-pills">
                                <span class="feat-pill">Micro-Savings</span>
                                <span class="feat-pill">Emergency Pool</span>
                                <span class="feat-pill">Welfare Discovery</span>
                                <span class="feat-pill">Digital SAYORA ID</span>
                            </div>
                        </div>
                        <div class="card-footer">
                            <a href="#sayora" class="btn btn-card-primary" onclick="switchProductTab('sayora')">
                                <span>Explore Concept &rarr;</span>
                            </a>
                            <span class="badge-in-dev">R&amp;D Architecture</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""
