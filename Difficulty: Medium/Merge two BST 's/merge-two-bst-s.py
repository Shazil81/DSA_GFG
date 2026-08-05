'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    # 1. Helper function for Inorder Traversal
    def get_inorder(self, root, arr):
        if not root:
            return
        self.get_inorder(root.left, arr)
        arr.append(root.data)
        self.get_inorder(root.right, arr)

    # 2. Helper function to merge two sorted lists
    def merge_sorted_arrays(self, arr1, arr2):
        merged = []
        i = j = 0
        n1, n2 = len(arr1), len(arr2)

        while i < n1 and j < n2:
            if arr1[i] <= arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1

        # Append remaining elements
        while i < n1:
            merged.append(arr1[i])
            i += 1
        while j < n2:
            merged.append(arr2[j])
            j += 1

        return merged
        
    def merge(self, r1: 'Node', r2: 'Node') -> list[int]:
        list1, list2 = [], []
        
        # Step 1: Extract sorted elements from both trees
        self.get_inorder(r1, list1)
        self.get_inorder(r2, list2)
        
        # Step 2: Merge the two sorted arrays
        return self.merge_sorted_arrays(list1, list2)
        
        