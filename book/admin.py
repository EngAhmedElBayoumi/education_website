from django.contrib import admin
from .models import Book
# import html_formate
from django.utils.html import format_html
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pages','display_image')
    search_fields = ('title', 'author')
    
    def display_image(self, obj):
        return format_html('<img src="{}" width="100" height="100" />'.format(obj.image.url))
    display_image.short_description = 'Image'
    
    
admin.site.register(Book, BookAdmin)