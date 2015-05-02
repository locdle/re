#from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponseRedirect, HttpResponse
#from django.core.urlresolvers import reverse

#from .models import Starq, Textq

## Create your views here.
#def index(request):
#    latest_starq_list = Starq.objects.order_by('-pub_date')[:5]
#    context = {'latest_starq_list': latest_starq_list}
#    return render(request, 'inquiries/index.html', context)

#def detail(request, starq_id):
#    starq = get_object_or_404(Starq, pk=starq_id)
#    return render(request, 'inquiries/detail.html', {'starq': starq})

#def rating(request, starq_id):
#    response = "You're looking at the rating of inquiry %s."
#    return HttpResponse(response % starq_id)

#def date(request, starq_id):
#    return HttpResponse("You're looking at the date for question %s." % starq_id)

#def rate(request, starq_id):
#    p = get_object_or_404(Starq, pk=starq_id)
#    try:
#        selected_starq = p._set.get(pk=request.POST['starq'])
#    except (KeyError, Starq.DoesNotExist):
#        # Redisplay the question voting form.
#        return render(request, 'inquiries/detail.html', {
#            'starq': q,
#            'error_message': "You didn't select a question.",
#        })
#    else:
#        selected_starq.votes += 1
#        selected_starq.save()
#        # Always return an HttpResponseRedirect after successfully dealing
#        # with POST data. This prevents data from being posted twice if a
#        # user hits the Back button.
#        return HttpResponseRedirect(reverse('inquiries:detail', args=(q.id,)))
