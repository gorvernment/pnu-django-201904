from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment

# Register your models here.
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     pass

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    pass

admin.site.register(Comment)