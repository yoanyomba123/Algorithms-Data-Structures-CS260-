'''
    Author: D Yoan L Mekontchou Yomba
    Date : 2/3/2018

    binary tree implementation
'''

class tree:
    def __init__(self, label, l_child=None, r_child=None):
        self.label = label
        self.l_child = l_child
        self.r_child = r_child
