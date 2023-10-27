from django.contrib.auth.models import User
from django.db import models

from customer.models import Customer


class UnitType(models.Model):
    name                = models.CharField(max_length=64,unique=True)
    description         = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']




class Tax(models.Model):
    amount                = models.IntegerField(null=True,blank=True, unique=True)
    description         = models.TextField(null=True,blank=True)

    def __str__(self):
        return f'%{self.amount}'




class ProductCategory(models.Model):
    title                       = models.CharField(max_length=64,unique=True)
    description                 = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']



class Product(models.Model):
    productCode                 = models.CharField(max_length=64, unique=True)
    name                        = models.CharField(max_length=64, unique=True)
    image                       = models.ImageField(upload_to='static/assets/images/', null=True, blank=True)
    category                    = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)
    type                        = models.ForeignKey(UnitType, on_delete=models.SET_NULL, null=True)
    tax                         = models.ForeignKey(Tax, on_delete=models.SET_NULL, null=True)
    staff                       = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    purchase_price              = models.FloatField()
    sell_price                  = models.FloatField()
    quentity                    = models.IntegerField(null=True, blank=True)
    datetime                    = models.DateTimeField(auto_now_add=True)
    description                 = models.TextField()



    @property
    def get_stock_items(self):
        if self.productinstock_set:
            items = self.productinstock_set.all()
            total = sum([item.quantity for item in items])
            return total


    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['-datetime']




class Stocks(models.Model):
    name = models.CharField(max_length=64, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Stock'




class ProductInStock(models.Model):
    stocks = models.ForeignKey(Stocks, blank=True, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, null=False)
    datetime = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, unique=True, blank=False, null=False)


    class Meta:
        ordering = ['-datetime']








class Invoice(models.Model):
    customer                    = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True,blank=True)
    user                        = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    datetime                    = models.DateTimeField(auto_now=True)
    tax                         = models.ForeignKey(Tax, on_delete=models.CASCADE, blank=True, null=True)
    description                 = models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.datetime.strftime('%Y-%m-%d %H:%M:%S')} For {self.customer}"





class Order(models.Model):
    staff                   = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    customer                = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    product                 = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    invoice                 = models.ForeignKey(Invoice, on_delete=models.CASCADE, blank=True, null=True)
    order_quantity          = models.PositiveIntegerField(blank=True, null=True)
    datetime                = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Order'
        ordering = ['-datetime']


    @property
    def get_total(self):
        total = self.product.sell_price * self.order_quantity
        return total




# class ReturnedProduct(models.Model):
#     sold_product    = models.ForeignKey(Order, on_delete=models.CASCADE)
#     datetime        = models.DateTimeField(auto_now=True)
#     note            = models.TextField(null=True,blank=True)