from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser


class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, email, phone_number, password=None):
        if not email:
            raise ValueError("User Must Have An Email Address")
        if not phone_number:
            raise ValueError("User Must Have A Phone Number")
        
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            phone_number = phone_number
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, first_name, email, password, phone_number="8098158006"):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            phone_number = phone_number,
            password=password,
            
        
        )
        user.is_active =  True
        user.is_superuser = True
        user.is_email_verified = True
        user.is_staff = True

        user.save()
        return user


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,blank=True)
    email = models.EmailField(max_length=100,unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    age = models.PositiveIntegerField(null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['first_name']
    
    objects = MyAccountManager()
    
    def __str__(self):
        return self.first_name
    
    def has_perm(self,perm,obj=None):
        return self.is_superuser
    
    def has_module_perms(self,add_label):
        return True
    

