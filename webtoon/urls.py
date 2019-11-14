from django.urls import path
from .views import *

urlpatterns = [
    path('', WebtoonList.as_view(), name='list'),
    path('daum/', DaumWebtoonList.as_view(), name='daum'),
    path('naver_crw', naver_webtoon_crw),
    path('daum_crw', daum_webtoon_crw)
]