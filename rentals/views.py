from django.shortcuts import render
from .models import Rentals,Review
from django.contrib import messages
from django.db.models import Q

# Create your views here.

# Show all the rentals
def rentals(request):
    rental = Rentals.objects.all()
    context = {'rentals': rental}
    return render(request, 'rentals/rentals.html', context)


# Show the rental details
def rental_details(request, pk):
    rental = Rentals.objects.get(id=pk)
    context = {'rentals': rental}

    # create review 
    if request.method == 'POST':
        Review.objects.create(
            content=request.POST['review-content'],
            title = request.POST['review-title'],
            rating = request.POST.get('star', 1),
            rental=rental,
            user=request.user,
        )
        messages.success(request, 'Your review has been published.')

    return render(request, 'rentals/rental_details.html', context)


# Search excursion in app
def input_search_result(request):
    rentals = Rentals.objects.all()
    navbar_input = request.GET.get('navbar')
    if navbar_input:
        rentals = Rentals.objects.filter(Q(title__icontains=navbar_input) | Q(description__icontains=navbar_input))
    context = {'rentals': rentals, 'navbar_input': navbar_input}
    return render(request,'rentals/input_search_result.html', context )