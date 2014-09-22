from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'lens.views.template'),
    url(r'^query/', 'lens.views.query'),
    url(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root': '/home/ccpizzadaisuki/website/lens/'}),
)
