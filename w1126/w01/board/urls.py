from django.urls import path, include
from . import views

app_name = 'member'
urlpatterns = [
    path('blist/', views.blist, name='blist'),
    path('bwrite/', views.bwrite, name='bwrite'),
    path('bview/<int:bno>/', views.bview, name='bview'),
    path('bdelete/<int:bno>/', views.bdelete, name='bdelete'), # 글삭제
    path('bupdate/<int:bno>/', views.bupdate, name='bupdate'), # 글수정
    path('breply/<int:bno>/', views.breply, name='breply'), # 답글 쓰기
]
