'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def postOrder(self, root):
        # Iterative se krte hain
        stack = []
        res = []
        # Iterative se krte hain
        if root is None: # Base condition
            return res
        
        stack.append(root)
        while stack:
            e = stack.pop()
            res.append(e.data)

            if e.left:
                stack.append(e.left)
                
            if e.right:
                stack.append(e.right)

            
        return res[::-1]
        
        