# -*- coding: utf-8 -*-
"""
Part 1 of Rentfy screens: L1, L2, L3, L4, L5
"""

def get_common_nav():
    return '''
  <!-- Desktop Navbar -->
  <header class="navbar">
    <div class="app-container navbar-inner">
      <div class="brand-logo" onclick="navigateTo('L3')">
        <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect width="32" height="32" rx="10" fill="#0F5C63"/>
          <path d="M9 22V10H16C18.2091 10 20 11.7909 20 14C20 16.2091 18.2091 18 16 18H9M15.5 18L21 22" stroke="white" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
          <circle cx="23" cy="9" r="3" fill="#F59E0B"/>
        </svg>
        <span class="brand-text">rentfy</span>
      </div>

      <div class="navbar-search">
        <div class="search-box-container">
          <div class="search-input-col">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#9CA3AF" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            <input type="text" id="desktop-search-input" placeholder="Mau sewa apa?" value="" onkeydown="if(event.key==='Enter') handleSearchTrigger('desktop')">
          </div>
          <div class="search-divider"></div>
          <button class="search-chip-btn" onclick="openLocationPicker()" title="Pilih lokasi">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
            <span id="nav-location-text">Jakarta Selatan</span>
          </button>
          <div class="search-divider"></div>
          <button class="search-chip-btn" onclick="openDatePickerModal()" title="Pilih tanggal">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
            <span id="nav-date-text">17 Nov</span>
          </button>
          <button class="search-submit-btn" onclick="handleSearchTrigger('desktop')" title="Cari">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          </button>
        </div>
      </div>

      <div class="navbar-actions">
        <button class="nav-link" onclick="navigateTo('L19')">Cara kerja</button>
        <button class="nav-link" onclick="navigateTo('L9')">Pesanan</button>
        <button class="nav-icon-btn" onclick="navigateTo('L10')" title="Pesan">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
        </button>
        <button class="nav-icon-btn" onclick="showToast('Fitur notifikasi belum tersedia di versi demo')" title="Notifikasi">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>
        </button>
        <div class="avatar-btn" onclick="navigateTo('L18')" title="Profil saya">
          <div class="avatar-circle">R</div>
          <span style="font-size: 13px; font-weight: 600;">Rina</span>
        </div>
      </div>
    </div>
  </header>

  <!-- Mobile App Bar Header -->
  <header class="mobile-app-bar">
    <div class="brand-logo" onclick="navigateTo('L3')">
      <svg width="28" height="28" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="32" height="32" rx="10" fill="#0F5C63"/>
        <path d="M9 22V10H16C18.2091 10 20 11.7909 20 14C20 16.2091 18.2091 18 16 18H9M15.5 18L21 22" stroke="white" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="23" cy="9" r="3" fill="#F59E0B"/>
      </svg>
      <span class="brand-text" style="font-size: 20px;">rentfy</span>
    </div>
    <div style="display: flex; align-items: center; gap: 8px;">
      <button class="nav-icon-btn" style="width: 36px; height: 36px;" onclick="navigateTo('L10')" title="Chat">
        <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
      </button>
      <button class="nav-icon-btn" style="width: 36px; height: 36px;" onclick="showToast('Fitur notifikasi belum tersedia di versi demo')" title="Notifikasi">
        <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>
      </button>
      <div class="avatar-circle" style="width: 32px; height: 32px; cursor: pointer;" onclick="navigateTo('L18')">R</div>
    </div>
  </header>
'''

def get_mobile_tabs(active_tab='beranda'):
    return f'''
  <!-- Mobile Bottom Navigation Tab Bar -->
  <nav class="mobile-tab-bar">
    <button class="tab-item {'active' if active_tab=='beranda' else ''}" onclick="navigateTo('L3')">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
      <span>Beranda</span>
    </button>
    <button class="tab-item {'active' if active_tab=='cari' else ''}" onclick="handleMobileSearchTab()">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
      <span>Cari</span>
    </button>
    <button class="tab-item {'active' if active_tab=='pesanan' else ''}" onclick="navigateTo('L9')">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
      <span>Pesanan</span>
    </button>
    <button class="tab-item {'active' if active_tab=='profil' else ''}" onclick="navigateTo('L18')">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
      <span>Profil</span>
    </button>
  </nav>
'''

