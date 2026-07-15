'''
class Node:
    def _init_(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def isIdentical(self, r1, r2):
        
        if r1 is None and r2 is None:
            return True
        
        if r1 is None or r2 is None or r1.data != r2.data:
            return False
        
        leftside = self.isIdentical(r1.left, r2.left)
        rightside = self.isIdentical(r1.right, r2.right)
        
        return leftside and rightside

        