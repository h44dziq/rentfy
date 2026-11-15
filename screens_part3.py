# -*- coding: utf-8 -*-
"""
Part 3 of Rentfy screens: L11, L12, L13, L14, L15
"""

def get_l11_screen():
    return '''
  <!-- L11: Order Detail Screen -->
  <section id="screen-L11" class="screen" style="background: var(--bg-page); min-height: 100vh;">
    <div class="step-container" style="max-width: 640px;">
      <!-- Header with back button -->
      <button class="btn-ghost" style="padding: 6px 0; margin-bottom: 16px; display: flex; align-items: center; gap: 6px;" onclick="navigateTo('L9')">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
        Kembali ke pesanan saya
      </button>

      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
        <h1 style="font-size: 20px; font-weight: 700;">Detail Pesanan #RF-20261117</h1>
        <span id="l11-status-badge" class="badge badge-yellow">Menunggu pemilik</span>
      </div>

      <!-- Item Card -->
      <div class="card" style="margin-bottom: 20px; display: flex; gap: 14px; align-items: center;">
        <div id="l11-item-thumb" style="width: 72px; height: 56px; border-radius: var(--radius-md); background: #334155; display: flex; align-items: center; justify-content: center; color: white; font-weight: 700; font-size: 11px; flex-shrink: 0; text-align: center; padding: 4px;">
          Foto
        </div>
        <div style="flex: 1;">
          <h3 id="l11-item-title" style="font-size: 14px; font-weight: 600; line-height: 1.3;">Kamera mirrorless dan lensa kit</h3>
          <div id="l11-item-dates" style="font-size: 12px; color: var(--text-muted); margin-top: 2px;">17 Nov - 18 Nov 2026 (2 hari kalender)</div>
        </div>
      </div>

      <!-- 5-Step Vertical Timeline -->
      <div class="card" style="margin-bottom: 20px;">
        <h3 style="font-size: 15px; font-weight: 600; margin-bottom: 16px;">Garis Waktu Penyewaan</h3>
        <div class="timeline" id="l11-timeline">
          <!-- Step 1 -->
          <div class="timeline-item" id="tl-step-1">
            <div class="timeline-line"></div>
            <div class="timeline-icon">1</div>
            <div class="timeline-content">
              <div class="timeline-title">Permintaan terkirim</div>
              <div class="timeline-desc">Permintaan sewa dikirim ke pemilik (17 Nov 2026, 09:30 WIB)</div>
            </div>
          </div>
          <!-- Step 2 -->
          <div class="timeline-item" id="tl-step-2">
            <div class="timeline-line"></div>
            <div class="timeline-icon">2</div>
            <div class="timeline-content">
              <div class="timeline-title">Permintaan diterima</div>
              <div class="timeline-desc">Pemilik menyetujui ketersediaan barang sewa</div>
            </div>
          </div>
          <!-- Step 3 -->
          <div class="timeline-item" id="tl-step-3">
            <div class="timeline-line"></div>
            <div class="timeline-icon">3</div>
            <div class="timeline-content">
              <div class="timeline-title">Pembayaran (Dana ditahan)</div>
              <div class="timeline-desc">Verifikasi identitas dan pembayaran aman di Rentfy</div>
            </div>
          </div>
          <!-- Step 4 -->
          <div class="timeline-item" id="tl-step-4">
            <div class="timeline-line"></div>
            <div class="timeline-icon">4</div>
            <div class="timeline-content">
              <div class="timeline-title">Pengambilan barang</div>
              <div class="timeline-desc">Pengecekan kondisi fisik dan konfirmasi serah terima</div>
            </div>
          </div>
          <!-- Step 5 -->
          <div class="timeline-item" id="tl-step-5">
            <div class="timeline-line"></div>
            <div class="timeline-icon">5</div>
            <div class="timeline-content">
              <div class="timeline-title">Pengembalian & Deposit</div>
              <div class="timeline-desc">Pemeriksaan kondisi barang dan pengembalian deposit penuh</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Cost Breakdown Card -->
      <div class="card" style="margin-bottom: 20px;">
        <h3 style="font-size: 14px; font-weight: 600; margin-bottom: 12px; border-bottom: 1px solid var(--border-color); padding-bottom: 8px;">
          Rincian Pembayaran
        </h3>
        <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 6px;">
          <span id="l11-calc-days-label">Sewa (2 hari kalender)</span>
          <span id="l11-calc-sewa" style="font-weight: 600;">Rp300.000</span>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 6px;">
          <span>Biaya perlindungan Rentfy</span>
          <span style="font-weight: 600;">Rp10.000</span>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 10px; color: var(--text-muted);">
          <span>Deposit (dikembalikan)</span>
          <span id="l11-calc-deposit" style="font-weight: 600;">Rp300.000</span>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 15px; font-weight: 700; border-top: 1px solid var(--border-color); padding-top: 10px;">
          <span>Total</span>
          <span id="l11-calc-total" style="color: var(--primary);">Rp610.000</span>
        </div>
      </div>

      <!-- Location and Owner Contact Card -->
      <div class="card" style="margin-bottom: 24px;" id="l11-contact-card">
        <!-- Will toggle between locked and unlocked based on status -->
        <div id="l11-contact-locked">
          <div style="display: flex; align-items: center; gap: 10px; color: var(--text-muted); font-size: 13px;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
            <span>Alamat tepat dan kontak WhatsApp/telepon pemilik akan terbuka otomatis setelah pembayaran diverifikasi.</span>
          </div>
        </div>
        <div id="l11-contact-unlocked" style="display: none;">
          <h4 style="font-size: 14px; font-weight: 600; margin-bottom: 8px;">Informasi Pengambilan & Kontak</h4>
          <div style="font-size: 13px; line-height: 1.6;">
            <div><strong>Pemilik:</strong> Dimas Suryo (0812-9876-5432)</div>
            <div><strong>Alamat Pengambilan:</strong> Jl. Senopati No. 42, Kebayoran Baru, Jakarta Selatan</div>
            <div><strong>Waktu Pengambilan:</strong> Pukul 10:00 WIB</div>
          </div>
        </div>
      </div>

      <!-- Dynamic Primary Action Button (Only ONE amber button) -->
      <div id="l11-action-container" style="margin-bottom: 12px;">
        <!-- Injected by JS based on current status -->
      </div>

      <div style="text-align: center;">
        <button class="btn-ghost" style="font-size: 12px; color: var(--text-muted);" onclick="showToast('Fitur pelaporan masalah belum tersedia di versi demo')">
          Laporkan masalah dengan pesanan ini
        </button>
      </div>
    </div>
  </section>
'''

