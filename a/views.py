# -*- coding: utf-8 -*-
# Create your views here.

from yueche.models import YueChe
from django.http import HttpResponse
from django.utils import simplejson
from django.core import serializers
from django.shortcuts import get_object_or_404, render_to_response

import datetime


def index(request):
    return HttpResponse("api")


def yueche(request):

    sevendaylater = datetime.date.today()+ datetime.timedelta(days=7)
   
    response_data = YueChe.objects.filter(yc_date__range=(sevendaylater, sevendaylater))

    json_serializer = serializers.get_serializer("json")()
    
    data = json_serializer.serialize(response_data, ensure_ascii=False)

    return HttpResponse(data,"application/json;charset=utf-8")

def detail(request,yueche_id):

    p = get_object_or_404(YueChe, pk=yueche_id)
    
    #json_serializer = serializers.get_serializer("json")()

    
    #data = json_serializer.serialize(list(p), ensure_ascii=False)

    data = simplejson.dumps(p,  default=lambda o: o.__dict__)
    
    return HttpResponse(data,"application/json;charset=utf-8")

    
    #return HttpResponse(simplejson.dumps(list(response_data)),"application/json")

def update(request,yueche_id):

    p = get_object_or_404(YueChe, pk=yueche_id)

    try:
        yc_result = p.yc_result
    except:
        pass
    else:
        if yc_result ==0 :
            return HttpResponse("ok","text/html")
        else:
            p.yc_result = request.GET['yc_result']
            p.yc_info   = request.GET['yc_info']
            p.update()
            return HttpResponse("save","text/html")        
    #json_serializer = serializers.get_serializer("json")()

    #data = json_serializer.serialize(list(p), ensure_ascii=False)

    #return HttpResponse(p,"application/json")

    
    #return HttpResponse(simplejson.dumps(list(response_data)),"application/json")

