from django.contrib import admin
from .models import courses , Lectures
# import html_formate
from django.utils.html import format_html
# Register your models here.

class CoursesAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('instructor','title','grade','department', 'display_image')
    search_fields = ('title', 'grade', 'department', 'instructor')
    
    def display_image(self, obj):
        if not obj.image:
            return 'No Image'
        return format_html('<img src="{}" width="100" height="100" />'.format(obj.image.url))
    display_image.short_description = 'Image'
    
    
class LecturesAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('title',)
    search_fields = ('title', 'course')
      
    
admin.site.register(courses, CoursesAdmin)
admin.site.register(Lectures, LecturesAdmin)
    

