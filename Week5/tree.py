'''
    Author: D Yoan L Mekontchou Yomba
    Date : 2/3/2018

    binary tree implementation
'''

class tree:
    def __init__(self, label, l_child=None, r_child=None):
        self.label = label
        self.leftchild = l_child
        self.rightchild = r_child
