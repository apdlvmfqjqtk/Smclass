from django.urls import path,include   #  includ 추가
from . import views

app_name = 'students'  # app_name을 설정 (url를 이용한 접속이 아닌 appname을 이용한 접속 이용)
urlpatterns = [
  # 'DEF/', view.qwer ,name='asdf
  # Pjt>setting과 같이 student/로 들어왔을 때 그 뒤에 오는 주소에 따라 뒤 함수를 실행
  # name을 지은 이유는 app_name처럼 이름으로 실행시키기 위함
  # url링크, views함수호출, name링크
    path('write/',views.write,name='write'), # 위탁시키기 students.urls연결
    path('search/',views.search,name='search'),
    path('list/',views.list,name='list'), # 위탁시키기 students.urls연결
    path('<str:name>/view/', views.view, name='view'),
    # path('view/<str:name>/', views.view, name='view'), # 이렇게 써도 상관은 없다.
    path('update/', views.update, name='update'),  # 파라미터 형태
    path('delete/<str:name>/', views.delete, name='delete'),
    # path('update/<str:name>/', views.update, name='update'),
]
