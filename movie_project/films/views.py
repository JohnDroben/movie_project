from django.shortcuts import render, redirect
from .forms import FilmForm
from .models import Film

def add_film(request):
    error = None
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('films_list')
    else:
        error = "Данные были заполнены некорректно"

    form = FilmForm()
    return render(request, 'films/add_film.html', {'form': form, 'error': error})

def films_list(request):
    films = Film.objects.all()
    return render(request, 'films/films_list.html', {'films': films})