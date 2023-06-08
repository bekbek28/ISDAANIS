from django.shortcuts import render
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test



# Create your views here.
@login_required(login_url='login/')

def usertype(request):
   return render(request, 'usertype.html')

def index(request):
   return HttpResponse('<h1>my first app</h1>')

# Custom decorator to check if the user is a Port Manager
def port_manager_required(view_func):
    def check_port_manager(user):
        return user.is_authenticated and user.groups.filter(name='Port Manager').exists()
    return user_passes_test(check_port_manager)(view_func)

@port_manager_required
def port_manager_view(request):
    # Only accessible by users with the 'Port Manager' role
    return HttpResponse("Port Manager view")

# Custom decorator to check if the user is a Market Checker
def market_checker_required(view_func):
    def check_market_checker(user):
        return user.is_authenticated and user.groups.filter(name='Market Checker').exists()
    return user_passes_test(check_market_checker)(view_func)

@market_checker_required
def market_checker_view(request):
    # Only accessible by users with the 'Market Checker' role
    return HttpResponse("Market Checker view")


def islogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Analytics:forms')
        else:
            return HttpResponse("Username or Password is incorrecsdsdt!!!")

    return render(request, 'index.html')

def isreghtml(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            try:
                my_user = User.objects.create_user(uname, password)
                my_user.save()
                return redirect('Authentication:login')
            except IntegrityError:
                return HttpResponse("Username or email already exists!")

    return render(request, 'register.html')
        
        
def ispmloginhtml(request):
   if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('Analytics:dashboard')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

   
   return render(request, 'PManager.html')

def ispmreghtml(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            try:
                my_user = User.objects.create_user(uname, password)
                my_user.save()
                return redirect('Authentication:pmlogin')
            except IntegrityError:
                return HttpResponse("Username or email already exists!")

    return render(request, 'PMregister.html')