def get_l12_screen():
    return '''
  <!-- L12: Identity Verification Screen (Step 3) -->
  <section id="screen-L12" class="screen" style="background: var(--bg-page); min-height: 100vh;">
    <div class="step-container">
      <button class="btn-ghost" style="padding: 6px 0; margin-bottom: 16px; display: flex; align-items: center; gap: 6px;" onclick="navigateTo('L11')">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
        Kembali ke detail pesanan
      </button>

      <!-- Banner info -->
      <div class="banner banner-info" style="margin-bottom: 20px;">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="flex-shrink: 0;"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
        <span style="font-size: 13px;">Permintaan diterima! Lakukan verifikasi identitas singkat agar pembayaran sewa dapat dilanjutkan.</span>
      </div>

      <!-- 3-Step Stepper -->
      <div class="stepper">
        <div class="step-node active" id="l12-node-1">
          <div class="step-circle">1</div>
          <span class="step-label">Foto KTP</span>
        </div>
        <div class="step-node" id="l12-node-2">
          <div class="step-circle">2</div>
          <span class="step-label">Selfie KTP</span>
        </div>
        <div class="step-node" id="l12-node-3">
          <div class="step-circle">3</div>
          <span class="step-label">Tinjau</span>
        </div>
      </div>

      <!-- Step 1 Content: Foto KTP -->
      <div id="l12-step-1" class="card" style="text-align: center; padding: 24px; margin-bottom: 20px;">
        <h3 style="font-size: 16px; font-weight: 600; margin-bottom: 4px;">Posisikan KTP di Dalam Bingkai</h3>
        <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 20px;">Pastikan semua data dan foto pada e-KTP terbaca jelas dan tidak terkena pantulan cahaya</p>

        <!-- Camera viewfinder frame -->
        <div style="width: 100%; max-width: 340px; height: 200px; margin: 0 auto 16px; border: 2px dashed var(--primary); border-radius: var(--radius-md); position: relative; display: flex; flex-direction: column; align-items: center; justify-content: center; background: #F8FAFC;">
          <!-- Corner markers -->
          <div style="position: absolute; top: 8px; left: 8px; width: 16px; height: 16px; border-top: 3px solid var(--primary); border-left: 3px solid var(--primary);"></div>
          <div style="position: absolute; top: 8px; right: 8px; width: 16px; height: 16px; border-top: 3px solid var(--primary); border-right: 3px solid var(--primary);"></div>
          <div style="position: absolute; bottom: 8px; left: 8px; width: 16px; height: 16px; border-bottom: 3px solid var(--primary); border-left: 3px solid var(--primary);"></div>
          <div style="position: absolute; bottom: 8px; right: 8px; width: 16px; height: 16px; border-bottom: 3px solid var(--primary); border-right: 3px solid var(--primary);"></div>
          
          <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="1.5" style="margin-bottom: 8px;"><rect x="2" y="5" width="20" height="14" rx="2"></rect><line x1="2" y1="10" x2="22" y2="10"></line></svg>
          <span style="font-size: 12px; color: var(--text-muted);">Area Foto e-KTP</span>
        </div>

        <button class="btn-ghost" style="font-size: 12px; color: var(--primary); font-weight: 500;" onclick="showToast('Foto KTP contoh dari galeri berhasil dimuat')">
          📁 Pilih dari galeri ponsel
        </button>
      </div>

      <!-- Step 2 Content: Selfie dengan KTP (Hidden initially) -->
      <div id="l12-step-2" class="card" style="display: none; text-align: center; padding: 24px; margin-bottom: 20px;">
        <h3 style="font-size: 16px; font-weight: 600; margin-bottom: 4px;">Selfie Memegang KTP</h3>
        <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 20px;">Posisikan wajah dan KTP berdampingan di dalam area panduan kamera</p>

        <div style="width: 100%; max-width: 340px; height: 220px; margin: 0 auto 16px; border: 2px dashed var(--primary); border-radius: var(--radius-md); position: relative; display: flex; flex-direction: column; align-items: center; justify-content: center; background: #F8FAFC;">
          <!-- Corner markers -->
          <div style="position: absolute; top: 8px; left: 8px; width: 16px; height: 16px; border-top: 3px solid var(--primary); border-left: 3px solid var(--primary);"></div>
          <div style="position: absolute; top: 8px; right: 8px; width: 16px; height: 16px; border-top: 3px solid var(--primary); border-right: 3px solid var(--primary);"></div>
          <div style="position: absolute; bottom: 8px; left: 8px; width: 16px; height: 16px; border-bottom: 3px solid var(--primary); border-left: 3px solid var(--primary);"></div>
          <div style="position: absolute; bottom: 8px; right: 8px; width: 16px; height: 16px; border-bottom: 3px solid var(--primary); border-right: 3px solid var(--primary);"></div>

          <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="1.5" style="margin-bottom: 8px;"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
          <span style="font-size: 12px; color: var(--text-muted);">Panduan Wajah & KTP</span>
        </div>

        <button class="btn-ghost" style="font-size: 12px; color: var(--primary); font-weight: 500;" onclick="showToast('Foto selfie contoh dari galeri berhasil dimuat')">
          📁 Pilih dari galeri ponsel
        </button>
      </div>

      <!-- Step 3 Content: Tinjau (Hidden initially) -->
      <div id="l12-step-3" class="card" style="display: none; padding: 20px; margin-bottom: 20px;">
        <h3 style="font-size: 16px; font-weight: 600; margin-bottom: 12px;">Tinjau Data Verifikasi</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 16px;">
          <div style="padding: 12px; background: #F8FAFC; border: 1px solid var(--border-color); border-radius: var(--radius-md); text-align: center;">
            <div style="color: var(--success); font-weight: 600; font-size: 12px; margin-bottom: 4px;">✓ Foto KTP Terunggah</div>
            <div style="font-size: 11px; color: var(--text-muted);">Format JPG · 1.2 MB</div>
          </div>
          <div style="padding: 12px; background: #F8FAFC; border: 1px solid var(--border-color); border-radius: var(--radius-md); text-align: center;">
            <div style="color: var(--success); font-weight: 600; font-size: 12px; margin-bottom: 4px;">✓ Selfie Terunggah</div>
            <div style="font-size: 11px; color: var(--text-muted);">Format JPG · 2.1 MB</div>
          </div>
        </div>

        <div style="padding: 12px; background: #F8FAFC; border-radius: var(--radius-md); font-size: 13px;">
          <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
            <span style="color: var(--text-muted);">Nama Sesuai KTP:</span>
            <strong>Rina Salsabila</strong>
          </div>
          <div style="display: flex; justify-content: space-between;">
            <span style="color: var(--text-muted);">NIK:</span>
            <strong>3171**********01</strong>
          </div>
        </div>
      </div>

      <!-- Security guarantee card -->
      <div style="display: flex; align-items: center; gap: 10px; padding: 12px; background: #F8FAFC; border: 1px solid var(--border-color); border-radius: var(--radius-md); margin-bottom: 24px; font-size: 12px; color: var(--text-muted);">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="flex-shrink: 0;"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
        <span>Data identitas dipakai semata-mata untuk verifikasi keamanan komunitas dan disimpan terenkripsi dengan aman.</span>
      </div>

      <!-- Single Amber Button (label adapts per step) -->
      <button id="l12-action-btn" class="btn btn-amber" onclick="handleL12NextStep()">
        Ambil foto KTP
      </button>
    </div>

    <!-- 2s Success Green Overlay Modal for L12 -->
    <div id="l12-success-modal" class="modal-backdrop">
      <div class="modal-sheet" style="max-width: 400px; text-align: center; padding: 36px 24px;">
        <div style="width: 64px; height: 64px; border-radius: 50%; background: var(--success-soft); color: var(--success); display: inline-flex; align-items: center; justify-content: center; margin-bottom: 16px;">
          <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
        </div>
        <h3 style="font-size: 18px; font-weight: 700; margin-bottom: 6px;">Identitas Terverifikasi!</h3>
        <p style="font-size: 13px; color: var(--text-muted); line-height: 1.4;">Data verifikasi kamu telah disetujui. Mengalihkan ke pembayaran...</p>
      </div>
    </div>
  </section>
'''

