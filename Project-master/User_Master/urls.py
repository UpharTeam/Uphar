from django.urls import path
from  User_Master import views


urlpatterns = [

    #User Signin,Signup,Logout,IndexpagenIndexpage1
    path('signin/',views.signin,name="signin"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.logout,name='logout'),
    path('',views.index,name="index"),
    path('Userindex/',views.index1,name="Userindex"),

    #User search function
    path('search/',views.search, name = "search"),
    
    #User Forgot Password
    path('forgot_pass/',views.forgot_pass,name="forgotpass"),
    path('otpcheck/',views.otpcheck,name="otpcheck"),
    path('newpassword/',views.newpassword,name="newpassword"),
    
    #User Add to Cart
    path('cart/',views.add_to_cart, name="cart"),
    path('getcartData/',views.get_cart_data, name = "cartData"),
    path('changedata/',views.change_quan,name="changeData"),
    path('payment_process/',views.Process_payment,name='process_payment'),
    path("handlerequest/",views.Handlerequest, name="handlerequest"),
]