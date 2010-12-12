from django.conf.urls.defaults import *
from django.views.generic import list_detail
from music.models import Album

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

album_info = {
        'queryset': Album.objects.all(),
        'template_name': 'music/album_list_page.html',
        'template_object_name':'album',
}

album_detail_info = {
        'queryset': Album.objects.all(),
        'template_name': 'music/album_detail_page.html',
        'template_object_name':'album',
}

urlpatterns = patterns('',
    # Example:
    # (r'^rangoliapp/', include('rangoliapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^music/', include('music.urls')),
    (r'^admin/', include(admin.site.urls)),
    #(r'^$', 'music.views.index'),
    #(r'^music/$', list_detail.object_list, album_info),
)
