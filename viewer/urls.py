from django.urls import path

from viewer.views import MoviesView, MovieCreateView, MovieUpdateView, MovieDeleteView, AuthorsView, AuthorCreateView, \
    AuthorUpdateView, AuthorDeleteView, GenresView, GenreCreateView, GenreUpdateView, GenreDeleteView

urlpatterns = [    # MOVIES
    path('movies/', MoviesView.as_view(), name='movie'),
    path('movies/create', MovieCreateView.as_view(), name='movie_create'),
    path('movies/<pk>/edit', MovieUpdateView.as_view(), name='movie_update'),
    path('movies/<pk>/delete', MovieDeleteView.as_view(), name='movie_delete'),
    # AUTHORS
    path('authors/', AuthorsView.as_view(), name='authors'),
    path('authors/create', AuthorCreateView.as_view(), name='author_create'),
    path('authors/<pk>/edit', AuthorUpdateView.as_view(), name='author_update'),
    path('authors/<pk>/delete', AuthorDeleteView.as_view(), name='author_delete'),
    # GENRES
    path('genres/', GenresView.as_view(), name='genres'),
    path('genres/create', GenreCreateView.as_view(), name='genre_create'),
    path('genres/<pk>/edit', GenreUpdateView.as_view(), name='genre_update'),
    path('genres/<pk>/delete', GenreDeleteView.as_view(), name='genre_delete')
]
