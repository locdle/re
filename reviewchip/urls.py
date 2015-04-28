from django.conf.urls import include, url, patterns


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', 'reviewchip.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^inquiries/', include('inquiries.urls')),
]
