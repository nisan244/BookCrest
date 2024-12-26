# Generated by Django 5.1.3 on 2024-12-24 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_remove_book_model_category_book_model_category'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_model',
            name='category',
        ),
        migrations.AddField(
            model_name='book_model',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='categories.category'),
        ),
    ]
