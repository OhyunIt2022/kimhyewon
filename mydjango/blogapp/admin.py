from django.contrib import admin

# Register your models here.

from .models import Post
@admin.register(Post)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at','updated_at')