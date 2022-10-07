from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.JSONField()
    roll=models.JSONField()
    city=models.JSONField()
    
