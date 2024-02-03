
from django.contrib import messages
from django.shortcuts import render
from home.models import Contact
from datetime import datetime
import requests, random

def get_news(source, api_key='e1b57251b1b94ed894f3c60d25551eb2'):
    try:
        gets = f'https://newsapi.org/v1/articles?source={source}&sortBy=top&apiKey={api_key}'
        req = requests.get(gets)
        box = req.json()['articles']

    except:
        gets = f'https://newsapi.org/v1/articles?source={source}&sortBy=top&apiKey=5f69434d32434ea8bdb16b347f71cca2'
        req = requests.get(gets)
        box = req.json()['articles']
    
    print(box)
    return box
    
def services(request):
    source = ['bbc-news', 'cnn', 'the-verge', 'time', 'the-wall-street-journal']
    source = random.choice(source)

    context = get_news(source)
    return render(request, 'services.html', {'context' : context})

def index(request):
    return render(request, 'index.html')
    # return HttpResponse('Home Page')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        
        contact = Contact(
            name = name,
            email = email,
            phone = phone,
            desc = desc,
            date = datetime.today()
        )

        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
