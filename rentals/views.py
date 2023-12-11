from django.shortcuts import render, redirect
from .models import Rentals,Review
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
# Show all the rentals
def rentals(request):
    if not request.user.is_superuser:
        return redirect("excursions")
    counts = Rentals.objects.filter(status='Active').count()
    p = Paginator(Rentals.objects.filter(status='Active'), 8)
    page = request.GET.get('page')
    rentals = p.get_page(page)
    context = {'rentals': rentals,'counts': counts}
    return render(request, 'rentals/rentals.html', context)

# Show the rental details
def rental_details(request, slug):
    if not request.user.is_superuser:
        return redirect("excursions")
    rental = Rentals.objects.get(slug=slug)
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
    if not request.user.is_superuser:
        return redirect("excursions")
    rentals = Rentals.objects.filter(status='Active')
    navbar_input = request.GET.get('navbar')
    if navbar_input:
        rentals = Rentals.objects.filter(Q(title__icontains=navbar_input) | Q(description__icontains=navbar_input))
    context = {'rentals': rentals, 'navbar_input': navbar_input}
    return render(request,'rentals/input_search_result.html', context )


# filter from newest to oldest rentals
def newest_rentals(request):
    if not request.user.is_superuser:
        return redirect("excursions")
    counts = Rentals.objects.filter(status='Active').order_by('-date_created').count()
    p = Paginator(Rentals.objects.filter(status='Active').order_by('-date_created'), 8)
    page = request.GET.get('page')
    rentals = p.get_page(page)
    context = {'rentals': rentals, 'counts': counts}
    return render(request, 'rentals/filters.html', context )


# filter from oldest to newest rentals
def oldest_rentals(request):
    if not request.user.is_superuser:
        return redirect("excursions")
    counts = Rentals.objects.filter(status='Active').order_by('date_created').count()
    p = Paginator(Rentals.objects.filter(status='Active').order_by('date_created'), 8)
    page = request.GET.get('page')
    rentals = p.get_page(page)
    context = {'rentals': rentals, 'counts': counts}
    return render(request, 'rentals/filters.html', context )


# filter rentals from low price to high
def filter_by_price_ascend(request):
    if not request.user.is_superuser:
        return redirect("excursions")
    counts = Rentals.objects.filter(status='Active').order_by('Price').count()
    p = Paginator(Rentals.objects.filter(status='Active').order_by('Price'), 8)
    page = request.GET.get('page')
    rentals = p.get_page(page)
    context = {'rentals': rentals, 'counts': counts}
    return render(request,'rentals/filters.html', context)

# filter rentals from low price to high
def filter_by_price_descend(request):
    if not request.user.is_superuser:
        return redirect("excursions")
    counts = Rentals.objects.filter(status='Active').order_by('-Price').count()
    p = Paginator(Rentals.objects.filter(status='Active').order_by('-Price'), 8)
    page = request.GET.get('page')
    rentals = p.get_page(page)
    context = {'rentals': rentals, 'counts': counts}
    return render(request,'rentals/filters.html', context)

# filter by rooms
def filter_by_rooms(request):
    if not request.user.is_superuser:
        return redirect("excursions")
    counts = Rentals.objects.filter(status='Active').filter(ACCOM_type = 'Room').count()
    p = Paginator(Rentals.objects.filter(ACCOM_type = 'Room'), 8)
    page = request.GET.get('page')
    rentals = p.get_page(page)
    context = {'rentals': rentals, 'counts': counts}
    return render(request,'rentals/filters.html', context)

# filter by apartment
def filter_by_apartments(request):
    if not request.user.is_superuser:
        return redirect("excursions")
    counts = Rentals.objects.filter(status='Active').filter(ACCOM_type = 'Apartment').count()
    p = Paginator(Rentals.objects.filter(ACCOM_type = 'Apartment'), 8)
    page = request.GET.get('page')
    rentals = p.get_page(page)
    context = {'rentals': rentals, 'counts': counts}
    return render(request,'rentals/filters.html', context)

# filter by villas
def filter_by_villas(request):
    if not request.user.is_superuser:
        return redirect("excursions")
    counts = Rentals.objects.filter(status='Active').filter(ACCOM_type = 'Villa').count()
    p = Paginator(Rentals.objects.filter(status='Active').filter(ACCOM_type = 'Villa'), 8)
    page = request.GET.get('page')
    rentals = p.get_page(page)
    context = {'rentals': rentals, 'counts': counts}
    return render(request,'rentals/filters.html', context)