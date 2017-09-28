from django.db import models

class Form(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    has_time_limit = models.BooleanField()
    time_limit = models.DateTimeField(null=True)

class Question(models.Model):
    text = models.TextField()
    min = models.IntegerField()
    max = models.IntegerField()
    form = models.ForeignKey(Form)