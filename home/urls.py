#from django.contrib import admin
from django.urls import path
from home import views
#url dispaching
urlpatterns = [
    path("",views.index,name="homepage"),
    path("about",views.about,name="aboutpage"),
    path("services",views.services,name="aboutpage"),
    path("contact",views.contact,name="aboutpage"),
    
]
