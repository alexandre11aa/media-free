from django.contrib import admin
from .models import movie

@admin.register(movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 
                    'name', 
                    'release_date', 
                    'duration', 
                    'imdb', 
                    'keyword_1', 
                    'keyword_2', 
                    'keyword_3', 
                    'keyword_4')
    
    search_fields = ('name', 
                     'original_name', 
                     'direction')
    
    list_filter = ('release_date', 
                   'language', 
                   'quality')

if not admin.site.is_registered(movie):
    admin.site.register(movie, MovieAdmin)