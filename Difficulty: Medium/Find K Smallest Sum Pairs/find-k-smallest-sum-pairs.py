import heapq
class Solution:
    def kSmallestPair(self, arr1, arr2, k):
        # heap : optimal one
        # base case
        if not arr1 or not arr2:
            return []

        res = []
        heap = []
        # initially arr1 ka element ko pair kr diya arr2[0] k sath
        for i in range(min(k, len(arr1))):
            heapq.heappush(heap, (arr1[i] + arr2[0], i, 0))
        
        while heap and len(res) < k:
            _, i, j = heapq.heappop(heap)
            res.append([arr1[i], arr2[j]])

            if j + 1 < len(arr2):
                heapq.heappush(heap, (arr1[i] + arr2[j + 1], i, j + 1))
        
        return res
        
