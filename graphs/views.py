from django.test.client import RequestFactory

from django.shortcuts import render
from django.urls import reverse

from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import RequestContext
from django.template import loader

from cell_modelling import automata
from cell_modelling import processing
from cell_modelling import drawgraph

from graphs.models import Cell
from graphs.models import Like
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

import tempfile

import os
import pickle

global likes_amount
likes_amount = 0

import random

from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.utils.cache import get_cache_key

import xml.etree.ElementTree as ET

from django.contrib.auth import authenticate
from django.contrib import auth

def generate_combinations(input_number):
    combinations = []

    # Generate all possible combinations of 1s and 0s with the given input number
    for i in range(2 ** input_number):
        binary_str = bin(i)[2:].zfill(input_number)
        combination = [int(digit) for digit in binary_str]
        combinations.append(combination)

    return combinations


def index(request, N=4, K=2):  # todo remove defult value duplication
    """
    A main view for graphs app. Renders a template with two sliders for N and K
    values respectively and three graph images.

    **Context**

    ``N``
        int value representing amount of genes in cell

    ``K``
        int value representing amount of links per each gene in cell

    **Template:**

        :template:`graphs/index.html`

    """
    user = request.user
    password = os.environ.get("SUPERUSER_PASS", "admin")
    if not request.user.is_authenticated:
        user = authenticate(request, username="admin", password=password)
        if user is not None:
            # If successful, log in the user
            login(request, user)
        # auth.login(request, user)

    nk_automata = get_current_automata(request)

    if nk_automata is None or not hasattr(nk_automata, 'graph_names_list'):
        # Handle the case when nk_automata is None or doesn't have the expected attribute
        # This could involve creating a new automata or returning an error response
        # For now, let's create a new automata if it's None
        nk_automata = automata.NK_Automata(N, K)
        nk_automata.fill_automata()
        request.session["current_automata"] = nk_automata

    graph_names_list = getattr(nk_automata, 'graph_names_list', [])

    combinations = generate_combinations(input_number=nk_automata.functions_list[0].K)
    result_dicts = []

    for func in nk_automata.functions_list:
        values_string = func.values_string
        combinations_tuples = [tuple(combination) for combination in combinations]
        result_dict = dict(zip(combinations_tuples, values_string))
        result_dicts.append(result_dict)

    zipped_list = zip(nk_automata.links_list, result_dicts)

    template_name = "graphs/index.html"
    context = {
        "N": nk_automata.N,
        "K": nk_automata.K,
        "graph_names_list": graph_names_list,
        "functions": nk_automata.functions_list,
        "links_list": nk_automata.links_list,
        "zipped_list": zipped_list,
    }

    return render(request, template_name, context)


def message(request):
    return HttpResponse("hello")


def build(request):
    N = int(request.POST["n_value"])
    K = int(request.POST["k_value"])

    nk_automata = automata.NK_Automata(N, K)
    nk_automata.fill_automata()
    request.session["current_automata"] = nk_automata

    return HttpResponseRedirect(reverse("index", args=[N, K]))


def build_ajax(request):
    global likes_amount

    likes_amount = 0
    # factory = RequestFactory()
    # url = reverse('dynamic-image', args=('simplified_cell_states_graph',))
    # fake_request = factory.get(url)

    # cache_key = get_cache_key(fake_request)
    # if cache_key:
    #     cache.delete(cache_key)
    # expire_page_cache('dynamic-image', args=('simplified_cell_states_graph',))

    N = int(request.GET["N"])
    K = int(request.GET["K"])

    create_current_automata(request, N, K)

    return HttpResponse("")


def adjust_svg(image):
    # manually set image width and height
    tree_root = ET.fromstring(image)
    tree_root.attrib["width"] = "100%"
    tree_root.attrib["height"] = "100%"

    # set font size in pixtels for Firefox browser
    for e in tree_root.getiterator():
        if "font-size" in e.attrib:
            e.attrib["font-size"] = e.attrib["font-size"] + "px"

    # set transparent background
    polygon_element = tree_root.getiterator()[3]
    polygon_element.attrib["fill"] = "transparent"
    polygon_element.attrib["stroke"] = "transparent"

    image = ET.tostring(tree_root, encoding="utf8", method="xml")
    return image


from django.core.cache import cache
from django.urls import reverse
from django.http import HttpRequest
from django.utils.cache import get_cache_key


def expire_page_cache(view, args=None):
    """
    Removes cache created by cache_page functionality.
    Parameters are used as they are in reverse()
    """

    if args is None:
        path = reverse(view)
    else:
        path = reverse(view, args=args)

    request = HttpRequest()
    request.path = path

    key = get_cache_key(request)

    if key in cache:
        cache.delete(key)


# @cache_page(60 * 15)
def dynamic_image(request, graph_name):
    nk_automata = get_current_automata(request)

    drawer = drawgraph.DrawGraph(nk_automata)
    image = drawer.draw_graph_by_name(graph_name)
    if image == None:
        return HttpResponse("noimage")

    #image = adjust_svg(image)

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
    c = Cell.objects.get(id=cell_id)
    user_lazy_simple_object = request.user
    # todo if unauthorized
    if request.user.is_authenticated():
        u = User.objects.get(id=user_lazy_simple_object.id)
    else:
        u = User.objects.get(username="guest")
    l = Like(cell=c, user=u)
    l.save()

    likes_amount += 1
    return HttpResponse("Times liked: " + str(likes_amount))


def create_current_automata(request, N=None, K=None):
    nk_automata = automata.NK_Automata(N, K)
    nk_automata.fill_automata()
    pickled_automata = pickle.dumps(nk_automata)

    c = Cell(n=nk_automata.N, k=nk_automata.K, pickled_automata=pickled_automata)
    c.save()
    request.session["cell_id"] = c.id


def get_current_cell_id(request):
    cell_id = request.session.get("cell_id", False)
    if cell_id:
        return cell_id
    else:
        create_current_automata(request)
        return get_current_cell_id(request)


def get_pickled_current_automata(request):
    cell_id = get_current_cell_id(request)
    c = Cell.objects.get(id=cell_id)
    return c.pickled_automata


def get_current_automata(request):
    pickled_data = get_pickled_current_automata(request)
    
    try:
        return pickle.loads(eval(pickled_data))
    except Exception as e:
        print("Error during unpickling:", e)
        # Handle the error or print additional information for debugging


# show previous graphs
def show_most_liked_cells(request):
    from django.db import connection

    template = loader.get_template("graphs/cells_top_list.html")
    cells_info_list = Like.objects.get_most_liked_cells_info()

    context = RequestContext(
        request,
        {
            "cells_info_list": cells_info_list,
            "graphs_subtitles": [
                "Genes' links network",
                "Cell states graph",
                "Simplified cell states graph",
            ],
        },
    )

    return HttpResponse(template.render(context))

    for item in cursor.fetchall():
        graphs_list = []
        for graph_name in automata.NK_Automata.graph_names_list:
            graphs_list.append(
                str(reverse("dynamic-image-by-cell-id", args=[cell[0], graph_name]))
            )
        graphs_list_list.append(graphs_list)
