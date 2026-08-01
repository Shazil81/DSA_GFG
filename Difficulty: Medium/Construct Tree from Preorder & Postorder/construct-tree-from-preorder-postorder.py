'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

'''

class Solution:
    def constructTree(self, pre, post):
        # bina queue k hoga ye bhi
        self.i = 0
        mapping = {}
        for i in range(len(post)):
            mapping[postorder[i]] = i

        def solve(start, end):
            if start > end:
                return None
            
            root = Node(pre[self.i])
            self.i += 1

            if start == end:
                return root
            
            index_left_subtree = mapping[pre[self.i]]
            root.left = solve(start, index_left_subtree)
            root.right = solve(index_left_subtree + 1, end-1)

            return root
        
        return solve(0, len(post)-1)
        