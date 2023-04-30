from django.db import models
from django.urls import reverse
from django.conf import settings
from games.models import Game
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):

    CONDITION = (
        ('Brand new', 'Brand new'),
        ('Like new', 'Like new'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
    )

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    condition = models.CharField(max_length=100, choices=CONDITION, default='Good')
    message = models.TextField()
    price = models.FloatField()
    game = models.ForeignKey(Game, related_name='posts', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.game}_{self.pk}"

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username': self.user.username,
                                               'pk': self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'id']

