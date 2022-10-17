from decimal import Decimal
from django.shortcuts import get_object_or_404
from excursions.models import Excursions
from rentals.models import Rentals
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
    rental_cart_items = []
    rental_cart_total = 0
    rental_cart = request.session.get('rental_cart', {})
    print('rental_cart', rental_cart)
    for id, value in rental_cart.items():
        rental = get_object_or_404(Rentals, pk=id)
        rental_cart_items.append({
            'item_id':id,
            'values': value,
            'rental':rental,
        })
    context = {
        'rental_cart_items':rental_cart_items,
        'rental_cart_total':rental_cart_total,
    }
    return context