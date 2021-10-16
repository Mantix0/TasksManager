from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name = 'home'),
    path('about-us', views.about,name = 'about'),
    path('create', views.create,name = 'create'),
    path('weather', views.weather,name = 'weather'),
    path('<int:pk>/delete', views.TaskDeleteView.as_view(),name = 'delete'),
    path('<int:pk>/w_delete', views.WTaskDeleteView.as_view(), name='w_delete'),
    path('<int:pk>/update', views.TaskUpdateView.as_view(),name = 'update'),

]