def get_l1_screen():
    return '''
  <!-- L1: Login Screen -->
  <section id="screen-L1" class="screen active" style="background-color: var(--primary); color: #FFFFFF; display: flex; align-items: center; justify-content: center; min-height: 100vh; padding: 24px 16px;">
    <div class="auth-container" style="background: #FFFFFF; border-radius: var(--radius-xl); padding: 36px 28px; box-shadow: var(--shadow-xl); color: var(--text-main); width: 100%; text-align: center;">
      <!-- Logo & Brand Header -->
      <div style="display: flex; justify-content: center; align-items: center; gap: 10px; margin-bottom: 12px;">
        <svg width="40" height="40" viewBox="0 0 32 32" fill="none">
          <rect width="32" height="32" rx="10" fill="#0F5C63"/>
          <path d="M9 22V10H16C18.2091 10 20 11.7909 20 14C20 16.2091 18.2091 18 16 18H9M15.5 18L21 22" stroke="white" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
          <circle cx="23" cy="9" r="3" fill="#F59E0B"/>
        </svg>
        <span style="font-family: 'Poppins', sans-serif; font-size: 28px; font-weight: 700; color: var(--primary); letter-spacing: -0.5px;">rentfy</span>
      </div>
      <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 28px; line-height: 1.4;">
        Sewa dan sewakan barang dengan sederhana dan aman
      </p>

      <!-- Form Inputs -->
      <div class="input-group">
        <label class="input-label" for="l1-email">Email</label>
        <div class="input-with-icon">
          <span class="input-icon-left">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
          </span>
          <input type="email" id="l1-email" class="input-field" placeholder="nama@email.com" value="rina@example.com">
        </div>
      </div>

      <div class="input-group" style="margin-bottom: 24px;">
        <label class="input-label" for="l1-password">Kata Sandi</label>
        <div class="input-with-icon">
          <span class="input-icon-left">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
          </span>
          <input type="password" id="l1-password" class="input-field" placeholder="••••••••" value="password123">
        </div>
      </div>

      <!-- Single Amber Button -->
      <button class="btn btn-amber" onclick="navigateTo('L3')">Masuk</button>

      <div style="margin-top: 20px; font-size: 13px; color: var(--text-muted);">
        Belum punya akun? <a href="javascript:void(0)" onclick="navigateTo('L2')" style="color: var(--primary); font-weight: 600; text-decoration: none;">Daftar</a>
      </div>
    </div>
  </section>
'''

