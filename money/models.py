from django.contrib.auth.models import User
from django.db import models
from customer.models import Customer
from product.models import Invoice


class Bank(models.Model):
    user                = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    bank_name           = models.CharField(max_length=64,null=True,blank=True)
    iban                = models.CharField(max_length=26,null=True,blank=True, unique=True)

    def __str__(self):
        return self.bank_name


class Payment(models.Model):
    invoice             = models.ForeignKey(Invoice,on_delete=models.CASCADE, null=True, blank=True)
    bank                = models.ForeignKey(Bank,on_delete=models.DO_NOTHING,null=True,blank=True)
    customer            = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    datetime            = models.DateTimeField(auto_now=True)
    amount              = models.FloatField(null=True,blank=True)
    description         = models.TextField(null=True,blank=True)


    def __str__(self):
        return f'{self.bank} - {self.amount}'


    class Meta:
        ordering = ['-datetime']