def get_l13_screen():
    return '''
  <!-- L13: Payment Screen -->
  <section id="screen-L13" class="screen" style="background: var(--bg-page); min-height: 100vh;">
    <div class="step-container" style="max-width: 540px;">
      <button class="btn-ghost" style="padding: 6px 0; margin-bottom: 16px; display: flex; align-items: center; gap: 6px;" onclick="navigateTo('L11')">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
        Kembali ke detail pesanan
      </button>

      <h1 style="font-size: 22px; font-weight: 700; margin-bottom: 4px;">Pembayaran Sewa</h1>
      <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 20px;">Selesaikan pembayaran agar pesanan siap untuk diambil</p>

      <!-- Item Card Summary -->
      <div class="card" style="margin-bottom: 20px; display: flex; gap: 14px; align-items: center;">
        <div id="l13-item-thumb" style="width: 72px; height: 56px; border-radius: var(--radius-md); background: #334155; display: flex; align-items: center; justify-content: center; color: white; font-weight: 700; font-size: 11px; flex-shrink: 0; text-align: center; padding: 4px;">
          Foto
        </div>
        <div>
          <h3 id="l13-item-title" style="font-size: 14px; font-weight: 600; line-height: 1.3;">Kamera mirrorless dan lensa kit</h3>
          <div id="l13-item-dates" style="font-size: 12px; color: var(--text-muted); margin-top: 2px;">17 Nov - 18 Nov 2026 (2 hari kalender)</div>
        </div>
      </div>

      <!-- Cost Breakdown -->
      <div class="card" style="margin-bottom: 20px;">
        <h3 style="font-size: 14px; font-weight: 600; margin-bottom: 12px; border-bottom: 1px solid var(--border-color); padding-bottom: 8px;">
          Rincian Tagihan
        </h3>
        <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 6px;">
          <span id="l13-calc-days-label">Sewa (2 hari kalender)</span>
          <span id="l13-calc-sewa" style="font-weight: 600;">Rp300.000</span>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 6px;">
          <span>Biaya perlindungan Rentfy</span>
          <span style="font-weight: 600;">Rp10.000</span>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 10px; color: var(--text-muted);">
          <span>Deposit (dikembalikan)</span>
          <span id="l13-calc-deposit" style="font-weight: 600;">Rp300.000</span>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 16px; font-weight: 700; border-top: 1px solid var(--border-color); padding-top: 10px;">
          <span>Total Bayar Sekarang</span>
          <span id="l13-calc-total" style="color: var(--primary);">Rp610.000</span>
        </div>
      </div>

      <!-- Payment Method Selection -->
      <div class="card" style="margin-bottom: 20px;">
        <h3 style="font-size: 14px; font-weight: 600; margin-bottom: 12px;">Pilih Metode Pembayaran</h3>
        <div style="display: flex; flex-direction: column; gap: 10px;">
          <label style="display: flex; align-items: center; justify-content: space-between; padding: 12px; border: 1px solid var(--primary); border-radius: var(--radius-md); background: var(--primary-soft); cursor: pointer;">
            <div style="display: flex; align-items: center; gap: 10px;">
              <input type="radio" name="paymethod" value="qris" checked style="accent-color: var(--primary);">
              <div>
                <strong style="font-size: 13px;">QRIS (Instant)</strong>
                <div style="font-size: 11px; color: var(--text-muted);">Semua e-wallet & mobile banking (GoPay, BCA, Mandiri, dll)</div>
              </div>
            </div>
            <span class="badge badge-teal" style="font-size: 10px;">Rekomendasi</span>
          </label>

          <label style="display: flex; align-items: center; justify-content: space-between; padding: 12px; border: 1px solid var(--border-color); border-radius: var(--radius-md); cursor: pointer;">
            <div style="display: flex; align-items: center; gap: 10px;">
              <input type="radio" name="paymethod" value="va" style="accent-color: var(--primary);">
              <div>
                <strong style="font-size: 13px;">Transfer Virtual Account</strong>
                <div style="font-size: 11px; color: var(--text-muted);">BCA, Mandiri, BNI, BRI</div>
              </div>
            </div>
          </label>

          <label style="display: flex; align-items: center; justify-content: space-between; padding: 12px; border: 1px solid var(--border-color); border-radius: var(--radius-md); cursor: pointer;">
            <div style="display: flex; align-items: center; gap: 10px;">
              <input type="radio" name="paymethod" value="ewallet" style="accent-color: var(--primary);">
              <div>
                <strong style="font-size: 13px;">Dompet Digital Langsung</strong>
                <div style="font-size: 11px; color: var(--text-muted);">ShopeePay, OVO, DANA</div>
              </div>
            </div>
          </label>
        </div>
      </div>

      <!-- Safety Escrow Note -->
      <div style="display: flex; align-items: center; gap: 10px; padding: 12px; background: #F8FAFC; border: 1px solid var(--border-color); border-radius: var(--radius-md); margin-bottom: 24px; font-size: 12px; color: var(--text-muted); line-height: 1.4;">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="flex-shrink: 0;"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
        <span>Bayar di dalam Rentfy supaya perlindungan tetap berlaku. Dana ditahan dengan aman oleh sistem sampai masa sewa selesai dan barang kembali.</span>
      </div>

      <!-- Single Amber Button -->
      <button class="btn btn-amber" onclick="startQrisPaymentSimulation()">
        Bayar sekarang
      </button>
    </div>

    <!-- QRIS Simulation Modal (Active for 3s, then shows payment success) -->
    <div id="l13-qris-modal" class="modal-backdrop">
      <div class="modal-sheet" style="max-width: 420px; text-align: center; padding: 28px 20px;">
        <div id="l13-qris-waiting-view">
          <h3 style="font-size: 18px; font-weight: 700; margin-bottom: 4px;">Pindai Kode QRIS</h3>
          <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 16px;">Buka aplikasi mobile banking atau e-wallet kamu untuk memindai</p>
          
          <!-- Styled QR code mock SVG -->
          <div style="width: 200px; height: 200px; margin: 0 auto 16px; background: white; padding: 12px; border: 2px solid var(--border-color); border-radius: var(--radius-md); box-shadow: var(--shadow-sm); display: flex; align-items: center; justify-content: center;">
            <svg width="176" height="176" viewBox="0 0 176 176" fill="none">
              <!-- QR Patterns -->
              <rect x="0" y="0" width="56" height="56" rx="6" fill="#1F2937"/>
              <rect x="12" y="12" width="32" height="32" rx="3" fill="white"/>
              <rect x="20" y="20" width="16" height="16" rx="2" fill="#1F2937"/>

              <rect x="120" y="0" width="56" height="56" rx="6" fill="#1F2937"/>
              <rect x="132" y="12" width="32" height="32" rx="3" fill="white"/>
              <rect x="140" y="20" width="16" height="16" rx="2" fill="#1F2937"/>

              <rect x="0" y="120" width="56" height="56" rx="6" fill="#1F2937"/>
              <rect x="12" y="132" width="32" height="32" rx="3" fill="white"/>
              <rect x="20" y="140" width="16" height="16" rx="2" fill="#1F2937"/>

              <!-- Dots -->
              <rect x="70" y="10" width="14" height="14" rx="2" fill="#1F2937"/>
              <rect x="92" y="24" width="14" height="14" rx="2" fill="#1F2937"/>
              <rect x="70" y="44" width="14" height="14" rx="2" fill="#1F2937"/>
              <rect x="18" y="74" width="14" height="14" rx="2" fill="#1F2937"/>
              <rect x="42" y="88" width="14" height="14" rx="2" fill="#1F2937"/>
              <rect x="74" y="74" width="28" height="28" rx="4" fill="#0F5C63"/>
              <circle cx="88" cy="88" r="6" fill="white"/>
              <rect x="114" y="74" width="14" height="14" rx="2" fill="#1F2937"/>
              <rect x="144" y="92" width="14" height="14" rx="2" fill="#1F2937"/>
              <rect x="70" y="120" width="14" height="14" rx="2" fill="#1F2937"/>
              <rect x="94" y="140" width="14" height="14" rx="2" fill="#1F2937"/>
              <rect x="124" y="124" width="20" height="20" rx="3" fill="#1F2937"/>
              <rect x="148" y="148" width="16" height="16" rx="2" fill="#1F2937"/>
            </svg>
          </div>

          <div style="font-size: 13px; font-weight: 600; margin-bottom: 4px;">Total Tagihan: <span id="l13-qris-total" style="color: var(--primary);">Rp610.000</span></div>
          <div style="font-size: 11px; color: var(--text-muted); display: flex; align-items: center; justify-content: center; gap: 6px;">
            <span style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: var(--accent); animation: pulse 1.5s infinite;"></span>
            Menunggu konfirmasi pembayaran otomatis (3 detik)...
          </div>
        </div>

        <!-- Payment Success State inside Modal -->
        <div id="l13-qris-success-view" style="display: none;">
          <div style="width: 64px; height: 64px; border-radius: 50%; background: var(--success-soft); color: var(--success); display: inline-flex; align-items: center; justify-content: center; margin-bottom: 16px;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
          </div>
          <h3 style="font-size: 20px; font-weight: 700; margin-bottom: 6px;">Pembayaran Berhasil!</h3>
          <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 20px;">Dana sewa & deposit telah ditahan dengan aman oleh Rentfy.</p>

          <div style="padding: 14px; background: #F8FAFC; border: 1px solid var(--border-color); border-radius: var(--radius-md); text-align: left; margin-bottom: 24px; font-size: 12px; line-height: 1.6;">
            <div><strong>Lokasi Pengambilan:</strong> Jl. Senopati No. 42, Kebayoran Baru, Jakarta Selatan</div>
            <div><strong>Waktu Pengambilan:</strong> Hari ini, pukul 10:00 WIB</div>
            <div><strong>Kontak Pemilik:</strong> Dimas Suryo (0812-9876-5432)</div>
          </div>

          <button class="btn btn-primary" onclick="finishPaymentToDetail()">
            Lihat pesanan saya
          </button>
        </div>
      </div>
    </div>
  </section>
'''

