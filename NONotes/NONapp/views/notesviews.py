from . import *
from django.shortcuts import render, redirect
from ..models import Note
from ..forms import NoteForm
from django.contrib.auth.mixins import LoginRequiredMixin

class NoteListView(LoginRequiredMixin, TemplateView):
    model = Note
    template_name = 'non/notes.html'
    redirect_field_name = '/user/login/?next=/notes/'
    
    #     form = NoteForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('notes')
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
		
        context.update({
            'notes': self.request.user.note_set.all(),
			'form': NoteForm,
		})
        
        return context
    
class NoteUpdateView(LoginRequiredMixin, TemplateView):
    model = Note
    template_name = 'non/notes.html'
    redirect_field_name = '/user/login/?next=/notes/'
    
    #     form = NoteForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('notes')
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
		
        context.update({
            'notes': self.request.user.note_set.all(),
			'form': NoteForm,
		})
        
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

# def notes(request):
#     if request.method == 'POST':
#         form = NoteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('notes')
#         else:
#             form = NoteForm()
            
#     context = {
#         'notes': request.user.note_set.order_by('timestampCreated').reverse(),
#         'count': request.user.note_set.count(),
#         'NoteForm': form,
#         'title': request.user.username
#     }
    

#     return render(request, 'non/notes.html',  context)