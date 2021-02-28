from django.db import models


class Announcements(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    region = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    address = models.CharField(max_length=75)
    type = models.CharField(max_length=14)
    status = models.CharField(max_length=14)
    price = models.FloatField()
    features = models.TextField()
    image = models.ImageField(upload_to='pictures')

    def __str__(self):
        return self.title


