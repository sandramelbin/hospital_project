from django.db import models

# Create your models here.
class hospital(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    user_name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    class Meta:
        db_table="dbhsptl"


class doctor(models.Model):
    objects=None
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    user_name = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    file = models.ImageField(upload_to='image/')
    status = models.CharField(max_length=50,blank=True,default="onhold")