def get_l2_screen():
    return '''
  <!-- L2: Register Screen -->
  <section id="screen-L2" class="screen" style="background-color: var(--bg-page); display: flex; align-items: center; justify-content: center; min-height: 100vh; padding: 32px 16px;">
    <div class="auth-container" style="background: #FFFFFF; border: 1px solid var(--border-color); border-radius: var(--radius-xl); padding: 36px 28px; box-shadow: var(--shadow-lg); width: 100%;">
      <div style="text-align: center; margin-bottom: 24px;">
        <div style="display: inline-flex; align-items: center; gap: 8px; margin-bottom: 8px;">
          <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
            <rect width="32" height="32" rx="10" fill="#0F5C63"/>
            <path d="M9 22V10H16C18.2091 10 20 11.7909 20 14C20 16.2091 18.2091 18 16 18H9M15.5 18L21 22" stroke="white" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
            <circle cx="23" cy="9" r="3" fill="#F59E0B"/>
          </svg>
          <span style="font-family: 'Poppins', sans-serif; font-size: 24px; font-weight: 700; color: var(--primary);">rentfy</span>
        </div>
        <h2 style="font-size: 20px; margin-bottom: 4px;">Buat Akun Baru</h2>
        <p style="font-size: 13px; color: var(--text-muted);">Mulai sewa dan sewakan barang di sekitarmu</p>
      </div>

      <div class="input-group">
        <label class="input-label" for="l2-name">Nama Lengkap</label>
        <input type="text" id="l2-name" class="input-field" placeholder="Nama lengkapmu" value="Rina Salsabila">
      </div>

      <div class="input-group">
        <label class="input-label" for="l2-email">Email</label>
        <input type="email" id="l2-email" class="input-field" placeholder="nama@email.com" value="rina@example.com">
      </div>

      <div class="input-group">
        <label class="input-label" for="l2-phone">Nomor HP</label>
        <input type="tel" id="l2-phone" class="input-field" placeholder="08xxxxxxxxxx" value="08123456789">
      </div>

      <div class="input-group">
        <label class="input-label" for="l2-city">Kota atau Area</label>
        <select id="l2-city" class="input-field">
          <option value="Jakarta Selatan" selected>Jakarta Selatan</option>
          <option value="Jakarta Pusat">Jakarta Pusat</option>
          <option value="Jakarta Barat">Jakarta Barat</option>
          <option value="Jakarta Timur">Jakarta Timur</option>
          <option value="Depok">Depok</option>
          <option value="Tangerang Selatan">Tangerang Selatan</option>
          <option value="Bekasi">Bekasi</option>
        </select>
      </div>

      <div class="input-group" style="margin-bottom: 24px;">
        <label class="input-label" for="l2-password">Kata Sandi</label>
        <div class="input-with-icon">
          <input type="password" id="l2-password" class="input-field" placeholder="Minimal 8 karakter" value="password123">
          <span class="input-icon-right" onclick="togglePasswordVisibility('l2-password', this)">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
          </span>
        </div>
      </div>

      <!-- Single Amber Button -->
      <button class="btn btn-amber" onclick="navigateTo('L3')">Daftar</button>

      <div style="margin-top: 20px; text-align: center; font-size: 13px; color: var(--text-muted);">
        Sudah punya akun? <a href="javascript:void(0)" onclick="navigateTo('L1')" style="color: var(--primary); font-weight: 600; text-decoration: none;">Masuk</a>
      </div>
    </div>
  </section>
'''

