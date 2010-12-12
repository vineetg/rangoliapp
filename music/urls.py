from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('music.views',
    (r'^$','index'),
    (r'^albums/$','album_index'),
    (r'^albums/(?P<album_id>\d+)/$','album'),
    (r'^artists/$','artist_index'),
    (r'^artists/(?P<artist_id>\d+)/$','artist'),
)
