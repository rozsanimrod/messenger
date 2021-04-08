from django.contrib import admin
from accounts.models import UserProfile
from django.contrib.admin import ModelAdmin


class UserProfileAdmin(ModelAdmin):
    @staticmethod
    def delete_picture_link(modeladmin, request, queryset):
        queryset.update()

    list_display = ['id', 'user', 'age']
    list_display_links = ['id', 'user']
    ordering = ['id']
    list_filter = ['accepted_terms', 'age']
    search_fields = ['user', 'age']


admin.site.register(UserProfile, UserProfileAdmin)