''' Structure of binary tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def areCousins(self, root, x, y):
        if not root:
            return False
        
        queue = deque([(root, None)])  # (node, parent)
        
        while queue:
            level_size = len(queue)
            found_x = found_y = False
            parent_x = parent_y = None
            
            for _ in range(level_size):
                node, parent = queue.popleft()
                
                if node.data == x:
                    found_x = True
                    parent_x = parent
                if node.data == y:
                    found_y = True
                    parent_y = parent
                
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
            
            # agar dono is level pe mile
            if found_x and found_y:
                return parent_x != parent_y  # same depth hai, ab check parent alag hai ya nahi
            
            # agar sirf ek mila is level pe, toh cousins nahi ho sakte
            if found_x or found_y:
                return False
        
        return False
        