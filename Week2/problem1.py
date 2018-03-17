# Author : D Yoan L Mekontchou Yomba
# Date: January 20, 2018
# concatenates the content of list B into list A

#   Import
from cell import Cell
import random

# Define list list_concat method
def list_concat(A, B):
    # get to the node right before None
    pos = A
    # iterating over all nodes in pos which is instance of A
    while pos.next != None:
        pos  = pos.next
        continue
    # point the last node of pos to the first node of B
    pos.next = B
    return A

def list2string( L ) :
    if L is None :
        rv = '()'
    else :
        rv = '('
        while L.next is not None:
            rv += L.__str__() + ','
            L = L.next
        rv += L.__str__() + ')'
    return rv





def main() :
        # test the above concat method
        c = Cell(13) # head -> 13 -> None
        d = Cell(12, c ) # head -> 12 -> 13 -> None
        d = Cell(14, d)  # head -> 14 -> 12 -> 13 -> None
        d = Cell(15, d)  # head -> 15 -> 14 -> 12 -> 13 -> None
        d = Cell(17, d)  # head -> 17 -> 15 -> 14 -> 12 -> 13 -> None
        d = Cell(18, d)  # head -> 18 -> 17 -> 15 -> 14 -> 12 -> 13 -> None
        # creating a new linked list
        z = Cell(0) # head -> 0 -> None
        Z = Cell(1,z) # head -> 1 -> 0 -> None
        z = Cell(2, z) # head -> 2 -> 1 -> 0 -> None
        z = Cell(3, z) # head -> 3 -> 2 -> 1 -> 0 -> None
        z = Cell(5, z) # head -> 5 -> 3 -> 2 -> 1 -> 0 -> None
        z = Cell(6, z) # head -> 6 -> 5 -> 3 -> 2 -> 1 -> 0 -> None

        print('Contents of linked list 1' + list2string(d))
        print('Contents of linked list 2' + list2string(z))
        # Test lsit_concat method
        list1 = list_concat(d, z)
        print('Contents of concatenated list is ' + list2string(list1))
if __name__ == "__main__" :
        # then this was NOT included in another file, so, run the test driver
        main()

