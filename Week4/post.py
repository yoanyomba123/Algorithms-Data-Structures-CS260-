'''
    Author: D Yoan L Mekontchou Yomba

    Date: 2/3/2017

'''

# imports
from lexer import *
from tree import *
stack = []
# specify inorder search
def inOrderSearch(tree):
    if tree.l_child is None or tree.r_child is None:
        return tree.label
    else:
        return inOrderSearch(tree.l_child) + " " + str(tree.label) + " " + inOrderSearch(tree.r_child);

# specify pre order search
def preOrderSearch(tree):
    if tree.l_child is None or tree.r_child is None:
        return tree.label
    else:
        return str(tree.label) + " " + preOrderSearch(tree.l_child) + " " + preOrderSearch(tree.r_child)

# specify postorder search
def postOrderSearch(tree):
    if tree.l_child is None or tree.r_child is None:
        return tree.label
    else:
        return postOrderSearch(tree.l_child) + " " + postOrderSearch(tree.r_child) + " " + str(tree.label)

def calculate(tree):
    if tree.l_child is None and tree.r_child is None:
        return int(tree.label)
    else:
        value = operation(calculate(tree.l_child), tree.label, calculate(tree.r_child))
        return value

def operation(l_child, label, r_child):
    op = 0
    if label is '-':
        return l_child - r_child
    elif label is '+':
        return l_child + r_child
    elif label is '*':
        return l_child * r_child
    elif label is '/':
        return l_child / r_child

def main():
    global stack
    while get_expression():
        value = get_next_token()
        while value:
            if str.isdigit(value[0]) is True:
                # create a tree with current value having no descendants
                subtree = tree(value)
                # append value to the stack
                stack.append(subtree)
            else:
                # here were are an operator so must specify current descendants as the two curent values in the stack
                right = stack.pop()
                left = stack.pop()
                subtree = tree(value, left, right)
                # append value to the stack
                stack.append(subtree)

            # get the next available token
            value = get_next_token()
    for i in range(0, len(stack)):
        # pre order
        print("pre-order search: " + preOrderSearch(stack[i]))
        # in order
        print("in-order search: " + inOrderSearch(stack[i]))
        # post order
        print("post-order search: " + postOrderSearch(stack[i]))
        # perform operation on the tree
        print("eval: " +  str(calculate(stack[i])))
        print("\n\n")
if __name__ == "__main__":
    main()
