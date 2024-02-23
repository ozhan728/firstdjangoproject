from django.db import models

# Create your models here.

class Person(models.Model) :
    name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=20)
    number = models.IntegerField()
    birthday = models.DateTimeField()