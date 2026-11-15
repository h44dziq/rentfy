import re

# Read current index.html
with open('c:/Users/hadziq/Documents/Rentfyy/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update .screen CSS
old_screen_css = """.screen {
      display: none;
      min-height: 100vh;
      width: 100%;
    }
    .screen.active {
      display: block;
    }"""

new_screen_css = """.screen {
      display: none;
      width: 100%;
      min-height: calc(100vh - 140px);
      padding-bottom: 40px;
    }
    .screen.active {
      display: block;
      animation: pageEnter 0.22s cubic-bezier(0.16, 1, 0.3, 1);
    }
    @keyframes pageEnter {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Demo Quick Top Bar */
    .demo-top-bar {
      background: #0A3F44;
      color: #E6F4F5;
      font-size: 12px;
      padding: 6px 16px;
      border-bottom: 1px solid rgba(255,255,255,0.1);
      position: sticky;
      top: 0;
      z-index: 1001;
    }
    .demo-bar-content {
      max-width: 1120px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }
    .demo-badge {
      display: flex;
      align-items: center;
      gap: 6px;
      font-weight: 600;
      color: #FDE68A;
      letter-spacing: 0.3px;
    }
    .pulse-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #10B981;
      box-shadow: 0 0 6px #10B981;
    }
    .demo-quick-links {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .demo-pill-btn {
      background: rgba(255,255,255,0.12);
      color: #FFFFFF;
      border: 1px solid rgba(255,255,255,0.2);
      border-radius: 12px;
      padding: 2px 10px;
      font-size: 11px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s;
    }
    .demo-pill-btn:hover {
      background: rgba(255,255,255,0.25);
    }
    .demo-pill-login {
      background: #F59E0B;
      color: #111827;
      border-color: #F59E0B;
      font-weight: 600;
    }
    .demo-pill-login:hover {
      background: #D97706;
      color: #111827;
    }

    /* Step indicator in checkout flow */
    .flow-stepper-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: #FFFFFF;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 12px 16px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
    }
    .flow-step-item {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      font-weight: 500;
      color: var(--text-muted);
    }
    .flow-step-item.active {
      color: var(--primary);
      font-weight: 700;
    }
    .flow-step-item.completed {
      color: var(--success);
    }
    .flow-step-num {
      width: 22px;
      height: 22px;
      border-radius: 50%;
      background: #F1F5F9;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
      font-weight: 700;
    }
    .flow-step-item.active .flow-step-num {
      background: var(--primary);
      color: #FFFFFF;
    }
    .flow-step-item.completed .flow-step-num {
      background: var(--success-soft);
      color: var(--success);
    }
    @media (max-width: 640px) {
      .demo-top-bar { display: none; }
      .flow-stepper-bar { display: none; }
    }"""

if old_screen_css in html:
    html = html.replace(old_screen_css, new_screen_css)
    print("Replaced screen CSS successfully")
else:
    print("WARNING: old_screen_css not found directly")

# Write updated file to test
with open('c:/Users/hadziq/Documents/Rentfyy/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("CSS updated")
