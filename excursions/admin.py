from django.contrib import admin

# Register your models here.
from .models import Excursions, Photos
admin.site.register(Excursions)
admin.site.register(Photos)