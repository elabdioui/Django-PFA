from django.db import models
from django.contrib.auth.models import AbstractUser

class Product(models.Model):
    CHOICES = (
        ('voiture', 'voiture'),
        ('moto', 'moto'),
    )
    CARB=(
        ('diesel','diesel'),
        ('essence','essence',)
        )
    name = models.CharField(max_length=100,default=" ",verbose_name='marque')
    description = models.TextField(default=" ")
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0,verbose_name='prix')
    stock = models.IntegerField(default=0)
    category = models.CharField(max_length=20, choices=CHOICES,default=" ")
    type = models.CharField(max_length=20, choices=CARB,default=" ")
    image = models.ImageField(upload_to='product_images/',default=None)
    
    
    class Meta:
        db_table = 'product'
        
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return f"{self.name} - {self.email}"