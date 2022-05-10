from . import *
from django.shortcuts import render, redirect
from ..models import Note
from ..forms import NoteForm

class NoteListView(TemplateView):
    model = Note
    template_name = 'non/notes.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['notes'] = self.request.user.note_set.all()
        return context
    

def create(request): # Нужно переписать этот view, под новую модель заметки
    error = ''
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = NoteForm

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'non/create.html', data)
