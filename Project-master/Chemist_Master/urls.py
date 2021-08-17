from django.urls import path
from Chemist_Master.views import chemist_index,chemist_signup,chemist_signin,Uploaded_Medi,update_med,delete_med,logout,forgot_pass,otpcheck,newpassword


urlpatterns = [
    # signin,signup,indexpage
    path('signin/',chemist_signin,name="ch_signin"),
    path('signup/',chemist_signup,name="ch_signup"),
    path('',chemist_index,name="ch_index"),

    #Chemist interactions with medicines
    path('Uploaded_Medi/',Uploaded_Medi,name='Uploaded_Medi'),
    path('update_med/<int:id>',update_med,name='update_med'),
    path('delete_med/<int:id>',delete_med,name='delete_med'),
    
    #Logout
    path('logout/',logout,name='logout'),
    
    # Forgot Password
    path('forgot_pass/',forgot_pass,name="forgotpass"),
    path('otpcheck/',otpcheck,name="otpcheck"),
    path('newpassword/',newpassword,name="newpassword"),
    
]