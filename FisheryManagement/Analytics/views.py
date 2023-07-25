from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User, Group
from .models import Species, DailyTransaction, Vessel, Origin
from django.http import JsonResponse
from collections import defaultdict
from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncYear
from django.db.models import Q
from django.core.paginator import Paginator



@login_required(login_url='Authentication:usertype')
def isforms(request):
    origins = Origin.objects.all()

    if request.method == 'POST':
        fishtype = request.POST['fishtype']
        quantity = request.POST['quantity']
        vessel = request.POST['vessel']
        placeofcatch = request.POST['placeofcatch']
        dateofCatch = request.POST['dateofCatch']
        price = request.POST['price']

        origin = placeofcatch.capitalize()
        print(origin)
        try:
            origin_instance = Origin.objects.get(origin=origin, date=dateofCatch)
        except Origin.DoesNotExist:
            origin_instance = Origin.objects.create(
                origin=origin,
                date=dateofCatch,
            )

        species_instance, _ = Species.objects.get_or_create(
            species_name=fishtype,
            quantity=quantity,
            price=price,
        )

        vessel_instance, _ = Vessel.objects.get_or_create(
            vessel_name=vessel,
            origin=origin_instance,
        )

        new_transaction = DailyTransaction(
            species=species_instance,
            quantity=quantity,
            vessel=vessel_instance,
            origin=origin_instance,
            date=dateofCatch,
            price=price,
        )
        new_transaction.save()

    return render(request, 'MCforms.html', {
        'origins': origins
    })

@login_required(login_url='Authentication:loginadmin')
def edit_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        username = request.POST.get('username')
        usergroup = request.POST.get('usergroup')

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        if user.username:
            pass
        else:
            user.username = username
        user.group = usergroup

        group = Group.objects.get(name=usergroup)
        user.group = group

        user.save()

        return redirect('Analytics:userstable') 

    return render(request, 'edituser.html', {
        'user': user
    })


def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('Analytics:userstable')  


@login_required(login_url='Authentication:usertype')
def  loadingdash(request):
    return render(request, 'loadingDash.html' )

def dataUnloadingDash(request):
    transactions = DailyTransaction.objects.all()

    # Use defaultdict to group quantities by date and calculate the sum for daily catch
    quantity_by_date = defaultdict(int)
    for transaction in transactions:
        quantity_by_date[str(transaction.date)] += transaction.quantity

    # Use Django's aggregation to calculate the sum for monthly and yearly catch
    monthly_catch = transactions.annotate(month=TruncMonth('date')).values('month').annotate(total_quantity=Sum('quantity'))
    yearly_catch = transactions.annotate(year=TruncYear('date')).values('year').annotate(total_quantity=Sum('quantity'))

    labels = []
    quantities = []
    prices = []
    species = []
    origins = []
    vessels = []
    quantities_monthly = []
    quantities_yearly = []

    # Extract the dates, quantities, prices, species, origin, and vessel for daily catch
    for transaction in transactions:
        labels.append(str(transaction.date))  # Convert date to string for chart labels
        quantities.append(transaction.quantity)
        prices.append(transaction.price)
        species.append(transaction.species.species_name)
        origin_data = transaction.origin.origin if transaction.origin else None
        origins.append(origin_data)
        vessels.append(transaction.vessel.vessel_name)

    # Extract the months and quantities for monthly catch
    for entry in monthly_catch:
        month = entry['month'].strftime('%Y-%m')
        quantities_monthly.append(entry['total_quantity'])
        labels.append(month)  # Add month labels for Chart.js

    # Extract the years and quantities for yearly catch
    for entry in yearly_catch:
        year = entry['year'].strftime('%Y')
        quantities_yearly.append(entry['total_quantity'])
        labels.append(year)  # Add year labels for Chart.js

    # Extract the daily catch quantities
    for date, quantity in quantity_by_date.items():
        quantities.append(quantity)
        # Add date labels for Chart.js
        labels.append(date)

    data = {
        'labels': labels,
        'quantities': quantities,
        'quantities_monthly': quantities_monthly,
        'quantities_yearly': quantities_yearly,
        'prices': prices,
        'species': species,
        'origin': origins,
        'vessel': vessels,
    }

    return JsonResponse(data)

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

    search_query = request.GET.get('q')
    if search_query:
        market_checker = market_checker.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(username__icontains=search_query)
        )

        pm_manager = pm_manager.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(username__icontains=search_query)
        )

        is_admin = is_admin.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(username__icontains=search_query)
        )
    
    return render(request, 'userstable.html', {
        'market_checker': market_checker,
        'pm_manager': pm_manager,
        'is_admin': is_admin,
        'search_query':search_query
    })

@login_required(login_url='Authentication:loginadmin')
def loadhistory(request,):
    transactions = DailyTransaction.objects.all()
    return render(request, 'loadhistory.html', {'transactions': transactions})

@login_required(login_url='Authentication:loginadmin')

def unloadhistory(request):
    transactions = DailyTransaction.objects.all()
    search_query = request.GET.get('q')
    if search_query:
        transactions = transactions.filter(
            Q(species__species_name__icontains=search_query) |
            Q(quantity__icontains=search_query) |
            Q(vessel__vessel_name__icontains=search_query) |
            Q(origin__origin__icontains=search_query) |
            Q(price__icontains=search_query)
        )
    paginator = Paginator(transactions, 4)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'unloadhistory.html', {'transactions': page})



def logout_view(request):
    logout(request)
    return redirect('Authentication:usertype')