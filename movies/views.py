from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

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


def index(request, mood_pk):

    mood = {
        '1' : ['Drama', 'Family', 'Fantasy', 'Romance'], 
        '2' : ['Family', 'Documentary', 'History'],
        '3' : ['Thriller', 'History', 'Romance'],
        '4' : ['Documentary', 'Music', 'Tv Movie', 'Drama'],
        '5' : ['Action', 'Adventure', 'Comedy', 'Fantasy', 'Romance'],
        '6' : ['Action', 'Western', 'Fantasy'],
        '7' : ['Thriller', 'War', 'Horror']
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
                if len(data) > 50:
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


def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    context = {
        'movie': movie,
        # 'mood_pk': mood_pk,
        
    }
    print(f'mood_pk')
    return render(request, 'movies/detail.html', context)


def save(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user

    response = {
        'saved': False,
        'count': 0,
    }

    if movie.bookmark.filter(pk=user.pk).exists():
        movie.bookmark.remove(user)
    else:
        movie.bookmark.add(user)
        response['saved'] = True

    response['count'] = movie.bookmark.count()

    # return JsonResponse(response)
    return redirect('movies:detail', movie_pk)


def create(request, movie_pk):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)

            review.user = request.user
            review.movie = Movie.objects.get(pk=movie_pk)
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


def update(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
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
        return HttpResponse('Not autorized')

    review = get_object_or_404(Review, pk=review_pk)
    review.delete()
    return redirect('movies:select_mood')