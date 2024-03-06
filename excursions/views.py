from django.shortcuts import render, redirect
from .models import Excursions, Photos, Review
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import ReferenceForm
from decimal import Decimal
from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.contrib.auth.models import User
from datetime import timedelta, datetime
import random
from datetime import timedelta, datetime
from administrator.models import Post
from django.core.exceptions import ValidationError

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


from django.shortcuts import render
from .models import PageVisit



# Show all the excursion
def excursion(request):
    counts = Excursions.objects.filter(status='Active').count()
    p = Paginator(Excursions.objects.filter(status='Active').order_by('Price'), 8)
    page = request.GET.get('page')
    excursions = p.get_page(page)
    context = {'excursions': excursions,'counts': counts}
    return render(request, 'excursions/excursions.html', context)

# Show the excursion details
def excursion_details(request, slugy):
    excursion = get_object_or_404(Excursions, slugy=slugy)
    time_available = excursion.available_times.all()
    unavailable_days = excursion.unavailable_days.all()
    unavailableDay = []
    for i in unavailable_days:
        unavailableDay.append(i.day_number)
    context = {'excursions': excursion,'time_available':time_available, 'unavailableDay':unavailableDay}

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


# generate reviews
def generate_reviews(request, pk):
    if request.user.is_superuser and request.method == 'POST':
        excursion = get_object_or_404(Excursions, id=pk)
        reviews_content = request.POST.get('reviews_content')
        if reviews_content is not None:
            reviews = [item.strip() for item in reviews_content.split('*')]
            users = User.objects.filter(last_name='generated')

            for review in reviews:
                # Set a character limit for the title
                max_title_length = 50
                if len(review) > max_title_length:
                    # Find the last space character within the limit
                    last_space_index = review.rfind(' ', 0, max_title_length)
                    if last_space_index != -1:
                        title = review[:last_space_index]
                    else:
                        # If no space character found, just truncate at the character limit
                        title = review[:max_title_length]
                else:
                    title = review

                content = review
                rating = 5

                # Generate a random past date within the last 30 days
                today = datetime.now()
                past_date = today - timedelta(days=random.randint(1, 30))

                # Shuffle the list of users to select a random user who hasn't posted yet
                unused_users = [user for user in users if not Review.objects.filter(title=title, user=user).exists()]
                if unused_users:
                    selected_user = random.choice(unused_users)
                    Review.objects.create(rating=rating, title=title, content=content, excursion=excursion, user=selected_user, created=past_date)

        return redirect('home')




   # if not Review.objects.filter(title=title).exists():
    #             password = username + username
    #             email = f"{username}@example.com"
    #             User.objects.create_user(username=username, password=password, email=email, last_name='generated')
    #     messages.success(request, 'Users have been created')
    # list_of_users = []
    # for i in users:
    #     list_of_users.append(i)
    # print('list_of_users', list_of_users)
    # if not Review.objects.filter(title=title).exists():
    #     reviews = Review(tile=title[i],content=reviews_content[i], rating=5, excursion=excursion, user=user[i])
    #     reviews.save()


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
        excursions = excursions.filter(Q(title__icontains=navbar_input) | Q(description__icontains=navbar_input))
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

def cancel_excursion(request, pk):
    new = 'calceled'
    print('new', new, pk)
    context= {'new':new}
    return 


# Show the excursion details
def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post}
    print('yes it works', post)
    return render(request, 'administrator/post.html', context)