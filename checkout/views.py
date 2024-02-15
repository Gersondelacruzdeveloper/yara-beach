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
from django.http import JsonResponse
from django.http import HttpResponse


def apply_discount_code(request):
    discount_percentage = Decimal(settings.DISCOUNT_PERCENTAGE)
    checkout_cart = request.session.get('checkout_cart', {})
    checkout_cart['discount'] = str(Decimal(0.00))
    checkout_cart['my_new_total'] = str(Decimal(0.00))
    reference_applied = False
    current_cart = cart_contents(request)

    if request.method == 'POST':
        discount_reference = request.POST.get('reference')
        extracted_reference = Reference.objects.filter(reference_number=discount_reference)
        if extracted_reference:
            checkout_cart['discount'] = str(Decimal(current_cart['m_total']) * Decimal(discount_percentage))
            checkout_cart['my_new_total'] = str(Decimal(current_cart['m_total']) - Decimal(checkout_cart['discount']))
            request.session['checkout_cart'] = checkout_cart
        else:
            messages.error(request, 'The discount code is invalid. Please check the spelling.')
    request.session['checkout_cart'] = checkout_cart
    return redirect('checkout')



# @login_required(login_url='/accounts/login/' )
def checkout(request):
    cart = request.session.get('cart', {})
    stripe_pk = settings.STRIPE_PUBLIC_KEY
    if not cart:
        return redirect('home')
    customer_contact = request.session.get('customer_contact', {})
    if request.method == 'POST':
        email=request.POST['email']
        name = request.POST['name']
        phone = request.POST['phone']
        customer_contact['name'] = name
        customer_contact['email'] = email
        customer_contact['phone'] = phone
    request.session['customer_contact'] = customer_contact
    context = {  'carts':cart, 'customer_contact':customer_contact, 'stripe_pk':stripe_pk}
    return render(request, 'checkout/checkout.html', context)


def stripe_checkout(request):
    # This is your test secret API key.
    stripe.api_key = settings.STRIPE_SECRET_KEY
    cart_content = cart_contents(request)
    anticipo = round(cart_content['anticipo'])
    try:
        # load json data
        data = json.loads(request.body)
        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount=anticipo * 100,
            currency='usd',
            automatic_payment_methods={
                'enabled': True,
            },
        )
        return JsonResponse({'clientSecret': intent.client_secret})
    except Exception as e:
        print('here error', str(e))
        return JsonResponse({'error': str(e)}, status=500)



# Allow the user know that the purchase has been successful
def checkout_success(request):
    # Get the current user
    stripe.api_key = settings.STRIPE_SECRET_KEY
    payment_intent = request.GET['payment_intent']
    response = stripe.PaymentIntent.retrieve(payment_intent)
    if response.status == 'succeeded':
        customer_contact = request.session.get('customer_contact', {})
        order_number = response.id 
        cart_content = cart_contents(request)
        anticipo = cart_content['anticipo']
        company_price_total = cart_content['company_price_total']

        
        for item in cart_content['cart_items']:
                date_str = item['values']['excursion_date']
                format_string = '%m/%d/%Y' 
                parsed_date = newTime.strptime(date_str, format_string)

                ExcursionOrder.objects.create(
                    excursion_name=item['excursion'].title,
                    user= None,
                    order_number = order_number, 
                    full_name= customer_contact['name'],
                    image=item['excursion'].main_image.url,
                    cellphone_number= customer_contact['phone'],
                    price=item['values']['price'],
                    subtotal=item['subTotal'],
                    adult_qty=item['values']['adult_qty'],
                    child_qty=item['values']['child_qty'],
                    infant_qty = item['values']['infant_qty'],
                    excursion_date=parsed_date,
                    customer_email=customer_contact['email'],
                    place_pickup=item['values']['place_pickup'],
                    place_dropup = item['values']['place_dropup'] or '',
                    date_created=datetime.date.today(),
                    reference= '',
                    time_selected = item['values']['selected_time'],
                    excursion_id = int(item['excursion'].id),
                    advanced = anticipo,
                    remaining = company_price_total,
                )
                # send an email with all the info to the user
                send_booking_email(cart_content, order_number,company_price_total, round(anticipo, 2), customer_contact['email'])

    # delete the cart 
    cart = request.session.get('cart', {})
    if cart:
        cart.popitem()
        # After modifying the dictionary, you might want to update the session
    request.session['cart'] = cart
    # If you want to set cart_content to an empty list, you can do that separately
    cart_content = []
    # du to stripe adding the amount in cents we have to multiply again to make it look normal for the customers
    context = {'order_number': order_number, 'Anticipo': response.amount/100}
    return render(request, 'checkout/success.html', context)

def checkout_no_pay(request):
        cart_content = cart_contents(request)
        anticipo = cart_content['anticipo']
        company_price_total = cart_content['company_price_total']
        customer_contact = request.session.get('customer_contact', {})
           
        for item in cart_content['cart_items']:
                date_str = item['values']['excursion_date']
                format_string = '%m/%d/%Y' 
                parsed_date = newTime.strptime(date_str, format_string)

                ExcursionOrder.objects.create(
                    excursion_name=item['excursion'].title,
                    user= None,
                    full_name= customer_contact['name'],
                    image=item['excursion'].main_image.url,
                    cellphone_number= customer_contact['phone'],
                    price=item['values']['price'],
                    subtotal=item['subTotal'],
                    adult_qty=item['values']['adult_qty'],
                    child_qty=item['values']['child_qty'],
                    infant_qty = item['values']['infant_qty'],
                    excursion_date=parsed_date,
                    customer_email=customer_contact['email'],
                    place_pickup=item['values']['place_pickup'],
                    place_dropup = item['values']['place_dropup'] or '',
                    date_created=datetime.date.today(),
                    reference= '',
                    time_selected = item['values']['selected_time'],
                    excursion_id = int(item['excursion'].id),
                    advanced = 0,
                    remaining = cart_content['final_total'],
                )
                # send an email with all the info to the user
                send_booking_email(cart_content, '92T76B672934A63A7AECB420D6D8CA4',cart_content['final_total'], round(0), customer_contact['email'])

    # delete the cart 
        cart = request.session.get('cart', {})
        if cart:
            cart.popitem()
            # After modifying the dictionary, you might want to update the session
        request.session['cart'] = cart
        # If you want to set cart_content to an empty list, you can do that separately
        cart_content = []
        # du to stripe adding the amount in cents we have to multiply again to make it look normal for the customers
        context = {'order_number': '92T76B672934A63A7AECB420D6D8CA4', 'Anticipo': 0}
        return render(request, 'checkout/success.html', context)



def clear_customers_info(request):
    try:
        request.session['customer_contact'] = {}
    except KeyError:
        print('erroir occur')
    return redirect('checkout')

# Chekout and process payment for rental cart
# @login_required(login_url='/accounts/login/')
def checkout_rental(request):
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

    context = {}
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
