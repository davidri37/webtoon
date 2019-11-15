from django.urls import path
from .views import *

urlpatterns = [
    path('', WebtoonList.as_view(), name='list'),
    path('detail/<str:pk>', WebtoonDetailView.as_view(), name='detail'),
    path('comment/<str:pk>', addComment, name='comment'),
    path('daum/', DaumWebtoonList.as_view(), name='daum'),
    path('naver_crw', naver_webtoon_crw),
    path('daum_crw', daum_webtoon_crw)
]