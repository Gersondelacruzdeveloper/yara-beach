from django.shortcuts import render
from excursions.models import Excursions
from rentals.models import Rentals

# Create your views here.

# show excursions and rentals in home page
def home(request):
    excursions = Excursions.objects.all()[:4]
    rentals = Rentals.objects.all()[:4]
    context = {'excursions': excursions, 'rentals':rentals}
    return render(request, 'home.html', context)