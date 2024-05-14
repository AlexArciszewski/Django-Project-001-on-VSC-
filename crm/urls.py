
from django.urls import path

from .import views
#jesteśmy w tym samym folderze wiec mozna zrobić import z . wiec importujemy wszystko...z crm/views
urlpatterns = [
    
    path('', views.homepage),
    
    path('task', views.task),
    
    path("register/", views.register),
    
 #importujemy funkcje register z views.py  pod routem "register"
 
]
