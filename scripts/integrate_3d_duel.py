import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Three.js script tags before </head>
three_script = '''  <!-- Three.js 3D 引擎 (優先本地 assets，並具備官方 CDN 備援) -->
  <script src="assets/three.min.js"></script>
  <script>
    if (typeof THREE === 'undefined') {
      document.write('<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"><\\/script>');
    }
  </script>
</head>'''

assert '</head>' in content, "</head> not found"
content = content.replace('</head>', three_script, 1)

# 2. Add 3D Stage CSS inside <style>
arena_css_target = '/* ===== ARENA 題目對決戰場 ===== */'
stage_css = '''    /* ===== 3D 全息考題對決戰鬥舞台 ===== */
    .duel-3d-stage-container {
      position: relative;
      width: 100%;
      height: 230px;
      border-radius: var(--radius);
      overflow: hidden;
      margin-bottom: 1.25rem;
      background: radial-gradient(circle at center, #111a33 0%, #070d1e 100%);
      border: 1.5px solid rgba(52, 211, 180, 0.4);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4), inset 0 0 40px rgba(16, 185, 129, 0.08);
      user-select: none;
    }
    #duel3DCanvas {
      width: 100%;
      height: 100%;
      display: block;
      cursor: grab;
    }
    #duel3DCanvas:active {
      cursor: grabbing;
    }
    .duel-3d-overlay {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      pointer-events: none;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 12px 16px;
    }
    .duel-boss-hud {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
      background: rgba(7, 13, 30, 0.78);
      backdrop-filter: blur(8px);
      padding: 6px 14px;
      border-radius: 999px;
      border: 1px solid rgba(255, 255, 255, 0.14);
    }
    .duel-boss-tag {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 13.5px;
      font-weight: 800;
      color: #f1f5f9;
    }
    .pulse-indicator {
      width: 8px;
      height: 8px;
      background: #ef4444;
      border-radius: 50%;
      box-shadow: 0 0 8px #ef4444;
      animation: pulseDot 1.5s infinite;
    }
    @keyframes pulseDot {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(0.7); }
    }
    .level-pill {
      background: rgba(16, 185, 129, 0.2);
      color: #34d3b4;
      padding: 2px 8px;
      border-radius: 999px;
      font-size: 11.5px;
      border: 1px solid rgba(52, 211, 180, 0.3);
    }
    .duel-hp-wrapper {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .hp-label {
      font-size: 12px;
      color: #94a3b8;
      font-weight: 700;
    }
    .hp-track {
      width: 140px;
      height: 10px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 999px;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.15);
    }
    .hp-bar-fill {
      height: 100%;
      background: linear-gradient(90deg, #10b981, #f59e0b, #ef4444);
      border-radius: 999px;
      transition: width 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    .duel-3d-hint {
      text-align: right;
    }
    .duel-3d-hint span {
      font-size: 11.5px;
      color: #cbd5e1;
      background: rgba(15, 23, 42, 0.65);
      padding: 3px 10px;
      border-radius: 999px;
      border: 1px solid rgba(255, 255, 255, 0.08);
    }

    /* ===== ARENA 題目對決戰場 ===== */'''

assert arena_css_target in content, "arena_css_target not found"
content = content.replace(arena_css_target, stage_css, 1)

# 3. Add 3D Stage HTML inside <div class="arena-box">
arena_box_target = '''    <div class="arena-box">
      <!-- 遭遇怪獸資訊 -->'''

stage_html = '''    <div class="arena-box">
      <!-- ===== 3D 全息考題對決戰鬥舞台 ===== -->
      <div class="duel-3d-stage-container">
        <canvas id="duel3DCanvas"></canvas>
        <div class="duel-3d-overlay">
          <div class="duel-boss-hud">
            <div class="duel-boss-tag">
              <span class="pulse-indicator"></span>
              <span id="duelBossName3D">3D 多重抗藥菌 (CRE) 模型</span>
              <span class="level-pill" id="duelLevelPill">第 1 關 / 共 5 關</span>
            </div>
            <div class="duel-hp-wrapper">
              <span class="hp-label">病原體威脅值</span>
              <div class="hp-track">
                <div class="hp-bar-fill" id="duelBossHpFill" style="width: 100%;"></div>
              </div>
            </div>
          </div>
          <div class="duel-3d-hint">
            <span>🎮 3D 實戰對決 · 支援 360° 滑鼠拖曳檢視</span>
          </div>
        </div>
      </div>

      <!-- 遭遇怪獸資訊 -->'''

