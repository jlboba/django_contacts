from django.db import models

# Create your models here.

## Contacts Model
class Contact(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    album1 = models.CharField(max_length=100, blank=True)
    image1 = models.CharField(max_length=100, blank=True)
    album2 = models.CharField(max_length=100, blank=True)
    image2 = models.CharField(max_length=100, blank=True)
    link = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
