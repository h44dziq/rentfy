import re

with open('c:/Users/hadziq/Documents/Rentfyy/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("File length:", len(text))
modals = re.findall(r'id=["\'](modal-[^"\']+)["\']', text)
print("Modals found:", modals)

screens = re.findall(r'id=["\'](screen-[^"\']+)["\']', text)
print("Screens found:", screens)
