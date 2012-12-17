from django.conf.urls import patterns, include, url

urlpatterns = patterns('a.views',

    url(r'^$', 'index'),
    url(r'^yueche/$', 'yueche'),
    url(r'^yueche/(?P<yueche_id>\d+)/$','detail'),
    url(r'^yueche/(?P<yueche_id>\d+)/update/$','update'),

    url(r'^config/$','config'),
    
)
