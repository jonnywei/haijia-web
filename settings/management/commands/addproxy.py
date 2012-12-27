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

proxy_ip = '127.0.0.1'
proxy_port = 8087


def get_content_from_url(url):

    cj = cookielib.LWPCookieJar()

    cookie_support = urllib2.HTTPCookieProcessor(cj)

    #print (u'http://%s:%d' % (ip, port))             
    proxy_handler = urllib2.ProxyHandler({'http':(u'http://%s:%d' % (proxy_ip, proxy_port))})

    my_opener = urllib2.build_opener(cookie_support, proxy_handler)
    try:
        
        response = my_opener.open(url,timeout=20)

        content = response.read()

        return content
       
        
    except Exception,er:
        print er
    
    return None

def parse_proxynova_proxy(web_content):
    if web_content == None:
        return None
    else:
        lines = web_content.split('\n')
        print lines[14:-1]
        lines = lines[14:-1]
        neb=[x.split(':') for x in lines] 
        return neb


def add_proxy_to_db(ipport_list):
    if ipport_list == None:
        print "get proxy error"
        return None
    for ipport in  ipport_list:
            ip = ipport[0]
            port =ipport[1]
            
            eobj = ProxyHost.objects.filter(ip__exact=ip, port__exact=port)
            if len(eobj) > 0:
                print ip, port ,"exist pass"
                pass
            else:
                print ip, port ,"add"
                cc = ProxyHost(ip=ip, port=port)
                cc.save()
    

class Command(BaseCommand):
    help = 'add proxy is or not alive'
    def handle(self, *args, **options):
        proxynova_url='http://www.proxynova.com/proxy_list.txt?country=cn'
        add_proxy_to_db (parse_proxynova_proxy(get_content_from_url(proxynova_url)))
        #self.stdout.write((u'%s:%s %s\r\n' % (proxy.ip,proxy.port,is_check_ok)))
            #except:
            #  raise CommandError('Poll "%s" does not exist')

