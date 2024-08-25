from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .form import *
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from django.core.serializers import serialize

# Create your views here.
# from django.http import HttpResponse

def apinew(request):
    a = register.objects.all()
    data = serialize('json',a,fields = 'email')
    return HttpResponse(data, content_type = 'application/json')


def h(request):
    # a=product.objects.filter(category=1)
    if 'user' in request.session.keys():
        a=category.objects.all()
        b=register.objects.get(email = request.session['user'])
        # b=request.session['user']
        return render(request,'h.html',{'k':a,'d':b})
    elif 'user1' in request.session:
        a=category.objects.all()
        c=vendors.objects.get(email = request.session['user1'])
        return render(request,'h.html',{'k':a,'k1':c})
    else:
        a=category.objects.all()
        return render(request,'h.html',{'k':a})
    # a=category.objects.all()
    # a=img.objects.filter(n="")
    # a=img.objects.all()
    # a=img.objects.get(n="kjgyuygu")
    # a1=Entry.objects.get(blog="olji")
    # a=Blog.objects.filter(name=a1)
    # return render(request,'h.html',{'k':a,'k1':b})
    # return render(request,'h.html',{'k':b})

def image1(request):
    if request.method=='POST' and request.FILES['image']:
        a=img()
        a.n=request.POST['n']
        a.image=request.FILES['image']
        a.save()
    return render(request,'home.html')

def i(request):
    return HttpResponse("This is written text")

def second(request):
    # v=Blog.objects.filter(name="xyz")|Blog.objects.filter(name=1)
    return render(request,'h.html')

def contact(request):
    if 'user' in request.session:
        return render(request,'c.html')
    else:
        return redirect('login')

def feedback(request):
    # c=contacts.objects.all()
    if request.method == 'POST':
        data=contacts()
        data.name=request.POST['name']
        data.email=request.POST['email']
        data.feedback=request.POST['feedback']
        data.save()
    return render(request,'feedback.html')

from .encrypt_util import encrypt,decrypt

def reg(request):
    if request.method=='POST':
        data = register()
        data.name = request.POST['name']
        data.email = request.POST['email']
        data.mob = request.POST['mob']
        encrypted_pass = encrypt(request.POST['password'])
        # data.password = encrypted_pass
        print(encrypted_pass,22222222222222222222222)
        decrypted_pass = decrypt(encrypted_pass)
        print(decrypted_pass,33333333333333)
        # print(data.password,11111111111111111)
        a = register.objects.filter(email = request.POST['email'])
        if len(a) <= 0:
            data.save()
        else:
            return render(request,'register.html',{'m':'User already exist!'})

        # print(name,email,mob,password)

    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        email1= request.POST['email']
        pass1 = request.POST['password']
        try:
            a=register.objects.get(email=email1,password=pass1)
            if a:
                request.session['user']=a.email
                request.session['userid']=a.pk
                return redirect('h')
            else:
                return render(request,'login.html',{'m':'invalid password'})
        except:
                return render(request,'login.html',{'m':'invalid password'})
    return render(request,'login.html')

# def logout(request):
#     if 'user' in request.session.keys():
#         del request.session['user']
#         return redirect('login')                      
#     return redirect('login')

# def reg(request):
#     obj = regif(request.POST)
#     # print(obj)
#     if obj.is_valid():
#         z = register.objects.filter(email = request.POST['email'])
#         if len(z)<=0:
#             obj.save()
#             return redirect('login')
#         else:
#             return render(request,'register.html',{'x':'user already exists!!'})
#     return render(request,'register.html')

def home(request):
    if 'user' in request.session:
        # del request.session['user']
        return redirect('index')
    return render(request,'c.html')


# def change(request):
#     if request.method=='POST':
#             a=register()
        # try:
            # n = request.POST['email']
            # m = request.POST['newemail']
            # xyz = register.objects.get(email=n)
            # if xyz:
            #     xyz.email=m
                # register.objects.update(id=m) 
                # xyz.save()
                # return redirect('home')
            # else:
            #     return render(request,'update.html',{'k3':'Enter valid email id'})
        # except:
        #         return render(request,'update.html',{'k3':'Enter valid email id'})
    # return render(request,'update.html')

