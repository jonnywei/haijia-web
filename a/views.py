# -*- coding: utf-8 -*-
# Create your views here.

from yueche.models import YueChe
from yueche.models import XueYuan
from settings.models import SystemConfig
from settings.models import CookieImgCode
from settings.models import ProxyHost


from django.http import HttpResponse
from django.utils import simplejson
from django.core import serializers
from django.shortcuts import get_object_or_404, render_to_response

import math
import datetime


def index(request):
    return HttpResponse("api")

#约车信息
def yueche(request):

    jia_xiao =request.GET.get('jx',None)

    yc_date=request.GET.get('yc_date',None)

    if yc_date == None:

        yc_date = datetime.date.today()+ datetime.timedelta(days=7)

    xue_yuan_all =XueYuan.objects.all()
    xue_yuan_dict = dict([(obj.id, obj) for obj in xue_yuan_all])
    
    
    if jia_xiao == None:
        response_data = YueChe.objects.select_related().filter(yc_date__range=(yc_date, yc_date))
        for obj in response_data:
            print obj.xue_yuan.id
            obj.xue_yuan_info =xue_yuan_dict[obj.xue_yuan.id]
            print obj.xue_yuan_info
    else:
        response_data = YueChe.objects.prefetch_related().filter(yc_date__range=(yc_date, yc_date),xue_yuan__jia_xiao=jia_xiao)
       
    json_serializer = serializers.get_serializer("json")()
    
    data = json_serializer.serialize(response_data, ensure_ascii=False)

    return HttpResponse(data,"application/json;charset=utf-8")
#需要扫描约车信息
def yueche_scan(request,jiaxiao_name):

   
    yc_date=request.GET.get('yc_date',None)

    start_date = datetime.date.today()+ datetime.timedelta(days=1)
    if yc_date == None:
        sevendaylater = datetime.date.today()+ datetime.timedelta(days=7)
        yc_date = sevendaylater
        
    response_data = YueChe.objects.filter(yc_date__range=(start_date, yc_date),xue_yuan__jia_xiao=jiaxiao_name,yc_result=None)

    json_serializer = serializers.get_serializer("json")()
    
    data = json_serializer.serialize(response_data, ensure_ascii=False)

    return HttpResponse(data,"application/json;charset=utf-8")

def detail(request,yueche_id):

    #p = get_object_or_404(YueChe, pk=yueche_id)
    #data = simplejson.dumps(p,  default=lambda o: o.__dict__)
    
    #return HttpResponse(data,"application/json;charset=utf-8")


    response_data = YueChe.objects.filter(id__exact=yueche_id)

    json_serializer = serializers.get_serializer("json")()

    
    data = json_serializer.serialize(response_data, ensure_ascii=False)

    
    return HttpResponse(data,"application/json;charset=utf-8")

def xueyuan_detail(request,xueyuan_id):
    response_data = XueYuan.objects.select_related().filter(id__exact=xueyuan_id)

    json_serializer = serializers.get_serializer("json")()

    data = json_serializer.serialize(response_data, ensure_ascii=False)

    return HttpResponse(data,"application/json;charset=utf-8")

def update(request,yueche_id):

    p = get_object_or_404(YueChe, pk=yueche_id)

    try:
        yc_result = p.yc_result
    except:
        pass
    else:
        if yc_result == 0 :
            return HttpResponse("ok","text/html")
        else:
            p.yc_result = request.GET['yc_result']
            p.yc_info   = request.GET['yc_info']
            p.save()
            return HttpResponse("save","text/html")        
    #json_serializer = serializers.get_serializer("json")()

    #data = json_serializer.serialize(list(p), ensure_ascii=False)

    #return HttpResponse(p,"application/json")

    
    #return HttpResponse(simplejson.dumps(list(response_data)),"application/json")
def yueche_update(request):
    p = get_object_or_404(YueChe, id_num=request.GET['id_num'], yc_date=request.GET['yc_date'])
    try:
        yc_result = p.yc_result
    except:
        pass
    else:
        if yc_result == 0 :
            return HttpResponse("ok","text/html")
        else:
            p.yc_result = request.GET['yc_result']
            p.yc_info   = request.GET['yc_info']
            p.save()
            return HttpResponse("save","text/html") 
        

#系统配置信息读取
def config(request):
    configs = SystemConfig.objects.all()
    output = "\r\n".join(u'%s=%s' %(p.key, p.value) for p in configs)
    return HttpResponse(output,content_type="text/plain;charset=utf-8")



def cookie_all(request):
    
    cc = CookieImgCode.objects.all()
    
    json_serializer = serializers.get_serializer("json")()
    
    data = json_serializer.serialize(cc, ensure_ascii=False)

    return HttpResponse(data,"application/json;charset=utf-8")
    
def cookie_add(request):
    
    rvcode = request.GET['vcode']
    rcookie  = request.GET['cookie']
    rcode_type = request.GET['code_type']
    
    cc = CookieImgCode(vcode=rvcode, cookie=rcookie,code_type=rcode_type)

    cc.save()
    
    return HttpResponse('ok',content_type="text/plain;charset=utf-8")

def alive_rate(obj):
    arate =0
    if obj.check_count == 0:
        arate = 0
        return False
    else :
        arate = int(math.floor(obj.alive_count/float(obj.check_count) * 100))
        if arate > 80:
            return True
    return False

#得到所有的代理列表
def proxy_all(request):
    
    cc = ProxyHost.objects.all()
    
    json_serializer = serializers.get_serializer("json")()
    cc = filter(alive_rate,list(cc))[:256]
    data = json_serializer.serialize(cc, ensure_ascii=False)

    return HttpResponse(data,"application/json;charset=utf-8")

#添加一个proxy   
def proxy_add(request):
    
    rip = request.GET['ip']
    rport  = request.GET['port']
    
    #rcode_type = request.GET['type']
    
    eobj = ProxyHost.objects.filter(ip__exact=rip, port__exact=rport)
    if len(eobj) > 0:
        return HttpResponse('exist',content_type="text/plain;charset=utf-8")
    
    cc = ProxyHost(ip=rip, port=rport)

    cc.save()
    
    return HttpResponse('ok',content_type="text/plain;charset=utf-8")


