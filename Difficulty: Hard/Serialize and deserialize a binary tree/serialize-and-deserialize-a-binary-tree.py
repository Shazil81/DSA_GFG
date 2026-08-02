'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def serialize(self, root):
        # preorder traversal ka use hoga
        lst = []

        def solve(node):
            if not node:
                lst.append('#')
                return
            
            lst.append(node.data)
            solve(node.left)
            solve(node.right)
        
        solve(root)
        return lst

    def deSerialize(self, arr):
        
        self.i = 0

        def dfs():
            if arr[self.i] == "#":
                self.i += 1
                return None
            
            node = Node(arr[self.i])
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
    