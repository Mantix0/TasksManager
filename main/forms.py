from .models import Task
from .models import City
from django.forms import ModelForm, TextInput, Textarea
from datetime import datetime


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title","task",]
        widgets = {
            "title": TextInput(attrs={

            'class': 'form-control', 'placeholder': 'Введите название'
        }),
            "task": Textarea(attrs={

            'class': 'form-control', 'placeholder': 'Введите описание'
        }),
        }
class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            "name": TextInput(attrs={

            'class': 'form-control', 'placeholder': 'Введите город','name':'city','id':'city',
        })
        }

