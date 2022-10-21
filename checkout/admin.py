from django.contrib import admin

# Register your models here.
from .models import ExcursionOrder, accommodationOrder
admin.site.register(ExcursionOrder)
admin.site.register(accommodationOrder)