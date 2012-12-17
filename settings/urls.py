from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('settings.views',
    url(r'^$', 'index'),
    url(r'^imagecode/$','image_code'),
    url(r'^bookcode/$', 'book_code'),                   
    url(r'^imagecode/img/$','image_code_get'),
    url(r'^bookcode/img/$', 'book_code_get'),
    url(r'^imagecode/add/$','image_code_add'),
    url(r'^bookcode/add/$', 'book_code_add'), 
    
    
)
