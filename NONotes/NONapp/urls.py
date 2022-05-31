"""NONotes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .forms import NoteForm
from .models import Note
from .views import generalviews, notesviews

urlpatterns = [
    path('about', generalviews.home, name='about'),
    path('', notesviews.NoteListView.as_view(), name='notes'),
    path('create_note', notesviews.create_note, name='create_note'),
    path('search_notes', notesviews.NoteSearchView.as_view(), name='search_notes'),
    path('delete_note/<pk>', notesviews.NoteDeleteView.as_view(), name='delete_note'),
    # path('settings', generalviews.profile, name='settings'),
    # path('create/', notes.create, name='create'),
    # path('update_note/<pk>', notesviews.update_note, name='update_note'),
]
