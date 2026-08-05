'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def predecessor(self, root, key):
        pred = None
        curr = root
        while curr:
            if curr.data < key:
                pred = curr
                curr = curr.right
            else:
                curr = curr.left
        return pred
    def successor(self, root, key):
        succ = None
        curr = root
        while curr:
            if curr.data > key:
                succ = curr
                curr = curr.left
            else:
                curr = curr.right
        return succ
    def findPreSuc(self, root, key):
        pred = self.predecessor(root, key)
        succ = self.successor(root, key)
        return [pred, succ]