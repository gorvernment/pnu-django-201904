from django.contrib import admin
from .models import Post
from .forms import PostForm

#admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ['title', 'ip', 'created_at', 'updated_at']

    def save_model(self, request, obj, form, change):
        obj.ip = request.META['REMOTE_ADDR']
        super().save_model(request, obj, form, change)
