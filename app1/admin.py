from django.contrib import admin
from .models import *
# Register your models here.

class im(admin.ModelAdmin):
    list_display=['n','image']
    list_display=['n','image']
admin.site.register(img,im)
class reg(admin.ModelAdmin):
    list_display=['id','name','email','mob','password']
    list_filter=['name','email','mob','password']
admin.site.register(register,reg)
# admin.site.register(contacts)

class con(admin.ModelAdmin):
    list_display=['name','email','feedback']
    list_filter=['name','email','feedback']
admin.site.register(contacts,con)
# admin.site.register(contacts)

class cat(admin.ModelAdmin):
    list_display=['id','name','image']
    list_filter=['name','image']
admin.site.register(category,cat)

class prod(admin.ModelAdmin):
    list_display=['id','category','name','qty','price','discription','image']
    list_filter=['category','name','qty','price','discription']
admin.site.register(product,prod)


class ven(admin.ModelAdmin):
    list_display=['id','name','email','mob','password']
    list_filter=['id','name','email','mob','password']
admin.site.register(vendors,ven)


class carta(admin.ModelAdmin):
    list_display=['id','orderid','productid','userid','quantity','price','tprice']
    list_filter=['id','orderid','productid','userid','quantity','price','tprice']
admin.site.register(cartadmin,carta)

class ordera(admin.ModelAdmin):
    list_display=['id','userid','name','email','mob','address','city','state','pincode','orderamount','paymentvia','paymentmethod','transactionid','orderdt']
    list_filter=['id','userid','name','email','mob','address','city','state','pincode','orderamount','paymentvia','paymentmethod','transactionid','orderdt']
admin.site.register(order,ordera)