# A binary tree Node
# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
         # Level order traversal (BFS - Breadth First Search)
        res = []
        queue = deque([])

        if root is None: # base case
            return []

        queue.append(root)

        while len(queue) != 0:

            for _ in range(len(queue)):
                e = queue.popleft()
                res.append(e.data)
                if e.left is not None:
                    queue.append(e.left)
                if e.right is not None:
                    queue.append(e.right)
        
        return res
        