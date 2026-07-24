'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def zigZagTraversal(self, root):
        # BFS lgega bs ek flag lena usi se manipulate krna hai
        res = []
        queue = deque()
        if root is None:
            return res
        queue.append(root)
        reverse = False
    
        while queue:
            level_size = len(queue)
            lst = []
            
            for _ in range(level_size):
               e = queue.popleft()
               lst.append(e.data)

               if e.left:
                queue.append(e.left)

               if e.right:
                queue.append(e.right)
            # agar reverse true hoga to reverse me add krna h
            if reverse:
                res.extend(lst[::-1])
            else:
                res.extend(lst)
            
            reverse = not reverse
  
        return res
        