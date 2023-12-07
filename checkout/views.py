from locale import currency
from django.shortcuts import redirect, render
from django.contrib import messages
from cart.contexts import cart_contents, rental_cart_contents
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
import stripe
from .models import ExcursionOrder, AccommodationOrder
from .utils import send_booking_email, send_email_to_seller
from excursions.models import Reference
from django.contrib.auth.decorators import login_required
import datetime
from django.http import JsonResponse
import json
import time
from decimal import Decimal, ROUND_HALF_UP
# Create your views here.
from datetime import datetime as newTime


def apply_discount_code(request):
    discount_percentage = Decimal(settings.DISCOUNT_PERCENTAGE)
    new_total = 0.00
    total_discount = 0
    checkout_cart = request.session.get('checkout_cart', {})
    reference_applied = False
    if request.method == 'POST':
        discount_reference = request.POST.get('reference')
        extracted_reference = Reference.objects.filter(reference_number=discount_reference)
        if extracted_reference and not reference_applied:
            checkout_cart['reference'] = str(discount_reference)
            checkout_cart['discount_applied'] = True
            reference_applied = True 

            if checkout_cart['total']:
                original_total = Decimal(checkout_cart['total'])
                total_discount = original_total * discount_percentage
                new_total = Decimal(checkout_cart['total']) - Decimal(total_discount)
                messages.success(request, 'Discount has been applied')    
        else: 
            messages.error(request, 'The discount code is invalid. Please check the spelling.')
    checkout_cart['total_discount'] = str(total_discount)
    request.session['cart_total'] = str(new_total)
    request.session['checkout_cart'] = checkout_cart
    return redirect('checkout')



# @login_required(login_url='/accounts/login/' )
def checkout(request):
    checkout_cart = request.session.get('checkout_cart', {})
    # if the checkout total is 0 then go home
    if checkout_cart['total'] == '0':
        return redirect('home')
    
    cart = request.session.get('cart', {})

    if 'total_discount' in checkout_cart:
        total_discount = Decimal(checkout_cart['total_discount'])
    else:
        total_discount = Decimal(0)  # or some default value
    try:
        new_total = Decimal(checkout_cart['total']) - total_discount
    except KeyError:
         return redirect('excursions')
    discount_applied = checkout_cart['discount_applied']
    paypal_client_id = settings.PAYPAL_CLIENT_ID
    cart = request.session.get('cart', {})
    current_cart = cart_contents(request)
    # Create the orders
    if request.method == 'POST':
        # print('checkout_cart', checkout_cart)
        data = json.loads(request.body)
        print('email', data)

        reference = checkout_cart.get('reference', '')
        extracted_reference = Reference.objects.filter(reference_number=reference)
        # Add the item in the database
        if request.user.is_authenticated:
            user  = request.user
            guest_email = request.user.email
        else:
            user = None
            guest_email = data['email']

        for item in current_cart['cart_items']:
            date_str = item['values']['excursion_date']
            parsed_date = newTime.strptime(date_str, '%A, %d %B')
            # Get the current year
            current_year = newTime.now().year
            parsed_date = parsed_date.replace(year=current_year)
            # Format the date as "YYYY-MM-DD"
            formatted_date = parsed_date.strftime('%Y-%m-%d')

            ExcursionOrder.objects.create(
                excursion_name=item['excursion'].title,
                user=user,
                full_name=data['full_name'],
                image=item['excursion'].main_image.url,
                cellphone_number=data['phone_number'],
                price=item['values']['price'],
                subtotal=item['subTotal'],
                adult_qty=item['values']['adult_qty'],
                child_qty=item['values']['child_qty'],
                infant_qty = item['values']['infant_qty'],
                excursion_date=formatted_date,
                customer_email=guest_email,
                place_pickup=item['values']['place_pickup'],
                date_created=datetime.date.today(),
                reference=reference,
                time_selected = item['values']['selected_time'],
                excursion_id = int(item['excursion'].id),
            )
        # send an email with all the info to the user
        send_booking_email(request, guest_email)
        send_email_to_seller(request, extracted_reference, checkout_cart)
        
    context = {'paypal_client_id': paypal_client_id,
               'new_total': new_total,'total_discount': 
               total_discount, 'discount_applied':discount_applied

               }
    return render(request, 'checkout/checkout.html', context)


