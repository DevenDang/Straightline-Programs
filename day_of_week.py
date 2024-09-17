import stdio
import sys

year = int(sys.argv[3])
month = int(sys.argv[1])
day = int(sys.argv[2])

y = year - ((14 - month)/12)
x = y + (y/4) - (y/100) + (y/400)
m = month + 12 * ((14 - month)/12) - 2
dow = (day + x + (31 * m/12)) % 7

stdio.writeln(int(dow))

