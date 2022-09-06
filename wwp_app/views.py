from django.shortcuts import render

def index(request):
  return render(request, "wwp_app/index.html")
