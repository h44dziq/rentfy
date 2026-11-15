# -*- coding: utf-8 -*-
"""
Part 4 of Rentfy screens: L16, L17, L18, L19, L20 and Common Modals & Footer
"""

def get_l16_screen():
    return '''
  <!-- L16: Return Screen -->
  <section id="screen-L16" class="screen" style="background: var(--bg-page); min-height: 100vh;">
    <div class="step-container" style="max-width: 640px;">
      <button class="btn-ghost" style="padding: 6px 0; margin-bottom: 16px; display: flex; align-items: center; gap: 6px;" onclick="navigateTo('L15')">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
        Kembali ke status sewa
      </button>

      <h1 style="font-size: 22px; font-weight: 700; margin-bottom: 4px;">Cek Kondisi Pengembalian</h1>
      <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 20px;">
        Pastikan seluruh kelengkapan dan kondisi fisik barang telah sesuai sebelum diserahkan kembali ke pemilik
      </p>

      <!-- Checklist Section -->
      <div class="card" style="margin-bottom: 20px;">
        <h3 style="font-size: 15px; font-weight: 600; margin-bottom: 12px;">Daftar Periksa Kelengkapan</h3>
        <div style="display: flex; flex-direction: column; gap: 10px;" id="l16-checklist-container">
          <label style="display: flex; align-items: center; gap: 10px; font-size: 13px; cursor: pointer;">
            <input type="checkbox" checked style="accent-color: var(--primary); width: 16px; height: 16px;">
            <span>Bodi kamera bersih dan bebas goresan baru</span>
          </label>
          <label style="display: flex; align-items: center; gap: 10px; font-size: 13px; cursor: pointer;">
            <input type="checkbox" checked style="accent-color: var(--primary); width: 16px; height: 16px;">
            <span>Lensa bersih, optik jernih tanpa jamur/debu</span>
          </label>
          <label style="display: flex; align-items: center; gap: 10px; font-size: 13px; cursor: pointer;">
            <input type="checkbox" checked style="accent-color: var(--primary); width: 16px; height: 16px;">
            <span>2x Baterai original & dual charger lengkap</span>
          </label>
          <label style="display: flex; align-items: center; gap: 10px; font-size: 13px; cursor: pointer;">
            <input type="checkbox" checked style="accent-color: var(--primary); width: 16px; height: 16px;">
            <span>SD Card 64GB dan strap leher terpasang</span>
          </label>
          <label style="display: flex; align-items: center; gap: 10px; font-size: 13px; cursor: pointer;">
            <input type="checkbox" checked style="accent-color: var(--primary); width: 16px; height: 16px;">
            <span>Tas kamera dalam kondisi baik & bersih</span>
          </label>
        </div>
      </div>

      <!-- 4 Photo Slots -->
      <div class="card" style="margin-bottom: 20px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
          <h3 style="font-size: 15px; font-weight: 600;">Foto Bukti Kondisi Pengembalian</h3>
          <span style="font-size: 11px; color: var(--text-muted);">Foto dicap waktu otomatis</span>
        </div>
        <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 14px;">Ketuk slot di bawah untuk mengunggah atau mengganti foto kondisi terkini</p>

        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
          <div onclick="simulatePhotoUpload(this, 'Depan')" style="aspect-ratio: 1/1; border: 2px dashed var(--border-color); border-radius: var(--radius-md); display: flex; flex-direction: column; align-items: center; justify-content: center; cursor: pointer; background: #F8FAFC; text-align: center; padding: 4px; transition: all 0.15s;">
            <span style="font-size: 20px;">📷</span>
            <span style="font-size: 11px; font-weight: 500; color: var(--text-muted); margin-top: 4px;">Depan</span>
          </div>
          <div onclick="simulatePhotoUpload(this, 'Belakang')" style="aspect-ratio: 1/1; border: 2px dashed var(--border-color); border-radius: var(--radius-md); display: flex; flex-direction: column; align-items: center; justify-content: center; cursor: pointer; background: #F8FAFC; text-align: center; padding: 4px; transition: all 0.15s;">
            <span style="font-size: 20px;">📷</span>
            <span style="font-size: 11px; font-weight: 500; color: var(--text-muted); margin-top: 4px;">Belakang</span>
          </div>
          <div onclick="simulatePhotoUpload(this, 'Samping')" style="aspect-ratio: 1/1; border: 2px dashed var(--border-color); border-radius: var(--radius-md); display: flex; flex-direction: column; align-items: center; justify-content: center; cursor: pointer; background: #F8FAFC; text-align: center; padding: 4px; transition: all 0.15s;">
            <span style="font-size: 20px;">📷</span>
            <span style="font-size: 11px; font-weight: 500; color: var(--text-muted); margin-top: 4px;">Samping</span>
          </div>
          <div onclick="simulatePhotoUpload(this, 'Aksesori')" style="aspect-ratio: 1/1; border: 2px dashed var(--border-color); border-radius: var(--radius-md); display: flex; flex-direction: column; align-items: center; justify-content: center; cursor: pointer; background: #F8FAFC; text-align: center; padding: 4px; transition: all 0.15s;">
            <span style="font-size: 20px;">📷</span>
            <span style="font-size: 11px; font-weight: 500; color: var(--text-muted); margin-top: 4px;">Aksesori</span>
          </div>
        </div>
      </div>

      <!-- Notes -->
      <div class="input-group">
        <label class="input-label" for="l16-notes">Catatan pengembalian (opsional)</label>
        <textarea id="l16-notes" class="input-field" rows="3" placeholder="Contoh: Barang telah diserahkan langsung ke Mas Dimas dalam kondisi sangat bersih dan lengkap..."></textarea>
      </div>

      <!-- Single Amber Button -->
      <button class="btn btn-amber" onclick="submitReturnReportL16()">
        Kirim laporan pengembalian
      </button>
    </div>
  </section>
'''

