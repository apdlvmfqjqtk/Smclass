from django.shortcuts import render,redirect
from students.models import Student
from django.urls import reverse

# 학생검색
def search(request):
  search = request.GET.get('search')
  print('검색 단어 : ', search)
  ## 데이터 검색
  qs = Student.objects.filter(name__contains=search)
  context = {"slist":qs}
  return render(request, 'list.html', context)

# 학생정보삭제
def delete(request,name):
  print("삭제정보 이름 :",name)
  Student.objects.get(name=name).delete()
  return redirect('/students/list')



# 1학생수정페이지, 2. 학생수정저장
def update(request):
  if request.method == 'GET':
    name = request.GET['name']
    print(name)
    qs = Student.objects.get(name=name)
    context = {'stu':qs}
    return render(request, 'update.html', context)
  else:
    name = request.POST.get('name')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    hobby = request.POST.getlist('hobby')

    # student 검색
    qs = Student.objects.get(name=name)
    qs.major = major
    qs.grade = grade
    qs.age = age
    qs.gender = gender
    qs.hobby = hobby
    qs.save()

    return redirect('students:view', name) ## 약식
    # return redirect(reverse('students:view',args=(name,))) # 정규표현식 
    pass



##  학생상세보기
def view(request, name):
  qs = Student.objects.get(name=name)
  context = {'stu':qs}
  return render(request, 'view.html', context)
  # html -> view : form, 파라미터, url app_name
  # view -> html : context, ajax 


# 학생리스트
def list(request):
  # 학생 전체정보 가져오기
  # qs = Student.objects.all()
  qs = Student.objects.order_by('-grade', 'name')  # 순차정렬. -붙이면 역순정렬, 2개 사용 가능함
  context = {"slist":qs,}
  return render(request, 'list.html', context)


# http 2가지 객체 (웹 공통, 데이터가 실리는 부분) : requset, response
# 1. 학생입력페이지 열기, 2. 학생정보저장
def write(request):
  if request.method == "POST":
    # 받는 방식에도 두가지가 있다.
    name = request.POST.get('name') # 데이터가 없을때 None  데이타 넘겨줌
    major = request.POST['major']   # 데이터가 없을때 error 데이타 넘겨줌
    grade = request.POST['grade']    
    age = request.POST['age']     
    gender = request.POST['gender']      
    # hobby = request.POST['hobby']      
    hobbys = request.POST.getlist('hobby')  # checkbox 있는 데이터 들고오기(복수데이터)
    # hobby = ','.join(hobbys)       # list -> str 타입으로 변경
    # hobby_list = hobby.split(",")  # str -> list 타입으로 변경

    print(name)
    # print("hobby : ",hobby)
    print("hobbys 복수 : ", hobbys)

    ## qs.save() 방법
    qs = Student(name=name, major=major, grade=grade, age=age, gender=gender, hobby=hobbys)
    qs.save()

    # ## create() : save()필요 없음
    # Student.objects.create(name=name, major=major, grade=grade, age=age, gender=gender, hobby=hobbys)

    return redirect('/students/list/')

  else: # GET 호출
    return render(request, 'write.html')
    # render : 웹 페이지를 열 때
    # redirect : url링크를 열 때
    # templates 폴더에서 html 파일을 검색함
