# Author: D Yoan L Mekontchou Yomba
# Date  : 1/26/2018
# Implement fibonacci in a recursive fashion using memoisation

# imports
import sys;

# recursive function definition implementing memoization
def fibmemoized(argument, memory):
    # check if input argument was 1 and handle special case
    if argument <= 1:
        return 1
    # case fibonacci sequence is stored in memory already
    elif argument in memory:
        return memory[argument]
    # fill the memo with the contents of fibonacci recursive call
    else:
        memory[argument] = fibmemoized(argument-1, memory) + fibmemoized(argument-2,memory)
    return memory[argument]

if __name__ == "__main__":
    # define memo
    memoize = {0:1,1:1}
    if(len(sys.argv)) > 1:
        arg = sys.argv[1]
        # process input
        print(fibmemoized(int(arg), memoize))
