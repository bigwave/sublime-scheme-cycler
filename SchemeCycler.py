import sys
#print(sys.version[0])
if sys.version[0] >= "3":
    from .python3 import NextColorSchemeCommand
    from .python3 import PreviousColorSchemeCommand
else:
    from python2 import NextColorSchemeCommand
    from python2 import PreviousColorSchemeCommand
   