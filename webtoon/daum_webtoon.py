import requests
import time


def artist_name(artists):
    return artists[0].get('name') + "/" + artists[1].get('name')

def daum_webtoon_day(day):
    json_object = requests.get("http://webtoon.daum.net/data/pc/webtoon/list_serialized/" + day
                               + "?timeStamp=" + str(time.time())).json()
    webtoon_list = json_object.get('data')
    for webtoon in webtoon_list:
        print(webtoon.get('title'))
        print(artist_name(webtoon.get('cartoon').get('artists')))
        print(webtoon.get('thumbnailImage2').get('url'))

def daum_webtoon():
    week_list = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    for day in week_list:
        daum_webtoon_day(day)

daum_webtoon()
