from decimal import Decimal
from django.shortcuts import get_object_or_404
from excursions.models import Excursions,Reference
from rentals.models import Rentals
from .utils import take_date_from_str, num_of_days
from django.http import Http404
from datetime import date, timedelta
from django.conf import settings
from django.contrib import messages
from django.shortcuts import HttpResponse, render, redirect

# A content processor, vailable in all templates

def cart_contents(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price_adul_child = Decimal(0.00)
    taxes_and_fees = Decimal(0.00)
    anticipo = round(0.00)
    company_price_total = Decimal(0.00)
    product_count = 0
    # for selcting tomorow excursions only
    today = date.today()
    # Calculate tomorrow's date
    tomorrow = today + timedelta(days=2)
    # Format the date as a string in the desired format
    tomorrow_str = tomorrow.strftime('%Y-%m-%d')
    reserve_no_pay = False
     

    for id, value in cart.items():
        try:
            excursion = Excursions.objects.get(pk=id)
            is_transfer = excursion.is_transfer
            total_price_adult = Decimal(value['price']) * int(value['adult_qty'])
            try:
                company_total_price_adult = Decimal(value['company_Price']) * int(value['adult_qty'])
            except KeyError:
                if value['reserve_no_pay'] == 'True':
                    reserve_no_pay = True
                company_total_price_adult = 0
            total_price_children = 0
            if value['child_qty']:
                try:
                    total_price_children = Decimal(value['price_children']) * int(value['child_qty'])
                    # company_total_price_children = Decimal(value['price_children']) * int(value['child_qty'])
                except ValueError:
                    print("An error occurred in our system. Please try again later.")
            total_price_adul_child += Decimal(total_price_adult + total_price_children)
            company_price_total += Decimal(company_total_price_adult + total_price_children)
            subTotal = total_price_adult + total_price_children

            

            cart_items.append({
                'item_id': id,
                'values': value,
                'excursion': excursion,
                'is_transfer': is_transfer,
                'subTotal': subTotal,
                'company_price_total':company_price_total,
            })
    
        except Excursions.DoesNotExist:
            # Handle the case where the Excursions object does not exist
            print(f"Excursions with id {id} does not exist.")
    taxes_and_fees += total_price_adul_child * Decimal(settings.TAXES_AND_FEES)
    final_total = total_price_adul_child + taxes_and_fees
    anticipo = final_total - company_price_total

    context = {
        'cart_items': cart_items,
        'product_count': product_count,
        'tomorrow_str':tomorrow_str,
        'last_item': cart_items[-1] if cart_items else None,
        'anticipo':round(anticipo),
        'taxes_and_fees':taxes_and_fees,
        'company_price_total':company_price_total,
        'final_total':final_total,
        'reserve_no_pay': reserve_no_pay,
    }
    request.session['cart'] = cart
    return context



# A content processor for rental cart
def rental_cart_contents(request):
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
    }
    return context

