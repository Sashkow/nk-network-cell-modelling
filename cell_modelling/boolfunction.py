import saveload
import os
import random

class BoolFunction(object):
    def __init__(self,p_K=0,p_valuesString=""):
	currentFolderPath = os.path.dirname(__file__)
	self.K=p_K
	self.valuesString=p_valuesString
    
    #self.__class__ = type(self.__class__.__name__, (self.__class__,), {})
    #self.__class__.__call__ = self.evaluate
    
    
    
  #def __getstate__(self): return self.__dict__
  
  #def __setstate__(self, d): self.__dict__.update(d)
  
  #def __reduce__(self):
  #  return (BoolFunction, ())
    
    
    
    def __str__(self):
	return self.valuesString
    
    def __repr__(self):
	return self.valuesString
    
    def generateRandom(self):
	self.valuesString=""
	i=0
	while i<2**self.K:
	    self.valuesString+=str(random.randrange(0,2))
	    i+=1

    def evaluate(self,inputsString):
	return self.valuesString[int(inputsString,base=2)]

def generateRandomBoolExpressionString(N,K):
    return
    
    
      
    
      
  
      
