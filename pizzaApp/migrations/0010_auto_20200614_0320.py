# Generated by Django 3.0.7 on 2020-06-14 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaApp', '0009_ordermodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='status',
            field=models.CharField(default='pending', max_length=10),
        ),
    ]
