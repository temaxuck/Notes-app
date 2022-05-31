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
	redirect_field_name = '/user/login/?next=/notes/'

	def post(self, request):
		print(request.POST)
		note = Note.objects.filter(id=request.POST.get('update_note')).first()
		
		if note in request.user.note_set.all():
			note.update(request.POST.get('title'), request.POST.get('content'))
   
		return redirect('/notes')

        
    
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)

		context.update({
			'notes': self.request.user.note_set.all(),
			'form': NoteForm,
		})

		return context
    

def create_note(request):
    error = ''
    if request.method == 'POST':
        context = {
            'QueryDict': request.POST,
            'title': 'Без названия',
            'content': '',
            'user': request.user
        }
        form = NoteForm(context)
        #print(form)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма была неверной'
    return redirect('notes/')

class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    redirect_field_name = '/user/login/?next=/notes/'
    
    def get(self, args, **kwargs):
        return self.post(args, **kwargs)

    def get_success_url(self) -> str:
        return reverse('notes')


class NoteSearchView(LoginRequiredMixin, TemplateView):
    model = Note
    template_name = 'non/notes.html'
    redirect_field_name = '/user/login/?next=/notes/'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
		
        query = self.request.GET.get('q')
        
        context.update({
            'notes': self.request.user.note_set.filter(Q(title__icontains=query) | Q(content__icontains=query)),
			'form': NoteForm,
		})
        
        return context

# def update_note(request, note_id):
# 	form = NoteForm
# 	if request.method == 'POST':
# 		...
#  	# note = Note.objects.filter(id=note_id).first()
# 	# if form.
# 	return redirect('notes')