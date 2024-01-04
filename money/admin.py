from django.contrib import admin
from .models import *


# Register your models here.
class BankAdmin(admin.ModelAdmin):
    model = Bank
    list_display = ['user', 'bank_name', 'iban']
    list_display_links = ['bank_name']
    list_per_page = 10

admin.site.register(Bank, BankAdmin)


class PaymentAdmin(admin.ModelAdmin):
    model = Payment
    list_display = ['customer', 'invoice', 'amount', 'datetime']
    list_display_links = ['customer']
    list_per_page = 10


admin.site.register(Payment, PaymentAdmin)