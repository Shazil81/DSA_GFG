"""  list Node is as defined below:

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

"""

# complete this function
# return head of list after swapping
class Solution:    
    def pairWiseSwap(self, head):
        dummy = Node(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            # Identify nodes to swap
            first = prev.next
            second = prev.next.next
            
            # Swapping pointers
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Move forward
            prev = first
            
        return dummy.next
        