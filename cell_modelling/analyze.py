import saveload
from proxyfunctions import *
import os



def countAverarageStabilityAndCycleAmount(automataList):
    stabilitySum=0
    stabilitySquareSum=0
    cycleAmountSum=0
    cycleAmountSquareSum=0
    automataListLength=len(automataList)

    for automata in automataList:
        stabilitySum+=automata.stability
        cycleAmountSum+=automata.basinAmount

    averageStability=float(stabilitySum)/automataListLength
    averageCycleAmount=float(cycleAmountSum)/automataListLength

    for automata in automataList:
        stabilitySquareSum+=(averageStability-automata.stability)**2
        cycleAmountSquareSum+=(averageCycleAmount-automata.basinAmount)**2
        #print automata.stability, automata.basinAmount

    stabilityStandardError=math.sqrt(float(stabilitySquareSum)/automataListLength)
    cycleAmountStandardError=math.sqrt(float(cycleAmountSquareSum)/automataListLength)



    print "Average stability:", str(averageStability)+"+-"+str(stabilityStandardError*3)
    print "Average cycleAmount:", str(averageCycleAmount)+"+-"+str(cycleAmountStandardError*3)


def stabilityToFile(automataList,currentFolderPath):
    f=open(currentFolderPath+"/" +"statFile.txt",'w')
    for automata in automataList:
        f.write(str(automata.stability)+"\n")
    f.close()

def stabilityToFiles(N,K,automataList,savePath,sampleDesiredLength):
    i=0
    f=open(savePath +"/"+generateStatFileName(N,K,i)+".txt",'w')
    for automataIndex in range(len(automataList)):
        if (automataIndex % sampleDesiredLength)==0:
            i+=1
            f.close()
            f=open(savePath +"/"+generateStatFileName(N,K,i)+".txt",'w')
        f.write(str(automataList[automataIndex].stability)+"\n")
    f.close()

def returnTimeToFiles(N,K,automataList,savePath,sampleDesiredLength):
    i=0
    f=open(savePath +"/"+generateStatFileName(N,K,i)+".txt",'w')
    for automataIndex in range(len(automataList)):
        if (automataIndex % sampleDesiredLength)==0:
            i+=1
            f.close()
            f=open(savePath +"/"+generateStatFileName(N,K,i)+".txt",'w')
        f.write(str(automataList[automataIndex].expectedReturnTime)+"\n")
    f.close()

def generateStatFileName(N,K,I):
    maxNK=20
    maxI=200
    return "N_"+addSucceedingZeroes(maxNK,N)+"_K_"+addSucceedingZeroes(maxNK,K)+"_I_"+addSucceedingZeroes(maxI,I)


def createAutomataStabilitySamples(N,K,currentFolderPath,sampleLength,samplesAmount):
    automataList=[]
    print "gatherData:"
    automataTypeFolderName=SaveLoad.generateAutomataTypeFolderName(N,K)
    SaveLoad.gatherData(automataList,currentFolderPath+'/'+"SavedAutomata"+'/'+automataTypeFolderName)
    print "statsToFile:"
    #countAverarageStabilityAndCycleAmount(automataList)
    savePath=currentFolderPath+"/"+"Statistics"+"/"+"Stability"+"/"+automataTypeFolderName
    if not os.path.exists(savePath):
        os.makedirs(savePath)
    stabilityToFiles(N,K,automataList,savePath,sampleLength)

def createAutomataReturnTimeSamples(N,K,currentFolderPath,sampleLength,samplesAmount):
    automataList=[]
    print "gatherData:"
    automataTypeFolderName=SaveLoad.generateAutomataTypeFolderName(N,K)
    SaveLoad.gatherData(automataList,currentFolderPath+'/'+"SavedAutomata"+'/'+automataTypeFolderName)
    print "statsToFile:"
    #countAverarageStabilityAndCycleAmount(automataList)
    savePath=currentFolderPath+"/"+"Statistics"+"/"+"ReturnTime"+"/"+automataTypeFolderName
    if not os.path.exists(savePath):
        os.makedirs(savePath)
    returnTimeToFiles(N,K,automataList,savePath,sampleLength)
