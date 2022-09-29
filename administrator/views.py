from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from excursions.models import Excursions,Photos
from rentals.models import Rentals
from .forms import ExcursionForm, ExcursionFormPhotos
from django.contrib import messages

# Create your views here.

# Administrator function
def administrator(request):
    total_users = User.objects.all().count()
    context = {'total_users': total_users}
    return render(request, 'administrator/administrator.html', context)

# Query all excursions for admin
def admin_excursions(request):
    excursions = Excursions.objects.all()
    context = {'excursions': excursions}
    return render(request, 'administrator/admin_excursions.html', context)

# Query all rentals for admin
def admin_rentals(request):
    rentals = Rentals.objects.all()
    context = {'rentals': rentals}
    return render(request, 'administrator/admin_rentals.html', context)

# Add excursion
def add_excursions(request):
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
    return render(request, 'administrator/add_excursions.html', context)

# Edit excursion and add more photos
def edit_excursions(request,pk):
    excursions = Excursions.objects.get(id=pk)
    form = ExcursionForm(instance=excursions)
    formPhotos = ExcursionFormPhotos()
    if request.method == 'POST':
        form = ExcursionForm(request.POST, request.FILES, instance=excursions)
        images = request.FILES.getlist('images')
        if form.is_valid():
            # Loop through all images and save then 
            for image in images:
                photo = Photos.objects.create(
                    excursion=excursions,
                    image_name = excursions.image_name,
                    images= image,
            )
            form.save()
            photo.save()
            messages.success(request, 'Excursion edit Succesfullly')
        return redirect('admin-excursion')
    context = {'form':form, 'formPhotos':formPhotos, 'excursions':excursions}
    return render(request, 'administrator/edit_excursion.html', context)

# Delete excursion
def delete_excursions(request, pk):
    excursion = Excursions.objects.get(id=pk)
    title = excursion.title
    if request.method == 'POST':
        excursion.delete()
        messages.success(request, 'Excursion deleted Succesfullly')
        return redirect('admin-excursion')
    context = {'excursion':excursion,'title':title}
    return render(request, 'administrator/delete_excursion.html', context)