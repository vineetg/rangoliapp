from music.models import Artist, Song, Album
from django.contrib import admin

class AlbumAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['name', 'songs']}),
            ('Optional', {'fields': ['release_date', 'album_artist', \
                    'album_art']}),
    ]

admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist)
admin.site.register(Song)


