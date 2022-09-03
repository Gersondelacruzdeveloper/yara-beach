from django.shortcuts import render

# Create your views here.

def excursion(request):
    return render(request, 'excursions/excursions.html')