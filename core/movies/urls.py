from django.urls import path

from movies.views.movies import (
    ReleasesView,
    TypesView,
    SearchsView,
    MovieView
)


urlpatterns = [

    # Public pages

    path('', ReleasesView.as_view(), name='releases'),
    path('index/', ReleasesView.as_view(), name='releases'),
    path('types/<str:type>/', TypesView.as_view(), name="types"),
    path('search/', SearchsView.as_view(), name='searchs'),
    path('movie/<int:id>/', MovieView.as_view(), name='movie_select'),
]