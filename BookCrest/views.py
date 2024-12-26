from django.shortcuts import render
from books.models import *
from categories.models import *



def all_categories(req):
    data = Book_Model.objects.all()
    categories = Category.objects.all()
    
    return render(req, 'home.html', {'data' : data, 'category' : categories})


def home(req, category_slug = None):
    data = Book_Model.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        data = Book_Model.objects.filter(category = category)
    categories = Category.objects.all()
    
    return render(req, 'home.html', {'data' : data, 'category' : categories})
