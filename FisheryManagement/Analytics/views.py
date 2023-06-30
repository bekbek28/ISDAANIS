from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.


@login_required
def  isforms(request):
    return render(request, 'MCforms.html' )

@login_required
def  isdashboard(request):
    return render(request, 'dashboard.html' )

""" @login_required """
def  isadmindashboard(request):
    return render(request, 'admindash.html' )

def logout_view(request):
    logout(request)
    return redirect('Authentication:usertype')
