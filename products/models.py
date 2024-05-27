# 2:22

from django.db import models
from base.models import Basemodel

# Create your models here.


class Category(Basemodel):
    category_name= models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to= 'categories')

    
    def __str__(self):
        return self.category_name
    

class Product(Basemodel):
    product_name= models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField()
    description = models.TextField()

class Product_Image(Basemodel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product')    




    