def profile(request):
    if 'user' in request.session:
        xyz = register.objects.get(email = request.session['user'] )
        if request.method == 'POST':
            xyz.name = request.POST['name']
            xyz.mob = request.POST['mob']
            xyz.save()
        return render(request,'profile.html',{'data':xyz})
    else:
        return redirect('login')

def change(request):
    if request.method == 'POST':
        a = register()
        # a.email = reques
        # t.POST['email']
        try:
            xyz = register.objects.get(email = request.session['user'])
            print(xyz)
            if xyz.password==request.POST['password']:
                xyz.password = request.POST['npassword']
                xyz.save()
            else:
                return render(request,'update.html',{'k3':'Enter valid password'})
        except:
            return render(request,'update.html',{'k3':'Enter valid password'})
    return render(request,'update.html')
   

def logout(request):
    if 'user' in request.session:
        del request.session['user']
        return redirect('login')
    elif 'user1' in request.session:
        del request.session['user1']
        return redirect('vlogin')
    return render(request,'login.html')


def cproduct(request,id):
    if 'user' in request.session:
        a=product.objects.filter(category=id)
        b=register.objects.get(email = request.session['user'])
        return render(request,'product.html',{'proid':a,'d':b})
    elif 'user1' in request.session:
        a=product.objects.filter(category=id)
        b=vendors.objects.get(email = request.session['user1'])
        return render(request,'product.html',{'proid':a,'k1':b})
    else:
       return redirect('login')
    
def allproducts(request):
    if 'user' in request.session:  
        a=product.objects.all()
        b=register.objects.get(email = request.session['user'])
        return render(request,'product.html',{'proid':a,'d':b})
    else:
        return redirect('login')
    

def prodetails(request,id):
    if 'user' in request.session:
        a=product.objects.get(id=id)
        c=register.objects.get(email = request.session['user'])
        if request.POST:
            b=cartadmin()
            b.orderid="0"
            b.productid=a.pk
            b.userid=request.session['userid']
            b.quantity=request.POST['quantity']
            b.price = a.price
            b.tprice = int(b.quantity) * a.price
            # proid = cartadmin.objects.filter(productid = a.pk)
            p = cartadmin.objects.filter(userid = request.session['userid']) & cartadmin.objects.filter(productid=a.pk) & cartadmin.objects.filter(orderid="0")
            if len(p)>0:
                return render(request,'prodetails.html',{'k':a,'a':'already che','d':c})
            else:
                if a.qty>0:
                    if int(b.quantity)>a.qty:
                        return render(request,'prodetails.html',{'k':a,'j':'ocha kr','d':c})
                    else:
                        b.save()
                        a.qty=int(a.qty)-int(b.quantity)
                        a.save()
                        return redirect('cart')
                else:
                    return render(request,'prodetails.html',{'k':a,'s':'kale avje','d':c})
        return render(request,'prodetails.html',{'k':a,'d':c})
    else:
        return redirect('login')


def cart(request):
    if 'user' in request.session:
        c=register.objects.get(email = request.session['user'])
        a=cartadmin.objects.filter(userid=request.session['userid']) & cartadmin.objects.filter(orderid="0")
        subtotal=0
        totalq=0
        cartset = []
        for i in a:
            subtotal+=int(i.tprice)
            totalq+=int(i.quantity)
            e=product.objects.get(id=i.productid)
            id=i.pk
            pn = e.name
            pq = i.quantity
            pp = i.price
            pi = e.image
            pd = e.discription
            cartdict={'id':id,'pn':pn,'pq':pq,'pp':pp,'pi':pi,'pd':pd}
            cartset.append(cartdict)
            # print(cartset)
        return render(request,'cart.html',{'d':c,'cartset':cartset,'totalpro':len(cartset),'subtotal':subtotal,'tquantity':totalq})
    else:
        return redirect('login')

def additem(request,id):
    if 'user' in request.session:
        d=register.objects.get(email = request.session['user'])
        c=cartadmin.objects.get(id=id)
        b=product.objects.get(id=c.productid)
        a=cartadmin.objects.filter(userid=request.session['userid']) & cartadmin.objects.filter(orderid="0")
        subtotal=0
        cartset = []
        c.tprice=int(c.quantity)*int(c.price)
        for i in a:
            subtotal+=int(i.tprice)
            e=product.objects.get(id=i.productid)
            id=i.pk
            pn = e.name
            pq = i.quantity
            pp = i.price
            pi = e.image
            ptp = i.tprice
            pd = e.discription
            cartdict={'id':id,'pn':pn,'pq':pq,'pp':pp,'pi':pi,'tpt':ptp,'pd':pd}
            cartset.append(cartdict)
        if 'plus' in request.POST:
            if b.qty == 0:
                return render(request,'cart.html',{'d':d,'cartset':cartset,'s':'kale avje','totalpro':len(cartset),'subtotal':subtotal})
            else:
                c.quantity = int(c.quantity)+1
                c.tprice = int(c.quantity) * int(c.price)
                b.qty=b.qty-1
                b.save()
                c.save()
                return redirect('cart')
    else:
        return redirect('login')
    
