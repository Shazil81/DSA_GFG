'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        # Slow fast Pointer
        
        if x == 1:
            return head.next
            
        curr = head
        
        for _ in range(1, x-1):
            curr = curr.next
        
        curr.next = curr.next.next
        return head
