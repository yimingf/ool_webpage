from django.template import loader, Context
from django.http import HttpResponse
from django.shortcuts import render

def template(request):
	temp = loader.get_template("temp_lens.html")
	cont = Context ({'label': 'lens page'})
    #context['label'] = 'Hello World!'
	return HttpResponse(temp.render(cont))

def query(request):
	temp = loader.get_template("temp_lens.html")
	cont = Context ({'label': 'Result:'})
	# Data manipulation codes goes here.
	return HttpResponse(temp.render(cont))