from django.shortcuts import render, redirect
from .models import Excursions, Photos,Review
from .forms import AddExcursionForm
from django.contrib import messages
from django.db.models import Q

# Create your views here.

# Show all the excursion
def excursion(request):
    excursions = Excursions.objects.all()
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

# Add the excursion
def add_excursions(request):
    form = AddExcursionForm()
    if request.method == 'POST':
        user = request.user
        author = Excursions(user=user)
        form = AddExcursionForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
        return redirect('excursions')
        
    context = {'form': form}
    return render(request, 'excursions/add_excursions_form.html', context)


# Search excursion in app
def input_search_result(request):
    excursions = Excursions.objects.all()
    navbar_input = request.GET.get('navbar')
    print(navbar_input)
    if navbar_input:
        excursions = Excursions.objects.filter(Q(title__icontains=navbar_input) | Q(description__icontains=navbar_input))
    context = {'excursions': excursions, 'navbar_input': navbar_input}
    return render(request,'excursions/input_search_result.html', context )

# filter from newest to oldest excursions
def newest_excursions(request):
    excursions = Excursions.objects.all().order_by('-date_created')
    context = {'excursions': excursions}
    return render(request, 'excursions/newest_excursions.html', context )

# filter from oldest to newest excursions
def oldest_excursions(request):
    excursions = Excursions.objects.all().order_by('date_created')
    content = {'excursions': excursions}
    return render(request, 'excursions/oldest_excursions.html', content )