def get_l3_screen():
    return '''
  <!-- L3: Homepage Screen -->
  <section id="screen-L3" class="screen">
    <!-- Navbar injected by JS or common -->
    <div id="l3-nav-container"></div>

    <main class="app-container" style="padding-top: 24px; padding-bottom: 40px;">
      <!-- Mobile Search Box (visible on mobile <640px) -->
      <div class="mobile-only-search" style="margin-bottom: 20px;">
        <div class="card" style="padding: 12px; border-radius: var(--radius-md);">
          <div style="display: flex; align-items: center; gap: 8px; padding-bottom: 10px; border-bottom: 1px solid var(--border-color);">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#9CA3AF" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            <input type="text" id="mobile-search-input" placeholder="Mau sewa apa?" style="border: none; outline: none; width: 100%; font-size: 14px;" onkeydown="if(event.key==='Enter') handleSearchTrigger('mobile')">
          </div>
          <div style="display: flex; align-items: center; justify-content: space-between; padding-top: 8px;">
            <div style="display: flex; gap: 8px;">
              <button class="search-chip-btn" style="padding: 4px 8px; font-size: 12px; background: #F1F5F9;" onclick="openLocationPicker()">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                <span id="m-nav-location-text">Jakarta Selatan</span>
              </button>
              <button class="search-chip-btn" style="padding: 4px 8px; font-size: 12px; background: #F1F5F9;" onclick="openDatePickerModal()">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                <span id="m-nav-date-text">17 Nov</span>
              </button>
            </div>
            <button class="search-submit-btn" style="width: 34px; height: 34px;" onclick="handleSearchTrigger('mobile')" title="Cari">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            </button>
          </div>
        </div>
      </div>

      <!-- Greeting & Header -->
      <div style="margin-bottom: 24px;">
        <h1 style="font-size: 26px; font-weight: 700; color: var(--text-main);">Halo, Rina 👋</h1>
        <p style="font-size: 14px; color: var(--text-muted);">Temukan barang yang kamu butuhkan untuk disewa hari ini di sekitarmu</p>
      </div>

      <!-- Banners -->
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 28px;">
        <div class="banner banner-info" style="margin-bottom: 0;">
          <div style="width: 36px; height: 36px; border-radius: 50%; background: var(--primary); color: white; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
          </div>
          <div>
            <div style="font-weight: 600; font-size: 13px;">Semua pemilik di Rentfy sudah terverifikasi</div>
            <div style="font-size: 12px; opacity: 0.85;">Penyewaan aman dengan perlindungan barang & penahanan deposit resmi.</div>
          </div>
        </div>

        <div class="banner" style="background: #FFFBEB; border: 1px solid #FDE68A; color: #92400E; margin-bottom: 0;">
          <div style="width: 36px; height: 36px; border-radius: 50%; background: #F59E0B; color: white; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
          </div>
          <div style="flex: 1;">
            <div style="font-weight: 600; font-size: 13px;">Baru pertama kali menyewa di Rentfy?</div>
            <div style="font-size: 12px; margin-top: 2px;">
              <a href="javascript:void(0)" onclick="navigateTo('L19')" style="color: #B45309; font-weight: 600; text-decoration: underline;">Lihat cara kerja & panduan sewa</a>
            </div>
          </div>
        </div>
      </div>

      <!-- Categories Row -->
      <div style="margin-bottom: 32px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
          <h2 style="font-size: 18px; font-weight: 600;">Kategori Pilihan</h2>
          <span style="font-size: 12px; color: var(--text-muted);">Geser untuk kategori lainnya</span>
        </div>
        <div class="category-scroll-row" id="l3-category-row">
          <!-- Populated by JS -->
        </div>
      </div>

      <!-- Section: Dekat Kamu -->
      <section style="margin-bottom: 40px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4px;">
          <h2 style="font-size: 20px; font-weight: 600;">Dekat Kamu</h2>
          <button class="btn-ghost" style="font-size: 13px; font-weight: 600; color: var(--primary);" onclick="navigateTo('L5', {category: 'Semua', sort: 'Terdekat'})">Lihat Semua →</button>
        </div>
        <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 16px;">Barang yang siap kamu ambil dalam jarak kurang dari 2 km dari lokasimu</p>
        <div class="items-grid" id="l3-nearby-grid">
          <!-- Populated by JS -->
        </div>
      </section>

      <!-- Section: Paling Sering Disewa -->
      <section style="margin-bottom: 40px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4px;">
          <h2 style="font-size: 20px; font-weight: 600;">Paling Sering Disewa</h2>
          <button class="btn-ghost" style="font-size: 13px; font-weight: 600; color: var(--primary);" onclick="navigateTo('L5', {category: 'Semua', sort: 'Rating'})">Lihat Semua →</button>
        </div>
        <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 16px;">Pilihan favorit penyewa dengan rating tertinggi dan ulasan terpercaya</p>
        <div class="items-grid" id="l3-popular-grid">
          <!-- Populated by JS -->
        </div>
      </section>
    </main>

    <!-- Footer injected by JS -->
    <div id="l3-footer-container"></div>
    <div id="l3-tabs-container"></div>
  </section>
'''

