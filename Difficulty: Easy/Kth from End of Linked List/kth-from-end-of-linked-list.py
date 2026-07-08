""" Node Structure
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""

class Solution:
    def getKthFromLast(self, head, k):
        # Optimal Solution two pointer approach
        
        slow = head
        fast = head
        for _ in range(k): # jitna n wha pe pehle hi fast ko rkh denge
            if fast is None:
                return -1
            fast = fast.next
        # Special case
        if fast is None:
            return head.data
            
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        
        return slow.next.data
        