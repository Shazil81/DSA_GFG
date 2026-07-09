''' Structure of a Linked List Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

'''
class Solution:
    def reverseBetween(self, a, b, head):
        if not head or a == b:
            return head

        dummy = Node(0)
        dummy.next = head
        curr1 = dummy

        # 1. curr1 ko 'a' se ek pehle lao
        for _ in range(a - 1):
            curr1 = curr1.next
        
        # 2. 'first' wo node hai jo reverse hone ke baad end mein jayegi
        first = curr1.next
        prev = None
        temp = first
        
        # 3. 'b - a + 1' nodes ko reverse karo
        for _ in range(b - a + 1):
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        
        # 4. Connection update
        # 'prev' ab naya head hai reverse segment ka
        # 'temp' ab wo node hai jo reverse segment ke just baad hai
        curr1.next = prev
        first.next = temp

        return dummy.next  # is liye ki agar a 1 hoga to head hi change ho jayega

        
        