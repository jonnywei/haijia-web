from yueche.models import XueYuan
from yueche.models import YueChe
from django.contrib import admin

class XueYuanAdmin (admin.ModelAdmin):

    list_display = ('name','create_date')

admin.site.register(XueYuan, XueYuanAdmin)
admin.site.register(YueChe)



