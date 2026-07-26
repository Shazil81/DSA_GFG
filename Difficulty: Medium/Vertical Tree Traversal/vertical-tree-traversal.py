'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque, defaultdict
class Solution:
    def verticalOrder(self, root):
        if not root:
            return []
        
        result = defaultdict(list)
        queue = deque([(root, 0, 0)]) # root, row, col
        ans = []
        
        while queue:
            node, row, col = queue.popleft()
            result[col].append((row, node.data))
            if node.left:
                queue.append((node.left, row+1, col-1))
            if node.right:
                queue.append((node.right, row+1, col+1))
        
        for key, value in sorted(result.items()):
            column_nodes = value
            tmp = []
            for row, val in column_nodes:
                tmp.append(val)
            ans.append(tmp)
        
        return ans
        
        
        