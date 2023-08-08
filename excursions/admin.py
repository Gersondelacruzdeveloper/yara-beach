from django.contrib import admin

# Register your models here.
from .models import Excursions, Photos,Review,Reference,Company
admin.site.register(Excursions)
admin.site.register(Photos)
admin.site.register(Review)
admin.site.register(Reference)
admin.site.register(Company)

