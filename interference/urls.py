from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'interference.views.template'),
    url(r'^query/', 'interference.views.query'),
)