def get_l17_screen():
    return '''
  <!-- L17: Return Complete & Review Screen -->
  <section id="screen-L17" class="screen" style="background: var(--bg-page); min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 24px 16px;">
    <div class="step-container" style="background: #FFFFFF; border: 1px solid var(--border-color); border-radius: var(--radius-xl); box-shadow: var(--shadow-lg); text-align: center; padding: 36px 24px; width: 100%;">
      
      <!-- State 1: Menunggu Pengecekan Pemilik (5s timer auto-switch) -->
      <div id="l17-state-1">
        <div style="width: 72px; height: 72px; border-radius: 50%; background: #FEF3C7; color: #D97706; display: inline-flex; align-items: center; justify-content: center; margin-bottom: 20px;">
          <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
        </div>
        <span class="badge badge-yellow" style="margin-bottom: 8px;">Menunggu Pengecekan</span>
        <h2 style="font-size: 20px; font-weight: 700; margin-bottom: 8px;">Barang Sedang Diperiksa Pemilik</h2>
        <p style="font-size: 13px; color: var(--text-muted); line-height: 1.5; margin-bottom: 20px;">
          Pemilik (Dimas) sedang melakukan verifikasi kondisi dan kelengkapan barang. Proses maksimal memakan waktu 24 jam.
        </p>

        <div style="padding: 16px; background: #F8FAFC; border: 1px solid var(--border-color); border-radius: var(--radius-md); font-size: 12px; color: var(--text-muted); display: flex; align-items: center; justify-content: center; gap: 8px;">
          <span style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: #F59E0B; animation: pulse 1.5s infinite;"></span>
          Simulasi pengecekan otomatis (beralih dalam 5 detik)...
        </div>
      </div>

      <!-- State 2: Selesai & Review (Switched by JS) -->
      <div id="l17-state-2" style="display: none;">
        <div style="width: 72px; height: 72px; border-radius: 50%; background: var(--success-soft); color: var(--success); display: inline-flex; align-items: center; justify-content: center; margin-bottom: 16px;">
          <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
        </div>
        <h2 style="font-size: 22px; font-weight: 700; color: var(--text-main); margin-bottom: 6px;">Selesai! Sewa Telah Berakhir</h2>
        <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 20px;">Pemilik telah mengonfirmasi bahwa barang kembali dalam kondisi prima.</p>

        <!-- Deposit Returned Summary Card -->
        <div style="padding: 16px; background: #ECFDF5; border: 1px solid #A7F3D0; border-radius: var(--radius-md); text-align: left; margin-bottom: 24px;">
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
              <strong style="font-size: 13px; color: #065F46;">Deposit Telah Dikembalikan</strong>
              <div style="font-size: 11px; color: #047857; margin-top: 2px;">Dana dikembalikan penuh ke metode pembayaran kamu</div>
            </div>
            <span id="l17-deposit-return-amount" style="font-family: 'Poppins', sans-serif; font-size: 16px; font-weight: 700; color: #065F46;">Rp300.000</span>
          </div>
        </div>

        <!-- Review Section -->
        <div style="text-align: left; margin-bottom: 24px;">
          <h3 style="font-size: 15px; font-weight: 600; margin-bottom: 4px;">Beri Ulasan untuk Dimas Suryo</h3>
          <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 12px;">Bantu komunitas Rentfy dengan membagikan pengalaman sewamu</p>

          <!-- Interactive Star Rating -->
          <div style="display: flex; gap: 8px; margin-bottom: 14px;" id="l17-star-container">
            <span class="star-rating-item" style="font-size: 28px; cursor: pointer; color: #F59E0B;" onclick="setRatingL17(1)">★</span>
            <span class="star-rating-item" style="font-size: 28px; cursor: pointer; color: #F59E0B;" onclick="setRatingL17(2)">★</span>
            <span class="star-rating-item" style="font-size: 28px; cursor: pointer; color: #F59E0B;" onclick="setRatingL17(3)">★</span>
            <span class="star-rating-item" style="font-size: 28px; cursor: pointer; color: #F59E0B;" onclick="setRatingL17(4)">★</span>
            <span class="star-rating-item" style="font-size: 28px; cursor: pointer; color: #F59E0B;" onclick="setRatingL17(5)">★</span>
          </div>

          <!-- Review Tags -->
          <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 14px;">
            <button class="chip active" onclick="this.classList.toggle('active')">Tepat waktu</button>
            <button class="chip active" onclick="this.classList.toggle('active')">Barang sesuai</button>
            <button class="chip active" onclick="this.classList.toggle('active')">Komunikatif</button>
            <button class="chip" onclick="this.classList.toggle('active')">Pemilik ramah</button>
            <button class="chip" onclick="this.classList.toggle('active')">Kondisi prima</button>
          </div>

          <!-- Optional Comment -->
          <textarea id="l17-comment" class="input-field" rows="2" placeholder="Tulis catatan ulasan (opsional)..."></textarea>
        </div>

        <!-- Single Amber Button -->
        <button class="btn btn-amber" onclick="submitReviewL17()" style="margin-bottom: 10px;">
          Kirim ulasan
        </button>
        <button class="btn-ghost" style="font-size: 13px;" onclick="skipReviewL17()">
          Lewati ulasan
        </button>
      </div>

    </div>
  </section>
'''

