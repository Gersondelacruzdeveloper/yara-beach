from django.shortcuts import render

# Create your views here.

# return the cart page
def checkout(request):
    return render(request, 'checkout/checkout.html')