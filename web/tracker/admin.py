from django.contrib import admin

from . import models


class TagAdmin(admin.ModelAdmin):
    list_display = 'value',
    search_fields = 'value',


class EventAdmin(admin.ModelAdmin):
    list_display = 'title', 'date', 'progress', 'rating'
    list_filter = 'progress', 'rating'
    search_fields = 'title',


class EntryAdmin(admin.ModelAdmin):
    list_display = 'datetime', 'event', 'duration', 'annotation'
    search_fields = 'annotation', 'event__title'


admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Entry, EntryAdmin)
