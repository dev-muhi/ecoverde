from django.contrib.auth.models import User
from django.db import models


class View(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        self.name



class Region(models.Model):
    name = models.CharField(max_length=30)



class District(models.Model):
    name = models.CharField(max_length=30)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE)



class Type(models.Model):
    name = models.CharField(max_length=14)



class Status(models.Model):
    name = models.CharField(max_length=14)
    


class Announcement(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    address = models.CharField(max_length=75)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    view = models.ForeignKey(View, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    price = models.FloatField()
    features = models.TextField()
    image = models.ImageField(upload_to='pictures')
    phone = models.CharField(max_length=25)
    author = models.CharField(max_length=25)

    def __str__(self):
        return self.title


