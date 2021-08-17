from django.shortcuts import render,redirect
from django.http import request,HttpResponseRedirect,HttpResponse
from Chemist_Master.models import ChemistRegister
from med.models import Medicine
from med.forms import MedicineForm
from Chemist_Master.forms import ChemistRegisterform,guideForm
from guide.models import guides
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import random
#email
import smtplib, ssl

#Chemist signin page
def chemist_signin(request):
    if request.method=="POST":
        print(request.POST['cid'])
        try:
            m = ChemistRegister.objects.get(cid=request.POST['cid'])
            if m.chemistpwd == request.POST['chemistpwd']:
                request.session['user'] = m.cid
                return redirect('chemist:ch_index')
            else:
                return render(request,'error.html')
        except:
            return render(request,'error.html')
    return render(request,'chemist_signin1.html')

# Showing uploaded medicines by chemist
def Uploaded_Medi(request):
    
        if 'user' in request.session:
            # chem = ChemistRegister.objects.get(cid=request.session['user'])
            med = guides.objects.all()
            paginator = Paginator(med, 5) # Show 10 medicines per page.
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request,'test.html',{'med':med,'page_obj': page_obj})
        else:
            return redirect('chemist:ch_signin')

            
  # Update medicine {done by chemist}   
def update_med(request,id):
    if 'user' in request.session:
        medi = guides.objects.get(id=id)  
        form = guideForm(request.POST or None, instance = medi)  
        if form.is_valid():  
            form.save()  
            return redirect('chemist:Uploaded_Medi')
        return render(request,'edit.html', {'medi': medi}) 
    else:
        return redirect('chemist:ch_signin')
 
# delete medicine{done by chemist}
def delete_med(request,id):
    med = guides.objects.get(id=id)
    med.delete()
    return redirect('chemist:Uploaded_Medi')
    
# Chemist module home page

#@login_required
def chemist_index(request):
    if 'user' in request.session:
        return render(request,'chemist_index.html')
    else:
        return redirect('chemist:ch_signin')
        
# chemist signup
def chemist_signup(request):
    obj=ChemistRegisterform(request.POST,request.FILES)
    if obj.is_valid():
        obj.save()
        return HttpResponseRedirect('/signin/')
    return render(request,'chemist_signup.html',{'obj':obj})

#chemist logout
def logout(request):
    if 'user' in request.session:
        del request.session['user']
        return redirect('chemist:ch_signin')
    else:
        return redirect('chemist:ch_signin')
#chemist forgotpassword

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
    print(otp)
    request.session['otp'] = otp


    port = 465
    password = "Abcd@1234"
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com",port,context=context)
    server.login("sspatel1048@gmail.com",password)
    server.sendmail("sspatel1048@gmail.com",email,otp)
    server.quit()
    return redirect('chemist:otpcheck')
        

    return render(request,'email.html')

def otpcheck(request):
    if request.session.has_key('otp'):
        otp = request.session['otp']
        try:
            otpobj = request.POST.get('otp')
            if otpobj == None:
                return render(request,'otp.html')
            if otp == request.POST.get('otp'):
                return redirect('chemist:newpassword')
            else:
                return HttpResponse("<a href = ''>Wrong OTP Entered.</a>")
        except:
            return redirect('chemist:ch_signin')
    return render(request,'otp.html')

def newpassword(request):
    new_pass = request.POST.get('password')
    if request.method == 'POST':
        obj = ChemistRegister.objects.get(cid = request.session['username'])
        obj.chemistpwd = new_pass
        obj.save()
        return redirect('chemist:ch_signin')
    return render(request,'forgotpassword.html')




    