def get_l14_screen():
    return '''
  <!-- L14: Item Pickup Screen (Step 4) -->
  <section id="screen-L14" class="screen" style="background: var(--bg-page); min-height: 100vh;">
    <div class="step-container" style="max-width: 640px;">
      <button class="btn-ghost" style="padding: 6px 0; margin-bottom: 16px; display: flex; align-items: center; gap: 6px;" onclick="navigateTo('L11')">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
        Kembali ke detail pesanan
      </button>

      <h1 style="font-size: 22px; font-weight: 700; margin-bottom: 4px;">Pengambilan Barang</h1>
      <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 20px;">Temui pemilik di lokasi yang disepakati dan periksa kondisi barang</p>

      <!-- Exact Location Card & Map -->
      <div class="card" style="margin-bottom: 20px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
          <h3 style="font-size: 15px; font-weight: 600;">Titik Temu Pengambilan</h3>
          <span class="badge badge-teal">Siap Diambil</span>
        </div>

        <div style="width: 100%; height: 220px; border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--border-color); margin-bottom: 14px; position: relative;">
          <div id="map-l14" style="width: 100%; height: 100%;"></div>
        </div>

        <div style="font-size: 13px; line-height: 1.6; margin-bottom: 14px;">
          <div><strong>Alamat:</strong> Jl. Senopati No. 42, Kebayoran Baru, Jakarta Selatan</div>
          <div><strong>Waktu Ambil:</strong> Hari ini, pukul 10:00 WIB</div>
          <div><strong>Pemilik:</strong> Dimas Suryo (0812-9876-5432)</div>
        </div>

        <button class="btn btn-outline btn-sm" onclick="navigateTo('L10')">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
          Kirim pesan ke Dimas
        </button>
      </div>

      <!-- Calendar day info banner -->
      <div class="banner banner-info" style="margin-bottom: 16px;">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="flex-shrink: 0;"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
        <span style="font-size: 12px;">Masa sewa dihitung per hari kalender, bukan per 24 jam. Hari sewa pertama terhitung mulai hari ini.</span>
      </div>

      <!-- Warning inspection banner -->
      <div class="banner banner-warning" style="margin-bottom: 24px;">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="flex-shrink: 0;"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
        <span style="font-size: 12px;">Periksa kondisi fisik dan fungsi barang bersama pemilik sebelum meninggalkan lokasi pengambilan.</span>
      </div>

      <!-- Condition Photos Option -->
      <div style="margin-bottom: 24px;">
        <button class="btn btn-outline" onclick="openConditionPhotosModal()">
          📷 Ambil foto kondisi barang (Opsional)
        </button>
      </div>

      <!-- Single Amber Button -->
      <button class="btn btn-amber" onclick="confirmItemReceivedL14()">
        Barang sudah saya terima
      </button>
    </div>
  </section>
'''

