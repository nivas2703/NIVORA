# builder/assemble_modal_site.py
import re
import os
import sys

builder_dir = os.path.dirname(os.path.abspath(__file__))
if builder_dir not in sys.path:
    sys.path.append(builder_dir)

import modal_system
import modal_content

def build():
    with open('/tmp/original_head.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update <style> with modal CSS
    style_close = "</style>"
    if style_close in html:
        html = html.replace(style_close, modal_system.MODAL_CSS + "\n  " + style_close, 1)

    # 2. Update Hero Satellites with onclick
    html = html.replace('class="satellite s-checkra"', 'class="satellite s-checkra" onclick="openConceptModal(\'checkra\', this)" title="Explore CHECKRA Concept"')
    html = html.replace('class="satellite s-homora"', 'class="satellite s-homora" onclick="openConceptModal(\'homora\', this)" title="Explore HOMORA Concept"')
    html = html.replace('class="satellite s-bubora"', 'class="satellite s-bubora" onclick="openConceptModal(\'bubora\', this)" title="Explore BUBORA Concept"')
    html = html.replace('class="satellite s-sayora"', 'class="satellite s-sayora" onclick="openConceptModal(\'sayora\', this)" title="Explore SAYORA Concept"')

    # 3. Clean up the #products section cards according to prompt section 15
    # Replace the old worlds-grid with the concise, premium cards
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

    # Locate and replace old worlds-grid in #products
    start_grid = html.find('<div class="worlds-grid">')
    end_grid = html.find('</section>', start_grid)
    # The container closes right before </section>
    grid_container_end = html.rfind('</div>', start_grid, end_grid)
    # The worlds-grid ends before that container closing div
    html = html[:start_grid] + clean_products_grid + '\n      </div>\n    </section>' + html[end_grid+10:]

    # 4. Inject Modal HTML right before </body>
    body_close = "</body>"
    if body_close in html:
        html = html.replace(body_close, modal_content.MODAL_HTML + "\n" + body_close, 1)

    # 5. Inject Modal JS right before </script>
    script_close = "</script>"
    if script_close in html:
        html = html.replace(script_close, modal_content.MODAL_JS + "\n  " + script_close, 1)

    # Save to Desktop and Downloads
    desktop_file = "/Users/bennabathulanivas/Desktop/my projects/NIVORA/index.html"
    downloads_file = "/Users/bennabathulanivas/Downloads/NIVORA/index.html"

    with open(desktop_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Assembled and saved {len(html)} chars to {desktop_file}")

    with open(downloads_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Assembled and saved {len(html)} chars to {downloads_file}")

if __name__ == '__main__':
    build()
