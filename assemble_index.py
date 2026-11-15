# -*- coding: utf-8 -*-
"""
Assembles the complete index.html for Rentfy prototype
"""

import json
import catalog_data
import screens_part1
import screens_part2
import screens_part3
import screens_part4
import app_script

def assemble():
    print("Starting assembly of index.html...")
    
    # 1. Read head from build_index_full.py
    with open('build_index_full.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    start_idx = None
    end_idx = None
    for i, line in enumerate(lines):
        if '<!DOCTYPE html>' in line:
            start_idx = i
        if '<body>' in line:
            end_idx = i
            
    if start_idx is None or end_idx is None:
        raise ValueError("Could not find DOCTYPE or <body> in build_index_full.py")
        
    head_lines = lines[start_idx:end_idx+1]
    if "f.write('''" in head_lines[0]:
        head_lines[0] = head_lines[0].split("f.write('''")[1]
    head_html = ''.join(head_lines)
    
    # 2. Gather all screen HTML
    body_parts = [
        screens_part1.get_l1_screen(),
        screens_part1.get_l2_screen(),
        screens_part1.get_l3_screen(),
        screens_part1.get_l4_modal(),
        screens_part1.get_l5_screen(),
        screens_part2.get_l6_screen(),
        screens_part2.get_l7_screen(),
        screens_part2.get_l8_screen(),
        screens_part2.get_l9_screen(),
        screens_part2.get_l10_screen(),
        screens_part3.get_l11_screen(),
        screens_part3.get_l12_screen(),
        screens_part3.get_l13_screen(),
        screens_part3.get_l14_screen(),
        screens_part3.get_l15_screen(),
        screens_part4.get_l16_screen(),
        screens_part4.get_l17_screen(),
        screens_part4.get_l18_screen(),
        screens_part4.get_l19_screen(),
        screens_part4.get_l20_modal(),
        screens_part4.get_common_modals_and_footer()
    ]
    
    # 3. Prepare scripts and catalog
    catalog = catalog_data.build()
    catalog_json = json.dumps(catalog, ensure_ascii=False)
    
    script_content = app_script.get_script_content().replace('__CATALOG_JSON_PLACEHOLDER__', catalog_json)
    
    # 4. Write full index.html
    output_path = "index.html"
    with open(output_path, "w", encoding="utf-8") as out:
        out.write(head_html)
        out.write("\n")
        for part in body_parts:
            out.write(part)
            out.write("\n")
        out.write(script_content)
        out.write("\n")
        
    print(f"index.html successfully assembled at {output_path}!")

if __name__ == "__main__":
    assemble()
