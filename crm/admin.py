from django.contrib import admin
#importujemy klase task z modelem
from .models import Task, Review

# Register your models here.
admin.site.register(Task)
#rejestrujemy Task aby dało sie go odczytac w panelu admina

admin.site.register(Review)
#rejestrujemy Review aby dało sie go odczytac w panelu admina







































