# -*- coding: utf-8 -*-
from yueche.models import DingDan
from yueche.models import XueYuan
from yueche.models import YueChe

from django.contrib import admin
from django.utils.timezone import localtime
from django.core.urlresolvers import reverse

class DingDanAdmin (admin.ModelAdmin):

    list_display = ('id','taobao_name','name','list_taobao_ordernum','yc_count','amount','phone_num','list_create_date')
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
    
class XueYuanAdmin(admin.ModelAdmin):
    list_display = ('id','ding_dan','jia_xiao','name','id_num', 'passwd','phone_num','car_type')
    search_fields =['id_num','jia_xiao','ding_dan__taobao_ordernum','ding_dan__taobao_name','ding_dan__name']

class YueCheAdmin(admin.ModelAdmin):
    fieldsets = ( 
        (None, {
            'fields': ('xue_yuan','yc_km', 'yc_date', 'yc_time','reserve')
        }),
        ('可选信息', {
            'classes': ('collapse',),
            'fields': ('white_car','black_car')
        }),
        ('约车结果', {
            'classes': ['wide', 'extrapretty'],
            'fields': ('yc_result','yc_info')
        }),
    )

    
    
    
    #'xue_yuan__id_num','xue_yuan__passwd','xue_yuan__phone_num',
    list_display = ('id','list_ding_dan_info','list_xue_yuan_link','list_xue_yuan_jia_xiao','list_xue_yuan_id_num',
                    'list_xue_yuan_passwd','list_xue_yuan__phone_num','list_yc_date','yc_time','yc_km','yc_result','yc_info')
    
    search_fields = ['xue_yuan__id_num','xue_yuan__name','xue_yuan__ding_dan__taobao_ordernum','xue_yuan__ding_dan__taobao_name',
                     'xue_yuan__phone_num']
    date_hierarchy = 'yc_date'

    def list_yc_date(self, obj):
           return obj.yc_date.strftime('%Y-%m-%d')
           #return obj.yc_date
   
    list_yc_date.short_description='约车日期'
    list_yc_date.admin_order_field = 'yc_date'

    #xue_yuan.short_description ='订单信息'
    def list_ding_dan_info(self,obj):
        url = reverse('admin:yueche_dingdan_change', args=(obj.xue_yuan.ding_dan.id,))
        return u'<a  target="_blank"  title="订单详细信息" href="%s"><strong style="color: #FF5500;font-weight:bold;font-size:15px">%s</strong></a>&nbsp;&nbsp;<a target="_blank"  title="淘宝订单详细信息" href="http://trade.taobao.com/trade/detail/trade_item_detail.htm?bizOrderId=%s">淘宝</a>'%( url ,obj.xue_yuan.ding_dan.taobao_name,obj.xue_yuan.ding_dan.taobao_ordernum)
    list_ding_dan_info.allow_tags = True
    list_ding_dan_info.short_description='订单信息'
    list_ding_dan_info.admin_order_field = 'xue_yuan__dian_dan__id'

    def list_xue_yuan_link(self, obj):
        CAR_TYPE_CHOICES={
            u'stn':u'普桑',
            u'qr': u'奇瑞',
        }
        url = reverse('admin:yueche_xueyuan_change', args=(obj.xue_yuan.id,))
        nm = obj.xue_yuan.name
        if obj.xue_yuan.jia_xiao == 'longquan':
            nm =CAR_TYPE_CHOICES[obj.xue_yuan.car_type]
        return u'<a target="_blank"  title="学员详细信息" href="%s"><strong>%s,%s</strong></a>'%( url,obj.xue_yuan.id_num,
                                                                                               nm)
    list_xue_yuan_link.allow_tags = True
    list_xue_yuan_link.short_description='学员信息'
    list_xue_yuan_link.admin_order_field = 'xue_yuan__id'

    def list_xue_yuan_id_num(self, obj):
        return obj.xue_yuan.id_num
    list_xue_yuan_id_num.short_description='学员账号'
    list_xue_yuan_id_num.admin_order_field = 'xue_yuan__id_num'

    def list_xue_yuan_passwd(self, obj):
        return obj.xue_yuan.passwd
    list_xue_yuan_passwd.short_description='密码'

    def list_xue_yuan__phone_num(self,obj):
        return obj.xue_yuan.phone_num
    list_xue_yuan__phone_num.short_description='手机号码'

    def list_xue_yuan_jia_xiao(self,obj):
        JIA_XIAO_TYPE_CHOICES={
        u'haijia':  u'海淀',
        u'longquan':u'龙泉',
        
        }
        return JIA_XIAO_TYPE_CHOICES[obj.xue_yuan.jia_xiao]
    list_xue_yuan_jia_xiao.short_description='驾校'
    list_xue_yuan_jia_xiao.admin_order_field='xue_yuan__jia_xiao'
    
admin.site.register(DingDan, DingDanAdmin)
admin.site.register(XueYuan, XueYuanAdmin)
admin.site.register(YueChe, YueCheAdmin)



