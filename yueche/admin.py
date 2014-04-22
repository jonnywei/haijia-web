# -*- coding: utf-8 -*-
from yueche.models import DingDan
from yueche.models import YueChe

from django.contrib import admin
from django.utils.timezone import localtime
from django.core.urlresolvers import reverse

class DingDanAdmin (admin.ModelAdmin):

    list_display = ('taobao_name','name','list_taobao_ordernum','phone_num','list_create_date')
    search_fields =['name','taobao_ordernum','phone_num']

    def list_create_date(self, obj):
        return localtime(obj.create_date).strftime('%Y-%m-%d %H:%M')
    list_create_date.description='创建日期'
    list_create_date.short_description='创建日期'
    list_create_date.admin_sort_field='create_date'

    def list_taobao_ordernum(self, obj):
        return u'<a title="淘宝订单详细信息" target="_blank" href="http://trade.taobao.com/trade/detail/trade_item_detail.htm?bizOrderId=%s">%s</a>'%(obj.taobao_ordernum,obj.taobao_ordernum)
    list_taobao_ordernum.allow_tags = True
    list_taobao_ordernum.description='淘宝订单号'
    list_taobao_ordernum.short_description='淘宝订单号'
    list_taobao_ordernum.admin_order_field='taobao_ordernum'
    



class YueCheAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('xue_yuan', 'id_num', 'passwd','yc_date', 'yc_time','yc_km','phone_num','reserve')
        }),
        ('可选信息', {
            'classes': ('collapse',),
            'fields': ('white_car','black_car','car_type')
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
           return obj.yc_date.strftime('%Y-%m-%d')
           #return obj.yc_date
   
    list_yc_date.short_description='约车日期'
    list_yc_date.admin_order_field = 'yc_date'

    #xue_yuan.short_description ='订单信息'

    def xue_yuan_link(self, obj):
        url = reverse('admin:yueche_dingdan_change', args=(obj.xue_yuan.id,))
        return u'<a  target="_blank"  title="用户详细信息" href="%s"><strong style="color: #FF5500;font-weight:bold;font-size:15px">%s</strong></a>&nbsp;&nbsp;<a target="_blank"  title="淘宝订单详细信息" href="http://trade.taobao.com/trade/detail/trade_item_detail.htm?bizOrderId=%s">淘宝</a>'%( url ,obj.xue_yuan.taobao_name,obj.xue_yuan.taobao_ordernum)
    xue_yuan_link.allow_tags = True
    xue_yuan_link.short_description='用户信息'
    xue_yuan_link.admin_order_field = 'xue_yuan'

    
admin.site.register(DingDan, DingDanAdmin)
admin.site.register(YueChe, YueCheAdmin)



