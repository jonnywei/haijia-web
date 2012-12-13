# -*- coding: utf-8 -*-
# Create your views here.

from yueche.models import YueChe
from django.http import HttpResponse
from django.utils import simplejson
from django.core import serializers

import datetime


def index(request):
    return HttpResponse("api")


def yueche(request):


    sevendaylater = datetime.date.today()+ datetime.timedelta(days=7)
   
    response_data = YueChe.objects.filter(yc_date__range=(sevendaylater, sevendaylater))

    json_serializer = serializers.get_serializer("json")()
    data = json_serializer.serialize(response_data, ensure_ascii=False)

    return HttpResponse(data,"application/json")

    
    #return HttpResponse(simplejson.dumps(list(response_data)),"application/json")
