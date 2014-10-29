from django.shortcuts import render
from django.core.urlresolvers import reverse

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.template import loader

from cell_modelling import automata	
from cell_modelling import processing
from cell_modelling import drawgraph

import tempfile

import os


import random


def index(request):
	print "in graphs/views/index"
	template = loader.get_template('graphs/index.html')
	context = RequestContext(request, {})

	return HttpResponse(template.render(context))


def message(request):
	return HttpResponse('hello')


def build(request):

	N = int(request.POST['nValue'])
	K = int(request.POST['kValue'])
	

	nkAutomata = automata.NK_Automata(N, K)
	nkAutomata.generateRandomAutomata()
	print "automata", nkAutomata

	nkAutomata.spanAutomata()
	print "satespan",nkAutomata.stateSpan

	nkAutomata.analyseAutomata()
	print nkAutomata.stateList

	nkAutomata.makeAttractorStatesDictionary()
	print "attractor states:", nkAutomata.attractorStatesDict

	drawGraphObject = drawgraph.DrawGraph()
	tmpSatesGraph=tempfile.NamedTemporaryFile()
	
	savePath = os.path.dirname(os.path.abspath(__file__))
	savePath = os.path.join(savePath, "static/graphs/images")
	
	drawGraphObject.drawGeneConnecionsGraph(nkAutomata.functionsList,nkAutomata.linksList, savePath)

	drawGraphObject.drawStatesGraph(nkAutomata.stateSpan, savePath)

	drawGraphObject.drawSimplfiedStatesGraph(nkAutomata.attractorStatesDict,2**nkAutomata.N,savePath)

	return HttpResponseRedirect(reverse('index'))
