import stdio
import sys

g =  6.674 * (10**-11)

m1 =float(sys.argv[1])
m2 = float(sys.argv[2])
r = float(sys.argv[3])
f = g * ((m1*m2)/r**2)

stdio.writeln(f)

...
