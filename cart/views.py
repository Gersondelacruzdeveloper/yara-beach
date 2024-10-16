from django.shortcuts import HttpResponse, render, redirect
from django.contrib import messages
from .utils import take_date_from_str, num_of_days
from datetime import date
from django.core.exceptions import ValidationError
from excursions.models import Excursions
from django.urls import reverse
from datetime import datetime

# ----------------------------------Excursion cart fucntionality 
# return the excursion cart page
def view_excursion_cart(request):
    # Get the previous page from the session, defaulting to an empty string
    previous_page = request.session.get('previous_page', '')
    # Store the current page's URL in the session
    request.session['previous_page'] = request.get_full_path()
    print('previous_page', previous_page)
    #   next_url = request.get_full_path()
    #     return redirect(f'/accounts/login/?next={next_url}')
    return render(request, 'cart/excursions_cart.html')

# Add a quantity of the specified product to the shopping excursion cart
def add_to_cart(request, item_id):
    excursion_date = request.POST.get('excursion_date')
    selected_time = request.POST.get('selected_time')
    adult_qty = int(request.POST.get('adult_qty'))
    print('adult_qty', adult_qty)

    try:
        child_qty = int(request.POST.get('child_qty'))
        infant_qty = int(request.POST.get('infant_qty'))
        place_dropup = request.POST.get('place_dropup')
    except TypeError:
        child_qty = 0
        infant_qty = 0
        place_dropup = None
    place_pickup = request.POST.get('place_pickup')
    redirect_url = request.POST.get("redirect_url")
    price = request.POST.get("price")
    price_children= request.POST.get("price_children")
    company_Price = request.POST.get('company_Price')
    reserve_no_pay = request.POST.get('reserve_no_pay')
    cart = request.session.get('cart', {})
    # Parse the date string into a datetime object with the input format

    # try: 
    #     date_obj = datetime.strptime(date_str, '%m/%d/%Y')
    #     excursion_date =  date_obj.strftime('%A, %d %B')
    # except ValueError:
    #     excursion_date = date_str

# if the item id is already on the excursion cart then it update it
    if item_id in list(cart.keys()):
        if 'adult_qty' in cart[item_id].keys():
            cart[item_id]['adult_qty'] = adult_qty

        if 'child_qty' in cart[item_id].keys():
            cart[item_id]['child_qty'] = child_qty

        if 'infant_qty' in cart[item_id].keys():
                cart[item_id]['infant_qty'] = infant_qty

        if 'place_pickup' in cart[item_id].keys():
            cart[item_id]['place_pickup'] = place_pickup

        if 'excursion_date' in cart[item_id].keys():
            cart[item_id]['excursion_date'] = excursion_date

        if 'selected_time' in cart[item_id].keys():
            cart[item_id]['selected_time'] = selected_time

        if 'price' in cart[item_id].keys():
            cart[item_id]['price'] = price

        if 'price_children' in cart[item_id].keys():
            cart[item_id]['price_children'] = price_children

        if 'company_Price' in cart[item_id].keys():
            cart[item_id]['company_Price'] = company_Price

        if 'place_dropup' in cart[item_id].keys():
            cart[item_id]['place_dropup'] = place_dropup

        if 'reserve_no_pay' in cart[item_id].keys():
            cart[item_id]['reserve_no_pay'] = reserve_no_pay
  
        messages.success(
            request, 'You already added this item so we just updated')
    else:
        # if the item id is not in  the cart it will add a new one
        cart[item_id] = {'adult_qty': adult_qty,  'excursion_date': excursion_date,
                         'child_qty': child_qty, 'infant_qty':infant_qty,'place_pickup': place_pickup, 'price': price, 'selected_time':selected_time, 'price_children': price_children, 'company_Price':company_Price, 'place_dropup':place_dropup, 'reserve_no_pay':reserve_no_pay}
        
    request.session['cart'] = cart
    return redirect(redirect_url)


# Update the child and adult quantity from excursion cart
def update_cart(request, item_id):
    redirect_url = request.POST.get('redirect_url')
    adult_qty = request.POST.get('cart-adult_qty')
    child_qty = request.POST.get('cart-child_qty')
    infant_qty = request.POST.get('cart-infant_qty')
    excursion_date = request.POST.get('excursion_date')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        if 'adult_qty' in cart[item_id].keys():
            cart[item_id]['adult_qty'] = adult_qty

        if 'child_qty' in cart[item_id].keys():
            cart[item_id]['child_qty'] = child_qty
        
        if 'infant_qty' in cart[item_id].keys():
            cart[item_id]['infant_qty'] = infant_qty

        if 'excursion_date' in cart[item_id].keys():
            cart[item_id]['excursion_date'] = excursion_date

    request.session['cart'] = cart
    messages.success(request, 'Cart item Updated Succesfullly')
    return redirect(redirect_url)


