from django.shortcuts import render
from .models import Rentals,Review
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
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


# Search rentals in app
def input_search_result(request):
    rentals = Rentals.objects.all()
    navbar_input = request.GET.get('navbar')
    if navbar_input:
        rentals = Rentals.objects.filter(Q(title__icontains=navbar_input) | Q(description__icontains=navbar_input))
    context = {'rentals': rentals, 'navbar_input': navbar_input}
    return render(request,'rentals/input_search_result.html', context )


# filter from newest to oldest rentals
def newest_rentals(request):
    counts = Rentals.objects.all().order_by('-date_created').count()
    p = Paginator(Rentals.objects.all().order_by('-date_created'), 1)
    page = request.GET.get('page')
    rentals = p.get_page(page)
    context = {'rentals': rentals, 'counts': counts}
    return render(request, 'rentals/filters.html', context )


# filter from oldest to newest rentals
def oldest_rentals(request):
    rentals = Rentals.objects.all().order_by('date_created')
    content = {'rentals': rentals}
    return render(request, 'rentals/filters.html', content )


# filter rentals from low price to high
def filter_by_price_ascend(request):
    rentals = Rentals.objects.all().order_by('Price')
    contex = {'rentals':rentals}
    return render(request,'rentals/filters.html', contex)

# filter rentals from low price to high
def filter_by_price_descend(request):
    rentals = Rentals.objects.all().order_by('-Price')
    contex = {'rentals':rentals}
    return render(request,'rentals/filters.html', contex)

# filter by rooms
def filter_by_rooms(request):
    rentals = Rentals.objects.filter(ACCOM_type = 'Room')
    contex = {'rentals':rentals}
    return render(request,'rentals/filters.html', contex)

# filter by apartment
def filter_by_apartments(request):
    rentals = Rentals.objects.filter(ACCOM_type = 'Apartment')
    contex = {'rentals':rentals}
    return render(request,'rentals/filters.html', contex)

# filter by villas
def filter_by_villas(request):
    rentals = Rentals.objects.filter(ACCOM_type = 'Villa')
    contex = {'rentals':rentals}
    return render(request,'rentals/filters.html', contex)