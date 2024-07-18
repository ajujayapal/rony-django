from django.shortcuts import render
import pyjokes

def get_joke():
    return  pyjokes.get_joke()

def index(request):
    context = {'joke': get_joke()}
    return render(request, 'website/index.html', context=context)