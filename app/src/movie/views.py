from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .functions import *

def index(request):
    template = loader.get_template('movie/index.html')
    context = {
        'test': testApi()
        # 'key': value,
    }
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('movie/about.html')
    context = {}
    return HttpResponse(template.render(context, request))
