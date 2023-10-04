from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from excursions.models import Excursions, Photos, Reference,PageVisit
from rentals.models import Rentals
from rentals.models import Photos as Rental_photos
from .forms import ExcursionForm, ExcursionFormPhotos, RentalForm, RentalFormPhotos,SellerForm
from django.contrib import messages
from checkout.models import ExcursionOrder, AccommodationOrder
from django.contrib.auth.decorators import login_required
import datetime
from datetime import date, timedelta
from django.db.models import Q
# Create your views here.
def pageVisit(request):
      user_visits = PageVisit.objects.all()
      context = {'user_visits':user_visits}
      return render(request, 'administrator/user_visits.html', context)

# Administrator function
@login_required(login_url='/accounts/login/')
def administrator(request):
    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have persmision to access that page')
        return redirect('home')

    total_users = User.objects.all().count()
    # Excursions queriess
    all_excursion_orders = ExcursionOrder.objects.all()
    # Today bookings
    today_excursion_bookings = all_excursion_orders.filter(
        excursion_date=datetime.date.today())
    # tomorow bookings
    tomorow_excursion_bookings = all_excursion_orders.filter(
        excursion_date=datetime.date.today() + timedelta(days=1))

    # Future bookings
    future_excursion_bookings = all_excursion_orders.filter(
        excursion_date__gt=datetime.date.today())
    # Previous bookings
    previous_excursion_bookings = all_excursion_orders.filter(
        excursion_date__lt=datetime.date.today())

    # All rentals
    all_rental_orders = AccommodationOrder.objects.all()
    # Today rental booking
    today_rental_bookings = all_rental_orders.filter(
        check_in=datetime.date.today())
    # Future rental bookings
    future_rental_bookings = all_rental_orders.filter(
        check_in__gte=datetime.date.today())
    # Previous bookings
    previous_rental_bookings = all_rental_orders.filter(
        check_in__lte=datetime.date.today())
    

    # rentals queries
    context = {'total_users': total_users,
               # excursions
               'today_excursion_bookings': today_excursion_bookings,
               'future_excursion_bookings': future_excursion_bookings,
               'previous_excursion_bookings': previous_excursion_bookings,
               'tomorow_excursion_bookings':tomorow_excursion_bookings,
               # rentals
               'today_rental_bookings': today_rental_bookings,
               'future_rental_bookings': future_rental_bookings,
               'previous_rental_bookings': previous_rental_bookings,
               }

    return render(request, 'administrator/administrator.html', context)

# create fake users
@login_required(login_url='/accounts/login/')
def generate_users(request):
    if request.method == "POST":
        fake_username = request.POST.get('usernames')
        if fake_username:
            usernames = [item.strip() for item in fake_username.split(',')]
            for username in usernames:
                if not User.objects.filter(username=username).exists():
                    password = username + username
                    email = f"{username}@example.com"
                    User.objects.create_user(username=username, password=password, email=email, last_name='generated')
            messages.success(request, 'Users have been created')
    return redirect('administrator')


@login_required(login_url='/accounts/login/')
def administrator_seller(request):
    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have persmision to access that page')
        return redirect('home')
    all_sellers = Reference.objects.all().order_by()
    sellers_to_be_pay = Reference.objects.filter(due_to_pay_amount__gt=0)
    
    context = {'all_sellers': all_sellers, 'sellers_to_be_pay': sellers_to_be_pay}
    return render(request, 'administrator/seller.html', context)

@login_required(login_url='/accounts/login/')
def paid_seller(request, pk):
    seller = Reference.objects.get(id=pk)
    seller_name = seller.full_name
    Seller_reference =seller.reference_number
    seller_du_amount = seller.due_to_pay_amount
    context = {'pk': pk, 'seller_name': seller_name, 'Seller_reference':Seller_reference, 'seller_du_amount':seller_du_amount}
    return render(request, 'administrator/excursions/seller_comfirm.html', context)

