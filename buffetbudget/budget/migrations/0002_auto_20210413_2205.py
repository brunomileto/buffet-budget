# Generated by Django 3.1.7 on 2021-04-14 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budgetitem',
            name='dish',
        ),
        migrations.AddField(
            model_name='budgetitem',
            name='dish',
            field=models.ManyToManyField(to='products.Dish'),
        ),
    ]
