from django.contrib import admin
from .models import Blog    
#import return html format
from django.utils.html import format_html
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'display_image')
    search_fields = ('title', 'topic', 'short_description')
    def display_image(self, obj):
        return format_html('<img src="{}" width="100" height="100" />'.format(obj.image.url))
    display_image.short_description = 'Image'
    
    
admin.site.register(Blog, BlogAdmin)
    

