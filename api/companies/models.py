from django.db import models
from users.models import User

class Company(models.Model):
    name = models.CharField(max_length=250, unique=True)
    owner = models.ForeignKey(User)

class Team(models.Model):
	name = models.CharField(max_length=250, unique=True)