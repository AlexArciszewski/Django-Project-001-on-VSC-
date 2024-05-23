from django.forms import ModelForm


#tworzymy model na obiekcie Task z models.py importujemy więc Task z models.py

from . models import Task


#tworze formularz na obiekcie klasy Task i musze oznaczyć poc zym dziedziczone czyli po ModelForm
#będą potrzebne metadane dla klasy więc robim podklase Meta

class TaskForm(ModelForm):
    
    class Meta:
        #model jest tworzony na bazie Task
        model = Task
        fields = '__all__'      #może być mniej np['title'] to sa atrybuty

#tworzymy templatkę






