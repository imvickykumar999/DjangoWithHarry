
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'myname' : 'Vicky',
        'location' : 'Home Page',
    }
    # return HttpResponse('Home Page')
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse('About Page')

def services(request):
    return HttpResponse('Services Page')

def contact(request):
    return HttpResponse('Contact Page')
