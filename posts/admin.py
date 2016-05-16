from django.contrib import admin

from posts.models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["__str__","title","update","timestamp"]
    list_display_links = ["title","update"]
    list_filter = ["update","timestamp"]
    search_fields = ["title","content"]
    class Meta:
        model = Post

admin.site.register(Post,PostModelAdmin)