# -*- coding: utf-8 -*-
from yueche.models import DingDan
from yueche.models import XueYuan
from yueche.models import YueChe

from django.contrib import admin
from django.utils.timezone import localtime
from django.core.urlresolvers import reverse
from urllib import quote
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
    list_filter = ('jia_xiao', 'car_type')

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
    list_display = ('id','list_ding_dan_info','list_xue_yuan_jia_xiao','list_xue_yuan_id_num',
                    'list_xue_yuan_passwd','list_xue_yuan__phone_num','list_yc_date','yc_time','yc_km','yc_result','yc_info')
    #list_filter = ('xue_yuan__ding_dan__taobao_name', 'xue_yuan__jia_xiao')
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
	bayer_info=obj.xue_yuan.ding_dan.taobao_name +u',次数：'+str(obj.xue_yuan.ding_dan.yc_count) +u',金额：'+str(obj.xue_yuan.ding_dan.amount)
	utf_quote_taobao_name =quote(obj.xue_yuan.ding_dan.taobao_name.encode('utf-8'))
	quote_taobao_name =quote(obj.xue_yuan.ding_dan.taobao_name.encode('gbk'))
        return u'<a  target="_blank"  title="%s" href="%s"><strong style="color: #FF5500;font-weight:bold;font-size:15px">%s</strong></a><a title="只看此买家约车信息" href="?q=%s">&#376;</a>&nbsp;<a target="_blank"  href="http://trade.taobao.com/trade/itemlist/list_sold_items.htm?event_submit_do_query=1&buyerNick=%s&closeorder_flag=1&isArchive=false&isArchiveDefault=0&action=itemlist%%2FQueryAction&user_type=1&pageNum=0&order=desc&order_type=orderList&isQueryMore=false&select_shop_name=&isOwnOfficialShop=false&sellerNumID=87781119&from_flag=&auctionTitle=&bizOrderTimeBegin=&bizOrderHourBegin=00&bizOrderMinBegin=00&bizOrderTimeEnd=&bizOrderHourEnd=00&bizOrderMinEnd=00&auctionStatus=ALL&commentStatus=ALL&bizOrderId=&logisticsService=ALL&tradeDissension=ALL&auctionType=0&shopName=All">淘宝</a>' %(bayer_info, url ,obj.xue_yuan.ding_dan.taobao_name,  utf_quote_taobao_name ,quote_taobao_name) 
    #<a target="_blank"  title="淘宝订单详细信息" href="http://trade.taobao.com/trade/detail/trade_item_detail.htm?bizOrderId=%s">淘宝</a>
    list_ding_dan_info.allow_tags = True
    list_ding_dan_info.short_description='买家(客户)信息'
    list_ding_dan_info.admin_order_field = 'xue_yuan__ding_dan__id'

    def list_xue_yuan_link(self, obj):
       	pass
    list_xue_yuan_link.allow_tags = True
    list_xue_yuan_link.short_description='学员信息'
    list_xue_yuan_link.admin_order_field = 'xue_yuan__id'

    def list_xue_yuan_id_num(self, obj):
        CAR_TYPE_CHOICES={
            u'stn':u'普桑',
            u'qr': u'奇瑞',
            u'hj': u'海驾',
        }
        url = reverse('admin:yueche_xueyuan_change', args=(obj.xue_yuan.id,))
        nm = obj.xue_yuan.name + ',' +CAR_TYPE_CHOICES[obj.xue_yuan.car_type]
        
        return u'%s<a target="_blank"  title="%s,%s" href="%s"><strong>&raquo;</strong></a>'%(obj.xue_yuan.id_num, obj.xue_yuan.id_num,nm,url) 
    list_xue_yuan_id_num.allow_tags = True   
    list_xue_yuan_id_num.short_description='学员信息'
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



