from decimal import Decimal
from django.shortcuts import get_object_or_404
from excursions.models import Excursions
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