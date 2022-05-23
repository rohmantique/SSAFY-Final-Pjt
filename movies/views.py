from django.shortcuts import get_object_or_404, render, redirect
from .forms import MoodForm, ReviewForm
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

def index(request, mood_pk):

    mood = {
        '1' : ['Drama', 'Family', 'Fantasy' ], 
        '2' : ['Family', 'Adventure', 'Fantasy', ],
        '3' : ['Documentary', 'History', 'Family', 'Romance', ],
        '4' : ['Music', 'Tv Movie', ],
        '5' : ['Adventure', 'Comedy', 'Fantasy', 'Romance', ],
        '6' : ['Action', 'Western', 'Science', 'Fiction', 'Fantasy', ],
        '7' : ['Thriller', 'War', 'Science Fiction', 'Horror', ]
    }

    # mood[f'{mood_pk}'] = Movie.objects.filter(genres=f'{}')



    
    return render(request, 'movies/index.html')

def joy(request):

    
    # movies = Movie.objects.filter(genres=)

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

def create(request, movie_pk):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)

            review.user = request.user
            review.save()

            return redirect('movies:detail', movie_pk)
    else:
        form = ReviewForm()
    
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)
