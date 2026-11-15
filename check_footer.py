import re

with open('c:/Users/hadziq/Documents/Rentfyy/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'<template id="common-footer-template">(.*?)</template>', content, re.DOTALL)
if m:
    print("Footer template length:", len(m.group(1)))
    print("Footer preview:", m.group(1)[:200])
else:
    print("Footer template not found")
