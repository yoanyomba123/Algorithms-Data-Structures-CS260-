# Author : D Yoan L Mekontchou Yomba
# Date   : 1/26/2018
# Method times methods

# specify imports
import random
import timeit
from problem1 import fib
from problem2 import fibmemoized

# specify ranges to time functions on
rng = range(1,41)

# open a file to write data to
file_w = open("yoan.out","a+")

for i in rng:
    memo = {0:1, 1:1}
    time1 = timeit.Timer('fib(i)', 'from problem1 import fib; from __main__ import i')
    time2 = timeit.Timer('fibmemoized(i, memo)','from problem2 import fibmemoized; from __main__ import i, memo')

    actualtime = time1.timeit(1)
    actualtime2 = time2.timeit(1)

    print "running for " + str(i) + " , " + str(actualtime) + " , " + str(actualtime2)
    file_w.write(str(i) + "      " + str(actualtime) + "      "+"     " + str(actualtime2) + "\n")



file_w.close()
