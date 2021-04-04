from django.contrib import admin
from .models import BudgetHeader, BudgetItem



class BudgetItemAdmin(admin.TabularInline):
    model = BudgetItem
    extra = 1

    
class BudgetHeaderAdmin(admin.ModelAdmin):
    inlines = [BudgetItemAdmin]
    date_hierarchy = 'event_date'
    list_filter = ['event_date', 'budget_date', 'name']
    list_display = ['company', 'name', 'phone', 'email', 'zip_code', 'cpf', 'people_qtd', 'space_restriction',
    'need_waiter', 'want_entrance', 'budget_date', 'event_distance', 'event_date', 'duration_hours']



admin.site.register(BudgetHeader, BudgetHeaderAdmin)