def get_l18_screen():
    return '''
  <!-- L18: Profile Screen -->
  <section id="screen-L18" class="screen">
    <div id="l18-nav-container"></div>

    <main class="app-container" style="max-width: 580px; padding-top: 24px; padding-bottom: 40px;">
      <h1 style="font-size: 24px; font-weight: 700; margin-bottom: 20px;">Profil Saya</h1>

      <!-- Account Card -->
      <div class="card" style="display: flex; align-items: center; gap: 16px; margin-bottom: 24px; padding: 20px;">
        <div style="width: 64px; height: 64px; border-radius: 50%; background: var(--primary); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 26px; flex-shrink: 0;">
          R
        </div>
        <div style="flex: 1;">
          <div style="display: flex; align-items: center; gap: 8px;">
            <h2 style="font-size: 18px; font-weight: 600;">Rina Salsabila</h2>
            <span class="badge badge-verified" style="font-size: 10px;">Terverifikasi</span>
          </div>
          <div style="font-size: 13px; color: var(--text-muted); margin-top: 2px;">rina.salsabila@example.com</div>
          <div style="font-size: 12px; color: var(--text-muted);">0812-3456-7890 · Jakarta Selatan</div>
        </div>
        <button class="btn-ghost" style="color: var(--primary); font-size: 12px; font-weight: 600;" onclick="showToast('Fitur ubah profil belum tersedia di versi demo')">
          Ubah
        </button>
      </div>

      <!-- Menu List Card -->
      <div class="card" style="padding: 6px; margin-bottom: 24px;">
        <button class="btn-ghost" style="width: 100%; display: flex; align-items: center; justify-content: space-between; padding: 14px 16px; border-bottom: 1px solid var(--border-color); border-radius: var(--radius-sm);" onclick="navigateTo('L9')">
          <div style="display: flex; align-items: center; gap: 12px; font-size: 14px; font-weight: 500; color: var(--text-main);">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
            Pesanan saya
          </div>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </button>

        <button class="btn-ghost" style="width: 100%; display: flex; align-items: center; justify-content: space-between; padding: 14px 16px; border-bottom: 1px solid var(--border-color); border-radius: var(--radius-sm);" onclick="showToast('Fitur barang tersimpan belum tersedia di versi demo')">
          <div style="display: flex; align-items: center; gap: 12px; font-size: 14px; font-weight: 500; color: var(--text-main);">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
            Barang tersimpan
          </div>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </button>

        <button class="btn-ghost" style="width: 100%; display: flex; align-items: center; justify-content: space-between; padding: 14px 16px; border-bottom: 1px solid var(--border-color); border-radius: var(--radius-sm);" onclick="navigateTo('L19')">
          <div style="display: flex; align-items: center; gap: 12px; font-size: 14px; font-weight: 500; color: var(--text-main);">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
            Cara kerja Rentfy
          </div>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </button>

        <button class="btn-ghost" style="width: 100%; display: flex; align-items: center; justify-content: space-between; padding: 14px 16px; border-bottom: 1px solid var(--border-color); border-radius: var(--radius-sm);" onclick="showToast('Fitur bantuan belum tersedia di versi demo')">
          <div style="display: flex; align-items: center; gap: 12px; font-size: 14px; font-weight: 500; color: var(--text-main);">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
            Bantuan & FAQ
          </div>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </button>

        <button class="btn-ghost" style="width: 100%; display: flex; align-items: center; justify-content: space-between; padding: 14px 16px; border-radius: var(--radius-sm);" onclick="showToast('Fitur syarat & kebijakan belum tersedia di versi demo')">
          <div style="display: flex; align-items: center; gap: 12px; font-size: 14px; font-weight: 500; color: var(--text-main);">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
            Syarat Layanan & Kebijakan Privasi
          </div>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </button>
      </div>

      <!-- Danger Button (NO amber button on this screen) -->
      <button class="btn btn-danger-outline" onclick="navigateTo('L1')">
        Keluar
      </button>
    </main>

    <div id="l18-footer-container"></div>
    <div id="l18-tabs-container"></div>
  </section>
'''

