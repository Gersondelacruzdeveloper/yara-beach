from django.shortcuts import render
from .models import Excursions

# Create your views here.

def excursion(request):
    """
    Show all the excursions
    """
    excursions = Excursions.objects.all()
    context = {'excursions':excursions}
    return render(request, 'excursions/excursions.html', context)