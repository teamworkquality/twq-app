from django.db import models
from users.models import User

class Company(models.Model):
    name = models.CharField(max_length=250, unique=True)
    owner = models.ForeignKey('users.User')
    editors = models.ManyToManyField('users.User', related_name="editors")

class Team(models.Model):
	name = models.CharField(max_length=250, unique=True)

class Employee(User):
    employer = models.ForeignKey('companies.Company', related_name="employer")
    team = models.ForeignKey('companies.Team', null=True)