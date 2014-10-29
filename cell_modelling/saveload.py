
import sys
import os
import pickle
import shutil
import os.path

def saveVariableToFile(variable,fileName,filePath):
    aFile=open(filePath+'/'+fileName,'w')
    pickle.dump(variable,aFile)
    aFile.close()

def loadVariableFromFile(fileName,filePath):
    aFile=open(filePath+'/'+fileName,'r')
    variable = pickle.load(aFile)
    aFile.close()
    return variable

import sys
import os
import pickle
import shutil
from proxyfunctions import*


def saveVariableToFile(variable,fileName,filePath):
    aFile=open(filePath+'/'+fileName,'w')
    pickle.dump(variable,aFile)
    aFile.close()

def loadVariableFromFile(fileName,filePath):
    aFile=open(filePath+'/'+fileName,'r')
    #print filePath+'/'+fileName
    variable = pickle.load(aFile)
    aFile.close()
    return variable

def generateAutomataTypeFolderName(N,K):
    maxNK=20
    return "N_"+addSucceedingZeroes(maxNK,N)+"_K_"+addSucceedingZeroes(maxNK,K)

def generateAutomataFolderName(automataTypeFoldersCollection):
    maxAutomataFoldersAmount=999
    currentAutomatFoldersAmount=len(automataTypeFoldersCollection)
    return addSucceedingZeroes(maxAutomataFoldersAmount,currentAutomatFoldersAmount)

def saveNKAutomata(currentFolderPath,nkAutomata,picture=False):

    dataFolderPath = os.path.join(currentFolderPath, '../../data')

    automataTypesFolderPath=os.path.join(dataFolderPath,'SavedAutomata')

    if not os.path.exists(automataTypesFolderPath):
        os.makedirs(automataTypesFolderPath)


    automataTypesFolderCollection = os.listdir(automataTypesFolderPath)

    automataTypeFolderName = generateAutomataTypeFolderName(nkAutomata.N,nkAutomata.K)

    automataTypeFolderPath = automataTypesFolderPath+'/'+automataTypeFolderName

    if not os.path.exists(automataTypeFolderPath):
        os.makedirs(automataTypeFolderPath)

    automataFoldersCollection = os.listdir(automataTypeFolderPath)

    #folders are numbered '000','001','002'...
    automataFolderName = generateAutomataFolderName(automataFoldersCollection)

    automataFolderPath = automataTypeFolderPath+'/'+automataFolderName

    os.makedirs(automataFolderPath)

    #print automataFolderPath

    saveVariableToFile(nkAutomata,'automata.txt',automataFolderPath)

    if picture:
        graphFileName = automataTypeFolderName+'_'+automataFolderName+'.png'
        graphCyclesOnlyFileName = automataTypeFolderName+'_'+automataFolderName+"_CyclesOnly"+'.png'
        graphFunLinksFileName = automataTypeFolderName+'_'+automataFolderName+"_FunLinks"+'.png'

        if os.path.exists(currentFolderPath+'/'+'tempPic.png'):
            shutil.copyfile(currentFolderPath+'/'+'tempPic.png', os.path.join(dataFolderPath, graphFileName))
        if os.path.exists(dataFolderPath+'/'+'tempPic2.png'):
            shutil.copyfile(dataFolderPath+'/'+'tempPic2.png', os.path.join(automataFolderPath,graphCyclesOnlyFileName))
        if os.path.exists(dataFolderPath+'/'+'tempPic3.png'):
            shutil.copyfile(dataFolderPath+'/'+'tempPic3.png', os.path.join(automataFolderPath, graphFunLinksFileName))


def gatherData(automataList,automataFoldersFolderPath):
    automataFoldersList=os.listdir(automataFoldersFolderPath) #'000','001','002'
    i=0
    for automataFolderName in automataFoldersList:
        print "gathering:", i
        i+=1
        nkAutomata=loadVariableFromFile('automata.txt',automataFoldersFolderPath+'/'+automataFolderName)
        automataList.append(nkAutomata)


def testFoldersCreation(dataFolderPath):
    automata=[]
    enters=[]
    initialState=[]
    N=5
    K=5
    I=3
    for n in range(N):
        for k in range(K):
            for i in range(I):
                saveNKAutomata(automata,enters,initialState,dataFolderPath,n,k)
