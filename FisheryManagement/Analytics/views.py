from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.


@login_required(login_url='Authentication:usertype')
def  isforms(request):
    return render(request, 'MCforms.html' )

@login_required(login_url='Authentication:usertype')
def  isdashboard(request):
    return render(request, 'dashboard.html' )

@login_required(login_url='Authentication:loginadmin')
def  isadmindashboard(request):
    return render(request, 'admindash.html' )

@login_required(login_url='Authentication:loginadmin')
def userstable(request,):
    return render(request, 'userstable.html' )

@login_required(login_url='Authentication:loginadmin')
def analyticsTable(request,):
    return render(request, 'analytics.html' )

@login_required(login_url='Authentication:loginadmin')
def loadhistory(request,):
    return render(request, 'loadhistory.html')

def logout_view(request):
    logout(request)
    return redirect('Authentication:usertype')