# Remove the item from the excursion shopping cart
def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    # customer_contact = request.session.get('customer_contact', {})
    try:
        if item_id in list(cart.keys()):
            cart.pop(item_id)
            request.session['cart'] = cart
            # request.session['customer_contact'] = {}
            messages.success(request, 'Cart item deleted Succesfullly')
            return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


# ----------------------------------All reantals cart fucntionality below

# return the cart page
def view_rental_cart(request):
    return render(request, 'cart/rentals_cart.html')

# Add a rental to the shopping cart
def add_to_cart_rental(request, item_id):
    check_in = request.POST.get('check_in')
    checkout = request.POST.get('checkout')
    redirect_url = request.POST.get("redirect_url")
    if request.method == 'POST':
        check_in_str = take_date_from_str(check_in)
        checkout_str = take_date_from_str(checkout)
        number_of_days = num_of_days(check_in_str, checkout_str)
        adult_qty = int(request.POST.get('adult_qty'))
        child_qty = int(request.POST.get('child_qty'))
        price = request.POST.get("price")
        rental_cart = request.session.get('rental_cart', {})
        # check if the date put it is valid date
        if number_of_days < 1:
            messages.error(request, 'Please select a valid date')
        else:
            # if the item id is already on the cart then it update it
            if item_id in list(rental_cart.keys()):
                if 'check_in' in rental_cart[item_id].keys():
                    rental_cart[item_id]['check_in'] = check_in

                if 'checkout' in rental_cart[item_id].keys():
                    rental_cart[item_id]['checkout'] = checkout

                if 'adult_qty' in rental_cart[item_id].keys():
                    rental_cart[item_id]['adult_qty'] = adult_qty

                if 'child_qty' in rental_cart[item_id].keys():
                    rental_cart[item_id]['child_qty'] = child_qty

                if 'price' in rental_cart[item_id].keys():
                    rental_cart[item_id]['price'] = price
                    messages.success(
                        request, 'You already added this item so we just updated')
            else:
                    # if the item id is not in  the cart it will add a new one
                    rental_cart[item_id] = {'check_in': check_in, 'checkout': checkout,
                                    'adult_qty': adult_qty, 'child_qty': child_qty, 'price': price}
                    messages.success(request, 'Item added to cart Succesfullly')
        request.session['rental_cart'] = rental_cart
        return redirect(redirect_url)
 

# Update rental cart
def update_rental_cart(request, item_id):
    redirect_url = request.POST.get('redirect_url')
    adult_qty = request.POST.get('cart-adult_qty')
    child_qty = request.POST.get('cart-child_qty')
    check_in = request.POST.get('check_in')
    checkout = request.POST.get('checkout')
    rental_cart = request.session.get('rental_cart', {})
    check_in_str = take_date_from_str(check_in)
    checkout_str = take_date_from_str(checkout)
    number_of_days = num_of_days(check_in_str, checkout_str)

    if number_of_days < 1:
        messages.error(request, 'Please select a valid date')
    else:
        if item_id in list(rental_cart.keys()):
            if 'adult_qty' in rental_cart[item_id].keys():
                rental_cart[item_id]['adult_qty'] = adult_qty

            if 'child_qty' in rental_cart[item_id].keys():
                rental_cart[item_id]['child_qty'] = child_qty

            if 'check_in' in rental_cart[item_id].keys():
                rental_cart[item_id]['check_in'] = check_in

            if 'checkout' in rental_cart[item_id].keys():
               rental_cart[item_id]['checkout'] = checkout

        request.session['rental_cart'] = rental_cart
        messages.success(request, 'Cart item Updated Succesfullly')
    return redirect(redirect_url)


# Remove the item from the rental shopping cart
def remove_from_rental_cart(request, item_id):
    print('item_id', item_id)
    rental_cart = request.session.get('rental_cart', {})
    try:
        if item_id in list(rental_cart.keys()):
            rental_cart.pop(item_id)
            request.session['rental_cart'] = rental_cart
            messages.success(request, 'Cart item deleted Succesfullly')
            return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

