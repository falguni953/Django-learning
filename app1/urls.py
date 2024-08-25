from django.urls import path    
from app1.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',h,name='h'),
    path("i/",i),
    path('second/',second,name='second'),
    # path('about/',about),
    path('contact/',contact,name='contact'),
    path('register/',reg,name='register'),
    path('home/',home,name='index'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('feedback/',feedback,name='feedback'),
    path('update/',change,name='update'),
    path('home/',image1,name='home'),
    path('profile/',profile,name='profile'),
    # path('pdemo/',pdemo,name='pdemo'),
    path('product/<int:id>',cproduct,name='product'),
    path('aproduct/',allproducts,name='aproduct'),
    path('vsignup/',vsignup,name='vsignup'),
    path('vlogin/',vlogin,name='vlogin'),
    # path('vpro/',vpro,name='vpro'),
    path('prodetails/<int:id>',prodetails,name='prodetails'),
    path('addproduct/',addpro,name='addproduct'),
    path('cart/',cart,name='cart'),
    path('cartview/<int:id>',additem,name='cartview'),
    path('cartviewr/<int:id>',removeitem,name='cartviewr'),
    path('search/',search,name='search'),
    path('addcat/',addcat,name='addcat'),
    path('remove/<int:id>',removeall,name='remove'),
    path('buynow/',buynow,name='buynow'),
    path('history/',history,name='history'),
    path('success/',success,name='success'),
    path('failed/',failed,name='failed'),
    path('Razorpay/',Razorpay,name='Razorpay'),
    path('paymenthandler/',paymenthandler,name='paymenthandler'),
    path('removeselected/',removeselected,name='rselect'),
    # path('apiurl/',apinew,name='apiurl'),
    path('invoice/',invoice,name='invoice'),
    path('invoicepdf/',invoice_pdf,name='invoicepdf'),

# <-------------------------------- API ---------------------------------------->
    # first try - complex code
    path('createapi/',serializeusers.as_view(),name='createapiusers'),
    path('updatedeleteapi/<int:pk>/',serializeuserupdatedelete.as_view(),name='updatedeleteusers'),

    # second try - easy code
    path('easyapi/',easyapi,name='easyapi'),
    path('getapimodel/',getapimodel,name='getapimodel'),
    path('postapistoredata/',regpostapi,name='postapistoredata'),
    path('updateapiput/<id>',updateapiput,name="updateapiput"),
    path('updateapipatch/<id>',updateapipatch,name="updateapipatch"),
    path('deleteapi/',deleteapi,name='deleteapi'),
    path('getcat/',get_category,name='getcat'),
    path('getpro/',getpro,name='getpro'),
    path('userapiview/<id>',userdata.as_view(),name='userapiview')

]
urlpatterns += staticfiles_urlpatterns()
