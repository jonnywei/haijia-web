# -*- coding: utf-8 -*-
from settings.models import SystemConfig
from settings.models import CookieImgCode
from settings.models import ProxyHost

from django.contrib import admin
from django.utils.timezone import localtime

class SystemConfigAdmin (admin.ModelAdmin):

    list_display = ('key','value','description','list_create_date','list_update_date')
    search_fields =['key','value']

    def list_create_date(self, obj):
           return localtime(obj.create_date).strftime('%Y-%m-%d %H:%M:%S')
    list_create_date.description='创建日期'
    list_create_date.short_description='创建日期'
    def list_update_date(self, obj):
           return localtime(obj.update_date).strftime('%Y-%m-%d %H:%M:%S')
    list_update_date.description='更新日期'
    list_update_date.short_description='更新日期'



class CookieImgCodeAdmin(admin.ModelAdmin):
    list_display = ('vcode','cookie','code_type','valid','list_create_date','list_update_date')
    search_fields = ['vcode','code_type']
    

    def list_create_date(self, obj):
           return localtime(obj.create_date).strftime('%Y-%m-%d %H:%M:%S')
    list_create_date.description='创建日期'
    list_create_date.short_description='创建日期'
    def list_update_date(self, obj):
           return localtime(obj.update_date).strftime('%Y-%m-%d %H:%M:%S')
    list_update_date.description='更新日期'
    list_update_date.short_description='更新日期'

class ProxyHostAdmin(admin.ModelAdmin):
    list_display=('id','ip','port','list_up_time','list_speed')
    search_fields =['ip']
    def list_up_time(self,obj):
        if obj.check_count == 0:
            return 'NoTest'
        else :
            return obj.alive_count/obj.check_count * 100
    list_up_time.short_description = '存活率(%)'
    list_up_time.admin_order_field = 'alive_count'

    def list_speed(self, obj):
        if obj.alive_count == 0 and obj.check_count > 0:
            return 0
        if obj.alive_count == 0 and obj.check_count == 0:
            return 'NoTest'
        return obj.speed/obj.alive_count
    list_speed.short_description ='速度(ms)'
    list_speed.admin_order_field ='speed'
    
admin.site.register(SystemConfig, SystemConfigAdmin)
admin.site.register(CookieImgCode, CookieImgCodeAdmin)
admin.site.register(ProxyHost,ProxyHostAdmin)



