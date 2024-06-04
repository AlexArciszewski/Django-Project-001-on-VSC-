from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
#dodajemy import response

from .models import Task

from .forms import TaskForm

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
    """dodajemy metodę zwracającą response o stronie rejestracji i taki będzie wyglad strony co w return"""
    return render(request, 'crm/register.html')



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
    
    return render(request, 'create-task.html', context)
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
    