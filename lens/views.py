import os
from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.context_processors import csrf
from Module_In import Light_source, Lens
from simu import ImagePos
import draw_lens

def template(request):
	ctx = {}
	#ctx['label'] = 'Lens (geometrical optics)'
	#ctx['labelplus'] = 'Please enter parameters.'
	return render(request, "lens.html", ctx)

def query(request):
	if os.path.isfile('/static/lens/pos.jpg'):
		os.remove('/static/lens/pos.jpg')
	ctx = {}
	ctx.update(csrf(request))
	#ctx['label'] = 'Result:'
	if request.POST.has_key('back'):
		return HttpResponseRedirect('http://127.0.0.1:8000/')
	source = Light_source()
	lensFoo = Lens()
	lensBar = Lens()
	if request.method == 'POST':
		source.x = float(request.POST['light.x'])
		source.y = float(request.POST['light.y'])
		lensFoo.pos = float(request.POST['position.foo'])
		lensFoo.focus = float(request.POST['focal.foo'])
		lensBar.pos = float(request.POST['position.bar'])
		lensBar.focus = float(request.POST['focal.bar'])
		ImagePos(source, lensFoo, lensBar)
	#ctx['src'] = source
	#ctx['lensFoo'] = lensFoo
	#ctx['lensBar'] = lensBar
	#request.session.flush()
	return render(request, "lens.html", ctx)