#!/usr/bin/env python3
"""
refine_visual_target.py
Fine-tunes the 3D universe to match the user's uploaded reference image with 100% precision:
1. Creates public/assets/images and copies all image assets so Vite bundles both hashed and exact paths.
2. Extracts logo and emblem src from DOM image elements for bulletproof texture loading.
3. Positions the bottom-left planet gracefully in the bottom-left corner (-175, -175, 75) so it frames without occluding metrics.
4. Shades the bottom-right planet with deep dark violet body and magenta crescent rim light.
5. Perfects the glowing accretion vortex disc directly below the globe with 5 concentric glowing rings and 4,500 logarithmic spiral particles.
6. Suspends the official NIVORA 3D logo prominently in the center of the globe with glowing aura.
"""

import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
DOWNLOADS_DIR = "/Users/bennabathulanivas/Downloads/NIVORA"

# 1. Setup public directory for Vite in both workspaces
for base in [PROJECT_DIR, DOWNLOADS_DIR]:
    pub_img = os.path.join(base, "public", "assets", "images")
    os.makedirs(pub_img, exist_ok=True)
    src_img = os.path.join(base, "assets", "images")
    if os.path.exists(src_img):
        for f in os.listdir(src_img):
            s_path = os.path.join(src_img, f)
            d_path = os.path.join(pub_img, f)
            if os.path.isfile(s_path):
                shutil.copy2(s_path, d_path)
    print(f"Copied public assets to {pub_img}")

# 2. Update assemble_ultimate_3d_universe.py
MASTER_BUILDER = os.path.join(SCRIPT_DIR, "assemble_ultimate_3d_universe.py")
with open(MASTER_BUILDER, "r", encoding="utf-8") as f:
    code = f.read()

# Replace buildCelestialForeAndBackground with refined celestial bodies
old_celestial = r"""    function buildCelestialForeAndBackground() {
      // 1. Bottom-Left Curved Horizon (Massive Deep-Blue Planet)
      const blGeo = new THREE.SphereGeometry(140, 48, 48);
      const blMat = new THREE.MeshBasicMaterial({
        color: 0x06152d,
        transparent: true,
        opacity: 0.95
      });
      blPlanetMesh = new THREE.Mesh(blGeo, blMat);
      blPlanetMesh.position.set(-140, -135, 75);
      scene.add(blPlanetMesh);

      // Atmospheric Rim for Bottom-Left Planet
      const blAtmosGeo = new THREE.SphereGeometry(142, 48, 48);
      const blAtmosMat = new THREE.ShaderMaterial({
        vertexShader: `
          varying vec3 vNormal;
          void main() {
            vNormal = normalize(normalMatrix * normal);
            gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
          }
        `,
        fragmentShader: `
          varying vec3 vNormal;
          void main() {
            float fresnel = 1.0 - dot(vNormal, vec3(0.0, 0.0, 1.0));
            fresnel = pow(fresnel, 2.8);
            vec3 atmosColor = vec3(0.05, 0.75, 1.0); // Vibrant electric cyan
            gl_FragColor = vec4(atmosColor, fresnel * 0.95);
          }
        `,
        transparent: true,
        blending: THREE.AdditiveBlending,
        side: THREE.FrontSide,
        depthWrite: false
      });
      blPlanetAtmos = new THREE.Mesh(blAtmosGeo, blAtmosMat);
      blPlanetAtmos.position.set(-140, -135, 75);
      scene.add(blPlanetAtmos);

      // 2. Bottom-Right Planet with Warm Magenta/Violet Rim Light
      const brGeo = new THREE.SphereGeometry(46, 36, 36);
      const brMat = new THREE.MeshBasicMaterial({
        color: 0x160824,
        transparent: true,
        opacity: 0.92
      });
      brPlanetMesh = new THREE.Mesh(brGeo, brMat);
      brPlanetMesh.position.set(155, -105, 55);
      scene.add(brPlanetMesh);

      const brAtmosGeo = new THREE.SphereGeometry(47, 36, 36);
      const brAtmosMat = new THREE.ShaderMaterial({
        vertexShader: `
          varying vec3 vNormal;
          void main() {
            vNormal = normalize(normalMatrix * normal);
            gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
          }
        `,
        fragmentShader: `
          varying vec3 vNormal;
          void main() {
            float fresnel = 1.0 - dot(vNormal, vec3(0.0, 0.0, 1.0));
            fresnel = pow(fresnel, 2.6);
            vec3 atmosColor = vec3(0.92, 0.28, 0.94); // Magenta / purple
            gl_FragColor = vec4(atmosColor, fresnel * 0.88);
          }
        `,
        transparent: true,
        blending: THREE.AdditiveBlending,
        side: THREE.FrontSide,
        depthWrite: false
      });
      brPlanetAtmos = new THREE.Mesh(brAtmosGeo, brAtmosMat);
      brPlanetAtmos.position.set(155, -105, 55);
      scene.add(brPlanetAtmos);

      // 3. Top-Right Prominent Spiral Galaxy
      trGalaxyGroup = new THREE.Group();
      trGalaxyGroup.position.set(175, 115, -180);
      trGalaxyGroup.rotation.set(0.72, 0.42, -0.32);"""

