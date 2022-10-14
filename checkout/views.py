from django.shortcuts import redirect, render
from django.contrib import messages
# Create your views here.

# return the cart page
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect('excursions')
    
    context = {
        'stripe_public_key': 'pk_test_51LsX2bBFqdL0Ka0uBMY3tRh7VxHDOj8KBkKmhbZLHQnyF9Uobngt07yrulCqWVG1sgffi1VwKcjUPcgRKllhruer00X74q4GDr',
        'client_secret': 'test client secret',
    }
    return render(request, 'checkout/checkout.html', context)