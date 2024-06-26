from django.contrib import admin
from django.utils.html import format_html

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html(f'<img src={obj.image.url} width="100" style="border-radius: 10px;" />')
    
    list_display = ['thumbnail', 'title', 'publish', 'status']
    prepopulated_fields = {'slug': ('title',)}