def removeitem(request,id):
    if 'user' in request.session:
        c=cartadmin.objects.get(id=id)
        a=cartadmin.objects.filter(userid=request.session['userid']) & cartadmin.objects.filter(orderid="0")
        subtotal=0
        c.tprice=int(c.quantity)*int(c.price)
        subtotal-=int(c.tprice)
        if int(c.quantity) == 1:
            b=product.objects.get(id=c.productid)
            b.qty=b.qty+1
            b.save()
            c.delete()
            return redirect('cart') 
        else:
            c.quantity=int(c.quantity)-1
            c.tprice=int(c.quantity)*int(c.price)
            b=product.objects.get(id=c.productid)
            b.qty=b.qty+1
            c.save()
            b.save()
            return redirect('cart') 
    else:
        return redirect('login')

def removeall(request,id):
    if 'user' in request.session:
        a=cartadmin.objects.get(id=id)
        b=product.objects.get(id=a.productid)
        b.qty+=int(a.quantity)
        b.save()
        a.delete()
        return redirect('cart')
    else:
        return redirect('login')

def removeselected(request):
    print(55555555555555)
    if 'user' in request.session:
        print(4444444444444)
        if request.method == 'POST':
        # if 'rselected' in request.POST:
            print(3333333333333333)
            selected_products = request.POST.getlist('product')
            cartadmin.objects.filter(id__in=selected_products).delete()
            # print(selected_products,222222222)
            # for i in selected_products:
            #     cartadmin.objects.get(id = i)
            return redirect('cart')
        else:
            print(55555)
            return redirect('cart')
    else:
        return redirect('login')

from django.db.models import Q
    
def search(request):
    if 'user' in request.session:
        d=request.session['user']
        word = request.GET.get('search')
        wordset=word.split(" ")
        # print(wordset)
        for j in wordset:
            a=product.objects.filter(Q(category__name__icontains=j)|Q(name__icontains=j)|Q(price__icontains=j)).distinct()
        return render(request,'product.html',{'proid':a,'d':d})
    else:
        word = request.GET.get['search']
        wordset=word.split(" ")
        for j in wordset:
            a=product.objects.filter(Q(category__name__icontains=j)|Q(name__icontains=j)|Q(price__icontains=j)).distinct()
        return render(request,'product.html',{'proid':a})
    
def buynow(request):
    if 'user' in request.session:
        d=register.objects.get(email = request.session['user'])
        cartdetails=cartadmin.objects.filter(userid=request.session['userid']) & cartadmin.objects.filter(orderid="0")
        proset=[]
        ta=0
        for i in cartdetails:
            prodetails=product.objects.get(id=i.productid)
            pn=prodetails.name
            pd=prodetails.discription
            pi=prodetails.image
            pp=prodetails.price
            pq=i.quantity
            ta+=int(i.tprice)
            prodict = {'pn':pn,'pd':pd,'pi':pi,'pp':pp,'pq':pq}
            proset.append(prodict)
        ordrdetail=order()
        if request.method == 'POST':
            ordrdetail.userid = request.session['userid']
            # ordrdetail.productid = prodetails.pk
            ordrdetail.name = request.POST['name']
            ordrdetail.email = request.POST['email']
            ordrdetail.address = request.POST['address']
            ordrdetail.city = request.POST['city']
            ordrdetail.state = request.POST['state']
            ordrdetail.pincode = request.POST['pincode']
            ordrdetail.paymentvia = request.POST['paymentvia']
            if ordrdetail.paymentvia == 'cod':
                ordrdetail.transactionid = ''
                ordrdetail.save()
                ordrid = order.objects.latest('id')
                cartordrid=cartadmin.objects.filter(userid=request.session['userid']) & cartadmin.objects.filter(orderid="0")
                for i in cartordrid:
                    i.orderid = ordrid.pk
                    i.save()
                # return render(request,'checkout.html',{'d':d,'q':ordrdetail})
                request.session['orderid'] = ordrid.pk
                return redirect('invoice')
            else:
                request.session['usershippingid'] = request.session['userid']
                request.session['usershippingname'] = request.POST['name']
                request.session['usershippingemail'] = request.POST['email']
                request.session['usershippingmob'] = request.POST['mob']
                request.session['usershippingaddress'] = request.POST['address']
                request.session['usershippingcity'] = request.POST['city']
                request.session['usershippingstate'] = request.POST['state']
                request.session['usershippingpincode'] = request.POST['pincode']
                request.session['usershippingpigamount'] =  str(ta)
                request.session['usershippingpayment'] = "Online"
                request.session['usershippingpaymethod'] = "RazorPay"
                request.session['usertransactionid'] = ""
                return redirect('Razorpay')
        return render(request,'checkout.html',{'d':d,'proset':proset,'ta':ta,'q':ordrdetail}) 
    else:
        return redirect('login')
    
