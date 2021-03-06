# -*- coding: utf-8 -*-
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from settings.models import CookieImgCode
from django.core.urlresolvers import reverse
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
    
    output="系统设置信息"
    
    return HttpResponse(output,"text/plain;charset=utf-8")


def image_code(request):
    allCookies = CookieImgCode.objects.all()
    rparam ={'image_code_type':'imagecode','all_cookies':allCookies}
    return render_to_response('image_code.html',rparam,context_instance=RequestContext(request))

def book_code(request):
    allCookies = CookieImgCode.objects.all()
    rparam ={'image_code_type':'bookcode','all_cookies':allCookies}
    return render_to_response('image_code.html',rparam,context_instance=RequestContext(request))



def image_code_add(request):
    vicode = request.POST['vcode']
    vcookie = request.COOKIES.get('cookieImgCode','default')
    vasp_session_id=request.COOKIES.get('cookieAspSessionId','default')
    cimgcode = CookieImgCode(vcode=vicode, cookie=vcookie,asp_session_id=vasp_session_id,code_type='ImgCode')
    cimgcode.save()
    return HttpResponseRedirect(reverse('settings.views.image_code'))

def book_code_add(request):
    vicode = request.POST['vcode']
    vcookie = request.COOKIES.get('cookieBookingCode','default')
    vasp_session_id=request.COOKIES.get('cookieAspSessionId','default')
    cimgcode = CookieImgCode(vcode=vicode, cookie=vcookie,asp_session_id=vasp_session_id,code_type='BookingCode')
    cimgcode.save()
    return HttpResponseRedirect(reverse('settings.views.book_code'))



#得到海驾的imagecode图片
def image_code_get(request):

    login_pic_url ="http://haijia.bjxueche.net/tools/CreateCode.ashx?key=ImgCode&random="+str(random.random())
    cookie_value='imgcookie'
    asp_session_id='asp_session_id'
    try:
        data = urllib2.urlopen(login_pic_url).read()
        for cookie in cj:
            if (cookie.name == 'ImgCode'):
                print cookie.name, cookie.value
                cookie_value=cookie.value
            elif cookie.name == 'ASP.NET_SessionId':
                print cookie.name, cookie.value
                asp_session_id=cookie.value
            else:
                pass
    except Exception,e:
        pass
    response  =   HttpResponse(data,"image/gif")
    response.set_cookie('cookieImgCode',cookie_value)
    response.set_cookie('cookieAspSessionId',asp_session_id)
    return response
    #return HttpResponse(data,"image/gif")


#得到海驾的bookcode图片
def book_code_get(requst):
   
    book_pic_url ="http://haijia.bjxueche.net/tools/CreateCode2.ashx?key=ImgCode&random="+str(random.random())
    cookie_value='bookcookie'
    asp_session_id='asp_session_id'

    try:
        data = urllib2.urlopen(book_pic_url).read()
        for cookie in cj:
            if (cookie.name == 'ImgCode'):
                print cookie.name, cookie.value
                cookie_value=cookie.value
            elif cookie.name == 'ASP.NET_SessionId':
                print cookie.name, cookie.value
                asp_session_id=cookie.value
            else:
                pass
    except Exception,e:
        print 'error occour'
            
    
    
    response  =   HttpResponse(data,"image/gif")
    response.set_cookie('cookieBookingCode',cookie_value)
    response.set_cookie('cookieAspSessionId',asp_session_id)

    return response
    #return HttpResponse(data,"image/gif")


