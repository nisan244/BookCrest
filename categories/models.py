from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length= 100)
    slug = models.SlugField(max_length= 120)
    
    def __str__(self):
        return self.category
    
    