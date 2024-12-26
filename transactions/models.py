from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User

# Create your models here.


class Transaction(models.Model):
    account = models.ForeignKey(User, on_delete = models.CASCADE) 
    amount = models.DecimalField(decimal_places= 2, max_digits = 12) 




class AccountBalance(models.Model):
    account = models.ForeignKey(User, on_delete = models.CASCADE, related_name= 'account_balances') 
    balance = models.DecimalField(decimal_places= 2, max_digits = 12, default= Decimal('0.00')) 

    def __str__(self):
        return self.account.username
    
    
