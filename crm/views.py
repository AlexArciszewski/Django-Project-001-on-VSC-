from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#dodajemy import response


from .models import Task


def homepage(request):

    """Tworzę  stronę startową"""
    return render(request, 'crm/index.html')

def task(request):
    
    return render(request, 'crm/task.html')
    
def register(request):
    """dodajemy metodę zwracającą response o stronie rejestracji i taki będzie wyglad strony co w return"""
    return render(request, 'crm/register.html')

