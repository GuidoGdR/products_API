# Generated by Django 4.2 on 2023-05-01 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='name',
            field=models.CharField(default='Menta granizada', max_length=50, unique=True, verbose_name='Nombre'),
        ),
    ]