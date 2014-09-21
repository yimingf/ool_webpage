from django.template import loader, Context
from django.http import HttpResponse
from django.shortcuts import render
from django.core.context_processors import csrf


def template(request):
	temp = loader.get_template("template.html")
	cont = Context ({'label': 'Welcome'})
    #context['label'] = 'Hello World!'
	return HttpResponse(temp.render(cont))

#@csrf_protect
#def query(request):
	#ctx = {}
	#ctx.update(csrf(request))
	#if request.POST.has_key('interference'):
		#return render(request, "interference/template/template.html")