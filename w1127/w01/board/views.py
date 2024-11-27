from django.shortcuts import render

def write(request):
  return render(request, 'write.html')

# 게시글 리스트
def list(request):
  return render(request, 'list.html')