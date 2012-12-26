# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

#系统配置信息
class SystemConfig(models.Model):
    key = models.CharField('key', max_length=256)
    value = models.CharField('value',max_length=1024)
    description = models.CharField('描述',max_length=1024,blank=True,null=True)
    create_date = models.DateTimeField('创建日期',auto_now_add=True)
    update_date = models.DateTimeField('更新日期',auto_now=True)
    def __unicode__(self):
        return  u"%s=%s" % (self.key, self.value)
    
#验证码信息
class CookieImgCode(models.Model):
    CODE_TYPE_CHOICES =(
        (u'ImgCode', u'登录验证码'),
        (u'BookingCode', u'约车验证码'),
        )
    VALID_TYPE_CHOICES =(
        (1,u'有效'),
        (0,u'无效'),
        )
    vcode = models.CharField('验证码',max_length=4)
    cookie = models.CharField('Cookie',max_length= 256)
    code_type = models.CharField('类型', max_length = 64,choices=CODE_TYPE_CHOICES)
    valid = models.IntegerField('有效标志',default=1, blank=True, null=True,choices=VALID_TYPE_CHOICES)
    create_date = models.DateTimeField('创建日期',auto_now_add=True)
    update_date = models.DateTimeField('更新日期',auto_now=True)

    def __unicode__(self):
        return  u"%s, %s ,%s " % (self.id, self.vcode, self.code_type)

#代理信息
class ProxyHost(models.Model):
    PRXOY_TYPE_CHOICES =(
        (u'HTTP', u'HTTP'),
        (u'SOCK4/5', u'SOCK4/5'),
        )
    ANONYMITY_CHOICES =(
        (u'NOA', u'(L3)non anonymous proxy'),
        (u'ANM', u'(L2)anonymous proxy server'),
        (u'HIA', u'(L1)high anonymous proxy'),
        )
    ip = models.CharField('IP',max_length=128)
    port = models.IntegerField('端口',default=80,blank=True)
    proxy_type = models.CharField('类型',default='HTTP',blank=True,null=True,max_length=32,choices=PRXOY_TYPE_CHOICES)
    anonymity  = models.CharField('匿名类型', max_length = 32, default='NOA', choices=ANONYMITY_CHOICES)
    source  = models.CharField('代理来源', max_length = 128,blank=True)
    name  = models.CharField('代理名称', max_length = 128,blank=True) 
    city  = models.CharField('所在城市', max_length = 128,blank=True) 
    check_date  = models.DateTimeField('检查日期',auto_now=True)
    speed = models.IntegerField('速度',default=0,blank=True)
    alive_count = models.IntegerField('存活次数',default=0,blank=True)
    check_count = models.IntegerField('检测次数',default=0,blank=True)
    retry_count = models.IntegerField('重试次数',default=0,blank=True)
    create_date = models.DateTimeField('创建日期',auto_now_add=True)
    update_date = models.DateTimeField('更新日期',auto_now=True)

    def __unicode__(self):
        return  u"%s  %s:%d" % (self.id, self.ip, self.port)

    
    
