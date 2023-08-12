from django.shortcuts import render, redirect
from .models import Excursions, Photos, Review
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import ReferenceForm
from decimal import Decimal
# import qrcode
# Create your views here.
# def make_barcode():
#     website_url = "https://www.puntacana-explore.com/excursions/"  # Replace with your actual website URL

#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4,
#      )
#     qr.add_data(website_url)
#     qr.make(fit=True)

#     img = qr.make_image(fill_color="black", back_color="white")
#     img.save("website_qrcode.png")  # Save the QR code as an image



# Show all the excursion
def excursion(request):
    counts = Excursions.objects.filter(status='Active').count()
    p = Paginator(Excursions.objects.filter(status='Active'), 8)
    klk = 'this is gerson'
    page = request.GET.get('page')
    excursions = p.get_page(page)
    context = {'excursions': excursions,'counts': counts, 'klk':klk}
    return render(request, 'excursions/excursions.html', context)

# Show the excursion details
def excursion_details(request, pk):
    excursion = Excursions.objects.get(id=pk)
    context = {'excursions': excursion}
    # make_barcode()

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
    p = Paginator(Excursions.objects.filter(status='Active').order_by('-date_created'), 8)
    page = request.GET.get('page')
    excursions = p.get_page(page)
    context = {'excursions': excursions,'counts': counts}
    return render(request, 'excursions/filters.html', context )


# filter from oldest to newest excursions
def oldest_excursions(request):
    counts = Excursions.objects.filter(status='Active').order_by('date_created').count()
    p = Paginator(Excursions.objects.filter(status='Active').order_by('date_created'), 8)
    page = request.GET.get('page')
    excursions = p.get_page(page)
    context = {'excursions': excursions,'counts': counts}
    return render(request, 'excursions/filters.html', context )

# filter excursions from low price to high
def filter_by_price_ascend(request):
    counts = Excursions.objects.filter(status='Active').order_by('Price').count()
    p = Paginator(Excursions.objects.filter(status='Active').order_by('Price'), 8)
    page = request.GET.get('page')
    excursions = p.get_page(page)
    context = {'excursions': excursions,'counts': counts}
    return render(request,'excursions/filters.html', context)

# filter excursions from high price to low
def filter_by_price_descend(request):
    counts = Excursions.objects.filter(status='Active').order_by('-Price').count()
    p = Paginator(Excursions.objects.filter(status='Active').order_by('-Price'), 8)
    page = request.GET.get('page')
    excursions = p.get_page(page)
    context = {'excursions': excursions,'counts': counts}
    return render(request,'excursions/filters.html', context)
    
# cart function
def cart(request):
    context = {}
    return render(request, 'excursions/cart.html', context)


def create_reference(request):
    if request.method == 'POST':
        form = ReferenceForm(request.POST)
        if form.is_valid():
            reference = form.save()
            return redirect('success_page', reference_number=reference.reference_number)
    else:
        form = ReferenceForm()
    return render(request, 'excursions/reference_form.html', {'form': form})

def success_page(request, reference_number):
    return render(request, 'excursions/success_page.html', {'reference_number': reference_number})
