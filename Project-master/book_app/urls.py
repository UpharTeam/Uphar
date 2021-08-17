from django.urls import path,include
from .  import views
urlpatterns = [
    
    path('',views.book_appo , name = "book"),
    path('show_app',views.show_appo , name = "show_app"),
    
    
    
]
