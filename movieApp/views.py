from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Movie
from .forms import RegistrationForm

User = get_user_model()

def flatten_list_of_lists(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]

def get_unique_genres():
    genres_nested = Movie.objects.values_list('genres', flat=True).distinct()
    genres_flat = flatten_list_of_lists(genres_nested)
    return list(set(genres_flat))
    


unique_genres = get_unique_genres(),
movies = Movie.objects.all()

def my_view(request):
    users = User.objects.all()

#login page
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('movie_list')  # Redirect to your home page
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'movieApp/login.html')

#user registration page
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to your home page after registration
    else:
        form = RegistrationForm()

    return render(request, 'movieApp/register.html', {'form': form})

#movie list page. Page of all datapoints
@login_required
def movie_list(request):
    username = request.user.username

    return render(request, 'movieApp/movie_lists.html', {'movies': movies, 'username': username})

#feature enhancement and filter for preprocessing
@login_required
def feature_enhancements(request):
    #unique_genres = set(genre for movie in movies for genre in movie.objects)

    # Create a context dictionary
    context = {
        'movies': movies,
        'unique_genres': unique_genres,
    }
    print("CONTEXT", context, " CONTEXTTTTTTTTT")

    return render(request, 'myapp/feature_enhancements.html', movies)
    
@login_required
def recommendations(request):
    return render(request, 'movieApp/recommendations.html')
