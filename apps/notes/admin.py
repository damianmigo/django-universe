from django.contrib import admin
from .models import Note, Icon


class NoteAdmin(admin.ModelAdmin):
    readonly_fields=('slug', 'content_html')


admin.site.register(Note, NoteAdmin)
admin.site.register(Icon)