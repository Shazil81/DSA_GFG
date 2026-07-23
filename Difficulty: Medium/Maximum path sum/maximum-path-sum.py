'''
Definition for Node
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxSum(self, root): 
        # Height wala pe based hai
        self.maxi = float('-inf')
        
        def solve(root):
            if root is None:
                return 0
            
            lh = solve(root.left)
            if lh < 0:
                lh = 0
            
            rh = solve(root.right)
            if rh < 0:
                rh = 0
            
            self.maxi = max(self.maxi, lh + root.data + rh)
            return root.data + max(lh, rh)
        
        solve(root)
        return self.maxi
        
        
        
        