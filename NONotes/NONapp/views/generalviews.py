import django
from django.shortcuts import redirect
from . import *
from ..models import Note
from ..forms import NoteForm
from django.views.generic import DeleteView

def home(request):
    context = {}

    return render(request, 'non/home.html', context)