from django.contrib import admin
from categories.models import Category

# Register your models here.

class AdminSlug(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('category', )}
    list_display = ['category', 'slug']
    
    
admin.site.register(Category, AdminSlug)