# Make the seller du amount back to 0
@login_required(login_url='/accounts/login/')
def seller_due_zero(request, pk):
    seller = Reference.objects.get(id=pk)
    if request.method == "POST":
        seller.due_to_pay_amount = 0.00
        seller.save()
        return redirect('seller')
    

@login_required(login_url='/accounts/login/')
def create_auto_sellers(request):
    # Check if the user is a superuser
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to access that page')
        return redirect('home')

    if request.method == 'POST':
        quantity = int(request.POST.get("generate_quantity_sellers"))

        for i in range(1, quantity):
            seller_name = f'automated seller {i}'

            # Check if the seller name already exists
            if not Reference.objects.filter(full_name=seller_name).exists():
                seller = Reference(full_name=seller_name)
                seller.save()

        messages.success(request, 'Your sellers have been created.')
        return redirect('seller')
          
# US Search in CRM with input
def search_sellers(request):
    sellers = Reference.objects.all()
    sellers_to_be_pay = Reference.objects.filter(due_to_pay_amount__gt=0)
    all_sellers = Reference.objects.all()
    seller_search_input = request.GET.get('seller_search_input')
    if seller_search_input:
        sellers = Reference.objects.filter(Q(full_name__icontains=seller_search_input) | Q(reference_number__icontains=seller_search_input) | Q(email__icontains=seller_search_input) | Q(phone_number__icontains=seller_search_input) | Q(
            cedula__icontains=seller_search_input) | Q(account_number__icontains=seller_search_input))
    context = {'sellers': sellers, 'seller_search_input': seller_search_input, 'sellers_to_be_pay':sellers_to_be_pay, 'all_sellers':all_sellers}
    return render(request, 'administrator/search_sellers.html', context)

# Edit seller and add more photos
@login_required(login_url='/accounts/login/')
def edit_seller(request, pk):
    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have persmision to access that page')
        return redirect('home')
    seller = Reference.objects.get(id=pk)
    form = SellerForm(instance=seller)
    if request.method == 'POST':
        form = SellerForm(request.POST,  instance=seller)
        form.save()
        messages.success(request, 'Seller edit Succesfullly')
        return redirect('seller')
    context = {'form': form,'seller': seller}
    return render(request, 'administrator/edit_seller.html', context)

# Delete excursion

@login_required(login_url='/accounts/login/')
def delete_seller(request, pk):
    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have persmision to access that page')
        return redirect('home')
    seller = Reference.objects.get(id=pk)
    name = Reference.full_name
    if request.method == 'POST':
        seller.delete()
        messages.success(request, 'seller deleted Succesfullly')
        return redirect('seller')
    context = {'seller': seller, 'seller_name': name}
    return render(request, 'administrator/delete_seller.html', context)

# Query all rentals for admin
@login_required(login_url='/accounts/login/')
def admin_rentals(request):
    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have persmision to access that page')
        return redirect('home')
    rentals = Rentals.objects.all()
    context = {'rentals': rentals}
    return render(request, 'administrator/rentals/admin_rentals.html', context)

# Add rentals


@login_required(login_url='/accounts/login/')
def add_rentals(request):
    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have persmision to access that page')
        return redirect('home')
    form = RentalForm()
    if request.method == 'POST':
        user = request.user
        author = Rentals(user=user)
        form = RentalForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rental created Succesfullly')
        return redirect('admin-rental')
    context = {'form': form}
    return render(request, 'administrator/rentals/add_rentals.html', context)

# Edit rentals and add more photos


@login_required(login_url='/accounts/login/')
def edit_rentals(request, pk):
    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have persmision to access that page')
        return redirect('home')
    rentals = Rentals.objects.get(id=pk)
    form = RentalForm(instance=rentals)
    formPhotos = RentalFormPhotos()
    if request.method == 'POST':
        form = RentalForm(request.POST, request.FILES, instance=rentals)
        images = request.FILES.getlist('images')
        if form.is_valid():
            if images:
                # Loop through all images and save then
                for image in images:
                    photo = Rental_photos.objects.create(
                        rental=rentals,
                        image_name=rentals.image_name,
                        images=image,
                    )
                    photo.save()
            form.save()
            messages.success(request, 'Rental edit Succesfullly')
        return redirect('admin-rental')
    context = {'form': form, 'formPhotos': formPhotos, 'rentals': rentals}
    return render(request, 'administrator/rentals/edit_rental.html', context)

