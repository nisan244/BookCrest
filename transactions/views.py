from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from transactions.models import Transaction, AccountBalance
from transactions.forms import Deposit_Form
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views import View
from books.models import Book_Model, Purchase_Model
from django.contrib import messages
from decimal import Decimal
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

@login_required
def send_transaction_email(user, amount, subject, template):
    message = render_to_string(template, {
        'user' : user, 
        'amount' : amount,
        
    })
    send_email = EmailMultiAlternatives(subject, '', to= [user.email])
    send_email.attach_alternative(message, 'text/html')
    send_email.send()

# ---------------------------------

@method_decorator(login_required, name='dispatch')
class Deposit(FormView):
    template_name = 'transactions/deposit.html'
    form_class = Deposit_Form
    success_url = reverse_lazy('user_profile')
    
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        user_account = self.request.user
            
        account_balance, created = AccountBalance.objects.get_or_create(account= user_account)
        account_balance.balance += amount
        account_balance.save()
        
        send_transaction_email(
            user_account,
            amount,
            'Your Deposit is Successful.',
            'transactions/deposit_email.html'
        )
        
        messages.success(self.request, f"Deposit of {amount} BDT was successful! Your updated balance is {account_balance.balance} BDT.")

        return super().form_valid(form)
    
# ---------------------------------------   
          
@login_required
def buy_product(req, id):
    if req.method == 'POST':
        product = get_object_or_404(Book_Model, pk = id)
        user_balance = AccountBalance.objects.get(account = req.user)
        
        if user_balance.balance < product.price:
            messages.error(req, "Insufficient balance. Please add funds to your account.")
            return redirect('user_profile')
        
        elif product.quantity <= 0:
            messages.error(req, "This product is out of stock.")
            return redirect('user_profile')
        
        user_balance.balance -= Decimal(product.price)
        user_balance.save()
        
        product.quantity -= 1
        product.save()
        
        purchase, created = Purchase_Model.objects.get_or_create(product = product)
        purchase.user.add(req.user)
        
        
        messages.success(req, f"Successfully purchased '{product.name}' for {product.price} BDT.")

        return redirect('user_profile')
                
                
            
@method_decorator(login_required, name='dispatch')
class Return_product(View):
    def get(self, request, id):
        purchase = Purchase_Model.objects.get(pk = id)
        
        user_balance = AccountBalance.objects.get(account = self.request.user)
        user_balance.balance += purchase.product.price
        user_balance.save()
        
        purchase.product.quantity += 1
        purchase.product.save()
        
        purchase.user.remove(request.user)
        purchase.save()
        
    
        messages.success(request, f"You have successfully returned the product '{purchase.product.name}'.")

        return redirect("user_profile")
    