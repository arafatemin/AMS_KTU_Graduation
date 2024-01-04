from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

from product.models import Order
from .models import *
from .forms import *
def payment_view(request):
    context = {
        'payments': Payment.objects.all()
    }
    return render(request, 'Payment/payment.html', context)

def payment_create_view(request):
    if request.method == 'POST':
        form = PaymentFrom(request.POST)
        if form.is_valid():
            form.save()
            payment_name = form.cleaned_data.get('invoice')
            messages.success(request, f' {payment_name} created successfully')
            return HttpResponseRedirect('payment')
    else:
        form = PaymentFrom()
    return render(request, 'Payment/paymentCreate.html', {'form': form})



def payment_update_view(request, pk):
    payment = Payment.objects.get(id=pk)
    if request.method == 'POST':
        form = PaymentFrom(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            messages.success(request, f' {payment.invoice} updated successfully')
            return redirect('payment')
    else:
        form = PaymentFrom(instance=payment)
    return render(request, 'Payment/paymentUpdate.html', {'form': form})




def payment_delete_view(request, pk):
    payment = Payment.objects.get(id=pk)
    if request.method == 'POST':
        payment.delete()
        messages.success(request, f' {payment.invoice} deleted successfully')
        return redirect('payment')
    return render(request, 'Payment/paymentDelete.html', {'payment': payment})








def payment_method_view(request):
    pass
    # context = {
    #     'payments': Payment.objects.all()
    # }
    # return render(request, 'Payment/paymentMethod.html', context)


def cash_method_view(request):
    amount = request.POST.get('amount')
    description = request.POST.get('description')
    order = request.POST.get('order')
    paid_customer = Order.objects.get(id=order)
    if request.method == 'POST':
        form = CashFrom(request.POST)
        if form.is_valid():
            if paid_customer.get_balance < int(amount):
                messages.warning(request, f'You have only {paid_customer.get_balance} $ to pay')
                return HttpResponseRedirect('invoiceCustomerDetail/' + str(order))
        newForm = form.save(commit=False)
        newForm.customer = paid_customer.customer
        newForm.invoice = paid_customer.invoice
        newForm.description = description
        newForm.amount = amount
        newForm.save()
        cash_amount = form.cleaned_data.get('amount')
        messages.success(request, f' {cash_amount} $ sanded successfully')
        return HttpResponseRedirect('invoiceCustomerDetail/' + str(order))

    else:
        form = CashFrom()
    return render(request, 'Payment/payment.html', {'form': form})





def bank_method_view(request):
    bank_name = request.POST.get('bank')



    if request.method == 'POST':
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        order = request.POST.get('order')
        paid_customer = Order.objects.get(id=order)


        balance = paid_customer.add_totals

        form = BankFrom(request.POST)
        if form.is_valid():
            if paid_customer.get_balance < int(amount):
                messages.warning(request, f'You have only {paid_customer.get_balance} $ to pay')
                return HttpResponseRedirect('invoiceCustomerDetail/' + str(order))
            paid_customer.save()
            bank_bank_name = form.data.get('bank')
            newForm = Payment(invoice=paid_customer.invoice,  customer=paid_customer.customer, amount=amount,  description=description)
            newForm.bank = Bank.objects.filter(bank_name=bank_bank_name).first()
            newForm.save()
            messages.success(request, f' {amount} $ sanded successfully')
            return redirect('invoiceCustomerDetail/' + str(order), {'balance': balance})


        
        













def bank_view(request):
    context = {
        'banks': Bank.objects.all()
    }
    return render(request, 'Bank/bank.html', context)



def bank_create_view(request):
    if request.method == 'POST':
        form = BankFrom(request.POST)
        if form.is_valid():
            form.save()
            bank_name = form.cleaned_data.get('bank_name')
            messages.success(request, f' {bank_name} created successfully')
            return HttpResponseRedirect('bank')
    else:
        form = BankFrom()
    return render(request, 'Bank/bankCreate.html', {'form': form})




def bank_update_view(request, pk):
    bank = Bank.objects.get(id=pk)
    if request.method == 'POST':
        form = BankFrom(request.POST, instance=bank)
        if form.is_valid():
            form.save()
            messages.success(request, f' {bank.bank_name} updated successfully')
            return redirect('bank')
    else:
        form = BankFrom(instance=bank)
    return render(request, 'Bank/bankUpdate.html', {'form': form})


def bank_delete_view(request, pk):
    bank = Bank.objects.get(id=pk)
    if request.method == 'POST':
        bank.delete()
        messages.success(request, f' {bank.bank_name} deleted successfully')
        return redirect('bank')
    return render(request, 'Bank/bankDelete.html', {'bank': bank})