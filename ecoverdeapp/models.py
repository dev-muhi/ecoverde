from django.db import models



class View(models.Model):
    name = models.CharField(max_length=10, default=1)

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Announcement(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    address = models.CharField(max_length=60)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    view = models.ForeignKey(View, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    price = models.FloatField()
    features = models.TextField()
    image = models.ImageField(upload_to = 'pictures')
    phone = models.CharField(max_length=25)
    author = models.CharField(max_length=25)

    def __str__(self):
        return self.title