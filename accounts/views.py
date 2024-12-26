from django.shortcuts import render, redirect
from . forms import UserRegistrationForm, UserDataChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from books.models import Purchase_Model
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.

# -------------------------------------------------------     

def user_signup(req):
    if req.method == "POST":
        signup_form = UserRegistrationForm(req.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect("user_login")
    else:
        signup_form = UserRegistrationForm()
        
    return render(req, 'accounts/signup.html', {'form' : signup_form})
        
        
# -------------------------------------------------------      
            
class user_login(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = AuthenticationForm
    
    def get_success_url(self):
        messages.success(self.request, "Welcome back, you have successfully logged in!")
        return reverse_lazy("user_profile")

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password. Please try again.")
        return super().form_invalid(form)
        
# ------------------------------------------------------- 
     
@login_required
def user_profile(req):
    purchases = Purchase_Model.objects.filter(user = req.user)
    return render(req, 'accounts/profile.html', {'purchases' : purchases})



# -------------------------------------------------------      
@login_required
def user_logout(req):
    logout(req)
    return redirect('user_login')

        
# -------------------------------------------------------      
@login_required
def edit_profile(req):
    if req.method == "POST":
        edit_form = UserDataChangeForm(req.POST, instance = req.user)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('user_profile')
    else:
        edit_form = UserDataChangeForm(instance = req.user)
        
    return render(req, 'accounts/edit_profile.html', {'form' : edit_form})

   

@login_required
def change_pass(req):
    if req.method == "POST":
        change_pass_form = PasswordChangeForm(req.user, req.POST)
        if change_pass_form.is_valid():
            change_pass_form.save()
            update_session_auth_hash(req, req.user)
            return redirect("user_profile")
    else:
        change_pass_form = PasswordChangeForm(req.user)
    return render(req, 'accounts/change_pass.html', {'form' : change_pass_form}) 


        