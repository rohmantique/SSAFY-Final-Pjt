from django.db import models
from django.conf import settings

# Create your models here.

class Mood(models.Model):
    status = models.CharField(max_length=10) #기분상태


class Movie(models.Model):
    title = models.CharField(max_length=100) #제목
    release_date = models.DateField(blank=True) #개봉일
    vote_average = models.FloatField(blank=True) #평점
    vote_count = models.IntegerField(blank=True)
    genres = models.CharField(max_length=50, blank=True) #장르
    mood = models.ManyToManyField(Mood, blank=True)
    description = models.TextField(blank=True) #줄거리
    poster_path = models.CharField(max_length=300, blank=True) #포스터 이미지 경로
    bookmark = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='saved') #북마크영화


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.FloatField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')


