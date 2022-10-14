from locale import currency
from django.shortcuts import redirect, render
from django.contrib import messages
from cart.contexts import cart_contents
from django.conf import settings
import stripe
# Create your views here.

# return the cart page
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect('excursions')

    current_cart = cart_contents(request)
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