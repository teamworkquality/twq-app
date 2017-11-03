from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    full_name = models.CharField(max_length=250, blank=False)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False, blank=False)

    USERNAME_FIELD = "email"

