'''
Structure of linked list node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def compute(self,head):
        # Stack: Optimal One
        values = []
        curr = head
        while curr:
            values.append(curr.data)
            curr = curr.next
        
        n = len(values)
        stack = []
        for i in range(n-1, -1, -1):
            if not stack:
                stack.append(values[i])
            else:
                if stack[-1] <= values[i]:
                    stack.append(values[i])
        
        dummy = Node(0)
        curr = dummy

        while stack:
            curr.next = Node(stack.pop())
            curr = curr.next
        
        return dummy.next
        