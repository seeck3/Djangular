from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=255)
    isComplete = models.CharField(max_length=255)