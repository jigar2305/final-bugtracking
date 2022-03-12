from dataclasses import field
from multiprocessing import context
from pyexpat import model
from re import template
from sre_constants import SUCCESS
from urllib import request
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import  ListView, CreateView, UpdateView, DeleteView, DetailView, FormView,TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.contrib.auth.views import redirect_to_login
from .forms import UserForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import User

# Create your views here.

class BaseRegisterView(SuccessMessageMixin, FormView):

    form_class = UserForm
    template_name = 'employee/register.html'
    success_url ="/view"
  
    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)  
        user.save()    
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        username = cleaned_data["username"]
        return username + " - User Created Successfully..!!"

class Userlogin(LoginView):
    model = User
    template_name = 'employee/login.html'
    success_url ="/home"

class profileview(TemplateView):
    template_name = "employee/profile.html"

class Listemployee(ListView):
    model = User
    users = model.objects.all()
    context_object_name = 'users'
    template_name = "employee/list_employee.html"

class Deleteemployee(DeleteView):
    model = User
    template_name = "employee/delete_employee.html"
    success_url ="/view"

class Updateemployee(UpdateView):
    model = User
    fields = ['username','email','roleid','picture','phone_number']
    template_name = "employee/update_employee.html"
    success_url ="/view"


