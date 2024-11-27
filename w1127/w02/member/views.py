from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from member.models import Member

# ajax 통신
# csrf_token
@csrf_exempt # csrf_token 예외 처리 
def loginChk(request):
  id = request.POST.get("id","")
  pw = request.POST.get("pw","")
  print("html에서 넘어온 데이터 : ", id, pw)

  # #  get 검색 객체 보내는 방법  (걍 안넘어감)
  # qs = Member.objects.get(id=id, pw=pw)  #.vlaues()
  # if qs:
  #   context = {"member":qs, "result":"success"}
  # else:
  #   context = {"result":'fail'}
  # return JsonResponse(context)


  #  filter 검색 객체 보내는 방법 -list로 넘겨야함 (안그러면 에러남)
  qs = list(Member.objects.filter(id=id, pw=pw).values())
  if qs:
    context = {"member":qs, "result":"success"}
  else:
    context = {"result":'fail'}
  return JsonResponse(context)


  # #  변수 보내는 방법
  # if qs:
  #   context = {"id":qs[0].id, "nicName":qs[0].nicName, "result":"success"}
  # else:
  #   context = {"result":'fail'}
  # return JsonResponse(context)


# 로그인페이지
def login(request):
  return render(request, 'login.html')