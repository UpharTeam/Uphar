from django.urls import path
from . import views

urlpatterns = [
    path("viewCategory",views.viewCategory,name="viewCategory"),
    path("createinc",views.createinc,name="createinc"),
    path("createcat",views.createcat,name="createcat"),
    path("createop",views.createop,name="createop"),
    path("viewinc",views.viewinc,name="viewinc"),
    path('viewcom/',views.viewcom,name="viewcom"),
    path('comupdate/<int:id>',views.comupdate,name="comupdate"),
    path('catdel/<int:id>',views.catdel,name="catdel"),
    path('comdel/<int:id>',views.comdel,name="comdel"),
    path('catupdate/<int:id>',views.catupdate,name="catupdate"),
    path('incupdate/<int:id>',views.incupdate,name="incupdate"),
    path('incdelete/<int:id>',views.incdelete, name = "incdelete"),
    path('incex',views.incex, name = "incex")
]
