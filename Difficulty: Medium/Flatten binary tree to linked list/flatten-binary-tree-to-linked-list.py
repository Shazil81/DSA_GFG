class Solution:
    def flatten(self, root):
        # Ye code optimal hai (Morris Algorithm)
        curr = root
        while curr:
            if curr.left:
                rightmost = curr.left
                while rightmost.right:
                    rightmost = rightmost.right
                
                rightmost.right = curr.right
                curr.right = curr.left
                curr.left = None
            
            curr = curr.right
        