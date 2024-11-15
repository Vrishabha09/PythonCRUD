from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegForm , MovieForm
from .models import Movies , Movie_T

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = RegForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('display')
    else:
        form = RegForm()
    
    return render(request,'index.html')

def display(request): 

    trailor = Movie_T.objects.all()
    objects = Movies.objects.all()
    return render(request,'display.html',{'objects':objects,'trailor':trailor})

def trailor(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)  # Handle both data and file uploads
        if form.is_valid():
            form.save()
            return redirect('display')  # Redirect to display page after successful submission
        else:
            print(form.errors) 
    else:
        form = MovieForm()
    return render(request, 'trailor.html',{'form':form})

def admin_home(request):
    movies = Movies.objects.all()
    movie_trailers = Movie_T.objects.all()
    return render(request, 'admin.html', {'movies': movies, 'movie_trailers': movie_trailers})

# Add a movie
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_home')
    else:
        form = MovieForm()
    return render(request, 'add_movie.html', {'form': form})

# Update a movie
def update_movie(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    if request.method == "POST":
        form = RegForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('admin_home')  # Redirect to a page that lists movies
    else:
        form = RegForm(instance=movie)
    return render(request, 'edit_movie.html', {'form': form, 'movie': movie})

# Delete movie
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    if request.method == "POST":
        movie.delete()
        return redirect('admin_home')  # Redirect to a page that lists movies
    return render(request, 'delete_movie.html', {'movie': movie})