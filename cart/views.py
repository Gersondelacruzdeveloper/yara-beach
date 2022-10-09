from django.shortcuts import render, redirect

# Create your views here.


# return the cart page
def view_cart(request):
    return render(request, 'cart/cart.html')

# Add a quantity of the specified product to the shopping cart
def add_to_cart(request, item_id):
    excursion_date = request.POST.get('excursion_date')
    adult_qty = int(request.POST.get('adult_qty'))
    child_qty = int(request.POST.get('child_qty'))
    place_pickup = request.POST.get('place_pickup')
    redirect_url = request.POST.get("redirect_url")
    price = request.POST.get("price")
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += {'adult_qty': adult_qty, 'excursion_date': excursion_date,
                          'child_qty': child_qty, 'place_pickup': place_pickup, 'price': price}
    else:
        cart[item_id] = {'adult_qty': adult_qty,  'excursion_date': excursion_date,
                         'child_qty': child_qty, 'place_pickup': place_pickup, 'price': price}

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)