from django.urls import path,include
from . import views

app_name = "students"
urlpatterns = [
    path('write/', views.write,name='write'),
    path('list/', views.list,name='list'),
    path('view/', views.view,name='view'),
    path('update/', views.update,name='update'),
]
