# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class XueYuan(models.Model):
    taobao_name = models.CharField('淘宝用户名', max_length=40)
    taobao_ordernum= models.CharField('淘宝订单号',max_length=64)
    phone_num =models.CharField('电话号码',max_length=20,null=True,blank=True)
    name = models.CharField('名字',max_length=20,null=True)
    address = models.CharField('地址',max_length=512,null=True,blank=True)
    create_date = models.DateTimeField('创建日期',auto_now_add=True)
    update_date = models.DateTimeField('更新日期',auto_now=True)
    reserve = models.CharField('备注',max_length=1024,null=True,blank=True)

    def __unicode__(self):
        return  u"%s, %s " % (self.name, self.taobao_name)

class YueChe(models.Model):
    AM_PM_CHOICES=(
        (u'am',u'上午'),
        (u'pm',u'下午'),
        (u'ni',u'晚上'),
        (u'am,pm',u'上午下午'),
        (u'pm,am',u'下午上午'),
        (u'am,pm,ni',u'全天'),
        )
    KM_CHOICES =(
        (u'km2',u'科目二'),
        (u'km3',u'科目三')
        )
    xue_yuan = models.ForeignKey(XueYuan)
    id_num = models.CharField('身份证号',max_length=18)
    passwd = models.CharField('密码',max_length=18)
    phone_num =models.CharField('电话号码',max_length=20,null=True,blank=True)
    yc_date = models.DateField('约车时间')
    yc_time = models.CharField('上午下午',max_length=64,choices=AM_PM_CHOICES)
    yc_km = models.CharField('科目几',max_length =18,choices=KM_CHOICES)
    yc_result = models.IntegerField('约车是否成功',null=True,blank=True)
    yc_info = models.CharField('约车结果',max_length=256,null=True,blank=True)
    reserve = models.CharField('备注',max_length=1024,null=True,blank=True)
    create_date = models.DateTimeField('创建日期',auto_now_add=True)
    update_date = models.DateTimeField('更新日期',auto_now=True)

    def __unicode__(self):
        return  u"%s, %s ,%s " % (self.xue_yuan, self.id_num, self.yc_date)
    

    
    
