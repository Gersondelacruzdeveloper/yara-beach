from django.contrib import admin

# Register your models here.
from .models import Excursions, Photos,Review
admin.site.register(Excursions)
admin.site.register(Photos)
admin.site.register(Review)