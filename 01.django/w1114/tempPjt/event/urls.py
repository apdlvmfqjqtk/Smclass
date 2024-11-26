from django.urls import path, include
from . import views

appname = 'event'
urlpatterns = [
    path('eventView/',views.eventView,name='eventView'),
]
