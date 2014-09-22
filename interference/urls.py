from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'interference.views.template'),
    url(r'^query/', 'interference.views.query'),
    url(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root': '/home/ccpizzadaisuki/website/interference/'}),
)
