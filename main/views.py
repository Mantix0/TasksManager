from django.shortcuts import render, redirect
from .models import Task, City
from .forms import TaskForm, CityForm
from django.views.generic import DeleteView, UpdateView, DetailView
import requests


# Create your views here.


class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/'
    template_name = 'main/task-delete.html'


class WTaskDeleteView(DeleteView):
    model = City
    success_url = '/weather'
    template_name = 'main/wtask-delete.html'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "main/create.html"
    form_class = TaskForm


def index(request):
    tasks = Task.objects.order_by("-id")
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def weather(request):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=4c32064793202d4996fc7a88c2e826d1"
    error = ''
    if (request.method == 'POST'):
        form = CityForm(request.POST)
        if not "city not found" in requests.get(url.format(form.data['name'])).json().values():  # Проверка на корректность города
            for c in City.objects.all():  # проверка на повторы
                if str(c) == str(form.data['name']):
                    break
            else:
                form.save()
            if len(City.objects.all()) > 5:  # ограничение по количеству городов
                City.objects.first().delete()
        else:
            error = 'Неверное название города'
    else:
        form = CityForm()
    cities = City.objects.all()
    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        try:
            city_info = {
                'city': city.name,
                "temp": res["main"]["temp"],
                "icon": res["weather"][0]["icon"],
                "id": city.id,

            }
            all_cities.append(city_info)
        except KeyError:
            City.objects.last().delete()
    context = {'all_info': all_cities, 'form': form,'error': error}
    return render(request, 'main/weather.html', context,)


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Неверная форма"
    else:
        form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
