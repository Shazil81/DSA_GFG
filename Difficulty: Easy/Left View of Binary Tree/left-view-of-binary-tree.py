''' 
class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None 
'''
from collections import deque
class Solution:
    def leftView(self, root):
        if not root:
            return []
        
        queue = deque([root])
        res = []
        while queue:
            lvl_size = len(queue)
            for i in range(lvl_size):
                e = queue.popleft()
                if i == 0:
                    res.append(e.data)
                
                if e.left:
                    queue.append(e.left)
                
                if e.right:
                    queue.append(e.right)
        
        return res
                    
            
        