from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the inquiries index")

def detail(request, starq_id):
    return HttpResponse("You're looking at question %s." % starq_id)

def results(request, starq_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % starq_id)

def vote(request, starq_id):
    return HttpResponse("You're voting on question %s." % starq_id)
