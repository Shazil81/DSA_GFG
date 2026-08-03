''' 
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''        
class Solution:
    def correctBST(self, root: 'Node') -> 'Node':
        # ye approach hai to inorder bs kya kr rhe hain ki jha pe inversion mil rha hai to store kr le rhe h 
        self.first = None
        self.second = None
        self.prev = None

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)

            # ab jha pe inversion aayega usko store kr lete hain
            if self.prev and self.prev.data > node.data:
                if not self.first: # agar pehla galti hua to first update 
                    self.first = self.prev
                self.second = node # ye pehla or sura dono me hoga catch ye hi ki isko prev se nhi hai mtlb ki dusra galti hamesha age wala ko store kr k swap hoga

            self.prev = node

            inorder(node.right)

        inorder(root)

        self.first.data, self.second.data = self.second.data, self.first.data
        
        return root
        