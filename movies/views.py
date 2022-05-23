from django.shortcuts import get_object_or_404, render, redirect
from .forms import MoodForm
import requests
import random
from pprint import pprint
from .models import Movie

# Create your views here.
def home(request):
    return render(request, 'movies/home.html')

def select_mood(request):
    # if request.method == 'POST':
    #     form = MoodForm(request.POST)
    #     if form.is_valid():
    #         mood = form.save()
    #         return redirect('movies:selected_mood', mood.pk)
    # else:
    #     form = MoodForm()

    # context = {
    #     'form': form,
    # }
    # return render(request, 'movies/select_mood.html', context)
    return render(request, 'movies/select_mood.html')

def selected_mood(request, mood_pk):
    
    return render(request, 'movies/selected_mood.html')

def joy(request):
    movies = Movie.objects.order_by('grade')[:10]

    # saved = Movie.objects.get('bookmark')

    context = {
        'movies': movies,
        # 'saved' : saved,
    }

    return render(request, 'movies/joy.html', context)

def gloomy(request):

    return render(request, 'movies/gloomy.html')

def active(request):
   
    return render(request, 'movies/active.html',)

def relax(request):
    return render(request, 'movies/relax.html')

def sad(request):
    return render(request, 'movies/sad.html')

def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)
