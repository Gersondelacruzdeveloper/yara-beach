from django.shortcuts import render
from django.contrib.auth.models import User
from excursions.models import Excursions
from rentals.models import Rentals

# Create your views here.

# Administrator function
def administrator(request):
    total_users = User.objects.all().count()
    context = {'total_users': total_users}
    return render(request, 'administrator/administrator.html', context)

def admin_excursions(request):
    excursions = Excursions.objects.all()
    context = {'excursions': excursions}
    return render(request, 'administrator/admin_excursions.html', context)

def admin_rentals(request):
    rentals = Rentals.objects.all()
    context = {'rentals': rentals}
    return render(request, 'administrator/admin_rentals.html', context)
