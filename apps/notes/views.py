from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Note


class NoteList(ListView):
    queryset = Note.objects.all().order_by('-date_published')
    

class NoteDetailView(DetailView):
    model = Note
    
    def get_context_data(self, **kwargs):
        context = super(NoteDetailView, self).get_context_data(**kwargs)
        return context
