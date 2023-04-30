from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django import template
from django.urls import reverse

User = get_user_model()
register = template.Library()


class Game(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    genre = models.CharField(max_length=100, blank=True)
    platform = models.CharField(max_length=100, blank=True)
    release_date = models.DateField(blank=True, default='')
    description = models.TextField(blank=True, default='')
    game_pic = models.ImageField(upload_to='game_pics', blank=True)
    # owners = models.ManyToManyField(User, through='GameOwner')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('games:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


# class GameOwner(models.Model):
#     game = models.ForeignKey(Game, related_name='ownerships', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, related_name='user_games', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.user.username
#
#     class Meta:
#         unique_together = ('game', 'user')

