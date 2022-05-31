from .models import Note
from django.forms import ModelForm, TextInput, Textarea

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'user']

        widgets = {
            "content": Textarea(attrs={
                'placeholder': 'Текст заметки'
            }),
            "title": TextInput(attrs={
                'placeholder': 'Название заметки'
            }),
        }
        