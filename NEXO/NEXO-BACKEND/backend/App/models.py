from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    image=models.ImageField(upload_to='product_images/')
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.CharField(max_length=100,choices=[("vetements_femme", "Vêtements Femme"), ("vetements_homme", "Vêtements Homme"),("Bijoux_Accessoires","Bijoux et Accessoires"),("Maison_jardin","Maison et jardin")])
    stock=models.IntegerField(default=0, validators=[MinValueValidator(0)])
    def __str__(self):
        return self.name
class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products=models.ManyToManyField(Products)
    


