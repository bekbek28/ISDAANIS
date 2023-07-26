from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User, Group
from .models import Species, DailyTransaction, Vessel, Origin
from django.http import JsonResponse
from collections import defaultdict
from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncYear
from datetime import datetime
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

    quantity_by_date = defaultdict(int)
    for transaction in transactions:
        quantity_by_date[str(transaction.date)] += transaction.quantity

    monthly_catch = transactions.annotate(month=TruncMonth('date')).values('month').annotate(total_quantity=Sum('quantity'))
    yearly_catch = transactions.annotate(year=TruncYear('date')).values('year').annotate(total_quantity=Sum('quantity'))

    species_quantities = transactions.values('species__species_name').annotate(total_quantity=Sum('quantity'))
    origin_quantities = transactions.values('origin__origin').annotate(total_quantity=Sum('quantity'))
    vessel_quantities = transactions.values('vessel__vessel_name').annotate(total_quantity=Sum('quantity'))

    labels_daily = []
    quantities = []
    prices = []
    species = []
    origins = []
    vessels = []
    labels_monthly = []
    quantities_monthly = []
    labels_yearly = []
    quantities_yearly = []

    unique_dates_set = set()  
    for transaction in transactions:
        date_str = transaction.date.strftime('%B %d, %Y')  
        if date_str not in unique_dates_set: 
            labels_daily.append(date_str) 
            quantities.append(quantity_by_date[str(transaction.date)]) 
            unique_dates_set.add(date_str) 

        prices.append(transaction.price)
        species.append(transaction.species.species_name)
        origin_data = transaction.origin.origin if transaction.origin else None
        origins.append(origin_data)
        vessels.append(transaction.vessel.vessel_name)

   
    daily_data_sorted = sorted(zip(labels_daily, quantities, prices, species, origins, vessels), key=lambda x: datetime.strptime(x[0], '%B %d, %Y'))


    labels_daily_sorted, quantities_sorted, prices_sorted, species_sorted, origins_sorted, vessels_sorted = zip(*daily_data_sorted)

    for entry in monthly_catch:
        month = entry['month'].strftime('%b %Y')
        labels_monthly.append(month)  
        quantities_monthly.append(entry['total_quantity'])

    for entry in yearly_catch:
        year = entry['year'].strftime('%Y')
        labels_yearly.append(year)  
        quantities_yearly.append(entry['total_quantity'])

    species_data = []
    for entry in species_quantities:
        species_data.append({
            'species_name': entry['species__species_name'],
            'total_quantity': entry['total_quantity'],
        })

    origin_data = []
    for entry in origin_quantities:
        origin_data.append({
            'origin': entry['origin__origin'],
            'total_quantity': entry['total_quantity'],
        })

  
    vessel_data = []
    for entry in vessel_quantities:
        vessel_data.append({
            'vessel_name': entry['vessel__vessel_name'],
            'total_quantity': entry['total_quantity'],
        })

    data = {
        'labels_daily': labels_daily_sorted,
        'quantities': quantities_sorted,
        'labels_monthly': labels_monthly,
        'quantities_monthly': quantities_monthly,
        'labels_yearly': labels_yearly,
        'quantities_yearly': quantities_yearly,
        'prices': prices_sorted,
        'species': species_sorted,
        'origin': origins_sorted,
        'vessel': vessels_sorted,
        'species_data': species_data,
        'origin_data': origin_data,  
        'vessel_data': vessel_data,  
    }

    return JsonResponse(data)






@login_required(login_url='Authentication:usertype')
def  unloadingdash(request):
    return render(request, 'unloadingDash.html' )

@login_required(login_url='Authentication:loginadmin')
def isadmindashboard(request):
    recent_transactions = DailyTransaction.objects.order_by('-date')[:4]

    transactions = DailyTransaction.objects.all()

    total_number_of_inputs = DailyTransaction.objects.count()

    

    return render(request, 'admindash.html', {
        'transactions': transactions,
        'recent_transactions': recent_transactions,
        'total_number_of_inputs': total_number_of_inputs,
    })

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
def loadhistory(request):
    transactions = DailyTransaction.objects.all()
    search_query = request.GET.get('q')
    
    if search_query:
        transactions = transactions.filter(
            Q(species__species_name__icontains=search_query) |
            Q(quantity__icontains=search_query) |
            Q(price__icontains=search_query)
        )
    
    paginator = Paginator(transactions, 4)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    
    return render(request, 'loadhistory.html', {'transactions': page, 'search_query': search_query})



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
    
    return render(request, 'unloadhistory.html', {'transactions': page, 'search_query': search_query})


def logout_view(request):
    logout(request)
    return redirect('Authentication:usertype')