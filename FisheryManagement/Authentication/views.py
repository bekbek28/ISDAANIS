from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group

# Create your views here.
# Create the 'Market Checker' group if it doesn't exist
market_checker_group, created = Group.objects.get_or_create(name='Market Checker')
port_manager_group, created = Group.objects.get_or_create(name='Port Manager')

def redirect_based_on_role(user):
    # Check if the user belongs to the 'Port Manager' group
    if user.groups.filter(name='Authentication:pmregister').exists():
        return redirect('Analytics:dashboard')  # Redirect to Port Manager dashboard

    # Check if the user belongs to the 'Market Checker' group
    elif user.groups.filter(name='Authentication:register').exists():
        return redirect('Analytics:forms')  # Redirect to Market Checker dashboard

    else:
        return HttpResponse("Invalid user role!")  # User has an unrecognized role

@login_required(login_url='/login/')
def usertype(request):
    return render(request, 'usertype.html')

def index(request):
    return HttpResponse('<h1>My first app</h1>')

@user_passes_test(lambda user: user.groups.filter(name='Market Checker').exists(), login_url='login/')
def islogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect_based_on_role(user)    # Update this with the correct URL
        else:
            return HttpResponse("Username or password is incorrect!")

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
            return HttpResponse("Your password and confirm password do not match!")
        else:
            try:
                my_user = User.objects.create_user(username=uname, password=password)
                my_user.save()

                # Assign the user to the 'Market Checker' group
                market_checker_group = Group.objects.get(name='Market Checker')
                market_checker_group.user_set.add(my_user)

                return redirect('Authentication:login')
            except IntegrityError:
                return HttpResponse("Username or email already exists!")

    return render(request, 'register.html')

@user_passes_test(lambda user: user.groups.filter(name='Port Manager').exists(), login_url='/pmlogin/')
def ispmloginhtml(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect_based_on_role(user)   # Update this with the correct URL
        else:
            return HttpResponse("Username or password is incorrect!")

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
            return HttpResponse("Your password and confirm password do not match!")
        else:
            try:
                my_user = User.objects.create_user(username=uname, password=password)
                my_user.save()

                # Assign the user to the 'Port Manager' group
                port_manager_group = Group.objects.get(name='Port Manager')
                port_manager_group.user_set.add(my_user)

                return redirect('Authentication:pmlogin')  # Update this with the correct URL
            except IntegrityError:
                return HttpResponse("Username or email already exists!")

    return render(request, 'PMregister.html')

@user_passes_test(lambda user: user.is_superuser, login_url='/login/')
def isadminloginhtml(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('Analytics:admindashboard')  # Update this with the correct URL
        else:
            return HttpResponse("Username or password is incorrect!")

    return render(request, 'admin.html')

@user_passes_test(lambda user: user.is_superuser, login_url='/login/')
def isadminreghtml(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return HttpResponse("Your password and confirm password do not match!")
        else:
            try:
                my_user = User.objects.create_user(username=uname, password=password)
                my_user.save()
                return redirect('Authentication:loginadmin')  # Update this with the correct URL
            except IntegrityError:
                return HttpResponse("Username or email already exists!")

    return render(request, 'adminreg.html')
