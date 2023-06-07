from django.shortcuts import render
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User



# Create your views here.
@login_required(login_url='login/')

def usertype(request):
   return render(request, 'usertype.html')

def index(request):
   return HttpResponse('<h1>my first app</h1>')


def islogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('forms/')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'index.html')

def isreghtml(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        uname = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            try:
                my_user = User.objects.create_user(uname, password)
                my_user.save()
                return redirect('login')
            except IntegrityError:
                return HttpResponse("Username or email already exists!")

    return render(request, 'register.html')
        
        
def ispmloginhtml(request):
   if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard/')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

   
   return render(request, 'PManager.html')

def ispmreghtml(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        uname = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            try:
                my_user = User.objects.create_user(uname, password)
                my_user.save()
                return redirect('login')
            except IntegrityError:
                return HttpResponse("Username or email already exists!")

    return render(request, 'PMregister.html')
