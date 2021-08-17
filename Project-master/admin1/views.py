from django.shortcuts import render,redirect
from admin1.models  import doctors,patient,adminapp,Doctor_Department
from .forms import AdminRegisterForm,DoctorRegisterForm,PatientRegisterForm,DoctorDEpForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from book_app.models import book 
from book_app.forms import newform
from plotly.offline import plot
from plotly.graph_objs import Scatter
from pred.forms import predform
from guide.models import guides
from django.core.paginator import Paginator

from django.template.loader import get_template
from xhtml2pdf import pisa

import csv

import random
#email
import smtplib, ssl

def signin(request):
    if request.method=="POST":
        try:
            m = adminapp.objects.get(email=request.POST['email'])
            
            if m.password == request.POST['password']:
                request.session['user'] = m.email
                return redirect('admin1:ind')

            else:
                return render(request,'error.html')
        except:
            return render(request,'error.html')
    return render(request,'login.html')

#Admin Logout
def logout(request):
    if 'user' in request.session.keys():
        del request.session['user']
        return redirect('user:index')
    return redirect('admin1:signin')




# Home Page............

def index(request):
    if 'user' in request.session:
        try:
            app = book.objects.all()
            doc = doctors.objects.all()
            count_app= book.objects.all().count() 
            count_doc= doctors.objects.all().count()
            count_pat= patient.objects.all().count()
            pat = patient.objects.all()
            paginator = Paginator(pat,1) # Show 1 pat per page.
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            
            return render(request,'ind.html',{'count_app':count_app,'count_doc':count_doc,'count_pat':count_pat,'app':app,'doc':doc,'pat':pat,'page_obj':page_obj })
        except:
            return render(request,'ind.html',{'count_app':count_app,'count_pat':count_pat,'count_doc':count_doc,'app':app,'doc':doc})
           
    else:
        return redirect('admin1:signin')
# Admin Register Page.........

def signup(request):
    obj=AdminRegisterForm(request.POST)
    if obj.is_valid():
        obj.save()
        return redirect('admin1:signin')
    return render(request,'register.html',{'obj':obj})

def admin_edit(request,id):
    getadmindetails=adminapp.objects.get(id=id)
    return render(request,'profile.html',{"adminapp":getadmindetails})
# Doctors....

def doctors1(request):
    results = doctors.objects.all()
    return render(request,'doctors.html',{"doctor":results})
    

def doctors_add(request):
    view_dep= doctors.objects.all()
    obj=DoctorRegisterForm(request.POST)
    if obj.is_valid():
        obj.save()
        return redirect('admin1:doctors')
    return render(request,'add-doctor.html',{'obj':obj,'ob':view_dep})

def doctors_edit(request,id):
    getdoctordetails=doctors.objects.get(id=id)
    return render(request,'edit-doctor.html',{"doctor":getdoctordetails})

def doctors_update(request,id):
    doctors_update=doctors.objects.get(id=id)
    form=DoctorRegisterForm(request.POST,instance=doctors_update)
    if form.is_valid():
        form.save()
        messages.success(request,"The Doctor Record is Updated Successfully..!")
        return render(request,"edit-doctor.html",{"doctor":doctors_update})

def doctors_delete(request,id):
    deldoctor=doctors.objects.get(id=id)
    deldoctor.delete()
    results=doctors.objects.all()
    return render(request,"doctors.html",{"doctor":results})

# Doctors Schedule...

def schedule(request):
    doc1=doctors.objects.all()
    doc = Doctor_Department.objects.all()
    return render(request,'schedule.html',{'doc':doc,'doc1':doc1})

def doctors_schedule(request):
    doc=doctors.objects.all()
    obj=DoctorDEpForm(request.POST)
    if obj.is_valid():
        obj.save()
        return redirect('admin1:schedule')
    return render(request,'add-schedule.html',{'obj':obj,'doc':doc})

def doctorsUpdateSchedule(request,id):
    doc_schedule=Doctor_Department.objects.get(id=id)
    form=DoctorDEpForm(request.POST,instance=doc_schedule)
    if form.is_valid():
        form.save()
        messages.success(request,"The Doctor Record is Updated Successfully..!")
    return render(request,"edit-schedule.html",{"doctor":doc_schedule})

