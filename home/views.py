from django.shortcuts import redirect, render
from excursions.models import Excursions
from rentals.models import Rentals
from django.shortcuts import render
from excursions.models import Excursions
from rentals.models import Rentals
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage
from checkout.models import ExcursionOrder
import datetime
# Create your views here.

# show excursions and rentals in home page


def home(request):
    excursions = Excursions.objects.all()[:4]
    rentals = Rentals.objects.all()[:4]
    context = {'excursions': excursions, 'rentals': rentals}
    return render(request, 'home/home.html', context)

# show excursions and rentals in home page


def home(request):
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


# Show  all the customer bookings
def customer_bookings(request):
    # Excursion queries
    user_orders = ExcursionOrder.objects.all().filter(user=request.user)
    print('user_orders', user_orders)
    # today bookins
    today_excursion_bookings = user_orders.filter(
        excursion_date=datetime.date.today())
    print('today', today_excursion_bookings)
    # future bookings
    future_excursion_bookings = user_orders.filter(
        excursion_date__gte=datetime.date.today())

    print('future', future_excursion_bookings)
    # pass bookings
    previous_excursion_bookings = user_orders.filter(
        excursion_date__lte=datetime.date.today())

    print('previous', previous_excursion_bookings)

    context = {'today_excursion_bookings': today_excursion_bookings,
               'future_excursion_bookings': future_excursion_bookings,
               'previous_excursion_bookings': previous_excursion_bookings}
    return render(request, 'home/customer_booking.html', context)

