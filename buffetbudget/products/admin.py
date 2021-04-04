from django.contrib import admin
from .models import Dish

class DishAdmin(admin.ModelAdmin):
    pass


admin.site.register(Dish, DishAdmin)






