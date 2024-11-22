from django.urls import path,include
from . import views

app_name = "board"
urlpatterns = [
    path('breply/<int:bno>/', views.breply, name='breply'),  # 글 삭제하기
    path('bdelete/<int:bno>/', views.bdelete, name='bdelete'),  # 글 삭제하기
    path('bmodify/<int:bno>/', views.bmodify, name='bmodify'),  # 글 수정하기
    path('bview/<int:bno>/', views.bview, name='bview'),  # 글 상세보기
    path('bwrite/', views.bwrite, name='bwrite'),         # 글 쓰기
    path('blist/', views.blist, name='blist'),            # 게시판 리스트
]
