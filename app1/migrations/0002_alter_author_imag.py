# Generated by Django 4.1.7 on 2023-03-14 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='imag',
            field=models.ImageField(upload_to='img2'),
        ),
    ]
