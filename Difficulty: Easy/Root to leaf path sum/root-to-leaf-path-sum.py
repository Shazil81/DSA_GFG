'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


class Solution:

    def hasPathSum(self, root, target):
        '''
        :param root: root of given tree.
        :param sm: root to leaf sum
        :return: true or false
        '''
        # code here
        def help(node, target, pathsum):
            if not node:
                return False
            
            pathsum += node.data
            
            if node.left is None and node.right is None:
                if pathsum == target:
                    return True
            
            left = help(node.left, target, pathsum)
            right = help(node.right, target, pathsum)
            
            if left == True or right == True:
                return True
            
            return False
        
        return help(root, target, 0)