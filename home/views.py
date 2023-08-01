from django.shortcuts import redirect, render
from excursions.models import Excursions
from rentals.models import Rentals
from django.shortcuts import render
from excursions.models import Excursions
from rentals.models import Rentals
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage
from checkout.models import ExcursionOrder, AccommodationOrder
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.


# show excursions and rentals in home page
def home(request):
    if not request.user.is_superuser:
        return redirect("excursions")
    excursions = Excursions.objects.all()[:4]
    rentals = Rentals.objects.all()[:4]
    context = {'excursions': excursions, 'rentals': rentals}
    return render(request, 'home/home.html', context)


# Contact form
def contact(request):
    if request.method == 'POST':
        template = render_to_string('home/email_templates.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['gersondelacruzdeveloper@gmail.com']
        )

        email.fail_silently = False
        email.send()
        return redirect('comfirmation')
    return render(request, 'home/contact.html')


# email comfirmation  for user
def email_comfirmation_page(request):
    return render(request, 'home/email_comfirmation.html')


# if the page does not exist will through a 404 error
def page_not_found(request, exception):
    return render(request, 'home/404.html', status=404)


# The 500 (server error)
def server_error(request):
    return render(request, 'home/500.html', status=500)


# Show  all the customer bookings
@login_required(login_url='/accounts/login/')
def customer_bookings(request):
    # Excursion queries
    user_orders = ExcursionOrder.objects.all().filter(user=request.user)
    # today bookins
    today_excursion_bookings = user_orders.filter(
        excursion_date=datetime.date.today())
    # future bookings
    future_excursion_bookings = user_orders.filter(
        excursion_date__gte=datetime.date.today())
    # pass bookings
    previous_excursion_bookings = user_orders.filter(
        excursion_date__lte=datetime.date.today())

    context = {'today_excursion_bookings': today_excursion_bookings,
               'future_excursion_bookings': future_excursion_bookings,
               'previous_excursion_bookings': previous_excursion_bookings}
    return render(request, 'home/customer_booking.html', context)


# Show  all the customer bookings
@login_required(login_url='/accounts/login/')
def customer_rental_bookings(request):
    # rental queries
    user_orders = AccommodationOrder.objects.all().filter(user=request.user)
    # today bookins
    today_rental_bookings = user_orders.filter(
        check_in=datetime.date.today())
    # future bookings
    future_rental_bookings = user_orders.filter(
        check_in__gte=datetime.date.today())
    # pass bookings
    previous_rental_bookings = user_orders.filter(
        check_in__lte=datetime.date.today())

    context = {'today_rental_bookings': today_rental_bookings,
               'future_rental_bookings': future_rental_bookings,
               'previous_rental_bookings': previous_rental_bookings}
    return render(request, 'home/customer_rental_booking.html', context)
