from locale import currency
from django.shortcuts import redirect, render
from django.contrib import messages
from cart.contexts import cart_contents
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
import stripe
from .models import ExcursionOrder
import datetime
# Create your views here.

# Chekout and process payment
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    cart = request.session.get('cart', {})
    current_cart = cart_contents(request)
    # Create the order
    if request.method == 'POST':
        for item in current_cart['cart_items']:
            ExcursionOrder.objects.create(
                excursion_name=item['excursion'].title,
                user=request.user,
                full_name=request.POST['full_name'],
                image=item['excursion'].main_image.url,
                cellphone_number=request.POST['Phone_number'],
                price=item['values']['price'],
                subtotal=item['subTotal'],
                adult_qty=item['values']['adult_qty'],
                child_qty=item['values']['child_qty'],
                excursion_date=item['values']['excursion_date'],
                customer_email=request.user.email,
                place_pickup=item['values']['place_pickup'],
                date_created=datetime.date.today()
            )

        # send an email with all the info to the user
        user_orders = ExcursionOrder.objects.all().filter(user=request.user)
        user_orders = user_orders.filter(date_created=datetime.date.today())
        excursion_total = 0
        template = ''
        thanks_booking = "<h2 style='background-color:#f85a15; padding: 10px;  color:#ffffff;';>Thank you for booking us</h2><hr>"
        subtitle = "<h3>Here are your bookings from today</h3>"
        template += thanks_booking + subtitle
        for item in user_orders:
            excursion_total += item.subtotal
            template += f"<p><strong>Item Name:</strong>{item.excursion_name[:25].title()}</p>"
            template += f"<img src='{item.image}' alt='{item.excursion_name}' style='object-fit:cover' width='200' height='200'><br/>"
            template += f"<strong>Excursion Date:</strong> {item.excursion_date}<br/>"
            template += f"<strong>Adult Quantity:</strong> {item.adult_qty}<br/>"
            if item.child_qty:
                template += f"<strong>Child Quantity:</strong> {item.child_qty}<br/>"
            template += f"<strong>Pick up:</strong> {item.place_pickup} <br/>"
            template += f"<strong>Excursion Booking Number:</strong> {item.order_number} <br/>"
            template += f"<strong>SubTotal:</strong> {item.subtotal} <hr>"
        template += f"<strong style='background-color:#f85a15; padding: 10px; color:#ffffff;'>Amount Paid:</strong> £{excursion_total} <hr>"
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
        request.session['cart'] = {}
        return redirect('checkout-success')
    else:
        if not cart:
            messages.error(
                request, "There's nothing in your cart at the moment")
            return redirect('excursions')
            
    # process the payment
    total = current_cart['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY
    )
    context = {
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, 'checkout/checkout.html', context)


# Allow the user know that the purchase has been successful
def checkout_success(request):
    user_orders = ExcursionOrder.objects.all().filter(user=request.user)
    user_orders = user_orders.filter(date_created=datetime.date.today())
    excursion_total = 0
    for item in user_orders:
        excursion_total += item.subtotal
    context = {'user_orders': user_orders, 'excursion_total': excursion_total}
    return render(request, 'checkout/success.html', context)




# Chekout and process payment for rental cart
def checkout_rental(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    rental_cart = request.session.get('rental_cart', {})
     # Create the order
    if request.method == 'POST':
        print('proccess form')
    else:
        if not rental_cart:
            messages.error(
                request, "There's nothing in your cart at the moment")
            return redirect('rentals')
    context = {
        'stripe_public_key': stripe_public_key,
        'client_secret': 'client_secret',
    }
    return render(request, 'checkout/checkout_rental.html', context)