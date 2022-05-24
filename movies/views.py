from django.shortcuts import get_object_or_404, render, redirect
from .forms import MoodForm, ReviewForm
import random
from pprint import pprint
from .models import Movie
import random

# Create your views here.
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
        '4' : ['Music', 'Tv Movie', 'Drama', 'Family', ],
        '5' : ['Adventure', 'Comedy', 'Fantasy', 'Romance', ],
        '6' : ['Action', 'Western', 'Science Fiction', 'Fantasy', ],
        '7' : ['Thriller', 'War', 'Science Fiction', 'Horror', ]
    }

    # 추천 알고리즘
    data = []
    movies = Movie.objects.all().order_by('-grade')[:50]
    randomlst = [random.choice(movies) for i in range(10)]
    for genre in mood[f'{mood_pk}']:
        for movie in randomlst:
            if genre in movie.genres:
                data.append(movie)

    context = {
        'data': data,
    }

    return render(request, 'movies/index.html', context)


def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    context = {
        'movie': movie,
        # 'release_date' : movie.release_date[-4:],
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
