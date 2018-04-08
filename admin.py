from django.contrib import admin
from oa.models import S20ticket, S20hotel
from django.http import StreamingHttpResponse
import xlwt
import os

# Register your models here.



class S20ticketAdmin(admin.ModelAdmin):
    list_display =('name', 'mobile', 'kol', 'title', 'quantity','msts',)
    list_editable = ('msts','mobile')
    list_filter =('kol', 'title', 'money', 'msts','reason')
    search_fields =('no', 'name', 'kol', 'title', 'mobile', 'add', 'quantity', 'money', 'msts', 'reason',)
    date_hierarchy ='timestamp'

# other statements
    actions = ["SaveExecl",]
    def SaveExecl(self, request, queryset):
        Begin = xlwt.Workbook()
        # some sentences
#        Begin.save("%s"%(filename))
        Begin.save("%s"%(filename.xls))
        def file_iterator(filename, chunk_size=512):
            with open(filename,'rb') as f:
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break
        response = StreamingHttpResponse(file_iterator(filename))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment; filename="{}" '.format("aaaesult.xls")
        return response
    SaveExecl.short_description = "以表格形式下载"

class S20hotelAdmin(admin.ModelAdmin):
    list_display =('ename', 'mobile', 'kol', 'title', 'msts',)
    list_editable = ('msts', 'mobile')
    list_filter =('kol', 'title', 'money', 'msts', 'reason',)
    search_fields =('no', 'name', 'ename', 'passport', 'kol', 'title', 'mobile', 'money', 'msts', 'reason',)
    date_hierarchy ='timestamp'

admin.site.site_header = 'Wonderland'
admin.site.site_title = 'WonderlandOA'
admin.site.register(S20ticket,S20ticketAdmin)
admin.site.register(S20hotel,S20hotelAdmin)