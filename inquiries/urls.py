from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /inquiries/
    url(r'^$', views.index, name = 'index'),
    # ex: /inquiries/5/ # added the word 'specifics'
    url(r'^specifics/(?P<starq_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /inquiries/5/results/
    url(r'^(?P<starq_id>[0-9]+)/results/$', views.rating, name='rating'),
    # ex: /inquiries/5/vote/
    url(r'^(?P<starq_id>[0-9]+)/vote/$', views.date, name='date'),
]
