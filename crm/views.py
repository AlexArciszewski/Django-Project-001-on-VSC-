from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
#dodajemy import response

from .models import Task

from .forms import TaskForm, CreateUserForm, LoginForm
#importujemy klase z form.py

from django.contrib.auth.models import auth
#pozwala tona autentykacje userów


from django.contrib.auth import authenticate, login, logout
#to pozwala logować sie i wylogowac z konta a authenticate to funkcja porównująca username wpisane z tym z bazy

from django.contrib.auth.decorators import login_required

#homepage/Firt page of webside

def homepage(request):

    """Tworzę  stronę startową"""
    return render(request, 'crm/index.html')


#CRUD -READ TASKs

def tasks(request):
    
    queryDataAll = Task.objects.all()
    
    context = {'AllTasks':queryDataAll}
    
    return render(request, 'crm/view-tasks.html', context)



def update_task(request, pk):
    
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)
    
    if request.method == 'POST':
        
        form = TaskForm(request.POST, instance=task)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('view-tasks')
    
    context = {'UpdateTask': form}
    
    return render(request, 'crm/update-task.html',context)     




#Registration Page    
def register(request):
    
    
    form = CreateUserForm() 
    #tworzymy zmienna i przypisujemy do niej CreateUserForm()
    if request.method == 'POST':    
    #sprawdzamy czy przekazujemy tutaj POST request...z pliku register.html  <form method="POST" autocomplete="'off" enctype="multipart/form-data">  czyli przekazujemy :)
        form = CreateUserForm(request.POST)
        
        #przygotowujemy nasze dajene z uzyciem post request
       
        if form.is_valid():
            #sprawdzamy czy formularz jest porpawny i czy nie ma bledow
            form.save()    
            #jak jest ok to pushujemy dane do bazy w sql
            return redirect('my-login')   
             #zamiast redirecta dajemy response z informacją czyli biala strona z tekstem user created
    
    context = {'RegistrationForm': form}
    #przeazaliśmy RegistrationForm'przez register.html jako context gdzie mamy klucz tego dicta 
    # w register.html w linii:    {{  RegistrationForm.as_p }}    as_p daje format tego formularza
    """dodajemy metodę zwracającą response o stronie rejestracji i taki będzie wyglad strony co w return"""
    return render(request, 'crm/register.html', context)



#CRUD Create tasks


def create_task(request):
    form = TaskForm()
    #sprawdzamy czy jest to metoda POST
    if request.method == 'POST':
        
        form = TaskForm(request.POST)
        #jeśli nie ma błedów sprawdzamy błędy
        if form.is_valid():
            
            form.save()
            
            return redirect('view-tasks')
    
    
    context = {'TaskForm': form}
    
    return render(request, 'crm/create-task.html', context)
    #outputujemy formularze z wszystkimi polami ajkie tu mamy title i description data jest wbudowana w django
    
    
# CRUD Delete tasks


def delete_task(request,pk):
    #pk to nasz pojemnik na dane
    task = Task.objects.get(id=pk)
    #jeśli jest zgodonosc z id z id z bazy to kasujemy
    #patrzymy na delete-task.html tam jest metoda POST to musimy dać if 
    if request.method == 'POST':
        
        task.delete()
        
        return redirect('view-tasks')
        #przekierowanie do strony z taskami
    
    return render(request, 'crm/delete-task.html')
#usuwam obiekt z dynamicznego urls
    
    
#Login


def my_login(request):
    
    form = LoginForm()
    
    if request.method == 'POST':
        
        form = LoginForm(request, data=request.POST)
        #uwzględniamy requesta do sprawdzenia
        #teraz sprawdzamy czy formularz jest poprawny
        if form.is_valid():
            #dodajemy import z logiką....musimy zaimportować funkcje 
            username = request.POST.get('username')
            password = request.POST.get('password')
            #chcemy get uzyskać username i password z naszej bazy na podstawie tego co napisal user w formularzu

            user = authenticate(request, username=username, password=password )
            #jak username w bazie = suerowi w formularzu
            #jeśli tak jest...
            if user is not None:
                #wtedy chcemy go dodać
                #i wtedy poniżej akceptujemy requesta dla tego usera
                auth.login(request, user)
                #zgadzamy sie na przejscie teo usera ktory został zautoryzowany

                #teraz możemy zrobić redirecta do innej strony jak user sie zgadza jest authneticated
                
                return redirect('dashboard')        #z urls.py
    #pracujemy z danymi wiec context
    context = {'LoginForm': form}
    
    return render(request,'crm/my-login.html', context)
    #otrzymujemy requesta templetke z uzupelnionym cnotextem i rpzekazujemy w context w tym slowiku dane
    
    
    
    
#Dashboard

@login_required(login_url='my-login')
def dashboard(request):
    
    return render(request, 'crm/dashboard.html')





#Logout

def user_logout(request):
    
    auth.logout(request)
    
    return redirect("")
    
    
    
    
    
    
    
    