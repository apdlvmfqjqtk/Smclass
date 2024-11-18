from django.shortcuts import render

def board(request):
  return render(request, 'list.html')
