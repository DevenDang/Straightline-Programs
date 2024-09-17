import stdio
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

alpha = min(x,y,z)
omega = max(x,y,z)
middle = x + y + z - alpha - omega

stdio.write(alpha)
stdio.write(" " + str(middle))
stdio.writeln(" " + str(omega))
...
