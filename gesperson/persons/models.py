from django.forms import ModelForm, Textarea
from django.db import models

# Create your models here.
class Persons(models.Model):
    prenompers = models.CharField(max_length = 100)
    nompers = models.CharField(max_length = 50)
    email = models.EmailField()
    adresse = models.CharField(max_length = 100)

class Meta : 
    db_table = "persons"
     