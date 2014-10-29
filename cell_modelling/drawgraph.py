#MGpb3.0m
#380961226820
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygraphviz import *
import os


class DrawGraph(object):
    #valueUpdated = QtCore.pyqtSignal(int)
    
    def drawGeneConnecionsGraph(self,functionsList, linksList, currentFolder):
        print "Saving function links"
        A= AGraph()
        for i in range(len(linksList)):
            A.add_node(i,label="gene "+str(i)) #str(int(str(functionsList[i]),2)))

        for boolFunNumber in range(len(linksList)):
            for link in linksList[boolFunNumber]:
                #print link, "->", boolFunNumber
                if (str(boolFunNumber),str(link)) in A.edges():
                    A.add_edge(link,boolFunNumber,dir='both')
                else:
                    A.add_edge(link,boolFunNumber,dir='forward')
                    
        A.layout(prog='dot')
     
        savePath=currentFolder+'/'+"tempGeneLinksGraph.png"
        print "Saving bool function links graph to file..."
          
        #save temporaryly
        A.draw(savePath)
        print "The graph has been saved at", savePath
 

    def drawStatesGraph(self, d, saveFolderPath):
        #d={[1]: {[2],[3]},[2]:{[4],[5]},[3]:{}}
        print "Drawing automata states graph:"
        A=AGraph()
        i=0
        
        for item in d:
          
            i+=1
            percentage =int((float(i)/float(len(d)))*100)
            #self.valueUpdated.emit(percentage) # progress bar
            
            if (str(d[item]),str(item)) in A.edges(): 
                A.add_edge(item,d[item], dir='both',arrowhead='normal')
            else:
                A.add_edge(item,d[item],dir='forward',arrowhead='normal')  
#             if (str(d[item][0]),str(item)) in A.edges(): 
#                 #print "here"
#                 A.add_edge(item,d[item][0], dir='both',arrowhead='normal',label=d[item][1])
#             else:
#                 A.add_edge(item,d[item][0],dir='forward',arrowhead='normal',label=d[item][1])
        A.layout(prog='neato')
        #savePath=currentFolder+'/'+"tempStatesGraph.png"
        print "Saving graph to file..."
        A.draw(os.path.join(saveFolderPath,"tempStatesGraph.png"))
        print "The graph has been saved at", saveFolderPath
        
        
    def drawSimplfiedStatesGraph(self,d,statesAmount,currentFolder):
        print "Drawing attractor automata states graph:"
        A=AGraph()
        i=0
        minNodeSize=0.5
        maxNodeSize=10
        
        for item in d:            
            nodeSize=minNodeSize+maxNodeSize* float(d[item][1])/statesAmount
            #print item, nodeSize, "=", minNodeSize,"+",maxNodeSize,"*",d[item][1],"/", statesAmount
            A.add_node(item,label=item,width=nodeSize,height=nodeSize/2)

        
        for item in d:
            if (str(d[item][0]),str(item)) in A.edges():     
                A.add_edge(item,d[item][0], dir='both',arrowhead='normal')
            else:
                A.add_edge(item,d[item][0],dir='forward',arrowhead='normal')
            
        A.layout(prog='circo')
        
        savePath=currentFolder+'/'+"tempSiplifiedStatesGraph.png"
        print "Saving graph to file..."
        
        A.draw(savePath)
        print "The graph has been saved at", savePath

  
def drawTriangles():
  
  A=AGraph()
  A.node_attr['style']='filled'
  A.add_node('1',label='1stGender', fillcolor='black', fontcolor='white')
  A.add_node('2',label='2ndGender', fillcolor='red')
  A.add_node('3',label='1stGender', fillcolor='black', fontcolor='white')
  
  A.add_edge('1','2', dir='forward',arrowhead='normal')
  A.add_edge('2','3', dir='forward',arrowhead='normal')
  
  A.add_node('4',label='1stGender', fillcolor='black', fontcolor='white')
  A.add_node('5',label='2ndGender', fillcolor='red')
  A.add_node('6',label='1stGender', fillcolor='black', fontcolor='white')
  
  A.add_edge('4','5', dir='forward',arrowhead='normal')
  A.add_edge('5','6', dir='forward',arrowhead='normal')
  A.add_edge('6','4', dir='forward',arrowhead='normal', style='bold')
  
  A.layout(prog='circo')
  A.draw('tr.png')
 

def drawDifferentNodes():
  A=AGraph()
  A.node_attr['style']='filled'
  A.add_node('1',label='1stGender', fillcolor='black', fontcolor='white',height=0.5,width=0.5)
  A.add_node('2',label='2ndGender', fillcolor='red',height=1,width=1)
  A.add_node('3',label='1stGender', fillcolor='black', fontcolor='white',height=5,width=5)
  
  A.add_edge('1','2', dir='forward',arrowhead='normal')
  A.add_edge('2','3', dir='forward',arrowhead='normal')
  
  A.layout(prog='circo')
  A.draw('tr2.png')
"""
drawDifferentNodes()
# set some default node attributes

A.node_attr['style']='filled'
A.node_attr['shape']='circle'
A.node_attr['fixedsize']='true'
A.node_attr['fontcolor']='#FFFFFF'

n=A.get_node('1')
n.attr['fillcolor']='black'

n=A.get_node('2')
n.attr['fillcolor']='red'

n=A.get_node('3')
n.attr['fillcolor']='black'

n=A.get_node('4')
n.attr['fillcolor']='black'

n=A.get_node('5')
n.attr['fillcolor']='black'

A.add_node('nill3',label='nill', fillcolor='black', shape='rectangle')
A.add_node('nill4',label='nill', fillcolor='black',shape='rectangle')
A.add_node('nill5',label='nill', fillcolor='black', shape='rectangle')

A.add_edge('3','nill3')
A.add_edge('4','nill4')
A.add_edge('5','nill5')

A.layout(prog='dot')
A.draw('star.png')

A.delete_edge('5','nill5')
A.delete_node('nill5')
A.add_node('nill6',label='nill', fillcolor='black',shape='rectangle')

A.add_node('6', fillcolor='red')
A.add_edge('5','6')
A.add_edge('6','nill6')
"""







