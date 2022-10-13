from django.shortcuts import HttpResponse, render, redirect
from django.contrib import messages

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

# if the item id is already on the cart then it update it
    if item_id in list(cart.keys()):
        if 'adult_qty' in cart[item_id].keys():
            cart[item_id]['adult_qty'] = adult_qty

        if 'child_qty' in cart[item_id].keys():
            cart[item_id]['child_qty'] = child_qty

        if 'place_pickup' in cart[item_id].keys():
            cart[item_id]['place_pickup'] = place_pickup

        if 'excursion_date' in cart[item_id].keys():
            cart[item_id]['excursion_date'] = excursion_date

        if 'price' in cart[item_id].keys():
            cart[item_id]['price'] = price
        messages.success(request, 'You already added this item so we just updated')
    else:
        # if the item id is not in  the cart it will add a new one
        cart[item_id] = {'adult_qty': adult_qty,  'excursion_date': excursion_date,
                         'child_qty': child_qty, 'place_pickup': place_pickup, 'price': price}
        messages.success(request, 'Item added to cart Succesfullly')

    request.session['cart'] = cart
    return redirect(redirect_url)


# Update the child and adult quantity from cart
def update_cart(request, item_id):
    redirect_url = request.POST.get('redirect_url')
    adult_qty = request.POST.get('cart-adult_qty')
    child_qty = request.POST.get('cart-child_qty')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        if 'adult_qty' in cart[item_id].keys():
            cart[item_id]['adult_qty'] = adult_qty

        if 'child_qty' in cart[item_id].keys():
            cart[item_id]['child_qty'] = child_qty
    request.session['cart'] = cart
    messages.success(request, 'Cart item Updated Succesfullly')
    return redirect(redirect_url)


# Remove the item from the shopping cart
def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})

    try:
        if item_id in list(cart.keys()):
         cart.pop(item_id)
         request.session['cart'] = cart
         messages.success(request, 'Cart item deleted Succesfullly')
         return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
