import re
import sys

filepath = "/Users/bennabathulanivas/Desktop/my projects/NIVORA/builder/assemble_consultancy_universe.py"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Fix global reset
old_resets = """    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      min-width: 0;
    }"""

new_resets = """    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }"""

content = content.replace(old_resets, new_resets)

# 2. Fix word-break on a, span, button
old_word_break = """    h1, h2, h3, h4, h5, h6, p, a, span, button {
      overflow-wrap: break-word;
      word-break: break-word;
    }"""

new_word_break = """    h1, h2, h3, h4, h5, h6, p {
      overflow-wrap: break-word;
    }

    .nav-link, .btn, .nav-cta-btn, .btn-primary, .btn-secondary,
    .btn-service-explore, .nav-status-pill, .kicker, .brand-title,
    .brand-subtitle, .badge, .step-badge, .service-kicker {
      white-space: nowrap;
    }"""

content = content.replace(old_word_break, new_word_break)

# 3. Ensure min-width: 0 on grid items specifically
old_grid_items = """.services-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.25rem;
    }"""

new_grid_items = """.services-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.25rem;
    }

    .services-grid > *,
    .solutions-grid > *,
    .products-grid > *,
    .insights-grid > *,
    .journey-steps-grid > *,
    .hero-metrics > * {
      min-width: 0;
    }"""

content = content.replace(old_grid_items, new_grid_items)

# 4. Fix WebGL initialization condition
old_init = """    // Start WebGL Engine
    window.addEventListener('DOMContentLoaded', () => {
      initUniverseEngineCinematic();
    });"""

new_init = """    // Start WebGL Engine (Guaranteed Execution)
    if (document.readyState === 'loading') {
      window.addEventListener('DOMContentLoaded', initUniverseEngineCinematic);
    } else {
      initUniverseEngineCinematic();
    }"""

content = content.replace(old_init, new_init)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Applied precision fixes to assemble_consultancy_universe.py")
