from django.contrib import admin

# Register your models here.
from .models import ExcursionOrder, RentalOrder
admin.site.register(ExcursionOrder)
admin.site.register(RentalOrder)