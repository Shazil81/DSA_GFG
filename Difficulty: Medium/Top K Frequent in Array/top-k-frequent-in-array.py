import heapq
class Solution:
	def topKFreq(self, arr, k):
		# heap se kr rhe h
        n = len(arr)
        heap = []
        
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        # max heap bnana hai
        for key, value in freq.items():
            heapq.heappush(heap, (-value, -key))
        
        res = []
        for i in range(k):
            freq, key = heapq.heappop(heap)
            res.append(-key)
        
        return res
		
		