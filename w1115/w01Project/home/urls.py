from django.urls import path,include
from . import views

app_name = ''  # App 이름: 앱 이름으로 접근할 때 사용 (아직은 url로 접근중)
urlpatterns = [
  # views.py 연결 - 함수호출, app함수이름
  path('',views.index, name='index')
]