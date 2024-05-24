from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
#dodajemy import response

from .models import Task

from .forms import TaskForm


def homepage(request):

    """Tworzę  stronę startową"""
    return render(request, 'crm/index.html')

def task(request):
    
    queryDataAll = Task.objects.all()
    
    context = {'AllTasks':queryDataAll}
    
    return render(request, 'crm/task.html', context)
    
def register(request):
    """dodajemy metodę zwracającą response o stronie rejestracji i taki będzie wyglad strony co w return"""
    return render(request, 'crm/register.html')

def create_task(request):
    form = TaskForm()
    #sprawdzamy czy jest to metoda POST
    if request.method == 'POST':
        
        form = TaskForm(request.POST)
        #jeśli nie ma błedów sprawdzamy błędy
        if form.is_valid():
            
            form.save()
            
            return redirect('task')
    
    
    context = {'TaskForm': form}
    
    return render(request, 'create-task.html', context)
    #outputujemy formularze z wszystkimi polami ajkie tu mamy title i description data jest wbudowana w django
    
    