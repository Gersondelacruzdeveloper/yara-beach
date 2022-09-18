from django.shortcuts import render
from .models import Rentals

# Create your views here.

def rentals(request):
    return render(request, 'rentals/rentals.html')

# Show all the rentals
def rentals(request):
    rental = Rentals.objects.all()
    context = {'rentals': rental}
    return render(request, 'rentals/rentals.html', context)