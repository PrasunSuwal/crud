from django.db import models

# Create your models here.

class Staffs(models.Model):
    name = models.CharField(default='123',max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(default=None, max_length=50)

