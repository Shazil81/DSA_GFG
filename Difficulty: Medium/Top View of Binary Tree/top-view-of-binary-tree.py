'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def topView(self, root):
        if not root:
            return None
        
        ans = []
        queue = deque()
        result = {}
        # Hmlog ek imaginary line le k chalenge jo ki ek trh se column hoga
        queue.append((root, 0))
        while queue:
            e, line = queue.popleft()
            # jo pehle aa jayega bs usi ko add krna h baaki ko ignore krna h
            if line not in result:
                result[line] = e.data
            if e.left:
                queue.append((e.left, line-1))
            if e.right:
                queue.append((e.right, line+1))
        # ye key k basis pe sort kr dega yaani jo imaginary line h uske
        for key, value in sorted(result.items()):
            ans.append(value)
        return ans
        
        