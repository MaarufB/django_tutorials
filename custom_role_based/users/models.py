from unittest import result
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import (
                                            AbstractBaseUser, 
                                            AbstractUser, 
                                            PermissionsMixin,
                                            BaseUserManager
                                       )
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    firstname = models.CharField(max_length=200, null=False)
    lastname = models.CharField(max_length=200, null=False)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=250, null=True)

def create_superuser(self, email, user_name, first_name, password, **otherfields):
    otherfields.setdefault('is_staff', True)
    otherfields.setdefault('is_superuser', True)
    otherfields.setdefault('is_active', True)

    if otherfields.get("is_staff") is not True:
        raise ValueError(
            "Superuser must be assigned to is_staff=True."
        )

    if otherfields.get("is_superuser") is not True:
        raise ValueError(
            "Superuser must be assigned to is_superuser=True."
            )

    return self.create_user(email, user_name, first_name, password, **otherfields)


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, user_name, first_name, password, **other_fields):
        if email:
            raise ValueError(_("You must provide an email address!"))
        

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                            first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()

        return user

class CustomSystemUser(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    start_date = models.DateTimeField()
    about = models.TextField(_('about'), 
                                max_length=500,
                                blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name