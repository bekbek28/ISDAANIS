from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .models import DailyTransaction, Species



@login_required(login_url='Authentication:usertype')
def isforms(request):
    if request.method == 'POST':
        fishtype = request.POST.get('fishtype')
        quantity = request.POST.get('quantity')
        vessel = request.POST.get('vessel')
        placeofcatch = request.POST.get('placeofcatch')
        dateofcatch = request.POST.get('dateofCatch')
        price = request.POST.get('price')

        # Retrieve the corresponding Species instance
        species = Species.objects.get(name=fishtype)

        # Create a new DailyTransaction object and save the data
        transaction = DailyTransaction(
            species=species,
            origin=placeofcatch,
            vessel=vessel,
            quantity=quantity,
            price=price, 
            date=dateofcatch
        )
        transaction.save()

        # Redirect to a success page or any other desired page
        return redirect('Analytics:loadhistory')  # Replace 'success' with your desired URL name

    # Render the MCforms.html template for GET requests
    return render(request, 'MCforms.html')



@login_required(login_url='Authentication:loginadmin')
def edit_user(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == 'POST':
        # Retrieve the updated user information from the form
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        username = request.POST.get('username')
        usergroup = request.POST.get('usergroup')

        # Retrieve the user object
        user = request.user

        # Update the user's attributes
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        # Update the user's group
        group = Group.objects.get(name=usergroup)
        user.group = group

        # Save the changes
        user.save()

        # Redirect to a success page or any other appropriate view
        return redirect('Analytics:userstable')  # Replace 'success-page' with your desired URL

    # Handle GET requests if needed
    return render(request, 'edituser.html', {
        'user': user
    })

def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()

    return redirect('Analytics:userstable')  # Replace 'user-list' with the URL of your user listing page



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
 

 