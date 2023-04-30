from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.ListGames.as_view(), name='all'),
    path('posts/in/<slug>/', views.SingleGame.as_view(), name='single'),
]
