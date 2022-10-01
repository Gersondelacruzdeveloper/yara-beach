from django.shortcuts import render, redirect
from .models import Excursions, Photos, Review
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

# Show all the excursion
def excursion(request):
    excursions = Excursions.objects.filter(status='Active')
    context = {'excursions': excursions}
    return render(request, 'excursions/excursions.html', context)

# Show the excursion details
def excursion_details(request, pk):
    excursion = Excursions.objects.get(id=pk)
    context = {'excursions': excursion}

    # create review 
    if request.method == 'POST':
        Review.objects.create(
            content=request.POST['review-content'],
            title = request.POST['review-title'],
            rating = request.POST.get('star', 1),
            excursion=excursion,
            user=request.user,
        )
        messages.success(request, 'Your review has been published.')

    return render(request, 'excursions/excursion_details.html', context)

# Add more images to the excursion 
def excursion_images(request, pk):
    excursion = Excursions.objects.get(id=pk)
    context = {'excursions': excursion}
    return render(request, 'excursions/add_more_photos.html', context)


# Search excursion in app
def input_search_result(request):
    excursions = Excursions.objects.filter(status='Active')
    navbar_input = request.GET.get('navbar')
    if navbar_input:
        excursions = Excursions.objects.filter(Q(title__icontains=navbar_input) | Q(description__icontains=navbar_input))
    context = {'excursions': excursions, 'navbar_input': navbar_input}
    return render(request,'excursions/input_search_result.html', context )

# filter from newest to oldest excursions
def newest_excursions(request):
    counts = Excursions.objects.filter(status='Active').order_by('-date_created').count()
    p = Paginator(Excursions.objects.filter(status='Active').order_by('-date_created'), 2)
    page = request.GET.get('page')
    excursions = p.get_page(page)
    context = {'excursions': excursions,'counts': counts}
    return render(request, 'excursions/filters.html', context )


# filter from oldest to newest excursions
def oldest_excursions(request):
    counts = Excursions.objects.filter(status='Active').order_by('date_created').count()
    p = Paginator(Excursions.objects.filter(status='Active').order_by('date_created'), 2)
    page = request.GET.get('page')
    excursions = p.get_page(page)
    context = {'excursions': excursions,'counts': counts}
    return render(request, 'excursions/filters.html', context )

# filter excursions from low price to high
def filter_by_price_ascend(request):
    counts = Excursions.objects.filter(status='Active').order_by('Price').count()
    p = Paginator(Excursions.objects.filter(status='Active').order_by('Price'), 2)
    page = request.GET.get('page')
    excursions = p.get_page(page)
    context = {'excursions': excursions,'counts': counts}
    return render(request,'excursions/filters.html', context)

# filter excursions from high price to low
def filter_by_price_descend(request):
    counts = Excursions.objects.filter(status='Active').order_by('-Price').count()
    p = Paginator(Excursions.objects.filter(status='Active').order_by('-Price'), 2)
    page = request.GET.get('page')
    excursions = p.get_page(page)
    context = {'excursions': excursions,'counts': counts}
    return render(request,'excursions/filters.html', context)
    
# cart function
def cart(request):
    context = {}
    return render(request, 'excursions/cart.html', context)
