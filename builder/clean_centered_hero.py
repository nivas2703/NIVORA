#!/usr/bin/env python3
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MASTER_BUILDER = os.path.join(SCRIPT_DIR, "assemble_ultimate_3d_universe.py")

with open(MASTER_BUILDER, "r", encoding="utf-8") as f:
    code = f.read()

# Replace buildGalacticAccretionPlatform with clean empty function so no horizontal disc cuts across centered text
old_accretion = r"""    function buildGalacticAccretionPlatform() {
      const beamHeight = 22;
      const vortexY = globeCenterY - 25.5 - beamHeight + 3;

      accretionGroup = new THREE.Group();
      accretionGroup.position.set(globeCenterX, vortexY, globeCenterZ);
      accretionGroup.rotation.set(Math.PI / 2.3, 0, 0.1);

      // 1. Concentric luminous vortex rings
      const ringConfigs = [
        { inner: 3, outer: 14, color: 0xffffff, opacity: 0.95 },
        { inner: 12, outer: 28, color: 0x06b6d4, opacity: 0.85 },
        { inner: 26, outer: 48, color: 0xa855f7, opacity: 0.75 },
        { inner: 45, outer: 72, color: 0xec4899, opacity: 0.65 },
        { inner: 68, outer: 95, color: 0x8b5cf6, opacity: 0.35 }
      ];

      ringConfigs.forEach(rc => {
        const rGeo = new THREE.RingGeometry(rc.inner, rc.outer, 64);
        const rMat = new THREE.MeshBasicMaterial({
          color: rc.color,
          transparent: true,
          opacity: rc.opacity,
          side: THREE.DoubleSide,
          blending: THREE.AdditiveBlending,
          depthWrite: false
        });
        const rMesh = new THREE.Mesh(rGeo, rMat);
        accretionGroup.add(rMesh);
      });

      // 2. 4,500 Swirling Spiral Particles
      const dPoints = 4500;
      const dPos = new Float32Array(dPoints * 3);
      const dCol = new Float32Array(dPoints * 3);

      for (let i = 0; i < dPoints; i++) {
        const arm = i % 4;
        const radius = 6 + Math.pow(Math.random(), 1.2) * 88;
        const angle = (arm * Math.PI / 2) + 2.8 * Math.log(radius / 5) + (Math.random() - 0.5) * 0.45;

        dPos[i * 3] = Math.cos(angle) * radius;
        dPos[i * 3 + 1] = (Math.random() - 0.5) * 2.2;
        dPos[i * 3 + 2] = Math.sin(angle) * radius;

        const p = radius / 94;
        if (p < 0.2) {
          dCol[i * 3] = 1.0; dCol[i * 3 + 1] = 1.0; dCol[i * 3 + 2] = 1.0;
        } else if (p < 0.45) {
          dCol[i * 3] = 0.05; dCol[i * 3 + 1] = 0.75; dCol[i * 3 + 2] = 0.95;
        } else if (p < 0.75) {
          dCol[i * 3] = 0.92; dCol[i * 3 + 1] = 0.28; dCol[i * 3 + 2] = 0.94;
        } else {
          dCol[i * 3] = 0.55; dCol[i * 3 + 1] = 0.22; dCol[i * 3 + 2] = 0.95;
        }
      }

      const dGeo = new THREE.BufferGeometry();
      dGeo.setAttribute('position', new THREE.BufferAttribute(dPos, 3));
      dGeo.setAttribute('color', new THREE.BufferAttribute(dCol, 3));
      accretionParticles = new THREE.Points(dGeo, new THREE.PointsMaterial({
        size: 2.2,
        vertexColors: true,
        map: createSoftPointTexture(),
        transparent: true,
        opacity: 0.85,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      }));
      accretionGroup.add(accretionParticles);
      scene.add(accretionGroup);

      // 3. Vertical Projection Light Column
      const beamGeo = new THREE.CylinderGeometry(1.6, 5.0, beamHeight, 32, 1, true);
      const beamCanvas = document.createElement('canvas');
      beamCanvas.width = 128; beamCanvas.height = 256;
      const bCtx = beamCanvas.getContext('2d');
      const bGrad = bCtx.createLinearGradient(0, 0, 0, 256);
      bGrad.addColorStop(0, 'rgba(255, 255, 255, 0.95)');
      bGrad.addColorStop(0.2, 'rgba(6, 182, 212, 0.85)');
      bGrad.addColorStop(0.7, 'rgba(168, 85, 247, 0.65)');
      bGrad.addColorStop(1, 'rgba(236, 72, 153, 0.1)');
      bCtx.fillStyle = bGrad;
      bCtx.fillRect(0, 0, 128, 256);

      energyBeam = new THREE.Mesh(beamGeo, new THREE.MeshBasicMaterial({
        map: new THREE.CanvasTexture(beamCanvas),
        transparent: true,
        opacity: 0.85,
        blending: THREE.AdditiveBlending,
        side: THREE.DoubleSide,
        depthWrite: false
      }));
      energyBeam.position.set(globeCenterX, globeCenterY - 25.5 - beamHeight / 2 + 2, globeCenterZ);
      scene.add(energyBeam);
    }"""

new_accretion = r"""    function buildGalacticAccretionPlatform() {
      // Clean minimal universe: removed distracting oversized horizontal discs to keep centered hero pure
    }"""

if old_accretion in code:
    code = code.replace(old_accretion, new_accretion)
    print("Replaced buildGalacticAccretionPlatform with clean implementation")
else:
    print("old_accretion target not found")

# Also ensure buildOrbitalRings3D has 3 delicate, thin glowing orbital rings around the core
old_rings = r"""    function buildOrbitalRings3D() {
      const ringSpecs = [
        { radiusX: 38, radiusY: 34, rotX: 1.25, rotY: 0.15, rotZ: 0.25, color: 0x06b6d4, speed: 0.002 },
        { radiusX: 44, radiusY: 38, rotX: 0.55, rotY: 1.15, rotZ: -0.50, color: 0xa855f7, speed: -0.0018 },
        { radiusX: 52, radiusY: 44, rotX: -0.75, rotY: 0.45, rotZ: 0.95, color: 0x38bdf8, speed: 0.0022 },
        { radiusX: 60, radiusY: 48, rotX: 0.35, rotY: -0.85, rotZ: 0.65, color: 0xec4899, speed: -0.0015 }
      ];"""

new_rings = r"""    function buildOrbitalRings3D() {
      // 3 Delicate, thin glowing orbital rings surrounding the central NIVORA Core
      const ringSpecs = [
        { radiusX: 24, radiusY: 22, rotX: 1.15, rotY: 0.20, rotZ: 0.30, color: 0x06b6d4, speed: 0.0018 },
        { radiusX: 29, radiusY: 26, rotX: 0.45, rotY: 1.05, rotZ: -0.45, color: 0xa855f7, speed: -0.0015 },
        { radiusX: 35, radiusY: 31, rotX: -0.65, rotY: 0.40, rotZ: 0.85, color: 0x38bdf8, speed: 0.0020 }
      ];"""

if old_rings in code:
    code = code.replace(old_rings, new_rings)
    print("Updated orbital rings around centered core")
else:
    print("old_rings target not found")

with open(MASTER_BUILDER, "w", encoding="utf-8") as f:
    f.write(code)

print("Saved updated assemble_ultimate_3d_universe.py!")
