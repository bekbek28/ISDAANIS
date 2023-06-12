from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.db import IntegrityError



# Create the 'Market Checker' group if it doesn't exist
market_checker_group, _ = Group.objects.get_or_create(name='Market Checker')

# Create the 'PManager' group if it doesn't exist
pmanager_group, _ = Group.objects.get_or_create(name='PManager')

# Create the 'ISAdmin' group if it doesn't exist
ISadmin_group, _ = Group.objects.get_or_create(name='ISAdmin')

def usertype(request):
    return render(request, 'usertype.html')

def islogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.groups.filter(name='Isadmin').exists() or user.groups.filter(name='PManager').exists():
                return HttpResponse("Port Managers and Admin cannot log in as Market Checkers.")
            else:
                login(request, user)
                return redirect('Analytics:forms')
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

                if not my_user.groups.filter(name='PManager').exists() and not my_user.groups.filter(name='ISAdmin').exists():
                    market_checker_group.user_set.add(my_user)  # Add the user to the Market Checker group

                return redirect('Authentication:login')  # Update this with the correct URL
            except IntegrityError:
                return HttpResponse("Username or email already exists!")

    return render(request, 'register.html')



def ispmloginhtml(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.groups.filter(name='Market Checker').exists() or user.groups.filter(name='ISAdmin').exists():
                return HttpResponse("Market Checkers and Admins cannot log in as Port Manager.")
            else:
                login(request, user)
                return redirect('Analytics:dashboard')
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

                if not my_user.groups.filter(name='ISAdmin').exists() and not my_user.groups.filter(name='Market Checker').exists():
                    pmanager_group.user_set.add(my_user)  # Add the user to the PManager group

                return redirect('Authentication:pmlogin')
            except IntegrityError:
                return HttpResponse("Username or email already exists!")

    return render(request, 'PMregister.html')


def isadminloginhtml(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.groups.filter(name='Market Checker').exists() or user.groups.filter(name='PManager').exists():
                return HttpResponse("Port Managers and Market Checkers cannot log in as Admins.")
            else:
                login(request, user)
                return redirect('Analytics:admindashboard')
        else:
            return HttpResponse("Username or password is incorrect!")

    return render(request, 'admin.html')




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

                if not my_user.groups.filter(name='PManager').exists() and not my_user.groups.filter(name='Market Checker').exists():
                    ISadmin_group.user_set.add(my_user)  # Add the user to the ISAdmin group

                return redirect('Authentication:loginadmin')  # Update this with the correct URL
            except IntegrityError:
                return HttpResponse("Username or email already exists!")

    return render(request, 'adminreg.html')

