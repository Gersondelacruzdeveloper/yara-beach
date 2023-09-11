from django.contrib import admin

# Register your models here.
from .models import Excursions, Photos,Review,Reference,Company,AvailableTime,DayOfWeek,PageVisit
admin.site.register(Excursions)
admin.site.register(Photos)
admin.site.register(Review)
admin.site.register(Reference)
admin.site.register(Company)
admin.site.register(AvailableTime)
admin.site.register(DayOfWeek)
admin.site.register(PageVisit)

