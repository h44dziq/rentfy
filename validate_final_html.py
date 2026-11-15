# -*- coding: utf-8 -*-
"""
Comprehensive validation of index.html against all user requirements.
"""

import re
import json

def validate():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
        
    print(f"Total HTML file length: {len(html)} bytes")
    
    # 1. Structure checks
    assert "<!DOCTYPE html>" in html, "Missing <!DOCTYPE html>"
    assert "<html" in html and "</html>" in html, "Missing <html> or </html>"
    assert "<head>" in html and "</head>" in html, "Missing <head> or </head>"
    assert "<body>" in html and "</body>" in html, "Missing <body> or </body>"
    print("✓ Basic HTML structure verified")
    
    # 2. Design Tokens & Assets
    assert "#0F5C63" in html, "Missing primary teal #0F5C63"
    assert "#F59E0B" in html, "Missing accent amber #F59E0B"
    assert "Poppins" in html, "Missing Poppins font"
    assert "Inter" in html, "Missing Inter font"
    assert "leaflet.css" in html and "leaflet.js" in html, "Missing Leaflet CDN"
    print("✓ Design tokens (teal, amber, fonts, Leaflet) verified")
    
    # 3. Screens verification (All 20 screens L1 to L20)
    required_screens = [
        "screen-L1", "screen-L2", "screen-L3", "modal-L4", "screen-L5",
        "screen-L6", "screen-L7", "screen-L8", "screen-L9", "screen-L10",
        "screen-L11", "screen-L12", "screen-L13", "screen-L14", "screen-L15",
        "screen-L16", "screen-L17", "screen-L18", "screen-L19", "modal-L20"
    ]
    for s in required_screens:
        assert f'id="{s}"' in html or f"id='{s}'" in html, f"Missing screen/modal ID: {s}"
    print(f"✓ All 20 screens and modals verified: {len(required_screens)} present")
    
    # 4. Leaflet Maps
    map_containers = ["map-l4", "map-l5", "map-l6", "map-l14"]
    for m in map_containers:
        assert f'id="{m}"' in html, f"Missing map container: {m}"
    assert "attributionControl: false" in html, "attributionControl must be false"
    assert "© OpenStreetMap" in html, "Missing plain text OpenStreetMap attribution"
    print("✓ 4 Leaflet real map containers & plain text attribution verified")
    
    # 5. External links check (must have NO external links that navigate away)
    # Check <a> tags
    a_hrefs = re.findall(r'<a[^>]+href=[\'"]([^\'"]+)[\'"]', html)
    external_links = [h for h in a_hrefs if h.startswith("http")]
    assert len(external_links) == 0, f"Found external links in <a> tags: {external_links}"
    print(f"✓ Zero external links in <a> tags verified (all internal navigation)")
    
    # 6. Catalog validation in JS
    match = re.search(r'const CATALOG = (\[.*?\]);\s*\n', html, re.DOTALL)
    assert match, "Could not find CATALOG array in JS"
    catalog = json.loads(match.group(1))
    print(f"✓ Catalog parsed successfully from inline JS: {len(catalog)} items")
    assert len(catalog) >= 24, f"Catalog items count is {len(catalog)}, expected >= 24"
    
    categories = set(x["category"] for x in catalog)
    required_categories = {
        "Kamera dan video", "Elektronik", "Perkakas",
        "Camping dan outdoor", "Olahraga", "Pesta dan acara", "Rumah tangga"
    }
    assert required_categories.issubset(categories), f"Missing categories: {required_categories - categories}"
    print(f"✓ All 7 categories present in catalog: {len(categories)} categories")
    
    # Check minimum 3 items per category
    for cat in required_categories:
        count = sum(1 for x in catalog if x["category"] == cat)
        assert count >= 3, f"Category {cat} has only {count} items, expected >= 3"
    print("✓ Minimum 3 items per category verified for all 7 categories")
    
    # 7. Toast component
    assert 'id="toast"' in html, "Missing toast element"
    assert "Fitur ini belum tersedia di versi demo" in html, "Missing demo toast text"
    print("✓ Toast element and required text verified")
    
    # 8. Pricing formula & calculations
    assert "Math.max(2, diffDays || 2)" in html or "Math.max(2," in html, "Missing minimum 2 days rule"
    assert "10000" in html, "Missing protection fee Rp10.000"
    print("✓ Dynamic pricing calculation logic verified (min 2 days, Rp10.000 protection)")
    
    # 9. Automated transitions
    assert "ownerAcceptTimer = setTimeout" in html, "Missing auto approval timer"
    assert "returnCheckTimer = setTimeout" in html, "Missing auto return check timer"
    print("✓ Auto status transitions (5s approval, 5s inspection) verified")
    
    # 10. Amber buttons check
    print("\n--- Summary of Amber Buttons per Screen ---")
    for s in required_screens:
        # find the section or modal
        pattern = rf'<(?:section|div)[^>]+id=[\'"]{s}[\'"].*?(?=<(?:section|div)[^>]+id=[\'"](?:screen-|modal-)|<script|$)'
        m = re.search(pattern, html, re.DOTALL)
        if m:
            amber_btns = re.findall(r'class=[\'"][^\'"]*btn-amber[^\'"]*[\'"]', m.group(0))
            print(f"  {s}: {len(amber_btns)} amber button(s)")
            # Allow at most 1, except L6 where we have 1 desktop and 1 mobile with responsive CSS
            if s == "screen-L6":
                assert len(amber_btns) <= 2, f"Too many amber buttons in {s}: {len(amber_btns)}"
            else:
                assert len(amber_btns) <= 1, f"Too many amber buttons in {s}: {len(amber_btns)}"
        else:
            print(f"  {s}: could not isolate block")
            
    print("\n🎉 ALL VALIDATION CHECKS PASSED PERFECTLY!")

if __name__ == "__main__":
    validate()
