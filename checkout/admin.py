from django.contrib import admin

# Register your models here.
from .models import ExcursionOrder, RentalOrders, myInventions
admin.site.register(ExcursionOrder)
admin.site.register(RentalOrders)
admin.site.register(myInventions)