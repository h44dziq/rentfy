# -*- coding: utf-8 -*-
"""
Client-side JavaScript logic for Rentfy prototype
"""

def get_script_content():
    return '''
  <!-- Leaflet JS -->
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

  <script>
    // --- CATALOG DATA ---
    const CATALOG = ''' + """__CATALOG_JSON_PLACEHOLDER__""" + ''';

    // --- CATEGORIES LIST ---
    const CATEGORIES = [
      { id: "kamera", name: "Kamera dan video", icon: "📷", count: 8 },
      { id: "elektronik", name: "Elektronik", icon: "💻", count: 4 },
      { id: "perkakas", name: "Perkakas", icon: "🔧", count: 3 },
      { id: "camping", name: "Camping dan outdoor", icon: "⛺", count: 3 },
      { id: "olahraga", name: "Olahraga", icon: "🚲", count: 3 },
      { id: "pesta", name: "Pesta dan acara", icon: "🎉", count: 3 },
      { id: "rumahtangga", name: "Rumah tangga", icon: "🏠", count: 3 }
    ];

    // --- APPLICATION STATE ---
    let currentScreen = 'L1';
    let previousScreen = 'L3';
    let hasPickedLocation = false;
    let searchLocation = "Jakarta Selatan";
    let searchLat = -6.2615;
    let searchLng = 106.8106;
    let searchStartDate = "2026-11-17";
    let searchEndDate = "2026-11-18";
    let searchQuery = "";
    let currentCategory = "Semua";
    let currentSubcategory = "Semua";
    let currentSort = "Terdekat";
    let currentViewL5 = "list";
    let savedItemIds = new Set();
    
    // Currently selected item for L6 detail & rental flow
    let selectedItem = CATALOG[0]; // Default mirrorless

    // Current active order state
    let currentOrder = {
      orderId: "#RF-20261117-001",
      item: CATALOG[0],
      startDate: "2026-11-17",
      endDate: "2026-11-18",
      days: 2,
      sewa: 300000,
      perlindungan: 10000,
      deposit: 300000,
      total: 610000,
      message: "",
      status: "Menunggu pemilik", // Status flow: Menunggu pemilik -> Permintaan diterima -> Dana ditahan, siap diambil -> Sedang disewa -> Menunggu pengecekan -> Selesai
      stepIndex: 1, // 1 to 5
      review: null
    };

    let completedOrders = [];
    let l12Step = 1;
    let l17Rating = 5;

    // Leaflet map instances
    let mapL4 = null;
    let markerL4 = null;
    let mapL5 = null;
    let markersLayerL5 = null;
    let mapL6 = null;
    let circleL6 = null;
    let mapL14 = null;
    let markerL14 = null;

    // Auto timers
    let ownerAcceptTimer = null;
    let returnCheckTimer = null;

    // --- UTILITIES ---
    function formatRupiah(num) {
      return "Rp" + Number(num).toLocaleString('id-ID');
    }

    function formatDateIndo(dateStr) {
      if (!dateStr) return "";
      const parts = dateStr.split('-');
      if (parts.length < 3) return dateStr;
      const months = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"];
      const day = parseInt(parts[2], 10);
      const monthIdx = parseInt(parts[1], 10) - 1;
      return `${day} ${months[monthIdx]}`;
    }

    function calcDays(d1Str, d2Str) {
      try {
        const d1 = new Date(d1Str);
        const d2 = new Date(d2Str);
        const diffTime = Math.abs(d2 - d1);
        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        return Math.max(2, diffDays || 2);
      } catch (e) {
        return 2;
      }
    }

    function showToast(message, duration = 3000) {
      const toast = document.getElementById('toast');
      if (!toast) return;
      toast.textContent = message;
      toast.classList.add('show');
      clearTimeout(toast._timer);
      toast._timer = setTimeout(() => {
        toast.classList.remove('show');
      }, duration);
    }

    // --- NAVIGATION ROUTER ---
    function navigateTo(screenId, params = {}) {
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
      currentScreen = screenId;

      // Handle screen-specific renders
      if (screenId === 'L3') {
        renderL3Screen();
      } else if (screenId === 'L5') {
        if (params.category) currentCategory = params.category;
        if (params.sort) currentSort = params.sort;
        if (params.query !== undefined) searchQuery = params.query;
        renderL5Screen();
      } else if (screenId === 'L6') {
        if (params.itemId) {
          const it = CATALOG.find(x => x.id === params.itemId);
          if (it) selectedItem = it;
        }
        renderL6Screen();
      } else if (screenId === 'L7') {
        renderL7Screen();
      } else if (screenId === 'L8') {
        renderL8Screen();
      } else if (screenId === 'L9') {
        renderL9Screen(params.tab || 'berjalan');
      } else if (screenId === 'L10') {
        renderL10Screen();
      } else if (screenId === 'L11') {
        renderL11Screen();
      } else if (screenId === 'L12') {
        resetL12Verification();
      } else if (screenId === 'L13') {
        renderL13Screen();
      } else if (screenId === 'L14') {
        renderL14Screen();
      } else if (screenId === 'L15') {
        renderL15Screen();
      } else if (screenId === 'L16') {
        renderL16Screen();
      } else if (screenId === 'L17') {
        renderL17Screen();
      } else if (screenId === 'L18') {
        renderL18Screen();
      }

      // Update mobile bottom tab active states
      updateMobileTabsActive(screenId);
    }

    function updateMobileTabsActive(screenId) {
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
    }

    // --- LEAFLET MAP HELPERS (PLAIN TEXT ATTRIBUTION ONLY, NO EXTERNAL LINKS) ---
    function createPlainAttribution() {
      const el = document.createElement('div');
      el.style.cssText = 'font-size:10px; color:#4B5563; background:rgba(255,255,255,0.85); padding:2px 6px; position:absolute; bottom:0; right:0; z-index:400; border-top-left-radius:4px; pointer-events:none;';
      el.textContent = '© OpenStreetMap';
      return el;
    }

    // --- L1 & L2 INTERACTIONS ---
    function togglePasswordVisibility(fieldId, iconContainer) {
      const f = document.getElementById(fieldId);
      if (!f) return;
      if (f.type === 'password') {
        f.type = 'text';
        iconContainer.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path><line x1="1" y1="1" x2="23" y2="23"></line></svg>';
      } else {
        f.type = 'password';
        iconContainer.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>';
      }
    }

    // --- SEARCH & LOCATION PICKER (L4) ---
    function handleSearchTrigger(source) {
      let query = "";
      if (source === 'desktop') {
        const inp = document.getElementById('desktop-search-input');
        query = inp ? inp.value.trim() : "";
      } else {
        const inp = document.getElementById('mobile-search-input');
        query = inp ? inp.value.trim() : "";
      }

      if (!query) query = "camera"; // Default keyword if empty per requirement
      searchQuery = query;

      if (!hasPickedLocation) {
        // First search opens location picker L4 per requirement
        openLocationPicker();
      } else {
        navigateTo('L5', { query: searchQuery, category: 'Semua' });
      }
    }

    function handleMobileSearchTab() {
      if (!hasPickedLocation) {
        openLocationPicker();
      } else {
        navigateTo('L5', { query: searchQuery || "camera", category: 'Semua' });
      }
    }

    function openLocationPicker() {
      const modal = document.getElementById('modal-L4');
      if (modal) modal.classList.add('active');
      setTimeout(initMapL4, 150);
    }

    function closeLocationPicker() {
      const modal = document.getElementById('modal-L4');
      if (modal) modal.classList.remove('active');
    }

    function initMapL4() {
      const container = document.getElementById('map-l4');
      if (!container) return;

      if (!mapL4) {
        mapL4 = L.map('map-l4', {
          attributionControl: false,
          zoomControl: true
        }).setView([searchLat, searchLng], 14);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          maxZoom: 19
        }).addTo(mapL4);

        container.appendChild(createPlainAttribution());

        markerL4 = L.marker([searchLat, searchLng], { draggable: true }).addTo(mapL4);
        markerL4.on('dragend', function (e) {
          const pos = e.target.getLatLng();
          searchLat = pos.lat;
          searchLng = pos.lng;
        });

        mapL4.on('click', function(e) {
          searchLat = e.latlng.lat;
          searchLng = e.latlng.lng;
          if (markerL4) markerL4.setLatLng(e.latlng);
        });
      } else {
        mapL4.invalidateSize();
        mapL4.setView([searchLat, searchLng], 14);
        if (markerL4) markerL4.setLatLng([searchLat, searchLng]);
      }
    }

    function centerMapL4CurrentLocation() {
      searchLat = -6.2442;
      searchLng = 106.7992;
      searchLocation = "Kebayoran Baru, Jakarta Selatan";
      const inp = document.getElementById('l4-search-input');
      if (inp) inp.value = searchLocation;
      if (mapL4 && markerL4) {
        mapL4.setView([searchLat, searchLng], 15);
        markerL4.setLatLng([searchLat, searchLng]);
      }
      showToast('Lokasi disetel ke titik terdekat kamu');
    }

    function selectLocationSuggestion(name, lat, lng) {
      searchLocation = name + ", Jakarta Selatan";
      searchLat = lat;
      searchLng = lng;
      const inp = document.getElementById('l4-search-input');
      if (inp) inp.value = searchLocation;
      if (mapL4 && markerL4) {
        mapL4.setView([lat, lng], 15);
        markerL4.setLatLng([lat, lng]);
      }
    }

    function confirmLocationL4() {
      hasPickedLocation = true;
      const inp = document.getElementById('l4-search-input');
      if (inp && inp.value.trim()) {
        searchLocation = inp.value.trim();
      }
      // Update text labels across nav
      const lText = document.getElementById('nav-location-text');
      if (lText) lText.textContent = searchLocation.split(',')[0];
      const mlText = document.getElementById('m-nav-location-text');
      if (mlText) mlText.textContent = searchLocation.split(',')[0];
      const infoLoc = document.getElementById('l5-info-location');
      if (infoLoc) infoLoc.textContent = searchLocation.split(',')[0];

      closeLocationPicker();
      showToast(`Lokasi disetel ke ${searchLocation}`);
      navigateTo('L5', { query: searchQuery || "camera" });
    }

    // --- DATE PICKER MODAL (NAVBAR & FILTER) ---
    function openDatePickerModal() {
      const modal = document.getElementById('modal-datepicker');
      if (modal) modal.classList.add('active');
    }
    function closeDatePickerModal() {
      const modal = document.getElementById('modal-datepicker');
      if (modal) modal.classList.remove('active');
    }
    function confirmDatePickerModal() {
      const s = document.getElementById('nav-date-input-start').value;
      const e = document.getElementById('nav-date-input-end').value;
      searchStartDate = s;
      searchEndDate = e;
      const sFormatted = formatDateIndo(s);
      
      const ndText = document.getElementById('nav-date-text');
      if (ndText) ndText.textContent = sFormatted;
      const mndText = document.getElementById('m-nav-date-text');
      if (mndText) mndText.textContent = sFormatted;
      const l5Date = document.getElementById('l5-info-date');
      if (l5Date) l5Date.textContent = sFormatted;

      closeDatePickerModal();
      showToast(`Periode sewa disetel: ${sFormatted}`);
    }

    // --- FILTER MODAL (L20) ---
    function openFilterModal() {
      const m = document.getElementById('modal-L20');
      if (m) m.classList.add('active');
    }
    function closeFilterModal() {
      const m = document.getElementById('modal-L20');
      if (m) m.classList.remove('active');
    }
    function toggleFilterChip(el) {
      el.parentElement.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
      el.classList.add('active');
    }
    function selectPriceRangeChip(el, range) {
      el.parentElement.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
      el.classList.add('active');
    }
    function selectSortChipL20(sortName) {
      const group = document.getElementById('l20-sort-group');
      if (!group) return;
      group.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
      if (sortName === 'Terdekat') document.getElementById('l20-sort-terdekat').classList.add('active');
      else if (sortName === 'Termurah') document.getElementById('l20-sort-termurah').classList.add('active');
      else if (sortName === 'Rating') document.getElementById('l20-sort-rating').classList.add('active');
      currentSort = sortName;
    }
    function resetFilterModal() {
      selectSortChipL20('Terdekat');
      showToast('Filter diatur ulang ke bawaan');
    }
    function applyFilterModal() {
      closeFilterModal();
      setSortL5(currentSort);
      showToast(`Filter diterapkan (Urutan: ${currentSort})`);
    }

    // --- CONDITION PHOTOS MODAL (L14) ---
    function openConditionPhotosModal() {
      const m = document.getElementById('modal-condition-photos');
      if (m) m.classList.add('active');
    }
    function closeConditionPhotosModal() {
      const m = document.getElementById('modal-condition-photos');
      if (m) m.classList.remove('active');
      showToast('Foto kondisi barang berhasil disimpan');
    }
    function simulateConditionPhotoSlot(el, slotName) {
      el.style.borderColor = 'var(--success)';
      el.style.backgroundColor = 'var(--success-soft)';
      el.innerHTML = `
        <span style="font-size:24px; color:var(--success);">✓</span>
        <strong style="font-size:12px; color:#065F46; margin-top:4px;">${slotName} Terunggah</strong>
        <span style="font-size:10px; color:#047857;">Cap waktu: 17 Nov, 10:05</span>
      `;
      showToast(`Foto ${slotName} berhasil diambil`);
    }

    // --- SAVED / HEART TOGGLE ---
    function toggleSaveItem(itemId, event) {
      if (event) event.stopPropagation();
      if (savedItemIds.has(itemId)) {
        savedItemIds.delete(itemId);
        showToast('Dihapus dari simpanan');
      } else {
        savedItemIds.add(itemId);
        showToast('Disimpan ke barang favorit');
      }
      // Update any visible heart buttons
      document.querySelectorAll(`[data-heart-id="${itemId}"]`).forEach(btn => {
        if (savedItemIds.has(itemId)) {
          btn.classList.add('saved');
          btn.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="#EF4444" stroke="#EF4444" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>';
        } else {
          btn.classList.remove('saved');
          btn.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>';
        }
      });
    }

    function toggleSaveDetailItem() {
      if (selectedItem) toggleSaveItem(selectedItem.id);
    }

    // --- ITEM CARD HTML GENERATOR ---
    function renderItemCardHtml(item) {
      const isSaved = savedItemIds.has(item.id);
      return `
        <div class="item-card" onclick="navigateTo('L6', {itemId: ${item.id}})">
          <div class="item-card-image" style="background: ${item.gradient};">
            <div class="bg-pattern"></div>
            <button class="heart-btn ${isSaved ? 'saved' : ''}" data-heart-id="${item.id}" onclick="toggleSaveItem(${item.id}, event)" title="Simpan">
              ${isSaved ?
                '<svg width="18" height="18" viewBox="0 0 24 24" fill="#EF4444" stroke="#EF4444" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>' :
                '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>'
              }
            </button>
            <div class="overlay-title">${item.name}</div>
          </div>
          <div class="item-card-body">
            <div>
              <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4px;">
                <span class="badge badge-verified">Terverifikasi</span>
                <span style="font-size: 11px; font-weight: 600; color: #D97706;">★ ${item.rating}</span>
              </div>
              <h4 class="item-title">${item.name}</h4>
              <div class="item-meta">
                <span>📍 ${item.distance} km</span>
                <span style="color: var(--text-muted); font-size: 11px;">Dep. ${formatRupiah(item.deposit)}</span>
              </div>
            </div>
            <div class="item-price">
              ${formatRupiah(item.pricePerDay)} <span>/ hari</span>
            </div>
          </div>
        </div>
      `;
    }

    // --- L3 HOMEPAGE RENDERER ---
    function renderL3Screen() {
      // Inject Nav, Footer, Mobile Tabs
      const navCont = document.getElementById('l3-nav-container');
      if (navCont && !navCont.innerHTML.trim()) {
        navCont.innerHTML = getCommonNavHtml();
      }
      const footerCont = document.getElementById('l3-footer-container');
      if (footerCont && !footerCont.innerHTML.trim()) {
        footerCont.innerHTML = getCommonFooterHtml();
      }
      const tabsCont = document.getElementById('l3-tabs-container');
      if (tabsCont && !tabsCont.innerHTML.trim()) {
        tabsCont.innerHTML = getCommonMobileTabsHtml('beranda');
      }

      // Render Categories
      const catRow = document.getElementById('l3-category-row');
      if (catRow) {
        catRow.innerHTML = CATEGORIES.map(cat => `
          <div class="category-card" onclick="navigateTo('L5', {category: '${cat.name}'})">
            <div class="category-icon">${cat.icon}</div>
            <div class="category-name">${cat.name}</div>
          </div>
        `).join('');
      }

      // Render "Dekat Kamu" (sorted by distance asc)
      const nearbyGrid = document.getElementById('l3-nearby-grid');
      if (nearbyGrid) {
        const sorted = [...CATALOG].sort((a, b) => a.distance - b.distance).slice(0, 4);
        nearbyGrid.innerHTML = sorted.map(renderItemCardHtml).join('');
      }

      // Render "Paling sering disewa" (sorted by rating desc)
      const popGrid = document.getElementById('l3-popular-grid');
      if (popGrid) {
        const sorted = [...CATALOG].sort((a, b) => b.rating - a.rating).slice(0, 4);
        popGrid.innerHTML = sorted.map(renderItemCardHtml).join('');
      }
    }

    // --- L5 SEARCH RESULTS RENDERER ---
    function renderL5Screen() {
      // Inject Nav & Footer
      const navCont = document.getElementById('l5-nav-container');
      if (navCont && !navCont.innerHTML.trim()) {
        navCont.innerHTML = getCommonNavHtml();
      }
      const footerCont = document.getElementById('l5-footer-container');
      if (footerCont && !footerCont.innerHTML.trim()) {
        footerCont.innerHTML = getCommonFooterHtml();
      }
      const tabsCont = document.getElementById('l5-tabs-container');
      if (tabsCont && !tabsCont.innerHTML.trim()) {
        tabsCont.innerHTML = getCommonMobileTabsHtml('cari');
      }

      // Subcategories Chips for Kamera / Current category
      const subcatRow = document.getElementById('l5-subcategory-chips');
      if (subcatRow) {
        let subs = ["Semua"];
        if (currentCategory === "Kamera dan video" || (!currentCategory || currentCategory === "Semua")) {
          subs = ["Semua", "Kamera mirrorless", "Kamera saku", "Kamera aksi", "Kamera polaroid", "Tas kamera", "Gimbal", "Aksesori"];
        } else {
          const categoryItems = CATALOG.filter(x => x.category === currentCategory);
          const distinctSubs = Array.from(new Set(categoryItems.map(x => x.subcategory)));
          subs = ["Semua", ...distinctSubs];
        }

        subcatRow.innerHTML = subs.map(sub => `
          <button class="chip ${sub === currentSubcategory ? 'active' : ''}" onclick="selectSubcategoryL5('${sub}')">${sub}</button>
        `).join('');
      }

      // Title & count
      const titleEl = document.getElementById('l5-result-title');
      const countEl = document.getElementById('l5-result-count');

      // Filter catalog
      let filtered = CATALOG.filter(item => {
        // Query match
        let matchQuery = true;
        if (searchQuery && searchQuery.trim()) {
          const q = searchQuery.toLowerCase().trim();
          matchQuery = item.name.toLowerCase().includes(q) ||
                       item.category.toLowerCase().includes(q) ||
                       item.subcategory.toLowerCase().includes(q) ||
                       (q === "camera" && item.category === "Kamera dan video") ||
                       (q === "tenda" && item.category === "Camping dan outdoor") ||
                       (q === "bor" && item.category === "Perkakas");
        }

        // Category match
        let matchCat = true;
        if (currentCategory && currentCategory !== "Semua") {
          matchCat = item.category === currentCategory;
        }

        // Subcategory match
        let matchSub = true;
        if (currentSubcategory && currentSubcategory !== "Semua") {
          matchSub = item.subcategory === currentSubcategory;
        }

        return matchQuery && matchCat && matchSub;
      });

      // Sort items
      if (currentSort === 'Terdekat') {
        filtered.sort((a, b) => a.distance - b.distance);
      } else if (currentSort === 'Termurah') {
        filtered.sort((a, b) => a.pricePerDay - b.pricePerDay);
      } else if (currentSort === 'Rating') {
        filtered.sort((a, b) => b.rating - a.rating);
      }

      // Update Header Info
      if (titleEl) {
        if (searchQuery) titleEl.textContent = `Hasil untuk "${searchQuery}"`;
        else if (currentCategory !== "Semua") titleEl.textContent = `Kategori "${currentCategory}"`;
        else titleEl.textContent = `Semua Barang Sewa`;
      }
      if (countEl) countEl.textContent = `${filtered.length} barang ditemukan`;

      // Update Sort Chip styling
      ['terdekat', 'termurah', 'rating'].forEach(st => {
        const el = document.getElementById('sort-' + st);
        if (el) {
          if (st === currentSort.toLowerCase()) el.classList.add('active');
          else el.classList.remove('active');
        }
      });

      // Render Grid
      const grid = document.getElementById('l5-items-grid');
      const emptyState = document.getElementById('l5-empty-state');
      if (grid && emptyState) {
        if (filtered.length === 0) {
          grid.style.display = 'none';
          emptyState.style.display = 'block';
        } else {
          grid.style.display = 'grid';
          emptyState.style.display = 'none';
          grid.innerHTML = filtered.map(renderItemCardHtml).join('');
        }
      }

      // Update Map View
      if (currentViewL5 === 'map') {
        setTimeout(() => updateMapL5(filtered), 150);
      }
    }

    function selectSubcategoryL5(sub) {
      currentSubcategory = sub;
      renderL5Screen();
    }

    function setSortL5(sortType) {
      currentSort = sortType;
      renderL5Screen();
    }

    function toggleViewL5(viewType) {
      currentViewL5 = viewType;
      const listView = document.getElementById('l5-list-view');
      const mapView = document.getElementById('l5-map-view');
      const btnList = document.getElementById('view-toggle-list');
      const btnMap = document.getElementById('view-toggle-map');

      if (viewType === 'list') {
        listView.style.display = 'block';
        mapView.style.display = 'none';
        btnList.style.background = 'var(--primary-light)';
        btnList.style.color = 'var(--primary)';
        btnMap.style.background = 'transparent';
        btnMap.style.color = 'var(--text-muted)';
      } else {
        listView.style.display = 'none';
        mapView.style.display = 'block';
        btnMap.style.background = 'var(--primary-light)';
        btnMap.style.color = 'var(--primary)';
        btnList.style.background = 'transparent';
        btnList.style.color = 'var(--text-muted)';
        setTimeout(() => {
          renderL5Screen();
        }, 100);
      }
    }

    function updateMapL5(items) {
      const container = document.getElementById('map-l5');
      if (!container) return;

      if (!mapL5) {
        mapL5 = L.map('map-l5', {
          attributionControl: false,
          zoomControl: true
        }).setView([-6.25, 106.81], 13);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          maxZoom: 19
        }).addTo(mapL5);

        container.appendChild(createPlainAttribution());
        markersLayerL5 = L.layerGroup().addTo(mapL5);
      }

      mapL5.invalidateSize();
      if (markersLayerL5) markersLayerL5.clearLayers();

      if (items.length === 0) return;

      const bounds = [];
      items.forEach(item => {
        const lat = item.lat || -6.2442;
        const lng = item.lng || 106.7992;
        bounds.push([lat, lng]);

        // Custom HTML marker pill
        const priceLabel = "Rp" + Math.round(item.pricePerDay / 1000) + "rb";
        const icon = L.divIcon({
          className: 'price-marker-div',
          html: `<div class="price-marker-pill" onclick="navigateTo('L6', {itemId: ${item.id}})">${priceLabel}</div>`,
          iconSize: [60, 26],
          iconAnchor: [30, 13]
        });

        const marker = L.marker([lat, lng], { icon: icon });
        marker.bindPopup(`
          <div style="font-family:'Inter',sans-serif; min-width:180px; padding:4px;">
            <strong style="font-size:13px; display:block; margin-bottom:4px;">${item.name}</strong>
            <div style="font-size:12px; color:#0F5C63; font-weight:700; margin-bottom:6px;">${formatRupiah(item.pricePerDay)}/hari</div>
            <button class="btn btn-primary btn-sm" onclick="navigateTo('L6', {itemId: ${item.id}})" style="width:100%;">Lihat Detail</button>
          </div>
        `);
        markersLayerL5.addLayer(marker);
      });

      if (bounds.length > 0) {
        mapL5.fitBounds(bounds, { padding: [40, 40], maxZoom: 15 });
      }
    }

    function resetSearchL5() {
      searchQuery = "";
      currentCategory = "Semua";
      currentSubcategory = "Semua";
      currentSort = "Terdekat";
      renderL5Screen();
    }

    // --- L6 ITEM DETAIL RENDERER ---
    function renderL6Screen() {
      const it = selectedItem || CATALOG[0];

      // Inject Nav & Footer
      const navCont = document.getElementById('l6-nav-container');
      if (navCont && !navCont.innerHTML.trim()) navCont.innerHTML = getCommonNavHtml();
      const footerCont = document.getElementById('l6-footer-container');
      if (footerCont && !footerCont.innerHTML.trim()) footerCont.innerHTML = getCommonFooterHtml();

      // Main Gallery
      const mainGal = document.getElementById('l6-gallery-main');
      if (mainGal) mainGal.style.background = it.gradient;
      const galTitle = document.getElementById('l6-gallery-title');
      if (galTitle) galTitle.textContent = it.name;

      // Item titles & badges
      document.getElementById('l6-item-title').textContent = it.name;
      document.getElementById('l6-badge-category').textContent = it.category;
      document.getElementById('l6-item-rating').textContent = it.rating;
      document.getElementById('l6-item-reviews').textContent = `(${it.reviewsCount} ulasan)`;
      document.getElementById('l6-item-area').textContent = `📍 ${it.area || 'Kebayoran Baru, Jakarta Selatan'} · ${it.distance} km`;
      document.getElementById('l6-price-per-day').textContent = formatRupiah(it.pricePerDay);
      document.getElementById('l6-deposit-amount').textContent = formatRupiah(it.deposit);
      document.getElementById('l6-item-description').textContent = it.desc;
      document.getElementById('l6-approx-area').textContent = it.area || 'Kebayoran Baru, Jakarta Selatan';

      // Package contents
      const pkgList = document.getElementById('l6-package-contents');
      if (pkgList) {
        pkgList.innerHTML = it.packageContents.map(c => `<li>${c}</li>`).join('');
      }

      // Heart button
      const heartBtn = document.getElementById('l6-heart-btn');
      if (heartBtn) {
        if (savedItemIds.has(it.id)) {
          heartBtn.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="#EF4444" stroke="#EF4444" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>';
        } else {
          heartBtn.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>';
        }
      }

      // Pricing for periods
      document.getElementById('l6-period-1d').textContent = formatRupiah(it.pricePerDay);
      document.getElementById('l6-period-2d').textContent = formatRupiah(it.pricePerDay * 2);
      document.getElementById('l6-period-3d').textContent = formatRupiah(it.pricePerDay * 3);
      document.getElementById('l6-period-7d').textContent = formatRupiah(Math.round(it.pricePerDay * 7 * 0.9));

      // Calculate Dates & Prices
      handleL6DateChange();

      // Render Similar items (4 items from same category)
      const simGrid = document.getElementById('l6-similar-grid');
      if (simGrid) {
        const sims = CATALOG.filter(x => x.category === it.category && x.id !== it.id).slice(0, 4);
        if (sims.length < 4) {
          const others = CATALOG.filter(x => x.id !== it.id && !sims.includes(x)).slice(0, 4 - sims.length);
          sims.push(...others);
        }
        simGrid.innerHTML = sims.map(renderItemCardHtml).join('');
      }

      // Map L6 (approximate circle)
      setTimeout(initMapL6, 150);
    }

    function switchGalleryTab(idx, label) {
      const it = selectedItem || CATALOG[0];
      const mainGal = document.getElementById('l6-gallery-main');
      const viewLabel = document.getElementById('l6-gallery-view-label');
      if (viewLabel) viewLabel.textContent = label;
      
      const tabBtns = mainGal.parentElement.querySelectorAll('.chip');
      tabBtns.forEach((b, i) => {
        if (i === idx) b.classList.add('active');
        else b.classList.remove('active');
      });
    }

    function handleL6DateChange() {
      const it = selectedItem || CATALOG[0];
      const sInput = document.getElementById('l6-date-start');
      const eInput = document.getElementById('l6-date-end');
      const sVal = sInput ? sInput.value : "2026-11-17";
      const eVal = eInput ? eInput.value : "2026-11-18";

      const days = calcDays(sVal, eVal);
      const sewa = it.pricePerDay * days;
      const perlindungan = 10000;
      const deposit = it.deposit;
      const total = sewa + perlindungan + deposit;

      // Update Order State
      currentOrder.item = it;
      currentOrder.startDate = sVal;
      currentOrder.endDate = eVal;
      currentOrder.days = days;
      currentOrder.sewa = sewa;
      currentOrder.perlindungan = perlindungan;
      currentOrder.deposit = deposit;
      currentOrder.total = total;

      // Update UI in L6
      document.getElementById('l6-calc-days-label').textContent = `Sewa (${days} hari kalender)`;
      document.getElementById('l6-calc-sewa-val').textContent = formatRupiah(sewa);
      document.getElementById('l6-calc-deposit-val').textContent = formatRupiah(deposit);
      document.getElementById('l6-calc-total-val').textContent = formatRupiah(total);

      document.getElementById('l6-bar-days').textContent = `${days} hari`;
      document.getElementById('l6-bar-total').textContent = formatRupiah(sewa);
    }

    function resetL6Dates() {
      document.getElementById('l6-date-start').value = "2026-11-17";
      document.getElementById('l6-date-end').value = "2026-11-18";
      handleL6DateChange();
      showToast('Tanggal dikembalikan ke 17 - 18 Nov (2 hari)');
    }

    function initMapL6() {
      const container = document.getElementById('map-l6');
      if (!container) return;
      const it = selectedItem || CATALOG[0];
      const lat = it.lat || -6.2442;
      const lng = it.lng || 106.7992;

      if (!mapL6) {
        mapL6 = L.map('map-l6', {
          attributionControl: false,
          zoomControl: true
        }).setView([lat, lng], 14);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          maxZoom: 19
        }).addTo(mapL6);

        container.appendChild(createPlainAttribution());

        circleL6 = L.circle([lat, lng], {
          radius: 400,
          color: '#0F5C63',
          fillColor: '#0F5C63',
          fillOpacity: 0.2
        }).addTo(mapL6);
      } else {
        mapL6.invalidateSize();
        mapL6.setView([lat, lng], 14);
        if (circleL6) circleL6.setLatLng([lat, lng]);
      }
    }

    function proceedToRentalSummary() {
      handleL6DateChange();
      navigateTo('L7');
    }

    // --- L7 RENTAL SUMMARY RENDERER ---
    function renderL7Screen() {
      const ord = currentOrder;
      const it = ord.item;

      document.getElementById('l7-item-title').textContent = it.name;
      document.getElementById('l7-category-badge').textContent = it.category;
      document.getElementById('l7-period-text').textContent = `${formatDateIndo(ord.startDate)} - ${formatDateIndo(ord.endDate)} (${ord.days} hari kalender)`;

      const thumb = document.getElementById('l7-item-thumb');
      if (thumb) {
        thumb.style.background = it.gradient;
        thumb.textContent = it.name.slice(0, 15);
      }

      document.getElementById('l7-calc-days-label').textContent = `Sewa (${ord.days} hari kalender)`;
      document.getElementById('l7-calc-sewa').textContent = formatRupiah(ord.sewa);
      document.getElementById('l7-calc-deposit').textContent = formatRupiah(ord.deposit);
      document.getElementById('l7-calc-total').textContent = formatRupiah(ord.total);
    }

    function submitRentalRequest() {
      const msg = document.getElementById('l7-message');
      if (msg) currentOrder.message = msg.value.trim();
      currentOrder.status = "Menunggu pemilik";
      currentOrder.stepIndex = 1;

      navigateTo('L8');
    }

    // --- L8 REQUEST SENT RENDERER ---
    function renderL8Screen() {
      const ord = currentOrder;
      document.getElementById('l8-item-title').textContent = ord.item.name;
      document.getElementById('l8-dates').textContent = `${formatDateIndo(ord.startDate)} - ${formatDateIndo(ord.endDate)} (${ord.days} hari)`;
      document.getElementById('l8-total').textContent = formatRupiah(ord.total);

      // Start 5-second auto transition to "Permintaan diterima" per requirement
      clearTimeout(ownerAcceptTimer);
      ownerAcceptTimer = setTimeout(() => {
        if (currentOrder.status === "Menunggu pemilik") {
          currentOrder.status = "Permintaan diterima";
          currentOrder.stepIndex = 2;
          showToast('Permintaan sewa kamu telah diterima oleh pemilik (Dimas)!');
          // If user is currently on L9 or L11, re-render
          if (currentScreen === 'L9') renderL9Screen('berjalan');
          if (currentScreen === 'L11') renderL11Screen();
        }
      }, 5000);
    }

    // --- L9 MY ORDERS RENDERER ---
    function switchOrderTab(tab) {
      renderL9Screen(tab);
    }

    function renderL9Screen(activeTab = 'berjalan') {
      // Inject Nav & Footer
      const navCont = document.getElementById('l9-nav-container');
      if (navCont && !navCont.innerHTML.trim()) navCont.innerHTML = getCommonNavHtml();
      const footerCont = document.getElementById('l9-footer-container');
      if (footerCont && !footerCont.innerHTML.trim()) footerCont.innerHTML = getCommonFooterHtml();
      const tabsCont = document.getElementById('l9-tabs-container');
      if (tabsCont && !tabsCont.innerHTML.trim()) tabsCont.innerHTML = getCommonMobileTabsHtml('pesanan');

      const btnBerjalan = document.getElementById('l9-tab-berjalan');
      const btnSelesai = document.getElementById('l9-tab-selesai');
      const contBerjalan = document.getElementById('l9-content-berjalan');
      const contSelesai = document.getElementById('l9-content-selesai');

      if (activeTab === 'berjalan') {
        btnBerjalan.style.color = 'var(--primary)';
        btnBerjalan.style.borderBottomColor = 'var(--primary)';
        btnSelesai.style.color = 'var(--text-muted)';
        btnSelesai.style.borderBottomColor = 'transparent';
        contBerjalan.style.display = 'block';
        contSelesai.style.display = 'none';
      } else {
        btnSelesai.style.color = 'var(--primary)';
        btnSelesai.style.borderBottomColor = 'var(--primary)';
        btnBerjalan.style.color = 'var(--text-muted)';
        btnBerjalan.style.borderBottomColor = 'transparent';
        contBerjalan.style.display = 'none';
        contSelesai.style.display = 'block';
      }

      // Render Active Order Card (if status not Selesai)
      const activeCont = document.getElementById('l9-active-order-container');
      if (activeCont) {
        if (currentOrder.status === 'Selesai') {
          activeCont.innerHTML = `
            <div style="text-align: center; padding: 48px 16px;">
              <div style="width: 56px; height: 56px; border-radius: 50%; background: #F1F5F9; color: var(--text-muted); display: inline-flex; align-items: center; justify-content: center; margin-bottom: 12px;">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
              </div>
              <h3 style="font-size: 16px; font-weight: 600; margin-bottom: 4px;">Tidak ada pesanan berjalan</h3>
              <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 20px;">Semua pesanan kamu telah selesai atau belum ada pengajuan baru.</p>
              <button class="btn btn-amber" style="width: auto; margin: 0 auto;" onclick="navigateTo('L3')">Mulai cari barang</button>
            </div>
          `;
          document.getElementById('l9-count-berjalan').textContent = "0";
        } else {
          document.getElementById('l9-count-berjalan').textContent = "1";
          const ord = currentOrder;
          const it = ord.item;

          // Status badge config
          let badgeClass = "badge-yellow";
          let actionLabel = "Lihat detail pesanan";
          let actionFn = "navigateTo('L11')";

          if (ord.status === "Menunggu pemilik") {
            badgeClass = "badge-yellow";
            actionLabel = "Kirim pesan ke pemilik";
            actionFn = "navigateTo('L10')";
          } else if (ord.status === "Permintaan diterima") {
            badgeClass = "badge-yellow";
            actionLabel = "Verifikasi dan bayar";
            actionFn = "navigateTo('L12')";
          } else if (ord.status === "Dana ditahan, siap diambil") {
            badgeClass = "badge-teal";
            actionLabel = "Lihat cara pengambilan";
            actionFn = "navigateTo('L14')";
          } else if (ord.status === "Sedang disewa") {
            badgeClass = "badge-teal";
            actionLabel = "Lihat masa sewa";
            actionFn = "navigateTo('L15')";
          } else if (ord.status === "Menunggu pengecekan") {
            badgeClass = "badge-teal";
            actionLabel = "Lihat status pengecekan";
            actionFn = "navigateTo('L17')";
          }

          activeCont.innerHTML = `
            <div class="card card-elevated" style="cursor: pointer; transition: transform 0.15s;" onclick="navigateTo('L11')">
              <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding-bottom: 12px; margin-bottom: 14px;">
                <span style="font-size: 12px; font-weight: 600; color: var(--text-muted);">${ord.orderId}</span>
                <span class="badge ${badgeClass}">${ord.status}</span>
              </div>
              <div style="display: flex; gap: 16px; align-items: center; margin-bottom: 16px;">
                <div style="width: 72px; height: 56px; border-radius: var(--radius-md); background: ${it.gradient}; color: white; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 700; text-align: center; padding: 4px;">
                  ${it.name.slice(0, 12)}
                </div>
                <div style="flex: 1;">
                  <h4 style="font-size: 15px; font-weight: 600; line-height: 1.3;">${it.name}</h4>
                  <div style="font-size: 12px; color: var(--text-muted); margin-top: 3px;">
                    📅 ${formatDateIndo(ord.startDate)} - ${formatDateIndo(ord.endDate)} (${ord.days} hari)
                  </div>
                  <div style="font-size: 13px; font-weight: 700; color: var(--primary); margin-top: 4px;">
                    Total: ${formatRupiah(ord.total)}
                  </div>
                </div>
              </div>
              <div style="display: flex; justify-content: flex-end; gap: 8px;">
                <button class="btn btn-amber btn-sm" style="width: auto; padding: 8px 18px;" onclick="event.stopPropagation(); ${actionFn};">
                  ${actionLabel}
                </button>
              </div>
            </div>
          `;
        }
      }

      // Render Selesai Tab Content
      const selesaiCont = document.getElementById('l9-completed-order-container');
      if (selesaiCont) {
        if (completedOrders.length > 0 || currentOrder.status === 'Selesai') {
          document.getElementById('l9-count-selesai').textContent = "1";
          const ord = currentOrder;
          const it = ord.item;
          selesaiCont.innerHTML = `
            <div class="card card-elevated" style="cursor: pointer;" onclick="navigateTo('L11')">
              <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding-bottom: 12px; margin-bottom: 14px;">
                <span style="font-size: 12px; font-weight: 600; color: var(--text-muted);">${ord.orderId}</span>
                <span class="badge badge-green">✓ Selesai</span>
              </div>
              <div style="display: flex; gap: 16px; align-items: center; margin-bottom: 16px;">
                <div style="width: 72px; height: 56px; border-radius: var(--radius-md); background: ${it.gradient}; color: white; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 700; text-align: center; padding: 4px;">
                  ${it.name.slice(0, 12)}
                </div>
                <div style="flex: 1;">
                  <h4 style="font-size: 15px; font-weight: 600;">${it.name}</h4>
                  <div style="font-size: 12px; color: var(--text-muted);">
                    Selesai disewa · Deposit telah dikembalikan
                  </div>
                  <div style="font-size: 13px; font-weight: 600; color: var(--primary); margin-top: 4px;">
                    Total Sewa: ${formatRupiah(ord.sewa + ord.perlindungan)}
                  </div>
                </div>
              </div>
              <div style="display: flex; justify-content: flex-end; gap: 8px;">
                <button class="btn btn-outline btn-sm" style="width: auto;" onclick="event.stopPropagation(); navigateTo('L17');">
                  Lihat ulasan & ringkasan
                </button>
              </div>
            </div>
          `;
        } else {
          document.getElementById('l9-count-selesai').textContent = "0";
        }
      }
    }

    // --- L10 CHAT WITH OWNER RENDERER ---
    function renderL10Screen() {
      const it = currentOrder.item;
      document.getElementById('l10-item-title').textContent = it.name;
      document.getElementById('l10-item-dates').textContent = `${formatDateIndo(currentOrder.startDate)} - ${formatDateIndo(currentOrder.endDate)} (${currentOrder.days} hari)`;
      const thumb = document.getElementById('l10-item-thumb');
      if (thumb) {
        thumb.style.background = it.gradient;
        thumb.textContent = it.name.slice(0, 8);
      }
    }

    function navigateBackFromChat() {
      if (previousScreen === 'L6' || previousScreen === 'L8' || previousScreen === 'L11' || previousScreen === 'L14' || previousScreen === 'L15') {
        navigateTo(previousScreen);
      } else {
        navigateTo('L6');
      }
    }

    function sendChatMessage() {
      const inp = document.getElementById('chat-input');
      if (!inp) return;
      const text = inp.value.trim();
      if (!text) return;

      appendChatBubble(text, 'user');
      inp.value = '';

      // Automated polite reply from Dimas after 1s
      setTimeout(() => {
        let reply = "Siap Rina! Barang sudah saya siapkan dan pastikan bersih serta berfungsi 100%. Nanti kabari saja ya kalau sudah di jalan.";
        if (text.includes("tersedia")) {
          reply = "Iya masih tersedia kak! Siap disewa untuk tanggal yang diajukan.";
        } else if (text.includes("jam")) {
          reply = "Boleh diambil mulai pukul 10.00 pagi ya kak di alamat yang tertera di aplikasi.";
        } else if (text.includes("tambah")) {
          reply = "Bisa banget kak, nanti bisa ajukan perpanjangan sewa langsung di aplikasi Rentfy ya.";
        }
        appendChatBubble(reply, 'owner');
      }, 1000);
    }

    function sendQuickReply(text) {
      appendChatBubble(text, 'user');
      setTimeout(() => {
        let reply = "Siap kak, barang sudah siap diserahkan sesuai jadwal yang disepakati!";
        if (text.includes("tersedia")) reply = "Masih ready kak! Silakan dilanjutkan proses sewanya ya.";
        if (text.includes("jam")) reply = "Bisa diambil mulai jam 10:00 WIB di Jl. Senopati No. 42.";
        if (text.includes("tambah")) reply = "Tentu bisa kak, nanti tinggal konfirmasi sebelum masa sewa habis.";
        appendChatBubble(reply, 'owner');
      }, 1000);
    }

    function appendChatBubble(text, sender) {
      const list = document.getElementById('chat-messages-list');
      if (!list) return;
      const now = new Date();
      const timeStr = `${String(now.getHours()).padStart(2,'0')}:${String(now.getMinutes()).padStart(2,'0')}`;
      const div = document.createElement('div');
      div.className = `chat-bubble ${sender}`;
      div.innerHTML = `${text}<div class="chat-time">${timeStr}</div>`;
      list.appendChild(div);
      list.scrollTop = list.scrollHeight;
    }

    // --- L11 ORDER DETAIL RENDERER ---
    function renderL11Screen() {
      const ord = currentOrder;
      const it = ord.item;

      document.getElementById('l11-item-title').textContent = it.name;
      document.getElementById('l11-item-dates').textContent = `${formatDateIndo(ord.startDate)} - ${formatDateIndo(ord.endDate)} (${ord.days} hari kalender)`;
      const thumb = document.getElementById('l11-item-thumb');
      if (thumb) {
        thumb.style.background = it.gradient;
        thumb.textContent = it.name.slice(0, 10);
      }

      // Cost breakdown
      document.getElementById('l11-calc-days-label').textContent = `Sewa (${ord.days} hari kalender)`;
      document.getElementById('l11-calc-sewa').textContent = formatRupiah(ord.sewa);
      document.getElementById('l11-calc-deposit').textContent = formatRupiah(ord.deposit);
      document.getElementById('l11-calc-total').textContent = formatRupiah(ord.total);

      // Status Badge & Timeline updates
      const badge = document.getElementById('l11-status-badge');
      badge.textContent = ord.status;

      const lockedCard = document.getElementById('l11-contact-locked');
      const unlockedCard = document.getElementById('l11-contact-unlocked');

      // Reset timeline items
      for (let i = 1; i <= 5; i++) {
        const node = document.getElementById('tl-step-' + i);
        if (node) {
          node.classList.remove('completed', 'active');
        }
      }

      const actionCont = document.getElementById('l11-action-container');

      if (ord.status === "Menunggu pemilik") {
        badge.className = "badge badge-yellow";
        document.getElementById('tl-step-1').classList.add('completed');
        document.getElementById('tl-step-2').classList.add('active');
        lockedCard.style.display = 'block';
        unlockedCard.style.display = 'none';

        actionCont.innerHTML = `<button class="btn btn-amber" onclick="navigateTo('L10')">Kirim pesan ke pemilik</button>`;
      } else if (ord.status === "Permintaan diterima") {
        badge.className = "badge badge-yellow";
        document.getElementById('tl-step-1').classList.add('completed');
        document.getElementById('tl-step-2').classList.add('completed');
        document.getElementById('tl-step-3').classList.add('active');
        lockedCard.style.display = 'block';
        unlockedCard.style.display = 'none';

        actionCont.innerHTML = `<button class="btn btn-amber" onclick="navigateTo('L12')">Verifikasi dan bayar</button>`;
      } else if (ord.status === "Dana ditahan, siap diambil") {
        badge.className = "badge badge-teal";
        document.getElementById('tl-step-1').classList.add('completed');
        document.getElementById('tl-step-2').classList.add('completed');
        document.getElementById('tl-step-3').classList.add('completed');
        document.getElementById('tl-step-4').classList.add('active');
        lockedCard.style.display = 'none';
        unlockedCard.style.display = 'block';

        actionCont.innerHTML = `<button class="btn btn-amber" onclick="navigateTo('L14')">Lihat cara pengambilan</button>`;
      } else if (ord.status === "Sedang disewa") {
        badge.className = "badge badge-teal";
        document.getElementById('tl-step-1').classList.add('completed');
        document.getElementById('tl-step-2').classList.add('completed');
        document.getElementById('tl-step-3').classList.add('completed');
        document.getElementById('tl-step-4').classList.add('completed');
        document.getElementById('tl-step-5').classList.add('active');
        lockedCard.style.display = 'none';
        unlockedCard.style.display = 'block';

        actionCont.innerHTML = `<button class="btn btn-amber" onclick="navigateTo('L15')">Lihat masa sewa</button>`;
      } else if (ord.status === "Menunggu pengecekan") {
        badge.className = "badge badge-teal";
        for (let i = 1; i <= 5; i++) document.getElementById('tl-step-' + i).classList.add('completed');
        lockedCard.style.display = 'none';
        unlockedCard.style.display = 'block';

        actionCont.innerHTML = `<button class="btn btn-amber" onclick="navigateTo('L17')">Lihat status pengecekan</button>`;
      } else if (ord.status === "Selesai") {
        badge.className = "badge badge-green";
        for (let i = 1; i <= 5; i++) document.getElementById('tl-step-' + i).classList.add('completed');
        lockedCard.style.display = 'none';
        unlockedCard.style.display = 'block';

        actionCont.innerHTML = `<button class="btn btn-amber" onclick="navigateTo('L17')">Beri ulasan</button>`;
      }
    }

    // --- L12 IDENTITY VERIFICATION RENDERER ---
    function resetL12Verification() {
      l12Step = 1;
      updateL12StepUI();
    }

    function updateL12StepUI() {
      document.getElementById('l12-step-1').style.display = l12Step === 1 ? 'block' : 'none';
      document.getElementById('l12-step-2').style.display = l12Step === 2 ? 'block' : 'none';
      document.getElementById('l12-step-3').style.display = l12Step === 3 ? 'block' : 'none';

      // Stepper node styles
      for (let i = 1; i <= 3; i++) {
        const node = document.getElementById('l12-node-' + i);
        if (node) {
          node.classList.remove('active', 'completed');
          if (i < l12Step) node.classList.add('completed');
          else if (i === l12Step) node.classList.add('active');
        }
      }

      const btn = document.getElementById('l12-action-btn');
      if (l12Step === 1) btn.textContent = "Ambil foto KTP";
      else if (l12Step === 2) btn.textContent = "Ambil foto selfie";
      else if (l12Step === 3) btn.textContent = "Kirim untuk ditinjau";
    }

    function handleL12NextStep() {
      if (l12Step === 1) {
        showToast('Foto KTP berhasil diambil');
        l12Step = 2;
        updateL12StepUI();
      } else if (l12Step === 2) {
        showToast('Foto selfie berhasil diambil');
        l12Step = 3;
        updateL12StepUI();
      } else if (l12Step === 3) {
        // Show green success modal for 2s then navigate to L13
        const modal = document.getElementById('l12-success-modal');
        if (modal) modal.classList.add('active');
        setTimeout(() => {
          if (modal) modal.classList.remove('active');
          navigateTo('L13');
        }, 2000);
      }
    }

    // --- L13 PAYMENT RENDERER ---
    function renderL13Screen() {
      const ord = currentOrder;
      const it = ord.item;

      document.getElementById('l13-item-title').textContent = it.name;
      document.getElementById('l13-item-dates').textContent = `${formatDateIndo(ord.startDate)} - ${formatDateIndo(ord.endDate)} (${ord.days} hari kalender)`;
      const thumb = document.getElementById('l13-item-thumb');
      if (thumb) {
        thumb.style.background = it.gradient;
        thumb.textContent = it.name.slice(0, 10);
      }

      document.getElementById('l13-calc-days-label').textContent = `Sewa (${ord.days} hari kalender)`;
      document.getElementById('l13-calc-sewa').textContent = formatRupiah(ord.sewa);
      document.getElementById('l13-calc-deposit').textContent = formatRupiah(ord.deposit);
      document.getElementById('l13-calc-total').textContent = formatRupiah(ord.total);
      document.getElementById('l13-qris-total').textContent = formatRupiah(ord.total);
    }

    function startQrisPaymentSimulation() {
      const modal = document.getElementById('l13-qris-modal');
      const waiting = document.getElementById('l13-qris-waiting-view');
      const success = document.getElementById('l13-qris-success-view');

      waiting.style.display = 'block';
      success.style.display = 'none';
      if (modal) modal.classList.add('active');

      // 3 seconds simulate payment confirmation
      setTimeout(() => {
        waiting.style.display = 'none';
        success.style.display = 'block';
      }, 3000);
    }

    function finishPaymentToDetail() {
      const modal = document.getElementById('l13-qris-modal');
      if (modal) modal.classList.remove('active');

      currentOrder.status = "Dana ditahan, siap diambil";
      currentOrder.stepIndex = 3;
      showToast('Pembayaran berhasil! Dana ditahan dengan aman.');
      navigateTo('L11');
    }

    // --- L14 ITEM PICKUP RENDERER ---
    function renderL14Screen() {
      setTimeout(initMapL14, 150);
    }

    function initMapL14() {
      const container = document.getElementById('map-l14');
      if (!container) return;
      const pickupLat = -6.2335;
      const pickupLng = 106.8091;

      if (!mapL14) {
        mapL14 = L.map('map-l14', {
          attributionControl: false,
          zoomControl: true
        }).setView([pickupLat, pickupLng], 16);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          maxZoom: 19
        }).addTo(mapL14);

        container.appendChild(createPlainAttribution());

        markerL14 = L.marker([pickupLat, pickupLng]).addTo(mapL14);
        markerL14.bindPopup("<b>Titik Temu:</b> Jl. Senopati No. 42").openPopup();
      } else {
        mapL14.invalidateSize();
        mapL14.setView([pickupLat, pickupLng], 16);
      }
    }

    function confirmItemReceivedL14() {
      currentOrder.status = "Sedang disewa";
      currentOrder.stepIndex = 4;
      showToast('Barang berhasil diterima! Masa sewa aktif.');
      navigateTo('L15');
    }

    // --- L15 CURRENTLY RENTING RENDERER ---
    function renderL15Screen() {
      const endD = formatDateIndo(currentOrder.endDate);
      document.getElementById('l15-return-time').textContent = `${endD} 2026, pukul 20:00 WIB`;
    }

    // --- L16 RETURN RENDERER ---
    function renderL16Screen() {
      // checklist ready
    }

    function simulatePhotoUpload(el, slotName) {
      el.style.borderColor = 'var(--success)';
      el.style.backgroundColor = 'var(--success-soft)';
      el.innerHTML = `
        <span style="font-size: 20px; color: var(--success);">✓</span>
        <span style="font-size: 11px; font-weight: 600; color: #065F46; margin-top: 4px;">${slotName}</span>
      `;
      showToast(`Foto ${slotName} terunggah`);
    }

    function submitReturnReportL16() {
      currentOrder.status = "Menunggu pengecekan";
      currentOrder.stepIndex = 5;
      showToast('Laporan pengembalian terkirim. Menunggu verifikasi pemilik.');
      navigateTo('L17');
    }

    // --- L17 RETURN COMPLETE & REVIEW RENDERER ---
    function renderL17Screen() {
      const s1 = document.getElementById('l17-state-1');
      const s2 = document.getElementById('l17-state-2');

      s1.style.display = 'block';
      s2.style.display = 'none';

      document.getElementById('l17-deposit-return-amount').textContent = formatRupiah(currentOrder.deposit);

      // Auto transition timer 5s
      clearTimeout(returnCheckTimer);
      returnCheckTimer = setTimeout(() => {
        s1.style.display = 'none';
        s2.style.display = 'block';
        showToast('Pengecekan selesai! Deposit telah dikembalikan penuh.');
      }, 5000);
    }

    function setRatingL17(val) {
      l17Rating = val;
      const stars = document.querySelectorAll('.star-rating-item');
      stars.forEach((s, idx) => {
        if (idx < val) s.style.color = '#F59E0B';
        else s.style.color = '#D1D5DB';
      });
    }

    function submitReviewL17() {
      currentOrder.status = "Selesai";
      currentOrder.review = {
        rating: l17Rating,
        comment: document.getElementById('l17-comment').value.trim()
      };
      completedOrders.push({...currentOrder});
      showToast('Terima kasih! Ulasan kamu telah terkirim.');
      navigateTo('L9', { tab: 'selesai' });
    }

    function skipReviewL17() {
      currentOrder.status = "Selesai";
      completedOrders.push({...currentOrder});
      navigateTo('L9', { tab: 'selesai' });
    }

    // --- L18 PROFILE RENDERER ---
    function renderL18Screen() {
      const navCont = document.getElementById('l18-nav-container');
      if (navCont && !navCont.innerHTML.trim()) navCont.innerHTML = getCommonNavHtml();
      const footerCont = document.getElementById('l18-footer-container');
      if (footerCont && !footerCont.innerHTML.trim()) footerCont.innerHTML = getCommonFooterHtml();
      const tabsCont = document.getElementById('l18-tabs-container');
      if (tabsCont && !tabsCont.innerHTML.trim()) tabsCont.innerHTML = getCommonMobileTabsHtml('profil');
    }

    // --- L19 HOW IT WORKS HELPER ---
    function navigateBackFromL19() {
      if (previousScreen && previousScreen !== 'L19') {
        navigateTo(previousScreen);
      } else {
        navigateTo('L3');
      }
    }

    // --- TEMPLATES INJECTION ---
    function getCommonNavHtml() {
      // Clones desktop and mobile header
      return `
        <!-- Desktop Navbar -->
        <header class="navbar">
          <div class="app-container navbar-inner">
            <div class="brand-logo" onclick="navigateTo('L3')">
              <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
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
                  <input type="text" id="desktop-search-input" placeholder="Mau sewa apa?" onkeydown="if(event.key==='Enter') handleSearchTrigger('desktop')">
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
              <button class="nav-icon-btn" onclick="navigateTo('L10')" title="Chat">
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
            <svg width="28" height="28" viewBox="0 0 32 32" fill="none">
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
      `;
    }

    function getCommonFooterHtml() {
      const template = document.getElementById('common-footer-template');
      return template ? template.innerHTML : '';
    }

    function getCommonMobileTabsHtml(activeTab) {
      return `
        <nav class="mobile-tab-bar">
          <button class="tab-item ${activeTab === 'beranda' ? 'active' : ''}" onclick="navigateTo('L3')">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
            <span>Beranda</span>
          </button>
          <button class="tab-item ${activeTab === 'cari' ? 'active' : ''}" onclick="handleMobileSearchTab()">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            <span>Cari</span>
          </button>
          <button class="tab-item ${activeTab === 'pesanan' ? 'active' : ''}" onclick="navigateTo('L9')">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
            <span>Pesanan</span>
          </button>
          <button class="tab-item ${activeTab === 'profil' ? 'active' : ''}" onclick="navigateTo('L18')">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
            <span>Profil</span>
          </button>
        </nav>
      `;
    }

    // --- INITIALIZATION ON LOAD ---
    window.addEventListener('DOMContentLoaded', () => {
      // Start at screen L1 per spec
      navigateTo('L1');
    });
  </script>
</body>
</html>
'''

print("app_script.py written successfully")
