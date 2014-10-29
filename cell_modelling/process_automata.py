import os, sys
lib_path = os.path.abspath('')
sys.path.append(lib_path)
print sys.path

from automata import NK_Automata
from debug import log

from state import State 
import analyze
from boolfunction import*
from proxyfunctions import*
from drawgraph import DrawGraph
 
import saveload

import os
   #N=4 K=2 8257536 
def doAutomata(N,K,drawGraphObject,nkAutomata=None,ordinalNumber=-1):
    currentFolderPath = os.path.dirname(__file__)
    
    if nkAutomata == None:
        nkAutomata = NK_Automata(N, K)
        nkAutomata.generateRandomAutomata()
    
    nkAutomata.ordinalNumber = ordinalNumber
    
    drawGraphObject.drawGeneConnecionsGraph(nkAutomata.linksList, currentFolderPath)
    
    #print nkAutomata
    
    nkAutomata.spanAutomata()
    
    # print "satespan",nkAutomata.stateSpan
    
    
    nkAutomata.analyseAutomata()
    
    # print nkAutomata.stateList
    
    nkAutomata.makeAttractorStatDictionary()
    
    # print nkAutomata.attractorDict
    
    
    # print "stateList", nkAutomata.stateList
    
    nkAutomata.countStability()
    
    nkAutomata.countExpectedReturnTime()
    
    
    
    drawGraphObject.drawSimplfiedStatesGraph(nkAutomata.makeAttractorsDictionary(),2**nkAutomata.N,currentFolderPath)
    
    drawGraphObject.drawStatesGraph(nkAutomata.stateSpan, currentFolderPath)
    
    SaveLoad.saveNKAutomata(currentFolderPath, nkAutomata, True)
