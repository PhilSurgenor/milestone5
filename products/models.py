from django.db import models

# ONE MODEL NEEDED FOR PRODUCTS, PRICE AND TOKEN AMOUNT VERY IMPORTANT

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='img')
    token_amount = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name