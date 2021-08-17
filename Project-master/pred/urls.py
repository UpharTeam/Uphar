from django.urls import path

from .views import graphview,hello

urlpatterns = [
    path('hello/',hello,name='hello'),
    path('a/',graphview,name='gra'),
]