def get_l15_screen():
    return '''
  <!-- L15: Currently Renting Screen (Step 5) -->
  <section id="screen-L15" class="screen" style="background: var(--bg-page); min-height: 100vh;">
    <div class="step-container" style="max-width: 640px;">
      <button class="btn-ghost" style="padding: 6px 0; margin-bottom: 16px; display: flex; align-items: center; gap: 6px;" onclick="navigateTo('L11')">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
        Kembali ke detail pesanan
      </button>

      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
        <h1 style="font-size: 22px; font-weight: 700;">Status Sewa Aktif</h1>
        <span class="badge badge-teal">Sedang Disewa</span>
      </div>

      <!-- Countdown Card -->
      <div class="card" style="background: linear-gradient(135deg, #0F5C63, #0A3F44); color: white; padding: 24px; margin-bottom: 20px; text-align: center;">
        <span class="badge" style="background: rgba(255,255,255,0.2); color: white; margin-bottom: 10px;">Sisa 1 Hari Sewa</span>
        <h2 style="font-size: 20px; font-weight: 700; color: white; margin-bottom: 6px;">Kembalikan paling lambat:</h2>
        <div id="l15-return-time" style="font-family: 'Poppins', sans-serif; font-size: 18px; font-weight: 600; color: #FDE68A;">
          18 Nov 2026, pukul 20:00 WIB
        </div>
      </div>

      <!-- Late Fee Warning Banner -->
      <div class="banner banner-warning" style="margin-bottom: 20px;">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="flex-shrink: 0;"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
        <span style="font-size: 12px;">Kembalikan tepat waktu di hari terakhir sewa untuk menghindari denda keterlambatan Rp50.000/hari.</span>
      </div>

      <!-- Care Tips Card -->
      <div class="card" style="margin-bottom: 24px;">
        <h3 style="font-size: 15px; font-weight: 600; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
          <span>💡 Tips Merawat Barang Sewaan</span>
        </h3>
        <ul style="padding-left: 20px; font-size: 13px; color: var(--text-main); line-height: 1.6;">
          <li>Simpan di tempat kering dan jauh dari paparan sinar matahari terik langsung.</li>
          <li>Hindari air, cipratan cairan kimia, dan benturan keras pada bodi serta lensa.</li>
          <li>Gunakan selalu strap leher/pengaman saat mengoperasikan perangkat.</li>
        </ul>
      </div>

      <!-- Support and Owner Chat -->
      <div style="display: flex; gap: 12px; margin-bottom: 24px;">
        <button class="btn btn-outline" onclick="navigateTo('L10')">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
          Kirim pesan ke pemilik
        </button>
      </div>

      <!-- Single Amber Action Button -->
      <button class="btn btn-amber" onclick="navigateTo('L16')">
        Kembalikan barang
      </button>

      <div style="text-align: center; margin-top: 14px;">
        <button class="btn-ghost" style="font-size: 12px; color: var(--text-muted);" onclick="showToast('Fitur pelaporan kendala teknis belum tersedia di versi demo')">
          Laporkan kendala teknis atau kerusakan
        </button>
      </div>
    </div>
  </section>
'''

print("screens_part3.py written successfully")
