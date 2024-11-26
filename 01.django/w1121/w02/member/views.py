from django.shortcuts import render,redirect
from member.models import Member

# 회원가입:
def join01(request):
  return render(request, 'join01.html')
def join02(request):
  return render(request, 'join02.html')
def join03(request):
  return render(request, 'join03.html')



# 로그아웃
def logout(request):
  request.session.clear()
  return redirect("/")

# 로그인 페이지, 로그인 확인
def login(request):
  if request.method == "GET":
    return render(request, 'login.html')
  else:
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    qs = Member.objects.filter(id=id, pw=pw)
    if qs:
      msg = "1"  # 로그인 성공
      request.session['session_id'] = id
      request.session['session_name'] = qs[0].name
      # return redirect('index')
    else:
      msg = "0"  # 로그인 실패

    return render(request, 'login.html',{"msg":msg})
