'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''
class Solution:
    # Step 1 get left boundary nodes
    def left_boundary(self, root, ans):
        if root is None:
            return
        if root.left is None and root.right is None:
            return
        ans.append(root.data)
        if root.left:
            self.left_boundary(root.left, ans)
        elif root.right:
            self.left_boundary(root.right, ans)
    # step 2 get leaf nodes
    def isleaf(self, root, ans):
        if root is None:
            return
        if root.left is None and root.right is None:
            ans.append(root.data)
        if root.left:
            self.isleaf(root.left, ans)
        if root.right:
            self.isleaf(root.right, ans)
    # step 3 get right boundary nodes
    def right_boundary(self, root, ans):
        if root is None:
            return
        if root.left is None and root.right is None:
            return
        if root.right:
            self.right_boundary(root.right, ans)
        elif root.left:
            self.right_boundary(root.left, ans)
        ans.append(root.data)
    def boundaryTraversal(self, root):
        res = []
        # hm kya kr rhe h ki root ko direct add kr de rhe h
        if root:
            res.append(root.data)
        # uske boundaries le rhe h isi liye root ka left pass kraya
        if root.left or root.right:
            self.left_boundary(root.left, res)
            self.isleaf(root, res)
            self.right_boundary(root.right, res)
        return res
            
        
        