assert arena_box_target in content, "arena_box_target not found"
content = content.replace(arena_box_target, stage_html, 1)

# 4. Add 3D Engine JS code
# We will place the 3D Engine code right before `function renderDuel()`
duel_3d_engine_js = '''
    // ===== 3D 考題對決戰場引擎 (Three.js 3D Duel Arena Engine) =====
    let duelScene = null, duelCamera = null, duelRenderer = null, duelMonsterGroup = null, duelAnimId = null;
    let duelParticles = [];
    let isDragging3D = false, prevMouseX = 0, prevMouseY = 0;
    let targetRotY = 0, targetRotX = 0;
    let currentRotY = 0, currentRotX = 0;
    let beamMesh = null, shockwaveMesh = null;
    let cameraShake = 0;
    let monsterFloatTime = 0;
    let monsterBaseScale = 1;
    let hitFlashTime = 0;

    function init3DDuelEngine() {
      const canvas = document.getElementById('duel3DCanvas');
      if (!canvas) return;
      if (typeof THREE === 'undefined') {
        console.warn('Three.js 尚未就緒，將於下一幀重試初始化');
        setTimeout(init3DDuelEngine, 200);
        return;
      }
      if (duelRenderer) return; // 已初始化

      const container = canvas.parentElement;
      const width = container.clientWidth || 700;
      const height = container.clientHeight || 230;

      duelScene = new THREE.Scene();
      duelCamera = new THREE.PerspectiveCamera(45, width / height, 0.1, 100);
      duelCamera.position.set(0, 0, 6.2);

      duelRenderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
      duelRenderer.setSize(width, height);
      duelRenderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

      // 燈光系統
      const ambientLight = new THREE.AmbientLight(0xdbeafe, 0.95);
      duelScene.add(ambientLight);

      const dirLight = new THREE.DirectionalLight(0xffffff, 1.4);
      dirLight.position.set(5, 8, 6);
      duelScene.add(dirLight);

      const rimLight = new THREE.PointLight(0x34d3b4, 2.0, 20);
      rimLight.position.set(-4, -2, 4);
      duelScene.add(rimLight);

      const bossGlow = new THREE.PointLight(0xef4444, 1.5, 12);
      bossGlow.position.set(0, 0, 1);
      duelScene.add(bossGlow);

      // 怪獸根節點
      duelMonsterGroup = new THREE.Group();
      duelScene.add(duelMonsterGroup);

      // 拖曳旋轉監聽
      canvas.addEventListener('pointerdown', (e) => {
        isDragging3D = true;
        prevMouseX = e.clientX;
        prevMouseY = e.clientY;
      });
      window.addEventListener('pointermove', (e) => {
        if (!isDragging3D) return;
        const deltaX = e.clientX - prevMouseX;
        const deltaY = e.clientY - prevMouseY;
        targetRotY += deltaX * 0.008;
        targetRotX += deltaY * 0.008;
        prevMouseX = e.clientX;
        prevMouseY = e.clientY;
      });
      window.addEventListener('pointerup', () => { isDragging3D = false; });
      window.addEventListener('pointercancel', () => { isDragging3D = false; });

      window.addEventListener('resize', () => {
        if (!duelRenderer || !duelCamera) return;
        const newW = container.clientWidth || 700;
        const newH = container.clientHeight || 230;
        duelCamera.aspect = newW / newH;
        duelCamera.updateProjectionMatrix();
        duelRenderer.setSize(newW, newH);
      });

      animate3DDuel();
    }

    // 建立 6 道關卡專屬 3D 形態病原體模型
    function build3DMonster(index) {
      if (!duelMonsterGroup || typeof THREE === 'undefined') return;

      // 清空原有怪獸子物件
      while (duelMonsterGroup.children.length > 0) {
        const obj = duelMonsterGroup.children[0];
        duelMonsterGroup.remove(obj);
        if (obj.geometry) obj.geometry.dispose();
        if (obj.material) {
          if (Array.isArray(obj.material)) obj.material.forEach(m => m.dispose());
          else obj.material.dispose();
        }
      }

      // 重置位置與縮放
      duelMonsterGroup.position.set(0, 0, 0);
      duelMonsterGroup.rotation.set(0, 0, 0);
      duelMonsterGroup.scale.set(1, 1, 1);
      targetRotX = 0;
      targetRotY = 0;
      currentRotX = 0;
      currentRotY = 0;
      monsterBaseScale = 1;

      const qIndex = index % 6;

      if (qIndex === 0) {
        // 第 1 關：CRE / MDRO 腸道抗藥桿菌（莢膜桿菌 + 質體光環 + 纖毛）
        const bodyGeo = new THREE.CylinderGeometry(0.7, 0.7, 1.8, 32);
        const topCap = new THREE.SphereGeometry(0.7, 32, 16);
        const mat = new THREE.MeshStandardMaterial({
          color: 0x7c3aed,
          roughness: 0.25,
          metalness: 0.45,
          emissive: 0x2e1065
        });
        const meshBody = new THREE.Mesh(bodyGeo, mat);
        const meshTop = new THREE.Mesh(topCap, mat);
        meshTop.position.y = 0.9;
        const meshBot = new THREE.Mesh(topCap, mat);
        meshBot.position.y = -0.9;
        meshBody.rotation.z = Math.PI / 4;
        meshTop.rotation.z = Math.PI / 4;
        meshBot.rotation.z = Math.PI / 4;

        duelMonsterGroup.add(meshBody);
        duelMonsterGroup.add(meshTop);
        duelMonsterGroup.add(meshBot);

        // 旋轉質體抗藥環
        const ringGeo = new THREE.TorusGeometry(1.4, 0.06, 16, 64);
        const ringMat = new THREE.MeshBasicMaterial({ color: 0x34d3b4, wireframe: true });
        const ringMesh = new THREE.Mesh(ringGeo, ringMat);
        ringMesh.rotation.x = Math.PI / 2.5;
        duelMonsterGroup.add(ringMesh);

        // 纖毛棘刺
        for (let i = 0; i < 24; i++) {
          const spikeGeo = new THREE.ConeGeometry(0.08, 0.4, 8);
          const spikeMat = new THREE.MeshStandardMaterial({ color: 0xa855f7 });
          const spike = new THREE.Mesh(spikeGeo, spikeMat);
          const angle = (i / 24) * Math.PI * 2;
          spike.position.set(Math.cos(angle) * 1.0, (i % 6 - 2.5) * 0.35, Math.sin(angle) * 1.0);
          spike.lookAt(0, 0, 0);
          spike.rotateX(Math.PI);
          duelMonsterGroup.add(spike);
        }
      } else if (qIndex === 1) {
        // 第 2 關：髒汙管灌交界魔王（紅黑棘狀高危二十面體病毒）
        const coreGeo = new THREE.IcosahedronGeometry(1.1, 2);
        const coreMat = new THREE.MeshStandardMaterial({
          color: 0xef4444,
          roughness: 0.3,
          metalness: 0.6,
          emissive: 0x7f1d1d
        });
        const coreMesh = new THREE.Mesh(coreGeo, coreMat);
        duelMonsterGroup.add(coreMesh);

        // 突起蛋白棘刺 (Spike Glycoproteins)
        const count = 28;
        for (let i = 0; i < count; i++) {
          const phi = Math.acos(-1 + (2 * i) / count);
          const theta = Math.sqrt(count * Math.PI) * phi;
          const spikeGeo = new THREE.CylinderGeometry(0.05, 0.12, 0.65, 8);
          const headGeo = new THREE.SphereGeometry(0.14, 8, 8);
          const spikeMat = new THREE.MeshStandardMaterial({ color: 0xf59e0b });
          const spikeGroup = new THREE.Group();
          const sMesh = new THREE.Mesh(spikeGeo, spikeMat);
          const hMesh = new THREE.Mesh(headGeo, spikeMat);
          hMesh.position.y = 0.32;
          spikeGroup.add(sMesh);
          spikeGroup.add(hMesh);

          const r = 1.15;
          spikeGroup.position.set(
            r * Math.cos(theta) * Math.sin(phi),
            r * Math.sin(theta) * Math.sin(phi),
            r * Math.cos(phi)
          );
          spikeGroup.lookAt(0, 0, 0);
          spikeGroup.rotateX(-Math.PI / 2);
          duelMonsterGroup.add(spikeGroup);
        }
      } else if (qIndex === 2) {
        // 第 3 關：超音波傳導膠迷魂獸（金黃葡萄球菌葡萄串菌膜 MRSA Cluster）
        const sphereMat = new THREE.MeshStandardMaterial({
          color: 0xfbbf24,
          roughness: 0.2,
          metalness: 0.5,
          emissive: 0xb45309
        });
        const clusterCoords = [
          [0, 0, 0, 0.7],
          [0.6, 0.5, 0.3, 0.6],
          [-0.6, 0.4, -0.2, 0.58],
          [0.3, -0.6, 0.4, 0.55],
          [-0.4, -0.5, -0.3, 0.52],
          [0.5, -0.2, -0.5, 0.5],
          [-0.5, 0.2, 0.5, 0.53],
          [0.1, 0.8, -0.2, 0.48]
        ];
        clusterCoords.forEach(([x, y, z, rad]) => {
          const sGeo = new THREE.SphereGeometry(rad, 24, 24);
          const sMesh = new THREE.Mesh(sGeo, sphereMat);
          sMesh.position.set(x, y, z);
          duelMonsterGroup.add(sMesh);
        });

        // 外層半透明生物膜 (Biofilm Matrix)
        const filmGeo = new THREE.SphereGeometry(1.65, 32, 32);
        const filmMat = new THREE.MeshStandardMaterial({
          color: 0x38bdf8,
          transparent: true,
          opacity: 0.28,
          wireframe: true
        });
        const filmMesh = new THREE.Mesh(filmGeo, filmMat);
        duelMonsterGroup.add(filmMesh);
      } else if (qIndex === 3) {
        // 第 4 關：隔離病室生死門守護者（接觸隔離稜面警戒晶體石）
        const prismGeo = new THREE.DodecahedronGeometry(1.2, 0);
        const prismMat = new THREE.MeshStandardMaterial({
          color: 0xf59e0b,
          roughness: 0.15,
          metalness: 0.7,
          emissive: 0x78350f
        });
        const prismMesh = new THREE.Mesh(prismGeo, prismMat);
        duelMonsterGroup.add(prismMesh);

        // 雙向反旋黃黑警示環
        const r1Geo = new THREE.TorusGeometry(1.7, 0.05, 16, 64);
        const r1Mat = new THREE.MeshBasicMaterial({ color: 0xfacc15, wireframe: true });
        const r1 = new THREE.Mesh(r1Geo, r1Mat);
        r1.name = 'ring1';
        duelMonsterGroup.add(r1);

        const r2Geo = new THREE.TorusGeometry(1.9, 0.05, 16, 64);
        const r2Mat = new THREE.MeshBasicMaterial({ color: 0x3b82f6, wireframe: true });
        const r2 = new THREE.Mesh(r2Geo, r2Mat);
        r2.name = 'ring2';
        r2.rotation.x = Math.PI / 2;
        duelMonsterGroup.add(r2);
      } else if (qIndex === 4) {
        // 第 5 關：交叉感染暗影怪（雙層冠狀跳躍微粒球）
        const coreGeo = new THREE.SphereGeometry(0.9, 32, 32);
        const coreMat = new THREE.MeshStandardMaterial({
          color: 0x0284c7,
          roughness: 0.3,
          metalness: 0.5,
          emissive: 0x075985
        });
        const coreMesh = new THREE.Mesh(coreGeo, coreMat);
        duelMonsterGroup.add(coreMesh);

        const outerGeo = new THREE.SphereGeometry(1.35, 16, 16);
        const outerMat = new THREE.MeshBasicMaterial({
          color: 0x38bdf8,
          wireframe: true,
          transparent: true,
          opacity: 0.5
        });
        const outerMesh = new THREE.Mesh(outerGeo, outerMat);
        duelMonsterGroup.add(outerMesh);

        // 環繞微粒
        const dotsGeo = new THREE.BufferGeometry();
        const dotCoords = [];
        for (let i = 0; i < 48; i++) {
          const ang = (i / 48) * Math.PI * 2;
          const dist = 1.6 + Math.sin(i) * 0.4;
          dotCoords.push(Math.cos(ang) * dist, (Math.random() - 0.5) * 1.2, Math.sin(ang) * dist);
        }
        dotsGeo.setAttribute('position', new THREE.Float32BufferAttribute(dotCoords, 3));
        const dotsMat = new THREE.PointsMaterial({ color: 0x34d3b4, size: 0.09 });
        const dots = new THREE.Points(dotsGeo, dotsMat);
        dots.name = 'shadowDots';
        duelMonsterGroup.add(dots);
      } else {
        // 第 6 關：共用尿缸群聚惡魔（長鞭毛游動大腸桿菌 / 綠膿桿菌）
        const rodGeo = new THREE.CylinderGeometry(0.6, 0.6, 2.2, 24);
        const capGeo = new THREE.SphereGeometry(0.6, 24, 16);
        const rodMat = new THREE.MeshStandardMaterial({
          color: 0x059669,
          roughness: 0.2,
          metalness: 0.5,
          emissive: 0x064e3b
        });
        const rodMesh = new THREE.Mesh(rodGeo, rodMat);
        const cap1 = new THREE.Mesh(capGeo, rodMat);
        cap1.position.y = 1.1;
        const cap2 = new THREE.Mesh(capGeo, rodMat);
        cap2.position.y = -1.1;

        rodMesh.rotation.z = Math.PI / 3;
        cap1.rotation.z = Math.PI / 3;
        cap2.rotation.z = Math.PI / 3;

        duelMonsterGroup.add(rodMesh);
        duelMonsterGroup.add(cap1);
        duelMonsterGroup.add(cap2);

        // 3 條擺動尾部鞭毛 (Flagella)
        for (let f = 0; f < 3; f++) {
          const curvePoints = [];
          for (let seg = 0; seg < 10; seg++) {
            curvePoints.push(new THREE.Vector3(
              -1.0 - seg * 0.22,
              -0.6 - seg * 0.15 + Math.sin(seg + f) * 0.18,
              (f - 1) * 0.25 + Math.cos(seg) * 0.18
            ));
          }
          const fCurve = new THREE.CatmullRomCurve3(curvePoints);
          const fGeo = new THREE.TubeGeometry(fCurve, 20, 0.04, 8, false);
          const fMat = new THREE.MeshStandardMaterial({ color: 0x10b981, roughness: 0.4 });
          const fMesh = new THREE.Mesh(fGeo, fMat);
          fMesh.name = `flagella_${f}`;
          duelMonsterGroup.add(fMesh);
        }
      }
    }

    // 觸發 3D 攻擊與受擊動畫演出
    function trigger3DAttack(isCorrect) {
      if (!duelScene || !duelMonsterGroup || typeof THREE === 'undefined') return;

      const hpFill = document.getElementById('duelBossHpFill');

      if (isCorrect) {
        // --- 答對：翡翠光束直擊 ＋ 3D 爆裂星光 ＋ 怪物擊退翻滾 ---
        if (hpFill) hpFill.style.width = '0%';

        // 1. 發射翡翠光束 (Guardian Beam)
        const beamGeo = new THREE.CylinderGeometry(0.08, 0.22, 7.5, 16);
        const beamMat = new THREE.MeshBasicMaterial({ color: 0x34d3b4, transparent: true, opacity: 0.95 });
        beamMesh = new THREE.Mesh(beamGeo, beamMat);
        beamMesh.position.set(0, -1.5, 3.2);
        beamMesh.rotation.x = Math.PI / 2.3;
        duelScene.add(beamMesh);

        // 2. 怪物受擊反應：劇烈後仰擊退、縮放震顫
        monsterBaseScale = 1.35;
        hitFlashTime = 1.0;
        duelMonsterGroup.position.z = -1.6;
        duelMonsterGroup.rotation.y += Math.PI * 1.5;

        // 3. 3D 爆裂粒子 (Particle Burst)
        for (let i = 0; i < 45; i++) {
          const pGeo = new THREE.SphereGeometry(0.06 + Math.random() * 0.07, 8, 8);
          const pMat = new THREE.MeshBasicMaterial({
            color: Math.random() > 0.4 ? 0x34d3b4 : 0xffd166,
            transparent: true,
            opacity: 1
          });
          const pMesh = new THREE.Mesh(pGeo, pMat);
          pMesh.position.copy(duelMonsterGroup.position);
          const theta = Math.random() * Math.PI * 2;
          const phi = Math.random() * Math.PI;
          const spd = 0.08 + Math.random() * 0.16;
          pMesh.userData = {
            vx: Math.sin(phi) * Math.cos(theta) * spd,
            vy: Math.sin(phi) * Math.sin(theta) * spd,
            vz: Math.cos(phi) * spd,
            life: 1.0
          };
          duelScene.add(pMesh);
          duelParticles.push(pMesh);
        }

        // 光束漸漸消失
        setTimeout(() => {
          if (beamMesh) {
            duelScene.remove(beamMesh);
            beamMesh.geometry.dispose();
            beamMesh.material.dispose();
            beamMesh = null;
          }
        }, 500);

      } else {
        // --- 答錯：怪物猛撲鏡頭 ＋ 赤紅震盪波 ＋ 攝影機 3D 震動 ---
        cameraShake = 0.45;
        duelMonsterGroup.position.z = 1.8;
        monsterBaseScale = 1.45;

        // 赤紅衝擊光環
        const shockGeo = new THREE.RingGeometry(0.2, 0.4, 32);
        const shockMat = new THREE.MeshBasicMaterial({
          color: 0xef4444,
          side: THREE.DoubleSide,
          transparent: true,
          opacity: 0.9
        });
        shockwaveMesh = new THREE.Mesh(shockGeo, shockMat);
        shockwaveMesh.position.set(0, 0, 1.5);
        duelScene.add(shockwaveMesh);

        // 震盪波擴散消失
        const expandShock = () => {
          if (!shockwaveMesh) return;
          shockwaveMesh.scale.x += 0.22;
          shockwaveMesh.scale.y += 0.22;
          shockwaveMesh.material.opacity -= 0.05;
          if (shockwaveMesh.material.opacity > 0) {
            requestAnimationFrame(expandShock);
          } else {
            duelScene.remove(shockwaveMesh);
            shockwaveMesh.geometry.dispose();
            shockwaveMesh.material.dispose();
            shockwaveMesh = null;
          }
        };
        requestAnimationFrame(expandShock);
      }
    }

    // 3D 戰鬥主動畫循環
    function animate3DDuel() {
      duelAnimId = requestAnimationFrame(animate3DDuel);

      if (!duelRenderer || !duelScene || !duelCamera || !duelMonsterGroup) return;

      monsterFloatTime += 0.035;

      // 平滑旋轉內插
      currentRotY += (targetRotY - currentRotY) * 0.08;
      currentRotX += (targetRotX - currentRotX) * 0.08;

      duelMonsterGroup.rotation.y = currentRotY + Math.sin(monsterFloatTime * 0.8) * 0.25;
      duelMonsterGroup.rotation.x = currentRotX + Math.cos(monsterFloatTime * 0.6) * 0.15;
      duelMonsterGroup.position.y = Math.sin(monsterFloatTime) * 0.18;

      // 怪物縮放與受擊位置回彈
      duelMonsterGroup.position.z += (0 - duelMonsterGroup.position.z) * 0.08;
      monsterBaseScale += (1.0 - monsterBaseScale) * 0.08;
      duelMonsterGroup.scale.set(monsterBaseScale, monsterBaseScale, monsterBaseScale);

      // 環狀物持續旋轉
      const ring1 = duelMonsterGroup.getObjectByName('ring1');
      if (ring1) ring1.rotation.z += 0.03;
      const ring2 = duelMonsterGroup.getObjectByName('ring2');
      if (ring2) ring2.rotation.y += 0.025;
      const shadowDots = duelMonsterGroup.getObjectByName('shadowDots');
      if (shadowDots) shadowDots.rotation.y += 0.02;

      // 更新受擊爆裂粒子
      for (let i = duelParticles.length - 1; i >= 0; i--) {
        const p = duelParticles[i];
        p.position.x += p.userData.vx;
        p.position.y += p.userData.vy;
        p.position.z += p.userData.vz;
        p.userData.life -= 0.028;
        p.material.opacity = p.userData.life;
        p.scale.multiplyScalar(0.96);
        if (p.userData.life <= 0) {
          duelScene.remove(p);
          p.geometry.dispose();
          p.material.dispose();
          duelParticles.splice(i, 1);
        }
      }

      // 攝影機震動阻尼
      if (cameraShake > 0.01) {
        duelCamera.position.x = (Math.random() - 0.5) * cameraShake;
        duelCamera.position.y = (Math.random() - 0.5) * cameraShake;
        cameraShake *= 0.85;
      } else {
        duelCamera.position.x = 0;
        duelCamera.position.y = 0;
      }

      duelRenderer.render(duelScene, duelCamera);
    }
'''

