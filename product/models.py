from django.contrib.auth.models import User
from django.db import models












class UnitType(models.Model):
    name                = models.CharField(max_length=64,unique=True)
    description         = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name

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
    quentity = models.IntegerField(blank=False, null=False)
    datetime = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE)





    class Meta:
        verbose_name = 'ProductsInStock'
        ordering = ['-datetime']



class Order(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    order_quantity = models.PositiveIntegerField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)

    


    class Meta:
        verbose_name = 'Order'
        ordering = ['-datetime']











