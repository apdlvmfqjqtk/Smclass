from django.urls import path,include
from . import views

urlpatterns = [
    path('input/', views.memberinput, name='minput'),
]
