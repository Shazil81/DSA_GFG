'''
class Node:
    def _init_(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def mergeKLists(self, arr):
        # heap k sath kr rhe hain
        # step 1 sare values ko ek list me daal dete hain
        heap = []
        for node in arr:
            while node:
                heapq.heappush(heap, node.data)
                node = node.next
        # step 2 heap se pop krte jao or naya linked list bnao kyun ki minimum wala hi pop hoga baar baar
        dummy = Node(0)
        curr = dummy
        
        while heap:
            curr.next = Node(heapq.heappop(heap))
            curr = curr.next
        return dummy.next
        