from django.urls import path
from .views import *

urlpatterns = [
    path('naver_crw', naver_webtoon_crw)
]