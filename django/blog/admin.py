from django.contrib import admin
from blog.models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'views')

admin.site.register(Entry, EntryAdmin)
