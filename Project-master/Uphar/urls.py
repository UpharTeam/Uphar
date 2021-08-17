from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('User_Master.urls','user'))),
    path('book_app/',include(('book_app.urls','book_app'))),
    path('guide/',include(('guide.urls','guide'))),
    path('med/',include(('med.urls','med'))),
    path('Chemist_Master/',include(('Chemist_Master.urls','chemist'))),
    path('admin1/',include(('admin1.urls','admin1'))),
    path('pred/',include(('pred.urls','pred'))),
    path('hello/',include(('hello.urls','hello'))),
]
