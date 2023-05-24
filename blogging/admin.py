# blogging/admin.py

from django.contrib import admin
from blogging.models import Post, Category


class CategoryInLine(admin.TabularInline):
    model = Category.post.through


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInLine]


class CategoryAdmin(admin.ModelAdmin):
    exclude = ["post"]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

# Wow that was confusing!!!
