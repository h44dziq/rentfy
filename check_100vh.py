import re

with open('c:/Users/hadziq/Documents/Rentfyy/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = [(m.start(), m.group(0)) for m in re.finditer(r'min-height:\s*100vh', text)]
print(f"Total min-height: 100vh found: {len(matches)}")

for pos, match in matches:
    start = max(0, pos - 60)
    end = min(len(text), pos + 60)
    snippet = text[start:end].replace('\n', ' ')
    print("Snippet:", snippet)
