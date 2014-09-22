from django.template import loader, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.context_processors import csrf


def template(request):
	ctx = {}
	ctx.update(csrf(request))
	ctx['label'] = 'Online Optics Laboratory'
	return render(request, "template.html", ctx)

def query(request):
	ctx = {}
	ctx.update(csrf(request))
	if request.POST.has_key('intf'):
		return HttpResponseRedirect('http://127.0.0.1:8000/interference')
	else:
		return HttpResponseRedirect('http://127.0.0.1:8000/lens')