render_duel_target = '    function renderDuel() {'
assert render_duel_target in content, "render_duel_target not found"
content = content.replace(render_duel_target, duel_3d_engine_js + '\n    function renderDuel() {', 1)

# 5. Update renderDuel to initialize/build 3D model and update HUD
old_render_duel_body = '''    function renderDuel() {
      state.answered = false;
      feedbackSheet.className = 'feedback-sheet';
      btnNextDuel.style.display = 'none';

      const q = duels[state.currentQ];
      monsterEmoji.textContent = q.monster;
      monsterTitle.textContent = `${q.monsterName} [關卡 ${state.currentQ + 1}/5]`;
      monsterDesc.textContent = q.monsterDesc;
      questionPrompt.textContent = q.prompt;'''

new_render_duel_body = '''    function renderDuel() {
      state.answered = false;
      feedbackSheet.className = 'feedback-sheet';
      btnNextDuel.style.display = 'none';

      const q = duels[state.currentQ];
      monsterEmoji.textContent = q.monster;
      monsterTitle.textContent = `${q.monsterName} [關卡 ${state.currentQ + 1}/${duels.length}]`;
      monsterDesc.textContent = q.monsterDesc;
      questionPrompt.textContent = q.prompt;

      // 同步 3D 考題對決戰場舞台
      init3DDuelEngine();
      build3DMonster(state.currentQ);
      const bossHpFill = document.getElementById('duelBossHpFill');
      if (bossHpFill) bossHpFill.style.width = '100%';
      const bossName3D = document.getElementById('duelBossName3D');
      if (bossName3D) bossName3D.textContent = `${q.monster} 3D 全息模型：${q.monsterName}`;
      const levelPill = document.getElementById('duelLevelPill');
      if (levelPill) levelPill.textContent = `第 ${state.currentQ + 1} 關 / 共 ${duels.length} 關`;'''

