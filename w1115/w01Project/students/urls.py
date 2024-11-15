from django.urls import path,include
from . import views

app_name = 'students'  # App 이름: 앱 이름으로 접근할 때 사용 (아직은 url로 접근중)
urlpatterns = [
  # views.py 연결 - 함수호출, app함수이름
  path('write/',views.write, name='write'),
  path('save/',views.save, name='save'),
  path('list/',views.list, name='list'),
]