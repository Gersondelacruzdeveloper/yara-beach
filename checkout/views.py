from locale import currency
from django.shortcuts import redirect, render
from django.contrib import messages
from cart.contexts import cart_contents, rental_cart_contents
from django.conf import settings
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
import stripe
from .models import ExcursionOrder, AccommodationOrder
from excursions.models import Reference
from django.contrib.auth.decorators import login_required
import datetime
from django.http import JsonResponse
import json
import time
import datetime
from decimal import Decimal, ROUND_HALF_UP
# Create your views here.
from decimal import Decimal


def apply_discount_code(request):
    discount_amount = 5
    cart = request.session.get('cart', {})
    new_total = 0.00
    checkout_cart = request.session.get('checkout_cart', {})
    total_discount = 0
    reference_applied = False
    if request.method == 'POST':
        discount_reference = request.POST.get('reference')
        extracted_reference = Reference.objects.filter(reference_number=discount_reference)
        if extracted_reference and not reference_applied:
            checkout_cart['reference'] = str(discount_reference)
            checkout_cart['discount_applied'] = True
            reference_applied = True  
            for id, value in cart.items():
                total_adult = int(value['adult_qty'])
                checkout_cart['total_adult'] = int(total_adult)
                total_discount += total_adult * discount_amount
            if checkout_cart['total']:
                new_total = Decimal(checkout_cart['total']) - Decimal(total_discount)
                messages.success(request, 'Discount has been applied')    
        else: 
            messages.error(request, 'The discount code is invalid. Please check the spelling.')
    checkout_cart['total_discount'] = total_discount
    request.session['cart_total'] = str(new_total)
    request.session['checkout_cart'] = checkout_cart
    return redirect('checkout')

@login_required(login_url='/accounts/login/' )
def checkout(request):
    checkout_cart = request.session.get('checkout_cart', {})
    total_discount =  Decimal(checkout_cart['total_discount'])
    new_total = Decimal(checkout_cart['total']) - total_discount
    discount_applied = checkout_cart['discount_applied']
    paypal_client_id = settings.PAYPAL_CLIENT_ID
    cart = request.session.get('cart', {})
    current_cart = cart_contents(request)
    # Create the orders
    if request.method == 'POST':
        # print('checkout_cart', checkout_cart)
        data = json.loads(request.body)
        reference = checkout_cart['reference']
        extracted_reference = Reference.objects.filter(reference_number=reference) or ''
        # Add the item in the database
        for item in current_cart['cart_items']:

            ExcursionOrder.objects.create(
                excursion_name=item['excursion'].title,
                user=request.user,
                full_name=data['full_name'],
                image=item['excursion'].main_image.url,
                cellphone_number=data['phone_number'],
                price=item['values']['price'],
                subtotal=item['subTotal'],
                adult_qty=item['values']['adult_qty'],
                child_qty=item['values']['child_qty'],
                infant_qty = item['values']['infant_qty'],
                excursion_date=item['values']['excursion_date'],
                customer_email=request.user.email,
                place_pickup=item['values']['place_pickup'],
                date_created=datetime.date.today(),
                reference=reference,
                time_selected = item['values']['selected_time'],
            )
        # send an email with all the info to the user
        user_orders = ExcursionOrder.objects.all().filter(user=request.user)
        user_orders = user_orders.filter(date_created=datetime.date.today())
        excursion_total = 0
        template = ''
        thanks_booking = "<h2 style='background-color:#f85a15; padding: 10px;  color:#ffffff;';>Thank you for booking with us</h2><hr>"
        subtitle = "<h3>Here are your bookings from today</h3>"
        template += thanks_booking + subtitle
        for item in user_orders:
            excursion_total += item.subtotal
            template += f"<p><strong>Item Name:</strong>{item.excursion_name[:25].title()}</p>"
            template += f"<img src='{item.image}' alt='{item.excursion_name}' style='object-fit:cover' width='200' height='200'><br/>"
            template += f"<strong>Excursion Date:</strong> {item.excursion_date}<br/>"
            print('here 1')
            template += f"<strong>Excursion Time:</strong> {item.time_selected}<br/>"
            print('here 2')
            template += f"<strong>Adult Quantity:</strong> {item.adult_qty}<br/>"
            if item.child_qty:
                template += f"<strong>Child Quantity:</strong> {item.child_qty}<br/>"
            if item.infant_qty:
                template += f"<strong>Child Quantity:</strong> {item.infant_qty}<br/>"
            template += f"<strong>Pick up:</strong> {item.place_pickup} <br/>"
            template += f"<strong>Excursion Booking Number:</strong> {item.order_number} <br/>"
            template += f"<strong>SubTotal:</strong> {item.subtotal} <hr>"
        template += f"<strong style='background-color:#f85a15; padding: 10px; color:#ffffff;'>Amount Paid:</strong> £{excursion_total} <hr>"
        email = EmailMultiAlternatives(
            'From Punta cana Explore',
            template,
            settings.EMAIL_HOST_USER,
            [request.user.email,'puntacanaexploregt@gmail.com']
        )
        email.attach_alternative(template, "text/html")
        email.fail_silently = False
        email.send()
        # send email for the seller imforming that the sell has gone throgh
        template_for_seller = ''
        if extracted_reference:
            for e in extracted_reference:
                e.due_to_pay_amount += checkout_cart['total_adult'] * 10
                e.paid_amount += checkout_cart['total_adult'] * 10
                e.save() 
                template_for_seller += f"<h2 style='background-color:#f85a15; padding: 10px;  color:#ffffff;';>¡Felicidades, {e.full_name}!</h2><hr>"
                template_for_seller += f"<p>Queríamos informarte que has ganado ${e.due_to_pay_amount} por la venta exitosa de excursión. Tu arduo trabajo está dando frutos.</p>"
                template_for_seller += f"<p>El dinero estará en tu cuenta ******{e.account_number[-4:]} en menos de 4 días, a menos que el cliente cancele la reserva.</p>"
                template_for_seller += f"<p>¡Sigue así!</p>"
                template_for_seller += f"<p>Saludos</p>"
                template_for_seller += f"<p>Punta Cana Explore</p>"
                email = EmailMultiAlternatives(
                'From Punta cana Explore for sellers',
                template_for_seller,
                settings.EMAIL_HOST_USER,
                [e.email]
                )
                email.attach_alternative(template_for_seller, "text/html")
                email.fail_silently = False
                email.send()
        # Empty the cart when payment has been process
        request.session['cart'] = {}
        return redirect('checkout-success')
    else:
        if not cart:
            return redirect('excursions')

    context = {'paypal_client_id': paypal_client_id,
               'new_total': new_total,'total_discount': 
               total_discount, 'discount_applied':discount_applied

               }
    return render(request, 'checkout/checkout.html', context)


# Allow the user know that the purchase has been successful
@login_required(login_url='/accounts/login/')
def checkout_success(request):
    user_orders = ExcursionOrder.objects.all().filter(user=request.user)
    user_orders = user_orders.filter(date_created=datetime.date.today())
    excursion_total = 0
    for item in user_orders:
        excursion_total += item.subtotal
    context = {'user_orders': user_orders, 'excursion_total': excursion_total}
    return render(request, 'checkout/success.html', context)


# Chekout and process payment for rental cart
@login_required(login_url='/accounts/login/')
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
                user=request.user,
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