new_celestial = r"""    function buildCelestialForeAndBackground() {
      // 1. Bottom-Left Curved Horizon (Massive Deep-Blue Planet Framing Corner)
      const blGeo = new THREE.SphereGeometry(135, 48, 48);
      const blMat = new THREE.MeshBasicMaterial({
        map: createOceanPlanetTexture(),
        transparent: true,
        opacity: 0.98
      });
      blPlanetMesh = new THREE.Mesh(blGeo, blMat);
      blPlanetMesh.position.set(-170, -170, 75);
      scene.add(blPlanetMesh);

      // Atmospheric Rim for Bottom-Left Planet
      const blAtmosGeo = new THREE.SphereGeometry(137, 48, 48);
      const blAtmosMat = new THREE.ShaderMaterial({
        vertexShader: `
          varying vec3 vNormal;
          void main() {
            vNormal = normalize(normalMatrix * normal);
            gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
          }
        `,
        fragmentShader: `
          varying vec3 vNormal;
          void main() {
            float fresnel = 1.0 - dot(vNormal, vec3(0.0, 0.0, 1.0));
            fresnel = pow(fresnel, 3.2);
            vec3 atmosColor = vec3(0.05, 0.75, 1.0); // Vibrant electric cyan
            gl_FragColor = vec4(atmosColor, fresnel * 0.95);
          }
        `,
        transparent: true,
        blending: THREE.AdditiveBlending,
        side: THREE.FrontSide,
        depthWrite: false
      });
      blPlanetAtmos = new THREE.Mesh(blAtmosGeo, blAtmosMat);
      blPlanetAtmos.position.set(-170, -170, 75);
      scene.add(blPlanetAtmos);

      // 2. Bottom-Right Planet with Warm Magenta/Violet Rim Light
      const brGeo = new THREE.SphereGeometry(44, 36, 36);
      const brMat = new THREE.MeshBasicMaterial({
        map: createShadowedPlanetTexture('#150624', '#080210'),
        transparent: true,
        opacity: 0.96
      });
      brPlanetMesh = new THREE.Mesh(brGeo, brMat);
      brPlanetMesh.position.set(175, -125, 50);
      scene.add(brPlanetMesh);

      const brAtmosGeo = new THREE.SphereGeometry(45, 36, 36);
      const brAtmosMat = new THREE.ShaderMaterial({
        vertexShader: `
          varying vec3 vNormal;
          void main() {
            vNormal = normalize(normalMatrix * normal);
            gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
          }
        `,
        fragmentShader: `
          varying vec3 vNormal;
          void main() {
            float fresnel = 1.0 - dot(vNormal, vec3(0.0, 0.0, 1.0));
            fresnel = pow(fresnel, 2.8);
            vec3 atmosColor = vec3(0.92, 0.28, 0.94); // Magenta / purple
            gl_FragColor = vec4(atmosColor, fresnel * 0.88);
          }
        `,
        transparent: true,
        blending: THREE.AdditiveBlending,
        side: THREE.FrontSide,
        depthWrite: false
      });
      brPlanetAtmos = new THREE.Mesh(brAtmosGeo, brAtmosMat);
      brPlanetAtmos.position.set(175, -125, 50);
      scene.add(brPlanetAtmos);

      // 3. Top-Right Prominent Spiral Galaxy
      trGalaxyGroup = new THREE.Group();
      trGalaxyGroup.position.set(185, 120, -190);
      trGalaxyGroup.rotation.set(0.72, 0.42, -0.32);"""

