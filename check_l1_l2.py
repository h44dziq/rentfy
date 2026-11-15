with open('c:/Users/hadziq/Documents/Rentfyy/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

s_l1 = text.find('id="screen-L1"')
s_l2 = text.find('id="screen-L2"')
s_l3 = text.find('id="screen-L3"')

print('L1 snippet:\n', text[s_l1-30:s_l1+300])
print('---')
print('L2 snippet:\n', text[s_l2-30:s_l2+300])
