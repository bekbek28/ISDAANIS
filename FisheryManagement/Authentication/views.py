from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h1>my first app</h1>')

def login(request):
   return render(request, 'index.html')

def isreghtml(request):
   return render(request, 'register.html')

def ispmloginhtml(request):
   return render(request, 'PManager.html')

def ispmreghtml(request):
   return render(request, 'PMregister.html')