def get_l19_screen():
    return '''
  <!-- L19: How Rentfy Works Screen -->
  <section id="screen-L19" class="screen" style="background: var(--bg-page); min-height: 100vh;">
    <!-- App Bar with Close button -->
    <header style="background: #FFFFFF; border-bottom: 1px solid var(--border-color); padding: 12px 16px; position: sticky; top: 0; z-index: 90;">
      <div style="max-width: 640px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between;">
        <h2 style="font-size: 17px; font-weight: 700;">Cara Kerja Rentfy</h2>
        <button class="btn-ghost" style="padding: 4px;" onclick="navigateBackFromL19()" title="Tutup">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </button>
      </div>
    </header>

    <main class="step-container" style="max-width: 640px; padding-top: 28px;">
      <div style="text-align: center; margin-bottom: 32px;">
        <h1 style="font-size: 24px; font-weight: 700; color: var(--primary); margin-bottom: 8px;">Sewa Mudah dalam 3 Langkah</h1>
        <p style="font-size: 14px; color: var(--text-muted); line-height: 1.5;">
          Sistem peer-to-peer terpercaya untuk menyewa barang berkualitas langsung dari pemilik terdekat
        </p>
      </div>

      <!-- 3 Vertical Steps with Icons -->
      <div style="display: flex; flex-direction: column; gap: 24px; margin-bottom: 32px;">
        
        <!-- Step 1 -->
        <div class="card" style="display: flex; gap: 16px; align-items: flex-start; padding: 20px;">
          <div style="width: 48px; height: 48px; border-radius: 50%; background: var(--primary-light); color: var(--primary); display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 700; flex-shrink: 0;">
            1
          </div>
          <div>
            <h3 style="font-size: 16px; font-weight: 600; margin-bottom: 4px;">Cari dan Pilih</h3>
            <p style="font-size: 13px; color: var(--text-muted); line-height: 1.5;">
              Temukan barang yang kamu butuhkan dari pemilik terdekat di sekitarmu. Urutkan berdasarkan jarak, harga sewa harian termurah, atau rating ulasan tertinggi.
            </p>
          </div>
        </div>

        <!-- Step 2 -->
        <div class="card" style="display: flex; gap: 16px; align-items: flex-start; padding: 20px;">
          <div style="width: 48px; height: 48px; border-radius: 50%; background: var(--primary-light); color: var(--primary); display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 700; flex-shrink: 0;">
            2
          </div>
          <div>
            <h3 style="font-size: 16px; font-weight: 600; margin-bottom: 4px;">Ajukan Sewa dan Bayar</h3>
            <p style="font-size: 13px; color: var(--text-muted); line-height: 1.5;">
              Pilih tanggal sewa kalender, kirim permintaan ke pemilik, lalu bayar dengan aman di dalam Rentfy. Dana sewa dan deposit ditahan dengan aman sampai barang kembali.
            </p>
          </div>
        </div>

        <!-- Step 3 -->
        <div class="card" style="display: flex; gap: 16px; align-items: flex-start; padding: 20px;">
          <div style="width: 48px; height: 48px; border-radius: 50%; background: var(--primary-light); color: var(--primary); display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 700; flex-shrink: 0;">
            3
          </div>
          <div>
            <h3 style="font-size: 16px; font-weight: 600; margin-bottom: 4px;">Ambil dan Kembalikan</h3>
            <p style="font-size: 13px; color: var(--text-muted); line-height: 1.5;">
              Ambil barang sesuai jadwal temu yang disepakati, pakai dengan baik, lalu kembalikan tepat waktu. Deposit otomatis dikembalikan penuh setelah barang dicek pemilik.
            </p>
          </div>
        </div>
      </div>

      <!-- Trust info card -->
      <div class="banner banner-info" style="margin-bottom: 32px;">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="flex-shrink: 0;"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
        <span style="font-size: 13px; line-height: 1.4;">
          Semua transaksi dilakukan di Rentfy agar kamu dan pemilik selalu terlindungi oleh Program Jaminan Rentfy.
        </span>
      </div>

      <!-- Single Amber Button -->
      <button class="btn btn-amber" onclick="navigateTo('L3')">
        Mulai cari barang
      </button>
    </main>
  </section>
'''

