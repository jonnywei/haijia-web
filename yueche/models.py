# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class XueYuan(models.Model):
    name = models.CharField('名字',max_length=20)
    create_date = models.DateTimeField('创建日期')

    

    
    def __unicode__(self):
        return self.name

class YueChe(models.Model):
    xue_yuan = models.ForeignKey(XueYuan)
    yc_date = models.DateTimeField('date yueche time')
    count = models.IntegerField()
    def __unicode__(self):
        return self.xue_yuan , self.yc_date

