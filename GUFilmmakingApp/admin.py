from typing import Any
from django.contrib import admin
from GUFilmmakingApp.models import Post, UserProfile


def approve_users(self, request, queryset):
    queryset.update(verified=True)
approve_users.short_description = "Approve selected users for verification"


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'likes']


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'verified']
    list_editable = ['verified'] 
    actions = [approve_users]

admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile, UserProfileAdmin)