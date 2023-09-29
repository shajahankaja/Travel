from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
class Details(models.Model):
    img=models.ImageField(upload_to='photo')
    name=models.CharField(max_length=200)
    decs=models.TextField()

    def __str__(self):
        return self.name