def get_l4_modal():
    return '''
  <!-- L4: Location Picker Modal / Bottom Sheet -->
  <div id="modal-L4" class="modal-backdrop">
    <div class="modal-sheet">
      <div class="modal-header">
        <h3 style="font-size: 16px; font-weight: 600;">Mau sewa di mana?</h3>
        <button class="btn-ghost" onclick="closeLocationPicker()" style="padding: 4px;" title="Tutup">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </button>
      </div>

      <div class="modal-body" style="padding-bottom: 12px;">
        <div class="input-with-icon" style="margin-bottom: 12px;">
          <span class="input-icon-left">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#9CA3AF" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          </span>
          <input type="text" id="l4-search-input" class="input-field" placeholder="Ketik area atau kecamatan..." value="Jakarta Selatan">
        </div>

        <!-- Quick location suggestions -->
        <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 14px;">
          <button class="chip" style="font-size: 11px; padding: 4px 10px;" onclick="selectLocationSuggestion('Kebayoran Baru', -6.2442, 106.7992)">Kebayoran Baru</button>
          <button class="chip" style="font-size: 11px; padding: 4px 10px;" onclick="selectLocationSuggestion('Senopati & SCBD', -6.2335, 106.8091)">Senopati</button>
          <button class="chip" style="font-size: 11px; padding: 4px 10px;" onclick="selectLocationSuggestion('Kemang', -6.2731, 106.8152)">Kemang</button>
          <button class="chip" style="font-size: 11px; padding: 4px 10px;" onclick="selectLocationSuggestion('Cilandak', -6.2905, 106.7981)">Cilandak</button>
          <button class="chip" style="font-size: 11px; padding: 4px 10px;" onclick="selectLocationSuggestion('Tebet', -6.2300, 106.8500)">Tebet</button>
        </div>

        <!-- Real Leaflet Map Container -->
        <div style="position: relative; width: 100%; height: 220px; border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--border-color);">
          <div id="map-l4" style="width: 100%; height: 100%;"></div>
          <!-- Floating Lokasi Saya Button -->
          <button onclick="centerMapL4CurrentLocation()" style="position: absolute; top: 10px; right: 10px; z-index: 500; background: #FFFFFF; border: 1px solid var(--border-color); border-radius: 9999px; padding: 6px 12px; font-size: 12px; font-weight: 600; display: flex; align-items: center; gap: 6px; box-shadow: var(--shadow-md); cursor: pointer; color: var(--primary);">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="22" y1="12" x2="18" y2="12"></line><line x1="6" y1="12" x2="2" y2="12"></line><line x1="12" y1="6" x2="12" y2="2"></line><line x1="12" y1="22" x2="12" y2="18"></line></svg>
            Lokasi saya
          </button>
        </div>
        <p style="font-size: 11px; color: var(--text-muted); margin-top: 8px; text-align: center;">
          Geser peta atau ketuk untuk memilih titik lokasi sewa
        </p>
      </div>

      <div class="modal-footer">
        <!-- Single Amber Button -->
        <button class="btn btn-amber" onclick="confirmLocationL4()">Pakai lokasi ini</button>
      </div>
    </div>
  </div>
'''

