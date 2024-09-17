import math
import stdio
import sys

theta1 = math.radians(float(sys.argv[1]))
n1 = float(sys.argv[2])
n2 = float(sys.argv[3])

theta2 = math.asin((n1/n2)*math.sin(theta1))
stdio.writeln(math.degrees(theta2))