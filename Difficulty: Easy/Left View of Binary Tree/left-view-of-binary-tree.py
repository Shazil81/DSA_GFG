''' 
class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None 
'''
class Solution:
    def leftView(self, root):
        # dfs se krte hain
        res = []
        def dfs(node, lvl):
            if not node:
                return []
            
            if lvl == len(res):
                res.append(node.data)
            
            dfs(node.left, lvl+1)
            dfs(node.right, lvl+1)
            
        dfs(root, 0)
        return res
                    
            
        