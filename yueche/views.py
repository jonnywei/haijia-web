# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("欢迎你来到海驾约车系统")
