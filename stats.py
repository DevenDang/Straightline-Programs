import math
import stdio
import stdrandom
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
x1 = stdrandom.uniformFloat(a,b)
x2 = stdrandom.uniformFloat(a,b)
x3 = stdrandom.uniformFloat(a,b)

v1 = (x1+x2+x3)/3
v2 = ((x1-v1)**2 + (x2 - v1)**2 + (x3 - v1)**2)/3
v3 = math.sqrt(v2)

stdio.write(v1)
stdio.write(" "+ str(v2))
stdio.writeln(" "+ str(v3))
...
