# Generated by Django 4.2 on 2023-05-01 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_productmodel_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productmodel',
            old_name='Decima',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='FloatField',
        ),
    ]