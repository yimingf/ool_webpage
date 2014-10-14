from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'lens.views.template'),
    url(r'^query/', 'lens.views.query'),
)
