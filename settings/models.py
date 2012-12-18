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

