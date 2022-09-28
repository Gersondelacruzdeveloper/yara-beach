from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from excursions.models import Excursions
from rentals.models import Rentals
from .forms import AddExcursionForm
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

# Add the excursion
def add_excursions(request):
    form = AddExcursionForm()
    if request.method == 'POST':
        user = request.user
        author = Excursions(user=user)
        form = AddExcursionForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            messages.success(request, 'A new excursion has been added')
        return redirect('admin-excursion')
    context = {'form': form}
    return render(request, 'administrator/add_excursions.html', context)