def get_l20_modal():
    return '''
  <!-- L20: Filter Modal / Bottom Sheet (Over L5) -->
  <div id="modal-L20" class="modal-backdrop">
    <div class="modal-sheet">
      <div class="modal-header">
        <h3 style="font-size: 16px; font-weight: 600;">Filter Pencarian</h3>
        <button class="btn-ghost" onclick="closeFilterModal()" style="padding: 4px;" title="Tutup">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </button>
      </div>

      <div class="modal-body" style="padding-bottom: 12px;">
        <!-- Tanggal Sewa -->
        <div style="margin-bottom: 20px;">
          <h4 style="font-size: 13px; font-weight: 600; margin-bottom: 8px;">Tanggal Sewa</h4>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
            <div>
              <label class="input-label" style="font-size: 11px;">Ambil</label>
              <input type="text" class="input-field" value="17 Nov 2026" readonly onclick="openDatePickerModal()" style="cursor: pointer;">
            </div>
            <div>
              <label class="input-label" style="font-size: 11px;">Kembalikan</label>
              <input type="text" class="input-field" value="18 Nov 2026" readonly onclick="openDatePickerModal()" style="cursor: pointer;">
            </div>
          </div>
        </div>

        <!-- Area / Lokasi -->
        <div style="margin-bottom: 20px;">
          <h4 style="font-size: 13px; font-weight: 600; margin-bottom: 8px;">Area</h4>
          <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            <button class="chip active" onclick="toggleFilterChip(this)">Jakarta Selatan</button>
            <button class="chip" onclick="toggleFilterChip(this)">Jakarta Pusat</button>
            <button class="chip" onclick="toggleFilterChip(this)">Depok</button>
            <button class="chip" onclick="toggleFilterChip(this)">Tangerang Selatan</button>
          </div>
        </div>

        <!-- Rentang Harga per Hari -->
        <div style="margin-bottom: 20px;">
          <h4 style="font-size: 13px; font-weight: 600; margin-bottom: 8px;">Rentang Harga per Hari</h4>
          <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            <button class="chip active" onclick="selectPriceRangeChip(this, 'all')">Semua</button>
            <button class="chip" onclick="selectPriceRangeChip(this, '<50')">Di bawah Rp50.000</button>
            <button class="chip" onclick="selectPriceRangeChip(this, '50-150')">Rp50.000 - Rp150.000</button>
            <button class="chip" onclick="selectPriceRangeChip(this, '>150')">Di atas Rp150.000</button>
          </div>
        </div>

        <!-- Urutan -->
        <div style="margin-bottom: 12px;">
          <h4 style="font-size: 13px; font-weight: 600; margin-bottom: 8px;">Urutan</h4>
          <div style="display: flex; gap: 8px; flex-wrap: wrap;" id="l20-sort-group">
            <button class="chip active" id="l20-sort-terdekat" onclick="selectSortChipL20('Terdekat')">Terdekat</button>
            <button class="chip" id="l20-sort-termurah" onclick="selectSortChipL20('Termurah')">Termurah</button>
            <button class="chip" id="l20-sort-rating" onclick="selectSortChipL20('Rating')">Rating tertinggi</button>
          </div>
        </div>
      </div>

      <div class="modal-footer" style="justify-content: space-between;">
        <button class="btn-ghost" style="font-size: 13px; color: var(--text-muted);" onclick="resetFilterModal()">
          Atur ulang
        </button>
        <!-- Single Amber Button -->
        <button class="btn btn-amber" style="width: auto; padding: 10px 24px;" onclick="applyFilterModal()">
          Terapkan
        </button>
      </div>
    </div>
  </div>
'''

