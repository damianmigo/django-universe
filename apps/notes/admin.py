from .models import Note, Icon
from djangoseo.admin import register_seo_admin
from django.contrib import admin
from .seo import BasicMetadata


class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', 'content_html')


admin.site.register(Note, NoteAdmin)
admin.site.register(Icon)

register_seo_admin(admin.site, BasicMetadata)
