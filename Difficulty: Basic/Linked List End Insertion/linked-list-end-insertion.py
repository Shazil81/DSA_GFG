'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        new_node = Node(x)
        if head is None: # pehla check ki head empty hai kya
            head = new_node
            return head
        
        curr = head
        while curr.next is not None: # Pehle curr ko last tk phunchayenge
            curr = curr.next
        curr.next = new_node
        
        return head
        