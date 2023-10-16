from django.contrib.auth.models import User
from django.db import models


class OutcomeCategory(models.Model):
    name             = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['-name']


class Outcome(models.Model):
    user                = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    outCategory         = models.ForeignKey(OutcomeCategory, on_delete=models.SET_NULL, null=True)
    amount              = models.FloatField()
    datetime            = models.DateTimeField(auto_now_add=True)
    description         = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.outCategory.name}"

    class Meta:
        ordering = ['-datetime']


class IncomeCategory(models.Model):
    name             = models.CharField(max_length=256,unique=True)
    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['-name']

class Income(models.Model):
    user                        = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    inCategory                  = models.ForeignKey(IncomeCategory, on_delete=models.SET_NULL, null=True)
    amount                      = models.IntegerField()
    description                 = models.TextField()
    datetime                    = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.inCategory.name}"

    class Meta:
        ordering = ['-datetime']
