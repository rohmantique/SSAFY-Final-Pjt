from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET, require_http_methods

from .models import Movie, Review
from .forms import ReviewForm

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


@require_GET
def index(request, mood_pk):

    mood = {
        '1' : ['Comedy', 'Family', 'Fantasy', 'Romance'], 
        '2' : ['Family', 'Documentary', 'History'],
        '3' : ['Drama', 'History', 'Documentary'],
        '4' : ['Music', 'Tv Movie', 'Drama'],
        '5' : ['Action', 'Adventure', 'Mystery',],
        '6' : ['Action', 'Western', 'Fantasy'],
        '7' : ['Thriller', 'Crime', 'War', 'Horror']
    }

    # 보관함에 저장된 영화 목록
    saved = request.user.saved.all()

    # 리뷰를 쓴 영화 제외
    rest_movies = Movie.objects.exclude(review__user=request.user).order_by('-vote_average')

    data = []
    for genre in mood[f'{mood_pk}']:
        for movie in rest_movies:
            if saved.filter(pk=movie.pk).exists():
                continue
            if genre in movie.genres:
                if len(data) > 30:
                    break
                data.append(movie)
        if len(data) > 100:
            break

    context = {
        'saved': saved,
        'data': data,
        'mood_pk': mood_pk,
    }

    return render(request, 'movies/index.html', context)


@require_GET
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    i = 0
    genres = []
    while i + 1 < len(movie.genres):
        i += 1
        if list(movie.genres)[i].isalpha():
            g = str(list(movie.genres)[i])
            while list(movie.genres)[i+1].isalpha():
                i += 1
                g += str(list(movie.genres)[i])
            genres.append(g)

    if len(genres) > 2:
        genre = f'{genres[0]}/{genres[1]}'
    else:
        genre = genres[0]

    total = format(movie.vote_count, ',')

    reviews = Review.objects.filter(movie=movie).order_by('-created_at')

    context = {
        'movie': movie,
        'genre': genre,
        'total': total,
        'reviews': reviews,
    }

    return render(request, 'movies/detail.html', context)


@require_POST
def save(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user

        response = {
            'saved': False,
        }

        if movie.bookmark.filter(pk=user.pk).exists():
            movie.bookmark.remove(user)
        else:
            movie.bookmark.add(user)
            response['saved'] = True

        return JsonResponse(response)
    return redirect('accounts:login')


@login_required
def create(request, movie_pk):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)

            review.user = request.user
            review.movie = Movie.objects.get(pk=movie_pk)

            movie = Movie.objects.get(pk=movie_pk)
            movie.vote_average = round((movie.vote_average * movie.vote_count + review.score) / (movie.vote_count + 1), 1)
            movie.vote_count += 1
            movie.save()

            review.save()

            return redirect('movies:detail', movie_pk)
    else:
        form = ReviewForm()
    
    context = {
        'form': form,
        # 'mood_pk': mood_pk,
    }
    return render(request, 'movies/create.html', context)


def read(request, review_pk):
    review = Review.objects.get(pk=review_pk)

    context = {
        'review': review,
        'review_pk': review_pk,
    }
    return render(request, 'movies/read.html', context)


@login_required
def update(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    movie = Movie.objects.get(pk=review.movie.pk)
    movie.vote_average = round((movie.vote_average * movie.vote_count - review.score) / (movie.vote_count - 1), 1)
    if movie.vote_average < 0: movie.vote_average = 0.0

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()

            movie.vote_average = round((movie.vote_average * movie.vote_count + review.score) / (movie.vote_count + 1), 1)
            movie.save()

            return redirect('movies:read', review_pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        'form': form,
    }
    return render(request, 'movies/update.html', context)


@login_required
def delete(request, review_pk):
    if not request.user.is_authenticated:
        return HttpResponse('Not authorized')

    review = get_object_or_404(Review, pk=review_pk)
    
    movie = Movie.objects.get(pk=review.movie.pk)
    movie.vote_average = round((movie.vote_average * movie.vote_count - review.score) / (movie.vote_count - 1), 1)
    if movie.vote_average < 0: movie.vote_average = 0.0
    movie.vote_count -= 1
    
    review.delete()
    movie.save()
    return redirect('movies:select_mood')