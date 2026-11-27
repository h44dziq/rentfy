/**
 * Rentfy - Production Data Store
 * All mock data, categories, catalog items, and calculation helpers
 */

window.RentfyData = {
  user: {
    name: "Arvin Maulana",
    email: "arvin@email.com",
    avatar: "A",
    location: "Jakarta Selatan",
    phone: "0812-3456-7890",
    role: "penyewa" // "penyewa" atau "pemilik"
  },

  owner: {
    name: "Dimas",
    avatar: "D",
    verified: true,
    rating: 4.9,
    reviews: 42,
    responseTime: "Biasanya membalas dalam beberapa menit",
    location: "Kebayoran Baru, Jakarta Selatan",
    address: "Jl. Gandaria I No. 18, Kebayoran Baru, Jakarta Selatan",
    pickupTime: "10:00 - 18:00 WIB",
    phone: "0811-2233-4455",
    joinedDate: "Jan 2026",
    totalListings: 8,
    completionRate: "96%"
  },

  // Data for owner mode (listing management, bookings)
  ownerListings: [
    {
      id: 1,
      title: "Kamera mirrorless Sony Alpha A7 III",
      category: "kamera",
      status: "aktif",
      pricePerDay: 150000,
      deposit: 300000,
      bookedDates: ["2026-11-20", "2026-11-21"],
      images: ["https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=800&q=80"],
      createdAt: "2026-10-15"
    },
    {
      id: 2,
      title: "Gimbal Smartphone DJI OM 5",
      category: "elektronik",
      status: "aktif",
      pricePerDay: 50000,
      deposit: 100000,
      bookedDates: [],
      images: ["https://images.unsplash.com/photo-1512790182412-b19e6d62bc39?w=800&q=80"],
      createdAt: "2026-11-01"
    }
  ],

  ownerBookings: [
    {
      id: "BK-001",
      itemId: 1,
      customerName: "Rina",
      startDate: "17 Nov 2026",
      endDate: "18 Nov 2026",
      status: "pending", // pending, approved, completed, cancelled
      totalAmount: 610000,
      commission: 61000, // 10%
      deposit: 300000,
      requestDate: "2026-11-16"
    }
  ],

  categories: [
    { id: "kamera", name: "Kamera dan video", iconType: "camera", count: 8, bg: "#0A3F44" },
    { id: "elektronik", name: "Elektronik", iconType: "laptop", count: 4, bg: "#0A3F44" },
    { id: "perkakas", name: "Perkakas", iconType: "wrench", count: 4, bg: "#0A3F44" },
    { id: "camping", name: "Camping dan outdoor", iconType: "tent", count: 4, bg: "#0A3F44" },
    { id: "olahraga", name: "Olahraga", iconType: "sports", count: 3, bg: "#0A3F44" },
    { id: "pesta", name: "Pesta dan acara", iconType: "party", count: 3, bg: "#0A3F44" },
    { id: "rumahtangga", name: "Rumah tangga", iconType: "home", count: 3, bg: "#0A3F44" }
  ],

  areas: [
    "Jakarta Selatan",
    "Jakarta Pusat",
    "Jakarta Barat",
    "Jakarta Timur",
    "Jakarta Utara",
    "Depok",
    "Tangerang Selatan",
    "Bekasi"
  ],

  defaultDates: {
    start: "17 Nov",
    end: "18 Nov",
    days: 2
  },

  items: [
    // --- Kamera dan video (8 items) ---
    {
      id: 1,
      name: "Kamera mirrorless Sony Alpha A7 III dan lensa kit 28-70mm",
      category: "kamera",
      subcategory: "Kamera mirrorless",
      pricePerDay: 150000,
      deposit: 300000,
      distance: "1,2 km",
      distanceKm: 1.2,
      rating: 4.8,
      reviewsCount: 38,
      locationName: "Kebayoran Baru, Jakarta Selatan",
      lat: -6.2442,
      lng: 106.7978,
      images: [
        "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=800&q=80",
        "https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=800&q=80",
        "https://images.unsplash.com/photo-1512790182412-b19e6d62bc39?w=800&q=80"
      ],
      description: "Sony Alpha A7 III Full-Frame Mirrorless Camera dengan sensor 24.2MP dan kemampuan rekam video 4K HDR. Sangat cocok untuk dokumentasi event, wedding, prewedding, atau produksi video kreatif.",
      packageContents: [
        "Body Sony Alpha A7 III",
        "Lensa Sony FE 28-70mm f/3.5-5.6 OSS",
        "2x Baterai Sony NP-FZ100 original",
        "Dual battery charger & kabel power",
        "SD Card SanDisk Extreme Pro 64GB 170MB/s",
        "Tas kamera selempang empuk & strap"
      ],
      condition: "Kondisi fisik 95% mulus, sensor bersih tanpa jamur, shutter count rendah. Semua tombol dan dial berfungsi presisi."
    },
    {
      id: 2,
      name: "Kamera saku compact Canon PowerShot G7X Mark III",
      category: "kamera",
      subcategory: "Kamera saku",
      pricePerDay: 75000,
      deposit: 150000,
      distance: "0,8 km",
      distanceKm: 0.8,
      rating: 4.7,
      reviewsCount: 24,
      locationName: "Gandaria, Jakarta Selatan",
      lat: -6.2481,
      lng: 106.7865,
      images: [
        "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=800&q=80",
        "https://images.unsplash.com/photo-1510127034890-ba27508e9f1c?w=800&q=80"
      ],
      description: "Kamera vlogging compact legendaris dengan layar flip-up 180 derajat, live streaming YouTube ready, dan kualitas video 4K tanpa crop.",
      packageContents: [
        "Kamera Canon G7X Mark III",
        "2x Baterai NB-13L",
        "Desktop Charger",
        "Memory Card 32GB High Speed",
        "Mini pouch pelindung"
      ],
      condition: "Mulus dan siap pakai untuk liburan santai maupun vlog harian."
    },
    {
      id: 3,
      name: "Kamera aksi GoPro HERO 11 Black 4K/5.3K Waterproof",
      category: "kamera",
      subcategory: "Kamera aksi",
      pricePerDay: 60000,
      deposit: 100000,
      distance: "2,0 km",
      distanceKm: 2.0,
      rating: 4.9,
      reviewsCount: 52,
      locationName: "Pondok Indah, Jakarta Selatan",
      lat: -6.2715,
      lng: 106.7853,
      images: [
        "https://images.unsplash.com/photo-1565849904461-04a58ad377e0?w=800&q=80",
        "https://images.unsplash.com/photo-1508873696983-2df5703bc222?w=800&q=80"
      ],
      description: "GoPro Hero 11 dengan stabilisasi HyperSmooth 5.0 terbaik, horizon lock 360 derajat, dan anti-air hingga 10 meter tanpa case tambahan.",
      packageContents: [
        "Unit GoPro Hero 11 Black",
        "2x Enduro Battery tahan dingin",
        "Floating hand grip & sticky mount",
        "MicroSD SanDisk Extreme 64GB",
        "Kabel USB-C & hard case"
      ],
      condition: "Lensa dan layar depan/belakang terlindung tempered glass sejak hari pertama."
    },
    {
      id: 4,
      name: "Kamera polaroid instan Fujifilm Instax Mini 11",
      category: "kamera",
      subcategory: "Kamera polaroid",
      pricePerDay: 50000,
      deposit: 100000,
      distance: "1,5 km",
      distanceKm: 1.5,
      rating: 4.6,
      reviewsCount: 19,
      locationName: "Blok M, Jakarta Selatan",
      lat: -6.2448,
      lng: 106.7995,
      images: [
        "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=800&q=80",
        "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?w=800&q=80"
      ],
      description: "Kamera cetak instan warna pastel yang lucu dan mudah digunakan. Cocok untuk photobooth mini, perayaan ulang tahun, atau kumpul teman.",
      packageContents: [
        "Kamera Instax Mini 11 Blush Pink",
        "Tali strap pergelangan tangan",
        "4x Baterai AA Alkaline cadangan",
        "Tas casing kulit vintage"
      ],
      condition: "Flash otomatis dan exposure sensor normal lancar. Kertas film dibeli terpisah."
    },
    {
      id: 5,
      name: "Lensa Sony FE 24-70mm f/2.8 GM G-Master Lens",
      category: "kamera",
      subcategory: "Aksesori",
      pricePerDay: 120000,
      deposit: 250000,
      distance: "1,2 km",
      distanceKm: 1.2,
      rating: 4.8,
      reviewsCount: 31,
      locationName: "Kebayoran Baru, Jakarta Selatan",
      lat: -6.2415,
      lng: 106.8021,
      images: [
        "https://images.unsplash.com/photo-1617005082133-548c4dd27f35?w=800&q=80",
        "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=800&q=80"
      ],
      description: "Lensa zoom standar profesional legendaris dengan ketajaman luar biasa dan bokeh creamy di seluruh rentang focal length.",
      packageContents: [
        "Lensa FE 24-70mm F2.8 GM",
        "Front & Rear lens cap",
        "Lens hood original",
        "Pouch pelindung tebal"
      ],
      condition: "Optik bening bebas jamur dan fog, autofocus sangat cepat dan senyap."
    },
    {
      id: 6,
      name: "Paket 4 lampu LED panel RGB Godox TL60 & Stand",
      category: "kamera",
      subcategory: "Pencahayaan",
      pricePerDay: 280000,
      deposit: 500000,
      distance: "3,1 km",
      distanceKm: 3.1,
      rating: 5.0,
      reviewsCount: 14,
      locationName: "Cilandak, Jakarta Selatan",
      lat: -6.2912,
      lng: 106.8015,
      images: [
        "https://images.unsplash.com/photo-1574717024653-61fd2cf4d44d?w=800&q=80"
      ],
      description: "Set 4 tube light RGB multifungsi dengan kendali via aplikasi smartphone. Sangat cocok untuk produksi musik video, podcast, dan foto katalog.",
      packageContents: [
        "4x Godox Tube Light",
        "4x Light stand kokoh 2 meter",
        "Power adapter & kabel daisy chain",
        "Tas jinjing studio beroda"
      ],
      condition: "Semua warna RGB dan mode effect berjalan 100% prima."
    },
    {
      id: 7,
      name: "Gimbal stabilizer smartphone DJI OM 6 (Osmo Mobile 6)",
      category: "kamera",
      subcategory: "Gimbal",
      pricePerDay: 50000,
      deposit: 100000,
      distance: "2,4 km",
      distanceKm: 2.4,
      rating: 4.7,
      reviewsCount: 40,
      locationName: "Kemang, Jakarta Selatan",
      lat: -6.2625,
      lng: 106.8142,
      images: [
        "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=800&q=80"
      ],
      description: "Gimbal 3-axis cerdas dengan extension rod terintegrasi, fitur ActiveTrack 6.0 untuk penguncian subjek otomatis.",
      packageContents: [
        "DJI Osmo Mobile 6",
        "DJI OM Magnetic Phone Clamp 3",
        "Grip tripod lipat",
        "Pouch penyimpanan & kabel type-C"
      ],
      condition: "Baterai awet 6 jam penggunaan, motor gimbal halus dan tidak ada getaran."
    },
    {
      id: 8,
      name: "Tripod profesional Manfrotto BeFree Live & tas kamera",
      category: "kamera",
      subcategory: "Aksesori",
      pricePerDay: 30000,
      deposit: 50000,
      distance: "0,5 km",
      distanceKm: 0.5,
      rating: 4.5,
      reviewsCount: 28,
      locationName: "Senopati, Jakarta Selatan",
      lat: -6.2361,
      lng: 106.8087,
      images: [
        "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=800&q=80"
      ],
      description: "Tripod video fleksibel berbahan aluminium dengan fluid head lembut untuk gerakan pan & tilt yang sinematik.",
      packageContents: [
        "Tripod Manfrotto BeFree Live",
        "Quick release plate",
        "Tas tripod original berbantalan"
      ],
      condition: "Kaki-kaki kokoh, kunci lock mengunci kuat tanpa selip."
    },

    // --- Elektronik (4 items) ---
    {
      id: 9,
      name: "Proyektor mini portable Anker Nebula Capsule II",
      category: "elektronik",
      subcategory: "Proyektor",
      pricePerDay: 90000,
      deposit: 200000,
      distance: "1,8 km",
      distanceKm: 1.8,
      rating: 4.6,
      reviewsCount: 22,
      locationName: "Bangka, Jakarta Selatan",
      lat: -6.2552,
      lng: 106.8189,
      images: [
        "https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?w=800&q=80"
      ],
      description: "Smart pocket projector berbasis Android TV dengan speaker 360 derajat. Ukuran sebesar kaleng minuman, praktis untuk nobar di mana saja.",
      packageContents: [
        "Proyektor Nebula Capsule II",
        "Remote kontrol",
        "Power delivery charger 30W & kabel",
        "Tripod mini meja"
      ],
      condition: "Lampu proyeksi terang, fokus otomatis responsif, speaker jernih."
    },
    {
      id: 10,
      name: "iPad Air 5th Gen 256GB M1 Chip + Apple Pencil 2",
      category: "elektronik",
      subcategory: "Tablet",
      pricePerDay: 130000,
      deposit: 300000,
      distance: "1,4 km",
      distanceKm: 1.4,
      rating: 4.9,
      reviewsCount: 35,
      locationName: "Kebayoran Baru, Jakarta Selatan",
      lat: -6.2472,
      lng: 106.8041,
      images: [
        "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=800&q=80"
      ],
      description: "Tablet performa tinggi dengan chip Apple M1. Sangat ideal untuk ilustrator digital, presentasi bisnis, dan editing foto ringan.",
      packageContents: [
        "iPad Air 5 256GB Wi-Fi Space Gray",
        "Apple Pencil Generasi ke-2",
        "Smart Folio Case magnetik",
        "Fast charger 20W USB-C"
      ],
      condition: "Layar bersih tanpa scratch, baterai health 98%."
    },
    {
      id: 11,
      name: "Speaker Bluetooth Marshall Kilburn II Portable",
      category: "elektronik",
      subcategory: "Audio",
      pricePerDay: 85000,
      deposit: 200000,
      distance: "2,2 km",
      distanceKm: 2.2,
      rating: 4.8,
      reviewsCount: 18,
      locationName: "Tebet, Jakarta Selatan",
      lat: -6.2301,
      lng: 106.8521,
      images: [
        "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=800&q=80"
      ],
      description: "Speaker ikonik bergaya amplifier klasik dengan suara multi-arah yang bertenaga dan bass mendalam. Daya tahan baterai hingga 20+ jam.",
      packageContents: [
        "Marshall Kilburn II Speaker",
        "Kabel power charger AC",
        "Kabel audio aux 3.5mm coiled"
      ],
      condition: "Knob analog berfungsi lancar, fisik vintage terawat sangat baik."
    },
    {
      id: 12,
      name: "Drone DJI Mini 3 Pro dengan Controller RC Layar",
      category: "elektronik",
      subcategory: "Drone",
      pricePerDay: 220000,
      deposit: 450000,
      distance: "3,0 km",
      distanceKm: 3.0,
      rating: 4.9,
      reviewsCount: 29,
      locationName: "Pancoran, Jakarta Selatan",
      lat: -6.2510,
      lng: 106.8423,
      images: [
        "https://images.unsplash.com/photo-1527977966376-1c8408f9f108?w=800&q=80"
      ],
      description: "Drone ringan di bawah 249 gram dengan sensor rintangan 3 arah, video 4K HDR, dan fitur True Vertical Shooting untuk konten reels/TikTok.",
      packageContents: [
        "DJI Mini 3 Pro Drone",
        "DJI RC Smart Controller dengan layar",
        "3x Baterai Intelligent Flight",
        "Two-way charging hub",
        "Shoulder bag & baling-baling cadangan"
      ],
      condition: "Siap terbang, kalibrasi gimbal normal, sudah terpasang pelindung sensor."
    },

    // --- Perkakas (4 items) ---
    {
      id: 13,
      name: "Bor listrik cordless Bosch GSB 185-LI & set mata bor komplit",
      category: "perkakas",
      subcategory: "Bor",
      pricePerDay: 40000,
      deposit: 100000,
      distance: "0,9 km",
      distanceKm: 0.9,
      rating: 4.7,
      reviewsCount: 33,
      locationName: "Mampang, Jakarta Selatan",
      lat: -6.2519,
      lng: 106.8281,
      images: [
        "https://images.unsplash.com/photo-1504148455328-c376907d081c?w=800&q=80"
      ],
      description: "Mesin bor impact cordless 18V multifungsi untuk kayu, besi, dan tembok bata. Tanpa kabel sehingga sangat leluasa digunakan.",
      packageContents: [
        "Cordless Impact Drill Bosch 18V",
        "2x Baterai Li-Ion 2.0Ah",
        "Charger docking cepat",
        "Set 33 pcs mata bor & obeng komplit",
        "Hard carrying box"
      ],
      condition: "Torsi kuat, chuck putaran presisi, lampu LED kerja menyala terang."
    },
    {
      id: 14,
      name: "High Pressure Washer Karcher K2 untuk cuci mobil & AC",
      category: "perkakas",
      subcategory: "Pembersih",
      pricePerDay: 65000,
      deposit: 120000,
      distance: "1,6 km",
      distanceKm: 1.6,
      rating: 4.8,
      reviewsCount: 26,
      locationName: "Cilandak, Jakarta Selatan",
      lat: -6.2891,
      lng: 106.8123,
      images: [
        "https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=800&q=80"
      ],
      description: "Mesin steam air bertekanan tinggi 110 bar hemat listrik. Efektif membersihkan kerak lantai garasi, lumut dinding, cuci motor dan mobil.",
      packageContents: [
        "Unit Karcher K2",
        "High pressure gun & selang 5 meter",
        "Vario Power jet lance",
        "Dirt blaster spray lance",
        "Konektor selang taman universal"
      ],
      condition: "Tekanan air kencang stabil, seal pipa rapat tanpa bocor."
    },
    {
      id: 15,
      name: "Tangga lipat aluminium teleskopik 3.8 meter kokoh",
      category: "perkakas",
      subcategory: "Tangga",
      pricePerDay: 35000,
      deposit: 70000,
      distance: "1,1 km",
      distanceKm: 1.1,
      rating: 4.6,
      reviewsCount: 15,
      locationName: "Kebayoran Baru, Jakarta Selatan",
      lat: -6.2411,
      lng: 106.7915,
      images: [
        "https://images.unsplash.com/photo-1513694203232-719a280e022f?w=800&q=80"
      ],
      description: "Tangga teleskopik modern yang dapat dipanjangkan hingga 3.8 meter namun bisa dilipat kompak hingga 85 cm sehingga muat di bagasi mobil.",
      packageContents: [
        "Tangga teleskopik 3.8m kapasitas beban 150kg",
        "Karet anti slip bantalan kaki"
      ],
      condition: "Mekanisme penguncian anak tangga klik dengan mantap dan aman."
    },
    {
      id: 16,
      name: "Mesin amplas kayu orbital sander Makita & amplas",
      category: "perkakas",
      subcategory: "Amplas",
      pricePerDay: 35000,
      deposit: 70000,
      distance: "2,5 km",
      distanceKm: 2.5,
      rating: 4.7,
      reviewsCount: 12,
      locationName: "Pasar Minggu, Jakarta Selatan",
      lat: -6.2851,
      lng: 106.8375,
      images: [
        "https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=800&q=80"
      ],
      description: "Mesin amplas getar untuk finishing furnitur kayu, meja, kusen, atau meratakan dempul dengan hasil permukaan yang halus merata.",
      packageContents: [
        "Makita Finishing Sander",
        "Dust bag penampung debu",
        "Set lembaran amplas grit 80, 120, 240"
      ],
      condition: "Getaran stabil, pad karet amplas rata, kabel utuh."
    },

    // --- Camping dan outdoor (4 items) ---
    {
      id: 17,
      name: "Tenda kapasitas 4 orang Naturehike Cloud Vessel Double Layer",
      category: "camping",
      subcategory: "Tenda",
      pricePerDay: 60000,
      deposit: 100000,
      distance: "2,0 km",
      distanceKm: 2.0,
      rating: 4.8,
      reviewsCount: 44,
      locationName: "Jagakarsa, Jakarta Selatan",
      lat: -6.3211,
      lng: 106.8245,
      images: [
        "https://images.unsplash.com/photo-1504280390367-361c6d9f38f4?w=800&q=80",
        "https://images.unsplash.com/photo-1478131143081-80f7f84ca84d?w=800&q=80"
      ],
      description: "Tenda dome outdoor anti-badai dan tahan hujan lebat (waterproof PU 3000mm). Dilengkapi vestibule teras depan yang luas untuk santai dan memasak.",
      packageContents: [
        "Inner tent & Outer flysheet waterproof",
        "Set frame aluminium alloy ringan",
        "Pasak aluminium & tali guyline reflektif",
        "Footprint alas terpal pelindung",
        "Tas kompresi bawaan"
      ],
      condition: "Bersih harum tanpa aroma apek, ritsleting lancar, jahitan seam seal rapi utuh."
    },
    {
      id: 18,
      name: "Paket masak camping nesting ultralight + kompor mini gas",
      category: "camping",
      subcategory: "Memasak",
      pricePerDay: 30000,
      deposit: 50000,
      distance: "1,5 km",
      distanceKm: 1.5,
      rating: 4.7,
      reviewsCount: 31,
      locationName: "Kemang, Jakarta Selatan",
      lat: -6.2681,
      lng: 106.8162,
      images: [
        "https://images.unsplash.com/photo-1510312305653-8ed496efae75?w=800&q=80"
      ],
      description: "Set peralatan masak praktis untuk 2-3 orang. Terdiri dari panci, wajan kecil anti lengket, dan kompor gas lipat portabel tahan angin.",
      packageContents: [
        "1x Panci aluminium anodized dengan tutup",
        "1x Wajan penggorengan mini",
        "Kompor lipat windproof dengan pemantik piezzo",
        "Sendok sup, mangkok mini, spons pembersih",
        "Mesh pouch"
      ],
      condition: "Bebas kerak gosong, pemantik kompor sekali klik menyala."
    },
    {
      id: 19,
      name: "Carrier Deuter Aircontact Core 50+10 Liter Original",
      category: "camping",
      subcategory: "Tas",
      pricePerDay: 45000,
      deposit: 100000,
      distance: "2,3 km",
      distanceKm: 2.3,
      rating: 4.9,
      reviewsCount: 27,
      locationName: "Cilandak, Jakarta Selatan",
      lat: -6.2952,
      lng: 106.8041,
      images: [
        "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800&q=80"
      ],
      description: "Ransel gunung ergonomis dengan sistem sirkulasi udara punggung terbaik dan sabuk pinggang empuk untuk mendaki tanpa pegal.",
      packageContents: [
        "Carrier Deuter 50+10L",
        "Rain cover original warna biru terang"
      ],
      condition: "Busa punggung empuk, buckle pengunci kuat, bersih luar dalam."
    },
    {
      id: 20,
      name: "Set 2 Kursi lipat outdoor camping & 1 Meja lipat portable",
      category: "camping",
      subcategory: "Furnitur",
      pricePerDay: 40000,
      deposit: 80000,
      distance: "1,7 km",
      distanceKm: 1.7,
      rating: 4.7,
      reviewsCount: 20,
      locationName: "Fatmawati, Jakarta Selatan",
      lat: -6.2821,
      lng: 106.7972,
      images: [
        "https://images.unsplash.com/photo-1517824806704-9040b037703b?w=800&q=80"
      ],
      description: "Set kursi santai dengan sandaran punggung dan meja lipat aluminium roll-top, sangat cocok untuk glamping, piknik taman, atau memancing.",
      packageContents: [
        "2x Kursi lipat rangka baja beban hingga 110kg",
        "1x Meja lipat aluminium",
        "Tas penyimpanan jinjing"
      ],
      condition: "Kain oxford tebal tanpa sobek, rangka stabil di permukaan tanah."
    },

    // --- Olahraga (3 items) ---
    {
      id: 21,
      name: "Sepeda lipat Brompton M6R Racing Green 6 Speed",
      category: "olahraga",
      subcategory: "Sepeda",
      pricePerDay: 175000,
      deposit: 400000,
      distance: "1,3 km",
      distanceKm: 1.3,
      rating: 4.9,
      reviewsCount: 16,
      locationName: "Senopati, Jakarta Selatan",
      lat: -6.2335,
      lng: 106.8062,
      images: [
        "https://images.unsplash.com/photo-1485965120184-e220f721d03e?w=800&q=80"
      ],
      description: "Sepeda lipat premium buatan Inggris. Sangat ringkas, elegan, dan lincah untuk gowes santai di CFD Sudirman-Thamrin.",
      packageContents: [
        "Sepeda Brompton M6R terawat",
        "Helm sepeda kasual size M/L",
        "Lampu depan/belakang rechargeable",
        "Kunci gembok sepeda kombinasi angka"
      ],
      condition: "Gears shifting sangat presisi, rem pakem, ban Schwalbe Marathon mulus."
    },
    {
      id: 22,
      name: "Set 2 Raket Badminton Yonex Astrox 88D Pro & Shuttlecock",
      category: "olahraga",
      subcategory: "Raket",
      pricePerDay: 45000,
      deposit: 80000,
      distance: "0,7 km",
      distanceKm: 0.7,
      rating: 4.7,
      reviewsCount: 22,
      locationName: "Blok A, Jakarta Selatan",
      lat: -6.2521,
      lng: 106.7932,
      images: [
        "https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?w=800&q=80"
      ],
      description: "Raket badminton tipe offensive untuk smash bertenaga. Sudah terpasang senar BG66 Ultimax tarikan 26 lbs siap tanding.",
      packageContents: [
        "2x Raket Yonex Astrox 88D Pro",
        "1x Slop shuttlecock (isi 12)",
        "Tas thermo raket ganda"
      ],
      condition: "Grip baru diganti nyaman tanpa licin, frame bebas retak."
    },
    {
      id: 23,
      name: "Papan Paddle Board Inflatable Stand Up Paddle (SUP) 3.2m",
      category: "olahraga",
      subcategory: "Air",
      pricePerDay: 120000,
      deposit: 250000,
      distance: "3,5 km",
      distanceKm: 3.5,
      rating: 4.8,
      reviewsCount: 11,
      locationName: "Pondok Indah, Jakarta Selatan",
      lat: -6.2751,
      lng: 106.7821,
      images: [
        "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=800&q=80"
      ],
      description: "Papan selancar dayung tiup serbaguna untuk olahraga dan rekreasi di danau atau pantai. Stabil dan mudah dinaiki pemula.",
      packageContents: [
        "Inflatable SUP Board 320cm",
        "Dayung aluminium adjustable",
        "Pompa manual high-pressure dengan manometer",
        "Leash tali pengaman kaki",
        "Drybag 20L & ransel carrier SUP"
      ],
      condition: "Tidak ada kebocoran udara, fin sirip bawah terkunci kokoh."
    },

    // --- Pesta dan acara (3 items) ---
    {
      id: 24,
      name: "Sound System Portable Wireless 200W + 2 Mic Wireless",
      category: "pesta",
      subcategory: "Audio",
      pricePerDay: 150000,
      deposit: 300000,
      distance: "1,9 km",
      distanceKm: 1.9,
      rating: 4.8,
      reviewsCount: 30,
      locationName: "Kebayoran Lama, Jakarta Selatan",
      lat: -6.2492,
      lng: 106.7781,
      images: [
        "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=800&q=80"
      ],
      description: "Speaker troli bertenaga dengan baterai aki internal tahan hingga 6 jam tanpa colokan listrik. Cocok untuk arisan, gathering, MC, dan senam.",
      packageContents: [
        "Speaker aktif troli 12 inch",
        "2x Mic wireless UHF jarak 30 meter",
        "Kabel audio bluetooth/aux input",
        "Kabel charger aki"
      ],
      condition: "Suara vokal bulat jernih tanpa feedback mendengung."
    },
    {
      id: 25,
      name: "Lampu Sorot Panggung Moving Head & Par LED RGBW",
      category: "pesta",
      subcategory: "Lighting",
      pricePerDay: 180000,
      deposit: 350000,
      distance: "2,7 km",
      distanceKm: 2.7,
      rating: 4.6,
      reviewsCount: 14,
      locationName: "Bangka, Jakarta Selatan",
      lat: -6.2589,
      lng: 106.8221,
      images: [
        "https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?w=800&q=80"
      ],
      description: "Pencahayaan panggung dramatis dengan mode sound-activated otomatis mengikuti dentuman musik. Cocok untuk pesta private atau mini konser.",
      packageContents: [
        "2x Moving Head Beam Light",
        "2x Par LED 54x3W RGBW",
        "Kabel sinyal DMX & power"
      ],
      condition: "Motor gerak rotasi halus, warna lampu LED terang pekat."
    },
    {
      id: 26,
      name: "Mesin Smoke Fogger Panggung 900W + Liquid Cairan Fog",
      category: "pesta",
      subcategory: "Efek",
      pricePerDay: 80000,
      deposit: 150000,
      distance: "2,1 km",
      distanceKm: 2.1,
      rating: 4.7,
      reviewsCount: 19,
      locationName: "Mampang, Jakarta Selatan",
      lat: -6.2482,
      lng: 106.8295,
      images: [
        "https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=800&q=80"
      ],
      description: "Mesin pembuat efek asap kabut panggung untuk memaksimalkan efek sorotan lampu dan laser pesta agar terlihat memukau.",
      packageContents: [
        "Unit Mesin Asap 900 Watt",
        "Remote kontrol nirkabel & tombol kabel",
        "1 Liter cairan liquid asap wangi non-toxic"
      ],
      condition: "Pemanasan cepat 3 menit, semburan asap tebal dan merata."
    },

    // --- Rumah tangga (3 items) ---
    {
      id: 27,
      name: "Mesin Cuci Karpet & Sofa Wet Vacuum Extractor Karcher",
      category: "rumahtangga",
      subcategory: "Pembersih",
      pricePerDay: 120000,
      deposit: 250000,
      distance: "1,6 km",
      distanceKm: 1.6,
      rating: 4.9,
      reviewsCount: 37,
      locationName: "Pondok Pinang, Jakarta Selatan",
      lat: -6.2781,
      lng: 106.7725,
      images: [
        "https://images.unsplash.com/photo-1558317374-067fb5f30001?w=800&q=80"
      ],
      description: "Mesin spray extraction spesialis mencuci kasur springbed, sofa kain, jok mobil, dan karpet rumah hingga tuntas membasmi tungau dan noda membandel.",
      packageContents: [
        "Unit Karcher Spray Extraction Cleaner",
        "Upholstery hand nozzle untuk sofa/kursi",
        "Floor nozzle untuk karpet",
        "Detergen tablet pembersih khusus kain"
      ],
      condition: "Daya sedot vacum sangat kuat, hasil cuci cepat kering."
    },
    {
      id: 28,
      name: "Robot Vacuum Cleaner Roborock S8 Pro Ultra Mop",
      category: "rumahtangga",
      subcategory: "Pembersih",
      pricePerDay: 110000,
      deposit: 250000,
      distance: "2,8 km",
      distanceKm: 2.8,
      rating: 4.8,
      reviewsCount: 23,
      locationName: "Kemang, Jakarta Selatan",
      lat: -6.2642,
      lng: 106.8115,
      images: [
        "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&q=80"
      ],
      description: "Robot pintar penyedot debu dan pengepel lantai otomatis dengan navigasi LiDAR 3D. Menjangkau kolong tempat tidur dan membersihkan mandiri.",
      packageContents: [
        "Robot Roborock S8",
        "Docking station pengisian daya",
        "Kain pel microfiber terpasang"
      ],
      condition: "Sensor anti tabrak akurat, baterai prima untuk 120 m²."
    },
    {
      id: 29,
      name: "Mesin Pemotong Rumput Baterai Cordless Stihl Praktis",
      category: "rumahtangga",
      subcategory: "Kebun",
      pricePerDay: 70000,
      deposit: 150000,
      distance: "2,1 km",
      distanceKm: 2.1,
      rating: 4.6,
      reviewsCount: 17,
      locationName: "Jagakarsa, Jakarta Selatan",
      lat: -6.3152,
      lng: 106.8291,
      images: [
        "https://images.unsplash.com/photo-1592417817098-8f3d6ef23912?w=800&q=80"
      ],
      description: "Mesin potong rumput senar tanpa polusi bising mesin bensin. Ringan dan nyaman untuk merapikan halaman rumah di akhir pekan.",
      packageContents: [
        "Mesin Trimmer Rumput Stihl Cordless",
        "2x Baterai Li-Ion",
        "Fast charger",
        "Kacamata safety pelindung mata"
      ],
      condition: "Motor bertenaga, putaran senar lancar dan seimbang."
    }
  ],

  sampleReviews: [
    {
      id: 1,
      name: "Aditya Pratama",
      avatar: "A",
      rating: 5,
      date: "3 hari yang lalu",
      text: "Barang sangat terawat dan berfungsi sempurna sesuai deskripsi. Dimas ramah dan responsnya cepat sekali saat serah terima.",
      tags: ["Tepat waktu", "Barang sesuai", "Komunikatif"]
    },
    {
      id: 2,
      name: "Siti Rahma",
      avatar: "S",
      rating: 5,
      date: "1 minggu yang lalu",
      text: "Dipakai untuk dokumentasi acara wisuda seharian berjalan lancar tanpa kendala. Baterai sehat dan kelengkapan aman.",
      tags: ["Barang sesuai", "Kondisi prima"]
    },
    {
      id: 3,
      name: "Budi Santoso",
      avatar: "B",
      rating: 4,
      date: "2 minggu yang lalu",
      text: "Proses cepat dan aman lewat Rentfy. Lokasi pengambilan mudah dijangkau di Kebayoran Baru.",
      tags: ["Tepat waktu", "Proses mudah"]
    }
  ],

  howItWorks: [
    {
      step: "1",
      iconType: "search",
      title: "Cari dan pilih",
      desc: "Temukan berbagai barang layak sewa dari pemilik terverifikasi di area terdekatmu."
    },
    {
      step: "2",
      iconType: "shield",
      title: "Ajukan sewa dan bayar",
      desc: "Pilih tanggal sewa, kirim permintaan, lalu bayar dengan aman di dalam Rentfy. Dana ditahan sampai barang kembali dengan selamat."
    },
    {
      step: "3",
      iconType: "box",
      title: "Ambil dan kembalikan",
      desc: "Ambil barang sesuai kesepakatan, gunakan dengan baik, dan kembalikan tepat waktu. Deposit otomatis cair setelah dicek pemilik."
    }
  ],

  calcPrice: function(pricePerDay, days) {
    var d = Math.max(2, parseInt(days, 10) || 2);
    var p = parseInt(pricePerDay, 10) || 0;
    var sewa = p * d;
    var perlindungan = 10000;
    var commission = Math.round(sewa * 0.10); // 10% biaya layanan
    return {
      days: d,
      pricePerDay: p,
      sewa: sewa,
      perlindungan: perlindungan,
      commission: commission,
      deposit: 0,
      total: sewa + perlindungan + commission
    };
  }
};
