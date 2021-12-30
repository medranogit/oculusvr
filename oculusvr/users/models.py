from django.db import models

# Create your models here.
class Users(models.Model):
    CLASSIFICATION = (
        ('S', 'Supervisor'),
        ('E', 'Stockist'),
        ('C', 'Conferee'),
        )

    fullname = models.CharField(max_length=100)
    login = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=100)
    nascimento = models.DateField(max_length=30)    
    classification = models.CharField(max_length=1, choices=CLASSIFICATION)
