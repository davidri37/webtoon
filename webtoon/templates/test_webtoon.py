import requests

json_object = requests.get('https://www.lezhin.com/api/v2/inventory_groups/home_scheduled_k?platform=web&store=web&_=1573792735471').json()
webtoon_list = json_object.get('data').get('inventoryList')
for webtoon in webtoon_list:
    for w in webtoon.get('items'):
        print(w.get('title'))