from typing import Reversible
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import reverse_related

# Create your models here.


class Category(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name

    

class Announcement(models.Model):
    title = models.CharField(max_length=50)
    date_created = models.DateField(auto_now=False, auto_now_add=True)
    category = models.ForeignKey(Category, related_name='announcements', on_delete=models.CASCADE)
    created_by = models.OneToOneField(User, on_delete=models.CASCADE)
    images = models.FileField(upload_to="announcements/files", max_length=100)

    

   

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return Reversible("Announcement_detail", kwargs={"pk": self.pk})




class Gallery(models.Model):
    image = models.FileField(upload_to="gallery", max_length=100)
    description = models.TextField()
    created_on = models.DateField(auto_now=False, auto_now_add=True)
    

    

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse_related("Gallery_detail", kwargs={"pk": self.pk})
    

