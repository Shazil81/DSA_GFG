"""
class Node:
    def __init__(self, d):
        self.data = d
        self.prev = None
        self.next = None
"""

class Solution:
    def delPos(self, head, x):
        curr = head
        # Pehla case ki pos 1 ho tb
        if x==1:
            head = head.next # head ko bhej denge ehad k next pe
            if head: # agar head exist krega to uska prev None kr denge tab hi to delete hoga
                head.prev = None
            return head # or agar head None hai to usi ko return kr denge
        # dusra case    
        for _ in range(x-1):
            if curr is not None:
                curr = curr.next
        if curr is None:  # ye is liye ki kya pta pos ki length zyada ho to curr to None hi hoga
            return head
       
        if curr.prev is not None:
            curr.prev.next = curr.next
        if curr.next is not None:
            curr.next.prev = curr.prev
        return head
        
        