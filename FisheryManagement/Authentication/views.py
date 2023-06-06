from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.

def usertype(request):
   return render(request, 'usertype.html')

def index(request):
   return HttpResponse('<h1>my first app</h1>')


def login(request):
   if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/login/')    
   return render(request, 'index.html')

def isreghtml(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            User.objects.create_user(username=username, password=password)
            return redirect('/login/')  # Replace with the desired URL for login
    
    return render(request, 'register.html')

def ispmloginhtml(request):
   return render(request, 'PManager.html')

def ispmreghtml(request):
   return render(request, 'PMregister.html')
