
from django.db import models
class person(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    dateofbirth=models.DateField()
    contactnumber=models.TextField()
    country =models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    idproofnumber=models.TextField()
    class Meta:
        verbose_name_plural="Registration details"
    def __str__(self):
        return self.firstname
class destinations(models.Model):
    wheretogo =models.CharField(max_length=50)
    date=models.DateField()
    traveltype=models.CharField(max_length=75)
    class Meta:
        verbose_name_plural="Destination Availability  Details"
    def __str__(self):
        return self.wheretogo
class blogreply(models.Model):
    comment=models.CharField(max_length=1000)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    website=models.CharField(max_length=100)
    class Meta:
        verbose_name_plural="Blog reply"
    def __str__(self):
        return self.name
class join(models.Model):
    name = models.CharField(max_length=50)
    phonenumber=models.IntegerField()
    message=models.CharField(max_length=1000)




# Create your models here.
