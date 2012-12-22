# -*- coding: utf-8 -*-
from yueche.models import DingDan
from yueche.models import YueChe

from django.contrib import admin
from django.utils.timezone import localtime
from django.core.urlresolvers import reverse

class DingDanAdmin (admin.ModelAdmin):

    list_display = ('taobao_name','name','taobao_ordernum','phone_num','list_create_date')
    search_fields =['name','taobao_ordernum','phone_num']

    def list_create_date(self, obj):
           return localtime(obj.create_date).strftime('%Y-%m-%d %H:%M')
    list_create_date.description='创建日期'
    list_create_date.short_description='创建日期'



class YueCheAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('xue_yuan', 'id_num', 'passwd','car_type','yc_date', 'yc_time','yc_km','phone_num')
        }),
        ('可选信息', {
            'classes': ('collapse',),
            'fields': ('white_car','black_car','reserve')
        }),
        ('约车结果', {
            'classes': ['wide', 'extrapretty'],
            'fields': ('yc_result','yc_info')
        }),
    )
    
    list_display = ('id','xue_yuan_link','id_num','phone_num','list_yc_date','yc_time','yc_km','yc_result','yc_info')
    
    search_fields = ['id_num','xue_yuan__taobao_ordernum','xue_yuan__taobao_name','xue_yuan__name','xue_yuan__phone_num']
    date_hierarchy = 'yc_date'

    def list_yc_date(self, obj):
           return localtime(obj.yc_date).strftime('%Y-%m-%d')
   
    list_yc_date.short_description='约车日期'
    list_yc_date.admin_order_field = 'yc_date'

    #xue_yuan.short_description ='订单信息'

    def xue_yuan_link(self, obj):
        url = reverse('admin:yueche_dingdan_change', args=(obj.xue_yuan.id,))
        return '<a href="%s">%s</a>' %( url ,obj.xue_yuan)
    xue_yuan_link.allow_tags = True
    xue_yuan_link.short_description='用户信息'
    xue_yuan_link.admin_order_field = 'xue_yuan'

    
admin.site.register(DingDan, DingDanAdmin)
admin.site.register(YueChe, YueCheAdmin)



