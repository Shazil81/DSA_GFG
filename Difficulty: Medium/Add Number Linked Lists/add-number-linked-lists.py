'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def help(self, node):
        prev = None
        curr = node
        
        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        
        return prev
        
    def addTwoLists(self, head1, head2):
        # Optimal one
        l1 = self.help(head1)
        l2 = self.help(head2)
        
        dummy = Node(0)
        tail = dummy
        carry = 0  # carry concept used

        while l1 or l2 or carry:  # head1 bacha ho ya head2 ya carry tab tk loop run kro
            if l1: # head1 ka valueaue liya
                v1 = l1.data
            else:
                v1 = 0
            if l2: # head2 ka value liya
                v2 = l2.data 
            else:
                v2 = 0
            
            total = v1 + v2 + carry  # total add kiya carry k sath

            carry = total // 10  # carry nikalne ka concept

            tail.next = Node(total % 10)  # last digit nikala or uska node bna diya

            # Pointers Updating
            tail = tail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        # 2. Yahan par galti thi: result ko reverse karna zaroori hai
        result_head = self.help(dummy.next)
        
        # 3. (Optional) GFG ke requirements ke hisaab se leading zeros hatayein
        # Agar result list 0->0->1->1 hai, to sirf 1->1 return karein
        while result_head and result_head.data == 0 and result_head.next:
            result_head = result_head.next
            
        return result_head
        
        