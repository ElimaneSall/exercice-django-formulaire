from django.db import models

# Create your models here.
class Professeur(models.Model):

    prenom = models.CharField(max_length=40, null=True)
    nom = models.CharField(max_length=40, null=True)
    email = models.EmailField(max_length=100, null=True)
    contact = models.CharField(max_length=10, null = True)
    Date_adhesion = models.DateField(null= True)
    chef_department = models.BooleanField(default=False)

