from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from students.models import Student

## 학생 전체리스트 호출
def list(request):
  qs = Student.objects.all()
  # 정보전달 변수생성
  context = {'list':qs}
  return render(request,'stu_list.html',context)


# 리퀘스트 무조건 적기
# 학생입력페이지 호출
def write(request):
# render: 웹페이지를 열어주는 형태
  print('학생등록페이지 호출')
  return render(request, 'stu_write.html')

# 학생입력 저장
def save(request):
  print('학생정보저장 호출')
  # if request.method == 'POST': #post 방식으로 왔는지 체크
  if request.method == 'POST':    #request.POST데이터가 있는지 체크
    print('post')
  else:
    print('GET : ',request.GET)
  
  if request.GET:
    print("get2:",request.GET)
  
  if request.POST:
    print('post2')
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    print(name,major,grade,age,gender)
    qs = Student(s_name=name,s_major=major,s_grade=grade,s_age=age,s_gender=gender)
    qs.save()
  return HttpResponseRedirect(reverse('index'))
  # return redirect('index')
  # redirect('/')
  # return redirect(reverse('index'))