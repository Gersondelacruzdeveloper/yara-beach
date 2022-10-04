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

from django.shortcuts import render
from excursions.models import Excursions
from rentals.models import Rentals
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage

# Create your views here.

# show excursions and rentals in home page
def home(request):
    excursions = Excursions.objects.all()[:4]
    rentals = Rentals.objects.all()[:4]
    context = {'excursions': excursions, 'rentals':rentals}
    return render(request, 'home.html', context)


# Contact form
def contact(request):
    return render(request, 'contact.html')
