from operator import mod
from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField

# Create your models here.

class Article(models.Model):
    titre = models.CharField(max_length=200)
    resume = models.CharField(max_length=200)
    miniature = models.ImageField(null=True)
    contenu = models.CharField(max_length=255)
    dateCreation= models.DateTimeField(auto_now_add=True)
    dateModification = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
     return f"{self.titre} {self.contenu} {self.dateCreation}"
