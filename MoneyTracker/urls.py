from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from MoneyTracker import settings
from TransactionTracker.api import TransactionResource, UserResource, TransactionTypeResource
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(TransactionResource())
v1_api.register(UserResource())
v1_api.register(TransactionTypeResource())

urlpatterns = patterns('',
    # Examples:
    url(r'^(?i)static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^api/', include(v1_api.urls), name='api'),
    url(r'^(?i)View/$', 'TransactionTracker.views.view', name='view'),
    url(r'^(?i)Add/$', 'TransactionTracker.views.add', name='add'),
    url(r'^(?i)debt/$', 'TransactionTracker.views.debt', name='debt'),
    url(r'^(?i)transactions/$', 'TransactionTracker.views.transactions', name='transactions'),
    url(r'^$', 'TransactionTracker.views.home', name='home'),
    # url(r'^MoneyTracker/', include('MoneyTracker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
