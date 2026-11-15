import re

with open('c:/Users/hadziq/Documents/Rentfyy/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect getCommonNavHtml
m_nav = re.search(r'function getCommonNavHtml\(\)\s*\{.*?return `(.*?)`;\s*\}', text, re.DOTALL)
if m_nav:
    nav_html = m_nav.group(1).strip()
    print("Found nav_html length:", len(nav_html))
else:
    print("Nav html not found!")

# Let's inspect footer template
m_footer = re.search(r'<template id="common-footer-template">\s*(<footer class="footer">.*?</footer>)\s*</template>', text, re.DOTALL)
if m_footer:
    footer_html = m_footer.group(1).strip()
    print("Found footer_html length:", len(footer_html))
else:
    print("Footer html not found!")
