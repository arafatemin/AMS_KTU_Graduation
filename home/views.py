from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from product.models import *
from users.models import *

@login_required(login_url='login')
def index(request):
    context = {
        'stocks_name': Stocks.objects.all(),
        'users': User.objects.all(),
        'order': Order.objects.all()
    }
    return render(request, 'home/index.html', context)



# def base(request):
#     # context = {
#     #     'stocks': Stocks.objects.all(),
#     # }
#     return render(request, 'base.html', context)