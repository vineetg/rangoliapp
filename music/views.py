from django.template import loader, Context
from django.http import HttpResponse
from music.models import Album, Artist, Song

# TODO
# Use this shorter version for returning from view functions
#def foo_view(request):
#    return render_to_response('foo/foo_detail', {'foo': 'bar'})

def index(request):
    album_list = Album.objects.all()
    c = Context({
            'album_list':album_list,
    })
    return HttpResponse(loader.get_template('music/index.html').render(c))

def album_index(request):
    album_list = Album.objects.all()
    c = Context({
            'album_list':album_list,
    })
    return HttpResponse(loader.get_template('music/album_list_page.html').render(c))


def album(request, album_id):
    a = Album.objects.get(id=album_id)
    c = Context({
            'song_list':a.songs.all(),
            'album_name':a.name,
            'album_art':a.album_art,
    })
    return HttpResponse(loader.get_template('music/album_detail_page.html').render(c))

def artist_index(request):
    # TODO Fix the model to have artists returned in alphabetical order
    #class Meta:
    #        ordering = ('-pub_date', 'headline')
    
    artist_list = Artist.objects.order_by('name')
    c = Context({
            'artist_list': artist_list
    })
    return HttpResponse(loader.get_template('music/artist_list_page.html').render(c))

def artist(request, artist_id):
    a = Artist.objects.get(id=artist_id)
    c = Context({
            'song_list':a.song_set.all(),
            'artist_name':a.name,
            'artist_bio':a.bio,
            'artist_pic':a.pic,
    })
    return HttpResponse(loader.get_template('music/artist_detail_page.html').render(c))


