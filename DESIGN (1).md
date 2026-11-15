Brief MVP prototipe Rentfy (sisi penyewa)
Kelompok 4 · Technopreneurship · Versi 2 · 15 November 2026 · Pendamping Brief UI Rentfy
1. Tujuan dan ruang lingkup
Brief ini mendefinisikan prototipe demo yang bisa diklik untuk Rentfy, khusus sisi penyewa. Hasilnya berupa website yang bisa dibuka di browser, bukan sekadar mockup. Tujuannya mencoba alur dan tampilan, jadi tidak ada logika sungguhan: tidak ada akun asli, validasi, pembayaran, atau basis data. Semua data statis. Hanya tombol penting pembentuk alur yang berfungsi, sedangkan tombol lain menampilkan toast "Fitur ini belum tersedia di versi demo". Pencarian dan kategori tetap bekerja untuk banyak kasus lewat katalog contoh.
Target pengguna: masyarakat umum, bukan hanya mahasiswa. Konsepnya mirip Hygglo: siapa saja bisa menyewa dan menyewakan barang yang layak sewa, mulai dari kamera sampai perkakas, dengan transaksi yang aman. Pencarian bekerja untuk berbagai kata kunci dan kategori, dan "camera" hanyalah salah satu contoh.
Platform: website biasa yang dibuka di browser dengan lebar penuh, bukan mockup di dalam bingkai ponsel. Tampilan utamanya desktop-first seperti Hygglo, lalu menyesuaikan otomatis (responsif) ke tablet dan ponsel.
Lebar layar
Navigasi
Grid kartu
Kolom cari
Desktop (1024 px ke atas)
Navbar atas, konten maksimal 1120 px dan dipusatkan
4 kolom
Satu baris
Tablet (640 sampai 1023 px)
Navbar atas ringkas
3 kolom
Dua baris
Ponsel (di bawah 640 px)
App bar dan tab bar bawah
2 kolom
Dua baris
Di desktop, layar bertahap (L7, L12 sampai L17) dan form (L1, L2) dipusatkan dengan lebar maksimal 480 sampai 640 px, sedangkan bottom sheet (L4, L20) tampil sebagai modal di tengah layar. Tab bar bawah hanya muncul di lebar ponsel.
Yang dikerjakan sekarang:
• Login dan daftar (tanpa verifikasi; verifikasi identitas baru diminta saat pembayaran)
• Beranda bergaya e-commerce
• Pencarian dengan pemilihan lokasi
• Hasil pencarian dan hasil per kategori, pemilik terdekat di atas
• Detail barang
• Ajukan sewa dan chat dengan pemilik
• Verifikasi identitas dan pembayaran di dalam Rentfy
• Pengambilan barang
• Penggunaan dan pengembalian barang
• Pesanan saya dan detail pesanan dengan garis waktu
Tambahan untuk demo: Profil statis, Cara kerja Rentfy, filter (bottom sheet), dan ikon simpan yang bisa berganti tampilan. Semuanya murah dibuat dan membuat demo terasa utuh.
Yang ditunda: mode pemilik dan admin. Aksi pemilik (menerima permintaan, menandai barang sudah diambil, mengecek pengembalian) tidak ada di versi ini: tidak ada layar, tombol, maupun pita Demo untuk itu. Perubahan status yang biasanya berasal dari pemilik berjalan otomatis di sisi penyewa (lihat bagian 5).
Keputusan bentuk hasil: website HTML yang dibuka di browser, memakai peta sungguhan (Leaflet dengan tile OpenStreetMap) dan foto stok bebas lisensi yang disimpan lokal di folder proyek.
Aturan satu website: semua tombol dan tautan hanya bergerak di dalam website ini (pindah layar, buka sheet, atau toast). Tidak ada tautan keluar: tanpa target _blank, tanpa tautan ke situs lain, tanpa mailto, tel, WhatsApp, atau Google Maps. Atribusi peta tampil sebagai teks biasa, bukan tautan.
Tampilan visual mengikuti token di Brief UI Rentfy (teal #0F5C63, amber #F59E0B, Poppins dan Inter, lebar desktop 1440 px sebagai tampilan utama dan 390 px untuk tampilan responsif di ponsel). Bahasa antarmuka dibuat santai tetapi sopan dan netral untuk semua usia, tanpa istilah khas kampus.
2. Referensi
Referensi berasal dari tiga tangkapan Hygglo (marketplace sewa barang): pop-up lokasi, halaman hasil pencarian "camera", dan halaman detail "Rent 4x Aputure Amaran P60C". Yang diambil hanya pola alur dan susunan layar. Logo, foto, teks, dan nama merek Hygglo tidak dipakai. Tema Hygglo gelap, sedangkan Rentfy memakai tema terang, bahasa Indonesia, dan rupiah.
Referensi
Pola yang dipakai di Rentfy
Pop-up "Where do you want to rent?"
Bottom sheet "Mau sewa di mana?" berisi kolom cari lokasi, tombol lokasi saya, dan peta
Hasil pencarian
Judul hasil, chip subkategori, baris lokasi dan periode sewa dengan tautan ubah, grid kartu barang
Detail barang
Galeri, pemilik dan lencana, isi paket, kebijakan pembatalan, kalender, harga per periode, lokasi perkiraan, ulasan, tombol aksi
Selain tiga tangkapan layar, kerangka alur di bagian 3 memakai tahapan peminjaman penyewa di Hygglo: pencarian, pengajuan sewa dan chat, verifikasi identitas dan pembayaran di dalam platform, pengambilan, lalu penggunaan dan pengembalian. Ringkasan tahapan itu berasal dari bahan tertulis yang dikirim tim, bukan dari tangkapan layar.
3. Alur utama
Alur mengikuti lima tahap peminjaman penyewa ala Hygglo. Semuanya demo tanpa logika sungguhan.
Tahap
Yang terjadi di Rentfy
Layar
1. Pencarian barang
Cari barang dan pilih pemilik yang paling dekat
L3 sampai L6
2. Pengajuan sewa dan komunikasi
Pilih tanggal, kirim permintaan, chat dengan pemilik
L6 sampai L8, L10
3. Verifikasi identitas dan pembayaran
Verifikasi setelah permintaan diterima, bayar di dalam Rentfy
L9, L11 sampai L13
4. Pengambilan barang
Ambil sesuai waktu dan lokasi yang disepakati, penyewa mengonfirmasi barang sudah diterima
L11, L14
5. Penggunaan dan pengembalian
Pakai barang, kembalikan tepat waktu di hari terakhir sewa
L15 sampai L17
Satu alur linear yang harus bisa diklik tanpa jalan buntu:
1.  L1 Login → ketuk Masuk (atau Daftar lewat L2) → langsung ke L3 Beranda
2.  Tahap 1, pencarian: L3 Beranda → ketuk tombol cari → L4 Pilih lokasi → L5 Hasil pencarian (terdekat dulu) → ketuk kartu → L6 Detail barang
3.  Tahap 2, pengajuan dan chat: L6 pilih tanggal → Ajukan sewa → L7 Ringkasan sewa → Kirim permintaan → L8 Permintaan terkirim → Kirim pesan → L10 Chat dengan pemilik
4.  Tahap 3, verifikasi dan pembayaran: L9 Pesanan saya (status berubah otomatis menjadi Permintaan diterima beberapa detik setelah L8) → L11 Detail pesanan → L12 Verifikasi identitas → L13 Pembayaran → status Dana ditahan
5.  Tahap 4, pengambilan: L11 (status Siap diambil) → L14 Pengambilan barang → status Sedang disewa
6.  Tahap 5, penggunaan dan pengembalian: L15 Sedang disewa → L16 Pengembalian → L17 Selesai
Layar tambahan di luar alur utama: L18 Profil, L19 Cara kerja Rentfy, dan L20 Filter (bottom sheet). Ketiganya dibuka dari L3, L5, atau tab Profil, dan selalu kembali ke layar asal.
4. Spesifikasi layar
Komponen kolom cari lengkap (dipakai di L3 dan L5)
Meniru kolom cari Hygglo: satu kontainer yang berisi pencarian, lokasi, tanggal, dan tombol cari.
Segmen
Isi
Saat diketuk
Kolom ketik
Ikon kaca pembesar dan placeholder "Mau sewa apa?"
Membuka keyboard
Chip lokasi
Ikon target dan nama area (bawaan "Jakarta Selatan")
Membuka L4
Chip tanggal
Ikon kalender dan tanggal ambil (bawaan "17 Nov")
Membuka kalender (bottom sheet)
Tombol cari
Bulat 40 px, warna teal, ikon kaca pembesar
Mencari: pencarian pertama membuka L4, lalu L5
• Tata letak ponsel (responsif, 390 px): satu kartu putih berborder 1 px, radius 12, dua baris. Baris 1 berisi kolom ketik selebar penuh. Baris 2 berisi chip lokasi, chip tanggal, dan tombol cari di ujung kanan, dipisah garis tipis.
• Tata letak desktop (utama): satu baris persis seperti referensi: kolom ketik, pemisah, chip lokasi, pemisah, chip tanggal, tombol cari.
• State: default, fokus (border primary 2 px), terisi.
• Aturan: tombol cari berwarna teal, bukan amber, agar tetap satu tombol amber per layar. Lokasi dan tanggal selalu terisi bawaan sehingga kolom tidak pernah kosong.
• Perilaku demo: kata kunci yang diketik dicocokkan dengan nama dan kategori di katalog contoh, dan kolom kosong memakai kata kunci bawaan "camera". Mengganti lokasi atau tanggal hanya mengubah teks di chip dan baris info L5, tanpa menyaring hasil.
Footer (dipakai di L3, L5, L6, L9, dan L18)
Meniru footer Hygglo. Tidak tampil di layar bertahap (L7, L12 sampai L17).
• Logo Rentfy dan slogan singkat (placeholder: "Sewa dan sewakan barang dengan sederhana dan aman").
• Kolom tautan: Tentang Rentfy, Bantuan, Syarat layanan, dan Kebijakan privasi (semuanya toast), serta Cara kerja (membuka L19 dan kembali ke layar asal).
• Kolom Kategori: tujuh kategori beranda, masing-masing membuka L5 untuk kategori itu.
• Baris bawah: "© 2026 Rentfy. Data dalam demo ini adalah contoh."
• Di lebar ponsel footer menjadi satu kolom.
L1. Login (layar pertama)
• Latar primary penuh, logo putih, slogan (sementara: placeholder), ilustrasi garis sederhana.
• Kolom email dan kata sandi, tombol utama Masuk (amber), dan tautan teks Belum punya akun? Daftar.
• Perilaku: kolom boleh kosong atau diisi apa saja. Masuk langsung membuka L3. Tidak ada login lewat Google karena itu membawa pengguna keluar dari website. Daftar membuka L2.
L2. Daftar
• Kolom: nama, email, nomor HP, kota atau area (dropdown contoh), kata sandi dengan tombol tampilkan.
• Tombol utama Daftar, tautan Sudah punya akun? Masuk (kembali ke L1).
• Perilaku: Daftar langsung membuka L3 tanpa verifikasi.
L3. Beranda (gaya e-commerce)
• Navbar atas: logo Rentfy, kolom cari lengkap, Cara kerja, Pesanan, ikon pesan, ikon notifikasi (toast), dan avatar Rina yang membuka menu Profil. Sapaan "Halo, Rina" tampil di atas bagian konten.
• Kolom cari lengkap di bagian atas (lihat komponen di awal bagian ini): kolom ketik, chip lokasi, chip tanggal, dan tombol cari.
• Dua banner kecil: info (Semua pemilik di Rentfy sudah terverifikasi) dan Cara kerja Rentfy dengan tautan Lihat caranya (membuka L19).
• Baris kategori yang bisa digeser: Kamera dan video, Elektronik, Perkakas, Camping dan outdoor, Olahraga, Pesta dan acara, Rumah tangga.
• Bagian Dekat kamu dan Paling sering disewa, berisi kartu barang dalam grid 2 kolom.
• Di lebar ponsel navbar berubah menjadi app bar dengan tab bar bawah: Beranda, Cari, Pesanan, Profil.
• Perilaku: tombol cari (atau tab Cari) membuka L4 pada pencarian pertama, lalu L5. Chip lokasi membuka L4, chip tanggal membuka kalender. Ketuk kartu membuka L6. Tab Pesanan membuka L9. Ketuk kategori mana pun membuka L5 berisi barang di kategori itu. Tab Profil membuka L18, dan ikon lain menampilkan toast "Fitur ini belum tersedia di versi demo".
L4. Pilih lokasi (bottom sheet)
• Judul Mau sewa di mana?, tombol tutup, kolom "Pilih lokasi" dengan ikon cari.
• Peta sungguhan (Leaflet, tile OpenStreetMap) dengan pin di tengah, tombol lokasi saya di pojok peta, hint "Geser peta untuk mencari alamat".
• Tombol utama Pakai lokasi ini.
• Alur pencarian: setelah pop-up ini, pencarian dijalankan dengan kata kunci yang diketik. Jika kolom kosong, kata kunci bawaannya adalah camera. Pengguna lalu diarahkan ke L5. Pop-up muncul otomatis sekali per sesi pada pencarian pertama, dan bisa dibuka kapan saja lewat chip lokasi di kolom cari. Pencarian berikutnya langsung ke L5.
• Perilaku: peta bisa digeser dan di-zoom, dan ketuk di peta memindahkan pin. Nama area diambil dari daftar area contoh yang terdekat dengan pin (tanpa layanan geocoding dari luar). Tombol lokasi saya memindahkan pin ke pusat area bawaan, tanpa meminta izin lokasi. Ketuk lokasi di daftar saran memindahkan pin dan mengisi teks.
L5. Hasil pencarian
• Judul Hasil untuk "[kata kunci]" dan kolom cari lengkap (sama seperti L3, berisi kata kunci terakhir, lokasi, dan tanggal) yang tetap terlihat di atas.
• Chip subkategori yang bisa digeser, mengikuti kategori hasil (contoh untuk kamera): Kamera mirrorless, Kamera saku, Kamera aksi, Kamera polaroid, Tas kamera, Baterai kamera, Gimbal, Aksesori.
• Dua baris info: Dekat Jakarta Selatan (ubah) dan Periode sewa 17 Nov (ubah). Keduanya membuka L4 dan kalender.
• Pengalih Daftar | Peta. Tampilan Peta memakai peta sungguhan dengan satu pin per barang hasil (harga per hari di pin). Ketuk pin membuka kartu kecil, dan ketuk kartu itu membuka L6.
• Chip urutan yang benar-benar mengurutkan kartu (urutan berlaku ulang setiap kali pencarian atau kategori berganti, dan chip aktif ikut tersorot; Terapkan di L20 memakai chip yang sama): Terdekat (aktif bawaan, jarak terkecil dulu), Termurah (harga per hari terendah dulu), Rating (tertinggi dulu). Grid kartu barang 2 kolom (6 sampai 8 kartu), pemilik terdekat di atas. Isi kartu: foto 4:3, nama, harga per hari, jarak, rating, badge Terverifikasi, dan ikon simpan berbentuk hati yang berganti terisi atau kosong saat diketuk (toast "Disimpan" atau "Dihapus dari simpanan").
• Perilaku: semua kartu membuka L6. Ikon filter di app bar membuka bottom sheet L20. Jika tidak ada barang yang cocok, tampil kondisi kosong "Belum ada barang untuk pencarian ini" dengan tombol Lihat semua barang. Chip subkategori hanya berganti tampilan aktif tanpa menyaring ulang, sedangkan chip urutan mengurutkan ulang kartu.
L6. Detail barang (meniru susunan Hygglo)
Urutan konten:
1.  Galeri foto 4:3 dengan indikator
2.  Nama (H1), area dan jarak, harga per hari
3.  Kartu pemilik: avatar, nama, badge Terverifikasi, rating, "Biasanya membalas dalam beberapa menit"
4.  Banner perlindungan: "Barang dilindungi. Biaya perlindungan sudah termasuk di rincian."
5.  Deskripsi dan Isi paket (daftar bullet), catatan kondisi
6.  Kartu deposit: "Deposit dikembalikan setelah barang dicek pemilik."
7.  Kebijakan pembatalan: gratis sampai 2 hari sebelum sewa. Setelahnya dana kembali 50% sampai sehari sebelumnya.
8.  Kalender ketersediaan dengan catatan "Minimal sewa 2 hari", pilihan Ambil dan Kembalikan, tombol Hapus tanggal, dan catatan "Masa sewa dihitung per hari kalender, bukan per 24 jam"
9.  Harga untuk semua periode (1 hari, 2 hari, 1 minggu)
10.  Lokasi perkiraan (peta sungguhan dengan lingkaran area, bukan pin tepat, "Lokasi tepat diberikan setelah pesanan diterima")
11.  Ulasan terbaru (3 ulasan contoh)
12.  Barang serupa: 4 kartu dari kategori yang sama (kartu seperti di L5), dan ketuk salah satunya membuka L6 untuk barang itu
• Bar bawah: harga dan tombol utama Ajukan sewa. Tombol sekunder Kirim pesan dan tautan teks Laporkan listing memunculkan toast, kecuali Kirim pesan yang membuka L10 (chat dengan pemilik).
• Perilaku: tanggal sudah terisi bawaan (17 sampai 18 Nov (2 hari kalender)). Pengguna boleh mengganti tanggal, dan rincian harga ikut terhitung ulang: sewa sama dengan harga per hari dikali jumlah hari kalender (minimal 2 hari), ditambah biaya perlindungan dan deposit. Tombol Ajukan sewa membuka L7. Ikon simpan di app bar berfungsi seperti di L5.
L7. Ringkasan sewa
• Ringkasan barang (thumbnail, nama, tanggal), pesan opsional untuk pemilik.
• Rincian biaya (selalu terlihat): Sewa (jumlah hari mengikuti tanggal yang dipilih), Biaya perlindungan, Deposit (dikembalikan), Perkiraan total.
• Kotak centang syarat layanan.
• Tombol utama Kirim permintaan.
• Perilaku: kotak centang tidak wajib dicentang. Tombol langsung membuka L8. Belum ada pembayaran di tahap ini: pembayaran baru diminta setelah pemilik menerima (L13).
L8. Permintaan terkirim
• Layar sukses hijau dengan ikon centang, teks "Permintaan terkirim. Pemilik akan merespons maksimal 24 jam."
• Tombol utama Lihat pesanan saya, tombol sekunder Kirim pesan ke pemilik (membuka L10), dan tombol teks Kembali ke beranda.
L9. Pesanan saya
• Dua tab: Berjalan dan Selesai.
• Tab Berjalan berisi satu kartu pesanan yang dibuat dari alur sebelumnya: barang, tanggal, dan total mengikuti pilihan di L6 dan L7, bukan kartu contoh yang sama, dengan badge status dan tombol aksi sesuai status (tabel status ada di L11). Tab Selesai berisi kondisi kosong "Belum ada pesanan selesai" dengan tombol Cari barang, lalu terisi setelah L17.
• Status kartu berubah mengikuti langkah penyewa. Langkah yang biasanya dilakukan pemilik (menerima permintaan dan mengecek pengembalian) berjalan otomatis tanpa tombol, dan perubahannya tampil lewat toast di dalam website serta badge yang ikut berganti.
• Ketuk kartu membuka L11.
L10. Chat dengan pemilik (tahap 2)
• App bar: tombol kembali, avatar dan nama pemilik (Dimas) dengan badge Terverifikasi. Di bawahnya kartu barang kecil (thumbnail, nama, tanggal sewa).
• Daftar pesan contoh, kolom ketik, tombol kirim, dan chip balasan cepat (Apakah masih tersedia?, Boleh ambil jam berapa?, Bisa tambah satu hari?).
• Banner info: "Semua transaksi dan pembayaran dilakukan di Rentfy agar dana dan barang tetap terlindungi."
• Perilaku: pesan yang diketik muncul di daftar tanpa dikirim ke mana pun. Pemilik membalas satu kali dengan teks contoh. Tombol kembali menuju layar asal (L6 atau L8).
L11. Detail pesanan
• Kartu barang, tanggal ambil dan kembali, badge status, garis waktu vertikal lima langkah (Permintaan terkirim, Permintaan diterima, Pembayaran, Pengambilan, Pengembalian), kartu rincian biaya, kartu lokasi dan kontak pemilik (terbuka setelah dana ditahan), tombol teks Laporkan masalah.
• Tombol utama dan badge berubah sesuai status:
Status
Badge
Tombol utama
Tujuan
Menunggu pemilik
Kuning
Kirim pesan ke pemilik
L10
Permintaan diterima
Kuning
Verifikasi dan bayar
L12
Dana ditahan, siap diambil
Teal muda
Lihat cara pengambilan
L14
Sedang disewa
Teal muda
Lihat masa sewa
L15
Menunggu pengecekan
Teal muda
Lihat status
L17
Selesai
Hijau
Beri ulasan
L17
• Perilaku: tidak ada pita Demo dan tidak ada tombol Lanjut. Status maju otomatis atau lewat aksi penyewa sendiri (bagian 5). Status selalu memakai ikon dan label.
L12. Verifikasi identitas (tahap 3)
• Muncul hanya setelah permintaan diterima, tepat sebelum pembayaran. Banner: "Permintaan diterima. Verifikasi dulu supaya pembayaran bisa dilanjutkan."
• Stepper 3 langkah: Foto KTP, Selfie dengan KTP, Tinjau. Tiap langkah punya bingkai kamera statis dengan sudut penanda, tip "Pastikan semua tulisan terbaca", dan tautan Pilih dari galeri.
• Kartu info dengan ikon gembok: "Data dipakai hanya untuk verifikasi dan disimpan dengan aman."
• Tombol utama berganti per langkah: Ambil foto (langkah 1 dan 2), Kirim untuk ditinjau (langkah 3).
• Perilaku: Ambil foto menampilkan foto contoh. Kirim untuk ditinjau membuka layar sukses hijau "Terverifikasi" selama 2 detik, lalu otomatis ke L13. Tidak ada pemeriksaan foto sungguhan.
L13. Pembayaran
• Ringkasan barang dan tanggal, lalu rincian biaya yang selalu terlihat, diambil dari pesanan yang dibuat di L6 dan L7 (bukan angka tetap): Sewa [jumlah hari], Biaya perlindungan Rp10.000, Deposit (dikembalikan), Total bayar. Contoh kamera mirrorless 2 hari: Sewa Rp300.000, Biaya perlindungan Rp10.000, Deposit Rp300.000, Total Rp610.000.
• Pilihan metode bayar: QRIS, Transfer bank, Dompet digital (satu terpilih bawaan).
• Catatan: "Bayar di dalam Rentfy supaya perlindungan tetap berlaku. Dana ditahan dengan aman sampai barang kembali."
• Tombol utama Bayar sekarang.
• Perilaku: tidak ada transaksi sungguhan. Untuk QRIS, kode contoh tampil 3 detik lalu pembayaran berhasil. Layar sukses hijau "Pembayaran berhasil" membuka alamat dan jam pengambilan contoh, dengan tombol utama Lihat pesanan saya menuju L11 berstatus Dana ditahan, siap diambil.
L14. Pengambilan barang (tahap 4)
• Kartu lokasi tepat (peta sungguhan dengan pin di titik ambil, alamat contoh), jam ambil, nama pemilik, tombol sekunder Kirim pesan (membuka L10).
• Banner info: "Masa sewa dihitung per hari kalender, bukan per 24 jam."
• Banner peringatan: "Periksa kondisi barang bersama pemilik sebelum meninggalkan lokasi."
• Tombol sekunder Ambil foto kondisi membuka bottom sheet dengan 4 slot foto (Depan, Belakang, Samping, Aksesori) dan catatan cap waktu otomatis. Foto bersifat opsional di demo.
• Tombol utama (amber) Barang sudah saya terima mengubah status menjadi Sedang disewa lalu membuka L15. Ini aksi penyewa, bukan aksi pemilik.
L15. Sedang disewa (tahap 5)
• Kartu hitung mundur: "Kembalikan paling lambat [tanggal kembali dari pesanan]" dan sisa hari sewa.
• Banner peringatan: "Kembalikan tepat waktu di hari terakhir sewa untuk menghindari denda keterlambatan."
• Tips merawat barang (2 sampai 3 baris), tombol sekunder Kirim pesan (membuka L10), tombol teks Laporkan masalah (toast).
• Tombol utama Kembalikan barang menuju L16.
L16. Pengembalian
• Judul Cek kondisi barang, daftar periksa sesuai kategori (kamera: bodi, lensa, baterai dan charger, kartu memori, tas), grid 4 slot foto, kolom catatan, info "Foto dicap waktu otomatis".
• Tombol utama Kirim laporan pengembalian menuju L17. Foto dan daftar periksa tidak divalidasi.
L17. Pengembalian selesai dan ulasan
• Keadaan 1: badge Menunggu pengecekan pemilik dengan hitung mundur maksimal 24 jam. Status berpindah otomatis ke Keadaan 2 sekitar 5 detik kemudian, tanpa tombol.
• Keadaan 2: layar sukses hijau "Selesai. Deposit sudah dikembalikan." dengan rincian deposit sesuai barang yang disewa, lalu ulasan opsional (bintang 1 sampai 5, chip Tepat waktu, Barang sesuai, Komunikatif, komentar opsional).
• Tombol utama Kirim ulasan dan tombol teks Lewati. Keduanya membuka L9 dengan kartu pesanan sudah pindah ke tab Selesai.
L18. Profil (tab Profil, tambahan demo)
• App bar: judul "Profil". Tab bar bawah dengan Profil aktif.
• Kartu akun: avatar bulat 64 px berinisial R, nama Rina, email contoh, tautan teks Ubah profil (toast).
• Daftar menu dengan ikon outline dan panah: Pesanan saya (membuka L9), Barang tersimpan (toast), Cara kerja Rentfy (membuka L19), Bantuan (toast), Syarat layanan dan kebijakan privasi (toast).
• Tombol bahaya Keluar (garis dan teks merah) di bagian bawah. Layar ini tidak punya tombol amber.
• Perilaku: Keluar langsung membuka L1 tanpa konfirmasi.
L19. Cara kerja Rentfy (tambahan demo)
• App bar: tombol tutup, judul "Cara kerja Rentfy".
• Tiga langkah vertikal, masing-masing dengan ikon outline, judul, dan satu kalimat:
    1.  Cari dan pilih: temukan barang dari pemilik terdekat.
    2.  Ajukan sewa dan bayar: pilih tanggal, kirim permintaan, lalu bayar di dalam Rentfy. Dana ditahan dengan aman sampai barang kembali.
    3.  Ambil dan kembalikan: pakai barang, kembalikan tepat waktu. Deposit dikembalikan setelah barang dicek pemilik.
• Kartu info primary-soft: "Semua transaksi dilakukan di Rentfy agar tetap terlindungi."
• Bar bawah: tombol amber Mulai cari barang menuju L3.
• Perilaku: tombol tutup kembali ke layar asal (L3 atau L18).
L20. Filter (bottom sheet di atas L5, tambahan demo)
• Handle, judul Filter, tombol tutup, overlay gelap 40%.
• Bagian Tanggal sewa: dua kolom Ambil (17 Nov) dan Kembalikan (18 Nov), keduanya membuka kalender.
• Bagian Area: chip Jakarta Selatan (terpilih), Jakarta Pusat, Depok, Tangerang Selatan (contoh).
• Bagian Rentang harga per hari: chip Semua (terpilih), Di bawah Rp50.000, Rp50.000 sampai Rp150.000, Di atas Rp150.000.
• Bagian Urutan: chip Terdekat (terpilih), Termurah, Rating tertinggi.
• Tombol amber Terapkan dan tombol teks Atur ulang.
• Perilaku: pilihan berganti status aktif. Terapkan menutup sheet dan hanya menerapkan pilihan urutan; tanggal, area, dan harga tidak menyaring hasil. Atur ulang mengembalikan pilihan bawaan.
5. Aturan prototipe tanpa logika
• Tidak ada validasi. Semua input lolos, termasuk yang kosong.
• Tidak ada penyimpanan data. Muat ulang berarti kembali ke L1.
• Semua data berasal dari satu daftar contoh (bagian 6). Kartu mana pun yang diketuk membuka template L6 dengan data barang tersebut.
• Tombol atau tautan yang belum punya layar menampilkan toast "Fitur ini belum tersedia di versi demo", bukan dibiarkan mati.
• Hindari tombol nonaktif, sesuai Brief UI.
• Hanya satu tombol amber per layar.
• Status selalu memakai ikon dan label, tidak hanya warna.
• Tidak ada aksi pemilik di versi ini dan tidak ada pita Demo. Status berubah otomatis: Menunggu pemilik menjadi Permintaan diterima sekitar 5 detik setelah L8 (toast "Permintaan kamu diterima" di dalam website), dan Menunggu pengecekan menjadi Selesai sekitar 5 detik setelah L16 dikirim. Pengambilan dikonfirmasi penyewa lewat tombol Barang sudah saya terima di L14.
• Semua tombol dan tautan hanya bergerak di dalam website ini. Tidak ada tautan keluar (lihat aturan satu website di bagian 1).
• Verifikasi identitas hanya muncul setelah permintaan diterima, dan semua pembayaran hanya lewat Rentfy.
• Tombol yang berfungsi (membentuk alur): Masuk, Daftar, kolom cari, tombol cari, chip lokasi dan tanggal, kategori, filter, chip urutan (Terdekat, Termurah, Rating), kalender di L6, kartu barang termasuk kartu Barang serupa, kategori dan Cara kerja di footer, ikon simpan, Ajukan sewa, Kirim permintaan, Kirim pesan, Verifikasi dan bayar, Bayar sekarang, tombol utama L12 sampai L17, tab bar, dan Keluar.
• Tombol yang menampilkan toast "Fitur ini belum tersedia di versi demo": ikon notifikasi, bagikan, Laporkan listing, Laporkan masalah, Bantuan, Syarat dan privasi, Tentang Rentfy (footer), Ubah profil, dan Barang tersimpan.
• Data pesanan (barang, tanggal, total) dibawa dari L6 ke L7, L9, L11, L13, L14, L15, L16, dan L17 selama sesi berjalan, dan hilang saat halaman dimuat ulang. Kartu di L9 dibuat dari pesanan ini, dan kartu itu pindah ke tab Selesai setelah L17.
6. Data contoh
Semua angka adalah contoh dan perlu diberi label "contoh" saat dipresentasikan. Gunakan foto stok bebas lisensi (misalnya dari Unsplash atau Pexels), bukan foto dari Hygglo. Foto disimpan sebagai berkas lokal di folder proyek, bukan tautan ke situs lain, dengan 3 sampai 4 foto per barang untuk galeri L6. Setiap barang juga punya koordinat contoh di sekitar Jakarta Selatan untuk peta.
Barang
Harga / hari
Deposit
Jarak
Rating
Kamera mirrorless dan lensa kit
Rp150.000
Rp300.000
1,2 km
4,8
Kamera saku compact
Rp75.000
Rp150.000
0,8 km
4,7
Kamera aksi 4K
Rp60.000
Rp100.000
2,0 km
4,9
Kamera polaroid instan
Rp50.000
Rp100.000
1,5 km
4,6
Lensa 24-70 mm f/2.8
Rp120.000
Rp250.000
1,2 km
4,8
Paket 4 lampu LED panel RGB
Rp280.000
Rp500.000
3,1 km
5,0
Gimbal smartphone
Rp50.000
Rp100.000
2,4 km
4,7
Tripod dan tas kamera
Rp30.000
Rp50.000
0,5 km
4,5
Tenda kapasitas 4 orang
Rp60.000
Rp100.000
2,0 km
4,8
Bor listrik dan set mata bor
Rp40.000
Rp100.000
0,9 km
4,7
Proyektor mini
Rp90.000
Rp200.000
1,8 km
4,6
Katalog dan pencarian: tabel di atas hanya sebagian. Katalog dibuat minimal 3 barang per kategori (7 kategori, sekitar 21 sampai 24 barang) supaya kategori mana pun menampilkan hasil. Pencarian mencocokkan kata kunci dengan nama dan kategori barang. Contohnya "tenda" menampilkan barang camping, "bor" menampilkan perkakas, dan kata yang tidak cocok menampilkan kondisi kosong.
Rincian contoh untuk kamera mirrorless, 2 hari: sewa Rp300.000, biaya perlindungan Rp10.000, deposit Rp300.000 (dikembalikan), total bayar Rp610.000.
Rumus hitung (demo): sewa = harga per hari x jumlah hari kalender, minimal 2 hari. Biaya perlindungan tetap Rp10.000 per pesanan. Deposit mengikuti barang dan tidak dihitung sebagai biaya. Total = sewa + biaya perlindungan + deposit. Harga untuk semua periode di L6 memakai rumus yang sama. Rumus ini dipakai di satu fungsi hitung yang sama untuk L6, L7, L9, L11, dan L13, sehingga angka di semua layar itu selalu konsisten.
Pengguna dan pemilik contoh: penyewa Rina, pemilik Dimas (nama fiktif, bukan nama anggota tim). Area contoh: Jakarta Selatan.
Data tahap peminjaman: tanggal sewa 17 sampai 18 Nov (2 hari kalender), alamat pengambilan fiktif di Jakarta Selatan, jam ambil 10.00, dan dua pesan chat contoh antara Rina dan Dimas.
7. Kriteria selesai
• Dari L1 sampai L17 bisa diklik berurutan tanpa jalan buntu, melewati lima tahap peminjaman.
• Daftar dan Masuk sama-sama membuka beranda.
• Pop-up lokasi muncul saat pencarian pertama, lalu hasil pencarian tampil.
• Semua kartu di L5 membuka L6, dan L6 terlihat setara dengan referensi (galeri, pemilik, isi paket, kalender, harga, lokasi, ulasan).
• Rincian biaya dan badge Terverifikasi tampil di kartu, detail, dan ringkasan sewa.
• Tidak ada tombol yang diam saat diketuk.
• Teks memakai bahasa Indonesia sentence case dan sesuai gaya di Brief UI.
• Verifikasi identitas (L12) hanya muncul setelah status Permintaan diterima, dan pembayaran (L13) hanya ada di dalam Rentfy.
• Catatan "per hari kalender" tampil di L6 dan L14, dan peringatan denda keterlambatan tampil di L15.
• Status yang biasanya bergantung pada pemilik berjalan otomatis, tanpa pita Demo dan tanpa tombol pemilik, sehingga alur tidak berhenti di tengah.
• Peta di L4, L5 (tampilan Peta), L6, dan L14 adalah peta sungguhan yang bisa digeser dan di-zoom.
• Semua gambar barang memakai foto stok lokal, dan tidak ada tombol atau tautan yang membuka halaman atau aplikasi di luar website ini.
• Tab Profil, banner Cara kerja, ikon filter, dan ikon simpan semuanya berfungsi: menuju layar yang benar atau berganti tampilan.
• Pencarian dengan kata kunci lain (misalnya "tenda") menampilkan hasil yang sesuai, dan kata yang tidak cocok menampilkan kondisi kosong.
• Halaman terbuka sebagai website biasa selebar browser, tanpa bingkai ponsel, dan menyesuaikan diri ke tablet dan ponsel.
• Mengganti tanggal di kalender L6 mengubah rincian harga, dan barang serta tanggal yang dipilih muncul sama di L7, L9, dan L13.
• Chip Terdekat, Termurah, dan Rating di L5 benar-benar mengubah urutan kartu.
8. Hal yang perlu diputuskan
1.  Bentuk hasil: sudah diputuskan, website HTML yang dibuka di browser.
2.  Peta: sudah diputuskan, memakai peta sungguhan.
3.  Foto barang: sudah diputuskan, memakai foto stok.
4.  Logo dan slogan: sementara pakai placeholder sampai keputusan final.
5.  Area default: Jakarta Selatan sebagai contoh, boleh diganti sesuai kota pengguna.
6.  Denda keterlambatan: tampil sebagai teks tanpa nominal, atau pakai nominal contoh.
7.  Aksi pemilik: sudah diputuskan, tidak ada dulu. Status berjalan otomatis.
8.  Tampilan utama web: desktop-first seperti Hygglo (navbar atas, grid 4 kolom) dengan tampilan ponsel sebagai versi responsif. Ini asumsi saat ini dan bisa dibalik jika tim lebih ingin mobile-first.