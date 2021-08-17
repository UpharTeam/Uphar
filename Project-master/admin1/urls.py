from django.urls import path
from . import views

urlpatterns = [

    # signup,signin,indexpage

    path('signup/',views.signup,name='signup'),
    path('',views.signin,name='signin'),
    path('ind/',views.index,name='ind'), 
    path('logout/',views.logout,name='logout'),

    # patients urls.......

    path('patients/',views.patients,name='patients'), 
    path('patients_add/',views.patients_add,name='patadd'),
    path('patients_edit/<int:id>',views.patients_edit,name='patedit'),
    path('patients_update/<int:id>',views.patients_update,name='patients_update'),
    path('patients_delete/<int:id>',views.patients_delete,name='patdel'),
    path('patients_print/<int:id>',views.patients_print,name='patpri'),
    path('patients_patex',views.patex,name='patex'),


    # Doctors urls.......

    path('doctors/',views.doctors1,name='doctors'),
    path('doctors_add/',views.doctors_add,name='docadd'),
    path('doctors_edit/<int:id>',views.doctors_edit,name='docedit'),
    path('doctors_update/<int:id>',views.doctors_update,name='doctors_update'),
    path('doctors_delete/<int:id>',views.doctors_delete,name='docdel'),
    path('records/',views.records,name='records'),
    path('schedule/',views.schedule,name='schedule'),
    path('doctors_schedule/',views.doctors_schedule,name='doc_sch'),
    path('doctorsUpdateSchedule/<int:id>',views.doctorsUpdateSchedule,name='DUS'),
    path('schedule_delete/<int:id>',views.schedule_delete,name='SchDel'),
    # Appointment urls........
    path('appointment_add/',views.appointment_add, name ='Appadd'),
    path('del_app/<int:id>',views.del_appointment,name='del_app'),
   
    # Forgot password urls...

    path('forgot_pass/',views.forgot_pass,name="forgotpass"),
    path('otpcheck/',views.otpcheck,name="otpcheck"),
    path('newpassword/',views.newpassword,name="newpassword"),
    
    # Medicine Prediction....
    path('medPred/',views.preMed,name='premed'),



     # Department urls.........
    path('department/',views.department, name= 'department'),

    #Accounts::Invoices,expenses....
    path('invoices/',views.invoices,name='invoices'),
    path('expenses/',views.expenses,name='expenses'),

]