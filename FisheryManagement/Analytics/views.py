from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='Authentication:loginadmin')
def addUser(request):
    if request.method == 'POST':
        # Retrieve user data from the form
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create a new user instance
        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )
        user.save()

        # Redirect to a success page or another view
        return redirect('Analytics:userstable')  # Change 'userstable' to your desired URL name

    # Render the template for the add user form
    return render(request, 'addUser.html')

@login_required(login_url='Authentication:usertype')
def  isforms(request):
    return render(request, 'MCforms.html' )

@login_required(login_url='Authentication:usertype')
def  loadingdash(request):
    return render(request, 'loadingDash.html' )

@login_required(login_url='Authentication:usertype')
def  unloadingdash(request):
    return render(request, 'unloadingDash.html' )

@login_required(login_url='Authentication:loginadmin')
def  isadmindashboard(request):
    return render(request, 'admindash.html' )

@login_required(login_url='Authentication:loginadmin')
def userstable(request):
    market_checker = Group.objects.get(name='Market Checker').user_set.all()
    pm_manager = Group.objects.get(name='PManager').user_set.all()
    is_admin = Group.objects.get(name='ISAdmin').user_set.all()
    
    return render(request, 'userstable.html', {
        'market_checker': market_checker,
        'pm_manager': pm_manager,
        'is_admin': is_admin
        
    })

@login_required(login_url='Authentication:loginadmin')
def analyticsTable(request,):
    return render(request, 'analytics.html' )

@login_required(login_url='Authentication:loginadmin')
def loadhistory(request,):
    return render(request, 'loadhistory.html')

@login_required(login_url='Authentication:loginadmin')
def unloadhistory(request,):
    return render(request, 'unloadhistory.html')



def logout_view(request):
    logout(request)
    return redirect('Authentication:usertype')
