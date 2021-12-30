from django.db import models

# Create your models here.

class Products(models.Model):
    TYPE = (
        ('MAIN','OCULUS'),
        ('SECO','ASSET'),
    )
    STORAGE = (
        ('MIN','128GB'),
        ('MAX','256GB'),
    )

    name = models.CharField(max_length=50)
    storage = models.CharField(max_length=3, choices=STORAGE)
    typee = models.CharField(max_length=4, choices=TYPE) 
