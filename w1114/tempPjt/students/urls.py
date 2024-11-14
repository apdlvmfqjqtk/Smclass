
from django.urls import path, include
from . import views

app_name = 'students'
# url 로 찾는 방법, 이름으로 찾는 방법 두 가지가 있음
urlpatterns = [
    ### url 주소 / views.py 함수명, url이름
    ## http://127.0.0.1:8000/students/reg/
    # students:reg
    path('reg/',views.regStudent,name='reg'),
    
]
