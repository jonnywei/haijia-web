from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hjadmin.views.home', name='home'),
    # url(r'^hjadmin/', include('hjadmin.foo.urls')),

    url(r'^yueche/$', 'yueche.views.index'),
    url(r'^set/$', 'set.views.index'),


    url(r'^a/$', 'a.views.index'),
    url(r'^a/yueche/$', 'a.views.yueche'),
                       
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
