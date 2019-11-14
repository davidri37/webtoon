import requests
import bs4
from .models import WebToon

def naver_webtoon_day(day):
    html = requests.get("https://comic.naver.com/webtoon/weekdayList.nhn?week=" + day)
    # print(html.status_code)
    # print(html.text)

    bs_object = bs4.BeautifulSoup(html.text, "html.parser")
    # print(bs_object)
    webtoon_list = bs_object.find('div', {'class': 'list_area daily_img'})
    # print(webtoon_list)
    webtoon_list_tags = webtoon_list.findAll('li')
    # print(webtoon_list_tags)

    for webtoon_tag in webtoon_list_tags:
        webtoon = WebToon()
        webtoon.site_name = "네이버"
        webtoon.webtoon_name = webtoon_tag.find('a')['title']
        webtoon.webtoon_author = webtoon_tag.find('dd', {'class': 'desc'}).text.strip()
        webtoon.webtoon_img_url = webtoon_tag.find('img')['src']
        webtoon.webtoon_id = "네이버_" + webtoon_tag.find('a')['title']

        webtoon.save()

        # print(webtoon_tag.find('a')['title'])
        # print(webtoon_tag.find('a').find('img')['src'])
        # print(webtoon_tag.find('dd', {'class': 'desc'}).text.strip())

def naver_webtoon():
    week_list = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    for week in week_list:
        naver_webtoon_day(week)
