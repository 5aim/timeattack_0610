# Generated by Django 4.1.5 on 2023-01-26 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_userorder'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
