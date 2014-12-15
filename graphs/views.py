

from django.shortcuts import render
from django.core.urlresolvers import reverse

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.template import loader

from cell_modelling import automata	
from cell_modelling import processing
from cell_modelling import drawgraph

from graphs.models import Cell
from graphs.models import Like
from django.contrib.auth.models import User



import tempfile

import os
import pickle

global likesAmount
likesAmount=0

import random 


import xml.etree.ElementTree as ET


def index(request,N=5,K=5): #todo remove defult value duplication

	nkAutomata = getCurrentAutomata(request)
	graphNamesList = nkAutomata.graphNamesList

	template = loader.get_template('graphs/index.html')
	contextArguments = {
		'N':N,
		'K':K,
		'cells_top_list_link': reverse('cells-top-list')
		}

	for graphName in graphNamesList:
		contextArguments[graphName] = reverse('dynamic-image', args=[graphName])
		
	context = RequestContext(request, contextArguments)
	return HttpResponse(template.render(context))

def message(request):
	return HttpResponse('hello')


def build(request):	
	N = int(request.POST['nValue'])
	K = int(request.POST['kValue'])
	
	nkAutomata = automata.NK_Automata(N,K)
	nkAutomata.fillAutomata()
	request.session['current_automata']=nkAutomata

	return HttpResponseRedirect(reverse('index', args=[N,K]))

def buildAjax(request):
	global likesAmount
	likesAmount = 0

	N = int(request.GET["N"])
	K = int(request.GET["K"])

	createCurrentAutomata(request,N,K)

	return HttpResponse("")

def adjustSvg(image):
	#manually set image width and height
	treeRoot=ET.fromstring(image)
	treeRoot.attrib["width"]='100%'
	treeRoot.attrib["height"]='100%'

	#set font size in pixtels for Firefox browser 
	for e in treeRoot.getiterator():
		if 'font-size' in e.attrib:
			e.attrib["font-size"]=e.attrib["font-size"]+"px"

	#set transparent background 
	polygonElement = treeRoot.getiterator()[3]
	polygonElement.attrib["fill"]="transparent"
	polygonElement.attrib["stroke"]="transparent"

	image = ET.tostring(treeRoot, encoding='utf8', method='xml')
	return image



def dynamic_image(request, graph_name):

	nkAutomata = getCurrentAutomata(request)

	drawer = drawgraph.DrawGraph(nkAutomata)	
	image = drawer.drawGraphByName(graph_name)
	if image == None:
		return HttpResponse("noimage")

	image = adjustSvg(image)

	return HttpResponse(image, content_type="image/svg+xml")

def dynamic_image_by_cell_id(request, graph_name, cell_id):

	nkAutomata = pickle.loads(Cell.objects.get(id=cell_id).pickled_automata)

	drawer = drawgraph.DrawGraph(nkAutomata)	
	image = drawer.drawGraphByName(graph_name)
	if image == None:
		return HttpResponse("noimage")

	image = adjustSvg(image)

	return HttpResponse(image, content_type="image/svg+xml")

def like(request):
	global likesAmount

	cell_id = getCurrentCellId(request)
	c = Cell.objects.get(id=cell_id)
	userLazySimpleObject = request.user
	#todo if authorized
	if request.user.is_authenticated():
		u = User.objects.get(id=userLazySimpleObject.id)
	else:
		u = User.objects.get(username='guest')
	l = Like(cell=c,user=u)
	l.save()
	
	likesAmount+=1
	return HttpResponse("Times liked: "+str(likesAmount))


def createCurrentAutomata(request,N=None,K=None):
	nkAutomata = automata.NK_Automata(N,K)
	nkAutomata.fillAutomata()
	pickledAutomata = pickle.dumps(nkAutomata)

	c = Cell(n=nkAutomata.N,k=nkAutomata.K,pickled_automata=pickledAutomata)
	c.save()
	request.session['cell_id']=c.id


def getCurrentCellId(request):
	cell_id=request.session.get('cell_id',False)
	if cell_id:
		return cell_id
	else:
		createCurrentAutomata(request)
		return getCurrentCellId(request)

def getPickledCurrentAutomata(request):
	cell_id=getCurrentCellId(request)
	c = Cell.objects.get(id=cell_id)
	return c.pickled_automata

def getCurrentAutomata(request):
	return pickle.loads(getPickledCurrentAutomata(request))

#show previous graphs
def showMostLikedCells(request):
	from django.db import connection
	template = loader.get_template('graphs/cells_top_list.html')
	cellsInfoList = Like.objects.getMostLikedCellsInfo()

	context = RequestContext(request, {
		'cells_info_list': cellsInfoList,
		'graphs_subtitles': ["Genes' links network","Cell states graph","Simplified cell states graph"]
		})

	return HttpResponse(template.render(context))

	for item in cursor.fetchall():
		graphs_list=[]
		for graph_name in automata.NK_Automata.graphNamesList:
			graphs_list.append(str(reverse('dynamic-image-by-cell-id', args=[cell[0],graph_name])))
		graphs_list_list.append(graphs_list)




