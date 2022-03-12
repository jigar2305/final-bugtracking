from django.urls import path,include
from .views import *
from todo import views
urlpatterns = [

    path('home/', views.Homeview ,name='home'),
    path('todolist/', views.Homeview ,name='todopage'),


    
]