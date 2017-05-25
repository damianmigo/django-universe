from django.conf.urls import url
from .views import NoteList, NoteDetailView


urlpatterns = [
    url(r'^$', NoteList.as_view(), name='index'),
    url(r'^note/[-\w]+/(?P<slug>[-\w]+)$', NoteDetailView.as_view(), name="detail"),
]
