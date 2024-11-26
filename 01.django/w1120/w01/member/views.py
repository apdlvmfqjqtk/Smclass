from django.shortcuts import render
from member.models import Member

# 회원권 관리
def m2(request):
  if request.method == 'GET':
    pass
  else : 
    memberId   = request.COOKIES.get('memberId')
    money      = request.COOKIES.get('money')
    option     = request.COOKIES.get('option')
    saveMember = request.COOKIES.get('saveMember')
    print(memberId, money, option, saveMember)
    response = render(request, 'm2.html')
    if saveMember != None:
      response.set_cookie('m_i', memberId)
      response.set_cookie('m_m', money)
      response.set_cookie('m_o', option)
  




# 상품번호, 상품명 저장 (pId, pName)
def product(request):
  if request.method == 'GET':
    # 쿠키 읽어오기
    c_pId = request.COOKIES.get('c_pId','')
    c_pName = request.COOKIES.get('c_pName','')
    context = {'c_pId':c_pId, 'c_pName':c_pName}
    print(context)
    return render(request, 'product.html', context)
  else:
    # 쿠키 저장
    pId     = request.POST.get('pId')
    pName   = request.POST.get('pName')
    pOption = request.POST.get('pOption')
    saveProduct = request.POST.get('saveProduct')
    print(pId, pName, pOption,saveProduct)
    response = render(request, 'product.html')
    if saveProduct is not None:
       # 체크가 되어 있으면.
      response.set_cookie('c_pId', pId, max_age=60*60)
      response.set_cookie('c_pName', pName, max_age=60*60)
    else:
      response.delete_cookie('c_pId', pId)
      response.delete_cookie('c_pName', pName)
    return response

# 로그인 2복습
def login2(request):
  if request.method == 'GET':
    cookId = request.COOKIES.get('cookId','')  # cookId가 없다면 빈공백('')을 보낸다.
    print('cookid : ',cookId)
    context = {'cookId':cookId}
    return render(request, 'login2.html', context)
  else:
    response = render(request, 'index.html')
    # 3개의 정보
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    saveId = request.POST.get('saveId')
    if saveId is not None:
      response.set_cookie('cookId', id, max_age=60*60)
    else:
      response.delete_cookie('cookId')

    return response



# 로그인
## 쿠키 정보 검색 request.COOKIES.get('이름')
## 쿠키 저장  response.set_cookie('key','value')
## 쿠키 삭제 response.delete_cookie('key)
def login(request):

  if request.method == 'GET':
    print("쿠키정보 : ", request.COOKIES)
    print("cookinfo 쿠키정보 : ", request.COOKIES.get('cookinfo'))
    saveId = request.COOKIES.get('saveId','')
    print('saveId : ', saveId)
    context = {'saveId':saveId}
    response = render(request, 'login.html', context)
    # 쿠키 설정(저장)
    # max_age=60*60가 없으면 브라우저 종료시 삭제, max_age=60*60 60초 60분 삭제 1달=> 60초*60분*24시간*30일
    ## cookie 정보 검색
    if request.COOKIES.get('cookinfo'):
      response.set_cookie('cookinfo','1111',max_age=60*60)
    return response

  else:
    print('쿠키정보 : ', request.COOKIES)
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    saveId = request.POST.get("saveId")
    print('전달받은 정보 : ', id, pw, saveId)
    response = render(request, 'login.html')
    ## 아이디 기억하기 정보가 있으면
    if saveId is not None :
      response.set_cookie('saveId', id, max_age=60*60) # 아이디 기억하기 체크가 있으면 쿠키 저장
    else:
      response.delete_cookie('saveId')  # 아이디 기억하기 체크가 없으면 쿠키 삭제

    return response



# 회원 전체 리스트 페이지
def mlist(request):
  qs = Member.objects.all()
  context = {"mlist":qs}
  return render(request, 'mlist.html', context) # context변수 안만들어도 되지만 훗날을 위해,,
