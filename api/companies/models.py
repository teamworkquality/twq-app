from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=250, unique=True)
    owner = models.ForeignKey('users.User')
    editors = models.ManyToManyField('users.User', related_name="editors")

class Team(models.Model):
	name = models.CharField(max_length=250, unique=True)