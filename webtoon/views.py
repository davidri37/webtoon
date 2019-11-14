from django.shortcuts import render
from django.http import HttpResponse
from .naver_webtoon import *
from .daum_webtoon import *
from django.views.generic import ListView

# Create your views here.
def naver_webtoon_crw(request):
    naver_webtoon()
    return HttpResponse("네이버 웹툰 크롤링 완료")

def daum_webtoon_crw(request):
    daum_webtoon()
    return HttpResponse("다음 웹툰 크롤링 완료")

class WebtoonList(ListView):
    model = WebToon
    paginate_by = 30
    # context_object_name = 'webtoon_list' # object_list 대신에

    def get_queryset(self):
        return WebToon.objects.filter(site_name='네이버')

class DaumWebtoonList(ListView):
    model = WebToon
    paginate_by = 50
        # context_object_name = 'webtoon_list' # object_list 대신에

    def get_queryset(self):
        return WebToon.objects.filter(site_name='다음')