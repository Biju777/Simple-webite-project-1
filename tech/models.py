from django.db import models
from django.utils.timezone import now


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    number = models.IntegerField()
    mesage = models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Service(models.Model):
    image = models.ImageField(upload_to='pics', default='')
    title = models.CharField(max_length=100)
    para = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    bimg = models.ImageField(upload_to='pics', default='')
    slug = models.CharField(max_length=130)
    data = models.DateTimeField(default=now)
    
    def __str__(self):
        return self.title 