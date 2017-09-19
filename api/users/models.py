from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    full_name = models.CharField(max_length=250)
    email = models.EmailField()
    is_admin = models.BooleanField(default=False)
    password = models.CharField(max_length=250)

class Employee(User):
    pass
