from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from movies.models import movie
from  movies.utils import extract_youtube_id


class ReleasesView(TemplateView):
    template_name = 'movies/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['last_movies'] = movie.objects.order_by('-release_date')[:10]
        
        context['total_movies'] = movie.objects.all()

        context['notification'] = self.request.session.pop('notification', None)

        context['hide_include'] = False

        return context


class TypesView(TemplateView):
    template_name = 'movies/types.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        type_param = self.kwargs.get('type')

        context['total_movies'] = movie.objects.filter(
            Q(keyword_1__iexact=type_param) |
            Q(keyword_2__iexact=type_param) |
            Q(keyword_3__iexact=type_param) |
            Q(keyword_4__iexact=type_param)
        )

        context['type'] = type_param.upper()

        context['hide_include'] = False

        return context


class SearchsView(TemplateView):
    template_name = 'movies/searchs.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        query = self.request.GET.get('query', '')

        search_movies = movie.objects.filter(
            Q(name__icontains=query) |
            Q(original_name__icontains=query) |
            Q(synopsis__icontains=query)
        )

        context['search_movies'] = search_movies
        context['query'] = query.upper()
        context['hide_include'] = False

        return context


class MovieView(TemplateView):
    template_name = 'movies/movie.html'

    def get(self, request, id, *args, **kwargs):
        
        movie_selected = get_object_or_404(movie, pk=id)

        movie_youtube_id = extract_youtube_id(movie_selected.movie)

        if movie_youtube_id:
            movie_embed_url   = f"https://www.youtube-nocookie.com/embed/{movie_youtube_id}"
        else:
            movie_embed_url   = None

        trailer_youtube_id = extract_youtube_id(movie_selected.trailer)

        if trailer_youtube_id:
            trailer_embed_url = f"https://www.youtube-nocookie.com/embed/{trailer_youtube_id}"
        else:
            trailer_embed_url = None

        context = {
            'details': movie_selected,
            'movie_embed_url': movie_embed_url,
            'trailer_embed_url': trailer_embed_url,
        }

        return render(request, self.template_name, context)