from django import forms
from .models import *


class BankFrom(forms.ModelForm):
    class Meta:
        model = Bank
        fields = '__all__'


class PaymentFrom(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'


class CashFrom(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'invoice', 'customer', 'description']


class BankMethodFrom(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
