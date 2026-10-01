from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    liked = models.ManyToManyField('Post', related_name='likes')


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.author}: {self.content[:50]}"

