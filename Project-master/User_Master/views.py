
from django.shortcuts import render,redirect,get_object_or_404
from django.http import request,HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.db.models import Q
from django.views import generic
from .models import UserRegister,cart,UserQuery
from .forms import UserRegisterForm,UserQueryForm
from Pay import Checksum
from med.models import Medicine
from guide.models import guides
from django.views.decorators.csrf import csrf_exempt
import csv  
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import random
#email
import smtplib, ssl

#time
import time
from datetime import datetime, timezone
import pytz

MERCHANT_KEY = 'Hb7gKKhWrKe%1UlX'

# User signin 
def signin(request):
    if request.POST:
        email = request.POST['uid']
        pass1 = request.POST['userpwd']
        try:
            valid = UserRegister.objects.get(uid=email,userpwd=pass1)
            if valid:
                request.session['user'] = email
                return redirect('/Userindex/')
            else:
                return render(request,'error.html')
        except:
            return render(request,'error.html')
            #  return redirect('/signin/')
    return render(request,'signin1.html')

#User logout
def logout(request):
    if 'user' in request.session.keys():
        del request.session['user']
        return redirect('user:index')
    return redirect('user:index')

#User index
def index(request):
    # if 'user' in request.session:
    #     return render(request,'index.html')
    # else:
    #     return redirect('user:index')
    return render(request,'index.html')

#User Index{This indexpage will open after doing signin}


def index1(request):
    if 'user' in request.session:
        qur=UserQueryForm(request.POST)
        if qur.is_valid():
            qur.save()
            messages.success(request,'Message sent..')
        return render(request,'index1.html',{'qur':qur})
    else:
        return redirect('user:signin')


# User register
def signup(request):
    obj=UserRegisterForm(request.POST)

    if obj.is_valid():
        obj.save()
        return HttpResponseRedirect('/signin/')    
    return render(request,'signup.html',{'obj':obj})
    

# User can search for medicines using this function
def search(request):
    try:
        serch = request.GET.get('query')
    except:
        serch = None
    if  serch:
        med = guides.objects.all().filter(Q(mname__icontains= serch) | Q(drug__icontains = serch) | Q(symptoms__icontains = serch) | Q(diseases__icontains = serch) )
        data = {
            'med':med
        }
    else:
        data={}
    return render(request,'search1.html',data)

# Forgot Password

def forgot_pass(request):
    email = request.POST.get('email')
    request.session['username'] = email
    if email == None:
        return render(request,'email.html')
        
    print(email)
    otp = ''
    rand = random.choice('0123456789')
    rand1 = random.choice('0123456789')
    rand2 = random.choice('0123456789')
    rand3 = random.choice('0123456789')
    otp = rand + rand1 + rand2 + rand3
    request.session['otp'] = otp


    port = 465
    password = "Abcd@1234"
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com",port,context=context)
    server.login("sspatel1048@gmail.com",password)
    server.sendmail("sspatel1048@gmail.com",email,otp)
    server.quit()
    return redirect('user:otpcheck')
        

    return render(request,'email.html')

def otpcheck(request):
    if request.session.has_key('otp'):
        otp = request.session['otp']
        try:
            otpobj = request.POST.get('otp')
            if otpobj == None:
                return render(request,'otp.html')
            if otp == request.POST.get('otp'):
                return redirect('user:newpassword')
            else:
                return HttpResponse("<a href = ''>Wrong OTP Entered.</a>")
        except:
            return redirect('user:signin')
    return render(request,'otp.html')

def newpassword(request):
    new_pass = request.POST.get('password')
    if request.method == 'POST':
        obj = UserRegister.objects.get(uid = request.session['username'])
        obj.userpwd = new_pass
        obj.save()
        return redirect('user:signin')
    return render(request,'forgotpassword.html')
#Add to cart 



def add_to_cart(request):
    if 'user' in request.session:
        data = request.session['user']
        ur = UserRegister.objects.get(uid=data)
        context={}
        items = cart.objects.filter(user = ur)
        context['items'] = items
        context['users'] = ur

        if request.method == "POST":
            mid = request.POST["mid"]
            qty = request.POST["qty"]
            # data = request.user.id
            is_exist =  cart.objects.filter(medicine__id = mid,user = ur,status= False)
            if len(is_exist)>0:
                context['msz'] = "Alredy in your cart"
                context['cls'] = "alert alert-warning"
            else:
                medicine = get_object_or_404(guides,id=mid)
                # usr = get_object_or_404(UserRegister,id=request.user.id)
                c = cart(user=ur ,medicine = medicine, quantity=qty)
                c.save()
                context['msz'] = "Added in your cart"
                context['cls'] = "alert alert-success"
              
        return render(request,'cart.html',context)
    else:
        return redirect('logout')

def get_cart_data(request):
    if 'user' in request.session:
        data = request.session['user']
        ur = UserRegister.objects.get(uid=data)
        items =  cart.objects.filter(user=ur, status=False)
        total,quantity = 0,0
        for i in items:
            total += float(i.medicine.package_price)*i.quantity
            request.session['order']= total
            quantity += float(i.quantity)

        res = {
            "Total":total, 
            "quan":quantity
        }
        return JsonResponse(res)
    else:
        return redirect('logout')

def change_quan(request):
    if "quantity" in request.GET:
        cid = request.GET["cid"]
        qty = request.GET["quantity"]
        cart_obj = get_object_or_404(cart,id=cid)
        cart_obj.quantity = qty
        cart_obj.save()
        return HttpResponse(cart_obj.quantity )
    
    if "delete_cart" in request.GET:
        id =request.GET["delete_cart"]
        cart_obj = get_object_or_404(cart,id=id)
        cart_obj.delete()
        return HttpResponseRedirect('/cart/')

def Process_payment(request):
    tz= pytz.timezone('Asia/Kolkata')
    time_now = datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))
    order_id = "Order"+str(millis)
    request.session['Order_id'] = order_id
    a= request.session['Order_id']
    print(a)
    amo = request.session['order']
    param_dict = {
        'MID':'qWcLys71208955621887',
        'ORDER_ID':str(request.session['Order_id']),
        'TXN_AMOUNT': str(amo),
        'CUST_ID': 'smit_patel',
        'INDUSTRY_TYPE_ID': 'Retail',
        'WEBSITE': 'WEBSTAGING',
        'CHANNEL_ID': 'WEB',
        'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest/',
    }
    param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
    return render(request, 'paytm.html', {'param_dict': param_dict})

@csrf_exempt
def Handlerequest(request):
    # paytm will send you post request here
    
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict,MERCHANT_KEY,checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful') 
           
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
            
    return render(request, 'paymentsatus.html', {'response': response_dict})