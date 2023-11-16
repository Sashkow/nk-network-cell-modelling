from .proxyfunctions import *
from . import boolfunction
import random


def generate_n_k_automata(N, K, functions_list, links_list):
    generate_functions_list(N, K, functions_list)
    generate_links_list(N, K, links_list)
    # generate_state(initial_state,N)


def generate_functions_list(N, K, functions_list):
    for i in range(N):
        # print "generating function", i
        bf = boolfunction.BoolFunction(K)
        bf.generate_random()

        functions_list.append(bf)


def generate_links_list(N, K, links_list):
    for n in range(N):
        current_function_links = []
        while len(current_function_links) < K:
            rand_value = random.randrange(0, N)

            if not (rand_value in current_function_links):
                current_function_links.append(rand_value)
        links_list.append(current_function_links)
