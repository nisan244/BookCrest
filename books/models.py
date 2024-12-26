from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
from django.utils import timezone
import pytz

# Create your models here.

class Book_Model(models.Model):
    name = models.CharField(max_length= 120)
    price = models.IntegerField()
    Description = models.TextField()
    quantity = models.IntegerField()
    img = models.ImageField(upload_to= 'uploads/')
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name= 'books')
    
    
    def __str__(self):
        return self.name
    
    
class Comment_model(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField()
    body = models.TextField()
    time = models.DateTimeField(auto_now_add= True)
    
    book = models.ForeignKey(Book_Model, on_delete= models.CASCADE, related_name= 'comments')
    
    def __str__(self):
        return f"Comments by {self.name}"



class Purchase_Model(models.Model):
    user = models.ManyToManyField(User, related_name= 'purchases')
    product = models.ForeignKey(Book_Model, on_delete= models.CASCADE)
    time = models.DateTimeField(auto_now_add= True)
    
    # bangladesh time dekhanor jonno
    def get_bangladesh_time(self):
        bangladesh_timezone = pytz.timezone('Asia/Dhaka')
        return self.time.astimezone(bangladesh_timezone)
    
    
    def __str__(self):
        return f"{self.user.username} bought {self.product.name}"
    