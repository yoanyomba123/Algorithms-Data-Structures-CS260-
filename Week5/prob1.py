'''
Author : D Yoan L mekontchou Yomba

Week 5 : Homework 5


'''

# imports
from tree import tree
from math import *
import random
import timeit



def getParent(n):
    parent = floor((n-1)/2)
    return parent

def getLeftChild(n):
    leftchild = 2*n+1
    return leftchild

def getRightChild(n):
    rightchild = 2*n+2
    return rightchild

def downheap(array, index):
    if(getLeftChild(index) < len(array)):
        templ = getLeftChild(index)
        placeholder_r = getRightChild(index)
        placeholder_l = getLeftChild(index)
        if((getRightChild(index) < len(array)) and (array[placeholder_l] < array[placeholder_r])):
            templ = getRightChild(index)
        if(array[index] < array[templ]):
            array[index], array[templ] = array[templ], array[index]
            downheap(array, templ)

def upheap(array, index):
    while(index > 0) and (getParent(index) < len(array)):
        temp = array[getParent(index)]
        temp1 = array[index]
        array[index] = temp
        array[getParent(index)] = temp1

def insert(array, value):
    array.append(value)
    upheap(array,len(array)-1)

def remove(array):
    value = array[0]
    array[0],array[len(array)-1] = array[len(array)-1], array[0]
    index = len(array)-1
    array.pop(index)
    downheap(array,0)
    return value

def getHeap(array):
    heap = array
    for i in range(len(heap)-1, -1, -1):
        downheap(heap, i)
    return heap

def main():
    #array = [1,3,4,5,76,12,234,12,7,0,-1]
    #array = getHeap(array)
    #print(array)
    print("============STARTING===========\n")
if __name__ == "__main__":
    arrays = []
    sizes = [10,25, 50, 75, 100, 500,300,  800, 1000, 3000, 5000, 8000, 10000,20000, 30000, 40000, 50000]
    for item in sizes:
        arr = [random.random() for i in range(item)]
        array = [int(round(i*100)) for i in arr]
        arrays.append(array)
    file_d = open("datafile.txt", "a+")
    file_d.write("Size of Array         Run Time T(n)        Run Time T(n^2)         Run Time T(n)/n         Run Time T(n^3)\n")
    print("n       |     t(n)\n")

    for item in arrays:
        time = timeit.Timer('getHeap(array)', 'from __main__ import getHeap; from __main__ import array')
        acttime = time.timeit(1)
        file_d.write(str(len(item)) + "       " + str(acttime) + "       " + str(acttime*acttime) + "      " + str(acttime/len(item)) + "       " + str(acttime*acttime*acttime)  +  "\n")
        print(str(len(item)) + "       " + str(acttime) + "\n")

    file_d.close()
