from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Starq, Textq

# Create your views here.
def index(request):
    latest_starq_list = Starq.objects.order_by('-pub_date')[:5]
    context = {'latest_starq_list': latest_starq_list}
    return render(request, 'inquiries/index.html', context)

def detail(request, starq_id):
    starq = get_object_or_404(Starq, pk=starq_id)
    return render(request, 'inquiries/detail.html', {'starq': starq})

def rating(request, starq_id):
    response = "You're looking at the rating of inquiry %s."
    return HttpResponse(response % starq_id)

def date(request, starq_id):
    return HttpResponse("You're looking at the date for question %s." % starq_id)
