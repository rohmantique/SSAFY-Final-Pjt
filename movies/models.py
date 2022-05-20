from django.db import models
from django.conf import settings

# Create your models here.

class Mood(models.Model):
    status = models.CharField(max_length=10) #기분상태


class Movie(models.Model):
    title = models.CharField(max_length=100) #제목
    release_date = models.DateField() #개봉일
    grade = models.IntegerField() #평점
    genres = models.CharField(max_length=50) #장르
    mood = models.ManyToManyField(Mood)
    descpription = models.TextField() #줄거리
    poster_path = models.CharField(max_length=300) #포스터 이미지 경로
    bookmark = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='saved') #북마크영화


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.FloatField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')


