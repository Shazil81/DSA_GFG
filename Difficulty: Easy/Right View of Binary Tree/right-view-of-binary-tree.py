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
    def rightView(self, root):
        # BfS ka use kr k solve ho rha h
        if root is None:
            return []
        queue = deque()
        res = []
        queue.append(root)
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                e = queue.popleft()
                # level size k last me aayega jo node wohi to hoga right view me
                if i == level_size - 1:
                    res.append(e.data)
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
        return res            
        