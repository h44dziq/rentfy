import re

with open('c:/Users/hadziq/Documents/Rentfyy/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's inspect getCommonNavHtml, getCommonFooterHtml, getCommonMobileTabsHtml
print("Checking common templates...")
has_nav_func = "function getCommonNavHtml()" in content
has_footer_func = "function getCommonFooterHtml()" in content
has_tabs_func = "function getCommonMobileTabsHtml(" in content

print(f"Nav func: {has_nav_func}, Footer func: {has_footer_func}, Tabs func: {has_tabs_func}")
