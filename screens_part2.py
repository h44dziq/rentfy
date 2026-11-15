# -*- coding: utf-8 -*-
"""
Part 2 of Rentfy screens: L6, L7, L8, L9, L10
"""

def get_l6_screen():
    return '''
  <!-- L6: Item Detail Screen -->
  <section id="screen-L6" class="screen">
    <div id="l6-nav-container"></div>

    <main class="app-container" style="padding-top: 16px; padding-bottom: 24px;">
      <!-- Breadcrumb / Back Navigation Bar -->
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
        <button class="btn-ghost" style="padding: 6px 0; font-weight: 500; display: flex; align-items: center; gap: 6px;" onclick="navigateTo('L5')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
          Kembali ke hasil pencarian
        </button>
        <div style="display: flex; align-items: center; gap: 8px;">
          <button class="nav-icon-btn" style="width: 36px; height: 36px;" onclick="showToast('Tautan berhasil disalin ke papan klip')" title="Bagikan">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="18" cy="5" r="3"></circle><circle cx="6" cy="12" r="3"></circle><circle cx="18" cy="19" r="3"></circle><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line></svg>
          </button>
          <button id="l6-heart-btn" class="nav-icon-btn" style="width: 36px; height: 36px;" onclick="toggleSaveDetailItem()" title="Simpan">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
          </button>
        </div>
      </div>

      <!-- Main Layout: 2 Columns on desktop (Gallery left, Info right) -->
      <div style="display: grid; grid-template-columns: 1.1fr 1fr; gap: 32px; align-items: start;" class="detail-grid-layout">
        
        <!-- Left Column: Gallery & Details -->
        <div>
          <!-- 1. Photo Gallery (4:3) -->
          <div style="background: #FFFFFF; border: 1px solid var(--border-color); border-radius: var(--radius-xl); overflow: hidden; margin-bottom: 24px;">
            <div id="l6-gallery-main" style="width: 100%; aspect-ratio: 4 / 3; display: flex; align-items: center; justify-content: center; position: relative; color: white; padding: 24px; text-align: center;">
              <div class="bg-pattern" style="position: absolute; inset: 0; opacity: 0.15; background-image: radial-gradient(#FFFFFF 1px, transparent 1px); background-size: 14px 14px;"></div>
              <div style="position: relative; z-index: 2;">
                <div id="l6-gallery-icon" style="margin-bottom: 12px; display: inline-flex;"></div>
                <h3 id="l6-gallery-title" style="font-size: 20px; font-weight: 700; color: #FFFFFF; text-shadow: 0 2px 4px rgba(0,0,0,0.5);"></h3>
                <span id="l6-gallery-view-label" class="badge" style="background: rgba(255,255,255,0.25); color: white; margin-top: 8px;">Tampak Depan</span>
              </div>
            </div>
            <!-- Thumbnails selector -->
            <div style="display: flex; gap: 8px; padding: 12px; background: #F8FAFC; border-top: 1px solid var(--border-color); overflow-x: auto;">
              <button class="chip active" style="font-size: 12px; padding: 6px 12px;" onclick="switchGalleryTab(0, 'Tampak Depan')">1. Depan</button>
              <button class="chip" style="font-size: 12px; padding: 6px 12px;" onclick="switchGalleryTab(1, 'Tampak Samping & Optik')">2. Samping</button>
              <button class="chip" style="font-size: 12px; padding: 6px 12px;" onclick="switchGalleryTab(2, 'Kelengkapan Paket')">3. Paket</button>
              <button class="chip" style="font-size: 12px; padding: 6px 12px;" onclick="switchGalleryTab(3, 'Detail Kondisi & Bodi')">4. Kondisi</button>
            </div>
          </div>

          <!-- 4. Protection Banner -->
          <div class="banner banner-info" style="margin-bottom: 24px;">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="flex-shrink: 0;"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path><polyline points="9 12 11 14 15 10"></polyline></svg>
            <div>
              <strong style="font-size: 13px;">Barang dilindungi Program Jaminan Rentfy</strong>
              <div style="font-size: 12px; opacity: 0.9;">Biaya perlindungan Rp10.000 sudah termasuk di rincian. Barang terlindungi dari kerusakan tak terduga selama masa sewa.</div>
            </div>
          </div>

          <!-- 5. Description & Package Contents -->
          <div class="card" style="margin-bottom: 24px;">
            <h3 style="font-size: 16px; font-weight: 600; margin-bottom: 12px;">Deskripsi Barang</h3>
            <p id="l6-item-description" style="font-size: 14px; color: var(--text-main); line-height: 1.6; margin-bottom: 20px;"></p>
            
            <h4 style="font-size: 14px; font-weight: 600; margin-bottom: 8px;">Isi paket yang disertakan:</h4>
            <ul id="l6-package-contents" style="padding-left: 20px; font-size: 13px; color: var(--text-main); line-height: 1.7; margin-bottom: 16px;">
              <!-- Populated by JS -->
            </ul>

            <div style="padding: 12px; background: #F8FAFC; border-radius: var(--radius-md); border-left: 3px solid var(--primary); font-size: 12px; color: var(--text-muted);">
              <strong>Catatan kondisi:</strong> Barang dalam kondisi sangat prima, fungsi 100% normal dan bersih terawat sebelum diserahkan ke penyewa.
            </div>
          </div>

          <!-- 6. Deposit Card -->
          <div class="card" style="background: #FFFBEB; border-color: #FDE68A; margin-bottom: 24px;">
            <div style="display: flex; gap: 12px; align-items: flex-start;">
              <div style="width: 36px; height: 36px; border-radius: 50%; background: #F59E0B; color: white; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
              </div>
              <div>
                <h4 style="font-size: 14px; font-weight: 600; color: #92400E; margin-bottom: 2px;">Deposit <span id="l6-deposit-amount">Rp300.000</span> (Dikembalikan)</h4>
                <p style="font-size: 12px; color: #B45309; line-height: 1.4;">
                  Deposit ditahan dengan aman oleh sistem Rentfy dan akan langsung ditransfer kembali penuh ke saldo/rekening kamu setelah barang diperiksa oleh pemilik.
                </p>
              </div>
            </div>
          </div>

          <!-- 7. Cancellation Policy -->
          <div class="card" style="margin-bottom: 24px;">
            <h3 style="font-size: 15px; font-weight: 600; margin-bottom: 8px;">Kebijakan Pembatalan Fleksibel</h3>
            <p style="font-size: 13px; color: var(--text-muted); line-height: 1.5;">
              Gratis pembatalan sampai 2 hari sebelum masa sewa dimulai. Pembatalan setelah batas waktu akan dikenakan biaya 50% hingga sehari sebelum hari pengambilan.
            </p>
          </div>

          <!-- 10. Approximate Location Map -->
          <div class="card" style="margin-bottom: 24px;">
            <h3 style="font-size: 15px; font-weight: 600; margin-bottom: 4px;">Perkiraan Lokasi Barang</h3>
            <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 12px;">
              📍 <span id="l6-approx-area">Kebayoran Baru, Jakarta Selatan</span>. Lokasi tepat dan nomor kontak pemilik akan dibuka otomatis setelah pesanan diterima dan dibayar.
            </p>
            <div style="width: 100%; height: 200px; border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--border-color); position: relative;">
              <div id="map-l6" style="width: 100%; height: 100%;"></div>
            </div>
          </div>

          <!-- 11. Recent Reviews -->
          <div class="card" style="margin-bottom: 24px;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
              <h3 style="font-size: 16px; font-weight: 600;">Ulasan Penyewa Sebelumnya</h3>
              <div style="display: flex; align-items: center; gap: 4px; font-weight: 600; color: #F59E0B;">
                <span>★ 4.9</span>
                <span style="font-size: 12px; color: var(--text-muted); font-weight: 400;">(42 ulasan)</span>
              </div>
            </div>

            <div style="display: flex; flex-direction: column; gap: 14px;">
              <div style="padding-bottom: 12px; border-bottom: 1px solid var(--border-color);">
                <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                  <strong style="font-size: 13px;">Budi Santoso</strong>
                  <span style="font-size: 11px; color: var(--text-muted);">2 minggu lalu · ★★★★★</span>
                </div>
                <p style="font-size: 13px; color: var(--text-main); line-height: 1.4;">Barang sangat mulus dan berfungsi sangat normal. Mas Dimas komunikatif banget dan fleksibel untuk jam ambil.</p>
              </div>

              <div style="padding-bottom: 12px; border-bottom: 1px solid var(--border-color);">
                <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                  <strong style="font-size: 13px;">Siti Nurhaliza</strong>
                  <span style="font-size: 11px; color: var(--text-muted);">1 bulan lalu · ★★★★★</span>
                </div>
                <p style="font-size: 13px; color: var(--text-main); line-height: 1.4;">Sewa untuk keperluan photoshoot wisuda. Lengkap dengan 2 baterai cadangan jadi aman seharian penuh!</p>
              </div>

              <div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                  <strong style="font-size: 13px;">Reza Pratama</strong>
                  <span style="font-size: 11px; color: var(--text-muted);">1 bulan lalu · ★★★★★</span>
                </div>
                <p style="font-size: 13px; color: var(--text-main); line-height: 1.4;">Proses sewa gampang banget di Rentfy, verifikasi cepat. Barangnya bersih dan terawat layaknya beli baru.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Column: Pricing, Owner Card, Availability Calendar (Sticky on desktop) -->
        <div style="position: sticky; top: 90px;">
          <!-- 2. Header & Pricing Summary Card -->
          <div class="card card-elevated" style="margin-bottom: 20px;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
              <span id="l6-badge-category" class="badge badge-teal">Kamera dan video</span>
              <div style="display: flex; align-items: center; gap: 4px; font-weight: 600; font-size: 13px;">
                <span style="color: #F59E0B;">★</span>
                <span id="l6-item-rating">4.8</span>
                <span style="font-size: 12px; color: var(--text-muted); font-weight: 400;" id="l6-item-reviews">(42)</span>
              </div>
            </div>

            <h1 id="l6-item-title" style="font-size: 22px; font-weight: 700; line-height: 1.3; margin-bottom: 8px;">Kamera mirrorless dan lensa kit</h1>
            <p id="l6-item-area" style="font-size: 13px; color: var(--text-muted); margin-bottom: 16px;">📍 Kebayoran Baru, Jakarta Selatan · 1.2 km</p>

            <div style="padding: 14px; background: var(--primary-soft); border-radius: var(--radius-md); margin-bottom: 20px;">
              <div style="font-size: 12px; color: var(--text-muted);">Harga sewa harian:</div>
              <div style="display: flex; align-items: baseline; gap: 4px;">
                <span id="l6-price-per-day" style="font-family: 'Poppins', sans-serif; font-size: 24px; font-weight: 700; color: var(--primary);">Rp150.000</span>
                <span style="font-size: 13px; color: var(--text-muted);">/ hari kalender</span>
              </div>
            </div>

            <!-- 3. Owner Card -->
            <div style="display: flex; align-items: center; justify-content: space-between; padding: 14px; border: 1px solid var(--border-color); border-radius: var(--radius-md); margin-bottom: 20px;">
              <div style="display: flex; align-items: center; gap: 12px;">
                <div style="width: 44px; height: 44px; border-radius: 50%; background: var(--primary); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 18px;">
                  D
                </div>
                <div>
                  <div style="display: flex; align-items: center; gap: 6px;">
                    <strong style="font-size: 14px;">Dimas Suryo</strong>
                    <span class="badge badge-verified" style="font-size: 10px; padding: 2px 6px;">Terverifikasi</span>
                  </div>
                  <div style="font-size: 11px; color: var(--text-muted); margin-top: 2px;">★ 4.9 · Biasanya membalas cepat</div>
                </div>
              </div>
              <button class="btn btn-outline btn-sm" style="width: auto;" onclick="navigateTo('L10')">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
                Chat
              </button>
            </div>

            <!-- 8. Availability Calendar & Date Selector -->
            <div style="margin-bottom: 20px;">
              <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
                <h4 style="font-size: 14px; font-weight: 600;">Pilih Tanggal Sewa</h4>
                <button class="btn-ghost" style="font-size: 11px; color: var(--primary); padding: 2px 6px;" onclick="resetL6Dates()">Hapus tanggal</button>
              </div>
              <p style="font-size: 11px; color: var(--text-muted); margin-bottom: 10px;">
                * Minimal sewa 2 hari. Masa sewa dihitung per hari kalender, bukan per 24 jam.
              </p>

              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 14px;">
                <div>
                  <label class="input-label" style="font-size: 11px;">Tanggal Ambil</label>
                  <input type="date" id="l6-date-start" class="input-field" value="2026-11-17" onchange="handleL6DateChange()">
                </div>
                <div>
                  <label class="input-label" style="font-size: 11px;">Tanggal Kembali</label>
                  <input type="date" id="l6-date-end" class="input-field" value="2026-11-18" onchange="handleL6DateChange()">
                </div>
              </div>

              <!-- Live Cost Breakdown Calculation in Card -->
              <div style="padding: 14px; background: #F8FAFC; border: 1px solid var(--border-color); border-radius: var(--radius-md);">
                <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 6px;">
                  <span id="l6-calc-days-label">Sewa (2 hari)</span>
                  <span id="l6-calc-sewa-val" style="font-weight: 600;">Rp300.000</span>
                </div>
                <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 6px;">
                  <span>Biaya perlindungan</span>
                  <span style="font-weight: 600;">Rp10.000</span>
                </div>
                <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 10px; color: var(--text-muted);">
                  <span>Deposit (dikembalikan)</span>
                  <span id="l6-calc-deposit-val" style="font-weight: 600;">Rp300.000</span>
                </div>
                <div style="display: flex; justify-content: space-between; font-size: 14px; font-weight: 700; border-top: 1px dashed var(--border-color); padding-top: 8px;">
                  <span>Total bayar nanti</span>
                  <span id="l6-calc-total-val" style="color: var(--primary);">Rp610.000</span>
                </div>
              </div>
            </div>

            <!-- 9. Pricing for all periods -->
            <div style="margin-bottom: 20px;">
              <h4 style="font-size: 13px; font-weight: 600; margin-bottom: 8px; color: var(--text-muted);">Estimasi harga untuk berbagai periode:</h4>
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 12px;">
                <div style="padding: 8px; background: #F8FAFC; border-radius: var(--radius-sm); border: 1px solid var(--border-color);">
                  <div style="color: var(--text-muted);">1 Hari (min. 2 hari)</div>
                  <strong id="l6-period-1d">Rp150.000</strong>
                </div>
                <div style="padding: 8px; background: #F8FAFC; border-radius: var(--radius-sm); border: 1px solid var(--border-color);">
                  <div style="color: var(--text-muted);">2 Hari (Standar)</div>
                  <strong id="l6-period-2d">Rp300.000</strong>
                </div>
                <div style="padding: 8px; background: #F8FAFC; border-radius: var(--radius-sm); border: 1px solid var(--border-color);">
                  <div style="color: var(--text-muted);">3 Hari</div>
                  <strong id="l6-period-3d">Rp450.000</strong>
                </div>
                <div style="padding: 8px; background: var(--primary-soft); border-radius: var(--radius-sm); border: 1px solid rgba(15,92,99,0.2);">
                  <div style="color: var(--primary); font-weight: 600;">1 Minggu (Diskon 10%)</div>
                  <strong id="l6-period-7d" style="color: var(--primary);">Rp945.000</strong>
                </div>
              </div>
            </div>

            <!-- Single Amber Action Button (Desktop) -->
            <button class="btn btn-amber detail-desktop-sidebar-btn" onclick="proceedToRentalSummary()" style="margin-bottom: 10px;">
              Ajukan sewa
            </button>
            <div style="text-align: center;">
              <button class="btn-ghost" style="font-size: 12px; color: var(--text-muted);" onclick="showToast('Fitur pelaporan listing belum tersedia di versi demo')">
                Laporkan listing ini
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- 12. Similar Items Section -->
      <section style="margin-top: 48px;">
        <h3 style="font-size: 18px; font-weight: 600; margin-bottom: 4px;">Barang serupa di kategori ini</h3>
        <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 16px;">Alternatif pilihan lain yang mungkin kamu butuhkan</p>
        <div class="items-grid" id="l6-similar-grid">
          <!-- Populated by JS -->
        </div>
      </section>
    </main>

    <!-- Sticky Bottom Bar on Mobile/Tablet -->
    <div class="detail-bottom-bar">
      <div class="detail-bottom-inner">
        <div>
          <div style="font-size: 11px; color: var(--text-muted);">Total sewa (<span id="l6-bar-days">2 hari</span>):</div>
          <div id="l6-bar-total" style="font-family: 'Poppins', sans-serif; font-size: 18px; font-weight: 700; color: var(--primary);">Rp300.000</div>
        </div>
        <div style="display: flex; gap: 8px;">
          <button class="btn btn-outline btn-sm" style="width: auto;" onclick="navigateTo('L10')">Kirim pesan</button>
          <button class="btn btn-amber btn-sm" style="width: auto; padding: 10px 24px;" onclick="proceedToRentalSummary()">Ajukan sewa</button>
        </div>
      </div>
    </div>

    <div id="l6-footer-container"></div>
  </section>
'''

