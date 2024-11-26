from django.urls import path,include   #  includ 추가
from . import views

app_name = ''
urlpatterns = [
    path('', views.index, name='index'), # home > urls.py연결
]
