from locale import currency
from django.shortcuts import redirect, render
from django.contrib import messages
from cart.contexts import cart_contents
from django.conf import settings
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
                excursion_name = item['excursion'].title,
                user = request.user,
                full_name = request.POST['full_name'],
                image = item['excursion'].main_image.url,
                cellphone_number = request.POST['Phone_number'],
                price = item['values']['price'],
                subTotal = item['subTotal'],
                adult_qty = item['values']['adult_qty'],
                child_qty = item['values']['child_qty'],
                excursion_date = item['values']['excursion_date'],
                customer_email = request.user.email,
                place_pickup = item['values']['place_pickup'],
                date_created  = datetime.date.today()
        )
        return redirect('checkout-success')
    else:
        if not cart:
            messages.error(request, "There's nothing in your cart at the moment")
            return redirect('excursions')
    # process the payment     
    total = current_cart['total']
    stripe_total = round(total * 100)
    stripe.api_key =stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount = stripe_total,
        currency = settings.STRIPE_CURRENCY
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
       excursion_total += item.subTotal
    context = {'user_orders':user_orders, 'excursion_total':excursion_total}
    return render(request,'checkout/success.html', context )
