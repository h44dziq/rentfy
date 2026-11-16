/**
 * Rentfy — Single-Page Application Router & Screen Controllers
 * UI System based on Referensi.md (Fiverr/Hygglo Commercial Model)
 * Clean vector SVG icons only — Zero emojis
 */

(function () {
  'use strict';

  // --------------------------------------------------------------------------
  // Vector SVG Icons Library (Zero Emojis)
  // --------------------------------------------------------------------------
  var Icons = {
    search: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>',
    pin: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>',
    calendar: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>',
    star: '<svg width="14" height="14" viewBox="0 0 24 24" fill="#F59E0B" stroke="#F59E0B" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>',
    starEmpty: '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F59E0B" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>',
    starFilled: '<svg width="24" height="24" viewBox="0 0 24 24" fill="#F59E0B" stroke="#F59E0B" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>',
    heartOutline: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>',
    heartFilled: '<svg width="18" height="18" viewBox="0 0 24 24" fill="#EF4444" stroke="#EF4444" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>',
    check: '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>',
    shield: '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>',
    bell: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>',
    message: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>',
    filter: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="21" x2="4" y2="14"></line><line x1="4" y1="10" x2="4" y2="3"></line><line x1="12" y1="21" x2="12" y2="12"></line><line x1="12" y1="8" x2="12" y2="3"></line><line x1="20" y1="21" x2="20" y2="16"></line><line x1="20" y1="12" x2="20" y2="3"></line><line x1="1" y1="14" x2="7" y2="14"></line><line x1="9" y1="8" x2="15" y2="8"></line><line x1="17" y1="16" x2="23" y2="16"></line></svg>',
    arrowRight: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>',
    arrowLeft: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>',
    info: '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>',
    camera: '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path><circle cx="12" cy="13" r="4"></circle></svg>',
    laptop: '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="2" y1="20" x2="22" y2="20"></line></svg>',
    wrench: '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg>',
    tent: '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 20 12 4 5 20"></path><path d="m5 20 7-7 7 7"></path><path d="M12 13v7"></path><path d="M2 20h20"></path></svg>',
    sports: '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"></path><path d="M2 12h20"></path></svg>',
    party: '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m4 11 7-7 5 5-7 7-5-5Z"></path><path d="m11 4 2 2"></path><path d="M17 11 4 22"></path><circle cx="19" cy="5" r="2"></circle><circle cx="5" cy="19" r="2"></circle></svg>',
    home: '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>',
    box: '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>',
    logout: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg>',
    upload: '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>',
    badgeCheck: '<svg width="14" height="14" viewBox="0 0 24 24" fill="#0F5C63" stroke="#ffffff" stroke-width="2"><path d="M12 2l2.4 2.8 3.7-.4 1.3 3.5 3.3 1.8-1 3.6 1.8 3.3-3.1 2.1-.4 3.7-3.7 1-2 3.2-3.2-2-3.7.4-1.3-3.5-3.3-1.8 1-3.6-1.8-3.3 3.1-2.1.4-3.7 3.7-1 2-3.2z"></path><polyline points="9 12 11 14 15 10" stroke="#ffffff" fill="none"></polyline></svg>',
    idCard: '<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="16" rx="2"></rect><circle cx="9" cy="10" r="2"></circle><line x1="15" y1="8" x2="17" y2="8"></line><line x1="15" y1="12" x2="17" y2="12"></line><line x1="7" y1="16" x2="17" y2="16"></line></svg>'
  };

  // --------------------------------------------------------------------------
  // Global Application State
  // --------------------------------------------------------------------------
  window.AppState = {
    isLoggedIn: false,
    selectedLocation: 'Jakarta Selatan',
    selectedDates: { start: '17 Nov', end: '18 Nov', days: 2 },
    searchQuery: 'camera',
    activeCategory: null,
    activeSort: 'terdekat',
    activeView: 'daftar',
    savedItems: new Set([1]),
    hasShownLocationModal: false,
    
    currentOrder: null,
    orderStatus: 'menunggu',
    verifyStep: 1,

    messages: [
      { sender: 'Dimas', text: 'Halo LeBron! Ada yang bisa saya bantu terkait unit kameranya?', time: '10:15' },
      { sender: 'LeBron James', text: 'Halo Mas Dimas, mau tanya apakah paketnya sudah termasuk tas dan memory card?', time: '10:17' },
      { sender: 'Dimas', text: 'Sudah lengkap LeBron, siap pakai langsung untuk kebutuhan dokumentasi.', time: '10:18' }
    ]
  };

  var mapInstances = [];

  function cleanupMaps() {
    mapInstances.forEach(function (m) {
      try { m.remove(); } catch (e) {}
    });
    mapInstances = [];
  }

  function formatRp(num) {
    return 'Rp' + (num || 0).toString().replace(/\B(?=(\d{3})+(?!\d))/g, '.');
  }

  window.showToast = function (message) {
    var toast = document.getElementById('toast-bar');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'toast-bar';
      toast.className = 'toast-bar';
      document.body.appendChild(toast);
    }
    toast.textContent = message;
    toast.classList.add('show');
    clearTimeout(toast._timer);
    toast._timer = setTimeout(function () {
      toast.classList.remove('show');
    }, 2800);
  };

  window.demoToast = function () {
    window.showToast('Fitur ini belum tersedia di versi demo');
  };

  // --------------------------------------------------------------------------
  // Router
  // --------------------------------------------------------------------------
  function router() {
    cleanupMaps();
    var hash = window.location.hash || '#/login';

    // Must start at login on first visit
    if (!window.AppState.isLoggedIn && hash !== '#/login' && hash !== '#/register') {
      window.location.hash = '#/login';
      return;
    }

    var app = document.getElementById('app');
    var nav = document.getElementById('top-nav');
    var subnav = document.getElementById('category-subnav');
    var footer = document.getElementById('site-footer');

    if (hash === '#/login') {
      nav.style.display = 'none';
      if (subnav) subnav.style.display = 'none';
      footer.style.display = 'none';
      renderLogin(app);
    } else if (hash === '#/register') {
      nav.style.display = 'none';
      if (subnav) subnav.style.display = 'none';
      footer.style.display = 'none';
      renderRegister(app);
    } else {
      nav.style.display = 'block';
      var trending = document.getElementById('trending-strip');
      var isHome = (hash === '#/' || hash === '#/home');
      var isSearch = (hash.indexOf('#/search') === 0);

      // Trending tag bar: visible on home and search
      if (trending) trending.style.display = (isHome || isSearch) ? 'block' : 'none';
      if (subnav) subnav.style.display = (isHome || isSearch) ? 'block' : 'none';

      // Navbar search bar:
      // Di Beranda & Kategori: searchbar di navbar disembunyikan saat di posisi atas
      // agar tidak dobel dengan hero search bar halaman. Saat di-scroll, baru muncul.
      // Di halaman lain (detail barang, pesanan, dsb): searchbar navbar langsung aktif.
      var hasPageSearch = isHome || isSearch;
      var navCenter = document.getElementById('nav-center-wrap');
      if (navCenter) {
        if (hasPageSearch) {
          navCenter.classList.add('hidden-nav-search');
        } else {
          navCenter.classList.remove('hidden-nav-search');
        }
      }

      // Sync navbar search input value
      var navInput = document.getElementById('nav-input');
      if (navInput) {
        if (isSearch) {
          var params = new URLSearchParams(hash.split('?')[1] || '');
          navInput.value = params.get('q') || '';
        } else if (isHome) {
          navInput.value = '';
        }
      }

      if (hash === '#/' || hash === '#/home') {
        footer.style.display = 'block';
        renderHome(app);
      } else if (hash.indexOf('#/search') === 0) {
        footer.style.display = 'block';
        renderSearch(app, hash);
      } else if (hash.indexOf('#/item/') === 0) {
        footer.style.display = 'block';
        var itemId = parseInt(hash.replace('#/item/', ''), 10);
        renderItemDetail(app, itemId);
      } else if (hash === '#/checkout') {
        footer.style.display = 'none';
        renderCheckout(app);
      } else if (hash === '#/request-sent') {
        footer.style.display = 'none';
        renderRequestSent(app);
      } else if (hash === '#/orders') {
        footer.style.display = 'block';
        renderOrders(app);
      } else if (hash === '#/order-detail') {
        footer.style.display = 'block';
        renderOrderDetail(app);
      } else if (hash === '#/chat') {
        footer.style.display = 'none';
        renderChat(app);
      } else if (hash === '#/verify') {
        footer.style.display = 'none';
        renderVerify(app);
      } else if (hash === '#/payment') {
        footer.style.display = 'none';
        renderPayment(app);
      } else if (hash === '#/pickup') {
        footer.style.display = 'none';
        renderPickup(app);
      } else if (hash === '#/renting') {
        footer.style.display = 'none';
        renderRenting(app);
      } else if (hash === '#/return') {
        footer.style.display = 'none';
        renderReturn(app);
      } else if (hash === '#/complete') {
        footer.style.display = 'none';
        renderComplete(app);
      } else if (hash === '#/profile') {
        footer.style.display = 'block';
        renderProfile(app);
      } else if (hash === '#/how-it-works') {
        footer.style.display = 'block';
        renderHowItWorks(app);
      } else {
        renderHome(app);
      }
    }

    // Mobile Bottom Tab Bar — visibility & active state
    var tabBar = document.getElementById('mobile-tab-bar');
    if (tabBar) {
      var hideTab = (hash === '#/login' || hash === '#/register');
      tabBar.style.display = hideTab ? 'none' : '';
      // Highlight active tab
      var tabMap = { '#/': 'beranda', '#/home': 'beranda', '#/search': 'cari', '#/orders': 'pesanan', '#/profile': 'profil' };
      var activeTab = tabMap[hash] || (hash.indexOf('#/search') === 0 ? 'cari' : '');
      tabBar.querySelectorAll('.mobile-tab-item').forEach(function(t) {
        t.classList.toggle('active', t.getAttribute('data-tab') === activeTab);
      });
    }

    window.scrollTo(0, 0);
  }

  // --------------------------------------------------------------------------
  // L1. LOGIN CONTROLLER
  // --------------------------------------------------------------------------
  function renderLogin(container) {
    container.innerHTML = `
      <div style="min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 40px 20px; background: #f8fafc;">
        <div style="width: 100%; max-width: 420px; background: #ffffff; border: 1px solid var(--color-mist); border-radius: var(--radius-cards); box-shadow: var(--shadow-md); padding: 40px;">
          <div style="text-align: center; margin-bottom: 28px;">
            <img src="images/logo.png" alt="Rentfy" style="height: 44px; width: auto; object-fit: contain; margin-bottom: 8px;">
            <p style="color: var(--color-graphite); font-size: 14px;">
              Sewa dan sewakan barang dengan sederhana dan aman
            </p>
          </div>

          <form id="login-form">
            <div style="margin-bottom: 18px;">
              <label style="display: block; font-size: 13px; font-weight: 600; margin-bottom: 6px; color: var(--color-slate);">Alamat Email</label>
              <input type="email" id="login-email" class="input-field" placeholder="nama@email.com" value="lebron@email.com">
            </div>
            <div style="margin-bottom: 24px;">
              <label style="display: block; font-size: 13px; font-weight: 600; margin-bottom: 6px; color: var(--color-slate);">Kata Sandi</label>
              <input type="password" id="login-pwd" class="input-field" placeholder="••••••••" value="password123">
            </div>

            <!-- Single Amber CTA per Screen -->
            <button type="submit" class="btn btn-amber btn-block">
              Masuk
            </button>
          </form>

          <div style="text-align: center; margin-top: 24px; font-size: 14px; color: var(--color-graphite);">
            Belum punya akun? <a href="#/register" style="color: var(--color-teal); font-weight: 600;">Daftar akun baru</a>
          </div>
        </div>
      </div>
    `;

    document.getElementById('login-form').addEventListener('submit', function (e) {
      e.preventDefault();
      window.AppState.isLoggedIn = true;
      window.location.hash = '#/';
      window.showToast('Selamat datang kembali, LeBron James');
    });
  }

  // --------------------------------------------------------------------------
  // L2. REGISTER CONTROLLER
  // --------------------------------------------------------------------------
  function renderRegister(container) {
    container.innerHTML = `
      <div style="min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 40px 20px; background: #f8fafc;">
        <div style="width: 100%; max-width: 440px; background: #ffffff; border: 1px solid var(--color-mist); border-radius: var(--radius-cards); box-shadow: var(--shadow-md); padding: 40px;">
          <div style="text-align: center; margin-bottom: 28px;">
            <img src="images/logo.png" alt="Rentfy" style="height: 44px; width: auto; object-fit: contain; margin-bottom: 8px;">
            <p style="color: var(--color-graphite); font-size: 14px;">Daftar akun penyewa untuk mulai bertransaksi</p>
          </div>

          <form id="reg-form">
            <div style="margin-bottom: 16px;">
              <label style="display: block; font-size: 13px; font-weight: 600; margin-bottom: 6px; color: var(--color-slate);">Nama Lengkap</label>
              <input type="text" class="input-field" value="LeBron James">
            </div>
            <div style="margin-bottom: 16px;">
              <label style="display: block; font-size: 13px; font-weight: 600; margin-bottom: 6px; color: var(--color-slate);">Email</label>
              <input type="email" class="input-field" value="lebron@email.com">
            </div>
            <div style="margin-bottom: 16px;">
              <label style="display: block; font-size: 13px; font-weight: 600; margin-bottom: 6px; color: var(--color-slate);">Nomor HP / WhatsApp</label>
              <input type="tel" class="input-field" value="081234567890">
            </div>
            <div style="margin-bottom: 16px;">
              <label style="display: block; font-size: 13px; font-weight: 600; margin-bottom: 6px; color: var(--color-slate);">Area Domisili</label>
              <select class="input-field">
                <option selected>Jakarta Selatan</option>
                <option>Jakarta Pusat</option>
                <option>Depok</option>
                <option>Tangerang Selatan</option>
              </select>
            </div>
            <div style="margin-bottom: 24px;">
              <label style="display: block; font-size: 13px; font-weight: 600; margin-bottom: 6px; color: var(--color-slate);">Kata Sandi</label>
              <input type="password" class="input-field" value="password123">
            </div>

            <!-- Single Amber CTA per Screen -->
            <button type="submit" class="btn btn-amber btn-block">
              Daftar Akun
            </button>
          </form>

          <div style="text-align: center; margin-top: 20px; font-size: 14px; color: var(--color-graphite);">
            Sudah punya akun? <a href="#/login" style="color: var(--color-teal); font-weight: 600;">Masuk</a>
          </div>
        </div>
      </div>
    `;

    document.getElementById('reg-form').addEventListener('submit', function (e) {
      e.preventDefault();
      window.AppState.isLoggedIn = true;
      window.location.hash = '#/';
      window.showToast('Akun berhasil dibuat');
    });
  }

  // --------------------------------------------------------------------------
  // L3. HOMEPAGE CONTROLLER
  // --------------------------------------------------------------------------
  function renderHome(container) {
    var items = window.RentfyData.items;
    var categories = window.RentfyData.categories;

    var nearbyItems = items.slice().sort(function (a, b) { return a.distanceKm - b.distanceKm; }).slice(0, 4);
    var popularItems = items.slice().sort(function (a, b) { return b.rating - a.rating; }).slice(0, 4);

    container.innerHTML = `
      <div class="container" style="padding-top: 36px;">
        <div style="margin-bottom: 24px;">
          <div style="font-size: 15px; font-weight: 600; color: var(--color-teal); margin-bottom: 4px;">
            Halo, ${window.RentfyData.user.name}
          </div>
          <h1 style="font-size: 36px; font-weight: 700; color: var(--color-carbon); letter-spacing: -0.5px;">
            Temukan barang yang ingin kamu sewa
          </h1>
        </div>

        <!-- Hygglo-Style Unified Search Bar (Referensi.md component) -->
        <div class="hero-search-container">
          <div class="search-slot slot-text">
            <span class="icon-svg" style="color: var(--color-smoke);">${Icons.search}</span>
            <input type="text" id="home-search-input" placeholder="Mau sewa apa? (kamera, tenda, bor, proyektor...)" value="${window.AppState.searchQuery}">
          </div>
          <div class="search-divider"></div>
          <div class="search-slot" id="home-open-loc">
            <span class="icon-svg" style="color: var(--color-teal);">${Icons.pin}</span>
            <div>
              <div class="slot-caption">Lokasi</div>
              <div class="slot-value">${window.AppState.selectedLocation}</div>
            </div>
          </div>
          <div class="search-divider"></div>
          <div class="search-slot" id="home-open-cal">
            <span class="icon-svg" style="color: var(--color-teal);">${Icons.calendar}</span>
            <div>
              <div class="slot-caption">Periode</div>
              <div class="slot-value">${window.AppState.selectedDates.start} (${window.AppState.selectedDates.days} hari)</div>
            </div>
          </div>
          <button class="search-dock-btn" id="home-search-action" title="Cari">
            <span class="icon-svg">${Icons.search}</span>
          </button>
        </div>

        <!-- Dark Promotional Banner (Referensi.md AI Director / Forest Stage Pattern) -->
        <div class="promo-stage-banner">
          <div>
            <h3>Jaminan Perlindungan Transaksi</h3>
            <p>Setiap transaksi di Rentfy dilindungi deposit keamanan dan verifikasi identitas resmi antara penyewa dan pemilik.</p>
          </div>
          <a href="#/how-it-works" class="btn btn-outline" style="background: transparent; color: #ffffff; border-color: rgba(255,255,255,0.4);">
            Pelajari Cara Kerja
          </a>
        </div>

        <!-- Section: Service Category Cards (Dark Forest Stage) -->
        <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 20px;">
          <div>
            <h2 style="font-size: 22px;">Kategori Pilihan</h2>
            <p style="font-size: 13px; color: var(--color-graphite); margin-top: 2px;">Sewa kebutuhan harian, hobi, dan pekerjaan dari pemilik terpercaya</p>
          </div>
        </div>

        <div class="category-cards-carousel">
          ${categories.map(function (c) {
            var iconHtml = Icons[c.iconType] || Icons.camera;
            return `
              <div class="service-category-card" data-cat="${c.id}">
                <div class="cat-title">${c.name}</div>
                <div class="cat-icon icon-svg">${iconHtml}</div>
              </div>
            `;
          }).join('')}
        </div>

        <!-- Section: Dekat kamu -->
        <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 20px;">
          <div>
            <h2 style="font-size: 22px;">Dekat kamu (${window.AppState.selectedLocation})</h2>
            <p style="font-size: 13px; color: var(--color-graphite); margin-top: 2px;">Urutan barang terdekat untuk kemudahan pengambilan fisik</p>
          </div>
          <a href="#/search" class="pill-tag" style="padding: 6px 14px; font-size: 13px;">
            Lihat Semua ${Icons.arrowRight}
          </a>
        </div>

        <div class="items-grid-4">
          ${nearbyItems.map(renderMarketplaceCard).join('')}
        </div>

        <!-- Feature Benefit Row (Referensi.md) -->
        <div class="benefit-row">
          <div class="benefit-item">
            <span class="icon-svg">${Icons.shield}</span>
            <div>
              <h4>Transaksi Terproteksi</h4>
              <p>Dana sewa ditahan aman oleh Rentfy sampai barang diterima dalam kondisi baik.</p>
            </div>
          </div>
          <div class="benefit-item">
            <span class="icon-svg">${Icons.pin}</span>
            <div>
              <h4>Lokasi Terverifikasi</h4>
              <p>Titik serah terima dan profil pemilik telah terverifikasi secara akurat.</p>
            </div>
          </div>
          <div class="benefit-item">
            <span class="icon-svg">${Icons.box}</span>
            <div>
              <h4>Jaminan Deposit Cair</h4>
              <p>Deposit penjamin otomatis dikembalikan 100% setelah barang selesai dicek.</p>
            </div>
          </div>
        </div>

        <!-- Section: Paling sering disewa -->
        <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 20px;">
          <div>
            <h2 style="font-size: 22px;">Paling sering disewa</h2>
            <p style="font-size: 13px; color: var(--color-graphite); margin-top: 2px;">Pilihan terpopuler dengan rating kepuasan tertinggi</p>
          </div>
          <a href="#/search" class="pill-tag" style="padding: 6px 14px; font-size: 13px;">
            Lihat Semua ${Icons.arrowRight}
          </a>
        </div>

        <div class="items-grid-4">
          ${popularItems.map(renderMarketplaceCard).join('')}
        </div>
      </div>
    `;

    // Events
    document.getElementById('home-open-loc').addEventListener('click', function () {
      openLocationModal(function () { renderHome(container); });
    });

    document.getElementById('home-open-cal').addEventListener('click', function () {
      openDateModal(function () { renderHome(container); });
    });

    function doHomeSearch() {
      var query = document.getElementById('home-search-input').value.trim();
      window.AppState.searchQuery = query || 'camera';
      if (!window.AppState.hasShownLocationModal) {
        window.AppState.hasShownLocationModal = true;
        openLocationModal(function () {
          window.location.hash = '#/search?q=' + encodeURIComponent(window.AppState.searchQuery);
        });
      } else {
        window.location.hash = '#/search?q=' + encodeURIComponent(window.AppState.searchQuery);
      }
    }

    document.getElementById('home-search-action').addEventListener('click', doHomeSearch);
    document.getElementById('home-search-input').addEventListener('keypress', function (e) {
      if (e.key === 'Enter') doHomeSearch();
    });

    container.querySelectorAll('.service-category-card').forEach(function (card) {
      card.addEventListener('click', function () {
        var cat = card.getAttribute('data-cat');
        window.location.hash = '#/search?cat=' + cat;
      });
    });

    bindCardEvents(container);
  }

  // --------------------------------------------------------------------------
  // ITEM CARD COMPONENT (Referensi.md 16px radius, soft shadow, badge)
  // --------------------------------------------------------------------------
  function renderMarketplaceCard(item) {
    var isSaved = window.AppState.savedItems.has(item.id);
    return `
      <div class="marketplace-card" data-id="${item.id}">
        <div class="card-media">
          <img src="${item.images[0]}" alt="${item.name}" loading="lazy">
          <button class="save-action-circle" data-id="${item.id}" title="Simpan">
            <span class="icon-svg">${isSaved ? Icons.heartFilled : Icons.heartOutline}</span>
          </button>
        </div>
        <div class="card-content">
          <div class="card-item-title">${item.name}</div>
          <div class="card-item-meta">
            <span class="meta-chip"><span class="icon-svg" style="color:var(--color-graphite);">${Icons.pin}</span> ${item.distance}</span>
            <span>•</span>
            <span class="meta-chip"><span class="icon-svg">${Icons.star}</span> ${item.rating}</span>
          </div>
          <div class="card-item-footer">
            <div class="item-price-rate">
              ${formatRp(item.pricePerDay)} <span>/ hari</span>
            </div>
            <span class="badge-status badge-teal">
              <span class="icon-svg">${Icons.check}</span> Terverifikasi
            </span>
          </div>
        </div>
      </div>
    `;
  }

  function bindCardEvents(scope) {
    scope.querySelectorAll('.marketplace-card').forEach(function (card) {
      card.addEventListener('click', function (e) {
        if (e.target.closest('.save-action-circle')) return;
        var id = card.getAttribute('data-id');
        window.location.hash = '#/item/' + id;
      });
    });

    scope.querySelectorAll('.save-action-circle').forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        e.stopPropagation();
        var id = parseInt(btn.getAttribute('data-id'), 10);
        if (window.AppState.savedItems.has(id)) {
          window.AppState.savedItems.delete(id);
          btn.innerHTML = `<span class="icon-svg">${Icons.heartOutline}</span>`;
          window.showToast('Dihapus dari simpanan');
        } else {
          window.AppState.savedItems.add(id);
          btn.innerHTML = `<span class="icon-svg">${Icons.heartFilled}</span>`;
          window.showToast('Disimpan ke favorit');
        }
      });
    });
  }

  // --------------------------------------------------------------------------
  // L4. LOCATION PICKER MODAL (Leaflet Map)
  // --------------------------------------------------------------------------
  function openLocationModal(onSelect) {
    var modal = document.createElement('div');
    modal.className = 'modal-backdrop';
    modal.innerHTML = `
      <div class="modal-card">
        <div class="modal-header-row">
          <h3 style="font-size: 18px;">Pilih Lokasi Sewa</h3>
          <button class="btn-ghost" id="loc-modal-close" style="font-size: 18px; font-weight: bold;">✕</button>
        </div>
        <div class="modal-content-area">
          <p style="font-size: 13px; color: var(--color-graphite); margin-bottom: 12px;">
            Tentukan area domisili kamu untuk menampilkan pemilik dan barang terdekat.
          </p>
          <div style="display: flex; gap: 8px; margin-bottom: 12px;">
            <input type="text" id="loc-input" class="input-field" value="${window.AppState.selectedLocation}">
            <button class="btn btn-outline" id="loc-curr-btn" style="white-space: nowrap;">
              <span class="icon-svg">${Icons.pin}</span> Lokasi Saya
            </button>
          </div>

          <div id="loc-leaflet-map" class="leaflet-map-element"></div>
          <div style="font-size: 12px; color: var(--color-smoke); text-align: center;">Geser peta untuk memilih titik serah terima</div>

          <div style="margin-top: 16px;">
            <div style="font-size: 12px; font-weight: 600; color: var(--color-slate); margin-bottom: 8px;">Pilihan Area:</div>
            <div style="display: flex; flex-wrap: wrap; gap: 8px;">
              ${window.RentfyData.areas.map(function (a) {
                var isActive = a === window.AppState.selectedLocation;
                return `<button class="pill-tag pill-neutral ${isActive ? 'active' : ''} area-choice-btn" data-area="${a}">${a}</button>`;
              }).join('')}
            </div>
          </div>
        </div>
        <div class="modal-footer-row">
          <button class="btn btn-amber btn-block" id="loc-confirm-btn">
            Pakai Lokasi Ini
          </button>
        </div>
      </div>
    `;

    document.body.appendChild(modal);

    var mapEl = document.getElementById('loc-leaflet-map');
    var center = [-6.2615, 106.8106];
    var map = L.map(mapEl, { attributionControl: false }).setView(center, 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
    var marker = L.marker(center, { draggable: true }).addTo(map);
    mapInstances.push(map);

    setTimeout(function () { map.invalidateSize(); }, 200);

    marker.on('dragend', function () {
      window.showToast('Titik koordinat diperbarui');
    });

    document.getElementById('loc-curr-btn').addEventListener('click', function () {
      map.setView(center, 14);
      marker.setLatLng(center);
      document.getElementById('loc-input').value = 'Jakarta Selatan';
      window.showToast('Lokasi diatur ke Jakarta Selatan');
    });

    modal.querySelectorAll('.area-choice-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var area = btn.getAttribute('data-area');
        document.getElementById('loc-input').value = area;
        modal.querySelectorAll('.area-choice-btn').forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');
      });
    });

    function close() {
      try { map.remove(); } catch (e) {}
      modal.remove();
    }

    document.getElementById('loc-modal-close').addEventListener('click', close);
    document.getElementById('loc-confirm-btn').addEventListener('click', function () {
      window.AppState.selectedLocation = document.getElementById('loc-input').value || 'Jakarta Selatan';
      close();
      if (onSelect) onSelect();
    });
  }

  // --------------------------------------------------------------------------
  // INTERACTIVE CALENDAR MODAL (Minimal 2 Hari Kalender)
  // --------------------------------------------------------------------------
  function openDateModal(onSelect) {
    var modal = document.createElement('div');
    modal.className = 'modal-backdrop';

    var currentDates = window.AppState.selectedDates;
    var startDay = currentDates.startNum || parseInt(currentDates.start, 10) || 17;
    var endDay = currentDates.endNum || parseInt(currentDates.end, 10) || 18;

    function renderCalendarGrid() {
      var daysHtml = '';
      // Nov 1, 2026 is Sunday, so 6 leading blanks for Mon-Sat
      for (var b = 0; b < 6; b++) {
        daysHtml += '<div class="cal-day-cell empty"></div>';
      }

      for (var d = 1; d <= 30; d++) {
        var isStart = (d === startDay);
        var isEnd = (d === endDay);
        var inRange = (d > startDay && d < endDay);

        var cls = 'cal-day-cell';
        if (isStart) cls += ' selected-start';
        if (isEnd) cls += ' selected-end';
        if (inRange) cls += ' in-range';

        daysHtml += '<div class="' + cls + '" data-day="' + d + '">' + d + '</div>';
      }

      var dur = (endDay - startDay) + 1;

      return `
        <div class="modal-card" style="max-width: 500px;">
          <div class="modal-header-row">
            <div>
              <h3 style="font-size: 18px; margin-bottom: 2px;">Pilih Periode Sewa</h3>
              <div style="font-size: 12px; color: var(--color-smoke);">Minimal sewa 2 hari kalender • Dihitung per hari kalender</div>
            </div>
            <button class="btn-ghost" id="date-close-btn" style="font-size: 18px; font-weight: bold;">✕</button>
          </div>

          <div class="modal-content-area">
            <!-- Calendar Grid Container -->
            <div class="calendar-widget">
              <div class="calendar-header">
                <button class="cal-nav-btn" id="cal-prev" title="Bulan Sebelumnya">
                  <span class="icon-svg">${Icons.arrowLeft}</span>
                </button>
                <div class="calendar-month-title">November 2026</div>
                <button class="cal-nav-btn" id="cal-next" title="Bulan Berikutnya">
                  <span class="icon-svg">${Icons.arrowRight}</span>
                </button>
              </div>

              <div class="cal-weekdays">
                <span>Sen</span>
                <span>Sel</span>
                <span>Rab</span>
                <span>Kam</span>
                <span>Jum</span>
                <span>Sab</span>
                <span>Min</span>
              </div>

              <div class="cal-days-grid" id="cal-grid">
                ${daysHtml}
              </div>
            </div>

            <!-- Quick Duration Presets -->
            <div style="margin-top: 14px;">
              <div style="font-size: 12px; font-weight: 600; color: var(--color-slate); margin-bottom: 8px;">Pilihan Cepat:</div>
              <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                <button class="pill-tag pill-neutral ${dur === 2 && startDay === 17 ? 'active' : ''}" data-preset="2">2 Hari (17 - 18 Nov)</button>
                <button class="pill-tag pill-neutral ${dur === 3 && startDay === 17 ? 'active' : ''}" data-preset="3">3 Hari (17 - 19 Nov)</button>
                <button class="pill-tag pill-neutral ${dur === 7 && startDay === 17 ? 'active' : ''}" data-preset="7">1 Minggu (17 - 23 Nov)</button>
                <button class="pill-tag pill-neutral ${dur === 14 && startDay === 17 ? 'active' : ''}" data-preset="14">2 Minggu (17 - 30 Nov)</button>
              </div>
            </div>

            <!-- Selected Summary Box -->
            <div class="cal-summary-box">
              <div>
                <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: var(--color-smoke); margin-bottom: 2px;">Tanggal Ambil</div>
                <div style="font-size: 14px; font-weight: 700; color: var(--color-teal);">${startDay} Nov 2026</div>
              </div>
              <div>
                <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: var(--color-smoke); margin-bottom: 2px;">Tanggal Kembali</div>
                <div style="font-size: 14px; font-weight: 700; color: var(--color-teal);">${endDay} Nov 2026 (${dur} Hari)</div>
              </div>
            </div>
          </div>

          <div class="modal-footer-row" style="display: flex; justify-content: space-between; align-items: center;">
            <button class="btn btn-ghost" id="date-reset-btn" style="font-size: 13px;">Hapus Tanggal</button>
            <button class="btn btn-amber" id="date-apply-btn" style="padding: 10px 24px;">
              Terapkan Jadwal (${dur} Hari)
            </button>
          </div>
        </div>
      `;
    }

    function updateModal() {
      modal.innerHTML = renderCalendarGrid();
      bindModalEvents();
    }

    function bindModalEvents() {
      var closeBtn = modal.querySelector('#date-close-btn');
      if (closeBtn) {
        closeBtn.addEventListener('click', function () {
          modal.remove();
        });
      }

      // Close on backdrop click
      modal.onclick = function (e) {
        if (e.target === modal) {
          modal.remove();
        }
      };

      // Day Click Logic
      var dayCells = modal.querySelectorAll('.cal-day-cell[data-day]');
      dayCells.forEach(function (cell) {
        cell.addEventListener('click', function (e) {
          e.stopPropagation();
          var d = parseInt(cell.getAttribute('data-day'), 10);
          if (d >= endDay || d === startDay) {
            if (d === startDay) {
              endDay = Math.min(30, startDay + 1);
            } else {
              endDay = d;
            }
          } else if (d < startDay) {
            startDay = d;
            if (endDay <= startDay) {
              endDay = Math.min(30, startDay + 1);
            }
          } else {
            endDay = d;
          }

          if (endDay <= startDay) {
            endDay = Math.min(30, startDay + 1);
          }

          updateModal();
        });
      });

      // Preset buttons
      modal.querySelectorAll('[data-preset]').forEach(function (btn) {
        btn.addEventListener('click', function (e) {
          e.stopPropagation();
          var p = parseInt(btn.getAttribute('data-preset'), 10);
          startDay = 17;
          endDay = Math.min(30, startDay + p - 1);
          updateModal();
        });
      });

      var prevBtn = modal.querySelector('#cal-prev');
      if (prevBtn) {
        prevBtn.addEventListener('click', function (e) {
          e.stopPropagation();
          window.showToast('Menampilkan bulan November 2026 (aktif)');
        });
      }

      var nextBtn = modal.querySelector('#cal-next');
      if (nextBtn) {
        nextBtn.addEventListener('click', function (e) {
          e.stopPropagation();
          window.showToast('Hanya bulan November 2026 yang tersedia di versi demo');
        });
      }

      var resetBtn = modal.querySelector('#date-reset-btn');
      if (resetBtn) {
        resetBtn.addEventListener('click', function (e) {
          e.stopPropagation();
          startDay = 17;
          endDay = 18;
          updateModal();
        });
      }

      var applyBtn = modal.querySelector('#date-apply-btn');
      if (applyBtn) {
        applyBtn.addEventListener('click', function (e) {
          e.stopPropagation();
          var daysCount = (endDay - startDay) + 1;
          window.AppState.selectedDates = {
            start: startDay + ' Nov',
            end: endDay + ' Nov',
            days: daysCount,
            startNum: startDay,
            endNum: endDay
          };

          modal.remove();
          window.showToast('Jadwal sewa diterapkan: ' + startDay + ' - ' + endDay + ' Nov (' + daysCount + ' hari)');
          if (onSelect) onSelect();
        });
      }
    }

    // Append to document FIRST, then render & bind
    document.body.appendChild(modal);
    updateModal();
  }

  // --------------------------------------------------------------------------
  // L5. SEARCH RESULTS CONTROLLER
  // --------------------------------------------------------------------------
  function renderSearch(container, hash) {
    var params = new URLSearchParams(hash.split('?')[1] || '');
    var query = params.get('q') || window.AppState.searchQuery || '';
    var catParam = params.get('cat') || window.AppState.activeCategory;

    var items = window.RentfyData.items.slice();

    if (catParam) {
      items = items.filter(function (it) { return it.category === catParam; });
    } else if (query) {
      var q = query.toLowerCase();
      items = items.filter(function (it) {
        return it.name.toLowerCase().indexOf(q) !== -1 ||
               it.category.toLowerCase().indexOf(q) !== -1 ||
               it.subcategory.toLowerCase().indexOf(q) !== -1;
      });
    }

    if (window.AppState.activeSort === 'termurah') {
      items.sort(function (a, b) { return a.pricePerDay - b.pricePerDay; });
    } else if (window.AppState.activeSort === 'rating') {
      items.sort(function (a, b) { return b.rating - a.rating; });
    } else {
      items.sort(function (a, b) { return a.distanceKm - b.distanceKm; });
    }

    var title = catParam 
      ? 'Kategori: ' + (window.RentfyData.categories.find(function (c) { return c.id === catParam; }) || {}).name
      : 'Hasil untuk "' + (query || 'Semua barang') + '"';

    container.innerHTML = `
      <div style="background: #ffffff; border-bottom: 1px solid var(--color-mist); padding: 24px 0 16px; margin-bottom: 24px;">
        <div class="container">
          <!-- In-Page Search Bar for Category Screen (L5) -->
          <div class="hero-search-container" style="margin-bottom: 16px;">
            <div class="search-slot slot-text">
              <span class="icon-svg" style="color: var(--color-smoke);">${Icons.search}</span>
              <input type="text" id="search-input-field" placeholder="Cari di kategori ini..." value="${query}">
            </div>
            <div class="search-divider"></div>
            <div class="search-slot" id="search-loc-trigger">
              <span class="icon-svg" style="color: var(--color-teal);">${Icons.pin}</span>
              <div>
                <div class="slot-caption">Lokasi</div>
                <div class="slot-value">${window.AppState.selectedLocation}</div>
              </div>
            </div>
            <div class="search-divider"></div>
            <div class="search-slot" id="search-cal-trigger">
              <span class="icon-svg" style="color: var(--color-teal);">${Icons.calendar}</span>
              <div>
                <div class="slot-caption">Periode</div>
                <div class="slot-value">${window.AppState.selectedDates.start} (${window.AppState.selectedDates.days} hari)</div>
              </div>
            </div>
            <button class="search-dock-btn" id="search-action-btn" title="Cari">
              <span class="icon-svg">${Icons.search}</span>
            </button>
          </div>

          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
            <div>
              <h2 style="font-size: 22px; margin-bottom: 4px;">${title}</h2>
              <p style="font-size: 13px; color: var(--color-graphite);">
                Tersedia <strong>${items.length}</strong> unit sewa di ${window.AppState.selectedLocation}
              </p>
            </div>
            <button class="btn btn-outline" id="filter-btn">
              <span class="icon-svg">${Icons.filter}</span> Filter
            </button>
          </div>

          <!-- Sort and Toggle View -->
          <div style="display: flex; align-items: center; justify-content: space-between;">
            <div style="display: flex; align-items: center; gap: 8px;">
              <span style="font-size: 13px; color: var(--color-smoke); font-weight: 600;">Urutan:</span>
              <button class="pill-tag pill-neutral ${window.AppState.activeSort === 'terdekat' ? 'active' : ''}" data-sort="terdekat">Terdekat</button>
              <button class="pill-tag pill-neutral ${window.AppState.activeSort === 'termurah' ? 'active' : ''}" data-sort="termurah">Termurah</button>
              <button class="pill-tag pill-neutral ${window.AppState.activeSort === 'rating' ? 'active' : ''}" data-sort="rating">Rating Tertinggi</button>
            </div>
            <div style="display: flex; border: 1px solid var(--color-mist); border-radius: var(--radius-pills); overflow: hidden; background: #ffffff;">
              <button id="view-list-btn" style="padding: 6px 16px; font-size: 13px; font-weight: 600; ${window.AppState.activeView === 'daftar' ? 'background:var(--color-teal); color:#ffffff;' : 'color:var(--color-slate);'}">
                Daftar
              </button>
              <button id="view-map-btn" style="padding: 6px 16px; font-size: 13px; font-weight: 600; ${window.AppState.activeView === 'peta' ? 'background:var(--color-teal); color:#ffffff;' : 'color:var(--color-slate);'}">
                Peta
              </button>
            </div>
          </div>
        </div>
      </div>

      <div class="container">
        <!-- Interactive Map Container -->
        <div id="search-map-wrap" style="display: ${window.AppState.activeView === 'peta' ? 'block' : 'none'}; margin-bottom: 24px;">
          <div id="search-map-el" class="leaflet-map-element" style="height: 420px; border-radius: var(--radius-cards);"></div>
        </div>

        <!-- Cards Grid -->
        ${items.length === 0 ? `
          <div style="text-align: center; padding: 60px 20px; background: #ffffff; border-radius: var(--radius-cards); border: 1px solid var(--color-mist);">
            <div class="icon-svg" style="color: var(--color-smoke); margin-bottom: 12px;">${Icons.box}</div>
            <h3 style="margin-bottom: 8px;">Belum ada barang untuk pencarian ini</h3>
            <p style="color: var(--color-graphite); margin-bottom: 20px;">Coba gunakan kata kunci lain seperti kamera atau tenda.</p>
            <a href="#/search?q=kamera" class="btn btn-amber">Lihat Semua Kamera</a>
          </div>
        ` : `
          <div class="items-grid-4">
            ${items.map(renderMarketplaceCard).join('')}
          </div>
        `}
      </div>
    `;

    if (window.AppState.activeView === 'peta' && items.length > 0) {
      setTimeout(function () {
        var mapEl = document.getElementById('search-map-el');
        if (mapEl) {
          var map = L.map(mapEl, { attributionControl: false }).setView([-6.25, 106.80], 12);
          L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
          items.forEach(function (it) {
            var marker = L.marker([it.lat, it.lng]).addTo(map);
            marker.bindPopup(`
              <div style="font-size: 13px; font-weight: 600; margin-bottom: 4px;">${it.name}</div>
              <div style="color: var(--color-teal); font-weight: 700;">${formatRp(it.pricePerDay)} / hari</div>
              <a href="#/item/${it.id}" style="color: var(--color-amber); font-size: 12px; display: inline-block; margin-top: 4px;">Lihat Unit</a>
            `);
          });
          mapInstances.push(map);
        }
      }, 150);
    }

    document.getElementById('view-list-btn').addEventListener('click', function () {
      window.AppState.activeView = 'daftar';
      renderSearch(container, hash);
    });

    document.getElementById('view-map-btn').addEventListener('click', function () {
      window.AppState.activeView = 'peta';
      renderSearch(container, hash);
    });

    container.querySelectorAll('[data-sort]').forEach(function (chip) {
      chip.addEventListener('click', function () {
        window.AppState.activeSort = chip.getAttribute('data-sort');
        renderSearch(container, hash);
      });
    });

    document.getElementById('search-loc-trigger').addEventListener('click', function () {
      openLocationModal(function () { renderSearch(container, hash); });
    });

    document.getElementById('search-cal-trigger').addEventListener('click', function () {
      openDateModal(function () { renderSearch(container, hash); });
    });

    function doCategorySearch() {
      var val = document.getElementById('search-input-field').value.trim();
      window.location.hash = '#/search?q=' + encodeURIComponent(val);
    }
    document.getElementById('search-action-btn').addEventListener('click', doCategorySearch);
    document.getElementById('search-input-field').addEventListener('keypress', function (e) {
      if (e.key === 'Enter') doCategorySearch();
    });

    document.getElementById('filter-btn').addEventListener('click', function () {
      openFilterModal(function () { renderSearch(container, hash); });
    });

    bindCardEvents(container);
  }

  // --------------------------------------------------------------------------
  // L6. ITEM DETAIL CONTROLLER (2-Column Desktop Spec)
  // --------------------------------------------------------------------------
  function renderItemDetail(container, itemId) {
    var item = window.RentfyData.items.find(function (it) { return it.id === itemId; }) || window.RentfyData.items[0];
    window.AppState.selectedItem = item;

    var owner = window.RentfyData.owner;
    var pricing = window.RentfyData.calcPrice(item.pricePerDay, window.AppState.selectedDates.days);
    var isSaved = window.AppState.savedItems.has(item.id);
    var similarItems = window.RentfyData.items.filter(function (it) {
      return it.category === item.category && it.id !== item.id;
    }).slice(0, 4);

    container.innerHTML = `
      <div class="container">
        <div style="padding: 16px 0;">
          <a href="#/search" style="font-size: 14px; color: var(--color-graphite); display: inline-flex; align-items: center; gap: 6px;">
            <span class="icon-svg">${Icons.arrowLeft}</span> Kembali ke Hasil Pencarian
          </a>
        </div>

        <div class="detail-grid-layout">
          <!-- Left Column: Content -->
          <div>
            <!-- Gallery -->
            <div class="detail-gallery">
              <div class="gallery-primary">
                <img id="detail-img-preview" src="${item.images[0]}" alt="${item.name}">
              </div>
              <div class="gallery-thumbs-row">
                ${item.images.map(function (img, idx) {
                  return `
                    <div class="thumb-box ${idx === 0 ? 'active' : ''}" data-src="${img}">
                      <img src="${img}" alt="Thumbnail">
                    </div>
                  `;
                }).join('')}
              </div>
            </div>

            <!-- Title & Meta -->
            <div class="detail-block">
              <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 16px;">
                <h1 style="font-size: 28px; font-weight: 700; color: var(--color-carbon);">${item.name}</h1>
                <button class="save-action-circle" style="position: static;" id="detail-save-trigger">
                  <span class="icon-svg">${isSaved ? Icons.heartFilled : Icons.heartOutline}</span>
                </button>
              </div>
              <div style="display: flex; align-items: center; gap: 16px; color: var(--color-graphite); font-size: 14px; margin-top: 10px;">
                <span class="meta-chip"><span class="icon-svg">${Icons.pin}</span> ${item.locationName} (${item.distance})</span>
                <span>•</span>
                <span class="meta-chip"><span class="icon-svg">${Icons.star}</span> ${item.rating} (${item.reviewsCount} ulasan)</span>
                <span>•</span>
                <span class="badge-status badge-teal"><span class="icon-svg">${Icons.check}</span> Terverifikasi</span>
              </div>
            </div>

            <!-- Owner Card -->
            <div class="owner-card-box">
              <div class="owner-info-flex">
                <div class="owner-avatar-circle">${owner.avatar}</div>
                <div>
                  <div style="font-weight: 700; font-size: 15px;">
                    ${owner.name} <span class="badge-status badge-teal" style="font-size: 11px;">Pemilik Terverifikasi</span>
                  </div>
                  <div style="font-size: 13px; color: var(--color-smoke); margin-top: 2px;">
                    ${owner.responseTime} • ⭐ ${owner.rating} (${owner.reviews} transaksi)
                  </div>
                </div>
              </div>
              <a href="#/chat" class="btn btn-outline" style="font-size: 13px;">
                <span class="icon-svg">${Icons.message}</span> Kirim Pesan
              </a>
            </div>

            <!-- Protection Banner -->
            <div style="background: var(--color-teal-light); border: 1px solid #b2ddde; border-radius: var(--radius-cards); padding: 18px 24px; margin-bottom: 24px; display: flex; align-items: center; gap: 14px;">
              <span class="icon-svg" style="color: var(--color-teal);">${Icons.shield}</span>
              <div>
                <div style="font-weight: 600; color: var(--color-teal); font-size: 14px;">Barang dilindungi jaminan keamanan</div>
                <div style="color: var(--color-forest-stage); font-size: 13px;">Biaya perlindungan Rp10.000 sudah termasuk dalam rincian pesanan.</div>
              </div>
            </div>

            <!-- Description & Packages -->
            <div class="detail-block">
              <h3 style="font-size: 18px; margin-bottom: 12px;">Deskripsi Barang</h3>
              <p style="font-size: 14px; color: var(--color-slate); line-height: 1.7; margin-bottom: 20px;">
                ${item.description}
              </p>

              <h4 style="font-size: 15px; margin-bottom: 10px;">Kelengkapan Isi Paket:</h4>
              <ul style="list-style: none; display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                ${item.packageContents.map(function (pkg) {
                  return `<li style="display:flex; align-items:center; gap:8px; font-size:14px; color:var(--color-slate);"><span class="icon-svg" style="color:var(--color-teal);">${Icons.check}</span> ${pkg}</li>`;
                }).join('')}
              </ul>

              <div style="margin-top: 20px; background: #f8fafc; border: 1px solid var(--color-mist); padding: 16px; border-radius: var(--radius-inputs);">
                <div style="font-size: 13px; font-weight: 600; color: var(--color-carbon); margin-bottom: 4px;">Catatan Kondisi Barang:</div>
                <div style="font-size: 13px; color: var(--color-graphite);">${item.condition}</div>
              </div>
            </div>

            <!-- Deposit & Cancellation Policy -->
            <div class="detail-block">
              <h3 style="font-size: 18px; margin-bottom: 14px;">Ketentuan Sewa & Deposit</h3>
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                <div style="background: #f8fafc; padding: 18px; border-radius: var(--radius-inputs); border: 1px solid var(--color-mist);">
                  <div style="font-weight: 600; font-size: 14px; margin-bottom: 4px;">Deposit Jaminan: ${formatRp(item.deposit)}</div>
                  <p style="font-size: 12px; color: var(--color-graphite); line-height: 1.5;">
                    Deposit dikembalikan penuh setelah barang diserahterimakan dan dicek kelengkapannya.
                  </p>
                </div>
                <div style="background: #f8fafc; padding: 18px; border-radius: var(--radius-inputs); border: 1px solid var(--color-mist);">
                  <div style="font-weight: 600; font-size: 14px; margin-bottom: 4px;">Kebijakan Pembatalan</div>
                  <p style="font-size: 12px; color: var(--color-graphite); line-height: 1.5;">
                    Gratis pembatalan sampai 2 hari sebelum masa sewa dimulai.
                  </p>
                </div>
              </div>
            </div>

            <!-- Approximate Map (Circle radius per spec) -->
            <div class="detail-block">
              <h3 style="font-size: 18px; margin-bottom: 4px;">Perkiraan Area Barang</h3>
              <p style="font-size: 13px; color: var(--color-smoke); margin-bottom: 12px;">
                Alamat pasti serah terima akan ditampilkan setelah pesanan diterima oleh pemilik.
              </p>
              <div id="detail-circle-map" class="leaflet-map-element"></div>
            </div>

            <!-- Reviews -->
            <div class="detail-block">
              <h3 style="font-size: 18px; margin-bottom: 16px;">Ulasan Penyewa (${item.reviewsCount})</h3>
              <div style="display: flex; flex-direction: column; gap: 16px;">
                ${window.RentfyData.sampleReviews.map(function (rev) {
                  return `
                    <div style="background: var(--color-paper); border: 1px solid var(--color-mist); padding: 18px; border-radius: var(--radius-inputs);">
                      <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                        <div style="display: flex; align-items: center; gap: 10px;">
                          <div style="width: 32px; height: 32px; border-radius: 50%; background: #e2e8f0; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 12px;">
                            ${rev.avatar}
                          </div>
                          <div style="font-weight: 600; font-size: 14px;">${rev.name}</div>
                        </div>
                        <div style="font-size: 12px; color: var(--color-smoke);">${rev.date}</div>
                      </div>
                      <div style="display: flex; gap: 2px; margin-bottom: 8px;">
                        ${Array(rev.rating).fill('<span class="icon-svg">' + Icons.star + '</span>').join('')}
                      </div>
                      <p style="font-size: 13px; color: var(--color-slate); line-height: 1.5;">${rev.text}</p>
                    </div>
                  `;
                }).join('')}
              </div>
            </div>

            <!-- Similar Items -->
            <div class="detail-block">
              <h3 style="font-size: 18px; margin-bottom: 16px;">Barang Serupa di Kategori Ini</h3>
              <div class="items-grid-4" style="grid-template-columns: repeat(2, 1fr);">
                ${similarItems.map(renderMarketplaceCard).join('')}
              </div>
            </div>
          </div>

          <!-- Right Column: Sticky Booking Widget -->
          <div class="sidebar-sticky-dock">
            <div class="booking-dock-card">
              <div class="booking-dock-price">
                ${formatRp(item.pricePerDay)} <span>/ hari</span>
              </div>
              <div style="font-size: 12px; color: var(--color-smoke); margin-bottom: 16px;">
                Minimal masa sewa 2 hari kalender
              </div>

              <div class="date-slot-card" id="detail-date-change-btn">
                <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: var(--color-smoke); margin-bottom: 4px;">
                  Periode Sewa
                </div>
                <div style="font-weight: 600; font-size: 14px; color: var(--color-carbon); display: flex; align-items: center; gap: 8px;">
                  <span class="icon-svg" style="color:var(--color-teal);">${Icons.calendar}</span>
                  ${window.AppState.selectedDates.start} - ${window.AppState.selectedDates.end} (${window.AppState.selectedDates.days} Hari)
                </div>
              </div>

              <!-- Cost breakdown -->
              <div style="margin: 20px 0;">
                <div class="cost-row">
                  <span>Sewa (${window.AppState.selectedDates.days} hari x ${formatRp(item.pricePerDay)})</span>
                  <span>${formatRp(pricing.sewa)}</span>
                </div>
                <div class="cost-row">
                  <span>Biaya Perlindungan Rentfy</span>
                  <span>${formatRp(pricing.perlindungan)}</span>
                </div>
                <div class="cost-row">
                  <span>Deposit (dikembalikan)</span>
                  <span>${formatRp(item.deposit)}</span>
                </div>
                <div class="cost-row cost-total">
                  <span>Perkiraan Total Bayar</span>
                  <span style="color: var(--color-teal); font-size: 18px;">${formatRp(pricing.sewa + pricing.perlindungan + item.deposit)}</span>
                </div>
              </div>

              <!-- ONE AMBER BUTTON PER SCREEN -->
              <button class="btn btn-amber btn-block" id="btn-request-rental" style="padding: 14px; font-size: 15px;">
                Ajukan Sewa
              </button>

              <div style="display: flex; gap: 8px; margin-top: 12px;">
                <a href="#/chat" class="btn btn-outline btn-block" style="font-size: 13px;">
                  <span class="icon-svg">${Icons.message}</span> Chat Pemilik
                </a>
              </div>

              <div style="font-size: 11px; color: var(--color-smoke); text-align: center; margin-top: 14px; line-height: 1.4;">
                Dana belum ditarik sampai pemilik menyetujui jadwal penyewaan.
              </div>
            </div>
          </div>
        </div>
      </div>
    `;

    // Leaflet Approximate Circle Map
    setTimeout(function () {
      var mapEl = document.getElementById('detail-circle-map');
      if (mapEl) {
        var map = L.map(mapEl, { attributionControl: false }).setView([item.lat, item.lng], 14);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
        L.circle([item.lat, item.lng], {
          color: '#0F5C63',
          fillColor: '#0F5C63',
          fillOpacity: 0.2,
          radius: 600
        }).addTo(map);
        mapInstances.push(map);
      }
    }, 150);

    // Gallery Thumbs
    container.querySelectorAll('.thumb-box').forEach(function (thumb) {
      thumb.addEventListener('click', function () {
        var src = thumb.getAttribute('data-src');
        document.getElementById('detail-img-preview').src = src;
        container.querySelectorAll('.thumb-box').forEach(function (t) { t.classList.remove('active'); });
        thumb.classList.add('active');
      });
    });

    // Save toggle
    document.getElementById('detail-save-trigger').addEventListener('click', function () {
      if (window.AppState.savedItems.has(item.id)) {
        window.AppState.savedItems.delete(item.id);
        this.innerHTML = `<span class="icon-svg">${Icons.heartOutline}</span>`;
        window.showToast('Dihapus dari simpanan');
      } else {
        window.AppState.savedItems.add(item.id);
        this.innerHTML = `<span class="icon-svg">${Icons.heartFilled}</span>`;
        window.showToast('Disimpan ke favorit');
      }
    });

    document.getElementById('detail-date-change-btn').addEventListener('click', function () {
      openDateModal(function () { renderItemDetail(container, itemId); });
    });

    document.getElementById('btn-request-rental').addEventListener('click', function () {
      window.AppState.currentOrder = {
        item: item,
        dates: window.AppState.selectedDates,
        pricing: window.RentfyData.calcPrice(item.pricePerDay, window.AppState.selectedDates.days),
        deposit: item.deposit,
        orderId: 'RF-' + Math.floor(100000 + Math.random() * 900000),
        createdAt: 'Hari ini'
      };
      window.location.hash = '#/checkout';
    });

    bindCardEvents(container);
  }

  // --------------------------------------------------------------------------
  // L7. CHECKOUT / RINGKASAN SEWA CONTROLLER
  // --------------------------------------------------------------------------
  function renderCheckout(container) {
    var order = window.AppState.currentOrder;
    if (!order) {
      window.location.hash = '#/';
      return;
    }

    var item = order.item;
    var totalCost = order.pricing.sewa + order.pricing.perlindungan + order.deposit;

    container.innerHTML = `
      <div class="step-card-centered">
        <div class="step-title-header">
          <h2 style="font-size: 22px;">Ringkasan Pengajuan Sewa</h2>
          <p style="font-size: 13px; color: var(--color-graphite); margin-top: 2px;">
            Pastikan detail barang dan jadwal sewa sudah sesuai sebelum mengirim permintaan.
          </p>
        </div>

        <div style="display: flex; gap: 16px; align-items: center; background: #f8fafc; padding: 16px; border-radius: var(--radius-inputs); margin-bottom: 24px;">
          <img src="${item.images[0]}" style="width: 80px; height: 60px; object-fit: cover; border-radius: 8px;">
          <div>
            <div style="font-weight: 700; font-size: 15px;">${item.name}</div>
            <div style="font-size: 13px; color: var(--color-smoke); margin-top: 4px; display: flex; align-items: center; gap: 6px;">
              <span class="icon-svg">${Icons.calendar}</span> ${order.dates.start} - ${order.dates.end} (${order.dates.days} hari)
            </div>
          </div>
        </div>

        <div style="margin-bottom: 20px;">
          <label style="display: block; font-size: 13px; font-weight: 600; margin-bottom: 6px; color: var(--color-slate);">
            Pesan untuk pemilik (${window.RentfyData.owner.name})
          </label>
          <textarea class="input-field" rows="3" placeholder="Contoh: Rencana serah terima pukul 10.00 pagi untuk dokumentasi event..."></textarea>
        </div>

        <div style="background: var(--color-paper); border: 1px solid var(--color-mist); padding: 20px; border-radius: var(--radius-inputs); margin-bottom: 24px;">
          <h4 style="font-size: 15px; margin-bottom: 12px;">Rincian Biaya</h4>
          <div class="cost-row">
            <span>Biaya Sewa (${order.dates.days} hari)</span>
            <span>${formatRp(order.pricing.sewa)}</span>
          </div>
          <div class="cost-row">
            <span>Biaya Perlindungan Barang</span>
            <span>${formatRp(order.pricing.perlindungan)}</span>
          </div>
          <div class="cost-row">
            <span>Deposit Jaminan (dikembalikan)</span>
            <span>${formatRp(order.deposit)}</span>
          </div>
          <div class="cost-row cost-total">
            <span>Total yang harus dibayar nanti</span>
            <span style="color: var(--color-teal); font-size: 18px;">${formatRp(totalCost)}</span>
          </div>
        </div>

        <div style="display: flex; align-items: flex-start; gap: 10px; margin-bottom: 24px;">
          <input type="checkbox" id="terms-chk" checked style="margin-top: 4px;">
          <label for="terms-chk" style="font-size: 13px; color: var(--color-slate); line-height: 1.4;">
            Saya setuju dengan syarat sewa Rentfy dan bersedia mengembalikan unit tepat waktu.
          </label>
        </div>

        <!-- 1 Amber Button -->
        <button class="btn btn-amber btn-block" id="btn-confirm-send" style="padding: 14px;">
          Kirim Permintaan Sewa
        </button>

        <div style="text-align: center; margin-top: 14px;">
          <a href="#/item/${item.id}" style="font-size: 13px; color: var(--color-graphite);">← Kembali ke detail</a>
        </div>
      </div>
    `;

    document.getElementById('btn-confirm-send').addEventListener('click', function () {
      window.AppState.orderStatus = 'menunggu';
      window.location.hash = '#/request-sent';

      // Auto update after 5s per spec: "Menunggu pemilik" -> "Permintaan diterima"
      setTimeout(function () {
        if (window.AppState.orderStatus === 'menunggu') {
          window.AppState.orderStatus = 'diterima';
          window.showToast('Permintaan sewa kamu telah diterima oleh pemilik');
        }
      }, 5000);
    });
  }

  // --------------------------------------------------------------------------
  // L8. REQUEST SENT SUCCESS CONTROLLER
  // --------------------------------------------------------------------------
  function renderRequestSent(container) {
    container.innerHTML = `
      <div class="step-card-centered" style="text-align: center; padding: 48px 32px;">
        <div style="width: 64px; height: 64px; border-radius: 50%; background: var(--color-success-bg); color: var(--color-success); display: flex; align-items: center; justify-content: center; margin: 0 auto 20px;">
          <span class="icon-svg" style="transform: scale(1.5);">${Icons.check}</span>
        </div>
        <h2 style="font-size: 24px; margin-bottom: 8px;">Permintaan Sewa Terkirim</h2>
        <p style="color: var(--color-graphite); font-size: 14px; max-width: 440px; margin: 0 auto 24px;">
          Pemilik akan merespons maksimal 24 jam. Kamu akan menerima pemberitahuan begitu permintaan disetujui.
        </p>

        <div style="background: #f8fafc; border: 1px solid var(--color-mist); padding: 14px; border-radius: var(--radius-buttons); margin-bottom: 32px; font-size: 13px; color: var(--color-slate);">
          Simulasi demo: Status pesanan otomatis disetujui dalam 5 detik.
        </div>

        <div style="display: flex; flex-direction: column; gap: 12px; max-width: 340px; margin: 0 auto;">
          <!-- 1 Amber CTA -->
          <a href="#/orders" class="btn btn-amber btn-block">
            Lihat Pesanan Saya
          </a>
          <a href="#/chat" class="btn btn-outline btn-block">
            <span class="icon-svg">${Icons.message}</span> Kirim Pesan ke Pemilik
          </a>
          <a href="#/" class="btn btn-ghost" style="font-size: 13px;">
            Kembali ke Beranda
          </a>
        </div>
      </div>
    `;
  }

  // --------------------------------------------------------------------------
  // L9. PESANAN SAYA CONTROLLER
  // --------------------------------------------------------------------------
  function renderOrders(container) {
    var order = window.AppState.currentOrder;
    var status = window.AppState.orderStatus;
    var activeTab = (status === 'selesai') ? 'selesai' : 'berjalan';

    container.innerHTML = `
      <div class="container" style="padding: 32px 0 60px;">
        <h1 style="font-size: 28px; margin-bottom: 24px;">Pesanan Saya</h1>

        <div style="display: flex; gap: 12px; border-bottom: 1px solid var(--color-mist); margin-bottom: 24px;">
          <button class="pill-tag pill-neutral ${activeTab === 'berjalan' ? 'active' : ''}" id="tab-run" style="border-radius: 8px 8px 0 0; border-bottom: none;">
            Sedang Berjalan
          </button>
          <button class="pill-tag pill-neutral ${activeTab === 'selesai' ? 'active' : ''}" id="tab-fin" style="border-radius: 8px 8px 0 0; border-bottom: none;">
            Selesai
          </button>
        </div>

        <div id="orders-list-box">
          ${activeTab === 'berjalan' && order ? renderActiveOrderCard(order, status) : ''}
          ${activeTab === 'berjalan' && !order ? `
            <div style="text-align: center; padding: 60px 20px; background: #ffffff; border-radius: var(--radius-cards); border: 1px solid var(--color-mist);">
              <div class="icon-svg" style="color: var(--color-smoke); margin-bottom: 12px;">${Icons.box}</div>
              <h3 style="margin-bottom: 8px;">Belum ada pesanan aktif</h3>
              <p style="color: var(--color-graphite); margin-bottom: 20px;">Temukan barang kebutuhanmu sekarang dari pemilik terdekat.</p>
              <a href="#/search" class="btn btn-amber">Cari Barang Sewa</a>
            </div>
          ` : ''}

          ${activeTab === 'selesai' && status === 'selesai' && order ? renderActiveOrderCard(order, 'selesai') : ''}
          ${activeTab === 'selesai' && status !== 'selesai' ? `
            <div style="text-align: center; padding: 60px 20px; background: #ffffff; border-radius: var(--radius-cards); border: 1px solid var(--color-mist);">
              <div class="icon-svg" style="color: var(--color-smoke); margin-bottom: 12px;">${Icons.check}</div>
              <h3 style="margin-bottom: 8px;">Belum ada pesanan selesai</h3>
              <p style="color: var(--color-graphite);">Pesanan yang sudah dikembalikan dan diverifikasi akan muncul di sini.</p>
            </div>
          ` : ''}
        </div>
      </div>
    `;

    document.getElementById('tab-run').addEventListener('click', function () {
      window.AppState.orderStatus = (window.AppState.orderStatus === 'selesai') ? 'diterima' : window.AppState.orderStatus;
      renderOrders(container);
    });

    document.getElementById('tab-fin').addEventListener('click', function () {
      renderOrders(container);
    });
  }

  function renderActiveOrderCard(order, status) {
    var statusLabels = {
      menunggu: { text: 'Menunggu Pemilik', badge: 'badge-amber', btn: 'Kirim Pesan', link: '#/chat' },
      diterima: { text: 'Permintaan Diterima', badge: 'badge-amber', btn: 'Verifikasi & Bayar', link: '#/verify' },
      siap_ambil: { text: 'Dana Ditahan, Siap Diambil', badge: 'badge-teal', btn: 'Lihat Cara Pengambilan', link: '#/pickup' },
      sedang_disewa: { text: 'Sedang Disewa', badge: 'badge-teal', btn: 'Lihat Masa Sewa', link: '#/renting' },
      pengecekan: { text: 'Menunggu Pengecekan', badge: 'badge-teal', btn: 'Lihat Status', link: '#/complete' },
      selesai: { text: 'Selesai', badge: 'badge-green', btn: 'Beri Ulasan', link: '#/complete' }
    };

    var s = statusLabels[status] || statusLabels.menunggu;
    var total = order.pricing.sewa + order.pricing.perlindungan + order.deposit;

    return `
      <div style="background: var(--color-paper); border: 1px solid var(--color-mist); border-radius: var(--radius-cards); padding: 24px; box-shadow: var(--shadow-sm); max-width: 760px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; border-bottom: 1px solid var(--color-mist); padding-bottom: 14px;">
          <div>
            <span style="font-size: 13px; color: var(--color-smoke);">No. Pesanan: <strong>${order.orderId}</strong></span>
          </div>
          <span class="badge-status ${s.badge}">${s.text}</span>
        </div>

        <div style="display: flex; gap: 20px; align-items: center;">
          <img src="${order.item.images[0]}" style="width: 100px; height: 75px; object-fit: cover; border-radius: var(--radius-inputs);">
          <div style="flex: 1;">
            <h3 style="font-size: 16px; margin-bottom: 4px;">${order.item.name}</h3>
            <div style="font-size: 13px; color: var(--color-graphite); margin-bottom: 6px; display: flex; align-items: center; gap: 6px;">
              <span class="icon-svg">${Icons.calendar}</span> ${order.dates.start} - ${order.dates.end} (${order.dates.days} hari)
            </div>
            <div style="font-size: 16px; font-weight: 700; color: var(--color-teal);">
              ${formatRp(total)}
            </div>
          </div>
        </div>

        <div style="display: flex; justify-content: flex-end; gap: 12px; margin-top: 20px; border-top: 1px solid #f1f5f9; padding-top: 16px;">
          <a href="#/order-detail" class="btn btn-outline" style="font-size: 13px;">Detail Pesanan</a>
          <a href="${s.link}" class="btn btn-amber" style="font-size: 13px;">${s.btn}</a>
        </div>
      </div>
    `;
  }

  // --------------------------------------------------------------------------
  // L10. CHAT CONTROLLER
  // --------------------------------------------------------------------------
  function renderChat(container) {
    var owner = window.RentfyData.owner;
    var order = window.AppState.currentOrder;

    container.innerHTML = `
      <div class="container" style="max-width: 760px; padding: 24px 0 60px;">
        <div style="background: #ffffff; border: 1px solid var(--color-mist); border-radius: var(--radius-cards); box-shadow: var(--shadow-md); overflow: hidden; display: flex; flex-direction: column; height: 70vh;">
          
          <!-- Header -->
          <div style="padding: 16px 20px; border-bottom: 1px solid var(--color-mist); display: flex; align-items: center; justify-content: space-between;">
            <div style="display: flex; align-items: center; gap: 12px;">
              <a href="#/orders" style="font-size: 16px; color: var(--color-slate);">${Icons.arrowLeft}</a>
              <div class="owner-avatar-circle" style="width: 38px; height: 38px; font-size: 14px;">${owner.avatar}</div>
              <div>
                <div style="font-weight: 700; font-size: 14px;">${owner.name} <span class="badge-status badge-teal" style="font-size: 10px;">Terverifikasi</span></div>
                <div style="font-size: 12px; color: var(--color-smoke);">${owner.responseTime}</div>
              </div>
            </div>
            <button class="btn btn-ghost" onclick="demoToast()">Hubungi</button>
          </div>

          <!-- Product Card Header -->
          ${order ? `
            <div style="background: #f8fafc; padding: 10px 20px; border-bottom: 1px solid var(--color-mist); display: flex; align-items: center; gap: 12px;">
              <img src="${order.item.images[0]}" style="width: 44px; height: 34px; object-fit: cover; border-radius: 4px;">
              <div style="flex: 1; font-size: 13px; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                ${order.item.name}
              </div>
              <div style="font-size: 13px; font-weight: 700; color: var(--color-teal);">
                ${formatRp(order.item.pricePerDay)}/hari
              </div>
            </div>
          ` : ''}

          <!-- Chat Messages Body -->
          <div id="chat-stream" style="flex: 1; overflow-y: auto; padding: 20px; display: flex; flex-direction: column; gap: 12px; background: #fafafa;">
            <div style="text-align: center; margin-bottom: 10px;">
              <span style="font-size: 11px; background: #e2e8f0; color: var(--color-slate); padding: 4px 12px; border-radius: var(--radius-pills);">
                Semua serah terima wajib dicatat di Rentfy demi keamanan
              </span>
            </div>

            ${window.AppState.messages.map(function (m) {
              var isMe = m.sender === 'LeBron James' || m.sender === 'LeBron';
              return `
                <div style="display: flex; justify-content: ${isMe ? 'flex-end' : 'flex-start'};">
                  <div style="max-width: 70%; background: ${isMe ? 'var(--color-teal)' : '#ffffff'}; color: ${isMe ? '#ffffff' : 'var(--color-carbon)'}; padding: 10px 16px; border-radius: var(--radius-inputs); box-shadow: var(--shadow-sm); font-size: 14px;">
                    <div>${m.text}</div>
                    <div style="font-size: 10px; text-align: right; opacity: 0.8; margin-top: 4px;">${m.time}</div>
                  </div>
                </div>
              `;
            }).join('')}
          </div>

          <!-- Quick replies chips -->
          <div style="display: flex; gap: 8px; padding: 8px 16px; background: #ffffff; border-top: 1px solid var(--color-mist); overflow-x: auto;">
            <button class="pill-tag pill-neutral" id="qr-1" style="font-size: 12px; padding: 4px 12px;">Apakah masih tersedia?</button>
            <button class="pill-tag pill-neutral" id="qr-2" style="font-size: 12px; padding: 4px 12px;">Boleh ambil jam berapa?</button>
            <button class="pill-tag pill-neutral" id="qr-3" style="font-size: 12px; padding: 4px 12px;">Bisa tambah 1 hari?</button>
          </div>

          <!-- Input row -->
          <div style="padding: 12px 16px; border-top: 1px solid var(--color-mist); display: flex; gap: 10px; background: #ffffff;">
            <input type="text" id="chat-input-text" class="input-field" placeholder="Ketik pesan..." style="border-radius: var(--radius-pills);">
            <!-- Carbon button for chat send -->
            <button class="btn btn-carbon" id="btn-chat-send" style="border-radius: var(--radius-pills); padding: 0 20px;">
              Kirim
            </button>
          </div>
        </div>
      </div>
    `;

    var listEl = document.getElementById('chat-stream');
    listEl.scrollTop = listEl.scrollHeight;

    function sendMsg(text) {
      if (!text) return;
      window.AppState.messages.push({ sender: 'LeBron James', text: text, time: 'Sekarang' });
      renderChat(container);

      setTimeout(function () {
        window.AppState.messages.push({
          sender: 'Dimas',
          text: 'Siap LeBron! Nanti kabari saja kalau sudah dekat titik serah terima ya.',
          time: 'Sekarang'
        });
        renderChat(container);
      }, 1500);
    }

    document.getElementById('btn-chat-send').addEventListener('click', function () {
      var val = document.getElementById('chat-input-text').value.trim();
      sendMsg(val);
    });

    document.getElementById('chat-input-text').addEventListener('keypress', function (e) {
      if (e.key === 'Enter') sendMsg(this.value.trim());
    });

    ['qr-1', 'qr-2', 'qr-3'].forEach(function (id) {
      var btn = document.getElementById(id);
      if (btn) btn.addEventListener('click', function () { sendMsg(btn.textContent); });
    });
  }

  // --------------------------------------------------------------------------
  // L11. ORDER DETAIL & TIMELINE CONTROLLER
  // --------------------------------------------------------------------------
  function renderOrderDetail(container) {
    var order = window.AppState.currentOrder;
    if (!order) {
      window.location.hash = '#/orders';
      return;
    }

    var status = window.AppState.orderStatus;
    var total = order.pricing.sewa + order.pricing.perlindungan + order.deposit;

    var steps = [
      { id: 'menunggu', title: 'Permintaan Terkirim', desc: 'Menunggu persetujuan pemilik barang' },
      { id: 'diterima', title: 'Permintaan Diterima', desc: 'Lakukan verifikasi KTP dan pembayaran' },
      { id: 'siap_ambil', title: 'Pembayaran Dikonfirmasi', desc: 'Dana ditahan aman di Rentfy' },
      { id: 'sedang_disewa', title: 'Barang Diambil & Disewa', desc: 'Penyewa mengonfirmasi penerimaan barang' },
      { id: 'selesai', title: 'Pengembalian & Selesai', desc: 'Barang dicek dan deposit dikembalikan' }
    ];

    var statusWeights = { menunggu: 1, diterima: 2, siap_ambil: 3, sedang_disewa: 4, pengecekan: 4, selesai: 5 };
    var currentWeight = statusWeights[status] || 1;

    container.innerHTML = `
      <div class="container" style="max-width: 760px; padding: 32px 0 60px;">
        <div style="margin-bottom: 20px;">
          <a href="#/orders" style="font-size: 14px; color: var(--color-graphite); display: inline-flex; align-items: center; gap: 6px;">
            <span class="icon-svg">${Icons.arrowLeft}</span> Kembali ke Pesanan
          </a>
        </div>

        <div style="background: #ffffff; border: 1px solid var(--color-mist); border-radius: var(--radius-cards); padding: 28px; box-shadow: var(--shadow-sm); margin-bottom: 24px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; border-bottom: 1px solid var(--color-mist); padding-bottom: 16px;">
            <div>
              <h2 style="font-size: 20px;">Pesanan #${order.orderId}</h2>
              <div style="font-size: 13px; color: var(--color-smoke); margin-top: 2px;">Dibuat ${order.createdAt}</div>
            </div>
            <span class="badge-status badge-teal">${status.toUpperCase()}</span>
          </div>

          <div style="display: flex; gap: 16px; align-items: center; background: #f8fafc; padding: 16px; border-radius: var(--radius-inputs); margin-bottom: 24px;">
            <img src="${order.item.images[0]}" style="width: 80px; height: 60px; object-fit: cover; border-radius: 8px;">
            <div>
              <div style="font-weight: 700; font-size: 15px;">${order.item.name}</div>
              <div style="font-size: 13px; color: var(--color-smoke); margin-top: 4px; display: flex; align-items: center; gap: 6px;">
                <span class="icon-svg">${Icons.calendar}</span> ${order.dates.start} - ${order.dates.end} (${order.dates.days} hari)
              </div>
            </div>
          </div>

          <!-- Timeline -->
          <h4 style="font-size: 16px; margin-bottom: 12px;">Garis Waktu Transaksi</h4>
          <div class="timeline-track">
            ${steps.map(function (st, idx) {
              var stepWeight = idx + 1;
              var isDone = stepWeight < currentWeight;
              var isActive = stepWeight === currentWeight;
              return `
                <div class="track-step ${isDone ? 'done' : ''} ${isActive ? 'active' : ''}">
                  <div class="track-dot">
                    ${isDone ? Icons.check : (idx + 1)}
                  </div>
                  <div style="font-weight: 600; font-size: 14px;">${st.title}</div>
                  <div style="font-size: 13px; color: var(--color-smoke);">${st.desc}</div>
                </div>
              `;
            }).join('')}
          </div>

          <!-- Cost Breakdown -->
          <div style="border-top: 1px solid var(--color-mist); padding-top: 20px; margin-top: 24px;">
            <h4 style="font-size: 15px; margin-bottom: 12px;">Rincian Pembayaran</h4>
            <div class="cost-row">
              <span>Sewa (${order.dates.days} hari)</span>
              <span>${formatRp(order.pricing.sewa)}</span>
            </div>
            <div class="cost-row">
              <span>Perlindungan Barang</span>
              <span>${formatRp(order.pricing.perlindungan)}</span>
            </div>
            <div class="cost-row">
              <span>Deposit Keamanan</span>
              <span>${formatRp(order.deposit)}</span>
            </div>
            <div class="cost-row cost-total">
              <span>Total Pembayaran</span>
              <span style="color: var(--color-teal);">${formatRp(total)}</span>
            </div>
          </div>

          <!-- Single Amber Action per Screen -->
          <div style="margin-top: 28px; display: flex; justify-content: flex-end; gap: 12px;">
            <a href="#/chat" class="btn btn-outline">
              <span class="icon-svg">${Icons.message}</span> Chat Pemilik
            </a>
            ${status === 'diterima' ? `<a href="#/verify" class="btn btn-amber">Verifikasi & Bayar Sekarang</a>` : ''}
            ${status === 'siap_ambil' ? `<a href="#/pickup" class="btn btn-amber">Lihat Cara Pengambilan</a>` : ''}
            ${status === 'sedang_disewa' ? `<a href="#/renting" class="btn btn-amber">Kelola Masa Sewa</a>` : ''}
            ${status === 'pengecekan' ? `<a href="#/complete" class="btn btn-amber">Lihat Status Pengembalian</a>` : ''}
            ${status === 'selesai' ? `<a href="#/complete" class="btn btn-amber">Beri Ulasan</a>` : ''}
          </div>
        </div>
      </div>
    `;
  }

  // --------------------------------------------------------------------------
  // L12. VERIFIKASI KTP CONTROLLER (Tahap 3)
  // --------------------------------------------------------------------------
  function renderVerify(container) {
    var step = window.AppState.verifyStep;

    container.innerHTML = `
      <div class="step-card-centered">
        <div class="step-title-header">
          <span class="badge-status badge-teal" style="margin-bottom: 8px;">Langkah ${step} dari 3</span>
          <h2 style="font-size: 22px;">Verifikasi Identitas Penyewa</h2>
          <p style="font-size: 13px; color: var(--color-graphite); margin-top: 2px;">
            Verifikasi identitas dilakukan demi keamanan bersama sebelum pembayaran diproses.
          </p>
        </div>

        ${step === 1 ? `
          <div style="text-align: center; margin-bottom: 24px;">
            <div style="width: 100%; aspect-ratio: 16/10; border: 2px dashed var(--color-teal); border-radius: var(--radius-cards); background: #f0fdf4; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 10px; padding: 20px;">
              <span class="icon-svg" style="color:var(--color-teal);">${Icons.idCard}</span>
              <div style="font-weight: 600; font-size: 15px;">Arahkan Sisi Depan e-KTP</div>
              <div style="font-size: 12px; color: var(--color-smoke);">Pastikan NIK, Foto, dan Alamat terbaca jelas tanpa pantulan</div>
            </div>
          </div>
        ` : step === 2 ? `
          <div style="text-align: center; margin-bottom: 24px;">
            <div style="width: 100%; aspect-ratio: 16/10; border: 2px dashed var(--color-teal); border-radius: var(--radius-cards); background: #f0fdf4; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 10px; padding: 20px;">
              <span class="icon-svg" style="color:var(--color-teal); transform: scale(1.5);">${Icons.camera}</span>
              <div style="font-weight: 600; font-size: 15px;">Selfie Bersama e-KTP</div>
              <div style="font-size: 12px; color: var(--color-smoke);">Pegang KTP di samping wajah dengan pencahayaan cukup</div>
            </div>
          </div>
        ` : `
          <div style="background: #f8fafc; padding: 20px; border-radius: var(--radius-inputs); border: 1px solid var(--color-mist); margin-bottom: 24px;">
            <h4 style="font-size: 15px; margin-bottom: 8px;">Tinjau Data Identitas</h4>
            <div style="font-size: 13px; color: var(--color-slate); line-height: 1.8;">
              <div>Nama: <strong>LeBron James</strong></div>
              <div>NIK: <strong>3174**********01</strong></div>
              <div>Status: <span class="badge-status badge-green"><span class="icon-svg">${Icons.check}</span> Dokumen Valid</span></div>
            </div>
          </div>
        `}

        <div style="background: var(--color-teal-light); padding: 12px 16px; border-radius: var(--radius-buttons); font-size: 12px; color: var(--color-forest-stage); margin-bottom: 24px; display: flex; align-items: center; gap: 8px;">
          <span class="icon-svg" style="color: var(--color-teal);">${Icons.shield}</span>
          Data identitas dienkripsi dan hanya dipakai untuk verifikasi keamanan sewa.
        </div>

        <!-- 1 Amber CTA -->
        <button class="btn btn-amber btn-block" id="verify-next-btn">
          ${step < 3 ? 'Ambil Foto & Lanjutkan' : 'Kirim untuk Ditinjau'}
        </button>
      </div>
    `;

    document.getElementById('verify-next-btn').addEventListener('click', function () {
      if (window.AppState.verifyStep < 3) {
        window.AppState.verifyStep++;
        renderVerify(container);
      } else {
        window.showToast('Identitas terverifikasi berhasil. Menuju pembayaran...');
        setTimeout(function () {
          window.location.hash = '#/payment';
        }, 1000);
      }
    });
  }

  // --------------------------------------------------------------------------
  // L13. PEMBAYARAN CONTROLLER
  // --------------------------------------------------------------------------
  function renderPayment(container) {
    var order = window.AppState.currentOrder;
    if (!order) {
      window.location.hash = '#/orders';
      return;
    }

    var total = order.pricing.sewa + order.pricing.perlindungan + order.deposit;

    container.innerHTML = `
      <div class="step-card-centered">
        <div class="step-title-header">
          <h2 style="font-size: 22px;">Pembayaran Sewa Rentfy</h2>
          <p style="font-size: 13px; color: var(--color-graphite); margin-top: 2px;">
            Dana ditahan secara aman sampai masa sewa selesai dan diverifikasi.
          </p>
        </div>

        <div style="background: #f8fafc; padding: 18px; border-radius: var(--radius-inputs); margin-bottom: 24px;">
          <div style="font-size: 13px; color: var(--color-smoke); margin-bottom: 4px;">Total yang harus dibayar:</div>
          <div style="font-size: 26px; font-weight: 700; color: var(--color-teal);">${formatRp(total)}</div>
        </div>

        <h4 style="font-size: 15px; margin-bottom: 12px;">Metode Pembayaran</h4>
        <div style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 24px;">
          <label style="display: flex; align-items: center; justify-content: space-between; padding: 14px 18px; border: 1.5px solid var(--color-teal); background: var(--color-teal-light); border-radius: var(--radius-buttons); cursor: pointer;">
            <div style="display: flex; align-items: center; gap: 10px;">
              <input type="radio" name="pay-method" value="qris" checked>
              <strong>QRIS Instan (BCA, GoPay, OVO, ShopeePay)</strong>
            </div>
            <span class="badge-status badge-teal">Instan</span>
          </label>
          <label style="display: flex; align-items: center; justify-content: space-between; padding: 14px 18px; border: 1px solid var(--color-mist); background: #ffffff; border-radius: var(--radius-buttons); cursor: pointer;">
            <div style="display: flex; align-items: center; gap: 10px;">
              <input type="radio" name="pay-method" value="va">
              <span>Virtual Account Bank (BCA / Mandiri / BNI)</span>
            </div>
          </label>
        </div>

        <div style="text-align: center; margin-bottom: 24px; padding: 20px; border: 1px solid var(--color-mist); border-radius: var(--radius-inputs); background: #ffffff;">
          <div style="font-weight: 600; font-size: 14px; margin-bottom: 12px;">Kode Pembayaran QRIS</div>
          <img src="https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=RENTFY-${order.orderId}" alt="QRIS Demo" style="display: inline-block;">
          <div style="font-size: 12px; color: var(--color-smoke); margin-top: 10px;">Klik tombol di bawah untuk simulasi penyelesaian pembayaran</div>
        </div>

        <!-- 1 Amber CTA -->
        <button class="btn btn-amber btn-block" id="pay-confirm-btn" style="padding: 14px;">
          Bayar Sekarang (${formatRp(total)})
        </button>
      </div>
    `;

    document.getElementById('pay-confirm-btn').addEventListener('click', function () {
      this.textContent = 'Memverifikasi Pembayaran...';
      this.disabled = true;

      setTimeout(function () {
        window.AppState.orderStatus = 'siap_ambil';
        window.showToast('Pembayaran berhasil! Dana ditahan aman.');
        window.location.hash = '#/pickup';
      }, 1500);
    });
  }

  // --------------------------------------------------------------------------
  // L14. PENGAMBILAN BARANG CONTROLLER (Tahap 4)
  // --------------------------------------------------------------------------
  function renderPickup(container) {
    var order = window.AppState.currentOrder;
    var owner = window.RentfyData.owner;

    container.innerHTML = `
      <div class="step-card-centered">
        <div class="step-title-header">
          <span class="badge-status badge-teal" style="margin-bottom: 8px;">Tahap 4: Serah Terima</span>
          <h2 style="font-size: 22px;">Pengambilan Barang</h2>
          <p style="font-size: 13px; color: var(--color-graphite); margin-top: 2px;">
            Ambil unit sesuai jadwal dan cek kelengkapan fisik langsung bersama pemilik.
          </p>
        </div>

        <div style="background: #f8fafc; border: 1px solid var(--color-mist); padding: 18px; border-radius: var(--radius-inputs); margin-bottom: 20px;">
          <div style="font-size: 12px; font-weight: 600; text-transform: uppercase; color: var(--color-smoke); margin-bottom: 4px;">Titik Serah Terima:</div>
          <div style="font-weight: 700; font-size: 15px; margin-bottom: 4px; display: flex; align-items: center; gap: 6px;">
            <span class="icon-svg" style="color:var(--color-teal);">${Icons.pin}</span> ${owner.address}
          </div>
          <div style="font-size: 13px; color: var(--color-slate); margin-bottom: 6px;">
            Jadwal: <strong>10:00 WIB (${order ? order.dates.start : '17 Nov'})</strong>
          </div>
          <div style="font-size: 13px; color: var(--color-slate);">
            Pemilik: <strong>${owner.name} (${owner.location})</strong>
          </div>
        </div>

        <!-- Interactive Map Pin -->
        <div id="pickup-map-el" class="leaflet-map-element"></div>

        <h4 style="font-size: 15px; margin-top: 24px; margin-bottom: 6px;">Dokumentasi Kondisi Awal (Opsional)</h4>
        <p style="font-size: 12px; color: var(--color-smoke);">Ambil foto kondisi fisik unit sebelum dibawa sebagai bukti serah terima.</p>
        
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin: 16px 0;">
          <div class="photo-slot-clean" onclick="showToast('Foto tampak depan tersimpan')">
            <span class="icon-svg">${Icons.camera}</span>
            <span>Tampak Depan</span>
          </div>
          <div class="photo-slot-clean" onclick="showToast('Foto tampak belakang tersimpan')">
            <span class="icon-svg">${Icons.camera}</span>
            <span>Tampak Belakang</span>
          </div>
          <div class="photo-slot-clean" onclick="showToast('Foto kelengkapan tersimpan')">
            <span class="icon-svg">${Icons.camera}</span>
            <span>Kelengkapan</span>
          </div>
          <div class="photo-slot-clean" onclick="showToast('Foto nomor seri tersimpan')">
            <span class="icon-svg">${Icons.camera}</span>
            <span>Nomor Seri</span>
          </div>
        </div>

        <!-- 1 Amber CTA -->
        <button class="btn btn-amber btn-block" id="btn-received-ok" style="padding: 14px; margin-top: 20px;">
          Barang Sudah Saya Terima
        </button>

        <div style="text-align: center; margin-top: 14px;">
          <a href="#/chat" class="btn btn-ghost" style="font-size: 13px;">
            <span class="icon-svg">${Icons.message}</span> Hubungi Mas Dimas
          </a>
        </div>
      </div>
    `;

    setTimeout(function () {
      var mapEl = document.getElementById('pickup-map-el');
      if (mapEl) {
        var map = L.map(mapEl, { attributionControl: false }).setView([-6.2442, 106.7978], 15);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
        L.marker([-6.2442, 106.7978]).addTo(map).bindPopup('Titik Pengambilan Unit').openPopup();
        mapInstances.push(map);
      }
    }, 150);

    document.getElementById('btn-received-ok').addEventListener('click', function () {
      window.AppState.orderStatus = 'sedang_disewa';
      window.showToast('Status diperbarui: Masa sewa dimulai');
      window.location.hash = '#/renting';
    });
  }

  // --------------------------------------------------------------------------
  // L15. SEDANG DISEWA CONTROLLER (Tahap 5)
  // --------------------------------------------------------------------------
  function renderRenting(container) {
    var order = window.AppState.currentOrder;
    var returnDate = order ? order.dates.end : '18 Nov';

    container.innerHTML = `
      <div class="step-card-centered">
        <div class="step-title-header">
          <span class="badge-status badge-teal" style="margin-bottom: 8px;">Masa Sewa Berjalan</span>
          <h2 style="font-size: 22px;">Barang Sedang Kamu Gunakan</h2>
          <p style="font-size: 13px; color: var(--color-graphite); margin-top: 2px;">
            Gunakan barang secara wajar dan kembalikan tepat waktu sesuai jadwal.
          </p>
        </div>

        <div style="background: var(--color-forest-stage); color: #ffffff; padding: 24px; border-radius: var(--radius-cards); text-align: center; margin-bottom: 24px;">
          <div style="font-size: 13px; opacity: 0.85; margin-bottom: 4px;">Kembalikan paling lambat:</div>
          <div style="font-size: 26px; font-weight: 700; margin-bottom: 8px; display: flex; align-items: center; justify-content: center; gap: 8px;">
            <span class="icon-svg">${Icons.calendar}</span> ${returnDate} pukul 18:00 WIB
          </div>
          <span class="badge-status badge-amber" style="color: #78350f;">Sisa Waktu: 1 Hari 8 Jam</span>
        </div>

        <div style="background: #fffbeb; border: 1px solid #fde68a; padding: 14px; border-radius: var(--radius-buttons); font-size: 13px; color: #92400e; margin-bottom: 24px; display: flex; align-items: center; gap: 8px;">
          <span class="icon-svg" style="color: #b45309;">${Icons.info}</span>
          Harap kembalikan tepat waktu untuk menghindari biaya keterlambatan per hari.
        </div>

        <h4 style="font-size: 15px; margin-bottom: 10px;">Tips Perawatan Selama Sewa:</h4>
        <ul style="padding-left: 20px; font-size: 13px; color: var(--color-slate); line-height: 1.8; margin-bottom: 28px;">
          <li>Simpan di tempat kering dan terlindung dari cuaca ekstrem.</li>
          <li>Gunakan tali strap pengaman saat mengoperasikan unit di luar ruangan.</li>
          <li>Pastikan kelengkapan aksesori tetap dalam tas penyimpanan.</li>
        </ul>

        <!-- 1 Amber CTA -->
        <button class="btn btn-amber btn-block" id="start-return-btn" style="padding: 14px;">
          Kembalikan Barang Sekarang
        </button>

        <div style="display: flex; justify-content: center; gap: 16px; margin-top: 16px;">
          <a href="#/chat" class="btn btn-ghost" style="font-size: 13px;">
            <span class="icon-svg">${Icons.message}</span> Chat Pemilik
          </a>
          <button class="btn btn-ghost" style="font-size: 13px;" onclick="demoToast()">Laporkan Kendala</button>
        </div>
      </div>
    `;

    document.getElementById('start-return-btn').addEventListener('click', function () {
      window.location.hash = '#/return';
    });
  }

  // --------------------------------------------------------------------------
  // L16. PENGEMBALIAN CONTROLLER
  // --------------------------------------------------------------------------
  function renderReturn(container) {
    container.innerHTML = `
      <div class="step-card-centered">
        <div class="step-title-header">
          <h2 style="font-size: 22px;">Pemeriksaan & Pengembalian</h2>
          <p style="font-size: 13px; color: var(--color-graphite); margin-top: 2px;">
            Centang kelengkapan yang dikembalikan langsung ke tangan pemilik.
          </p>
        </div>

        <div style="background: #f8fafc; border: 1px solid var(--color-mist); padding: 18px; border-radius: var(--radius-inputs); margin-bottom: 20px;">
          <h4 style="font-size: 14px; margin-bottom: 10px;">Daftar Kelengkapan Unit:</h4>
          <div style="display: flex; flex-direction: column; gap: 10px;">
            <label style="display: flex; align-items: center; gap: 10px; font-size: 13px; cursor: pointer;">
              <input type="checkbox" checked> Bodi kamera & lensa tanpa lecet baru
            </label>
            <label style="display: flex; align-items: center; gap: 10px; font-size: 13px; cursor: pointer;">
              <input type="checkbox" checked> 2x Baterai & charger dock bawaan
            </label>
            <label style="display: flex; align-items: center; gap: 10px; font-size: 13px; cursor: pointer;">
              <input type="checkbox" checked> SD Card 64GB
            </label>
            <label style="display: flex; align-items: center; gap: 10px; font-size: 13px; cursor: pointer;">
              <input type="checkbox" checked> Tas kamera & strap asli
            </label>
          </div>
        </div>

        <h4 style="font-size: 15px; margin-bottom: 8px;">Foto Bukti Serah Terima Kembali</h4>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 20px;">
          <div class="photo-slot-clean" onclick="showToast('Foto fisik diunggah')">
            <span class="icon-svg">${Icons.camera}</span>
            <span>Foto Fisik</span>
          </div>
          <div class="photo-slot-clean" onclick="showToast('Foto kelengkapan diunggah')">
            <span class="icon-svg">${Icons.camera}</span>
            <span>Aksesori</span>
          </div>
          <div class="photo-slot-clean" onclick="showToast('Foto serah terima diunggah')">
            <span class="icon-svg">${Icons.camera}</span>
            <span>Serah Terima</span>
          </div>
          <div class="photo-slot-clean" onclick="showToast('Foto kwitansi diunggah')">
            <span class="icon-svg">${Icons.camera}</span>
            <span>Lainnya</span>
          </div>
        </div>

        <div style="margin-bottom: 24px;">
          <label style="display: block; font-size: 13px; font-weight: 600; margin-bottom: 6px; color: var(--color-slate);">
            Catatan Pengembalian (Opsional)
          </label>
          <textarea class="input-field" rows="2" placeholder="Barang diserahkan dalam kondisi bersih dan berfungsi normal."></textarea>
        </div>

        <!-- 1 Amber CTA -->
        <button class="btn btn-amber btn-block" id="btn-return-report" style="padding: 14px;">
          Kirim Laporan Pengembalian
        </button>
      </div>
    `;

    document.getElementById('btn-return-report').addEventListener('click', function () {
      window.AppState.orderStatus = 'pengecekan';
      window.location.hash = '#/complete';

      setTimeout(function () {
        if (window.AppState.orderStatus === 'pengecekan') {
          window.AppState.orderStatus = 'selesai';
          window.showToast('Deposit berhasil dikembalikan');
          renderComplete(container);
        }
      }, 5000);
    });
  }

  // --------------------------------------------------------------------------
  // L17. COMPLETE & REVIEW CONTROLLER
  // --------------------------------------------------------------------------
  function renderComplete(container) {
    var status = window.AppState.orderStatus;
    var order = window.AppState.currentOrder;
    var depositAmount = order ? order.deposit : 300000;

    if (status === 'pengecekan') {
      container.innerHTML = `
        <div class="step-card-centered" style="text-align: center; padding: 48px 32px;">
          <div class="icon-svg" style="color: var(--color-teal); margin-bottom: 16px; transform: scale(1.6);">${Icons.search}</div>
          <h2 style="font-size: 22px; margin-bottom: 8px;">Menunggu Pengecekan Pemilik</h2>
          <p style="color: var(--color-graphite); font-size: 14px; max-width: 440px; margin: 0 auto 24px;">
            Mas Dimas sedang memeriksa kondisi fisik dan kelengkapan unit. Deposit otomatis dicairkan setelah selesai.
          </p>
          <div style="background: #f8fafc; border: 1px solid var(--color-mist); padding: 14px; border-radius: var(--radius-buttons); margin-bottom: 24px; font-size: 13px; color: var(--color-slate);">
            Simulasi demo: Pengecekan selesai otomatis dalam 5 detik.
          </div>
          <a href="#/orders" class="btn btn-outline">Lihat Daftar Pesanan</a>
        </div>
      `;
    } else {
      container.innerHTML = `
        <div class="step-card-centered">
          <div style="text-align: center; margin-bottom: 28px;">
            <div style="width: 64px; height: 64px; border-radius: 50%; background: var(--color-success-bg); color: var(--color-success); display: flex; align-items: center; justify-content: center; margin: 0 auto 16px;">
              <span class="icon-svg" style="transform: scale(1.5);">${Icons.check}</span>
            </div>
            <h2 style="font-size: 24px; margin-bottom: 6px;">Sewa Selesai</h2>
            <p style="color: var(--color-graphite); font-size: 14px;">
              Deposit sebesar <strong>${formatRp(depositAmount)}</strong> telah dikembalikan ke saldo kamu.
            </p>
          </div>

          <div style="background: #ffffff; border: 1px solid var(--color-mist); padding: 24px; border-radius: var(--radius-cards); margin-bottom: 24px;">
            <h4 style="font-size: 16px; margin-bottom: 12px; text-align: center;">Beri Penilaian untuk Pemilik</h4>
            
            <div style="display: flex; justify-content: center; gap: 8px; margin-bottom: 16px; cursor: pointer;">
              <span class="icon-svg">${Icons.starFilled}</span>
              <span class="icon-svg">${Icons.starFilled}</span>
              <span class="icon-svg">${Icons.starFilled}</span>
              <span class="icon-svg">${Icons.starFilled}</span>
              <span class="icon-svg">${Icons.starFilled}</span>
            </div>

            <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; margin-bottom: 16px;">
              <button class="pill-tag pill-neutral active">Tepat waktu</button>
              <button class="pill-tag pill-neutral active">Barang sesuai</button>
              <button class="pill-tag pill-neutral active">Komunikatif</button>
            </div>

            <div>
              <label style="display: block; font-size: 13px; font-weight: 600; margin-bottom: 6px; color: var(--color-slate);">Ulasan Kamu</label>
              <textarea class="input-field" rows="3" placeholder="Ceritakan kepuasan menyewa dari Mas Dimas..."></textarea>
            </div>
          </div>

          <!-- 1 Amber CTA -->
          <button class="btn btn-amber btn-block" id="btn-finish-review" style="padding: 14px;">
            Kirim Ulasan
          </button>

          <div style="text-align: center; margin-top: 14px;">
            <a href="#/orders" style="font-size: 13px; color: var(--color-graphite);">Lewati Ulasan</a>
          </div>
        </div>
      `;

      document.getElementById('btn-finish-review').addEventListener('click', function () {
        window.showToast('Terima kasih atas ulasanmu');
        window.location.hash = '#/orders';
      });
    }
  }

  // --------------------------------------------------------------------------
  // L18. PROFIL CONTROLLER
  // --------------------------------------------------------------------------
  function renderProfile(container) {
    var user = window.RentfyData.user;

    container.innerHTML = `
      <div class="container" style="max-width: 640px; padding: 32px 0 60px;">
        <h1 style="font-size: 28px; margin-bottom: 24px;">Profil Saya</h1>

        <div style="background: #ffffff; border: 1px solid var(--color-mist); border-radius: var(--radius-cards); padding: 24px; box-shadow: var(--shadow-sm); margin-bottom: 24px; display: flex; align-items: center; gap: 20px;">
          <div style="width: 64px; height: 64px; border-radius: 50%; background: var(--color-teal); color: #ffffff; font-size: 28px; font-weight: 700; display: flex; align-items: center; justify-content: center;">
            ${user.avatar}
          </div>
          <div style="flex: 1;">
            <h3 style="font-size: 18px; margin-bottom: 2px;">${user.name}</h3>
            <div style="font-size: 13px; color: var(--color-graphite);">${user.email} • ${user.location}</div>
            <div style="font-size: 12px; color: var(--color-smoke); margin-top: 4px;">Penyewa Terverifikasi</div>
          </div>
          <button class="btn btn-outline" style="font-size: 12px;" onclick="demoToast()">Ubah</button>
        </div>

        <div style="background: #ffffff; border: 1px solid var(--color-mist); border-radius: var(--radius-cards); overflow: hidden; margin-bottom: 24px;">
          <a href="#/orders" style="display: flex; align-items: center; justify-content: space-between; padding: 16px 20px; border-bottom: 1px solid var(--color-mist); font-size: 14px; font-weight: 500;">
            <span style="display: flex; align-items: center; gap: 10px;"><span class="icon-svg">${Icons.box}</span> Pesanan Saya</span>
            <span class="icon-svg">${Icons.arrowRight}</span>
          </a>
          <div onclick="demoToast()" style="display: flex; align-items: center; justify-content: space-between; padding: 16px 20px; border-bottom: 1px solid var(--color-mist); font-size: 14px; font-weight: 500; cursor: pointer;">
            <span style="display: flex; align-items: center; gap: 10px;"><span class="icon-svg">${Icons.heartOutline}</span> Barang Tersimpan</span>
            <span class="icon-svg">${Icons.arrowRight}</span>
          </div>
          <a href="#/how-it-works" style="display: flex; align-items: center; justify-content: space-between; padding: 16px 20px; border-bottom: 1px solid var(--color-mist); font-size: 14px; font-weight: 500;">
            <span style="display: flex; align-items: center; gap: 10px;"><span class="icon-svg">${Icons.info}</span> Cara Kerja Rentfy</span>
            <span class="icon-svg">${Icons.arrowRight}</span>
          </a>
          <div onclick="demoToast()" style="display: flex; align-items: center; justify-content: space-between; padding: 16px 20px; font-size: 14px; font-weight: 500; cursor: pointer;">
            <span style="display: flex; align-items: center; gap: 10px;"><span class="icon-svg">${Icons.shield}</span> Pusat Bantuan & Keamanan</span>
            <span class="icon-svg">${Icons.arrowRight}</span>
          </div>
        </div>

        <button class="btn btn-danger btn-block" id="logout-btn">
          <span class="icon-svg">${Icons.logout}</span> Keluar dari Akun
        </button>
      </div>
    `;

    document.getElementById('logout-btn').addEventListener('click', function () {
      window.AppState.isLoggedIn = false;
      window.location.hash = '#/login';
      window.showToast('Kamu telah keluar');
    });
  }

  // --------------------------------------------------------------------------
  // L19. CARA KERJA CONTROLLER
  // --------------------------------------------------------------------------
  function renderHowItWorks(container) {
    var steps = window.RentfyData.howItWorks;

    container.innerHTML = `
      <div class="container" style="max-width: 760px; padding: 40px 0 60px;">
        <h1 style="font-size: 32px; text-align: center; margin-bottom: 8px;">Cara Kerja Rentfy</h1>
        <p style="text-align: center; color: var(--color-graphite); font-size: 15px; margin-bottom: 40px;">
          Platform peer-to-peer terpercaya untuk menyewa dan menyewakan barang dengan mudah dan aman.
        </p>

        <div style="display: flex; flex-direction: column; gap: 24px; margin-bottom: 40px;">
          ${steps.map(function (st) {
            var iconHtml = Icons[st.iconType] || Icons.box;
            return `
              <div style="display: flex; gap: 20px; background: #ffffff; border: 1px solid var(--color-mist); padding: 24px; border-radius: var(--radius-cards); box-shadow: var(--shadow-sm); align-items: flex-start;">
                <div class="icon-svg" style="color: var(--color-teal); padding: 14px; background: var(--color-teal-light); border-radius: var(--radius-buttons); font-size: 20px;">
                  ${iconHtml}
                </div>
                <div>
                  <h3 style="font-size: 18px; margin-bottom: 6px;">${st.step}. ${st.title}</h3>
                  <p style="font-size: 14px; color: var(--color-slate); line-height: 1.6;">${st.desc}</p>
                </div>
              </div>
            `;
          }).join('')}
        </div>

        <div style="background: var(--color-teal-light); padding: 24px; border-radius: var(--radius-cards); text-align: center; margin-bottom: 32px;">
          <h4 style="color: var(--color-teal); margin-bottom: 6px;">Jaminan 100% Proteksi Barang & Deposit</h4>
          <p style="color: var(--color-forest-stage); font-size: 13px;">
            Setiap transaksi di Rentfy dilindungi garansi keamanan barang dan deposit penjamin resmi.
          </p>
        </div>

        <div style="text-align: center;">
          <a href="#/search" class="btn btn-amber" style="padding: 12px 32px; font-size: 15px;">
            Mulai Cari Barang
          </a>
        </div>
      </div>
    `;
  }

  // --------------------------------------------------------------------------
  // L20. FILTER MODAL
  // --------------------------------------------------------------------------
  function openFilterModal(onApply) {
    var modal = document.createElement('div');
    modal.className = 'modal-backdrop';
    modal.innerHTML = `
      <div class="modal-card" style="max-width: 500px;">
        <div class="modal-header-row">
          <h3 style="font-size: 18px;">Filter Pencarian</h3>
          <button class="btn-ghost" id="filter-close" style="font-size: 18px; font-weight: bold;">✕</button>
        </div>
        <div class="modal-content-area">
          <div style="margin-bottom: 20px;">
            <div style="font-size: 13px; font-weight: 600; margin-bottom: 8px;">Area Lokasi</div>
            <div style="display: flex; flex-wrap: wrap; gap: 8px;">
              ${window.RentfyData.areas.slice(0, 4).map(function (a) {
                return `<button class="pill-tag pill-neutral ${a === window.AppState.selectedLocation ? 'active' : ''}">${a}</button>`;
              }).join('')}
            </div>
          </div>

          <div style="margin-bottom: 20px;">
            <div style="font-size: 13px; font-weight: 600; margin-bottom: 8px;">Urutkan Hasil</div>
            <div style="display: flex; gap: 8px;">
              <button class="pill-tag pill-neutral ${window.AppState.activeSort === 'terdekat' ? 'active' : ''}">Terdekat</button>
              <button class="pill-tag pill-neutral ${window.AppState.activeSort === 'termurah' ? 'active' : ''}">Termurah</button>
              <button class="pill-tag pill-neutral ${window.AppState.activeSort === 'rating' ? 'active' : ''}">Rating</button>
            </div>
          </div>

          <div style="margin-bottom: 12px;">
            <div style="font-size: 13px; font-weight: 600; margin-bottom: 8px;">Rentang Tarif / Hari</div>
            <div style="display: flex; flex-wrap: wrap; gap: 8px;">
              <button class="pill-tag pill-neutral active">Semua</button>
              <button class="pill-tag pill-neutral">Di bawah Rp50rb</button>
              <button class="pill-tag pill-neutral">Rp50rb - Rp150rb</button>
              <button class="pill-tag pill-neutral">Di atas Rp150rb</button>
            </div>
          </div>
        </div>
        <div class="modal-footer-row" style="display: flex; justify-content: space-between;">
          <button class="btn btn-ghost" id="filter-reset">Atur Ulang</button>
          <button class="btn btn-amber" id="filter-apply">Terapkan Filter</button>
        </div>
      </div>
    `;

    document.body.appendChild(modal);
    document.getElementById('filter-close').addEventListener('click', function () { modal.remove(); });
    document.getElementById('filter-reset').addEventListener('click', function () {
      window.AppState.activeSort = 'terdekat';
      modal.remove();
      if (onApply) onApply();
    });
    document.getElementById('filter-apply').addEventListener('click', function () {
      modal.remove();
      if (onApply) onApply();
    });
  }

  // --------------------------------------------------------------------------
  // INITIALIZATION & GLOBAL NAVIGATION EVENTS
  // --------------------------------------------------------------------------
  window.addEventListener('scroll', function () {
    var hash = window.location.hash || '#/login';
    var isHome = (hash === '#/' || hash === '#/home');
    var isSearch = (hash.indexOf('#/search') === 0);
    var hasPageSearch = isHome || isSearch;
    var navCenter = document.getElementById('nav-center-wrap');

    if (navCenter && hasPageSearch) {
      var threshold = isHome ? 220 : 180;
      if (window.scrollY > threshold) {
        navCenter.classList.remove('hidden-nav-search');
      } else {
        navCenter.classList.add('hidden-nav-search');
      }
    }
  }, { passive: true });

  window.addEventListener('hashchange', router);
  window.addEventListener('DOMContentLoaded', function () {
    router();

    var navInput = document.getElementById('nav-input');
    var navBtn = document.getElementById('nav-search-btn');

    function triggerNavSearch() {
      if (!navInput) return;
      var q = navInput.value.trim();
      window.AppState.searchQuery = q;
      window.location.hash = '#/search?q=' + encodeURIComponent(q);
    }

    if (navInput) {
      navInput.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') triggerNavSearch();
      });
    }
    if (navBtn) {
      navBtn.addEventListener('click', triggerNavSearch);
    }
  });

})();
