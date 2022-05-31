from . import *
from django.shortcuts import render, redirect
from ..models import Note
from ..forms import NoteForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView, FormView
from django.db.models import Q

class NoteListView(LoginRequiredMixin, TemplateView):
    model = Note
    template_name = 'non/notes.html'
    redirect_field_name = '/user/login/?next=/'   
    
    def post(self, request):
        note = Note.objects.filter(id=request.POST.get('update_note')).first()

        if note in request.user.note_set.all():
            note.update(request.POST.get('title'), request.POST.get('content'))

        return redirect(reverse('notes'))

        
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        new = self.request.session.get('new')
        self.request.session['new'] = None
        
        context.update({
            'notes': self.request.user.note_set.all(),
            'form': NoteForm,
            'open_note': new
        })

        return context
    

def create_note(request):
    error = ''
    if request.method == 'POST':
        initial = {
            'QueryDict': request.POST,
            'title': 'Без названия',
            'content': '',
            'user': request.user
        }
        
        form = NoteForm(initial)
        
        if form.is_valid():
            form.save()
        
        else:
            error = 'Форма была неверной'
        
        request.session['new'] = request.user.note_set.order_by('-id').first().id
    return redirect(reverse('notes'))

class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    redirect_field_name = '/user/login/?next=/'
    
    def get(self, args, **kwargs):
        return self.post(args, **kwargs)

    def get_success_url(self) -> str:
        return reverse('notes')


class NoteSearchView(LoginRequiredMixin, TemplateView):
    model = Note
    template_name = 'non/notes.html'
    redirect_field_name = '/user/login/?next=/'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
		
        query = self.request.GET.get('q')
        
        context.update({
            'notes': self.request.user.note_set.filter(Q(title__icontains=query) | Q(content__icontains=query)),
			'form': NoteForm,
		})
        
        return context