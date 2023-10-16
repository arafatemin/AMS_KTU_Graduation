from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import *
from .models import *


def income_view(request):
    context = {
        'incomes': Income.objects.all(),
    }
    return render(request, 'finance/Income/income.html', context)


@login_required
def income_create_view(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            description = form.cleaned_data.get('description')
            messages.success(request, f'{description} created successfully')
            return HttpResponseRedirect('income')
    else:
        form = IncomeForm()
    context = {
        'form': form,
    }
    return render(request, "Finance/Income/income_create.html", context)




def income_update_view(request, pk):
    income = Income.objects.get(id=pk)
    if request.method == "POST":
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect("income")
    else:
        form = IncomeForm(instance=income)
    context = {
        'form': form,
    }
    return render(request, "Finance/Income/income_update.html", context)





def income_delete_view(request, pk):
    income = Income.objects.get(id=pk)
    if request.method == "POST":
        income.delete()
        return redirect("income")
    return render(request, "Finance/Income/income_delete.html", {"income": income})









def income_category_view(request):
    context = {
        'income_categories': IncomeCategory.objects.all(),
    }
    return render(request, 'finance/IncomeCategory/income_category.html', context)


def income_category_create_view(request):
    if request.method == 'POST':
        form = IncomeCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            category_name = form.cleaned_data.get('name')
            messages.success(request, f'{category_name} created successfully')
            return HttpResponseRedirect('income_category')
    else:
        form = IncomeCategoryForm()
    context = {
        'form': form,
    }
    return render(request, "Finance/IncomeCategory/income_category_create.html", context)



def income_category_update_view(request, pk):
    income_category = IncomeCategory.objects.get(id=pk)
    if request.method == "POST":
        form = IncomeCategoryForm(request.POST, instance=income_category)
        if form.is_valid():
            form.save()
            return redirect("income_category")
    else:
        form = IncomeCategoryForm(instance=income_category)
    context = {
        'form': form,
    }
    return render(request, "Finance/IncomeCategory/income_category_update.html", context)




def income_category_delete_view(request, pk):
    income_category = IncomeCategory.objects.get(id=pk)
    if request.method == "POST":
        income_category.delete()
        return redirect("income_category")
    return render(request, "Finance/IncomeCategory/income_category_delete.html", {"income_category": income_category})








def outcome_view(request):
    context = {
        'outcomes': Outcome.objects.all(),
    }
    return render(request, 'finance/Outcome/outcome.html', context)



def outcome_create_view(request):
    if request.method == 'POST':
        form = OutcomeForm(request.POST)
        if form.is_valid():
            form.save()
            description = form.cleaned_data.get('description')
            messages.success(request, f'{description} created successfully')
            return HttpResponseRedirect('outcome')
    else:
        form = OutcomeForm()
    context = {
        'form': form,
    }
    return render(request, "Finance/Outcome/outcome_create.html", context)


def outcome_update_view(request, pk):
    outcome = Outcome.objects.get(id=pk)
    if request.method == "POST":
        form = OutcomeForm(request.POST, instance=outcome)
        if form.is_valid():
            form.save()
            return redirect("outcome")
    else:
        form = OutcomeForm(instance=outcome)
    context = {
        'form': form,
    }
    return render(request, "Finance/Outcome/outcome_update.html", context)


def outcome_delete_view(request, pk):
    outcome = Outcome.objects.get(id=pk)
    if request.method == "POST":
        outcome.delete()
        return redirect("outcome")
    return render(request, "Finance/Outcome/outcome_delete.html", {"outcome": outcome})








def outcome_category_view(request):
    context = {
        'outcome_categories': OutcomeCategory.objects.all(),
    }
    return render(request, 'finance/OutcomeCategory/outcome_category.html', context)


def outcome_category_create_view(request):
    if request.method == 'POST':
        form = OutcomeCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            category_name = form.cleaned_data.get('name')
            messages.success(request, f'{category_name} created successfully')
            return HttpResponseRedirect('outcome_category')
    else:
        form = OutcomeCategoryForm()
    context = {
        'form': form,
    }
    return render(request, "Finance/OutcomeCategory/outcome_category_create.html", context)

def outcome_category_update_view(request, pk):
    outcome_category = OutcomeCategory.objects.get(id=pk)
    if request.method == "POST":
        form = OutcomeCategoryForm(request.POST, instance=outcome_category)

        if form.is_valid():
            form.save()
            category_name = form.cleaned_data.get('name')
            messages.success(request, f'{category_name} updated successfully')
            return redirect("outcome_category")
    else:
        form = OutcomeCategoryForm(instance=outcome_category)
    context = {
        'form': form,
    }
    return render(request, "Finance/OutcomeCategory/outcome_category_update.html", context)



def outcome_category_delete_view(request, pk):
    outcome_category = OutcomeCategory.objects.get(id=pk)
    if request.method == "POST":
        outcome_category.delete()
        return redirect("outcome_category")
    context = {
        'outcome_category': outcome_category
    }
    return render(request, "Finance/OutcomeCategory/outcome_category_delete.html", context)