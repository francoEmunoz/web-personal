from django.contrib import admin
from .models import Description

class DescriptionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('texto', 'image','link' ,'created', 'modified')

admin.site.register(Description, DescriptionAdmin)