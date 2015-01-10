

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

global likes_amount
likes_amount = 0

import random 


import xml.etree.ElementTree as ET


def index(request,N=5,K=5): #todo remove defult value duplication

	nk_automata = get_current_automata(request)
	graph_names_list = nk_automata.graph_names_list

	template = loader.get_template('graphs/index.html')
	context_arguments = {
		'N':N,
		'K':K,
		'cells_top_list_link': reverse('cells-top-list')
		}

	for graph_name in graph_names_list:
		context_arguments[graph_name] = reverse('dynamic-image', args=[graph_name])
		
	context = RequestContext(request, context_arguments)
	return HttpResponse(template.render(context))

def message(request):
	return HttpResponse('hello')


def build(request):	
	N = int(request.POST['n_value'])
	K = int(request.POST['k_value'])
	
	nk_automata = automata.NK_Automata(N,K)
	nk_automata.fill_automata()
	request.session['current_automata']=nk_automata

	return HttpResponseRedirect(reverse('index', args=[N,K]))

def build_ajax(request):
	global likes_amount
	likes_amount = 0

	N = int(request.GET["N"])
	K = int(request.GET["K"])

	create_current_automata(request,N,K)

	return HttpResponse("")

def adjust_svg(image):
	#manually set image width and height
	tree_root=ET.fromstring(image)
	tree_root.attrib["width"]='100%'
	tree_root.attrib["height"]='100%'

	#set font size in pixtels for Firefox browser 
	for e in tree_root.getiterator():
		if 'font-size' in e.attrib:
			e.attrib["font-size"]=e.attrib["font-size"]+"px"

	#set transparent background 
	polygon_element = tree_root.getiterator()[3]
	polygon_element.attrib["fill"]="transparent"
	polygon_element.attrib["stroke"]="transparent"

	image = ET.tostring(tree_root, encoding='utf8', method='xml')
	return image



def dynamic_image(request, graph_name):

	nk_automata = get_current_automata(request)

	drawer = drawgraph.DrawGraph(nk_automata)	
	image = drawer.draw_graph_by_name(graph_name)
	if image == None:
		return HttpResponse("noimage")

	image = adjust_svg(image)

	return HttpResponse(image, content_type="image/svg+xml")

def dynamic_image_by_cell_id(request, graph_name, cell_id):

	nk_automata = pickle.loads(Cell.objects.get(id=cell_id).pickled_automata)

	drawer = drawgraph.DrawGraph(nk_automata)	
	image = drawer.draw_graph_by_name(graph_name)
	if image == None:
		return HttpResponse("noimage")

	image = adjust_svg(image)

	return HttpResponse(image, content_type="image/svg+xml")

def like(request):

	global likes_amount

	cell_id = get_current_cell_id(request)
	print cell_id
	c = Cell.objects.get(id=cell_id)
	user_lazy_simple_object = request.user
	#todo if authorized
	if request.user.is_authenticated():
		u = User.objects.get(id=user_lazy_simple_object.id)
	else:
		u = User.objects.get(username='guest')
	l = Like(cell=c,user=u)
	l.save()
	
	likes_amount+=1
	print "hhh"
	return HttpResponse("Times liked: "+str(likes_amount))


def create_current_automata(request,N=None,K=None):
	nk_automata = automata.NK_Automata(N,K)
	nk_automata.fill_automata()
	pickled_automata = pickle.dumps(nk_automata)

	c = Cell(n=nk_automata.N,k=nk_automata.K,pickled_automata=pickled_automata)
	c.save()
	request.session['cell_id']=c.id


def get_current_cell_id(request):
	cell_id=request.session.get('cell_id',False)
	if cell_id:
		return cell_id
	else:
		create_current_automata(request)
		return get_current_cell_id(request)

def get_pickled_current_automata(request):
	cell_id=get_current_cell_id(request)
	c = Cell.objects.get(id=cell_id)
	return c.pickled_automata

def get_current_automata(request):
	return pickle.loads(get_pickled_current_automata(request))

#show previous graphs
def show_most_liked_cells(request):
	from django.db import connection
	template = loader.get_template('graphs/cells_top_list.html')
	cells_info_list = Like.objects.get_most_liked_cells_info()

	context = RequestContext(request, {
		'cells_info_list': cells_info_list,
		'graphs_subtitles': ["Genes' links network","Cell states graph","Simplified cell states graph"]
		})

	return HttpResponse(template.render(context))

	for item in cursor.fetchall():
		graphs_list=[]
		for graph_name in automata.NK_Automata.graph_names_list:
			graphs_list.append(str(reverse('dynamic-image-by-cell-id', args=[cell[0],graph_name])))
		graphs_list_list.append(graphs_list)




