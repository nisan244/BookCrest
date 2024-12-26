from django.urls import path
from books.views import *


urlpatterns = [
    path("details/<int:id>/", All_details.as_view(), name= 'all_details'),
    
]
