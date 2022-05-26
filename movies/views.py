from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET, require_http_methods


from .models import Movie, Review, Comment
from .forms import ReviewForm, CommentForm

# Create your views here.
def select_mood(request):
    return render(request, 'movies/select_mood.html')

@login_required
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
    personal = request.user.saved.all()

    # 리뷰를 쓴 영화 제외
    rest_movies = Movie.objects.exclude(review__user=request.user).order_by('-vote_average')

    data = []
    for movie in rest_movies:
        for genre in mood[f'{mood_pk}']:
            if personal.filter(pk=movie.pk).exists():
                continue
            if genre in movie.genres:
                if movie not in data:
                    data.append(movie)
            if len(data) == 100:
                break
        if len(data) == 100:
            break

    saved = []
    for saved_movie in personal:
        if saved_movie in Movie.objects.filter(review__user=request.user):
            continue
        for genre in mood[f'{mood_pk}']:
            if genre in saved_movie.genres:
                if not saved_movie in saved:
                    saved.append(saved_movie)

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

    already_review = movie.review_set.filter(user=request.user)

    context = {
        'movie': movie,
        'genre': genre,
        'total': total,
        'reviews': reviews,
        'already_review': already_review,
    }

    return render(request, 'movies/detail.html', context)


@require_POST
def save(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user

        response = {
            'saved': False,
            'text': 'Save this film',
            'count': 0,
        }

        if movie.bookmark.filter(pk=user.pk).exists():
            movie.bookmark.remove(user)
        else:
            movie.bookmark.add(user)
            response['saved'] = True
            response['text'] = 'Already saved'
            
        response['count'] = movie.bookmark.count()
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
    }
    return render(request, 'movies/create.html', context)

@login_required
def read(request, review_pk):

    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
    
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
            return redirect('movies:read', review.pk)
    else:
        comment_form = CommentForm()

    context = {
        'review': review,
        'review_pk': review_pk,
        'comment_form' : comment_form,
        'review' : review,
        'comments' : review.comments.all(),
    }
    return render(request, 'movies/read.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def updatecomment(request, comment_pk):

    comment = Comment.objects.get(pk=comment_pk)
    review_pk = comment.review.pk

    if request.method == 'POST':
        if request.user == comment.user:
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('movies:read', review_pk)
    else:
        form = CommentForm(instance=comment)
    context = {
        'form': form,
        'review_pk': review_pk,
        'comment_pk': comment.pk,
    }
    return render(request, 'movies/update_comment.html', context)         

        
@login_required
@require_http_methods(['GET', 'POST'])
def deletecomment(request, comment_pk):

    if not request.user.is_authenticated:
        return HttpResponse('권한이 없습니다', status=401)

    comment = get_object_or_404(Comment, pk=comment_pk)
    review_pk = comment.review.pk

    if request.user == comment.user:
        comment.delete()
        return redirect('movies:read', review_pk)
    else:
        return render(request, 'movies/error.html')

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

            return redirect('movies:detail', movie.pk)
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
    return redirect('accounts:profile', request.user.username)

@login_required
@require_POST
def review_like(request, review_pk):

    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        user = request.user

        response = {
            'liked': False,
            'count': 0,
        }

        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)

        else:
            review.like_users.add(user)
            response['liked'] = True

        response['count'] = format(review.like_users.count(), ',')

        return JsonResponse(response)
    return redirect('accounts:login')
