# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Cookie(models.Model):
    cookie_name = models.CharField('淘宝用户名', max_length=40)
    taobao_ordernum= models.CharField('淘宝订单号',max_length=64)
    phone_num =models.CharField('电话号码',max_length=20,null=True,blank=True)
    name = models.CharField('名字',max_length=20,null=True)
    create_date = models.DateTimeField('创建日期',auto_now_add=True)
    update_date = models.DateTimeField('更新日期',auto_now=True)
    reserve = models.CharField('备注',max_length=512,null=True,blank=True)

    def __unicode__(self):
        return  u"%s, %s " % (self.name, self.taobao_name)