def get_l7_screen():
    return '''
  <!-- L7: Rental Summary Screen (Step screen, no footer) -->
  <section id="screen-L7" class="screen" style="background: var(--bg-page); min-height: 100vh;">
    <div class="step-container">
      <!-- Back Header -->
      <button class="btn-ghost" style="padding: 6px 0; margin-bottom: 16px; display: flex; align-items: center; gap: 6px;" onclick="navigateTo('L6')">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
        Kembali ke detail barang
      </button>

      <h1 style="font-size: 22px; font-weight: 700; margin-bottom: 4px;">Ringkasan Pengajuan Sewa</h1>
      <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 24px;">Periksa kembali rincian tanggal dan biaya sebelum mengirimkan permintaan ke pemilik</p>

      <!-- Item Card Summary -->
      <div class="card" style="margin-bottom: 20px; display: flex; gap: 16px; align-items: center;">
        <div id="l7-item-thumb" style="width: 80px; height: 60px; border-radius: var(--radius-md); background: #334155; display: flex; align-items: center; justify-content: center; color: white; font-weight: 700; font-size: 12px; flex-shrink: 0; text-align: center; padding: 4px;">
          Foto
        </div>
        <div>
          <span class="badge badge-teal" id="l7-category-badge" style="font-size: 10px; margin-bottom: 4px;">Kamera</span>
          <h3 id="l7-item-title" style="font-size: 14px; font-weight: 600; line-height: 1.3;">Kamera mirrorless dan lensa kit</h3>
          <div id="l7-period-text" style="font-size: 12px; color: var(--text-muted); margin-top: 2px;">17 Nov - 18 Nov 2026 (2 hari kalender)</div>
        </div>
      </div>

      <!-- Optional message for owner -->
      <div class="input-group">
        <label class="input-label" for="l7-message">Pesan untuk pemilik (opsional)</label>
        <textarea id="l7-message" class="input-field" rows="3" placeholder="Contoh: Halo Mas Dimas, barang akan saya gunakan untuk keperluan dokumentasi proyek kuliah..."></textarea>
      </div>

      <!-- Cost Breakdown (Always visible) -->
      <div class="card" style="margin-bottom: 20px;">
        <h3 style="font-size: 14px; font-weight: 600; margin-bottom: 12px; border-bottom: 1px solid var(--border-color); padding-bottom: 8px;">
          Rincian Biaya
        </h3>
        <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 8px;">
          <span id="l7-calc-days-label">Sewa (2 hari kalender)</span>
          <span id="l7-calc-sewa" style="font-weight: 600;">Rp300.000</span>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 8px;">
          <span>Biaya perlindungan Rentfy</span>
          <span style="font-weight: 600;">Rp10.000</span>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 12px; color: var(--text-muted);">
          <span>Deposit (dikembalikan)</span>
          <span id="l7-calc-deposit" style="font-weight: 600;">Rp300.000</span>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 15px; font-weight: 700; border-top: 1px solid var(--border-color); padding-top: 12px;">
          <span>Perkiraan total bayar nanti</span>
          <span id="l7-calc-total" style="color: var(--primary);">Rp610.000</span>
        </div>
        <p style="font-size: 11px; color: var(--text-muted); margin-top: 8px; line-height: 1.4;">
          * Belum ada pembayaran saat ini. Pembayaran baru akan diminta setelah pemilik menerima permintaan sewamu.
        </p>
      </div>

      <!-- Terms Checkbox -->
      <div style="margin-bottom: 24px; display: flex; align-items: flex-start; gap: 10px;">
        <input type="checkbox" id="l7-terms" checked style="margin-top: 3px; accent-color: var(--primary); cursor: pointer;">
        <label for="l7-terms" style="font-size: 12px; color: var(--text-muted); cursor: pointer; line-height: 1.4;">
          Saya menyetujui <a href="javascript:void(0)" onclick="showToast('Syarat layanan dapat dibaca di halaman profil')" style="color: var(--primary); font-weight: 600;">Syarat Layanan</a> dan kebijakan pembatalan Rentfy.
        </label>
      </div>

      <!-- Single Amber Action Button -->
      <button class="btn btn-amber" onclick="submitRentalRequest()">
        Kirim permintaan
      </button>
    </div>
  </section>
'''

