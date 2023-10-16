from users.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from users.forms import UserForm, ProfileForm
from .models import *
from django.views.generic import *
from .forms import *


@login_required
def product_list_view(request):
    products = Product.objects.all()
    profile = Profile.objects.get(staff__username=request.user)
    context = {
        "products": products,
        "stocks_name": Stocks.objects.all(),
        'profile': profile

    }
    return render(request, "product/productListView.html", context)


@login_required
def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'Product {product_name} created successfully')
            return HttpResponseRedirect('productListView')
    else:
        form = ProductForm()
    context = {
        'form': form,
        'products': Product.objects.all(),
        'taxs': Tax.objects.all(),
        'categories': ProductCategory.objects.all(),
        'units': UnitType.objects.all(),


    }
    return render(request, "product/productCreate.html", context)







@login_required
def product_update_view(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        form = ProductForm(request.POST or None, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("productListView")
    else:
        form = ProductForm(instance=product)
    context = {
        'form': form
    }
    return render(request, "product/productUpdate.html", context)


@login_required
def product_delete_view(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect("productListView")
    return render(request, "product/productDelete.html", {"product": product})



@login_required
def product_category_view(request):
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    context = {
        "products": products,
        "categories": categories,
    }
    return render(request, "product/category/productCategory.html", context)


@login_required
def category_create_view(request):
    if request.method == 'POST':
        form = CategoryFrom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('productCategory')
    else:
        form = CategoryFrom()
    return render(request, "product/category/categoryCreate.html", {"form": form})


@login_required
def product_unit_view(request):
    unitTypes = UnitType.objects.all()
    context = {
        "unitTypes": unitTypes,
    }
    return render(request, "product/Unit/productUnit.html", context)


@login_required
def unit_create_view(request):
    if request.method == 'POST':
        form = UnitFrom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('productUnit')
    else:
        form = UnitFrom()

    return render(request, "product/Unit/unitCreate.html", {"form": form})



@login_required
def product_tax_view(request):
    taxs = Tax.objects.all()
    context = {
        "taxs": taxs,
    }
    return render(request, "product/tax/productTax.html", context)


@login_required
def tax_create_view(request):
    if request.method == 'POST':
        form = TaxFrom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('productTax')
    else:
        form = TaxFrom()

    return render(request, "product/tax/taxCreate.html", {"form": form})



@login_required
def product_tax_view(request):
    taxs = Tax.objects.all()
    context = {
        "taxs": taxs,
    }
    return render(request, "product/tax/productTax.html", context)



@login_required
def product_stock_view(request):
    stocks = ProductInStock.objects.all()
    products = Product.objects.all()
    users = User.objects.all()
    stocks_name = Stocks.objects.all()

    if request.method == 'POST':
        quentity = request.POST.get("quentity")
        description = request.POST.get("description")
        product = Product.objects.filter(name=request.POST.get("product"))
        for p in product:
            print(p.name)
        user = request.POST.get("user")
        print(user)
        newStock = ProductInStock(user_id=request.user.id, quentity=quentity, description=description)
        newStock.save()
        return HttpResponseRedirect('productInStock')

    context = {
        "stocks": stocks,
        "users": users,
        "products": products,
        "stocks_name": stocks_name,
    }
    return render(request, "Stoke/stoke.html", context)



@login_required
def stock_create_view(request):
    if request.method == 'POST':
        user = request.POST.get("user")
        quentity = request.POST.get("quentity")
        description = request.POST.get("description")
        newStock = ProductInStock(user=user, quentity=quentity, description=description)
        newStock.save()
        # form = StockFrom(request.POST)
        # if form.is_valid():
        #     form.save()
        return HttpResponseRedirect('productInStock')
    else:
        form = StockFrom()
    return render(request, "Stoke/stoke.html", {"form": form})




@login_required
def staff_view(request):
    users = User.objects.all()
    users_count = users.count()
    context = {
        "users": users,
        'users_count': users_count
    }
    return render(request, "Staff/staff.html", context)


def staff_detail_view(request, pk):
    user = User.objects.get(id=pk)
    context = {
        "user": user
    }
    return render(request, "Authentication/profile.html", context)



@login_required
def staff_update_view(request, pk):
    user = User.objects.get(id=pk)
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "successfully updated")

            return redirect("staff")
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=user.profile)
    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "user": user
    }
    return render(request, "staff/staffUpdate.html", context)




@login_required
def staff_delete_view(request, pk):
    user = User.objects.get(id=pk)
    if request.method == "POST":
        user.delete()
        return redirect("staff")
    return render(request, "staff/staffDelete.html", {"user": user})




@login_required
def order_view(request):
    orders = Order.objects.all()
    context = {
        "orders": orders,
    }
    return render(request, "Staff/order.html", context)

@login_required
def order_Create_view(request):
    if request.method == 'POST':
        form = OrderFrom(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return HttpResponseRedirect('order')
    else:
        form = OrderFrom()
    return render(request, "Staff/orderCreate.html", {"form": form})