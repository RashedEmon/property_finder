# Generated by Django 4.1.1 on 2022-09-22 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='img/property/'),
        ),
    ]
