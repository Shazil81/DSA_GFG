'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        # Step 1: Find the middle using slow/fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev = None
        curr = slow
        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        # 'prev' is now head of reversed second half

        # Step 3: Compare first half and reversed second half
        left, right = head, prev
        result = True
        while right:  # right half is shorter or equal
            if left.data != right.data:
                result = False
                break
            left = left.next
            right = right.next
        
        return result
        
        