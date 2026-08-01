'''
Structure of tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def solve(self, node, p, q):
        if node is None:
            return None
        if node.data == p or node.data == q:
            return node
        
        left = self.solve(node.left, p, q)
        right = self.solve(node.right, p, q)
        
        # 3 condition check krenge
        if left is None and right is None:
            return None
        
        elif left is None:
            return right
        
        elif right is None:
            return left
        
        return node
        
    def lca(self, root, n1, n2):
        return self.solve(root, n1, n2)

