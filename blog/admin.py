from django.contrib import admin

from .models import Author, Post, Tag

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["last_name", "first_name", "email"]

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'excerpt']
    prepopulated_fields = {'slug':('title',)}

class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)