from django.shortcuts import render
from .models import *
def income_view(request):
    context = {
        'income_category': IncomeCategory.objects.all(),
        'incomes': Income.objects.all(),
        'outcome_category': OutcomeCategory.objects.all(),
        'outcomes': Outcome.objects.all(),
    }
    return render(request, 'finance/income.html', context)
