from django.http import HttpResponse

# Create your views here.

def index(request):
    #/dashboard/
    return HttpResponse("<h1>This is the Dashboard main homepage!</h1>")
    # "<h1>This is the Dashboard main homepage!!</h1>"
