with open('c:/Users/hadziq/Documents/Rentfyy/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

s_l5 = text.find('id="screen-L5"')
print(text[s_l5:s_l5+1000])
