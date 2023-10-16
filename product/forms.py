from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryFrom(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class UnitFrom(forms.ModelForm):
    class Meta:
        model = UnitType
        fields = '__all__'


class TaxFrom(forms.ModelForm):
    class Meta:
        model = Tax
        fields = '__all__'

class StockFrom(forms.ModelForm):
    class Meta:
        model = Stocks
        fields = '__all__'



class OrderFrom(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'order_quantity']