with open('c:/Users/hadziq/Documents/Rentfyy/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

s_l6 = text.find('id="screen-L6"')
print(text[s_l6:s_l6+1000])
