# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class DingDan(models.Model):
    WANG_DIAN_CHOICES =(
        (u'w',u'w'),
        (u'x',u'x')
        )
    taobao_name = models.CharField('淘宝用户名', max_length=40)
    taobao_ordernum= models.CharField('淘宝订单号',max_length=64)
    phone_num =models.CharField('电话号码',max_length=20,null=True,blank=True)
    name = models.CharField('名字',max_length=20,null=True)
    wang_dian = models.CharField('网店',max_length=20,null=True,blank=True,choices=WANG_DIAN_CHOICES,default='w')
    address = models.CharField('地址',max_length=512,null=True,blank=True)
    create_date = models.DateTimeField('创建日期',auto_now_add=True)
    update_date = models.DateTimeField('更新日期',auto_now=True)
    reserve = models.CharField('备注',max_length=1024,null=True,blank=True)

    def __unicode__(self):
        return  u"%s@_@%0.5s" % (self.taobao_name,self.taobao_ordernum)

class YueChe(models.Model):
    AM_PM_CHOICES=(
        (u'am',u'上午'),
        (u'pm',u'下午'),
        (u'am,pm',u'上午下午'),
        (u'pm,am',u'下午上午'),
        (u'am,ni',u'上午晚上'),
        (u'pm,ni',u'下午晚上'),
        (u'ni',u'晚上'),
        (u'am,pm,ni',u'全天'),
        )
    KM_CHOICES =(
        (u'km0',u'科目自动'),
        (u'km1',u'科目一'),
        (u'km2',u'科目二'),
        (u'km3',u'科目三'),
        (u'ks2',u'科目二考试'),
        (u'ks3',u'科目三考试')
        )
    CAR_TYPE_CHOICES =(
        (u'als',u'爱丽舍'),
        (u'byd',u'比亚迪'),
        (u'stn',u'桑塔纳'),
        (u'zdd',u'自动档'),
        (u'fk', u'富康'),
        (u'other',u'其他'),
        )
    xue_yuan = models.ForeignKey(DingDan)
    id_num = models.CharField('身份证号',max_length=18)
    passwd = models.CharField('密码',max_length=18)
    car_type = models.CharField('车辆类型',max_length=18,choices=CAR_TYPE_CHOICES,default='byd')
    yc_date = models.DateField('约车时间')
    yc_time = models.CharField('上午下午',max_length=64,choices=AM_PM_CHOICES)
    yc_km = models.CharField('科目考试',max_length =18,choices=KM_CHOICES,default='km2')

    phone_num =models.CharField('电话号码',max_length=20,null=True,blank=True)
    yc_result = models.IntegerField('约车是否成功',null=True,blank=True)
    yc_info = models.CharField('约车结果',max_length=256,null=True,blank=True)
    white_car = models.CharField('喜欢的车',max_length=256,null=True,blank=True)
    black_car = models.CharField('讨厌的车',max_length=256,null=True,blank=True)

    reserve = models.CharField('备注',max_length=1024,null=True,blank=True)

    
    create_date = models.DateTimeField('创建日期',auto_now_add=True)
    update_date = models.DateTimeField('更新日期',auto_now=True)

    def __unicode__(self):
        return  u"%s, %s ,%s " % (self.xue_yuan, self.id_num, self.yc_date)
    

    
    