assert old_render_duel_body in content, "old_render_duel_body not found"
content = content.replace(old_render_duel_body, new_render_duel_body, 1)

# 6. Update selectDuelAnswer to trigger trigger3DAttack(true/false)
old_answer_pass = '''      if (selectedIdx === q.answer) {
        state.score += pts;
        sound.play('correct');
        spawnFloater(`✨ ${q.skillName}！+${pts} 分`, '#34d3b4', clickX, clickY);
        feedbackSheet.className = 'feedback-sheet show pass';
        feedbackSheet.innerHTML = `<strong>🎉 守護神底氣發動！擊退危機！</strong><br>${q.feedback}`;
      } else {'''

new_answer_pass = '''      if (selectedIdx === q.answer) {
        state.score += pts;
        sound.play('correct');
        trigger3DAttack(true); // 觸發 3D 翡翠雷射光束與爆裂星光
        spawnFloater(`✨ ${q.skillName}！+${pts} 分`, '#34d3b4', clickX, clickY);
        feedbackSheet.className = 'feedback-sheet show pass';
        feedbackSheet.innerHTML = `<strong>🎉 守護神底氣發動！擊退危機！</strong><br>${q.feedback}`;
      } else {
        trigger3DAttack(false); // 觸發 3D 怪物猛撲與攝影機震盪'''

assert old_answer_pass in content, "old_answer_pass not found"
content = content.replace(old_answer_pass, new_answer_pass, 1)

# 7. Also when entering startAdventure, ensure init3DDuelEngine is invoked
old_start_render = '''      document.getElementById('home').style.display = 'none';
      hudEl.classList.remove('hidden');
      arenaEl.classList.remove('hidden');
      sound.play('click');
      renderDuel();'''

new_start_render = '''      document.getElementById('home').style.display = 'none';
      hudEl.classList.remove('hidden');
      arenaEl.classList.remove('hidden');
      sound.play('click');
      init3DDuelEngine();
      renderDuel();'''

assert old_start_render in content, "old_start_render not found"
content = content.replace(old_start_render, new_start_render, 1)

# Write back to 感控不踩雷網站/index.html
with open('感控不踩雷網站/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully integrated 3D Duel Arena into 感控不踩雷網站/index.html")
