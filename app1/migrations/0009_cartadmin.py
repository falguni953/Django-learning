# Generated by Django 4.1.7 on 2023-04-05 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_vendors'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartadmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.CharField(max_length=50)),
                ('productid', models.CharField(max_length=50)),
                ('userid', models.CharField(max_length=50)),
                ('quantity', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('tprice', models.CharField(max_length=50)),
            ],
        ),
    ]
