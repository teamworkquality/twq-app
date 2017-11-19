from django.db import models
from django.contrib.auth.models import User

class Admin(User):
    full_name = models.CharField(max_length=250, blank=False)
    is_admin = models.BooleanField(default=False, blank=False)

    USERNAME_FIELD = "email"

