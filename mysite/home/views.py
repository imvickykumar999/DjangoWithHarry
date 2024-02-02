
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'myname' : 'Guys',
        'location' : 'Home Page',
    }
    # return HttpResponse('Home Page')
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')
