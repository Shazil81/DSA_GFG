'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.random = None
'''        

class Solution:
    def cloneLinkedList(self, head):
        # Hashmap ka use kr k kr rhe hain optimal nhi hai
        hashmap = {None:None}
        curr = head

        while curr:
            hashmap[curr] = Node(curr.data)
            curr = curr.next
        
        curr = head

        while curr:
            hashmap[curr].next = hashmap.get(curr.next)
            hashmap[curr].random = hashmap.get(curr.random)
            curr = curr.next
        
        return hashmap[head]
        