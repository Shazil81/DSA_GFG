'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def search(self, root, key):
        curr = root
        while curr:
            if curr.data == key:
                return curr
            elif curr.data < key:
                curr = curr.right
            else:
                curr = curr.left
        return None
        