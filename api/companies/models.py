from django.db import models
from users.models import Admin


class Company(models.Model):
    name = models.CharField(max_length=250, unique=True)
    owner = models.ForeignKey('users.Admin')
    editors = models.ManyToManyField('users.Admin', related_name="editors")


class Team(models.Model):
    name = models.CharField(max_length=250, unique=True)


class Employee(Admin):
    employer = models.ForeignKey('companies.Company', related_name="employer")
    team = models.ForeignKey('companies.Team', null=True)