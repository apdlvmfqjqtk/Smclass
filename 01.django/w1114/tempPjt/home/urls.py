
from django.urls import path, include
from . import views

app_name = ''
# url 로 찾는 방법, 이름으로 찾는 방법 두 가지가 있음
urlpatterns = [
    path('',views.index,name='index'),
    
]
