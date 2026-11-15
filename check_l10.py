with open('c:/Users/hadziq/Documents/Rentfyy/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

s_l10 = text.find('id="screen-L10"')
print(text[s_l10:s_l10+800])
