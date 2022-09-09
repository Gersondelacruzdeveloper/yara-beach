from django.contrib import admin

# Register your models here.
from .models import Excursions, ExcursionExtraPhotos
admin.site.register(Excursions)
admin.site.register(ExcursionExtraPhotos)