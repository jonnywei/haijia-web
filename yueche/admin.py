# -*- coding: utf-8 -*-
from yueche.models import XueYuan
from yueche.models import YueChe

from django.contrib import admin
from django.utils.timezone import localtime

class XueYuanAdmin (admin.ModelAdmin):

    list_display = ('name','taobao_name','phone_num','list_create_date')
    search_fields =['name','taobao_ordernum','phone_num']

    def list_create_date(self, obj):
           return localtime(obj.create_date).strftime('%Y-%m-%d %H:%M')
    list_create_date.description='创建日期'
    list_create_date.short_description='创建日期'



class YueCheAdmin(admin.ModelAdmin):
    list_display = ('xue_yuan','id_num','list_yc_date','yc_time','yc_km','yc_result','yc_info')
    search_fields = ['id_num','yc_result']
    

    def list_yc_date(self, obj):
           return localtime(obj.yc_date).strftime('%Y-%m-%d')
   
    list_yc_date.short_description='约车日期'
    
admin.site.register(XueYuan, XueYuanAdmin)
admin.site.register(YueChe, YueCheAdmin)



