from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.

# return the cart page
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect('excursions')

    return render(request, 'checkout/checkout.html')