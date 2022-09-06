from django.shortcuts import render

def index(request):
    return render(request, 'abiko_app/index.html')
