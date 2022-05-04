from . import *

def home(request):
    context = {
    }
    return render(request, 'non/home.html')