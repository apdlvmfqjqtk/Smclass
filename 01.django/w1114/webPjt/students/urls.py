from django.urls import path,include
from . import views  # . : 현재 폴더, 현재 폴더에서 view 찾아 임포트해줘

# # # 메인 URL # # #
app_name = 'students'
urlpatterns = [
    path('write/', views.write, name='write'),
]
