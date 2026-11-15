import re

with open('c:/Users/hadziq/Documents/Rentfyy/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'function getCommonNavHtml\(\)\s*\{(.*?return `)(.*?)(`;\s*\})', content, re.DOTALL)
if m:
    nav_html = m.group(2)
    print("Nav HTML length:", len(nav_html))
    print("Nav HTML preview:\n", nav_html[:300])
else:
    print("Nav HTML not found")
