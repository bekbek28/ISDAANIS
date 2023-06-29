from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required
def  isforms(request):
    return render(request, 'MCforms.html' )

@login_required
def  isdashboard(request):
    return render(request, 'dashboard.html' )

@login_required
def  isadmindashboard(request):
    return render(request, 'admindash.html' )
