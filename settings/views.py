# -*- coding: utf-8 -*-
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response

import urllib2
import cookielib
import json
import hashlib
import random

cj = cookielib.LWPCookieJar()

cookie_support = urllib2.HTTPCookieProcessor(cj)

opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)

urllib2.install_opener(opener)


def index(request):
    login_pic_url ="http://haijia.bjxueche.net/tools/CreateCode.ashx?key=ImgCode&random="+str(random.random())
    book_pic_url ="http://haijia.bjxueche.net/tools/CreateCode.ashx?key=BookingCode&random="+str(random.random())

    data = urllib2.urlopen(login_pic_url).read()

    data = urllib2.urlopen(book_pic_url).read()
    
    for cookie in cj:
        print cookie
    return HttpResponse(data,"image/gif")


def image_code(request):
    
    return render_to_response('image_code.html',{'image_code_type':'imagecode'})

def book_code(request):
    #imgage_code_type ={'image_code_type','bookcode'}
    return render_to_response('image_code.html',{'image_code_type':'bookcode'})



def image_code_add(request):
    
    return render_to_response('image_code.html',{'image_code_type':'imagecode'})

def book_code_add(request):
    #imgage_code_type ={'image_code_type','bookcode'}
    return render_to_response('image_code.html',{'image_code_type':'bookcode'})




#得到海驾的imagecode图片
def image_code_get(request):

    login_pic_url ="http://haijia.bjxueche.net/tools/CreateCode.ashx?key=ImgCode&random="+str(random.random())

    data = urllib2.urlopen(login_pic_url).read()
    
    for cookie in cj:
        if cookie.name == 'ImgCode':
            print cookie.name, cookie.value
            break
    #response  =   HttpResponse(data,"image/gif")
    #response.set_cookie('cookieImgCode',cookie.value)
    #return response
    return HttpResponse(data,"image/gif")


#得到海驾的bookcode图片
def book_code_get(requst):
   
    book_pic_url ="http://haijia.bjxueche.net/tools/CreateCode.ashx?key=BookingCode&random="+str(random.random())

    data = urllib2.urlopen(book_pic_url).read()
    
    for cookie in cj:
        print cookie
    return HttpResponse(data,"image/gif")


