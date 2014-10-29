import os, sys
lib_path = os.path.abspath('')
sys.path.append(lib_path)
print lib_path


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
def doAutomata(N,K,nkAutomata=None,ordinalNumber=-1):
    drawGraphObject = DrawGraph()

    currentFolderPath = os.path.dirname(__file__)
    
    if nkAutomata == None:
        nkAutomata = NK_Automata(N, K)
        nkAutomata.generateRandomAutomata()
    
    nkAutomata.ordinalNumber = ordinalNumber
    print nkAutomata
    
    nkAutomata.spanAutomata()
    print "satespan",nkAutomata.stateSpan
    
    nkAutomata.analyseAutomata()
    print nkAutomata.stateList
    
    nkAutomata.makeAttractorStatDictionary()
    print nkAutomata.attractorDict
    
    nkAutomata.countStability()
    print "Stability:", nkAutomata.stability
    
    nkAutomata.countExpectedReturnTime()
    print "ExpectedReturnTime:", nkAutomata.expectedReturnTime

    drawGraphObject.drawGeneConnecionsGraph(nkAutomata.linksList, currentFolderPath)
    
    drawGraphObject.drawStatesGraph(nkAutomata.stateSpan, currentFolderPath)

    drawGraphObject.drawSimplfiedStatesGraph(nkAutomata.attractorDict,2**nkAutomata.N,currentFolderPath)

    # print "saving..."
    # saveload.saveNKAutomata(currentFolderPath, nkAutomata, True)
    # print "saved."
