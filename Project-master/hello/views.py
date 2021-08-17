
from django.shortcuts import render,get_object_or_404,redirect
from .models import cat,com,inc
from django.contrib import messages
from django.http import HttpResponse
from .forms import catform,comform,incform
import smtplib
import email.message
import csv
# Create your views here.

# category's crud...........................

def createcat(request):
    if request.method == "POST":
            if request.POST.get('ccca')and request.POST.get('ccde'):
                savest=cat()
                savest.catn=request.POST.get('ccca')
                savest.dhmail=request.POST.get('ccde')
                savest.save()
                messages.success(request,' The Record ' +savest.catn+ ' Is Saved Successfully..! ')
                return redirect('hello:viewCategory')
    else:
        results=cat.objects.all()
        return render(request,"createcat.html",{"crudst":results})
    return render(request,"createcat.html")

def viewCategory(request):
    results=cat.objects.all()
    return render(request,"viewCategory.html",{"crudst":results})

def catupdate(request,id):
    stupdate=cat.objects.get(id=id)
    form=catform(request.POST,instance=stupdate)
    if form.is_valid():
        form.save()
        messages.success(request,"The category Record is updated Successfully")
        return redirect('hello:viewCategory')
    return render(request,'catedit.html',{"stupdate":stupdate})

def catdel(request,id):
    delcat=cat.objects.get(id=id)
    delcat.delete()
    return redirect('hello:viewCategory')

# Company's CRUD...................

def createop(request):
    if request.method == "POST":
            if request.POST.get('cocn')and request.POST.get('coch')and request.POST.get('cocp'):
                savest=com()
                savest.coname=request.POST.get('cocn')
                savest.cohmail=request.POST.get('coch')
                savest.copmail=request.POST.get('cocp')
                savest.save()
                messages.success(request,' The Record ' +savest.coname+ ' Is Saved Successfully..! ')
                return redirect('hello:viewcom')
    else:
        results=com.objects.all()
        return render(request,"createop.html",{"crudst":results})
    return render(request,"createop.html")

def viewcom(request):
    results=com.objects.all()
    return render(request,"VIewCom.html",{"crudst":results})

def comupdate(request,id):
    stupdate=com.objects.get(id=id)
    form=comform(request.POST,instance=stupdate)
    if form.is_valid():
        form.save()
        messages.success(request,"The company Record is updated Successfully")
        return redirect('hello:viewcom')
    return render(request,'comedit.html',{"crudst":stupdate})

def comdel(request,id):
    delcom= com.objects.get(id=id)
    delcom.delete()
    return redirect('hello:viewcom')


# Incident's CRUD..............................
def createinc(request):
    xyz=cat.objects.all()
    form = com.objects.all()
    if request.method=="POST":
        form1=inc()
        form1.incdes=request.POST.get('incdes')
        form1.buildname=request.POST.get('buildname')
        form1.wardname=request.POST.get('wardname')
        form1.roomname=request.POST.get('roomname')
        form1.bedname=request.POST.get('bedname')
        form1.catname=request.POST.get('catname')
        form1.opname=request.POST.get('opname')
        form1.save()
        incident1=f'''
incident {form1.incdes}
Building Name {form1.buildname}
Ward Name {form1.wardname}
Room  Number {form1.roomname}
Bed  Number {form1.bedname}
Category  {form1.catname}
Operator name {form1.opname}


This is an auto generated mail

'''
        temp=cat.objects.get(catn=form1.catname)
        mail=[]
        mail.append(temp.dhmail)
        temp=com.objects.get(coname=form1.opname)
        mail.append(temp.cohmail)
        mail.append(temp.copmail)
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login("UphaRProjecT@gmail.com","uphar007")
        s.sendmail("UphaRProjecT@gmail.com",mail,incident1)
        return redirect('hello:viewinc')
    return render(request,"createinc.html",{'xyz':xyz,'form':form})

def viewinc(request):
    results=inc.objects.all()
    return render(request,'viewinc.html',{"crudst":results})


def incupdate(request,id):
    incupdate=inc.objects.get(id=id)
    form=incform(request.POST,instance=incupdate)
    if form.is_valid():
        form.save()
        messages.success(request,"The incedent Record is updated Successfully")
        return redirect("hello:viewinc")
    return render(request,'incedit.html',{"incupdate":incupdate})


def incdelete(request,id):
    delinc=inc.objects.get(id=id)
    delinc.delete()
    return redirect('hello:viewinc')

def incex(request):
    pat=inc.objects.all()
    response= HttpResponse(content_type='text/csv')
    response['Content-Disposition']='filename="incedent.csv"'
    writer =csv.writer(response)
    writer.writerow(['Incedent Description','Building Name','Ward','Room Number','Bed Number','Category','Opeartor'])
    for i in pat:
        writer.writerow([i.incdes,i.buildname,i.wardname,i.roomname,i.bedname,i.catname,i.opname])


    return response