def get_l8_screen():
    return '''
  <!-- L8: Request Sent Screen (Success Green, step screen) -->
  <section id="screen-L8" class="screen" style="background: var(--bg-page); min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 24px 16px;">
    <div class="step-container" style="background: #FFFFFF; border: 1px solid var(--border-color); border-radius: var(--radius-xl); box-shadow: var(--shadow-lg); text-align: center; padding: 40px 24px; width: 100%;">
      <!-- Green Success Icon -->
      <div style="width: 72px; height: 72px; border-radius: 50%; background: var(--success-soft); color: var(--success); display: inline-flex; align-items: center; justify-content: center; margin-bottom: 20px;">
        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
      </div>

      <h1 style="font-size: 22px; font-weight: 700; color: var(--text-main); margin-bottom: 8px;">Permintaan Terkirim!</h1>
      <p style="font-size: 14px; color: var(--text-muted); line-height: 1.5; margin-bottom: 24px;">
        Permintaan sewa telah dikirimkan ke pemilik (Dimas). Pemilik akan merespons maksimal dalam 24 jam.
      </p>

      <!-- Info Card Summary -->
      <div style="padding: 16px; background: #F8FAFC; border: 1px solid var(--border-color); border-radius: var(--radius-md); text-align: left; margin-bottom: 28px;">
        <div style="font-size: 12px; color: var(--text-muted); margin-bottom: 2px;">Barang yang diajukan:</div>
        <div id="l8-item-title" style="font-size: 14px; font-weight: 600; margin-bottom: 8px;">Kamera mirrorless dan lensa kit</div>
        <div style="display: flex; justify-content: space-between; font-size: 12px; color: var(--text-muted);">
          <span id="l8-dates">17 Nov - 18 Nov 2026</span>
          <span id="l8-total" style="font-weight: 700; color: var(--primary);">Rp610.000</span>
        </div>
      </div>

      <!-- Actions: 1 Amber button, 1 Secondary outline, 1 Text link -->
      <div style="display: flex; flex-direction: column; gap: 12px;">
        <button class="btn btn-amber" onclick="navigateTo('L9')">
          Lihat pesanan saya
        </button>
        <button class="btn btn-outline" onclick="navigateTo('L10')">
          Kirim pesan ke pemilik
        </button>
        <button class="btn-ghost" style="font-size: 13px;" onclick="navigateTo('L3')">
          Kembali ke beranda
        </button>
      </div>
    </div>
  </section>
'''

