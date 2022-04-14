import requests
page = requests.get('https://utas.s2.fut.ea.com/ut/game/fifa16/transfermarket?maxb=900&start=0&type=player&maskedDefId=177604&num=16', headers=headers, cookies=cookies)
# print page.json

page_dict = page.json()
print(page_dict['tradeId'])