from django.shortcuts import render
from .models import book
from .forms import newform
from django.contrib import messages

#Booking Appointment from user side
def book_appo(request):
    form = newform(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,'Your appoinement is book with doctor.')
    return render(request,'book_appoinement.html',{'form':form})
 
#Showing Booked appointments to admin {app:admin1}   
def show_appo(request):
    results=book.objects.all()
    return render(request,'appointments.html',{'book':results})



