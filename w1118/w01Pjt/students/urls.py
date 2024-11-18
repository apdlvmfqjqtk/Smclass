from django.urls import path, include
from . import views

# 학생삭제


app_name = 'students'   ## name:url연결 시 사용
urlpatterns = [
    path('list/',views.list, name='list'),  # 학생 리스트

    path('write/',views.write, name='write'),  # 학생입력페이지

    path('<str:name>/sview/',views.view, name='view'),  # 학생 상세 페이지 정수라면 이런식으로 받기<int:no>

    ## 수정 1,2,3,
    path('<str:name>/modify/',views.modify, name='modify'),
    path('/modify2/', views.modify2, name='modify2'),
    path('<str:name>/modify3/', views.modify3, name='modify3'), # 학생수정3

    path('<str:name>/delete/', views.delete, name='delete'), # 학생삭제

    # path('doWrite/',views.doWrite, name='doWrite'),  # 학생입력페이지
]
