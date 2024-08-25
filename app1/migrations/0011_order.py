# Generated by Django 4.1.7 on 2023-04-20 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_remove_entry_authors_remove_entry_blog_delete_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderdt', models.DateTimeField(auto_created=True, auto_now=True)),
                ('userid', models.CharField(max_length=50)),
                ('productid', models.CharField(max_length=50)),
                ('quantityb', models.CharField(max_length=50)),
                ('cartid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('mob', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=10)),
                ('orderamount', models.CharField(max_length=200)),
                ('paymentvia', models.CharField(max_length=100)),
                ('paymentmethod', models.CharField(max_length=100)),
                ('transactionid', models.TextField()),
            ],
        ),
    ]
