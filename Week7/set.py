import random

class setNode():

    def __init__(self, value=None, parent=None):
        self.value = value
        self.parent = parent
        self.height = 1


def Initialize(values):
    universal_set = {}
    # return a dictionary where each key witholds a set node
    for item in values:
        universal_set[item] = setNode(item, None)
    # return the universal set or set of sets
    return universal_set


def Find(universal_set, value):
    child = universal_set[value]
    parents = []
    # iterate until our current node has no parent
    while child.parent is not None:
        # append the child under analysis to the parent array
        parents.append(child)
        child = child.parent
    # append child upholding the terminationg condition
    parents.append(child)

    # iterate over all elements in the parent except the last one
    for i in range(len(parents)-1):
        # set the parent of each child as the set parent and that parent being the last node in the parent list
        parents[i].parent = parents[-1]
    del parents[:]
    return child


def Merge(universal_set, value1, value2):
    # call find for both values
    omega = Find(universal_set, value1)
    beta = Find(universal_set, value2)
    # if the heights are equal it doesnt really matter so we set omega as betta's parent
    if (omega.height is beta.height) and (omega is not beta):
        beta.parent = omega
        omega.height = omega.height + 1
    elif omega is beta:
        return

    # if beta height is bigger then set beta as parent to omega
    if omega.height < beta.height:
        omega.parent = beta
    # if omega height is bigger than set omega as parent ot beta
    elif omega.height > beta.height:
        beta.parent = omega


