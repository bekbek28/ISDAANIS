from django.contrib import admin
from .models import *


admin.site.register(Species)
admin.site.register(Origin)
admin.site.register(Vessel)
admin.site.register(DailyTransaction)
admin.site.register(Province)
admin.site.register(City)

