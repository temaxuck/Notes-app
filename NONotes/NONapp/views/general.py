from . import *
from ..models import Note

def home(request):
    context = {}
    return render(request, 'non/home.html')

def notes(request):
    text = request.user.note_set.all()
    context = {
        'notes': request.user.note_set.all(),
    }
    return render(request, 'non/notes.html',  context)
