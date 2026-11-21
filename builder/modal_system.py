# builder/modal_system.py
# Complete Premium Product Concept Modal System for NIVORA

MODAL_CSS = """
    /* =========================================================
       NIVORA CONCEPT MODAL SYSTEM — PREMIUM IMMERSIVE INTERFACE
       ========================================================= */
    :root {
      --modal-accent: #21d9ff;
      --modal-glow: rgba(33, 217, 255, 0.28);
      --modal-secondary: #9d5cff;
    }

    /* Product Theme Overrides for Modal */
    .theme-checkra {
      --modal-accent: #21d9ff;
      --modal-glow: rgba(33, 217, 255, 0.26);
      --modal-secondary: #9d5cff;
    }
    .theme-homora {
      --modal-accent: #21d9ff;
      --modal-glow: rgba(33, 217, 255, 0.26);
      --modal-secondary: #4b8cff;
    }
    .theme-bubora {
      --modal-accent: #ec6dff;
      --modal-glow: rgba(236, 109, 255, 0.26);
      --modal-secondary: #9d5cff;
    }
    .theme-sayora {
      --modal-accent: #24d8a7;
      --modal-glow: rgba(36, 216, 167, 0.28);
      --modal-secondary: #21d9ff;
    }

    /* Background Page Lock */
    body.modal-scroll-locked {
      position: fixed;
      left: 0;
      right: 0;
      width: 100%;
      overflow: hidden;
      touch-action: none;
    }

    /* Modal Overlay & Backdrop */
    .concept-modal-overlay {
      position: fixed;
      inset: 0;
      z-index: 10000;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: clamp(12px, 2.5vw, 28px);
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
      transition: opacity 0.35s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.35s ease;
    }

    .concept-modal-overlay.active {
      opacity: 1;
      visibility: visible;
      pointer-events: auto;
    }

    .concept-modal-backdrop {
      position: absolute;
      inset: 0;
      background: rgba(4, 5, 12, 0.82);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      transition: opacity 0.35s ease;
    }

    /* Modal Window */
    .concept-modal-window {
      position: relative;
      z-index: 2;
      width: min(94vw, 1460px);
      height: min(90vh, 900px);
      max-height: 92dvh;
      display: flex;
      flex-direction: column;
      border-radius: 24px;
      border: 1px solid rgba(255, 255, 255, 0.14);
      background: linear-gradient(160deg, rgba(15, 17, 36, 0.97), rgba(6, 7, 16, 0.99));
      box-shadow: 0 40px 120px rgba(0, 0, 0, 0.85), 0 0 70px var(--modal-glow);
      overflow: hidden;
      transform: scale(0.96) translateY(14px);
      transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.35s ease, border-color 0.35s ease;
    }

    .concept-modal-overlay.active .concept-modal-window {
      transform: scale(1) translateY(0);
    }

    /* Sticky Modal Header */
    .concept-modal-header {
      flex-shrink: 0;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      padding: 16px 28px;
      background: rgba(10, 12, 26, 0.92);
      backdrop-filter: blur(18px);
      -webkit-backdrop-filter: blur(18px);
      border-bottom: 1px solid rgba(255, 255, 255, 0.10);
      z-index: 10;
    }

    .cmh-left {
      display: flex;
      align-items: center;
      gap: 16px;
      min-width: 0;
    }

    .cmh-logo-wrap {
      width: 48px;
      height: 48px;
      border-radius: 12px;
      display: grid;
      place-items: center;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 6px;
      flex-shrink: 0;
    }

    .cmh-logo-wrap img {
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      filter: drop-shadow(0 4px 12px rgba(0, 0, 0, 0.5));
    }

    .cmh-title-group {
      display: flex;
      flex-direction: column;
      min-width: 0;
    }

    .cmh-meta {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .cmh-name {
      font-size: 19px;
      font-weight: 850;
      letter-spacing: -0.02em;
      color: #ffffff;
    }

    .cmh-status-badge {
      font-size: 10px;
      font-weight: 800;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      padding: 3px 8px;
      border-radius: 999px;
      background: rgba(33, 217, 255, 0.14);
      color: var(--cyan);
      border: 1px solid rgba(33, 217, 255, 0.32);
    }
    .cmh-status-badge.concept {
      background: rgba(36, 216, 167, 0.14);
      color: var(--emerald);
      border-color: rgba(36, 216, 167, 0.32);
    }

    .cmh-tagline {
      font-size: 13px;
      font-weight: 600;
      color: var(--modal-accent);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      margin-top: 1px;
    }

    /* Modal In-Page Navigation Pills */
    .cmh-nav {
      display: flex;
      align-items: center;
      gap: 6px;
      background: rgba(255, 255, 255, 0.04);
      padding: 4px;
      border-radius: 999px;
      border: 1px solid rgba(255, 255, 255, 0.08);
    }

    .cmh-nav-link {
      padding: 6px 14px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 700;
      color: #9fa2b8;
      background: transparent;
      border: none;
      cursor: pointer;
      transition: all 0.22s ease;
      white-space: nowrap;
    }

    .cmh-nav-link:hover {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.06);
    }

    .cmh-nav-link.active {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.14);
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
    }

    .cmh-actions {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-shrink: 0;
    }

    .cmh-launch-btn {
      padding: 8px 16px;
      font-size: 12.5px;
      font-weight: 750;
    }

    .concept-modal-close {
      width: 40px;
      height: 40px;
      border-radius: 12px;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.14);
      color: #c5c7dc;
      display: grid;
      place-items: center;
      cursor: pointer;
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .concept-modal-close:hover {
      background: rgba(255, 255, 255, 0.16);
      color: #ffffff;
      border-color: rgba(255, 255, 255, 0.35);
      transform: scale(1.06);
    }

    /* Scrollable Modal Body */
    .concept-modal-body {
      flex: 1;
      overflow-y: auto;
      overflow-x: hidden;
      padding: clamp(24px, 4vw, 44px) clamp(20px, 4vw, 48px);
      scroll-behavior: smooth;
      -webkit-overflow-scrolling: touch;
    }

    .concept-modal-body::-webkit-scrollbar {
      width: 7px;
    }
    .concept-modal-body::-webkit-scrollbar-track {
      background: rgba(255, 255, 255, 0.02);
    }
    .concept-modal-body::-webkit-scrollbar-thumb {
      background: rgba(255, 255, 255, 0.15);
      border-radius: 999px;
    }
    .concept-modal-body::-webkit-scrollbar-thumb:hover {
      background: rgba(255, 255, 255, 0.28);
    }

    /* Product Content Panels inside Modal */
    .modal-product-panel {
      display: none;
    }
    .modal-product-panel.active {
      display: block;
      animation: modalFadeIn 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @keyframes modalFadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Modal Interior Sections */
    .modal-sec {
      margin-bottom: clamp(32px, 4vw, 48px);
    }

    .modal-intro-lead {
      font-size: clamp(16px, 1.8vw, 21px);
      line-height: 1.65;
      color: #e4e6f4;
      max-width: 980px;
      margin-bottom: 24px;
      font-weight: 500;
    }

    .modal-sec-title {
      font-size: 11px;
      font-weight: 850;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: var(--modal-accent);
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .modal-sec-heading {
      font-size: clamp(22px, 2.4vw, 32px);
      font-weight: 850;
      letter-spacing: -0.03em;
      color: #ffffff;
      margin-bottom: 12px;
    }

    /* Cards Grid in Modal (Capabilities) */
    .modal-grid-4 {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
    }
    .modal-grid-5 {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 12px;
    }
    .modal-grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
    }
    .modal-grid-2 {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 16px;
    }

    .modal-cap-card {
      padding: 18px 16px;
      border-radius: 14px;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .modal-cap-card:hover {
      background: rgba(255, 255, 255, 0.065);
      border-color: rgba(255, 255, 255, 0.22);
      transform: translateY(-3px);
      box-shadow: 0 10px 24px rgba(0, 0, 0, 0.35);
    }

    .mcc-icon {
      width: 34px;
      height: 34px;
      border-radius: 9px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      display: grid;
      place-items: center;
      color: var(--modal-accent);
      flex-shrink: 0;
    }

    .modal-cap-card h5 {
      font-size: 13.5px;
      font-weight: 750;
      color: #ffffff;
      letter-spacing: -0.01em;
      line-height: 1.3;
    }

    .modal-cap-card p {
      font-size: 11.5px;
      line-height: 1.6;
      color: #9ca0b6;
    }

    /* Core Idea Callout Banner in Modal */
    .modal-core-idea {
      padding: 30px 28px;
      border-radius: 18px;
      text-align: center;
      background: radial-gradient(circle at 50% 50%, var(--modal-glow), transparent 70%), rgba(255, 255, 255, 0.025);
      border: 1px solid rgba(255, 255, 255, 0.12);
      margin-bottom: clamp(32px, 4vw, 44px);
    }

    .modal-core-idea blockquote {
      font-size: clamp(20px, 2.4vw, 30px);
      font-weight: 850;
      letter-spacing: -0.03em;
      line-height: 1.3;
      color: #ffffff;
      margin-bottom: 12px;
    }

    .modal-core-idea p {
      max-width: 760px;
      margin: 0 auto;
      font-size: 13.5px;
      line-height: 1.7;
      color: #a4a7bf;
    }

    /* Compact Question / Chip Row */
    .modal-chip-row {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      justify-content: center;
      margin-top: 16px;
    }

    .modal-chip {
      padding: 6px 14px;
      border-radius: 999px;
      font-size: 11.5px;
      font-weight: 700;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #ffffff;
    }

    /* Visual Architecture / Pipeline Model */
    .modal-arch-rail {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      margin: 20px 0;
    }
    .modal-arch-rail.levels-3 {
      grid-template-columns: repeat(3, 1fr);
    }

    .modal-arch-step {
      padding: 18px 16px;
      border-radius: 14px;
      background: rgba(255, 255, 255, 0.025);
      border: 1px solid rgba(255, 255, 255, 0.09);
      position: relative;
    }

    .mas-tag {
      font-size: 10px;
      font-weight: 850;
      letter-spacing: 0.18em;
      color: var(--modal-accent);
      margin-bottom: 6px;
    }

    .modal-arch-step b {
      font-size: 14px;
      color: #ffffff;
      display: block;
      margin-bottom: 6px;
    }

    .modal-arch-step p {
      font-size: 11.5px;
      color: #9295ab;
      line-height: 1.6;
    }

    /* Horizontal Workflow Rail */
    .modal-workflow-rail {
      display: flex;
      gap: 10px;
      overflow-x: auto;
      padding-bottom: 8px;
      margin: 16px 0;
    }

    .modal-wf-step {
      flex: 1;
      min-width: 130px;
      padding: 14px 12px;
      border-radius: 12px;
      background: rgba(255, 255, 255, 0.035);
      border: 1px solid rgba(255, 255, 255, 0.08);
      text-align: center;
    }

    .mwf-num {
      font-size: 9px;
      font-weight: 850;
      letter-spacing: 0.15em;
      color: var(--modal-accent);
      margin-bottom: 4px;
    }

    .modal-wf-step b {
      font-size: 12.5px;
      color: #ffffff;
      display: block;
    }

    /* Visual Network / Ecosystem Box */
    .modal-network-diagram {
      padding: 24px;
      border-radius: 16px;
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid rgba(255, 255, 255, 0.08);
      text-align: center;
      margin: 18px 0;
    }

    .mnd-nodes {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      flex-wrap: wrap;
    }

    .mnd-node {
      padding: 8px 18px;
      border-radius: 10px;
      font-size: 12px;
      font-weight: 750;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.14);
      color: #ffffff;
    }

    .mnd-arrow {
      color: var(--modal-accent);
      font-weight: 800;
      font-size: 14px;
    }

    /* Responsible Design Card in Modal */
    .modal-responsible-notice {
      padding: 20px 24px;
      border-radius: 14px;
      border: 1px solid rgba(255, 255, 255, 0.12);
      background: rgba(255, 255, 255, 0.02);
      margin-top: 24px;
      position: relative;
    }

    .mrn-kicker {
      font-size: 9.5px;
      font-weight: 850;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: #ffa07a;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .modal-responsible-notice h5 {
      font-size: 15px;
      color: #ffffff;
      margin-bottom: 6px;
    }

    .modal-responsible-notice p {
      font-size: 12px;
      color: #9aa0b6;
      line-height: 1.7;
    }

    /* Modal Vision & Taglines */
    .modal-vision-box {
      display: grid;
      grid-template-columns: 1.3fr 0.7fr;
      gap: 20px;
      padding: 24px 28px;
      border-radius: 16px;
      background: rgba(255, 255, 255, 0.035);
      border: 1px solid rgba(255, 255, 255, 0.10);
      align-items: center;
      margin-top: 28px;
    }

    .mv-left h4 {
      font-size: 10px;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: var(--modal-accent);
      margin-bottom: 6px;
    }

    .mv-left p {
      font-size: 14px;
      line-height: 1.65;
      color: #ffffff;
      font-weight: 550;
    }

    .mv-right {
      text-align: right;
      border-left: 1px solid rgba(255, 255, 255, 0.08);
      padding-left: 20px;
    }

    .mv-tagline-primary {
      font-size: 17px;
      font-weight: 850;
      color: #ffffff;
      margin-bottom: 4px;
    }

    .mv-tagline-secondary {
      font-size: 12px;
      color: #8c90a8;
      font-weight: 600;
    }

    /* Modal Footer Switcher */
    .modal-footer-nav {
      margin-top: 36px;
      padding-top: 22px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }

    .mfn-links {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }

    .mfn-btn {
      padding: 8px 14px;
      border-radius: 9px;
      font-size: 12px;
      font-weight: 700;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: #c4c6dc;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .mfn-btn:hover {
      background: rgba(255, 255, 255, 0.09);
      color: #ffffff;
      border-color: rgba(255, 255, 255, 0.22);
    }

    /* Media Queries for Modal Responsiveness */
    @media (max-width: 1200px) {
      .modal-grid-5 { grid-template-columns: repeat(3, 1fr); }
      .modal-grid-4 { grid-template-columns: repeat(3, 1fr); }
      .modal-arch-rail { grid-template-columns: repeat(2, 1fr); }
    }

    @media (max-width: 900px) {
      .concept-modal-header {
        padding: 14px 18px;
      }
      .cmh-nav { display: none; }
      .modal-grid-5 { grid-template-columns: repeat(2, 1fr); }
      .modal-grid-4 { grid-template-columns: repeat(2, 1fr); }
      .modal-grid-3 { grid-template-columns: repeat(2, 1fr); }
      .modal-arch-rail.levels-3 { grid-template-columns: 1fr; }
      .modal-vision-box {
        grid-template-columns: 1fr;
      }
      .mv-right {
        text-align: left;
        border-left: none;
        padding-left: 0;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        padding-top: 12px;
      }
    }

    @media (max-width: 600px) {
      .concept-modal-overlay {
        padding: 8px;
      }
      .concept-modal-window {
        width: 100%;
        height: 96dvh;
        max-height: 96dvh;
        border-radius: 16px;
      }
      .concept-modal-body {
        padding: 20px 16px;
      }
      .cmh-tagline { display: none; }
      .cmh-launch-btn span:not(.btn-arrow) { display: none; }
      .cmh-launch-btn { padding: 8px 10px; }
      .modal-grid-5, .modal-grid-4, .modal-grid-3, .modal-grid-2 {
        grid-template-columns: 1fr;
      }
      .modal-arch-rail { grid-template-columns: 1fr; }
      .modal-workflow-rail {
        flex-direction: column;
      }
    }
"""
