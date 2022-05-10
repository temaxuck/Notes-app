from django.shortcuts import redirect
from . import *
from ..models import Note
from ..forms import NoteForm

def home(request):
    context = {}
    return render(request, 'non/home.html')

def notes(request):
    context = {
        'notes': request.user.note_set.order_by('timestampCreated').reverse(),
        'count': request.user.note_set.count()
    }
    return render(request, 'non/notes.html',  context)

def create_note(request):
    error = ''
    if request.method == 'POST':
        print(request.POST)
        context = {
            'QueryDict': request.POST,
            'title': 'Untitled',
            'content': '...',
            'user': request.user
        }
        form = NoteForm(context)
        #print(form)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма была неверной'
    print(error)
    return redirect('notes/')