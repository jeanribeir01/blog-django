from django.contrib import admin
from .models import Post, Category

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'author', 'date')
    list_filter = ('status', 'date', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 20

admin.site.register(Category)
