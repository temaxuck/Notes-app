from . import *
from django.shortcuts import render, redirect
from ..models import Note
from ..forms import NoteForm

def create(request):
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