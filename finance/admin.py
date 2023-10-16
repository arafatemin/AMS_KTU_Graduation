from django.contrib import admin
from .models import *

class OutcomeAdmin(admin.ModelAdmin):
    model = Outcome
    list_display = ['user', 'outCategory', 'amount', 'datetime', 'description']
    list_display_links = ['user']
    list_per_page = 10

admin.site.register(OutcomeCategory)
admin.site.register(Outcome, OutcomeAdmin)


class IncomeAdmin(admin.ModelAdmin):
    model = Income
    list_display = ['user', 'inCategory', 'amount', 'datetime', 'description']
    list_display_links = ['user']
    list_per_page = 10

admin.site.register(IncomeCategory)
admin.site.register(Income, IncomeAdmin)



