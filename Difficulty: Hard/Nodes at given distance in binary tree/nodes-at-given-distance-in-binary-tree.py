'''
Structure of Binary Tree Node
 class Node:
     def __init__(self, val):
         self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def build_parent_map(self, root, parent_map):
        queue = deque([root])
        while queue:
            node = queue.popleft()
            for child in (node.left, node.right):
                if child:
                    parent_map[child] = node
                    queue.append(child)
    
    def find_target_node(self, root, target):
        # target ek value hai, node dhoondhna padega
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.data == target:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return None
                    
    def kDistanceNodes(self, root, target, k):
        parent_map = {}
        self.build_parent_map(root, parent_map)
        
        target_node = self.find_target_node(root, target)
        seen = {target_node}
        queue = deque([target_node])  # target find krne ka zarurat nhi hai bs queue ko wohi se start kro or har trf check kro parent ko bhi
        dist = 0

        while queue and dist < k:
            dist += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbour in (node.left, node.right, parent_map.get(node)): # parent bhi ho rha h check
                    if neighbour and neighbour not in seen:
                        seen.add(neighbour)
                        queue.append(neighbour)
        # last me kya hai ki queue mw=e wohi elements honge jo k dist pe honge uske values ko extract kr k res me daal denge
        res = []
        for node in queue:
            res.append(node.data)
        
        res.sort()
        return res
        