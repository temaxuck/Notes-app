from . import *

def home(request):
    context = {}
    return render(request, 'non/home.html')

@login_required
def notes(request):
    return render(request, 'non/notes.html')