def history(request):
    if 'user' in request.session:
        b=register.objects.get(email = request.session['user'])
        cartdata = cartadmin.objects.filter(userid = request.session['userid']) 
        subtotal = 0
        proset=[]
        dtlist=[]
        for i in cartdata:
            if i.orderid != "0":
                orderdetail = order.objects.filter(id = i.orderid)
                for j in orderdetail:
                    orderdate = j.orderdt
                    # orderdt = {'od':orderdate} 
                    # dtlist.append(orderdt)
                # subtotal+=int(i.tprice)
                    prdetails=product.objects.get(id=i.productid)
                    pn=prdetails.name
                    pd=prdetails.discription
                    pi=prdetails.image
                    pp=prdetails.price
                    pq=i.quantity
                    pt = i.tprice
                    prodict = {'pn':pn,'pd':pd,'pi':pi,'pp':pp,'pq':pq,'pt':pt,'od':orderdate}
                    proset.append(prodict)    
                # return render(request,'history.html',{'d':b,'proset':proset,'subtotal':subtotal})    
                # print(proset)
                # print(i,'hiii')
            # return render(request,'history.html',{'d':b,'proset':proset,'subtotal':subtotal})           
        return render(request,'history.html',{'d':b,'proset':proset,'subtotal':subtotal,'odt':dtlist})           
    else:
        return redirect('login')

# def history(request):
#     if 'user' in request.session:
#         b=register.objects.get(email = request.session['user'])
#         orderdata = order.objects.filter(userid = request.session['userid'])
#         proset = []
#         for i in orderdata:
#             q=cartadmin.objects.filter(userid = request.session['userid'])
#             prodetails=product.objects.get(id=i.productid)
#             pn=prodetails.name
#             pd=prodetails.discription
#             pi=prodetails.image
#             pp=prodetails.price
#             prodict = {'pn':pn,'pd':pd,'pi':pi,'pp':pp}
#             proset.append(prodict)
#         # print(i,'hiii')
#             return render(request,'history.html',{'d':b,'proset':proset})
#         return render(request,'history.html',{'d':b,'proset':proset})  
#     else:
#         return redirect('login')

KEY_ID = 'rzp_test_iMkS2jT8I83i92'
KEY_SECRET = 'C05guXdV2Dzz84nLulNduMkb'
client = razorpay.Client(auth=(KEY_ID,KEY_SECRET))

