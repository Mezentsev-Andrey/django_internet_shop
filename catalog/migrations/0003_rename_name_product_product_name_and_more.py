# Generated by Django 4.2.9 on 2024-03-24 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_version'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='version',
            old_name='name',
            new_name='name_version',
        ),
    ]
