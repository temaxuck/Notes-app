from .models import Note
from django.forms import ModelForm, TextInput, Textarea

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'user']

        widgets = {
            "user": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя'
            }),
            "content": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст заметки'
            }),
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название заметки'
            }),
        }
        