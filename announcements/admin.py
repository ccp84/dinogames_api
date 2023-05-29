from django.contrib import admin
from .models import Announcement, Category


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('lastupdated', 'title', 'author')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
