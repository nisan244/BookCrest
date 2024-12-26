from django import forms
from transactions.models import *

class Deposit_Form(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount']
        
       