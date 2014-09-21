from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^interference/', include('interference.urls')),
    url(r'^lens/', include('lens.urls')),
    url(r'^$', 'website.views.template'),
)
