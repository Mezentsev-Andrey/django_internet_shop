from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'photo', 'created_at', 'is_published')
    list_filter = ('is_published', 'count_views')
