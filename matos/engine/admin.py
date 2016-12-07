from django.contrib import admin

# Register your models here.

from .models import Operation

class OperationAdmin(admin.ModelAdmin):
    list_display = ['date','ip','operation',]
    list_filter = ('date','ip','operation',)
admin.site.register(Operation, OperationAdmin)
