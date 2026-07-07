# structure of list node:
# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.next = None

class Solution:
    def findIntersection(self, head1, head2):
        # Hashset ka use kr rhe hain
        node_set = set()
        curr2 = head2
        while curr2 is not None:
            node_set.add(curr2.data)
            curr2 = curr2.next
        
        curr1 = head1
        new_node = Node(0)
        temp = new_node
        while curr1 is not None:
            if curr1.data in node_set:
                temp.next = Node(curr1.data)
                temp = temp.next
            curr1 = curr1.next
        
        return new_node.next
        
            
        
        