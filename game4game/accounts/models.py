from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    location = models.CharField(max_length=256)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    rating = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return f'@{self.user.username}'
