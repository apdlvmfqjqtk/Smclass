from django.urls import path, include
from . import views

app_name = 'board'   ## name:url연결 시 사용
urlpatterns = [
    path('list/',views.board, name='list'),  # 학생입력페이지
    ]
