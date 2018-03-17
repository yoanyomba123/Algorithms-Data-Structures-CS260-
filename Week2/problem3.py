from cell import Cell
import random
import timeit

from problem1 import list_concat, list2string
from problem2 import list_concat_copy, list2string

################## Time Functions ########################

rangec = range(1000, 15003,1000)
# open file which writing data to
filec = open("data.txt","a+")

prob1 ='from problem1 import list_concat; from __main__ import d,z'
prob2 ='from problem2 import list_concat_copy; from __main__ import d,z'

def countit(A):
    count = 0
    while A is not None:
        count += 1
        A = A.next
    return count

# iterate over values in range
for i in rangec:
    d = None
    z = None
    for i in range(1, i+1):
        d = Cell(i,d)
        z = Cell(i,z)
    count = countit(d)
    mytime = timeit.Timer( 'list_concat(d, z)', prob1 )
    mytime2 = timeit.Timer( 'list_concat_copy(d, z)', prob2 )

    delta = mytime.timeit(1)
    delta2 = mytime2.timeit(1)

    filec.write(str(count) + "     " + str(delta) + "     "+"      "+ str(delta2) + "\n")
    print "1 run of list_concat took " + "     " + str(delta) + "     "+"1 run of list_concat_copy took "+"      "+ str(delta2) + "\n"

filec.close()
