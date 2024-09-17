from operator import truediv
from xmlrpc.client import boolean

import stdio
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

expr = bool
if z>x+y:
    expr = False
elif y>x+z:
    expr = False
elif x>y+z:
    expr = False
else:
    expr = True

stdio.writeln(expr)




