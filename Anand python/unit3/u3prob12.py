import re
import os
from inspect import isfunction
def mydoc(module):
  a=dir(module)
  for each in a:
  
    print each,each.__doc__
#mydoc(len)
#mydoc(os)
mydoc(range)
    