# Allow the user know that the purchase has been successful
def checkout_success(request):
     # Get the current user
    if request.user.is_authenticated:
        user = request.user 
        user_orders = ExcursionOrder.objects.all().filter(user=user)
        user_orders = user_orders.filter(date_created=datetime.date.today())
        excursion_total = sum(item.subtotal for item in user_orders)
    else:
        user_orders = []
         # An empty list for anonymous users
        excursion_total = 0
    context = {'user_orders': user_orders, 'excursion_total': excursion_total}
    return render(request, 'checkout/success.html', context)


# Chekout and process payment for rental cart
# @login_required(login_url='/accounts/login/')
def checkout_rental(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    rental_cart = request.session.get('rental_cart', {})
    current_cart = rental_cart_contents(request)
    # Create the order
    if request.method == 'POST':
        for item in current_cart['rental_cart_items']:
            AccommodationOrder.objects.create(
                rental_name=item['rental'].title,
                # user=request.user,
                full_name=request.POST['full_name'],
                image=item['rental'].main_image.url,
                price=item['values']['price'],
                adult_qty=item['values']['adult_qty'],
                child_qty=item['values']['child_qty'],
                check_in=item['values']['check_in'],
                checkout=item['values']['checkout'],
                customer_email=request.user.email,
                cellphone_number=request.POST['Phone_number'],
                rental_type=item['rental'].ACCOM_type,
                date_created=datetime.date.today(),
                subtotal=item['sub_total'],
            )
        # send an email with all the info to the user
        user_orders = AccommodationOrder.objects.all().filter(user=request.user)
        user_orders = user_orders.filter(date_created=datetime.date.today())
        rental_total = 0
        template = ''
        thanks_booking = "<h2 style='background-color:#f85a15; padding: 10px;  color:#ffffff;';>Thank you for booking with us</h2><hr>"
        subtitle = "<h3>Here are your bookings from today</h3>"
        template += thanks_booking + subtitle
        for item in user_orders:
            rental_total += item.subtotal
            template += f"<p><strong>Item Name:</strong>{item.rental_name[:25].title()}</p>"
            template += f"<img src='{item.image}' alt='{item.rental_name}' style='object-fit:cover' width='200' height='200'><br/>"
            template += f"<strong>Check-IN:</strong> {item.check_in}<br/>"
            template += f"<strong>Checkout:</strong> {item.checkout}<br/>"
            template += f"<strong>Adult Quantity:</strong> {item.adult_qty}<br/>"
            if item.child_qty:
                template += f"<strong>Child Quantity:</strong> {item.child_qty}<br/>"
            template += f"<strong>Rental type:</strong> {item.rental_type} <br/>"
            template += f"<strong>Rental Booking Number:</strong> {item.order_number} <br/>"
            template += f"<strong>SubTotal:</strong> {item.subtotal} <hr>"
        template += f"<strong style='background-color:#f85a15; padding: 10px; color:#ffffff;'>Amount Paid:</strong> £{rental_total} <hr>"
        email = EmailMultiAlternatives(
            'From Yara beach',
            template,
            settings.EMAIL_HOST_USER,
            [request.user.email]
        )
        email.attach_alternative(template, "text/html")
        email.fail_silently = False
        email.send()
        # Empty the cart when payment has been process
        request.session['rental_cart'] = {}
        return redirect('checkout-rental-success')
    else:
        if not rental_cart:
            messages.error(
                request, "There's nothing in your cart at the moment")
            return redirect('rentals')

       # process the payment
    rental_cart_total = current_cart['rental_cart_total']
    stripe_total = round(rental_cart_total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY
    )
    context = {
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, 'checkout/checkout_rental.html', context)


# Allow the user know that the purchase has been successful
@login_required(login_url='/accounts/login/')
def checkout_rental_success(request):
    user_orders = AccommodationOrder.objects.all().filter(user=request.user)
    user_orders = user_orders.filter(date_created=datetime.date.today())
    rental_total = 0
    for item in user_orders:
        rental_total += item.subtotal
    context = {'user_orders': user_orders, 'rental_total': rental_total}
    return render(request, 'checkout/rental_success.html', context)
