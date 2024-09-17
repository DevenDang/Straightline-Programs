import math
import stdio
import sys

r = float(sys.argv[1])
theta = math.radians(float(sys.argv[2]))

x = math.cos(theta) * r
y = math.sin(theta) * r

stdio.write(x)
stdio.write(" ")
stdio.writeln(y)