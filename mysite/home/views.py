
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Home Page')

def about(request):
    return HttpResponse('About Page')

def services(request):
    return HttpResponse('Services Page')

def contact(request):
    return HttpResponse('Contact Page')
