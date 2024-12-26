from django.urls import path
from . views import *

urlpatterns = [
    path('signup/', user_signup, name= 'user_signup'),
    path('login/', user_login.as_view(), name= 'user_login'),
    path('logout/', user_logout, name= 'user_logout'),
    path('profile/', user_profile, name= 'user_profile'),
    path('profile/edit/', edit_profile, name= 'edit_profile'),
    path('profile/edit/password/', change_pass, name= 'change_pass'),
    
]
