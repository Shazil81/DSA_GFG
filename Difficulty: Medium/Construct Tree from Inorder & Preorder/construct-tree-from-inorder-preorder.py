'''  Structure of a Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''
from collections import deque
class Solution:
    def buildTree(self, inorder, preorder):
        # Step 1
        mapping = {}
        queue = deque(preorder)
        for i in range(len(inorder)):
            mapping[inorder[i]] = i
        
        def solve(start, end):
            if start > end:
                return None
            
            # root banana hai
            root = Node(queue.popleft())
            # mid banaya
            mid = mapping[root.data]
            
            root.left = solve(start, mid-1)
            root.right = solve(mid+1, end)
            
            return root
        
        return solve(0, len(preorder)-1)
        
        
        