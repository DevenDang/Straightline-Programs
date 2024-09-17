import stdio
import stdrandom
import sys

n = int(sys.argv[1])
die1 = stdrandom.uniformInt(1,n)
die2 = stdrandom.uniformInt(1,n)

stdio.writeln(die1+die2)
...
