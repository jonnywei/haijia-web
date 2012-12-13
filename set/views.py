# -*- coding: utf-8 -*-
# Create your views here.

from django.http import HttpResponse

import urllib2
import cookielib
import json
import hashlib

cj = cookielib.LWPCookieJar()

cookie_support = urllib2.HTTPCookieProcessor(cj)

opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)

urllib2.install_opener(opener)


def index(request):
    login_pic_url ="http://haijia.bjxueche.net/tools/CreateCode.ashx?key=ImgCode&random=0.3782570156516717"
    book_pic_url ="http://haijia.bjxueche.net/tools/CreateCode.ashx?key=BookingCode&random=0.3782570156516717"

    #data = urllib2.urlopen(login_pic_url).read()

    data = urllib2.urlopen(book_pic_url).read()
    
    for cookie in cj:
        print cookie
    return HttpResponse(data,"image/Gif")
