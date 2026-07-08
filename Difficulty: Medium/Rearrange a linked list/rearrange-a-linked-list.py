""" Node Structure
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""

class Solution:
    def rearrangeEvenOdd(self, head):
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_head = even
        
        while even is not None and even.next is not None:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        
        odd.next = even_head
        return head
        