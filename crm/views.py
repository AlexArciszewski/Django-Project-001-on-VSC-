from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#dodajemy import response


from .models import Task

from .forms import TaskForm


def homepage(request):

    """Tworzę  stronę startową"""
    return render(request, 'crm/index.html')

def task(request):
    
    queryDataSingle = Task.objects.get(id=3)
    
    context = {'singleTask':queryDataSingle}
    
    return render(request, 'crm/task.html', context)
    
def register(request):
    """dodajemy metodę zwracającą response o stronie rejestracji i taki będzie wyglad strony co w return"""
    return render(request, 'crm/register.html')

def task_form(request):
    form = TaskForm()
    #prypisujemy zmiennę do importortowanego formularza
    
    #teraz renderujemy modelform dict z context jak wcześniej
    
    context = {'TaskForm': form}
    
    return render(request, 'task-form.html', context)
    #outputujemy formularze z wszystkimi polami ajkie tu mamy title i description data jest wbudowana w django
    
    