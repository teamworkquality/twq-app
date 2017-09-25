from django.db import models

class Form(models.Model):
    name = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    has_time_limit = models.BooleanField(required=True)
    time_limit = models.DateTimeField()

class Question(models.Model):
    text = models.TextField()
    min = models.IntegerField()
    max = models.IntegerField()