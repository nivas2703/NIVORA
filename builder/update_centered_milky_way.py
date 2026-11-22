#!/usr/bin/env python3
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MASTER_BUILDER = os.path.join(SCRIPT_DIR, "assemble_ultimate_3d_universe.py")

with open(MASTER_BUILDER, "r", encoding="utf-8") as f:
    code = f.read()

# Replace buildProceduralMilkyWay with centered concentrated Milky Way (symmetric, dense core)
old_mw = r"""    function buildProceduralMilkyWay() {
      milkyWayGroup = new THREE.Group();
      milkyWayGroup.position.set(globeCenterX, globeCenterY, globeCenterZ);
      milkyWayGroup.rotation.set(0.82, 0.22, -0.15); // Majestic cinematic 3D tilt

      const starCount = 42000;
      const positions = new Float32Array(starCount * 3);
      const colors = new Float32Array(starCount * 3);

      const armAngles = [0.45, 0.45 + Math.PI, 1.85, 1.85 + Math.PI];
      const armWeights = [0.38, 0.38, 0.12, 0.12];
      const rMin = 22;
      const rMax = 380;

      const cosX = Math.cos(0.82), sinX = Math.sin(0.82);
      const cosY = Math.cos(0.22), sinY = Math.sin(0.22);

      for (let i = 0; i < starCount; i++) {
        const randArm = Math.random();
        let armIdx = 0;
        if (randArm < armWeights[0]) armIdx = 0;
        else if (randArm < armWeights[0] + armWeights[1]) armIdx = 1;
        else if (randArm < 0.88) armIdx = 2;
        else armIdx = 3;

        const baseAngle = armAngles[armIdx];
        const pRand = Math.random();
        const r = rMin + (rMax - rMin) * Math.pow(pRand, 1.65);

        // Mathematical logarithmic spiral
        const spiralAngle = baseAngle + 2.25 * Math.log(r / rMin) + 0.22 * (r / rMax);

        // Radial and vertical Gaussian dispersion
        const armWidth = 4.0 + 24.0 * (r / rMax);
        const rDisp = (Math.random() + Math.random() - 1.0) * armWidth;
        const tDisp = (Math.random() + Math.random() - 1.0) * (armWidth / (r + 25));

        const vertThickness = 12.0 * Math.exp(-r / 100) + 3.0 * (1.0 - r / rMax);
        const yDisp = (Math.random() + Math.random() - 1.0) * vertThickness;

        const actualR = r + rDisp;
        const actualTheta = spiralAngle + tDisp;

        const lx = actualR * Math.cos(actualTheta);
        const lz = actualR * Math.sin(actualTheta);
        const ly = yDisp;

        const wx = globeCenterX + lx * cosY - lz * sinY;
        const wy = globeCenterY + ly * cosX - (lx * sinY + lz * cosY) * sinX;

        // Quiet zone protection for left hero typography
        let starWeight = 1.0;
        if (wx < 12 && wy > -35 && wy < 45) {
          starWeight = 0.12;
        }

        positions[i * 3] = lx;
        positions[i * 3 + 1] = ly;
        positions[i * 3 + 2] = lz;

        // Color Grading: soft white, electric cyan, indigo, violet, magenta
        const frac = r / rMax;
        let cr, cg, cb;
        if (frac < 0.18) {
          cr = 0.96; cg = 0.98; cb = 1.0;
        } else if (frac < 0.52) {
          cr = 0.30; cg = 0.72; cb = 1.0;
        } else if (frac < 0.8) {
          cr = 0.65; cg = 0.42; cb = 0.95;
        } else {
          cr = 0.82; cg = 0.38; cb = 0.78;
        }

        colors[i * 3] = cr * starWeight;
        colors[i * 3 + 1] = cg * starWeight;
        colors[i * 3 + 2] = cb * starWeight;
      }

      const armGeo = new THREE.BufferGeometry();
      armGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
      armGeo.setAttribute('color', new THREE.BufferAttribute(colors, 3));

      const armMat = new THREE.PointsMaterial({
        size: 1.5,
        sizeAttenuation: true,
        vertexColors: true,
        map: createSoftPointTexture(),
        transparent: true,
        opacity: 0.85,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });

      spiralArmStars = new THREE.Points(armGeo, armMat);
      milkyWayGroup.add(spiralArmStars);
      scene.add(milkyWayGroup);
    }"""

