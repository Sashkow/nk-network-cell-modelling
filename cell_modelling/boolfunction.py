from . import saveload
import os
import random

class BoolFunction(object):
    def __init__(self,p__k=0,p_values_string=""):
        current_folder_path = os.path.dirname(__file__)
        self.K=p__k
        self.values_string=p_values_string
        
        #  self.__class__ = type(self.__class__.__name__, (self.__class__,), {})
        #  self.__class__.__call__ = self.evaluate

  #  def __getstate__(self): return self.__dict__
  
  #  def __setstate__(self, d): self.__dict__.update(d)
  
  #  def __reduce__(self):
  #     return (BoolFunction, ())
    
    def __str__(self):
        return self.values_string

    def __repr__(self):
        return self.values_string

    def generate_random(self):
        self.values_string = ""
        i = 0
        while i < 2 ** self.K:
            self.values_string += str(random.randrange(0, 2))
            i += 1

    def evaluate(self, inputs_string):
        return self.values_string[int(inputs_string, base=2)]


def generate_random_bool_expression_string(N,K):
    return
