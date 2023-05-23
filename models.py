from django.db import models

class Page(models.Model):
    image = models.ImageField(upload_to="images/", default="NA")
    title = models.CharField(max_length=20,default="NA")
    phonenumber = models.CharField(max_length=10, default="NA")
    hmhrsback= models.CharField(max_length=10, default="NA")
    quantity = models.CharField(max_length=10, default="NA")
    address = models.TextField()
class bookedlist(models.Model):
    username = models.CharField(max_length=20, default="NA")
def __str__(self):
    return self.title

