from django.contrib import admin
from django.urls import path,include   #  includ 추가

urlpatterns = [
  # 'ABC',asdf : ABC/주소로 들어오면 asdf로 보내줘
    path('admin/', admin.site.urls),  # admin 관리자 사이트 연결
    path('students/', include('students.urls')), # 위탁시키기 students.urls연결
    path('', include('home.urls')), # home > urls.py연결
]
