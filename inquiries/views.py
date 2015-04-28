from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Starq, Textq

# Create your views here.
def index(request):
    latest_starq_list = Starq.objects.order_by('-pub_date')[:5]
    template = loader.get_template('inquiries/index.html')
    context = RequestContext(request, {
        'latest_starq_list': latest_starq_list,
    })
    return HttpResponse(template.render(context))

def detail(request, starq_id):
    return HttpResponse("You're looking at question %s." % starq_id)

def results(request, starq_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % starq_id)

def vote(request, starq_id):
    return HttpResponse("You're voting on question %s." % starq_id)
