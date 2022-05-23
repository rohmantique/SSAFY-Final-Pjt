from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    nickname = models.CharField(null=True, max_length=20)
    image = models.ImageField(null=True, blank=True)
