from django.http import HttpResponse
from django.shortcuts import render

def index(requrest):
    return HttpResponse('<h1>Hello Matsuo App</h1>')
