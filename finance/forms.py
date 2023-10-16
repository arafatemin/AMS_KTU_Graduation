from .models import *
from django import forms

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = '__all__'


class IncomeCategoryForm(forms.ModelForm):
    class Meta:
        model = IncomeCategory
        fields = '__all__'


class OutcomeForm(forms.ModelForm):
    class Meta:
        model = Outcome
        fields = '__all__'


class OutcomeCategoryForm(forms.ModelForm):
    class Meta:
        model = OutcomeCategory
        fields = '__all__'


