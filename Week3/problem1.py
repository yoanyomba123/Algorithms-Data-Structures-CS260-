# Author: D Yoan L Mekontchou Yomba
# Date  : 1/26/2018
# Implement fibonacci in a recursive fashion

# imports
import sys;

# recursive function definition
def fib(argument):
    if argument <= 1:
        return 1
    else:
        return fib(argument-1) + fib(argument-2)

if __name__ == "__main__":
    if(len(sys.argv)) > 1:
        arg = sys.argv[1]
        print(fib(int(arg)))