def get_l5_screen():
    return '''
  <!-- L5: Search Results Screen -->
  <section id="screen-L5" class="screen">
    <div id="l5-nav-container"></div>

    <main class="app-container" style="padding-top: 20px; padding-bottom: 40px;">
      <!-- Title & Results count -->
      <div style="display: flex; align-items: baseline; justify-content: space-between; flex-wrap: wrap; gap: 8px; margin-bottom: 12px;">
        <div>
          <h1 id="l5-result-title" style="font-size: 22px; font-weight: 700;">Hasil untuk "Kamera"</h1>
          <p id="l5-result-count" style="font-size: 13px; color: var(--text-muted);">8 barang ditemukan</p>
        </div>
        <!-- Ubah Lokasi & Tanggal chips info -->
        <div style="display: flex; align-items: center; gap: 8px; font-size: 12px; color: var(--text-muted);">
          <span>📍 Dekat <strong id="l5-info-location">Jakarta Selatan</strong> (<a href="javascript:void(0)" onclick="openLocationPicker()" style="color: var(--primary); font-weight: 600;">ubah</a>)</span>
          <span>·</span>
          <span>📅 Periode <strong id="l5-info-date">17 Nov</strong> (<a href="javascript:void(0)" onclick="openDatePickerModal()" style="color: var(--primary); font-weight: 600;">ubah</a>)</span>
        </div>
      </div>

      <!-- Subcategory Chips (Scrollable) -->
      <div class="category-scroll-row" id="l5-subcategory-chips" style="padding-bottom: 10px; margin-bottom: 8px;">
        <!-- Populated by JS -->
      </div>

      <!-- Controls Row: Sort Chips, List/Map Toggle, Filter Button -->
      <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; padding: 12px 0; border-top: 1px solid var(--border-color); border-bottom: 1px solid var(--border-color); margin-bottom: 20px;">
        <!-- Sort chips (Actually reorders items!) -->
        <div style="display: flex; align-items: center; gap: 8px;">
          <span style="font-size: 13px; font-weight: 500; color: var(--text-muted); margin-right: 4px;">Urutkan:</span>
          <button class="chip active" id="sort-terdekat" onclick="setSortL5('Terdekat')">Terdekat</button>
          <button class="chip" id="sort-termurah" onclick="setSortL5('Termurah')">Termurah</button>
          <button class="chip" id="sort-rating" onclick="setSortL5('Rating')">Rating</button>
        </div>

        <div style="display: flex; align-items: center; gap: 10px;">
          <!-- Filter Button (Opens L20) -->
          <button class="btn btn-secondary btn-sm" style="width: auto;" onclick="openFilterModal()">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"></polygon></svg>
            Filter
          </button>

          <!-- List / Map View Toggle -->
          <div style="display: flex; border: 1px solid var(--border-color); border-radius: var(--radius-md); overflow: hidden; background: #FFFFFF;">
            <button id="view-toggle-list" class="btn-ghost" style="padding: 6px 12px; font-size: 12px; font-weight: 600; background: var(--primary-light); color: var(--primary);" onclick="toggleViewL5('list')" title="Tampilan Daftar">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line><line x1="3" y1="6" x2="3.01" y2="6"></line><line x1="3" y1="12" x2="3.01" y2="12"></line><line x1="3" y1="18" x2="3.01" y2="18"></line></svg>
              Daftar
            </button>
            <button id="view-toggle-map" class="btn-ghost" style="padding: 6px 12px; font-size: 12px; font-weight: 600; color: var(--text-muted);" onclick="toggleViewL5('map')" title="Tampilan Peta">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"></polygon><line x1="8" y1="2" x2="8" y2="18"></line><line x1="16" y1="6" x2="16" y2="22"></line></svg>
              Peta
            </button>
          </div>
        </div>
      </div>

      <!-- List Container -->
      <div id="l5-list-view">
        <div class="items-grid" id="l5-items-grid">
          <!-- Populated by JS -->
        </div>

        <!-- Empty State Container -->
        <div id="l5-empty-state" style="display: none; text-align: center; padding: 60px 16px;">
          <div style="width: 64px; height: 64px; border-radius: 50%; background: #F1F5F9; color: var(--text-muted); display: inline-flex; align-items: center; justify-content: center; margin-bottom: 16px;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          </div>
          <h3 style="font-size: 18px; font-weight: 600; margin-bottom: 6px;">Belum ada barang untuk pencarian ini</h3>
          <p style="font-size: 13px; color: var(--text-muted); max-width: 380px; margin: 0 auto 20px;">Coba gunakan kata kunci lain seperti "kamera", "tenda", "bor", atau jelajahi semua kategori kami.</p>
          <button class="btn btn-outline" style="width: auto; margin: 0 auto;" onclick="resetSearchL5()">Lihat semua barang</button>
        </div>
      </div>

      <!-- Map View Container -->
      <div id="l5-map-view" style="display: none;">
        <div style="position: relative; width: 100%; height: 550px; border-radius: var(--radius-lg); overflow: hidden; border: 1px solid var(--border-color);">
          <div id="map-l5" style="width: 100%; height: 100%;"></div>
        </div>
        <p style="font-size: 12px; color: var(--text-muted); margin-top: 8px; text-align: center;">
          Ketuk pin pada peta untuk melihat detail singkat dan membuka rincian barang
        </p>
      </div>
    </main>

    <div id="l5-footer-container"></div>
    <div id="l5-tabs-container"></div>
  </section>
'''

print("screens_part1.py written successfully")
