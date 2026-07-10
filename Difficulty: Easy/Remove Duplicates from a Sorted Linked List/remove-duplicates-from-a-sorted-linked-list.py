''' Structure of linked list Node
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
def removeDuplicates(head):
    
    if not head:
        return None
    
    curr = head
    
    while curr.next is not None:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    
    return head