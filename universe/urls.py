from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.notes.urls', namespace='notes')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
