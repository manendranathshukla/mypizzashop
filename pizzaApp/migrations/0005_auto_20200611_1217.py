# Generated by Django 3.0.7 on 2020-06-11 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaApp', '0004_auto_20200611_1149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='password',
            new_name='phone',
        ),
    ]
