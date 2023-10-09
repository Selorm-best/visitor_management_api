from django.db import models

# Create your models here.
from django.db import models

class Visitor(models.Model):
    name=models.CharField(max_length=255)
    organization =models.CharField(max_length=255)
    contact_details=models.CharField(max_length=255)
    photo=models.ImageField(upload_to="photos/")

class Destination(models.Model):
    name = models.CharField(max_length=255)

class Visit(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    purpose_of_visit = models.TextField()
    date_visited = models.DateTimeField(auto_now_add=True)