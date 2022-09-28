from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from excursions.models import Excursions
from rentals.models import Rentals
from .forms import ExcursionForm
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

# Edit excursion
def edit_excursions(request,pk):
    excursion = Excursions.objects.get(id=pk)
    form = ExcursionForm(instance=excursion)
    if request.method == 'POST':
        form = ExcursionForm(request.POST, request.FILES, instance=excursion,)
        if form.is_valid():
            form.save()
            messages.success(request, 'Excursion edit Succesfullly')
        return redirect('admin-excursion')
    context = {'form':form}
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