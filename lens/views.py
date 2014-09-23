from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.context_processors import csrf
from Module_In import Light_source, Lens
from simu import ImagePos
import draw_lens

def template(request):
	ctx = {}
	ctx['label'] = 'Lens (geometrical optics)'
	ctx['labelplus'] = 'Please enter parameters.'
	return render(request, "temp_lens.html", ctx)

def query(request):
	ctx = {}
	ctx.update(csrf(request))
	ctx['label'] = 'Result:'
	if request.POST.has_key('back'):
		return HttpResponseRedirect('http://127.0.0.1:8000/')
	if request.POST:
		source = Light_source(
			float(request.POST['light.x']),
			float(request.POST['light.y']),
			)
		lensFoo = Lens(
			float(request.POST['position.foo']),
			float(request.POST['focal.foo']),
			)
		lensBar = Lens(
			float(request.POST['position.bar']),
			float(request.POST['focal.bar']),
			)
		ImagePos(source, lensFoo, lensBar)
	return render(request, "temp_lens.html", ctx)