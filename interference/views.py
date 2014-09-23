from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.context_processors import csrf
from simu import SpIn
from Module_In import Light_source, Light_screen

def template(request):
	ctx = {}
	ctx['label'] = 'Interference'
	ctx['labelplus'] = 'Please enter parameters.'
	return render(request, "temp_intf.html", ctx)

def query(request):
	ctx = {}
	ctx.update(csrf(request))
	ctx['label'] = 'Result:'
	if request.POST.has_key('back'):
		return HttpResponseRedirect('http://127.0.0.1:8000/')
	if request.POST:
		screen = Light_screen (
			float(request.POST['screen.a']),
			float(request.POST['screen.b']),
			float(request.POST['screen.c']),
			)
		sourceFoo = Light_source (
			float(request.POST['position.x1']),
			float(request.POST['position.y1']),
			float(request.POST['w_length.1']),
			)
		sourceBar = Light_source (
			float(request.POST['position.x2']),
			float(request.POST['position.y2']),
			float(request.POST['w_length.2']),
			)
		SpIn(sourceFoo, sourceBar, screen)
	return render(request, "temp_intf.html", ctx)