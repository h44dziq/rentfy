# -*- coding: utf-8 -*-
"""
Generates the complete index.html for the Rentfy prototype
"""

import json
from catalog_data import build as get_catalog

catalog = get_catalog()
catalog_json = json.dumps(catalog, ensure_ascii=False)

def main():
    with open("index.html", "w", encoding="utf-8") as f:
        # Part 1: DOCTYPE and HTML head
        f.write('''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Rentfy — Sewa Barang Mudah & Aman</title>
  
  <!-- Google Fonts: Poppins (headings), Inter (body) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@500;600;700&display=swap" rel="stylesheet">
  
  <!-- Leaflet CSS -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
  
  <style>
    :root {
      --primary: #0F5C63;
      --primary-dark: #0A3F44;
      --primary-light: #E6F4F5;
      --primary-soft: #F0F8F8;
      --accent: #F59E0B;
      --accent-hover: #D97706;
      --accent-soft: #FEF3C7;
      --text-main: #1F2937;
      --text-muted: #6B7280;
      --text-light: #9CA3AF;
      --bg-page: #F8FAFC;
      --bg-surface: #FFFFFF;
      --border-color: #E2E8F0;
      --success: #10B981;
      --success-soft: #ECFDF5;
      --danger: #EF4444;
      --danger-soft: #FEE2E2;
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      --radius-xl: 24px;
      --shadow-sm: 0 1px 3px 0 rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -1px rgba(0, 0, 0, 0.04);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -2px rgba(0, 0, 0, 0.04);
      --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      color: var(--text-main);
      background-color: var(--bg-page);
      line-height: 1.5;
      font-size: 14px;
      overflow-x: hidden;
      min-height: 100vh;
    }

    h1, h2, h3, h4, h5, h6 {
      font-family: 'Poppins', sans-serif;
      font-weight: 600;
      color: var(--text-main);
      line-height: 1.25;
    }

    /* Screen visibility */
    .screen {
      display: none;
      min-height: 100vh;
      width: 100%;
    }
    .screen.active {
      display: block;
    }

    /* Containers */
    .app-container {
      max-width: 1120px;
      margin: 0 auto;
      padding: 0 16px;
    }
    .step-container {
      max-width: 580px;
      margin: 0 auto;
      padding: 24px 16px 80px;
    }
    .auth-container {
      max-width: 440px;
      margin: 0 auto;
      padding: 32px 16px;
    }

    /* Buttons */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      font-family: 'Inter', sans-serif;
      font-weight: 600;
      font-size: 14px;
      padding: 12px 20px;
      border-radius: var(--radius-md);
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.2s ease;
      text-decoration: none;
      user-select: none;
      width: 100%;
    }
    .btn:active {
      transform: scale(0.98);
    }
    .btn-amber {
      background-color: var(--accent);
      color: #111827;
      border-color: var(--accent);
      box-shadow: 0 2px 4px rgba(245, 158, 11, 0.25);
    }
    .btn-amber:hover {
      background-color: var(--accent-hover);
      border-color: var(--accent-hover);
      color: #111827;
    }
    .btn-primary {
      background-color: var(--primary);
      color: #FFFFFF;
      border-color: var(--primary);
    }
    .btn-primary:hover {
      background-color: var(--primary-dark);
      border-color: var(--primary-dark);
    }
    .btn-outline {
      background-color: transparent;
      color: var(--primary);
      border-color: var(--primary);
    }
    .btn-outline:hover {
      background-color: var(--primary-light);
    }
    .btn-secondary {
      background-color: #F1F5F9;
      color: var(--text-main);
      border-color: #E2E8F0;
    }
    .btn-secondary:hover {
      background-color: #E2E8F0;
    }
    .btn-ghost {
      background-color: transparent;
      color: var(--text-muted);
      border: none;
      padding: 8px 12px;
      width: auto;
    }
    .btn-ghost:hover {
      color: var(--text-main);
      background-color: rgba(0,0,0,0.05);
    }
    .btn-danger-outline {
      background-color: transparent;
      color: var(--danger);
      border-color: var(--danger);
    }
    .btn-danger-outline:hover {
      background-color: var(--danger-soft);
    }
    .btn-sm {
      padding: 8px 14px;
      font-size: 13px;
      border-radius: var(--radius-sm);
    }

    /* Form Inputs */
    .input-group {
      margin-bottom: 16px;
      text-align: left;
    }
    .input-label {
      display: block;
      font-size: 13px;
      font-weight: 500;
      color: var(--text-main);
      margin-bottom: 6px;
    }
    .input-field {
      width: 100%;
      padding: 12px 14px;
      font-family: 'Inter', sans-serif;
      font-size: 14px;
      color: var(--text-main);
      background-color: #FFFFFF;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      transition: all 0.2s ease;
      outline: none;
    }
    .input-field:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(15, 92, 99, 0.15);
    }
    .input-with-icon {
      position: relative;
    }
    .input-with-icon .input-field {
      padding-left: 40px;
    }
    .input-icon-left {
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-light);
      pointer-events: none;
      display: flex;
    }
    .input-icon-right {
      position: absolute;
      right: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-light);
      cursor: pointer;
      display: flex;
    }

    /* Cards */
    .card {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 16px;
      box-shadow: var(--shadow-sm);
    }

    /* Badges */
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 4px 8px;
      border-radius: 9999px;
      font-size: 11px;
      font-weight: 600;
      white-space: nowrap;
    }
    .badge-verified {
      background-color: var(--primary-light);
      color: var(--primary);
    }
    .badge-yellow {
      background-color: #FEF3C7;
      color: #92400E;
    }
    .badge-teal {
      background-color: var(--primary-light);
      color: var(--primary);
    }
    .badge-green {
      background-color: var(--success-soft);
      color: #065F46;
    }
    .badge-gray {
      background-color: #F1F5F9;
      color: var(--text-muted);
    }

    /* Top Desktop Navbar */
    .navbar {
      background: #FFFFFF;
      border-bottom: 1px solid var(--border-color);
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: var(--shadow-sm);
    }
    .navbar-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 72px;
      gap: 20px;
    }
    .brand-logo {
      display: flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      cursor: pointer;
      user-select: none;
    }
    .brand-text {
      font-family: 'Poppins', sans-serif;
      font-size: 24px;
      font-weight: 700;
      color: var(--primary);
      letter-spacing: -0.5px;
    }
    .navbar-search {
      flex: 1;
      max-width: 560px;
    }
    .navbar-actions {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .nav-link {
      font-weight: 500;
      color: var(--text-main);
      text-decoration: none;
      padding: 8px 12px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      transition: color 0.15s;
      white-space: nowrap;
    }
    .nav-link:hover {
      color: var(--primary);
      background-color: var(--primary-soft);
    }
    .nav-icon-btn {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #F1F5F9;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      position: relative;
      transition: background 0.15s;
    }
    .nav-icon-btn:hover {
      background: #E2E8F0;
      color: var(--text-main);
    }
    .avatar-btn {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 4px 10px 4px 4px;
      border-radius: 9999px;
      border: 1px solid var(--border-color);
      background: #FFFFFF;
      cursor: pointer;
      font-weight: 500;
      transition: border-color 0.15s;
    }
    .avatar-btn:hover {
      border-color: var(--primary);
    }
    .avatar-circle {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: var(--primary);
      color: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 600;
      font-size: 13px;
    }

    /* Search Box Component */
    .search-box-container {
      background: #FFFFFF;
      border: 1px solid var(--border-color);
      border-radius: 9999px;
      display: flex;
      align-items: center;
      padding: 4px 6px 4px 16px;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s ease;
    }
    .search-box-container:focus-within {
      border-color: var(--primary);
      box-shadow: 0 0 0 2px rgba(15, 92, 99, 0.15);
    }
    .search-input-col {
      flex: 1.3;
      display: flex;
      align-items: center;
      gap: 8px;
      min-width: 120px;
    }
    .search-input-col input {
      width: 100%;
      border: none;
      outline: none;
      font-family: 'Inter', sans-serif;
      font-size: 14px;
      color: var(--text-main);
      background: transparent;
    }
    .search-divider {
      width: 1px;
      height: 24px;
      background-color: var(--border-color);
      margin: 0 8px;
      flex-shrink: 0;
    }
    .search-chip-btn {
      display: flex;
      align-items: center;
      gap: 6px;
      background: transparent;
      border: none;
      font-size: 13px;
      font-weight: 500;
      color: var(--text-main);
      cursor: pointer;
      padding: 6px 10px;
      border-radius: 9999px;
      white-space: nowrap;
    }
    .search-chip-btn:hover {
      background-color: var(--primary-soft);
      color: var(--primary);
    }
    .search-submit-btn {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background-color: var(--primary);
      color: #FFFFFF;
      border: none;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      flex-shrink: 0;
      transition: background 0.15s;
    }
    .search-submit-btn:hover {
      background-color: var(--primary-dark);
    }

    /* Mobile Bottom Navigation */
    .mobile-tab-bar {
      display: none;
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      height: 64px;
      background: #FFFFFF;
      border-top: 1px solid var(--border-color);
      z-index: 99;
      justify-content: space-around;
      align-items: center;
      box-shadow: 0 -2px 5px rgba(0,0,0,0.03);
    }
    .tab-item {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 3px;
      flex: 1;
      height: 100%;
      color: var(--text-muted);
      text-decoration: none;
      font-size: 11px;
      font-weight: 500;
      cursor: pointer;
      border: none;
      background: transparent;
    }
    .tab-item.active {
      color: var(--primary);
      font-weight: 600;
    }

    /* Mobile App Bar Header */
    .mobile-app-bar {
      display: none;
      align-items: center;
      justify-content: space-between;
      height: 56px;
      padding: 0 16px;
      background: #FFFFFF;
      border-bottom: 1px solid var(--border-color);
      position: sticky;
      top: 0;
      z-index: 90;
    }
    .mobile-app-bar-title {
      font-family: 'Poppins', sans-serif;
      font-size: 16px;
      font-weight: 600;
      color: var(--text-main);
    }

    /* Item Cards & Grid */
    .items-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      margin-top: 16px;
    }

    .item-card {
      background: #FFFFFF;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      overflow: hidden;
      cursor: pointer;
      transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
      display: flex;
      flex-direction: column;
      position: relative;
    }
    .item-card:hover {
      transform: translateY(-3px);
      box-shadow: var(--shadow-md);
      border-color: #CBD5E1;
    }
    .item-card-image {
      width: 100%;
      aspect-ratio: 4 / 3;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 16px;
      color: #FFFFFF;
      text-align: center;
      overflow: hidden;
    }
    .item-card-image .overlay-title {
      font-family: 'Poppins', sans-serif;
      font-weight: 600;
      font-size: 15px;
      line-height: 1.3;
      z-index: 2;
      text-shadow: 0 2px 4px rgba(0,0,0,0.4);
    }
    .item-card-image .bg-pattern {
      position: absolute;
      inset: 0;
      opacity: 0.15;
      background-image: radial-gradient(#FFFFFF 1px, transparent 1px);
      background-size: 12px 12px;
    }
    .heart-btn {
      position: absolute;
      top: 10px;
      right: 10px;
      width: 34px;
      height: 34px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.9);
      backdrop-filter: blur(4px);
      border: none;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 5;
      color: var(--text-muted);
      transition: all 0.15s;
    }
    .heart-btn:hover {
      background: #FFFFFF;
      transform: scale(1.1);
    }
    .heart-btn.saved {
      color: #EF4444;
    }
    .item-card-body {
      padding: 14px;
      display: flex;
      flex-direction: column;
      flex: 1;
      justify-content: space-between;
    }
    .item-title {
      font-family: 'Inter', sans-serif;
      font-size: 14px;
      font-weight: 600;
      color: var(--text-main);
      line-height: 1.35;
      margin-bottom: 6px;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
      min-height: 38px;
    }
    .item-meta {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 12px;
      color: var(--text-muted);
      margin-bottom: 8px;
    }
    .item-price {
      font-family: 'Poppins', sans-serif;
      font-size: 15px;
      font-weight: 700;
      color: var(--primary);
    }
    .item-price span {
      font-size: 12px;
      font-weight: 400;
      color: var(--text-muted);
    }

    /* Category Scroll Row */
    .category-scroll-row {
      display: flex;
      gap: 12px;
      overflow-x: auto;
      padding: 6px 0 16px;
      scrollbar-width: none;
      -ms-overflow-style: none;
    }
    .category-scroll-row::-webkit-scrollbar {
      display: none;
    }
    .category-card {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 8px;
      padding: 12px 14px;
      background: #FFFFFF;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      cursor: pointer;
      white-space: nowrap;
      flex-shrink: 0;
      transition: all 0.15s;
    }
    .category-card:hover {
      border-color: var(--primary);
      background-color: var(--primary-soft);
    }
    .category-icon {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: var(--primary-light);
      color: var(--primary);
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .category-name {
      font-size: 12px;
      font-weight: 600;
      color: var(--text-main);
    }

    /* Chips */
    .chip {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: 9999px;
      font-size: 13px;
      font-weight: 500;
      background: #FFFFFF;
      border: 1px solid var(--border-color);
      color: var(--text-main);
      cursor: pointer;
      transition: all 0.15s;
      white-space: nowrap;
    }
    .chip:hover {
      border-color: var(--primary);
    }
    .chip.active {
      background: var(--primary);
      color: #FFFFFF;
      border-color: var(--primary);
    }

    /* Banners */
    .banner {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 14px 18px;
      border-radius: var(--radius-md);
      margin-bottom: 16px;
    }
    .banner-info {
      background-color: var(--primary-light);
      color: var(--primary-dark);
      border: 1px solid rgba(15, 92, 99, 0.2);
    }
    .banner-warning {
      background-color: #FEF3C7;
      color: #92400E;
      border: 1px solid rgba(245, 158, 11, 0.3);
    }
    .banner-success {
      background-color: var(--success-soft);
      color: #065F46;
      border: 1px solid rgba(16, 185, 129, 0.3);
    }

    /* Modals & Bottom Sheets */
    .modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.5);
      z-index: 1000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 16px;
      backdrop-filter: blur(2px);
    }
    .modal-backdrop.active {
      display: flex;
    }
    .modal-sheet {
      background: #FFFFFF;
      border-radius: var(--radius-xl);
      width: 100%;
      max-width: 520px;
      max-height: 90vh;
      overflow-y: auto;
      box-shadow: var(--shadow-xl);
      animation: modalFadeIn 0.2s ease;
      position: relative;
    }
    @keyframes modalFadeIn {
      from { transform: scale(0.96); opacity: 0; }
      to { transform: scale(1); opacity: 1; }
    }
    .modal-header {
      padding: 16px 20px;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .modal-body {
      padding: 20px;
    }
    .modal-footer {
      padding: 16px 20px;
      border-top: 1px solid var(--border-color);
      display: flex;
      gap: 12px;
    }

    /* Toast */
    #toast {
      position: fixed;
      bottom: 80px;
      left: 50%;
      transform: translateX(-50%) translateY(20px);
      background-color: #1F2937;
      color: #FFFFFF;
      padding: 10px 20px;
      border-radius: 9999px;
      font-size: 13px;
      font-weight: 500;
      box-shadow: var(--shadow-lg);
      z-index: 9999;
      opacity: 0;
      pointer-events: none;
      transition: all 0.25s ease;
      white-space: nowrap;
      max-width: 90vw;
      text-align: center;
    }
    #toast.show {
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }

    /* Leaflet customization - plain text attribution only, no external links */
    .leaflet-control-attribution {
      background: rgba(255, 255, 255, 0.85) !important;
      font-size: 10px !important;
      color: #4B5563 !important;
      padding: 2px 6px !important;
      border-radius: 4px !important;
    }
    .leaflet-control-attribution a {
      pointer-events: none !important;
      cursor: default !important;
      text-decoration: none !important;
      color: inherit !important;
    }

    /* Price marker pill on map */
    .price-marker-pill {
      background: var(--primary);
      color: #FFFFFF;
      font-weight: 700;
      font-size: 12px;
      padding: 4px 8px;
      border-radius: 9999px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.3);
      border: 2px solid #FFFFFF;
      white-space: nowrap;
      text-align: center;
      cursor: pointer;
    }
    .price-marker-pill:hover {
      background: var(--primary-dark);
      transform: scale(1.05);
    }

    /* Stepper */
    .stepper {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 24px;
      position: relative;
    }
    .stepper::before {
      content: '';
      position: absolute;
      top: 14px;
      left: 24px;
      right: 24px;
      height: 2px;
      background: #E2E8F0;
      z-index: 1;
    }
    .step-node {
      position: relative;
      z-index: 2;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
    }
    .step-circle {
      width: 30px;
      height: 30px;
      border-radius: 50%;
      background: #E2E8F0;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 12px;
      font-weight: 600;
      border: 2px solid #FFFFFF;
    }
    .step-node.active .step-circle {
      background: var(--primary);
      color: #FFFFFF;
    }
    .step-node.completed .step-circle {
      background: var(--success);
      color: #FFFFFF;
    }
    .step-label {
      font-size: 11px;
      font-weight: 500;
      color: var(--text-muted);
    }
    .step-node.active .step-label {
      color: var(--primary);
      font-weight: 600;
    }

    /* Timeline */
    .timeline {
      display: flex;
      flex-direction: column;
      position: relative;
      margin: 16px 0;
    }
    .timeline-item {
      display: flex;
      gap: 16px;
      position: relative;
      padding-bottom: 24px;
    }
    .timeline-item:last-child {
      padding-bottom: 0;
    }
    .timeline-line {
      position: absolute;
      left: 15px;
      top: 30px;
      bottom: 0;
      width: 2px;
      background: #E2E8F0;
    }
    .timeline-item:last-child .timeline-line {
      display: none;
    }
    .timeline-icon {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: #F1F5F9;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      z-index: 2;
      border: 2px solid #FFFFFF;
    }
    .timeline-item.completed .timeline-icon {
      background: var(--success);
      color: #FFFFFF;
    }
    .timeline-item.active .timeline-icon {
      background: var(--primary);
      color: #FFFFFF;
      box-shadow: 0 0 0 4px var(--primary-light);
    }
    .timeline-content {
      flex: 1;
      padding-top: 4px;
    }
    .timeline-title {
      font-weight: 600;
      font-size: 14px;
      color: var(--text-main);
    }
    .timeline-desc {
      font-size: 12px;
      color: var(--text-muted);
      margin-top: 2px;
    }

    /* Chat UI */
    .chat-container {
      display: flex;
      flex-direction: column;
      height: calc(100vh - 180px);
      max-width: 640px;
      margin: 0 auto;
      background: #FFFFFF;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      overflow: hidden;
    }
    .chat-messages {
      flex: 1;
      overflow-y: auto;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .chat-bubble {
      max-width: 78%;
      padding: 10px 14px;
      border-radius: 16px;
      font-size: 13px;
      line-height: 1.4;
      position: relative;
    }
    .chat-bubble.owner {
      background: #F1F5F9;
      color: var(--text-main);
      align-self: flex-start;
      border-bottom-left-radius: 4px;
    }
    .chat-bubble.user {
      background: var(--primary);
      color: #FFFFFF;
      align-self: flex-end;
      border-bottom-right-radius: 4px;
    }
    .chat-time {
      font-size: 10px;
      opacity: 0.7;
      margin-top: 4px;
      text-align: right;
    }

    /* Footer */
    .footer {
      background: #FFFFFF;
      border-top: 1px solid var(--border-color);
      padding: 48px 16px 32px;
      margin-top: 60px;
    }
    .footer-grid {
      display: grid;
      grid-template-columns: 2fr 1fr 1fr 1fr;
      gap: 32px;
      max-width: 1120px;
      margin: 0 auto;
    }
    .footer-col h5 {
      font-family: 'Poppins', sans-serif;
      font-size: 14px;
      font-weight: 600;
      margin-bottom: 16px;
      color: var(--text-main);
    }
    .footer-links {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .footer-links a, .footer-links button {
      color: var(--text-muted);
      text-decoration: none;
      font-size: 13px;
      background: none;
      border: none;
      padding: 0;
      text-align: left;
      cursor: pointer;
      font-family: inherit;
    }
    .footer-links a:hover, .footer-links button:hover {
      color: var(--primary);
    }
    .footer-bottom {
      max-width: 1120px;
      margin: 32px auto 0;
      padding-top: 24px;
      border-top: 1px solid var(--border-color);
      font-size: 12px;
      color: var(--text-muted);
      text-align: center;
    }

    /* Sticky Bottom Bar on detail page */
    .detail-bottom-bar {
      position: sticky;
      bottom: 0;
      left: 0;
      right: 0;
      background: #FFFFFF;
      border-top: 1px solid var(--border-color);
      padding: 12px 16px;
      z-index: 80;
      box-shadow: 0 -4px 10px rgba(0,0,0,0.05);
    }
    .detail-bottom-inner {
      max-width: 1120px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }

    @media (min-width: 640px) {
      .detail-bottom-bar {
        display: none !important;
      }
    }
    @media (max-width: 639px) {
      .detail-desktop-sidebar-btn {
        display: none !important;
      }
    }

    /* Responsive Breakpoints */
    @media (max-width: 1023px) {
      .items-grid {
        grid-template-columns: repeat(3, 1fr);
      }
      .footer-grid {
        grid-template-columns: 1fr 1fr;
      }
    }
    @media (max-width: 639px) {
      .items-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 12px;
      }
      .navbar {
        display: none;
      }
      .mobile-app-bar {
        display: flex;
      }
      .mobile-tab-bar {
        display: flex;
      }
      .footer {
        margin-bottom: 64px;
        padding: 32px 16px;
      }
      .footer-grid {
        grid-template-columns: 1fr;
        gap: 24px;
      }
      .modal-backdrop {
        padding: 0;
        align-items: flex-end;
      }
      .modal-sheet {
        border-bottom-left-radius: 0;
        border-bottom-right-radius: 0;
        max-height: 85vh;
      }
      .detail-bottom-bar {
        bottom: 64px;
      }
    }
  </style>
</head>
<body>
''')
        print("Head written")

if __name__ == "__main__":
    main()
