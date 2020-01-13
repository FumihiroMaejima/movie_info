from django.http import HttpResponse
from django.template import loader

def index(request):
    latest_question_list = 1
    template = loader.get_template('movie/index.html')
    context = {
        #'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('movie/about.html')
    context = {}
    return HttpResponse(template.render(context, request))
