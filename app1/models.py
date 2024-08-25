from django.db import models
from datetime import date


# Create your models here.

    

class img(models.Model):
    n = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img')

    def __str__(self):
        return self.n

class register(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mob = models.IntegerField()
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class contacts(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    feedback = models.TextField()

class category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img1')
    def __str__(self):
        return self.name

class product(models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img2')
    name = models.CharField(max_length=50)
    qty = models.IntegerField()
    price = models.IntegerField()
    discription = models.TextField()
    def __str__(self):
        return self.name
    
class vendors(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mob = models.IntegerField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class cartadmin(models.Model):
    orderid = models.CharField(max_length=50)
    productid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    quantity = models.CharField( max_length=50)
    price = models.CharField(max_length=50)
    tprice = models.CharField(max_length=50)

class order(models.Model):
    userid = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    mob = models.CharField(max_length=50)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    orderamount = models.CharField(max_length=200)
    paymentvia = models.CharField(max_length=100)
    paymentmethod = models.CharField(max_length=100)
    transactionid = models.TextField()
    orderdt = models.DateTimeField(auto_created=True,auto_now=True)

    def __str__(self):
        return self.name