def Razorpay(request):
    currency = 'INR'
    amount = int(request.session['usershippingpigamount']) * 100
    
    order = client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
    razorpay_order_id = order['id']
    callback_url = 'http://127.0.0.1:8000/paymenthandler/'
    context={}
    context['razorpay_order_id'] = razorpay_order_id
    context['KEY_ID'] = KEY_ID
    context['Razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
    return render(request,'RazorPay.html',context=context)

@csrf_exempt
def paymenthandler(request):
    if request.method == 'POST':
        print(6666666)  
        try:
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict={'razorpay_payment_id':payment_id,'razorpay_order_id':razorpay_order_id,'razorpay_signature':signature}

            vorder = client.utility.verify_payment_signature(params_dict)
            # if vorder is None:
                
            #     return render(request,'failed.html')
            # else:
            amount = int(request.session['usershippingpigamount']) * 100

            print(11111111111111)
                
            client.payment.capture(payment_id , amount)
            oredrdetails = order()
            oredrdetails.userid = request.session['usershippingid']
            oredrdetails.name = request.session['usershippingname']
            oredrdetails.email = request.session['usershippingemail']
            oredrdetails.mob = request.session['usershippingmob']
            print(2222222222)
            oredrdetails.address = request.session['usershippingaddress']
            oredrdetails.city = request.session['usershippingcity']
            oredrdetails.state = request.session['usershippingstate']
            oredrdetails.pincode = request.session['usershippingpincode']
            oredrdetails.orderamount = request.session['usershippingpigamount']
            oredrdetails.paymentvia = request.session['usershippingpayment']
            print(333333333333333333333)
            oredrdetails.paymentmethod = request.session['usershippingpaymethod']
            oredrdetails.transactionid = payment_id
            oredrdetails.save()
            orderlatestid = order.objects.latest('id')
            cartdetails = cartadmin.objects.filter(userid = request.session['userid']) & cartadmin.objects.filter(orderid = "0")
            for i in cartdetails:
                i.orderid = orderlatestid.pk
                i.save()
            return redirect('success')
                    # return render(request,'failed.html')         
        except:
            print(4444444444444444444444444444)
            # return HttpResponseBadRequest()
            return redirect('failed')
    else:
        print(55555555555555555555555555555555555)
        return HttpResponseBadRequest()

def success(request):
    if 'user' in request.session:
        b=register.objects.get(email = request.session['user'])
        return render(request,'success.html',{'d':b})
    else:
        return redirect('login')

def failed(request):
    if 'user' in request.session:
        b=register.objects.get(email = request.session['user'])
        return render(request,'failed.html',{'d':b})
    else:
        return redirect('login')


def invoice(request):
    if 'user' in request.session:
        user = register.objects.get(email = request.session['user'])
        orderdata = order.objects.get(id = int(request.session['orderid']))
        print(orderdata.orderamount,": orderamount",orderdata.orderdt,":orderdatetime",orderdata.userid)
        print("invoicee functionn...")
        cartdata = cartadmin.objects.filter(orderid = orderdata.id)
        totalprice = 0
        prolist = []
        for i in cartdata:
            prodata = product.objects.get(id = i.productid)
            totalprice += prodata.price
            prodict = {'proname':prodata.name,'cartqty':i.quantity,'proprice':prodata.price}
            prolist.append(prodict)
            
        return render(request,'Invoice.html',{'user':user,'orderdata':orderdata,'prolist':prolist,'totalprice':totalprice})
    else:
        return redirect('login')

from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
import pdfkit
def render_invoice_to_pdf(template_path, context):
    from django.template.loader import render_to_string
    html = render_to_string(template_path, context)
    options = {
        'page-size': 'A4',
        'encoding': 'UTF-8',
        'enable-local-file-access': None
    }
    pdf = pdfkit.from_string(html, False, options=options)
    return pdf

# def invoice_pdf(request):
#     if 'user' in request.session:
#         user = register.objects.get(email = request.session['user'])
#         orderdata = order.objects.get(id = int(request.session['orderid']))
#         print(orderdata.orderamount,": orderamount",orderdata.orderdt,":orderdatetime",orderdata.userid)
#         print("invoicee functionn...")
#         cartdata = cartadmin.objects.filter(orderid = orderdata.id)
#         totalprice = 0
#         prolist = []
#         for i in cartdata:
#             prodata = product.objects.get(id = i.productid)
#             totalprice += prodata.price
#             prodict = {'proname':prodata.name,'cartqty':i.quantity,'proprice':prodata.price}
#             prolist.append(prodict)
#         data1 = {'user':user,'orderdata':orderdata,'prolist':prolist,'totalprice':totalprice}
#         pdf = render_invoice_to_pdf('pdf.html', data1)
#         return HttpResponse(pdf, content_type='application/pdf')
#         # return render(request,'Invoice.html',{'user':user,'orderdata':orderdata,'prolist':prolist,'totalprice':totalprice})
#     else:
#         return redirect('login')

def invoice_pdf(request):
    if 'user' in request.session:
        user = register.objects.get(email=request.session['user'])
        orderdata = order.objects.get(id=int(request.session['orderid']))
        cartdata = cartadmin.objects.filter(orderid=orderdata.id)
        
        totalprice = 0
        prolist = []
        for i in cartdata:
            prodata = product.objects.get(id=i.productid)
            totalprice += prodata.price * i.quantity
            prodict = {'proname': prodata.name, 'cartqty': i.quantity, 'proprice': prodata.price}
            prolist.append(prodict)

        data1 = {
            'user': user,
            'orderdata': orderdata,
            'prolist': prolist,
            'totalprice': totalprice
        }
        
        pdf = render_invoice_to_pdf('pdf.html', data1)
        return HttpResponse(pdf, content_type='application/pdf')
    else:
        return redirect('login')



# vendor

def vsignup(request):
    if request.method=='POST':
        data = vendors()
        data.name = request.POST['name']
        data.email = request.POST['email']
        data.mob = request.POST['mob']
        data.password = request.POST['password']
        a=vendors.objects.filter(email = request.POST['email'])
        if len(a)<=0:
            data.save()
            return redirect('vlogin')
        else:
            return render(request,'vsignup.html',{'x':'User already exist!'})
    return render(request,'vsignup.html')

def vlogin(request):
    if request.method=='POST':
        email1= request.POST['email']
        pass1 = request.POST['password']
        try:
            a=vendors.objects.get(email=email1,password=pass1)
            if a:
                request.session['user1']=a.email
                request.session['userid1']=a.password
                return redirect('h')
            else:
                return render(request,'vlogin.html',{'m':'invalid password'})
        except:
                return render(request,'vlogin.html',{'m':'invalid password'})
    return render(request,'vlogin.html')


def addpro(request):
    if 'user1' in request.session:
        b=vendors.objects.get(email=request.session['user1'])
        if request.method == 'POST' and request.FILES['image']:
            a=product()
            c=category.objects.all()
            cat=request.POST['category']                                                                                                                                                            
            b=category.objects.get(id=cat)
            a.category=b
            a.image=request.FILES['image']
            a.name=request.POST['name']
            a.qty=request.POST['qty']
            a.price=request.POST['price']
            a.discription=request.POST['discription']
            a.save()
            return render(request,'addproduct.html',{'k2':c,'k1':b})
        else:
            c=category.objects.all()
            # return render(request,'addproduct.html',{'k':'Enter Valid details of product','k1':c})
            return render(request,'addproduct.html',{'k2':c})
    else:
        return redirect('login')

def addcat(request):
    if 'user1' in request.session:
        if request.POST and request.FILES['image']:
            a=category()
            a.name=request.POST['name']
            a.image=request.FILES['image']
            a.save()
            return redirect('addproduct')
        else:
            return render(request,'addcat.html')
    return render(request,'addcat.html')


from rest_framework import generics,status
from .serialize import *

class serializeusers(generics.ListCreateAPIView):
    queryset = register.objects.all()
    serializer_class = userregister_serialize

class serializeuserupdatedelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = register.objects.all()
    serializer_class = userregister_serialize
    lookup_field = 'pk'
    
from rest_framework.decorators import api_view
from rest_framework.response import Response


# this function simply returns the api we create and shows the use of decorator..
@api_view(['POST'])
def easyapi(request):
    return Response({'status':1,'content':"this is ocntent for first api.."})


# this function will fetch the data from a model and serialze its data into an api and as we 
# want to just get data from database we will use get method..
@api_view(['GET'])
def getapimodel(request):
    serializeobject = register.objects.all()
    serialize = serialize_user(serializeobject,many = True) # this is the serializer we 
                                                            # defined in serialize.py file.
    return Response({'data':serialize.data}) 


# this function allows us to form a data and store it in a specific table, 
# we are storing this in register table 

@api_view(['POST'])
def regpostapi(request):
    data = request.data
    # serializer = serialize_user(data = request.data)
    # if not serializer.is_valid():
    #     return Response({'data':"data not found..."})
    # serializer.save()
    # print(serializer,"serializer data this is....")
    serialize_user_data = serialize_user(data = request.data)
    if serialize_user_data.is_valid():
        serialize_user_data.save()
        return Response({'data':"data stored..."})   
    else:
        return Response({'data':"Something went wrong",'error':serialize_user_data.errors})

    # print(data)
    # return Response({'data':data})


# this is update function for a specific data with the help of PUT function
# In PUT function we have to pass all the columns data , it does not allow partial data

from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned


@api_view(['PUT'])
def updateapiput(request,id):
        try:
            print("line 1")
            loggedin_user = register.objects.get(id = id)
            print('line 2')
            update_user_data = serialize_user(loggedin_user,data = request.data)
            print('line 3')

            if update_user_data.is_valid():
                print('line 4')

                update_user_data.save()
                print('line 5')
                return Response({'data':"data updated"})
            else:
                print("line 6")
                return Response({'data':"data is not valid / fully updated"})
        # except:
        #         print("line 7")
                
        #         return Response({'data':"Invalid id"})
        except ObjectDoesNotExist:
            print("line 7")
            return Response({'data': "Invalid id"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return Response({'data': f"An unexpected error occurred: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# this is PATCH method same as PUT used for update but its all allows partial data updation unlike PUT

@api_view(['PATCH'])
def updateapipatch(request,id):
        try:
            print("line 1")
            loggedin_user = register.objects.get(id = id)
            print('line 2')
            update_user_data = serialize_user(loggedin_user,data = request.data,partial = True)
            print('line 3')

            if update_user_data.is_valid():
                print('line 4')

                update_user_data.save()
                print('line 5')
                return Response({'data':"data updated"})
            else:
                print("line 6")
                return Response({'data':"data is not valid / fully updated"})
        # except:
        #         print("line 7")
                
        #         return Response({'data':"Invalid id"})
        except ObjectDoesNotExist:
            print("line 7")
            return Response({'data': "Invalid id"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return Response({'data': f"An unexpected error occurred: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# this is delete operation in api and now in this function 
# we are fetching id through the url of postman or thunder client for ex: 127.0.0.1:8000/deleteapi/?id=1 
# so we dont need to pass parameter to function we can access it using request.data

@api_view(['DELETE'])
def deleteapi(request):
    try:
        id = request.GET.get('id')
        delete_user = register.objects.get(id = id)
        delete_user.delete()
        return Response({'data':"data deleted.."})
    except ObjectDoesNotExist:
        return Response({'data':"invalid id.."},status=status.HTTP_404_NOT_FOUND)
    except MultipleObjectsReturned:
        return Response({'data':'Id is not unique..'})
    except Exception as e:
        return Response({'data':e})

# now we will get data from a table the same way we did above but now the table has a foreign key, so this is example with foreign key

@api_view(['GET'])
def get_category(request):
    cat = category.objects.all()
    serialize_cat = serialize_category(cat,many = True)
    print(serialize_cat)
    return Response({'data':serialize_cat.data})


@api_view(['GET'])
def getpro(request):
    pro = product.objects.all()
    serialize_pro = serialize_products(pro,many = True)
    return Response({'data':serialize_pro.data})



from rest_framework.views import APIView


class userdata(APIView):
    
    def get(self,request):
        serializeobject = register.objects.all()
        serialize = serialize_user(serializeobject,many = True) # this is the serializer we 
                                                            # defined in serialize.py file.
        return Response({'data':serialize.data}) 

    def post(self,request):
        print(1111111111111111)
        data = request.data
        # serializer = serialize_user(data = request.data)
        # if not serializer.is_valid():
        #     return Response({'data':"data not found..."})
        # serializer.save()
        # print(serializer,"serializer data this is....")
        serialize_user_data = serialize_user(data = request.data)
        if serialize_user_data.is_valid():
            serialize_user_data.save()
            return Response({'data':"data stored..."})   
        else:
            return Response({'data':"Something went wrong",'error':serialize_user_data.errors})

        

    def put(self,request,id):
        try:
            print("line 1")
            loggedin_user = register.objects.get(id = id)
            print('line 2')
            update_user_data = serialize_user(loggedin_user,data = request.data)
            print('line 3')

            if update_user_data.is_valid():
                print('line 4')

                update_user_data.save()
                print('line 5')
                return Response({'data':"data updated"})
            else:
                print("line 6")
                return Response({'data':"data is not valid / fully updated"})
        # except:
        #         print("line 7")
                
        #         return Response({'data':"Invalid id"})
        except ObjectDoesNotExist:
            print("line 7")
            return Response({'data': "Invalid id"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return Response({'data': f"An unexpected error occurred: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        

    def patch(self,request):
        pass

    def delete(self,request):
        pass
