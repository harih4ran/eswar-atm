from random import choices
from django.db import models

class Customer(models.Model):
    cid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=400, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True,unique = True)

    def __str__(self) -> str:
        return str(self.name)

class Account(models.Model):
    customer = models.ForeignKey('Customer', related_name='account_customer', on_delete=models.CASCADE)
    account_no = models.CharField(max_length=30, blank=True, null=True,unique = True)
    account_type = models.CharField(max_length=40, blank=True, null=True,choices=(
                                        ('CURRENT', 'CURRENT'),
                                        ('SAVINGS', 'SAVINGS')
                                    ))
    amount = models.FloatField(blank=True, null=True)
    pin = models.CharField(max_length=30, blank=True, null=True,unique = True)

    def __str__(self) -> str:
        return str(self.account_no)