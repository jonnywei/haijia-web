# -*- coding: utf-8 -*-
from settings.models import SystemConfig
from settings.models import CookieImgCode

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
    list_display = ('vcode','cookie','code_type','list_create_date','list_update_date')
    search_fields = ['vcode','code_type']
    

    def list_create_date(self, obj):
           return localtime(obj.create_date).strftime('%Y-%m-%d %H:%M:%S')
    list_create_date.description='创建日期'
    list_create_date.short_description='创建日期'
    def list_update_date(self, obj):
           return localtime(obj.update_date).strftime('%Y-%m-%d %H:%M:%S')
    list_update_date.description='更新日期'
    list_update_date.short_description='更新日期'
   
admin.site.register(SystemConfig, SystemConfigAdmin)
admin.site.register(CookieImgCode, CookieImgCodeAdmin)



