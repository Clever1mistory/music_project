from django.contrib import admin
from .models import Artist, Album, Song


class ArtistAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'year']


class SongAdmin(admin.ModelAdmin):
    list_display = ['track_number', 'name', 'album']


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
