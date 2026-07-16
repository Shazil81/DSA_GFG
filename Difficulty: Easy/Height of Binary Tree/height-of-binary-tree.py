'''
Definition for Node
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def height(self, root):
        def solve(root):
            if root is None:
                return 0
            leftheight = solve(root.left)
            rightheight = solve(root.right)
            return 1 + max(leftheight, rightheight)
        res = solve(root)
        return res - 1
        