def get_l9_screen():
    return '''
  <!-- L9: My Orders Screen -->
  <section id="screen-L9" class="screen">
    <div id="l9-nav-container"></div>

    <main class="app-container" style="padding-top: 24px; padding-bottom: 40px; min-height: 70vh;">
      <h1 style="font-size: 24px; font-weight: 700; margin-bottom: 16px;">Pesanan Saya</h1>

      <!-- Tabs: Berjalan vs Selesai -->
      <div style="display: flex; border-bottom: 2px solid var(--border-color); margin-bottom: 24px;">
        <button id="l9-tab-berjalan" class="btn-ghost" style="font-size: 15px; font-weight: 600; color: var(--primary); border-bottom: 2px solid var(--primary); border-radius: 0; padding: 10px 24px; margin-bottom: -2px;" onclick="switchOrderTab('berjalan')">
          Berjalan <span id="l9-count-berjalan" class="badge badge-teal" style="font-size: 11px; margin-left: 4px;">1</span>
        </button>
        <button id="l9-tab-selesai" class="btn-ghost" style="font-size: 15px; font-weight: 500; color: var(--text-muted); border-bottom: 2px solid transparent; border-radius: 0; padding: 10px 24px; margin-bottom: -2px;" onclick="switchOrderTab('selesai')">
          Selesai <span id="l9-count-selesai" class="badge badge-gray" style="font-size: 11px; margin-left: 4px;">0</span>
        </button>
      </div>

      <!-- Berjalan Tab Content -->
      <div id="l9-content-berjalan">
        <div id="l9-active-order-container">
          <!-- Dynamically populated order card -->
        </div>
      </div>

      <!-- Selesai Tab Content -->
      <div id="l9-content-selesai" style="display: none;">
        <div id="l9-completed-order-container">
          <!-- Empty or completed cards -->
          <div style="text-align: center; padding: 48px 16px;">
            <div style="width: 56px; height: 56px; border-radius: 50%; background: #F1F5F9; color: var(--text-muted); display: inline-flex; align-items: center; justify-content: center; margin-bottom: 12px;">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
            </div>
            <h3 style="font-size: 16px; font-weight: 600; margin-bottom: 4px;">Belum ada pesanan selesai</h3>
            <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 20px;">Pesanan yang telah selesai disewa dan dikembalikan akan muncul di sini.</p>
            <button class="btn btn-outline" style="width: auto; margin: 0 auto;" onclick="navigateTo('L3')">Cari barang</button>
          </div>
        </div>
      </div>
    </main>

    <div id="l9-footer-container"></div>
    <div id="l9-tabs-container"></div>
  </section>
'''

