import heapq
class Geeks:
    def __init__(self):
        self.q = []
    
    # Function to insert element into the queue
    def insert(self, q, k):
        heapq.heappush(q, -k)
        
    # If k is in q return true else return false
    def find(self, q, k):
        return (-k) in q
        
    
    # delete the max element from queue
    def delete(self, q):
        if q:
            return -heapq.heappop(q)
        