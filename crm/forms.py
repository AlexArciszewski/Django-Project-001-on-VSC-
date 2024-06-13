from django.forms import ModelForm

#tworzymy model na obiekcie Task z models.py importujemy więc Task z models.py

from . models import Task

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


#importujemy formularze aby korzystać z widgetów
from django import forms
#teraz importujemy z dot forms i  dot widgets password...
 
from django.forms.widgets import PasswordInput, TextInput
# są to specjalne pola...widgety
#password imput pozwala wpisac haslo ale widzimy wtedy kropki to jest dzieki django.forms.widgets
#TextInput jest dla naszego usera widzimy usera ktorego wpisujemy

class CreateUserForm(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['username', 'email', 'password1','password2' ]
        #password 1 podaj haslo a password2 to weryfikacj hasla dla usera
        


class LoginForm(AuthenticationForm):
    '''nazwa klasy może być jakakolwiek ważne aby dziedziczyła po authentication form'''
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    #tu będziemy wpisywać nasze dane z wykorzystaniem widgetów
    
#tworze formularz na obiekcie klasy Task i musze oznaczyć poc zym dziedziczone czyli po ModelForm
#będą potrzebne metadane dla klasy więc robim podklase Meta

class TaskForm(ModelForm):
    
    class Meta:
        #model jest tworzony na bazie Task
        model = Task
        fields = '__all__'      #może być mniej np['title'] to sa atrybuty
#tworzymy templatkę