def get_l10_screen():
    return '''
  <!-- L10: Chat with Owner Screen (Step 2 Communication) -->
  <section id="screen-L10" class="screen" style="background: var(--bg-page); min-height: 100vh;">
    <!-- Chat Header App Bar -->
    <header style="background: #FFFFFF; border-bottom: 1px solid var(--border-color); padding: 10px 16px; position: sticky; top: 0; z-index: 90;">
      <div style="max-width: 640px; margin: 0 auto; display: flex; align-items: center; gap: 12px;">
        <button class="btn-ghost" style="padding: 6px;" onclick="navigateBackFromChat()" title="Kembali">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
        </button>
        <div style="width: 38px; height: 38px; border-radius: 50%; background: var(--primary); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 16px;">
          D
        </div>
        <div style="flex: 1;">
          <div style="display: flex; align-items: center; gap: 6px;">
            <strong style="font-size: 14px;">Dimas Suryo</strong>
            <span class="badge badge-verified" style="font-size: 10px; padding: 1px 6px;">Terverifikasi</span>
          </div>
          <div style="font-size: 11px; color: var(--success); font-weight: 500;">● Online · Biasanya membalas cepat</div>
        </div>
      </div>
    </header>

    <main class="app-container" style="padding-top: 12px; padding-bottom: 20px;">
      <!-- Chat Outer Wrapper -->
      <div class="chat-container">
        <!-- Mini Item Context Card -->
        <div style="padding: 10px 14px; background: #F8FAFC; border-bottom: 1px solid var(--border-color); display: flex; align-items: center; justify-content: space-between;">
          <div style="display: flex; align-items: center; gap: 10px;">
            <div id="l10-item-thumb" style="width: 38px; height: 38px; border-radius: var(--radius-sm); background: #334155; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700; text-align: center;">
              Foto
            </div>
            <div>
              <div id="l10-item-title" style="font-size: 13px; font-weight: 600;">Kamera mirrorless dan lensa kit</div>
              <div id="l10-item-dates" style="font-size: 11px; color: var(--text-muted);">17 - 18 Nov 2026 (2 hari)</div>
            </div>
          </div>
          <button class="btn btn-outline btn-sm" style="width: auto; padding: 4px 10px; font-size: 11px;" onclick="navigateTo('L11')">
            Detail pesanan
          </button>
        </div>

        <!-- Safety Banner -->
        <div style="padding: 8px 14px; background: #FEF3C7; border-bottom: 1px solid #FDE68A; font-size: 11px; color: #92400E; display: flex; align-items: center; gap: 8px;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="flex-shrink: 0;"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
          <span>Semua transaksi & pembayaran dilakukan di Rentfy agar dana dan barang tetap terlindungi.</span>
        </div>

        <!-- Chat Messages Scroll List -->
        <div class="chat-messages" id="chat-messages-list">
          <div class="chat-bubble owner">
            Halo Rina! Ada yang bisa saya bantu terkait barang sewa ini? Barang dalam kondisi sangat siap pakai.
            <div class="chat-time">09:15</div>
          </div>
        </div>

        <!-- Quick Reply Chips -->
        <div style="padding: 8px 12px; background: #FFFFFF; border-top: 1px solid var(--border-color); display: flex; gap: 8px; overflow-x: auto; white-space: nowrap;">
          <button class="chip" style="font-size: 11px; padding: 4px 10px;" onclick="sendQuickReply('Apakah masih tersedia?')">Apakah masih tersedia?</button>
          <button class="chip" style="font-size: 11px; padding: 4px 10px;" onclick="sendQuickReply('Boleh ambil jam berapa?')">Boleh ambil jam berapa?</button>
          <button class="chip" style="font-size: 11px; padding: 4px 10px;" onclick="sendQuickReply('Bisa tambah satu hari?')">Bisa tambah satu hari?</button>
        </div>

        <!-- Message Input Box -->
        <div style="padding: 10px 14px; background: #FFFFFF; border-top: 1px solid var(--border-color); display: flex; align-items: center; gap: 8px;">
          <input type="text" id="chat-input" class="input-field" placeholder="Ketik pesan untuk Dimas..." style="padding: 10px 14px; font-size: 13px;" onkeydown="if(event.key==='Enter') sendChatMessage()">
          <button class="btn btn-primary" style="width: 40px; height: 40px; padding: 0; border-radius: 50%; flex-shrink: 0;" onclick="sendChatMessage()" title="Kirim">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
          </button>
        </div>
      </div>
    </main>
  </section>
'''

print("screens_part2.py written successfully")
