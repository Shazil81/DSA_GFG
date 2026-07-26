'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.nextRight = None
'''  
from collections import deque
class Solution:
    def connect(self, root):
        if not root:
            return None
            
        q = deque([root])
        
        while q:
            size = len(q)
            prev = None
            
            for i in range(size):
                curr = q.popleft()
                
                # Agar pichla node tha same level par, usko current se jodo
                if prev:
                    prev.nextRight = curr
                prev = curr
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                    
        return root
            
        

        