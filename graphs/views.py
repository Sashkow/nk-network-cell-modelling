from django.shortcuts import render
from django.core.urlresolvers import reverse

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.template import loader

from cell_modelling import automata	
from cell_modelling import processing
from cell_modelling import drawgraph

from graphs.models import Cell

import tempfile

import os
import pickle

global likesAmount
likesAmount=0

import random 


import xml.etree.ElementTree as ET


def index(request,N=5,K=5): #todo remove defult value dublication
	global likesAmount

	template = loader.get_template('graphs/index.html')
	context = RequestContext(request, {
		'N':N,
		'K':K,
		'gene_links_graph':reverse('dynamic-image', args=['gene_links_graph']),
		'cell_states_graph':reverse('dynamic-image', args=['cell_states_graph']),
		'simplified_cell_states_graph':reverse('dynamic-image', args=['simplified_cell_states_graph']),
		'likes':likesAmount,
		})

	return HttpResponse(template.render(context))


def message(request):
	return HttpResponse('hello')


def build(request):
	#global nkAutomata

	
	N = int(request.POST['nValue'])
	K = int(request.POST['kValue'])
	
	nkAutomata = automata.NK_Automata(N,K)
	nkAutomata.fillAutomata()

	request.session['current_automata']=nkAutomata

	return HttpResponseRedirect(reverse('index', args=[N,K]))

def buildAjax(request):
	print dict(request.session)
	#global nkAutomata

	N = int(request.GET["N"])
	K = int(request.GET["K"])

	nkAutomata = automata.NK_Automata(N,K)
	nkAutomata.fillAutomata()

	savedAutomata = pickle.dumps(nkAutomata)

	c = Cell(n=N,k=K,serialized_object=savedAutomata)

	c.save()

	request.session['current_automata']=savedAutomata





	#print Cell.objects.all()


	return HttpResponse("")


def dynamic_image(request, graph_name):
	#global nkAutomata
	nkAutomataString = request.session.get('current_automata',None)
	if nkAutomataString:
		nkAutomata = pickle.loads(nkAutomataString)
	else:
		nkAutomata = automata.NK_Automata()
		nkAutomata.fillAutomata()
		savedAutomata = pickle.dumps(nkAutomata)
		request.session['current_automata']=savedAutomata


	drawer = drawgraph.DrawGraph(nkAutomata)	
	image = drawer.drawGraphByName(graph_name)
	if image == None:
		return HttpResponse("noimage")

	treeRoot=ET.fromstring(image)
	treeRoot.attrib["width"]='100%'
	treeRoot.attrib["height"]='100%'
	image = ET.tostring(treeRoot, encoding='utf8', method='xml')

	return HttpResponse(image, content_type="image/svg+xml")

def like(request):
	print "CALL like"
	global likesAmount
	likesAmount+=1
	return HttpResponse(likesAmount)


