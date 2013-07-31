from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from MoneyTracker import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^(?i)static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^(?i)View/$', 'TransactionTracker.views.view', name='view'),
    url(r'^(?i)Add/$', 'TransactionTracker.views.add', name='add'),
    url(r'^$', 'TransactionTracker.views.home', name='home'),
    # url(r'^MoneyTracker/', include('MoneyTracker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
