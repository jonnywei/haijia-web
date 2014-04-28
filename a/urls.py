from django.conf.urls import patterns, include, url

urlpatterns = patterns('a.views',

    url(r'^$', 'index'),
    url(r'^yueche/$', 'yueche'),
    url(r'^yueche/scan/(?P<jiaxiao_name>\w+)/$','yueche_scan'),

    url(r'^yueche/(?P<yueche_id>\d+)/$','detail'),
    url(r'^yueche/(?P<yueche_id>\d+)/update/$','update'),
    url(r'^yueche/update/$','yueche_update'),
    url(r'^xueyuan/(?P<xueyuan_id>\d+)/$','xueyuan_detail'),                   
                    
    url(r'^cookie/all/$','cookie_all'),
    #url(r'^cookie/bookcode/$','cookie_bookcode'),
                      
    url(r'^cookie/add/$','cookie_add'),
    url(r'^config/$','config'),
    url(r'^proxy/add/$','proxy_add'),
    url(r'^proxy/all/$','proxy_all'),
    
)
