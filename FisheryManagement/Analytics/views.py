from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import Species, unloadType, Origin, Vessel, DailyTransaction
from django.http import JsonResponse
from collections import defaultdict
from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncYear
from datetime import datetime
from django.db.models import Q
from django.core.paginator import Paginator
from django.utils import timezone
from django.db import IntegrityError
from django.db.models import Max
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib import messages

from django.core.exceptions import MultipleObjectsReturned


""" TO GET DATA FROM THE FORMS """


@login_required(login_url='Authentication:MClandingPage')
def isforms(request):
    origins = Origin.objects.all()
    species_list = Species.objects.all()

    if request.method == 'POST':
        fishtype = request.POST.get('fishtype')
        quantity = request.POST.get('quantity')
        vessel = request.POST.get('vessel')
        placeofcatch = request.POST.get('placeofcatch')
        unload_type_name = request.POST.get('typeofUnload')

        # Check for completeness of form data
        if not all([fishtype, quantity, vessel, placeofcatch, unload_type_name]):
            return render(request, 'MCforms.html', {
                'origins': origins,
                'species_list': species_list,
                'error_message': 'Please fill in all the required fields.'
            })

        origin = placeofcatch.capitalize()

        try:
            dateofCatch = timezone.now().strftime('%Y-%m-%d')

            # Create or get Origin
            origin_instance, _ = Origin.objects.get_or_create(
                origin=origin
            )
        except Origin.DoesNotExist:
            origin_instance = Origin.objects.create(
                origin=origin,
            )

        # Check if the species already exists
        existing_species = Species.objects.filter(species_name=fishtype).first()

        if existing_species:
            # Use the existing species instead of creating a new one
            species_instance = existing_species
        else:
            try:
                species_instance, _ = Species.objects.get_or_create(
                    species_name=fishtype,
                    quantity=quantity,
                )
            except IntegrityError:
                species_instance = Species.objects.get(species_name=fishtype)

        vessel_instance, _ = Vessel.objects.get_or_create(
            vessel_name=vessel,
            origin=origin_instance,
        )

        unload_type_instance, _ = unloadType.objects.get_or_create(unloadTypeName=unload_type_name)

        new_transaction = DailyTransaction(
            species=species_instance,
            quantity=quantity,
            vessel=vessel_instance,
            origin=origin_instance,
            date=dateofCatch,
            unloadType=unload_type_instance,
        )
        new_transaction.save()

        return HttpResponse('Form submitted successfully.')  # You can modify this as needed

    return render(request, 'MCforms.html', {
        'origins': origins,
        'species_list': species_list,
    })

@login_required(login_url='Authentication:MClandingPage')
def recentList(request):
    most_recent_date = DailyTransaction.objects.aggregate(max_date=Max('date'))['max_date']

    transactions = DailyTransaction.objects.filter(date=most_recent_date)

    search_query = request.GET.get('q')

    if search_query:
        transactions = transactions.filter(
            Q(species__species_name__icontains=search_query) |
            Q(quantity__icontains=search_query) |
            Q(vessel__vessel_name__icontains=search_query) |
            Q(origin__origin__icontains=search_query)
        )

    paginator = Paginator(transactions, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'recentlist.html', {'transactions': page, 'search_query': search_query})

""" FOR EDITING USER INFORMATION """
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

""" TO DELETE USER IN USER'S TABLE """
@login_required(login_url='Authentication:loginadmin')
def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('Analytics:userstable')  

@login_required(login_url='Authentication:PortManager')
def OCdash(request):
    # Get unique origins directly from the database using distinct()
    unique_origins = Origin.objects.values('origin').distinct()

    # Rest of your code
    years = DailyTransaction.objects.dates('date', 'year').order_by('-date').distinct()
    unique_years_set = set(year.year for year in years)
    unique_years = list(unique_years_set)

    return render(request, 'OCDash.html', {'origins': unique_origins, 'unique_years': unique_years})

