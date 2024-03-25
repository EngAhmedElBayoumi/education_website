from django.contrib import admin
from .models import events as event
from django.utils.html import format_html

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'formatted_description','time','date', 'display_image')
    search_fields = ('title', 'description', 'time', 'date')
   
   
    def formatted_description(self, obj):
        return format_html('<p>{}</p>'.format(obj.description))  
   
    def display_image(self, obj):
        return format_html('<img src="{}" width="100" height="100" />'.format(obj.image.url))
    
    display_image.short_description = 'Image'   
    
    
admin.site.register(event, EventAdmin)