from django.shortcuts import render

# Create your views here.

def rentals(request):
    return render(request, 'rentals/rentals.html')