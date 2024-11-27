from django.shortcuts import render
from member.models import Member

# 로그아웃 처리
def logout(request):
  request.session.clear()  # 설정해 둔 모든 세션 삭제 처리(session_id, session_nicName)
  context = {"lgot":"1"}   # 로그아웃 확인 메시지 변수
  return render(request, 'index.html', context) # 담아서 index로 전송


# 로그인 페이지(GET), 로그인 확인 처리(POST)
def login(request):
  # url클릭
  if request.method == 'GET':
    return render(request, 'login.html')
  else:
  # form으로 받는다면
    # id와 pw정보 가져오기
    id = request.POST.get('uid')
    pw = request.POST.get('upw')
    print(id, pw)
    # Member model에서 id와 pw 꺼내서 대조하기
    qs = Member.objects.filter(id=id, pw=pw)

    # 일치하는 정보가 있다면
    if qs:
      # 세션에 session_id라는 이름으로 id담기
      # 세션에 session_nicName 이라는 이름으로 nicName담기
      # 추후 여러 적용 위한 세션값 설정
      request.session['session_id'] = id
      request.session['session_nicName'] = qs[0].nicName

      # context에 lmsg(로그인 확인 메시지 변수 이름) 참 변수 대입
      context = {'lgin':'1'}
      # 위 정보들을 login.html에 다시 보내줌
      return render(request, 'login.html', context)
    # 일치하는 정보다 없다면
    else:
      # context에 lmsg 실패 넣음
      context = {'lgin':'0'}
      return render(request, 'login.html', context)
      # 위 정보들을 login.html에 다시 보내줌