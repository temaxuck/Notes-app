from . import *

def home(request):
    return render(request, 'non/home.html')