# builder/build_consultancy_universe.py
# Transforms NIVORA into a Premium Business • Finance • Technology Consultancy

import os
import sys

TARGET_FILE = "/Users/bennabathulanivas/Desktop/my projects/NIVORA/builder/assemble_ultimate_3d_universe.py"

def generate_consultancy_builder():
    with open(TARGET_FILE, "r", encoding="utf-8") as f:
        existing = f.read()

    # Verify that Three.js WebGL and modal logic are present
    assert "initUniverseEngineCinematic" in existing, "Three.js engine not found"
    assert "conceptModalOverlay" in existing, "Modal overlay not found"

    print("Existing file read successfully. Generating complete consultancy upgrade...")

if __name__ == '__main__':
    generate_consultancy_builder()
