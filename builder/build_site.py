# builder/build_site.py
import os
import sys

# Ensure this directory is in sys.path
builder_dir = os.path.dirname(os.path.abspath(__file__))
if builder_dir not in sys.path:
    sys.path.append(builder_dir)

import css_styles
import header_html
import nav_hero_cards
import universe_philosophy
import deepdive_products
import remaining_sections

def build():
    print("Building full NIVORA index.html...")
    header = header_html.get_header_html(css_styles.CSS_CONTENT)
    nav_hero = nav_hero_cards.NAV_HERO_CARDS_HTML
    philosophy = universe_philosophy.UNIVERSE_PHILOSOPHY_HTML
    deepdive = deepdive_products.DEEPDIVE_PRODUCTS_HTML
    remaining = remaining_sections.REMAINING_SECTIONS_HTML

    full_html = header + nav_hero + philosophy + deepdive + remaining

    desktop_path = "/Users/bennabathulanivas/Desktop/my projects/NIVORA/index.html"
    downloads_path = "/Users/bennabathulanivas/Downloads/NIVORA/index.html"

    with open(desktop_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Successfully wrote {len(full_html)} chars to {desktop_path}")

    with open(downloads_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Successfully wrote {len(full_html)} chars to {downloads_path}")

if __name__ == "__main__":
    build()