""" API FOR DATA COLLECTION AND GRAPHS """
@require_GET
def dataUnloadingDash(request):
    selected_fish_type = request.GET.get('fish_type', None)
    selected_month = request.GET.get('month', None)
    selected_year = request.GET.get('year', None)
    selected_origin = request.GET.get('origin', None)

    transactions = DailyTransaction.objects.filter(species__species_name=selected_fish_type) if selected_fish_type else DailyTransaction.objects.all()
    if selected_month:
        transactions = transactions.filter(date__month=selected_month)  
    if selected_year:
        transactions = transactions.filter(date__year=selected_year)
    if selected_origin:
        transactions = transactions.filter(origin__origin=selected_origin)

    # Calculate quantity by date
    quantity_by_date = defaultdict(int)
    for transaction in transactions:
        quantity_by_date[str(transaction.date)] += transaction.quantity

    # Calculate monthly and yearly catch
    monthly_catch = transactions.annotate(month=TruncMonth('date')).values('month').annotate(total_quantity=Sum('quantity'))
    yearly_catch = transactions.annotate(year=TruncYear('date')).values('year').annotate(total_quantity=Sum('quantity'))

    # Calculate quantities by species, origin, and vessel
    species_quantities = transactions.values('species__species_name').annotate(total_quantity=Sum('quantity'))
    origin_quantities = transactions.values('origin__origin').annotate(total_quantity=Sum('quantity'))
    vessel_quantities = transactions.values('vessel__vessel_name').annotate(total_quantity=Sum('quantity'))

    # Prepare data for labels and quantities
    labels_daily = []
    quantities = []
    species = []
    origins = []
    vessels = []

    unique_dates_set = set()  
    for transaction in transactions:
        date_str = transaction.date.strftime('%B %d, %Y')  
        if date_str not in unique_dates_set: 
            labels_daily.append(date_str) 
            quantities.append(quantity_by_date[str(transaction.date)]) 
            unique_dates_set.add(date_str) 
        species.append(transaction.species.species_name)
        origin_data = transaction.origin.origin if transaction.origin else None
        origins.append(origin_data)
        vessels.append(transaction.vessel.vessel_name)

    # Sort daily data based on date
    daily_data_sorted = sorted(zip(labels_daily, quantities, species, origins, vessels), key=lambda x: datetime.strptime(x[0], '%B %d, %Y'))
    labels_daily_sorted, quantities_sorted, species_sorted, origins_sorted, vessels_sorted = zip(*daily_data_sorted)

    # Prepare data for monthly and yearly catch
    labels_monthly = []
    quantities_monthly = []
    labels_yearly = []
    quantities_yearly = []

    for entry in monthly_catch:
        month = entry['month'].strftime('%b %Y')
        labels_monthly.append(month)  
        quantities_monthly.append(entry['total_quantity'])

    for entry in yearly_catch:
        year = entry['year'].strftime('%Y')
        labels_yearly.append(year)  
        quantities_yearly.append(entry['total_quantity'])

    # Prepare data for species, origin, and vessel quantities
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

    # Construct the response data
    data = {
        'labels_daily': labels_daily_sorted,
        'quantities': quantities_sorted,
        'labels_monthly': labels_monthly,
        'quantities_monthly': quantities_monthly,
        'labels_yearly': labels_yearly,
        'quantities_yearly': quantities_yearly,
        'species': species_sorted,
        'origin': origins_sorted,
        'vessel': vessels_sorted,
        'species_data': species_data,
        'origin_data': origin_data,  
        'vessel_data': vessel_data,
    }

    return JsonResponse(data)

@login_required(login_url='Authentication:PortManager')
def FCdash(request):
    species_list = Species.objects.all()
    
    # Get distinct years from the database
    years = DailyTransaction.objects.dates('date', 'year').order_by('-date').distinct()

    # Extract unique years using a set
    unique_years_set = set(year.year for year in years)

    # Convert the set back to a list for iteration in the template
    unique_years = list(unique_years_set)

    return render(request, 'FCDash.html', {'species_list': species_list, 'unique_years': unique_years})

