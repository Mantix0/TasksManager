from django.db import models
from datetime import datetime

# Create your models here.

class Task(models.Model):
    title = models.CharField('Название', max_length= 50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return '/'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class City(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'