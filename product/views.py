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
    stocks = Stocks.objects.all()
    context = {
        "products": products,
        "stocks_name": Stocks.objects.all(),
        'profile': profile,
        'stocks': stocks,

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
def product_category_update_view(request, pk):
    category = ProductCategory.objects.get(id=pk)
    if request.method == "POST":
        form = CategoryFrom(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("productCategory")
    else:
        form = CategoryFrom(instance=category)
    context = {
        'form': form,
    }
    return render(request, "product/category/product_category_update.html", context)


@login_required
def product_category_delete_view(request, pk):
    category = ProductCategory.objects.get(id=pk)
    if request.method == "POST":
        category.delete()
        return redirect("productCategory")
    return render(request, "product/category/product_category_delete.html", {"product_category": category})


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


def product_unit_update_view(request, pk):
    unit = UnitType.objects.get(id=pk)
    if request.method == "POST":
        form = UnitFrom(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect("productUnit")
    else:
        form = UnitFrom(instance=unit)
    context = {
        'form': form,
    }
    return render(request, "product/Unit/productUnitUpdate.html", context)


def product_unit_delete_view(request, pk):
    unit = UnitType.objects.get(id=pk)
    if request.method == "POST":
        unit.delete()
        return redirect("productUnit")
    return render(request, "product/Unit/productUnitDelete.html", {"product_unit": unit})


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


def product_tax_update_view(request, pk):
    tax = Tax.objects.get(id=pk)
    if request.method == "POST":
        form = TaxFrom(request.POST, instance=tax)
        if form.is_valid():
            form.save()
            return redirect("productTax")
    else:
        form = TaxFrom(instance=tax)
    context = {
        'form': form,
    }
    return render(request, "product/tax/productTaxUpdate.html", context)


def product_tax_delete_view(request, pk):
    tax = Tax.objects.get(id=pk)
    if request.method == "POST":
        tax.delete()
        return redirect("productTax")
    return render(request, "product/tax/productTaxDelete.html", {"product_tax": tax})


@login_required
def stock_view(request):
    stock = request.GET.get("stock")
    if stock == None:
        stocks = ProductInStock.objects.all()
    else:
        stocks = ProductInStock.objects.filter(stocks__name=stock)

    context = {
        "stocks": stocks,
        "stock": stock,
    }
    return render(request, "Stoke/stoke.html", context)


@login_required
def stock_create_view(request):
    if request.method == 'POST':
        form = StockFrom(request.POST)
        if form.is_valid():
            form.save()
            stock_name = form.cleaned_data.get('name')
            messages.success(request, f"{stock_name} stock name created successfully")
            return HttpResponseRedirect("../productInStock?stock=" + stock_name)
    else:
        form = StockFrom()
    return render(request, "Stoke/create_stock.html", {"form": form})


def create_product_in_stock_view(request):
    stocks_name = request.POST.get("stocks")
    stock = Stocks.objects.filter(id=stocks_name)
    user = request.POST.get("user")

    if request.method == 'POST':
        form = CreateNewProdcutInStockFrom(request.POST)
        if form.is_valid():
            form.instance.user = User.objects.get(id=user)
            form.save()
            product_name = form.cleaned_data.get('product')
            messages.success(request, f" the {product_name} added successfully")
            return HttpResponseRedirect("../productInStock?stock=" + stock[0].name)
    else:
        form = CreateNewProdcutInStockFrom()
    return render(request, "Stoke/create_product_in_stock.html", {"form": form})


def add_new_product_in_stock_view(request, pk):
    stock = ProductInStock.objects.get(id=pk)
    if request.method == "POST":
        quantity = request.POST.get("quantity")
        product_name = request.POST.get("product")
        if int(quantity) > 0:
            stock.quantity += int(quantity)
            stock.user = User.objects.get(username=request.user.username)
            stock.save()
            messages.success(request, f"{quantity} of the {product_name} added successfully")
            return redirect("../productInStock?stock=" + stock.stocks.name)
        else:
            messages.warning(request, f"{quantity} Quantity must bigger than: 0 :(")
            return redirect("../productInStock?stock=" + stock.stocks.name)
    context = {
        'stock': stock
    }
    return render(request, "Stoke/add_new_product_in_stock.html", context)


def add_product_from_store_to_stock_view(request, pk):
    stock = ProductInStock.objects.get(id=pk)
    if request.method == "POST":
        quantity = request.POST.get("quantity")
        user_username = request.POST.get("user")

        print(user_username)
        product_name = request.POST.get("product")
        if stock.product.quentity > 0 and stock.product.quentity >= int(quantity) and int(quantity) > 0:
            stock.quantity += int(quantity)
            stock.product.quentity -= int(quantity)
            stock.user = User.objects.get(username=request.user.username)
            stock.save()
            stock.product.save()
            messages.success(request, f"{quantity} of the {product_name} added successfully")
        else:
            messages.warning(request, f"{quantity}  of the {product_name} product is not available in the store:(")
            return redirect("productListView")

        return redirect("../productInStock?stock=" + stock.stocks.name)
    context = {
        'stock': stock
    }
    return render(request, "Stoke/add_from_product_in_stock.html", context)


def subtract_product_from_stock_to_store_view(request, pk):
    stock = ProductInStock.objects.get(id=pk)
    if request.method == "POST":
        product_name = request.POST.get("product")
        quantity = request.POST.get("quantity")
        user_username = request.POST.get("user")
        print(user_username)

        if stock.quantity >= int(quantity) and int(quantity) > 0:
            stock.quantity -= int(quantity)
            stock.product.quentity += int(quantity)
            stock.user = User.objects.get(username=request.user.username)
            stock.save()
            stock.product.save()
            messages.success(request, f"{quantity} of the {product_name} subtracted successfully")
            return HttpResponseRedirect("../productInStock?stock=" + stock.stocks.name)
        else:
            messages.warning(request, f"{quantity}  of the {product_name} product is not available in the Stock:(")
            return redirect("../productInStock?stock=" + stock.stocks.name)
    context = {
        'stock': stock
    }
    return render(request, "Stoke/subtract_product_from_stock_to_store.html", context)


@login_required
def order_view(request):
    orders = Order.objects.all()
    context = {
        "orders": orders,
    }
    return render(request, "Staff/order.html", context)


# @login_required
# def order_Create_view(request):
#     o_product_id = request.POST.get("product")
#     p_product = Product.objects.all()
#     quantity = request.POST.get("order_quantity")
#     customer = request.POST.get("customer")
#
#     if request.method == 'POST':
#         form = OrderFrom(request.POST)
#         if form.is_valid():
#             for p in p_product:
#                 if p.id == int(o_product_id):
#                     if p.quentity >= int(quantity):
#
#                         newOrder = Order(staff=request.user, product=p, order_quantity=quantity, customer=customer)
#                         newOrder.save()
#                         p.quentity -= int(quantity)
#                         p.save()
#                         messages.success(request, f'Order created successfully')
#                         return HttpResponseRedirect('order')
#                     else:
#                         order_quantity = form.cleaned_data.get('order_quantity')
#                         messages.warning(request, f'Product {order_quantity} not enough quantity :(')
#                         return HttpResponseRedirect('order')
#
#     else:
#         form = OrderFrom()
#     return render(request, "Staff/orderCreate.html", {"form": form})


def order_Create_view(request):
    # user = Order.objects.get(staff__username=request.user.username)
    # print(user)
    if request.method == 'POST':
        # print(user.staff.username)
        form = OrderFrom(request.POST)
        if form.is_valid():
            if form.instance.product.quentity >= form.instance.order_quantity and form.instance.order_quantity > 0 and form.instance.product.quentity > 0:
                form.instance.product.quentity -= form.instance.order_quantity
                form.instance.product.save()
            else:
                messages.warning(request, f'Product {form.instance.order_quantity} not enough quantity in store :( you have only {form.instance.product.quentity} product/s in store')
                return HttpResponseRedirect('orderCreate')



            newOrder = Order(staff=request.user, product=form.instance.product, order_quantity=form.instance.order_quantity, customer=form.instance.customer)
            product_name = form.cleaned_data.get('product')
            newOrder.save()
            messages.success(request, f'In order {form.instance.order_quantity} {product_name} created successfully.')
            return HttpResponseRedirect('order')

    else:
        form = OrderFrom()
    return render(request, "Staff/orderCreate.html", {"form": form})

"""

def create_product_in_stock_view(request):
    stocks_name = request.POST.get("stocks")
    stock = Stocks.objects.filter(id=stocks_name)
    user = request.POST.get("user")

    if request.method == 'POST':
        form = CreateNewProdcutInStockFrom(request.POST)
        if form.is_valid():
            form.instance.user = User.objects.get(id=user)
            form.save()
            product_name = form.cleaned_data.get('product')
            messages.success(request, f" the {product_name} added successfully")
            return HttpResponseRedirect("../productInStock?stock=" + stock[0].name)
    else:
        form = CreateNewProdcutInStockFrom()
    return render(request, "Stoke/create_product_in_stock.html", {"form": form})
    """


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
