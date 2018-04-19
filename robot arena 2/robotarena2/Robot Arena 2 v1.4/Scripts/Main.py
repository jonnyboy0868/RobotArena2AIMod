#import everything from the C-code
from plus import *

import giScript

#hook into our custom output routines
class giScript_stdout:
    def write(self, s):
        giScript.debug_stdout(s)

class giScript_stderr:
    def __init__(self):
        self.count = 0
    def write(self, s):
        self.count += 1
        giScript.debug_stderr(s)
    def flush(self):
        pass

import sys
sys.stdout = giScript_stdout()
sys.stderr = giScript_stderr()

#import all necessary modules here
try:
    import Arenas
    import AI
except:
    import sys
    giScript.debug_stderr("Error loading module\n")
    giScript.debug_stderr(str(sys.exc_info()[1]) + "\n")

def dispatchEvent(event_name, data):
    "Call 'event_name(data)' on all objects that respond to that event."
    #TODO: would a map be quicker?
    # ie, map(dispatchToObject, objects, (data,) * len(objects))

    pass
#    for obj in objects:
#        func = getattr(obj, event_name, None)
#        if func <> None:
#           NOTE: apply's second parameter is a sequence (that seems odd to me)
#            apply(func, (data,))

def cleanup():
    print "Cleaning up"

global compileFilename
compileFilename = "<string>"

def SetCompileFilename(filename):
    global compileFilename
    compileFilename = filename

def Compile(code):
    "Return bytecode from a string."
    return compile(code, compileFilename, "exec")

#register this function so it can be called from C++
giScript.register_function(dispatchEvent)

print "Main module loaded"

# from http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/52192
def add_method(self, method, name=None):
  if name is None: name = method.func_name
  class new(self.__class__): pass
  setattr(new, name, method)
  self.__class__ = new
