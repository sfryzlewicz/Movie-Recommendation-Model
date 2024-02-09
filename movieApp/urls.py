from . import views
from django.urls import path
from .views import user_login, register, movie_list, recommendations, feature_enhancements
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', user_login, name='login'),
    #path("", views.index, name="index"),
    path('register/', register, name='register'),
    path('movies/', login_required(movie_list), name='movie_list'),    
    path('movies/feature_enhancements/', feature_enhancements, name='feature_enhancements'),

    path('movies/recommendations/', recommendations, name='recommendations'),
    # Add other URL patterns as needed
]