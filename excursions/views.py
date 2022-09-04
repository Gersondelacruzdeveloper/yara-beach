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



def excursion_details(request,pk):
    """
    Show the excursion details
    """
    excursions = Excursions.objects.get(id=pk)
    context = {'excursions':excursions}
    return render(request, 'excursions/excursion_details.html', context)