from django.contrib import admin
from .models import profile
# import user model
from django.contrib.auth.models import User
#import return html format
from django.utils.html import format_html
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('display_user', 'points', 'display_image')
    search_fields = ('user', 'points')
    
    def display_user(self, obj):
        return obj.user.username
    
    display_user.short_description = 'User'
    
    def display_image(self, obj):
        if not obj.image:
            return 'No Image'
        return format_html('<img src="{}" width="100" height="100" />'.format(obj.image.url))
    display_image.short_description = 'Image'
    
    
admin.site.register(profile, ProfileAdmin)