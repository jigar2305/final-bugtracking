from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import  RegexValidator
from generic.models import BaseField

# Create your models here.

class role(models.Model):
    rolename = models.CharField(max_length=50)
    class meta:
        db_table = "role"


class User(AbstractUser, BaseField):
    roleid = models.ForeignKey(role, on_delete=models.CASCADE)
    username = models.CharField(max_length = 99, unique = True)
    # password = models.CharField(max_length=50, blank=False)
    email = models.EmailField(_('email address') ,max_length=150, unique=True)
    # phone_number = PhoneNumberField(unique=True,null=False, region = 'IN')
    phone_number = models.CharField(max_length=10, blank=True, unique=True) 
    roleid = models.ForeignKey(role, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="img")
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    class Meta:
        db_table = "User"


    def __str__(self):
        return self.username

  