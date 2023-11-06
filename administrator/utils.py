
from checkout.models import ExcursionOrder
from excursions.models import Excursions
from datetime import date, timedelta
import datetime

def filter_category(category):
    all_excursion_orders = ExcursionOrder.objects.all()
    # fileter tomorow excursio
    tomorow_excursion_bookings = all_excursion_orders.filter(excursion_date=datetime.date.today() + timedelta(days=1))
    category_bookings = []
    Santo_domingo = Excursions.objects.filter(category__category=category)
    # print('Santo_domingo', Santo_domingo[0].id)
    for i in Santo_domingo:
        category_bookings += tomorow_excursion_bookings.filter(excursion_id=i.id)
    return category_bookings
