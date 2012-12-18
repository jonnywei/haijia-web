from django.conf.urls import patterns, include, url

urlpatterns = patterns('a.views',

    url(r'^$', 'index'),
    url(r'^yueche/$', 'yueche'),
    url(r'^yueche/(?P<yueche_id>\d+)/$','detail'),
    url(r'^yueche/(?P<yueche_id>\d+)/update/$','update'),
    url(r'^cookie/all/$','cookie_all'),
    #url(r'^cookie/imagecode/$','cookie_imagecode'),
    #url(r'^cookie/bookcode/$','cookie_bookcode'),
                      
    url(r'^cookie/add/$','cookie_add'),
    url(r'^config/$','config'),
    
)
