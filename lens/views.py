from django.template import loader, RequestContext
from django.http import HttpResponse
from django.shortcuts import render
from django.core.context_processors import csrf

def template(request):
	ctx = {}
	ctx['label'] = 'lens:'
	ctx['labelplus'] = 'Image'
	return render(request, "temp_lens.html", ctx)

def query(request):
	ctx = {}
	ctx.update(csrf(request))
	ctx['label'] = 'Result:'
	return render(request, "temp_lens.html", ctx)