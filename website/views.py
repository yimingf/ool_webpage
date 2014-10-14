from django.template import loader, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.context_processors import csrf

#def query(request):
#	if request.POST.has_key('lens'):
#		return HttpResponseRedirect('/lens/')



def template(request):
	ctx = {}
	ctx.update(csrf(request))
	#ctx['label'] = 'Online Optics Laboratory'
	return render(request, "index.html", ctx)