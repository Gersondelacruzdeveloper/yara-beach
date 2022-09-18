from django.contrib import admin

# Register your models here.
from .models import Rentals,Review, Photos
admin.site.register(Rentals)
admin.site.register(Review)
admin.site.register(Photos)