new_mw = r"""    function buildProceduralMilkyWay() {
      // CONCENTRATED PROCEDURAL MILKY WAY CENTERED DIRECTLY AROUND NIVORA CORE
      milkyWayGroup = new THREE.Group();
      milkyWayGroup.position.set(globeCenterX, globeCenterY, globeCenterZ);
      milkyWayGroup.rotation.set(0.72, 0.12, -0.08); // Balanced symmetrical cosmic angle

      const starCount = 36000;
      const positions = new Float32Array(starCount * 3);
      const colors = new Float32Array(starCount * 3);

      const armAngles = [0.35, 0.35 + Math.PI, 1.85, 1.85 + Math.PI];
      const armWeights = [0.38, 0.38, 0.12, 0.12];
      const rMin = 18;
      const rMax = 280; // Concentrated around central core

      for (let i = 0; i < starCount; i++) {
        const randArm = Math.random();
        let armIdx = 0;
        if (randArm < armWeights[0]) armIdx = 0;
        else if (randArm < armWeights[0] + armWeights[1]) armIdx = 1;
        else if (randArm < 0.88) armIdx = 2;
        else armIdx = 3;

        const baseAngle = armAngles[armIdx];
        const pRand = Math.random();
        const r = rMin + (rMax - rMin) * Math.pow(pRand, 1.6);

        // Mathematical logarithmic spiral
        const spiralAngle = baseAngle + 2.6 * Math.log(r / rMin) + 0.18 * (r / rMax);

        const armWidth = 3.5 + 18.0 * (r / rMax);
        const rDisp = (Math.random() + Math.random() - 1.0) * armWidth;
        const tDisp = (Math.random() + Math.random() - 1.0) * (armWidth / (r + 20));

        const vertThickness = 8.0 * Math.exp(-r / 90) + 2.5 * (1.0 - r / rMax);
        const yDisp = (Math.random() + Math.random() - 1.0) * vertThickness;

        const actualR = r + rDisp;
        const actualTheta = spiralAngle + tDisp;

        positions[i * 3] = actualR * Math.cos(actualTheta);
        positions[i * 3 + 1] = yDisp;
        positions[i * 3 + 2] = actualR * Math.sin(actualTheta);

        // Radiant white-cyan at core, electric blue & violet arms, magenta accents
        const frac = r / rMax;
        if (frac < 0.22) {
          colors[i * 3] = 0.98; colors[i * 3 + 1] = 0.99; colors[i * 3 + 2] = 1.0;
        } else if (frac < 0.55) {
          colors[i * 3] = 0.22; colors[i * 3 + 1] = 0.74; colors[i * 3 + 2] = 1.0;
        } else if (frac < 0.80) {
          colors[i * 3] = 0.68; colors[i * 3 + 1] = 0.42; colors[i * 3 + 2] = 0.98;
        } else {
          colors[i * 3] = 0.90; colors[i * 3 + 1] = 0.32; colors[i * 3 + 2] = 0.82;
        }
      }

      const armGeo = new THREE.BufferGeometry();
      armGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
      armGeo.setAttribute('color', new THREE.BufferAttribute(colors, 3));

      const armMat = new THREE.PointsMaterial({
        size: 1.5,
        sizeAttenuation: true,
        vertexColors: true,
        map: createSoftPointTexture(),
        transparent: true,
        opacity: 0.88,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });

      spiralArmStars = new THREE.Points(armGeo, armMat);
      milkyWayGroup.add(spiralArmStars);
      scene.add(milkyWayGroup);
    }"""

if old_mw in code:
    code = code.replace(old_mw, new_mw)
    print("Replaced buildProceduralMilkyWay with symmetric concentrated Milky Way")
else:
    print("old_mw target not found")

with open(MASTER_BUILDER, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated assemble_ultimate_3d_universe.py successfully!")
