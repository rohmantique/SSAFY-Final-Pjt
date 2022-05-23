from django.shortcuts import render, redirect
from .forms import MoodForm
import requests
import random
from pprint import pprint

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


# 감정 하나 선택하면 해당 감정과 매칭되는 영화 목록으로 이동
# 우선 now playing에서 영화 정보 불러온 뒤
# movie id로 similar movie 불러와서 저장
# 장르별로 하나씩 정해서 if movie_id == ~~면 감정 '설렘' 으로 지정

def selected_mood(request, mood_pk):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/now_playing'
    params = {
        'api_key': '86bdc6ba5098674a46de6901a230c5f7',
        'region' : 'KR',
        # 'language' : 'kr',
    }
    response = requests.get(BASE_URL + path, params = params).json().get('results')

    movielst = []
    for movie in response:

        tmp = []
        tmp.append(movie['title'])
        tmp.append(movie['overview'])
        tmp.append(movie['release_date'])
        tmp.append('https://image.tmdb.org/t/p/w500' + movie['poster_path'])
        movielst.append(tmp)

    randomlst = random.choice(movielst)
    context = {
        'response': response,
        'movielst': movielst,
        'randomlst': randomlst
    }

    return render(request, 'movies/selected_mood.html', context)

def joy(request):
    BASE_URL = 'https://api.themoviedb.org/3'
    
    return render(request, 'movies/joy.html')

def gloomy(request):

    return render(request, 'movies/gloomy.html')

def active(request):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key' : '86bdc6ba5098674a46de6901a230c5f7',
        'region' : 'KR',
        'language' : 'kr',
        'query' : '로스트 시티'
    }
    response = requests.get(BASE_URL + path, params=params).json().get('results')
    movie_id = response[0]['id']
    BASE_URL_B = 'https://api.themoviedb.org/3'
    path_b = f'/movie/{movie_id}/recommendations'
    params_b = {
        'api_key' : '86bdc6ba5098674a46de6901a230c5f7',
        'language' : 'ko'
    }
    response_b = requests.get(BASE_URL_B + path_b ,params=params_b).json().get('results')
    movielst = []
    for movie in response_b:
        tmp = []
        tmp.append(movie['title'])
        tmp.append(movie['overview'])
        tmp.append(movie['release_date'])
        tmp.append('https://image.tmdb.org/t/p/w500' + movie['poster_path'])
        movielst.append(tmp)
    randomlst = random.choice(movielst)
    context = {
        'randomlst': randomlst,
        'movielst' : movielst,
    }

    return render(request, 'movies/active.html', context)

def relax(request):
    return render(request, 'movies/relax.html')

def sad(request):
    return render(request, 'movies/sad.html')