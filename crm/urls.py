
from django.urls import path

from .import views
#jesteśmy w tym samym folderze wiec mozna zrobić import z . wiec importujemy wszystko...z crm/views
urlpatterns = [
    
    path('', views.homepage, name=""),
    
    path('view-tasks', views.tasks, name="view-tasks"),
    
    path('register/', views.register, name="register"),
    
    path('create-task', views.create_task, name="create-task"),
    
    path('update-task/<str:pk>', views.update_task, name="update-task"),
    
    path('delete-task/<str:pk>', views.delete_task, name="delete-task"),
    
 #importujemy funkcje register z views.py  pod routem "register"
    path('my-login', views.my_login, name="my-login"),
    
    path('dashboard', views.dashboard, name="dashboard"),
 
 
]


