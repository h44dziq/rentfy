import re

with open('c:/Users/hadziq/Documents/Rentfyy/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Extract nav_html
m_nav = re.search(r'function getCommonNavHtml\(\)\s*\{.*?return `(.*?)`;\s*\}', text, re.DOTALL)
nav_html = m_nav.group(1).strip() if m_nav else ""

# 2. Extract footer_html
m_footer = re.search(r'<template id="common-footer-template">\s*(<footer class="footer">.*?</footer>)\s*</template>', text, re.DOTALL)
footer_html = m_footer.group(1).strip() if m_footer else ""

# 3. Create demo bar
demo_bar_html = """
  <!-- Demo Top Bar -->
  <div id="demo-banner" class="demo-top-bar">
    <div class="demo-bar-content">
      <div class="demo-badge"><span class="pulse-dot"></span> PROTOTIPE DEMO RENTFY (SISI PENYEWA)</div>
      <div class="demo-user-info">Login sebagai: <strong>Rina</strong> · Lokasi: <span id="demo-loc-text">Jakarta Selatan</span> · Tanggal: <span id="demo-date-text">17 Nov</span></div>
      <div class="demo-quick-links">
        <button class="demo-pill-btn" onclick="navigateTo('L3')">🏠 Beranda</button>
        <button class="demo-pill-btn" onclick="navigateTo('L5')">🔍 Katalog</button>
        <button class="demo-pill-btn" onclick="navigateTo('L9')">📦 Pesanan</button>
        <button class="demo-pill-btn" onclick="navigateTo('L18')">👤 Profil</button>
        <button class="demo-pill-btn demo-pill-login" onclick="navigateTo('L1')">🔑 Uji Alur Login (L1)</button>
      </div>
    </div>
  </div>
"""

# Wrap persistent header
persistent_header_html = f"""
  {demo_bar_html}
  <!-- Global Persistent Navbar Header -->
  <div id="global-header-wrapper">
    {nav_html}
  </div>
"""

# Mobile tabs html
mobile_tabs_html = """
  <!-- Global Mobile Navigation Bar -->
  <nav id="global-mobile-tabs" class="mobile-tab-bar">
    <button class="tab-item active" id="tab-btn-beranda" onclick="navigateTo('L3')">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
      <span>Beranda</span>
    </button>
    <button class="tab-item" id="tab-btn-cari" onclick="handleMobileSearchTab()">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
      <span>Cari</span>
    </button>
    <button class="tab-item" id="tab-btn-pesanan" onclick="navigateTo('L9')">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
      <span>Pesanan</span>
    </button>
    <button class="tab-item" id="tab-btn-profil" onclick="navigateTo('L18')">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
      <span>Profil</span>
    </button>
  </nav>
"""

# Global footer html with id
persistent_footer_html = f"""
  <div id="global-footer" style="display: block;">
    {footer_html}
  </div>
  {mobile_tabs_html}
"""

# Insert persistent header right after <body>
text = re.sub(r'(<body[^>]*>)', r'\1\n' + persistent_header_html, text, count=1)

# Remove template common-footer-template and place persistent footer before Leaflet script
text = re.sub(r'<template id="common-footer-template">.*?</template>', persistent_footer_html, text, flags=re.DOTALL)

# Switch initial active screen from L1 to L3
text = text.replace('<section id="screen-L1" class="screen active"', '<section id="screen-L1" class="screen"')
text = text.replace('<section id="screen-L3" class="screen"', '<section id="screen-L3" class="screen active"')

# Update L1 and L2 styles to clean auth container without 100vh lock
text = text.replace(
    'id="screen-L1" class="screen" style="background-color: var(--primary); color: #FFFFFF; display: flex; align-items: center; justify-content: center; min-height: 100vh; padding: 24px 16px;"',
    'id="screen-L1" class="screen" style="background-color: var(--primary); color: #FFFFFF; min-height: 100vh; padding: 48px 16px 80px;"'
)
text = text.replace(
    'id="screen-L2" class="screen" style="background-color: var(--bg-page); display: flex; align-items: center; justify-content: center; min-height: 100vh; padding: 32px 16px;"',
    'id="screen-L2" class="screen" style="background-color: var(--bg-page); min-height: 100vh; padding: 48px 16px 80px;"'
)

# Add "Kembali ke Beranda" button inside L1 and L2 auth containers
l1_back_btn = """
      <div style="text-align: left; margin-bottom: 20px;">
        <button class="btn-ghost" style="color: #FFFFFF; padding: 4px 0; font-size: 13px; display: inline-flex; align-items: center; gap: 6px; cursor: pointer;" onclick="navigateTo('L3')">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
          Kembali ke Beranda
        </button>
      </div>
"""
text = text.replace(
    '<section id="screen-L1" class="screen" style="background-color: var(--primary); color: #FFFFFF; min-height: 100vh; padding: 48px 16px 80px;">\n    <div class="auth-container"',
    '<section id="screen-L1" class="screen" style="background-color: var(--primary); color: #FFFFFF; min-height: 100vh; padding: 48px 16px 80px;">\n    <div class="auth-container">\n' + l1_back_btn
)

l2_back_btn = """
      <div style="text-align: left; margin-bottom: 20px;">
        <button class="btn-ghost" style="color: var(--text-muted); padding: 4px 0; font-size: 13px; display: inline-flex; align-items: center; gap: 6px; cursor: pointer;" onclick="navigateTo('L3')">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
          Kembali ke Beranda
        </button>
      </div>
"""
text = text.replace(
    '<section id="screen-L2" class="screen" style="background-color: var(--bg-page); min-height: 100vh; padding: 48px 16px 80px;">\n    <div class="auth-container"',
    '<section id="screen-L2" class="screen" style="background-color: var(--bg-page); min-height: 100vh; padding: 48px 16px 80px;">\n    <div class="auth-container">\n' + l2_back_btn
)

# Remove min-height: 100vh from step screens
screen_replaces = [
    ('id="screen-L7" class="screen" style="background: var(--bg-page); min-height: 100vh;"', 'id="screen-L7" class="screen" style="padding: 24px 0 60px;"'),
    ('id="screen-L8" class="screen" style="background: var(--bg-page); min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 24px 16px;"', 'id="screen-L8" class="screen" style="padding: 32px 16px 60px;"'),
    ('id="screen-L10" class="screen" style="background: var(--bg-page); min-height: 100vh;"', 'id="screen-L10" class="screen" style="padding: 0 0 40px;"'),
    ('id="screen-L11" class="screen" style="background: var(--bg-page); min-height: 100vh;"', 'id="screen-L11" class="screen" style="padding: 24px 0 60px;"'),
    ('id="screen-L12" class="screen" style="background: var(--bg-page); min-height: 100vh;"', 'id="screen-L12" class="screen" style="padding: 24px 0 60px;"'),
    ('id="screen-L13" class="screen" style="background: var(--bg-page); min-height: 100vh;"', 'id="screen-L13" class="screen" style="padding: 24px 0 60px;"'),
    ('id="screen-L14" class="screen" style="background: var(--bg-page); min-height: 100vh;"', 'id="screen-L14" class="screen" style="padding: 24px 0 60px;"'),
    ('id="screen-L15" class="screen" style="background: var(--bg-page); min-height: 100vh;"', 'id="screen-L15" class="screen" style="padding: 24px 0 60px;"'),
    ('id="screen-L16" class="screen" style="background: var(--bg-page); min-height: 100vh;"', 'id="screen-L16" class="screen" style="padding: 24px 0 60px;"'),
    ('id="screen-L17" class="screen" style="background: var(--bg-page); min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 24px 16px;"', 'id="screen-L17" class="screen" style="padding: 32px 16px 60px;"'),
    ('id="screen-L19" class="screen" style="background: var(--bg-page); min-height: 100vh;"', 'id="screen-L19" class="screen" style="padding: 0 0 60px;"'),
]
for old_s, new_s in screen_replaces:
    text = text.replace(old_s, new_s)

# Remove placeholder container divs from screens
containers_to_remove = [
    '<div id="l3-nav-container"></div>',
    '<div id="l3-footer-container"></div>',
    '<div id="l3-tabs-container"></div>',
    '<div id="l5-nav-container"></div>',
    '<div id="l5-footer-container"></div>',
    '<div id="l5-tabs-container"></div>',
    '<div id="l6-nav-container"></div>',
    '<div id="l6-footer-container"></div>',
    '<div id="l9-nav-container"></div>',
    '<div id="l9-footer-container"></div>',
    '<div id="l9-tabs-container"></div>',
    '<div id="l18-nav-container"></div>',
    '<div id="l18-footer-container"></div>',
    '<div id="l18-tabs-container"></div>',
]
for c in containers_to_remove:
    text = text.replace(c, '')

# Update navigateTo in JavaScript
old_nav_logic = """    function navigateTo(screenId, params = {}) {
      if (screenId === 'L4') {
        openLocationPicker();
        return;
      }
      if (screenId === 'L20') {
        openFilterModal();
        return;
      }

      if (screenId !== currentScreen && screenId !== 'L10' && screenId !== 'L19') {
        previousScreen = currentScreen;
      }

      // Hide all screens
      const screens = document.querySelectorAll('.screen');
      screens.forEach(s => s.classList.remove('active'));

      // Show target screen
      const target = document.getElementById('screen-' + screenId);
      if (target) {
        target.classList.add('active');
        window.scrollTo(0, 0);
      }
      currentScreen = screenId;"""

new_nav_logic = """    function navigateTo(screenId, params = {}) {
      if (screenId === 'L4') {
        openLocationPicker();
        return;
      }
      if (screenId === 'L20') {
        openFilterModal();
        return;
      }

      if (screenId !== currentScreen && screenId !== 'L10' && screenId !== 'L19') {
        previousScreen = currentScreen;
      }

      // Hide all screens
      const screens = document.querySelectorAll('.screen');
      screens.forEach(s => s.classList.remove('active'));

      // Show target screen
      const target = document.getElementById('screen-' + screenId);
      if (target) {
        target.classList.add('active');
        window.scrollTo({ top: 0, behavior: 'instant' });
      }
      currentScreen = screenId;

      // Update persistent Global Header & Footer visibility
      const isAuthScreen = (screenId === 'L1' || screenId === 'L2');
      const headerWrap = document.getElementById('global-header-wrapper');
      const demoBar = document.getElementById('demo-banner');
      if (headerWrap) headerWrap.style.display = isAuthScreen ? 'none' : 'block';
      if (demoBar) demoBar.style.display = isAuthScreen ? 'none' : 'block';

      // Footer visibility: L3, L5, L6, L9, L18, L19 show footer. Step screens hide footer.
      const footerScreens = ['L3', 'L5', 'L6', 'L9', 'L18', 'L19'];
      const footerEl = document.getElementById('global-footer');
      if (footerEl) {
        footerEl.style.display = footerScreens.includes(screenId) ? 'block' : 'none';
      }

      // Mobile Tab Bar visibility: active on L3, L5, L9, L18
      const mobileTabsScreens = ['L3', 'L5', 'L9', 'L18'];
      const mobileTabsEl = document.getElementById('global-mobile-tabs');
      if (mobileTabsEl) {
        mobileTabsEl.style.display = mobileTabsScreens.includes(screenId) ? 'flex' : 'none';
      }

      // Sync persistent search input if on L3 or L5
      const desktopSearchInput = document.getElementById('desktop-search-input');
      if (desktopSearchInput && searchQuery) {
        desktopSearchInput.value = searchQuery;
      }
      // Sync persistent location chip text
      const navLocText = document.getElementById('nav-location-text');
      const demoLocText = document.getElementById('demo-loc-text');
      if (navLocText) navLocText.textContent = currentLocationName;
      if (demoLocText) demoLocText.textContent = currentLocationName;"""

text = text.replace(old_nav_logic, new_nav_logic)

# Update DOMContentLoaded to load L3 instead of L1
text = text.replace(
    "window.addEventListener('DOMContentLoaded', () => {\n      // Start at screen L1 per spec\n      navigateTo('L1');\n    });",
    "window.addEventListener('DOMContentLoaded', () => {\n      // Start at Homepage L3 per web standard (L1 can be tested anytime via top bar)\n      navigateTo('L3');\n    });"
)

# Also make sure mobile tab bar updates active state cleanly
old_tab_active_func = """    function updateMobileTabsActive(screenId) {
      const tabBars = document.querySelectorAll('.mobile-tab-bar');
      tabBars.forEach(bar => {
        const items = bar.querySelectorAll('.tab-item');
        items.forEach(it => it.classList.remove('active'));
        if (screenId === 'L3') {
          if (items[0]) items[0].classList.add('active');
        } else if (screenId === 'L5') {
          if (items[1]) items[1].classList.add('active');
        } else if (screenId === 'L9' || screenId === 'L11') {
          if (items[2]) items[2].classList.add('active');
        } else if (screenId === 'L18') {
          if (items[3]) items[3].classList.add('active');
        }
      });
    }"""

new_tab_active_func = """    function updateMobileTabsActive(screenId) {
      const bBeranda = document.getElementById('tab-btn-beranda');
      const bCari = document.getElementById('tab-btn-cari');
      const bPesanan = document.getElementById('tab-btn-pesanan');
      const bProfil = document.getElementById('tab-btn-profil');
      [bBeranda, bCari, bPesanan, bProfil].forEach(b => { if(b) b.classList.remove('active'); });

      if (screenId === 'L3' && bBeranda) bBeranda.classList.add('active');
      else if (screenId === 'L5' && bCari) bCari.classList.add('active');
      else if ((screenId === 'L9' || screenId === 'L11') && bPesanan) bPesanan.classList.add('active');
      else if (screenId === 'L18' && bProfil) bProfil.classList.add('active');
    }"""

text = text.replace(old_tab_active_func, new_tab_active_func)

with open('c:/Users/hadziq/Documents/Rentfyy/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Refactor applied successfully!")
