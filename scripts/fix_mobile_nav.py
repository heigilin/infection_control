# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html
with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_nav_css = '''    /* 全站統一導覽列 (純淨專業醫療風格，清楚標示 步驟 1 ➔ 步驟 2) */
    .site-nav {
      background: #ffffff;
      border-bottom: 1.5px solid #e2e8f0;
      position: sticky;
      top: 0;
      z-index: 100;
      padding: 0.75rem clamp(18px, 3.5vw, 48px);
      box-shadow: 0 2px 10px rgba(15, 23, 42, 0.05);
    }
    .nav-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      max-width: 1400px;
      margin: 0 auto;
    }
    .nav-brand {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
    }
    .nav-logo {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      object-fit: cover;
      border: 2px solid #085446;
    }
    .nav-brand-text {
      display: flex;
      flex-direction: column;
    }
    .nav-title {
      font-size: 1.15rem;
      font-weight: 900;
      color: #085446;
      line-height: 1.2;
    }
    .nav-flow-hint {
      font-size: 0.76rem;
      font-weight: 700;
      color: #64748b;
      letter-spacing: 0.5px;
    }
    .nav-links {
      display: flex;
      align-items: center;
      gap: 0.65rem;
      flex-wrap: wrap;
    }
    .nav-btn {
      padding: 0.5rem 0.95rem;
      border-radius: 999px;
      font-size: 0.88rem;
      font-weight: 800;
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      transition: all 0.15s;
      text-decoration: none;
      border: 1.5px solid #cbd5e1;
      background: #ffffff;
      color: #1e293b;
    }
    .nav-btn:hover {
      border-color: #085446;
      color: #085446;
      background: #f0fdf4;
    }
    .nav-btn.active {
      background: #085446 !important;
      color: #ffffff !important;
      border-color: #085446 !important;
      box-shadow: 0 2px 8px rgba(8, 84, 70, 0.25);
    }
    .current-dot {
      font-size: 0.68rem;
      background: #2dd4bf;
      color: #042f2e;
      padding: 1px 6px;
      border-radius: 999px;
      font-weight: 900;
    }
    .nav-btn-line {
      background: #059669;
      color: #ffffff !important;
      border-color: #059669;
    }
    .nav-btn-line:hover {
      background: #047857;
      color: #ffffff !important;
    }'''

new_nav_css = '''    /* 全站統一導覽列 (支援行動版響應式排版，無縫融入深色沉浸主題) */
    .site-nav {
      background: rgba(8, 18, 15, 0.96);
      backdrop-filter: blur(14px);
      border-bottom: 1.5px solid rgba(45, 212, 191, 0.25);
      position: sticky;
      top: 0;
      z-index: 100;
      padding: 0.65rem clamp(12px, 3vw, 36px);
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }
    .nav-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
      max-width: 1400px;
      margin: 0 auto;
    }
    .nav-brand {
      display: flex;
      align-items: center;
      gap: 0.65rem;
      text-decoration: none;
      min-width: 0;
      flex-shrink: 0;
    }
    .nav-logo {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      object-fit: cover;
      border: 2px solid #2dd4bf;
      flex-shrink: 0;
    }
    .nav-brand-text {
      display: flex;
      flex-direction: column;
      min-width: 0;
      white-space: nowrap;
    }
    .nav-title {
      font-size: 1.1rem;
      font-weight: 900;
      color: #ffffff;
      line-height: 1.2;
      white-space: nowrap;
    }
    .nav-flow-hint {
      font-size: 0.74rem;
      font-weight: 700;
      color: #2dd4bf;
      letter-spacing: 0.3px;
      white-space: nowrap;
    }
    .nav-links {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      flex-wrap: wrap;
    }
    .nav-btn {
      padding: 0.45rem 0.85rem;
      border-radius: 999px;
      font-size: 0.84rem;
      font-weight: 800;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.15s;
      text-decoration: none;
      border: 1px solid rgba(45, 212, 191, 0.35);
      background: rgba(255, 255, 255, 0.08);
      color: #e2f1ec;
      white-space: nowrap;
    }
    .nav-btn:hover {
      border-color: #2dd4bf;
      color: #ffffff;
      background: rgba(45, 212, 191, 0.2);
    }
    .nav-btn.active {
      background: #0f766e !important;
      color: #ffffff !important;
      border-color: #2dd4bf !important;
      box-shadow: 0 2px 10px rgba(45, 212, 191, 0.3);
    }
    .current-dot {
      font-size: 0.68rem;
      background: #2dd4bf;
      color: #042f2e;
      padding: 1px 6px;
      border-radius: 999px;
      font-weight: 900;
      white-space: nowrap;
    }
    .nav-btn-line {
      background: #059669;
      color: #ffffff !important;
      border-color: #10b981;
    }
    .nav-btn-line:hover {
      background: #047857;
      color: #ffffff !important;
    }

    /* 手機直向與小螢幕自適應排版 (防止字元直立排列與按鈕擠壓) */
    @media (max-width: 768px) {
      .site-nav {
        padding: 0.5rem 12px;
      }
      .nav-inner {
        flex-direction: column;
        align-items: stretch;
        gap: 0.5rem;
      }
      .nav-brand {
        justify-content: flex-start;
      }
      .nav-title {
        font-size: 0.98rem;
      }
      .nav-flow-hint {
        font-size: 0.68rem;
      }
      .nav-links {
        display: flex;
        flex-wrap: nowrap;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        gap: 6px;
        padding-bottom: 2px;
        scrollbar-width: none;
      }
      .nav-links::-webkit-scrollbar {
        display: none;
      }
      .nav-btn {
        flex-shrink: 0;
        padding: 0.35rem 0.75rem;
        font-size: 0.78rem;
      }
    }'''

