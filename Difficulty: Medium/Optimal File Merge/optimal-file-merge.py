import heapq
class Solution:
    def minComputation(self, files):
        heapq.heapify(files)
        
        total = 0
        
        while len(files) > 1:
            first = heapq.heappop(files)
            second = heapq.heappop(files)
            
            curr = first + second
            total += curr
            
            heapq.heappush(files, curr)
        
        return total
        