from django.contrib import admin

# Register your models here.
from .models import ExcursionOrder, AccommodationOrder
admin.site.register(ExcursionOrder)
admin.site.register(AccommodationOrder)