""" CONTENTS OF ADMIN DASHBOARD """
@login_required(login_url='Authentication:loginadmin')
def isadmindashboard(request):
    recent_transactions = DailyTransaction.objects.order_by('-date')[:4]

    transactions = DailyTransaction.objects.all()

    total_number_of_inputs = DailyTransaction.objects.count()

    top_fishes = DailyTransaction.objects.values('species__species_name').annotate(total_quantity=Sum('quantity')).order_by('-total_quantity')[:3]

    top_vessels = DailyTransaction.objects.values('vessel__vessel_name').annotate(total_quantity=Sum('quantity')).order_by('-total_quantity')[:3]

    top_origins = DailyTransaction.objects.values('origin__origin').annotate(total_quantity=Sum('quantity')).order_by('-total_quantity')[:3]

    return render(request, 'admindash.html', {
        'transactions': transactions,
        'recent_transactions': recent_transactions,
        'total_number_of_inputs': total_number_of_inputs,
        'top_fishes': top_fishes,
        'top_vessels': top_vessels,
        'top_origins': top_origins,
    })

""" USER'S TABLE """
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

        paginator = Paginator(userstable, 9)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)

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



""" UNLOADING HISTORY TABLE """
@login_required(login_url='Authentication:loginadmin')
def unloadhistory(request):
    transactions = DailyTransaction.objects.all()
    search_query = request.GET.get('q')
    
    if search_query:
        transactions = transactions.filter(
            Q(species__species_name__icontains=search_query) |
            Q(quantity__icontains=search_query) |
            Q(vessel__vessel_name__icontains=search_query) |
            Q(origin__origin__icontains=search_query) 

        )
    
    paginator = Paginator(transactions, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    
    return render(request, 'unloadhistory.html', {'transactions': page, 'search_query': search_query})


""" FOR EDITING UNLOADING HISTORY """


@login_required(login_url='Authentication:loginadmin')
def edit_unloading(request, id):
    transaction = get_object_or_404(DailyTransaction, id=id)

    if request.method == 'POST':
        origin_name = request.POST.get('placeofcatch')
        try:
            # Attempt to get the origin from the database
            origin = Origin.objects.get(origin=origin_name)
        except Origin.DoesNotExist:
            # Handle the case when the origin does not exist
            return HttpResponse(f"Origin '{origin_name}' does not exist. Please select a valid origin.")

        try:
            # Attempt to get the vessel from the database
            vessel_name = request.POST.get('vessel')
            vessel = Vessel.objects.filter(vessel_name=vessel_name).first()
            if not vessel:
                raise Vessel.DoesNotExist
        except Vessel.DoesNotExist:
            # Handle the case when the vessel does not exist
            return HttpResponse(f"Vessel '{vessel_name}' does not exist. Please select a valid vessel.")
        except MultipleObjectsReturned:
            # Handle the case when multiple vessels with the same name exist
            return HttpResponse(f"Multiple vessels with the name '{vessel_name}' exist. Please contact support.")

        # Update the transaction with the new data from the form
        transaction.species = Species.objects.get(species_name=request.POST.get('fishtype'))
        transaction.quantity = request.POST.get('quantity')
        transaction.vessel = vessel
        transaction.origin = origin
        transaction.unloadType = unloadType.objects.get(unloadTypeName=request.POST.get('typeofUnload'))
        
        transaction.save()
        
        # Redirect to the unload history page after editing
        return redirect('Analytics:unloadhistory') 

    # Pass the transaction details to the template
    return render(request, 'editunloading.html', {
        'transaction': transaction,
        'origins': Origin.objects.all(),  # Pass origins for the dropdown
        'species_list': Species.objects.all(),  # Pass species for the dropdown
    })


""" FOR DELETING UNLOADING HISTORY """
@login_required(login_url='Authentication:loginadmin')
def delete_unload_history(request, id):
    try:
        transaction = get_object_or_404(DailyTransaction, id=id)
        transaction.delete()
        messages.success(request, 'Transaction deleted successfully.')
    except IntegrityError as e:
        messages.error(request, f'Error deleting transaction: {e}')
    return redirect('Analytics:unloadhistory')
