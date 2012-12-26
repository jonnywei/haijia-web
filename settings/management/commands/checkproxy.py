# -*- coding: utf-8 -*-
# Create your views here.

from django.core.management import BaseCommand, CommandError
from settings.models import ProxyHost

import urllib2
import cookielib
import json
import hashlib
import random
import datetime
import time
import socket

#default_timeout = 1

#socket.setdefaulttimeout(default_timeout)
urllib2.socket.setdefaulttimeout(1) # 另一种方式

#opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)

#urllib2.install_opener(opener)


def get_cookie(cookieJar, cookie_name):
    cookie_value = None
    for cookie in cookieJar:
        if cookie.name == cookie_name :
            #print cookie.name, cookie.value
            cookie_value=cookie.value
            break
    return cookie_value
    

def test_proxy(ip,port):

    cj = cookielib.LWPCookieJar()

    ck = cookielib.Cookie(version=0, name='client_cookie', value='client_cookie', port=None, port_specified=False, domain='.sohu.com', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)

    cj.set_cookie(ck)

    cookie_support = urllib2.HTTPCookieProcessor(cj)

    #print (u'http://%s:%d' % (ip, port))             
    proxy_handler = urllib2.ProxyHandler({'http':(u'http://%s:%d' % (ip, port))})

    my_opener = urllib2.build_opener(cookie_support, proxy_handler)
    try:
        
        response = my_opener.open("http://w.sohu.com/t2/reqinfo.do",timeout=10)

        content = response.read()
        
        #.stdout.write((u' %s \r\n' % ( content)))
        
        json.loads(content)

        print content
        
        if get_cookie(cj, 'client_cookie')=='client_cookie' and get_cookie(cj, 'cookie_test')=='true':

            return True;
       
        
    except Exception,er:
        print er
    
    return False

    #导入cookie支持


class Command(BaseCommand):
    help = 'check proxy is or not alive'
    def handle(self, *args, **options):
        for proxy in ProxyHost.objects.all():
            start = time.time()
            is_check_ok = test_proxy(proxy.ip, proxy.port)
            end =  time.time()
            exetime = (end-start)*1000

            print long(exetime)
            
            proxy.check_count += 1

            if is_check_ok:
                proxy.alive_count += 1
                proxy.speed += long(exetime)
            else:
                proxy.retry_count +=1
                
            proxy.save()
            
            
            self.stdout.write((u'%s:%s %s\r\n' % (proxy.ip,proxy.port,is_check_ok)))
            #except:
            #  raise CommandError('Poll "%s" does not exist')

