from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('selectmood/', views.select_mood, name='select_mood'),
    path('index/<str:mood_pk>/', views.index, name='index'),
    path('<str:movie_pk>/', views.detail, name='detail'),
    path('<str:movie_pk>/create/', views.create, name='create'), #리뷰작성
    


    

    
]
