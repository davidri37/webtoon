import requests
import bs4

html = requests.get("https://comic.naver.com/webtoon/weekdayList.nhn?week=thu")
# print(html.status_code)
# print(html.text)

bs_object = bs4.BeautifulSoup(html.text, "html.parser")
# print(bs_object)
webtoon_list = bs_object.find('div', {'class': 'list_area daily_img'})
# print(webtoon_list)
webtoon_list_tags = webtoon_list.findAll('li')
# print(webtoon_list_tags)

for webtoon_tag in webtoon_list_tags:
    print(webtoon_tag.find('a')['title'])
