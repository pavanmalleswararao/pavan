from django.db import models
class Mallesh(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    phone=models.IntegerField(null=True)
    date=models.DateField(null=True)

# Create your models here.
