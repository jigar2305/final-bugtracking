from django.urls import path,include
from employee import views
from .views import *

urlpatterns = [
    path('login/', Userlogin.as_view(), name='userlogin'),
    path('profile/', profileview.as_view(), name='profilepage'),
    path('register/',BaseRegisterView.as_view() , name='add_employee'),
    path('view/', Listemployee.as_view(), name='list_employee'),
    path('<int:pk>delete/', Deleteemployee.as_view(), name='delete_employee'),
    path('<int:pk>update/', Updateemployee.as_view(), name='update_employee'),
    
    
]