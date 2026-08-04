'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def kthSmallest(self, root, k): 
        # Morris Algorithm se krte hain
        ans = -1
        count = 0
        curr = root
        
        while curr is not None:
            if curr.left is None:
                count += 1
                if count == k:
                    ans = curr.data
                curr = curr.right
            else:
                predecessor = curr.left
                
                while predecessor.right is not None and predecessor.right != curr:
                    predecessor = predecessor.right
                
                if predecessor.right is None:
                    predecessor.right = curr
                    curr = curr.left
                
                else:
                    predecessor.right = None
                    count += 1
                    if count == k:
                        ans = curr.data
                    curr = curr.right
        
        return ans
                    
        