from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from logging import getLogger

from viewer.forms import MovieCreateForm, AuthorCreateForm, GenreCreateForm
from viewer.models import Movie, Author, Genre

LOGGER = getLogger()


# MOVIE VIEWS
class MoviesView(ListView):
    template_name = 'movies/index.html'
    model = Movie


class MovieCreateView(LoginRequiredMixin, CreateView):
    template_name = 'movies/save.html'
    form_class = MovieCreateForm
    success_url = '/viewer/movies'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'movies/save.html'
    model = Movie
    form_class = MovieCreateForm
    success_url = '/viewer/movies'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data while updating a movie.')
        return super().form_invalid(form)


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Movie
    success_url = '/viewer/movies'


# AUTHOR VIEWS

class AuthorsView(ListView):
    template_name = 'authors/index.html'
    model = Author


class AuthorCreateView(LoginRequiredMixin, CreateView):
    template_name = 'authors/save.html'
    form_class = AuthorCreateForm
    success_url = '/viewer/authors'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'authors/save.html'
    model = Author
    form_class = AuthorCreateForm
    success_url = '/viewer/authors'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data while updating an author.')
        return super().form_invalid(form)


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Author
    success_url = '/viewer/authors'


class GenresView(ListView):
    template_name = 'genres/index.html'
    model = Genre


class GenreCreateView(LoginRequiredMixin, CreateView):
    template_name = 'genres/save.html'
    form_class = GenreCreateForm
    success_url = '/viewer/authors'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class GenreUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'genres/save.html'
    model = Genre
    form_class = GenreCreateForm
    success_url = '/viewer/genres'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data while updating an author.')
        return super().form_invalid(form)


class GenreDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Genre
    success_url = '/viewer/genres'
