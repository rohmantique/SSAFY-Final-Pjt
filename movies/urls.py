from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.home, name='home'),
    path('selectmood/', views.select_mood, name='select_mood'),
    path('index/<str:mood_pk>/', views.index, name='index'),
    # path('selectmood/happy/', views.happy, name='happy'),
    # path('selectmood/hungry/', views.hungry, name='hungry'),
    # path('selectmood/low/', views.low, name='low'),
    # path('selectmood/chill/', views.chill, name='chill'),
    # path('selectmood/bored/', views.bored, name='bored'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/create/', views.create, name='create'), #리뷰작성
    


    

    
]
