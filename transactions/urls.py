from django.urls import path
from transactions.views import *

urlpatterns = [
    path('deposit/', Deposit.as_view(), name= 'deposit'),
    path('buy/<int:id>/', buy_product, name= 'Buy_book'),
    path('return/<int:id>/', Return_product.as_view(), name= 'return_book'),
    
]
