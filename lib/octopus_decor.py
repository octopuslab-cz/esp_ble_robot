# (c) OctopusLAB 2017-23 - MIT
# this module is "decorators" library for Octopus FrameWork

__version__ = "1.0.3"

"""
usage:
from octopus_decor import octopus_duration, octopus_debug
@octopus_duration
def yourFunc(): ...
"""

def octopus_duration(milis=True):
         
   def _octopus_duration(fnc):
      from time import ticks_ms
      print("--- decorator --- @octopus_duration:")
            
      try:
            fname = fnc.__name__
      except:
            fname = "?"
      
      def ff(*args, **kwargs):
         #start = time.time() # todo: if milis...
         start = ticks_ms()
         result = fnc(*args, **kwargs)
         end = ticks_ms() - start
                  
         print(".:. function: ", fname)
         print("--> duration (milis.) -->", str(end))
         return result

      return ff
   return _octopus_duration


def octopus_debug(ledon=False,info=True):
   if ledon:
         from components.led import Led
         led = Led(2)
         
   def _octopus_debug(fnc):
      import time
      print("--- decorator --- @octopus_debug:")
      #if ledon: led.blink()
      
      try:
            fname = fnc.__name__
      except:
            fname = "?"
      
      def ff(*args, **kwargs):
         if ledon: led.value(1)
         start = time.time()
         result = fnc(*args, **kwargs)
         end = time.time() - start
         if ledon: led.value(0)
         
         print("=== function name: ", fname)
         print("=== duration (sec.) --->", str(end))
         return result

      return ff
   return _octopus_debug
