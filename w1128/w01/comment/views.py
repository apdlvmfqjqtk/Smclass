from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from member.models import Member
from board.models import Board
from comment.models import Comment


# 하단 댓글쓰기 저장
def cwrite(request):
  # 데이터 가져오기
  id = request.session['session_id']
  member = Member.objects.get(id=id)
  bno = request.POST.get("bno",1)
  board = Board.objects.get(bno=bno)
  cpw = request.POST.get("pw","")
  ccontent = request.POST.get("ccontent","")
  print(cpw, ccontent)
  # 데이터 저장
  qs = Comment.objects.create(board=board, member=member, cpw=cpw, ccontent=ccontent)
  json_qs = serializers.serialize("json",[qs])
  context = {"comment":json_qs, "result":"success"}
  return JsonResponse(context)

# 하단 댓글 리스트
def clist(request):
  return