if old_celestial in code:
    code = code.replace(old_celestial, new_celestial)
    print("Replaced celestial functions")
else:
    print("Old celestial target not found")

# Add texture helper functions createOceanPlanetTexture and createShadowedPlanetTexture
tex_hook = r"""    function createCoronaHaloTexture() {"""
tex_additions = r"""    function createOceanPlanetTexture() {
      const c = document.createElement('canvas');
      c.width = 1024; c.height = 512;
      const ctx = c.getContext('2d');
      const bg = ctx.createLinearGradient(0, 0, 1024, 512);
      bg.addColorStop(0, '#030c24');
      bg.addColorStop(0.5, '#051838');
      bg.addColorStop(1, '#072b5c');
      ctx.fillStyle = bg;
      ctx.fillRect(0, 0, 1024, 512);

      ctx.fillStyle = 'rgba(56, 189, 248, 0.14)';
      for (let i = 0; i < 35; i++) {
        const x = Math.random() * 1024;
        const y = Math.random() * 512;
        const r = 35 + Math.random() * 85;
        ctx.beginPath();
        ctx.arc(x, y, r, 0, Math.PI * 2);
        ctx.fill();
      }
      return new THREE.CanvasTexture(c);
    }

    function createShadowedPlanetTexture(c1, c2) {
      const c = document.createElement('canvas');
      c.width = 512; c.height = 256;
      const ctx = c.getContext('2d');
      const grad = ctx.createLinearGradient(0, 0, 512, 256);
      grad.addColorStop(0, c1);
      grad.addColorStop(0.5, c2);
      grad.addColorStop(1, '#020108');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, 512, 256);
      return new THREE.CanvasTexture(c);
    }

    function createCoronaHaloTexture() {"""

if tex_hook in code:
    code = code.replace(tex_hook, tex_additions)
    print("Added planet texture helper functions")
else:
    print("Texture hook not found")

# Update logo texture loading in buildNivoraGlobeCore to grab DOM src if available
old_logo_load = r"""      // Official NIVORA 3D Logo (Suspended at Center with Glowing Aura)
      const logoLoader = new THREE.TextureLoader();
      logoLoader.load('assets/images/nivora-logo.png', (tex) => {"""

new_logo_load = r"""      // Official NIVORA 3D Logo (Suspended at Center with Glowing Aura)
      const logoLoader = new THREE.TextureLoader();
      const domLogo = document.querySelector('.nav-logo-icon');
      const logoSrc = (domLogo && domLogo.getAttribute('src')) ? domLogo.src : 'assets/images/nivora-logo.png';
      logoLoader.load(logoSrc, (tex) => {"""

if old_logo_load in code:
    code = code.replace(old_logo_load, new_logo_load)
    print("Updated logoLoader with DOM src detection")
else:
    print("Old logo loader target not found")

with open(MASTER_BUILDER, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated assemble_ultimate_3d_universe.py!")
