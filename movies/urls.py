from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.home, name='home'),
    path('selectmood/', views.select_mood, name='select_mood'),
    path('selectedmood/<int:mood_pk>/', views.selected_mood, name='selected_mood'),
    path('selectmood/joy/', views.joy, name='joy'),
    path('selectmood/gloomy/', views.gloomy, name='gloomy'),
    path('selectmood/active/', views.active, name='active'),
    path('selectmood/relax/', views.relax, name='relax'),
    path('selectmood/sad/', views.sad, name='sad'),
    path('<int:movie_pk>/', views.detail, name='detail'),

    

    
]
