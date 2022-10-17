from decimal import Decimal
from django.shortcuts import get_object_or_404
from excursions.models import Excursions
from rentals.models import Rentals
from .utils import take_date_from_str, num_of_days
from datetime import date

# A content processor, vailable in all templates
def cart_contents(request):
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for id, value in cart.items():
        excursion = get_object_or_404(Excursions, pk=id)
        total_price_adult = Decimal(value['price']) * int(value['adult_qty'])
        total_price_children = Decimal(value['price']) / 2 * int(value['child_qty'])
        total += total_price_adult + total_price_children
        subTotal = total_price_adult + total_price_children
        cart_items.append({
            'item_id':id,
            'values': value,
            'excursion':excursion,
            'subTotal':subTotal
        })
    context = {
        'cart_items':cart_items,
        'total':total,
        'product_count':product_count,
    }
    return context


# A content processor for rental cart
def rental_cart_contents(request):
    today = date.today().strftime('%Y-%m-%d')
    rental_cart_items = []
    rental_cart_total = 0
    rental_cart = request.session.get('rental_cart', {})
    for id, value in rental_cart.items():
        rental = get_object_or_404(Rentals, pk=id)
        check_in = take_date_from_str(value['check_in'])
        checkout = take_date_from_str(value['checkout'])
        price = Decimal(value['price'])
        number_of_days  = num_of_days(check_in, checkout)
        sub_total = price * number_of_days
        rental_cart_total += price * number_of_days
        print('sub_total', sub_total)

        rental_cart_items.append({
            'item_id':id,
            'values': value,
            'rental':rental,
            'sub_total':sub_total,
            'number_of_days':number_of_days,
        })
    context = {
        'rental_cart_items':rental_cart_items,
        'rental_cart_total':rental_cart_total,
        'today':today
    }
    return context
