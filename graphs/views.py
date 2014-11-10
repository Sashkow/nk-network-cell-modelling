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

import svgwrite
import xml.etree.ElementTree as ET






def index(request):
	template = loader.get_template('graphs/index.html')
	context = RequestContext(request, {
		})

	return HttpResponse(template.render(context))


def message(request):
	return HttpResponse('hello')


def build(request):
	global nkAutomata
	
	N = int(request.POST['nValue'])
	K = int(request.POST['kValue'])
	print "rebuild automata"
	nkAutomata = automata.NK_Automata(N,K)
	nkAutomata.fillAutomata()

	return HttpResponseRedirect(reverse('index'))



def dynamic_image(request, graph_name):
	global nkAutomata
	# template = loader.get_template('graphs/im.html')
	# context = RequestContext(request, {})

	# return HttpResponse(template.render(context))
	# return HttpResponse("--> "+os.getcwd())
	if nkAutomata:
		nkAutomata = automata.NK_Automata()
		nkAutomata.fillAutomata()

	drawer = drawgraph.DrawGraph(nkAutomata)
	print nkAutomata
	image = drawer.drawGraphByName(graph_name)




	# imgPath =os.path.join(os.getcwd(),"graphs/static/graphs/images/"+image_name+".svg")
	# imgXmlTree=ET.parse(imgPath)
	# treeRoot=imgXmlTree.getroot()
	# treeRoot.attrib["width"]='100%'
	# treeRoot.attrib["height"]='100%'
	# imgXmlTree.write(imgPath)


	# image_data = open(imgPath, "rb").read()
	return HttpResponse(image, content_type="image/svg+xml")