def schedule_delete(request,id):
    deldoctor=Doctor_Department.objects.get(id=id)
    deldoctor.delete()
    return redirect('admin1:schedule')


# Patients........

def patients(request):
    results=patient.objects.all()
    return render(request,'patients.html',{"patient":results})

def patients_add(request):
    obj=PatientRegisterForm(request.POST)
    if obj.is_valid():
        obj.save()
        messages.success(request,"The Patient is Successfully added")
        return redirect('admin1:patients')
    return render(request,'add-patient.html',{'obj':obj})
def patex(request):
    pat=patient.objects.all()
    response= HttpResponse(content_type='text/csv')
    response['Content-Disposition']='filename="incedent.csv"'
    writer =csv.writer(response)
    writer.writerow(['Name','DOB','Address','Phone','Email'])
    for i in pat:
        writer.writerow([i.pat_fname,i.pat_dob,i.pat_address,i.pat_mob,i.pat_email])


    return response

def patients_edit(request,id):
    getpatientdetails=patient.objects.get(id=id)
    return render(request,'edit-patient.html',{"patient":getpatientdetails})
    
def patients_print(request,id):
    getpatientdetails=patient.objects.get(id=id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='filename="report.pdf"'
    template=get_template('pdf1.html')
    html=template.render({'customer':getpatientdetails})

    pisa_status =pisa.CreatePDF(html,dest=response)
    if pisa_status.err:
        return HttpResponse('we have some error<pre>' +html + '</pre>')
    return response

def patients_update(request,id):
    patients_update=patient.objects.get(id=id)
    form=PatientRegisterForm(request.POST,instance=patients_update)
    if form.is_valid():
        form.save()
        messages.success(request,"The Patient Record is Updated Successfully..!")
        return render(request,"edit-patient.html",{"patient":patients_update})
    
def patients_delete(request,id):
    delpatient=patient.objects.get(id=id)
    delpatient.delete()
    results=patient.objects.all()
    return render(request,"patients.html",{"patient":results})

def records(request):
    patients_record=patient.objects.all()
    return render(request,'pat_record.html',{'pat':patients_record})


# Appoinement.........

def appointment_add(request):
    form = newform(request.POST)
    if form.is_valid():
        form.save()
        return redirect('book_app:show_app')
    return render(request,'add-appointment.html',{'form':form})
    
def del_appointment(request,id):
    delAppointment = book.objects.get(id=id)
    mail1=[]
    mail1.append(delAppointment.email)
    abc=f'''
Dear {delAppointment.name},
        Your Appointment has been booked on {delAppointment.schedule}
        Please be on scheduled time.
        Thanks and Regards
        UpharTeam
          
    '''
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("UphaRprojecT@gmail.com","uphar007")
    s.sendmail("UphaRprojecT@gmail.com",mail1,abc)
    delAppointment.delete()
    return redirect('book_app:show_app')
 
# Forgot password..........


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
    return redirect('admin1:otpcheck')
        

    return render(request,'email.html')

def otpcheck(request):
    if request.session.has_key('otp'):
        otp = request.session['otp']
        try:
            otpobj = request.POST.get('otp')
            if otpobj == None:
                return render(request,'otp.html')
            if otp == request.POST.get('otp'):
                return redirect('admin1:newpassword')
            else:
                return HttpResponse("<a href = ''>Wrong OTP Entered.</a>")
        except:
            return redirect('admin1:signin')
    return render(request,'otp.html')

def newpassword(request):
    new_pass = request.POST.get('password')
    if request.method == 'POST':
        obj = adminapp.objects.get(email = request.session['username'])
        obj.password = new_pass
        obj.save()
        return redirect('admin1:signin')
    return render(request,'forgotpassword.html')


 # Medicine  Prediction .....

def preMed(request):
    if 'user' in request.session:
        abc=guides.objects.all()
        form = predform(request.POST or None)
        if  form.is_valid():
            form.save()
            return redirect('pred:gra')
    return render(request,'PredictionForm.html',{'abc':abc ,'form':form})



    # At Now Only for rendering file : no backend code
def department(request):
    return render(request,'departments.html')   

def invoices(request):
    return render(request,'invoices.html') 

def expenses(request):
    return render(request,'expenses.html')
