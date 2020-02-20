from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets, filters
from rest_framework.response import Response
from .functions import *

class MovieViewSet(viewsets.ViewSet):
    def list(self, request):
        # queryset = User.objects.all()
        # serializer = UserSerializer(queryset, many=True)
        # return Response(execSearchApi('Hello'))
        return Response(execSearchApi(request.GET.get(key='title', default='')))

def index(request):
    template = loader.get_template('movie/index.html')
    context = {
        'response': execSearchApi('Hello'),
    }
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('movie/about.html')
    context = {}
    return HttpResponse(template.render(context, request))
