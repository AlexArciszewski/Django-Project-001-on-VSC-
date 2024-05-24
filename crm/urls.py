
from django.urls import path

from .import views
#jesteśmy w tym samym folderze wiec mozna zrobić import z . wiec importujemy wszystko...z crm/views
urlpatterns = [
    
    path('', views.homepage, name=""),
    
    path('task', views.task, name="task"),
    
    path('register/', views.register, name="register"),
    
    path('create-task', views.create_task, name="create-task"),
    
 #importujemy funkcje register z views.py  pod routem "register"
 
]

