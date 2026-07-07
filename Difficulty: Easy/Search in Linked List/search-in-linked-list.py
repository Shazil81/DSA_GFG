'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def searchKey(self, head, key):
        # while loop lga k ho jaga
        curr = head
        while curr is not None:
            if curr.data == key:
                return True
            curr = curr.next
        return False
        