text_norm = text.replace('\r\n', '\n')
old_nav_css_norm = old_nav_css.replace('\r\n', '\n')

if old_nav_css_norm in text_norm:
    text_norm = text_norm.replace(old_nav_css_norm, new_nav_css.replace('\r\n', '\n'), 1)
    with open('感控不踩雷網站/index.html', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(text_norm)
    print("index.html site-nav CSS updated successfully.")
else:
    print("WARNING: old_nav_css not found in index.html!")

# 2. Update presentation.html with same mobile protection
with open('感控不踩雷網站/presentation.html', 'r', encoding='utf-8') as f:
    p_text = f.read()

old_p_nav_css = '''    .nav-brand {
      display: flex;
      align-items: center;
      gap: 0.85rem;
      font-weight: 900;
      font-size: 1.15rem;
      color: var(--accent);
    }'''

new_p_nav_css = '''    .nav-brand {
      display: flex;
      align-items: center;
      gap: 0.85rem;
      font-weight: 900;
      font-size: 1.15rem;
      color: var(--accent);
      min-width: 0;
      flex-shrink: 0;
      white-space: nowrap;
    }
    .nav-btn {
      white-space: nowrap;
    }
    @media (max-width: 768px) {
      .site-nav {
        padding: 0.5rem 12px;
      }
      .nav-inner {
        flex-direction: column;
        align-items: stretch;
        gap: 0.5rem;
      }
      .nav-brand {
        font-size: 1rem;
      }
      .nav-links {
        display: flex;
        flex-wrap: nowrap;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        gap: 6px;
        padding-bottom: 2px;
        scrollbar-width: none;
      }
      .nav-links::-webkit-scrollbar {
        display: none;
      }
      .nav-btn {
        flex-shrink: 0;
        padding: 0.35rem 0.75rem;
        font-size: 0.78rem;
      }
    }'''

p_text_norm = p_text.replace('\r\n', '\n')
old_p_nav_css_norm = old_p_nav_css.replace('\r\n', '\n')

if old_p_nav_css_norm in p_text_norm:
    p_text_norm = p_text_norm.replace(old_p_nav_css_norm, new_p_nav_css.replace('\r\n', '\n'), 1)
    with open('感控不踩雷網站/presentation.html', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(p_text_norm)
    print("presentation.html site-nav CSS updated successfully.")
else:
    print("WARNING: old_p_nav_css not found in presentation.html!")

print("CSS updates completed.")
