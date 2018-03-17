#   Import
from cell import Cell
import random

# Define list list_concat method
def list_concat_copy(A, B):
    # get the right node
    count = 0
    while A.next is not None:
        if count == 0:
            temp = Cell(A.data,None)
            A = A.next
        else:
            temp = Cell(A.data, temp)
            A = A.next
        count +=1
    temp = Cell(A.data, temp)
    while B.next is not None:
        temp = Cell(B.data, temp)
        B = B.next
    temp = Cell(B.data, temp)

    # iterate over temp and reverse the order of the list
    listcount = None
    while temp.next is not None:
        listcount = Cell(temp.data, listcount)
        temp = temp.next
    listcount = Cell(temp.data, listcount)
    return listcount

def reverselist(l):
    while l.next is not None:
        temp1 = l.next
        temp0 = l
        l = temp1
        l.next = temp0
        continue
    return l


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
    f = list_concat_copy(d,z)
    print('Contents of linked list list concatenations' + list2string(f))
if __name__ == "__main__" :
    # then this was NOT included in another file, so, run the test driver
    main()


