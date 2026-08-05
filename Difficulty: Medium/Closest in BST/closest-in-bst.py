'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = self.left = None
        
'''
class Solution:
    
    def minDiff(self, root: 'Node', k: int) -> int:
        curr = root
        min_diff = float('inf')
        
        while curr:
            # 1. Update the minimum difference found so far
            min_diff = min(min_diff, abs(curr.data - k))
            
            # 2. If exact match found, minimum possible difference is 0
            if curr.data == k:
                return 0
            
            # 3. Use BST property to decide direction
            if curr.data > k:
                curr = curr.left
            else:
                curr = curr.right
                
        return min_diff
        
        