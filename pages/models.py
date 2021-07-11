from django.db import models

# Create your models here.
class Teams(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    designation=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d')