# Delete rental photos

@login_required(login_url='/accounts/login/')
def delete_rentals_photos(request, pk):
    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have persmision to access that page')
        return redirect('home')
    photo = Rental_photos.objects.get(id=pk)
    if request.method == 'POST':
        photo.delete()
        messages.success(request, 'Photo deleted Succesfullly')
        return redirect('edit_rental', pk=photo.rental.id)
    context = {'photo': photo}
    return render(request, 'administrator/rentals/delete_rental_photos.html', context)

# Delete rental
@login_required(login_url='/accounts/login/')
def delete_rentals(request, pk):
    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have persmision to access that page')
        return redirect('home')
    rental = Rentals.objects.get(id=pk)
    title = rental.title
    if request.method == 'POST':
        rental.delete()
        messages.success(request, 'Rental deleted Succesfullly')
        return redirect('admin-rental')
    context = {'rental': rental, 'title': title}
    return render(request, 'administrator/rentals/delete_rental.html', context)


# --------------------------------- All admin excursion functions are from here below

# Query all excursions for admin
@login_required(login_url='/accounts/login/')
def admin_excursions(request):
    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have persmision to access that page')
        return redirect('home')
    excursions = Excursions.objects.all()
    context = {'excursions': excursions}
    return render(request, 'administrator/excursions/admin_excursions.html', context)

# Add excursion


@login_required(login_url='/accounts/login/')
def add_excursions(request):
    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have persmision to access that page')
        return redirect('home')
    form = ExcursionForm()
    if request.method == 'POST':
        user = request.user
        author = Excursions(user=user)
        form = ExcursionForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            messages.success(request, 'Excursion created Succesfullly')
        return redirect('admin-excursion')
    context = {'form': form}
    return render(request, 'administrator/excursions/add_excursions.html', context)


# Edit excursion and add more photos
@login_required(login_url='/accounts/login/')
def edit_excursions(request, pk):
    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have persmision to access that page')
        return redirect('home')
    excursions = Excursions.objects.get(id=pk)
    form = ExcursionForm(instance=excursions)
    formPhotos = ExcursionFormPhotos()
    if request.method == 'POST':
        form = ExcursionForm(request.POST, request.FILES, instance=excursions)
        images = request.FILES.getlist('images')
        if form.is_valid():
            if images:
                # Loop through all images and save then
                for image in images:
                    photo = Photos.objects.create(
                        excursion=excursions,
                        image_name=excursions.image_name,
                        images=image,
                    )
                    photo.save()
            form.save()
            messages.success(request, 'Excursion edit Succesfullly')
        return redirect('admin-excursion')
    context = {'form': form, 'formPhotos': formPhotos,
               'excursions': excursions}
    return render(request, 'administrator/excursions/edit_excursion.html', context)

# Delete excursion

@login_required(login_url='/accounts/login/')
def delete_excursions(request, pk):
    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have persmision to access that page')
        return redirect('home')
    excursion = Excursions.objects.get(id=pk)
    title = excursion.title
    if request.method == 'POST':
        excursion.delete()
        messages.success(request, 'Excursion deleted Succesfullly')
        return redirect('admin-excursion')
    context = {'excursion': excursion, 'title': title}
    return render(request, 'administrator/excursions/delete_excursion.html', context)

# Delete excursion photos


@login_required(login_url='/accounts/login/')
def delete_excursions_photos(request, pk):
    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have persmision to access that page')
        return redirect('home')
    photo = Photos.objects.get(id=pk)
    if request.method == 'POST':
        photo.delete()
        messages.success(request, 'Photo deleted Succesfullly')
        return redirect('edit_excursion', pk=photo.excursion.id)
    context = {'photo': photo}
    return render(request, 'administrator/excursions/delete_excursion_photos.html', context)