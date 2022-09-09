from django.shortcuts import render, redirect
from .models import Excursions, ExcursionExtraPhotos
from .forms import AddExcursionForm

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
