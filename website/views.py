from django.shortcuts import render
import pyjokes
from datetime import datetime

def get_joke():
    return  pyjokes.get_joke()

def index(request):
    
    context = {
        'joke': get_joke(),
        'birthday': '',
    }

    if datetime.now().day == 19 and datetime.now().month == 8:
        context['birthday'] = 'Happy Birthday Rony!!'
    return render(request, 'website/index.html', context=context)