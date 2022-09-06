from django.shortcuts import render

def index(request):
  return render(request, 'hl_app/index.html')
