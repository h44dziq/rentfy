with open('c:/Users/hadziq/Documents/Rentfyy/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

screens_to_check = ['screen-L7', 'screen-L8', 'screen-L11', 'screen-L12', 'screen-L13', 'screen-L14', 'screen-L15', 'screen-L16', 'screen-L17']
for s in screens_to_check:
    idx = text.find(f'id="{s}"')
    print(f"=== {s} ===")
    print(text[idx:idx+200].replace('\n', ' '))