def get_common_modals_and_footer():
    return '''
  <!-- Common Date Picker Modal (for top navbar / filter) -->
  <div id="modal-datepicker" class="modal-backdrop">
    <div class="modal-sheet" style="max-width: 440px;">
      <div class="modal-header">
        <h3 style="font-size: 16px; font-weight: 600;">Pilih Tanggal Sewa</h3>
        <button class="btn-ghost" onclick="closeDatePickerModal()" style="padding: 4px;" title="Tutup">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </button>
      </div>
      <div class="modal-body">
        <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 16px;">
          Minimal sewa adalah 2 hari kalender. Tanggal dihitung per hari kalender, bukan per 24 jam.
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 16px;">
          <div>
            <label class="input-label" style="font-size: 12px;">Tanggal Ambil</label>
            <input type="date" id="nav-date-input-start" class="input-field" value="2026-11-17">
          </div>
          <div>
            <label class="input-label" style="font-size: 12px;">Tanggal Kembali</label>
            <input type="date" id="nav-date-input-end" class="input-field" value="2026-11-18">
          </div>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-amber" onclick="confirmDatePickerModal()">Terapkan Tanggal</button>
      </div>
    </div>
  </div>

  <!-- Common Photo Condition Modal (for L14) -->
  <div id="modal-condition-photos" class="modal-backdrop">
    <div class="modal-sheet" style="max-width: 500px;">
      <div class="modal-header">
        <h3 style="font-size: 16px; font-weight: 600;">Foto Kondisi Awal Barang</h3>
        <button class="btn-ghost" onclick="closeConditionPhotosModal()" style="padding: 4px;" title="Tutup">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </button>
      </div>
      <div class="modal-body">
        <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 14px;">
          Ketuk slot untuk mendokumentasikan kondisi fisik barang saat serah terima. Foto diberi cap waktu otomatis.
        </p>
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; margin-bottom: 16px;">
          <div onclick="simulateConditionPhotoSlot(this, 'Depan')" style="aspect-ratio: 4/3; border: 2px dashed var(--border-color); border-radius: var(--radius-md); display: flex; flex-direction: column; align-items: center; justify-content: center; cursor: pointer; background: #F8FAFC; padding: 12px; text-align: center;">
            <span style="font-size: 24px;">📷</span>
            <span style="font-size: 12px; font-weight: 600; margin-top: 4px;">Tampak Depan</span>
            <span style="font-size: 10px; color: var(--text-muted);">Ketuk untuk ambil foto</span>
          </div>
          <div onclick="simulateConditionPhotoSlot(this, 'Belakang')" style="aspect-ratio: 4/3; border: 2px dashed var(--border-color); border-radius: var(--radius-md); display: flex; flex-direction: column; align-items: center; justify-content: center; cursor: pointer; background: #F8FAFC; padding: 12px; text-align: center;">
            <span style="font-size: 24px;">📷</span>
            <span style="font-size: 12px; font-weight: 600; margin-top: 4px;">Tampak Belakang</span>
            <span style="font-size: 10px; color: var(--text-muted);">Ketuk untuk ambil foto</span>
          </div>
          <div onclick="simulateConditionPhotoSlot(this, 'Samping')" style="aspect-ratio: 4/3; border: 2px dashed var(--border-color); border-radius: var(--radius-md); display: flex; flex-direction: column; align-items: center; justify-content: center; cursor: pointer; background: #F8FAFC; padding: 12px; text-align: center;">
            <span style="font-size: 24px;">📷</span>
            <span style="font-size: 12px; font-weight: 600; margin-top: 4px;">Tampak Samping</span>
            <span style="font-size: 10px; color: var(--text-muted);">Ketuk untuk ambil foto</span>
          </div>
          <div onclick="simulateConditionPhotoSlot(this, 'Aksesori')" style="aspect-ratio: 4/3; border: 2px dashed var(--border-color); border-radius: var(--radius-md); display: flex; flex-direction: column; align-items: center; justify-content: center; cursor: pointer; background: #F8FAFC; padding: 12px; text-align: center;">
            <span style="font-size: 24px;">📷</span>
            <span style="font-size: 12px; font-weight: 600; margin-top: 4px;">Kelengkapan Paket</span>
            <span style="font-size: 10px; color: var(--text-muted);">Ketuk untuk ambil foto</span>
          </div>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-primary" onclick="closeConditionPhotosModal()">Simpan Foto Kondisi</button>
      </div>
    </div>
  </div>

  <!-- Common Toast Component -->
  <div id="toast">Fitur ini belum tersedia di versi demo</div>

  <!-- Common Footer Template -->
  <template id="common-footer-template">
    <footer class="footer">
      <div class="footer-grid">
        <div class="footer-col">
          <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 12px;">
            <svg width="28" height="28" viewBox="0 0 32 32" fill="none">
              <rect width="32" height="32" rx="10" fill="#0F5C63"/>
              <path d="M9 22V10H16C18.2091 10 20 11.7909 20 14C20 16.2091 18.2091 18 16 18H9M15.5 18L21 22" stroke="white" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
              <circle cx="23" cy="9" r="3" fill="#F59E0B"/>
            </svg>
            <span style="font-family: 'Poppins', sans-serif; font-size: 22px; font-weight: 700; color: var(--primary);">rentfy</span>
          </div>
          <p style="font-size: 13px; color: var(--text-muted); line-height: 1.5; max-width: 280px; margin-bottom: 16px;">
            Sewa dan sewakan barang dengan sederhana dan aman. Marketplace peer-to-peer terpercaya untuk berbagai kebutuhanmu.
          </p>
        </div>

        <div class="footer-col">
          <h5>Tentang Rentfy</h5>
          <ul class="footer-links">
            <li><button onclick="navigateTo('L19')">Cara kerja</button></li>
            <li><button onclick="showToast('Fitur Tentang Rentfy belum tersedia di versi demo')">Tentang kami</button></li>
            <li><button onclick="showToast('Fitur Bantuan belum tersedia di versi demo')">Bantuan & FAQ</button></li>
            <li><button onclick="showToast('Fitur Syarat layanan belum tersedia di versi demo')">Syarat layanan</button></li>
            <li><button onclick="showToast('Fitur Kebijakan privasi belum tersedia di versi demo')">Kebijakan privasi</button></li>
          </ul>
        </div>

        <div class="footer-col">
          <h5>Kategori Populer</h5>
          <ul class="footer-links">
            <li><button onclick="navigateTo('L5', {category: 'Kamera dan video'})">Kamera dan video</button></li>
            <li><button onclick="navigateTo('L5', {category: 'Elektronik'})">Elektronik</button></li>
            <li><button onclick="navigateTo('L5', {category: 'Perkakas'})">Perkakas</button></li>
            <li><button onclick="navigateTo('L5', {category: 'Camping dan outdoor'})">Camping dan outdoor</button></li>
            <li><button onclick="navigateTo('L5', {category: 'Olahraga'})">Olahraga</button></li>
          </ul>
        </div>

        <div class="footer-col">
          <h5>Kategori Lainnya</h5>
          <ul class="footer-links">
            <li><button onclick="navigateTo('L5', {category: 'Pesta dan acara'})">Pesta dan acara</button></li>
            <li><button onclick="navigateTo('L5', {category: 'Rumah tangga'})">Rumah tangga</button></li>
            <li><button onclick="navigateTo('L5', {category: 'Semua'})">Semua kategori</button></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        © 2026 Rentfy. Data dalam demo ini adalah contoh untuk prototipe Technopreneurship.
      </div>
    </footer>
  </template>
'''

print("screens_part4.py written successfully")
