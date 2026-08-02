'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def solve(self, nums, left, right):
        if left > right:
            return None
        
        mid = (left + right) // 2
        root = Node(nums[mid])
        root.left = self.solve(nums, left, mid - 1)
        root.right = self.solve(nums, mid + 1, right)
        return root
        
    def sortedArrayToBST(self, arr):
        return self.solve(arr, 0, len(arr) - 1)
        