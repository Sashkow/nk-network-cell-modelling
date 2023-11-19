#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygraphviz import *
import os


class DrawGraph(object):
    def __init__(self, automata):
        self.automata = automata

    def draw_graph_by_name(self, graph_name):
        if graph_name == "gene_links_graph":
            return self.gene_links_graph()
        elif graph_name == "cell_states_graph":
            return self.cell_states_graph()
        elif graph_name == "simplified_cell_states_graph":
            return self.simplified_cell_states_graph()
        else:
            raise Exception("Wrong graph name")

    def gene_links_graph(self):
        A = AGraph()
        duplicant_names = ["Hassan", "Ari", "Marie", "Ada", "Otto", "Jean", "Mae", "Ruby", "Leira", "Bubbles"]

        for i in range(len(self.automata.links_list)):

            A.add_node(i, label=str(i) + str(duplicant_names[i]))  # str(int(str(functions_list[i]),2)))

        for bool_fun_number in range(len(self.automata.links_list)):
            for link in self.automata.links_list[bool_fun_number]:
                if (str(bool_fun_number), str(link)) in A.edges():
                    A.add_edge(link, bool_fun_number, dir="both")
                else:
                    A.add_edge(link, bool_fun_number, dir="forward")
        A.layout(prog="dot")

        # save_path=current_folder+'/'+"temp_gene_links_graph.svg"
        # print "Saving bool function links graph to file..."

        # save temporarily

        img = A.draw(format="svg")
        return img
        # print "The graph has been saved at", save_path

    def cell_states_graph(self):
        # d={[1]: {[2],[3]},[2]:{[4],[5]},[3]:{}}
        print("Drawing automata states graph:")
        A = AGraph()
        i = 0
        d = self.automata.state_span

        for item in d:
            i += 1
            percentage = int((float(i) / float(len(d))) * 100)
            # self.value_updated.emit(percentage) # progress bar

            if (str(d[item]), str(item)) in A.edges():
                A.add_edge(item, d[item], dir="both", arrowhead="normal")
            else:
                A.add_edge(item, d[item], dir="forward", arrowhead="normal")
            # labeled
            # if (str(d[item][0]),str(item)) in A.edges():
            #
            #     A.add_edge(item,d[item][0], dir='both',arrowhead='normal',label=d[item][1])
            # else:
            #     A.add_edge(item,d[item][0],dir='forward',arrowhead='normal',label=d[item][1])
        A.layout(prog="neato")
        # save_path=current_folder+'/'+"temp_states_graph.svg"
        # print "Saving graph to file..."
        # A.draw(os.path.join(save_folder_path,"temp_states_graph.svg"))
        # print "The graph has been saved at", save_folder_path

        return A.draw(format="svg")

    def simplified_cell_states_graph(self):
        # print "Drawing attractor automata states graph:"
        A = AGraph()
        i = 0
        min_node_size = 1
        max_node_size = 10
        min_font_size = 14.0
        d = self.automata.attractor_states_dict
        states_amount = 2 ** (self.automata.N)
        points_per_inch = 72
        for item in d:
            node_size = (
                min_node_size + max_node_size * float(d[item][1]) / states_amount
            )
            # print item, node_size, "=", min_node_size,"+",max_node_size,"*",d[item][1],"/", states_amount
            A.add_node(
                item,
                label=str(d[item][1]) + "|" + str(item),
                width=node_size,
                height=node_size / 2,
                fontsize=(node_size * points_per_inch) / 2,
            )

        for item in d:
            if (str(d[item][0]), str(item)) in A.edges():
                A.add_edge(item, d[item][0], dir="both", arrowhead="normal")
            else:
                A.add_edge(item, d[item][0], dir="forward", arrowhead="normal")

        A.layout(prog="circo")

        # save_path=current_folder+'/'+"temp_siplified_states_graph.svg"
        # print "Saving graph to file..."

        # A.draw(save_path)
        # print "The graph has been saved at", save_path

        return A.draw(format="svg")


# def draw_triangles():

#   A=AGraph()
#   A.node_attr['style']='filled'
#   A.add_node('1',label='1st_gender', fillcolor='black', fontcolor='white')
#   A.add_node('2',label='2nd_gender', fillcolor='red')
#   A.add_node('3',label='1st_gender', fillcolor='black', fontcolor='white')

#   A.add_edge('1','2', dir='forward',arrowhead='normal')
#   A.add_edge('2','3', dir='forward',arrowhead='normal')

#   A.add_node('4',label='1st_gender', fillcolor='black', fontcolor='white')
#   A.add_node('5',label='2nd_gender', fillcolor='red')
#   A.add_node('6',label='1st_gender', fillcolor='black', fontcolor='white')

#   A.add_edge('4','5', dir='forward',arrowhead='normal')
#   A.add_edge('5','6', dir='forward',arrowhead='normal')
#   A.add_edge('6','4', dir='forward',arrowhead='normal', style='bold')

#   A.layout(prog='circo')
#   A.draw('tr.svg')


# def draw_different_nodes():
#   A=AGraph()
#   A.node_attr['style']='filled'
#   A.add_node('1',label='1st_gender', fillcolor='black', fontcolor='white',height=0.5,width=0.5)
#   A.add_node('2',label='2nd_gender', fillcolor='red',height=1,width=1)
#   A.add_node('3',label='1st_gender', fillcolor='black', fontcolor='white',height=5,width=5)

#   A.add_edge('1','2', dir='forward',arrowhead='normal')
#   A.add_edge('2','3', dir='forward',arrowhead='normal')

#   A.layout(prog='circo')
#   A.draw('tr2.svg')
# """
# draw_different_nodes()
# # set some default node attributes

# A.node_attr['style']='filled'
# A.node_attr['shape']='circle'
# A.node_attr['fixedsize']='true'
# A.node_attr['fontcolor']='#FFFFFF'

# n=A.get_node('1')
# n.attr['fillcolor']='black'

# n=A.get_node('2')
# n.attr['fillcolor']='red'

# n=A.get_node('3')
# n.attr['fillcolor']='black'

# n=A.get_node('4')
# n.attr['fillcolor']='black'

# n=A.get_node('5')
# n.attr['fillcolor']='black'

# A.add_node('nill3',label='nill', fillcolor='black', shape='rectangle')
# A.add_node('nill4',label='nill', fillcolor='black',shape='rectangle')
# A.add_node('nill5',label='nill', fillcolor='black', shape='rectangle')

# A.add_edge('3','nill3')
# A.add_edge('4','nill4')
# A.add_edge('5','nill5')

# A.layout(prog='dot')
# A.draw('star.svg')

# A.delete_edge('5','nill5')
# A.delete_node('nill5')
# A.add_node('nill6',label='nill', fillcolor='black',shape='rectangle')

# A.add_node('6', fillcolor='red')
# A.add_edge('5','6')
# A.add_edge('6','nill6')
# """
