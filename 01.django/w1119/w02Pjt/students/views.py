from django.shortcuts import render

# 1. 학생 입력 페이지 열기, 2. 학생 정보 저장하기
def write(request):
  if request.method == "GET":
    # url로 write에 접근 시 작성 페이지를 띄워 줌
    return render(request, 'write.html')
  else:
    # post로 데이터 접근 시 작성된 정보 저장
    name = request.POST.get('name')
    name = request.POST.get('name')

def list(request):
  return render(request, 'list.html')

def view(request):
  return render(request, 'view.html')

def update(request):
  return render(request, 'update.html')
