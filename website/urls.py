from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^interference/', include('interference.urls')),
    url(r'^lens/', include('lens.urls')),
    url(r'^query/', 'website.views.query'),
    url(r'^$', 'website.views.template'),
	url(r'^css/(?P<path>.*)$','django.views.static.serve',{'document_root':'./static/css'}),
	url(r'^js/(?P<path>.*)$','django.views.static.serve',{'document_root':'./static/js'}),
	url(r'^images/(?P<path>.*)$','django.views.static.serve',{'document_root':'./static/images'}),

)
