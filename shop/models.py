from django.db import models
import os


# Create your models here.
class Product (models.Model):
    productName = models.CharField(max_length= 100)
    productImage = models.ImageField(upload_to=os.path.join('photo/%y/%m/%d'))
    productPrice = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.productName
    
    class Meta:
        ordering = ['productName']