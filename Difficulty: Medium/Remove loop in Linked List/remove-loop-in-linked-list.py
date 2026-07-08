''' Structure of linked list Node
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    def removeLoop(self, head):
        if head is None or head.next is None:
            return

        slow = head
        fast = head
    
        # 1. Cycle detection
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
    
            if fast == slow:
                # Cycle mil gayi, ab loop remove karo
                
                # Case 1: Agar cycle head se start ho rahi hai
                if slow == head:
                    while fast.next != head:
                        fast = fast.next
                    fast.next = None
                    return True
                
                # Case 2: Cycle kahin beech mein hai
                slow = head
                while slow.next != fast.next:
                    slow = slow.next
                    fast = fast.next
                
                # Ab 'fast' cycle ke last node par hai
                fast.next = None
                return True
                
        return False
        