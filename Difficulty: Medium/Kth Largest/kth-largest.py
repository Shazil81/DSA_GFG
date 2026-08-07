import heapq
class Solution:
    def kthLargest(self, arr, k):
        ans = []
        n = len(arr)
        # K length ka daal do heap me wo min heap bna lega by default
        for i in range(k):
            heapq.heappush(ans, arr[i])
        # ab k se n chala k check krna h elements ko
        for i in range(k, n):
            # by default to mera min heap bnega yaani kya hoga ki jo top rhega yaani 0th
            # index pe wo mera sab se min rhega or pop bhi wohi hoga
            if arr[i] > ans[0]:
                heapq.heappop(ans)
                heapq.heappush(ans, arr[i])
        # k ka length jo hai utna ans me hoga element lekin jo kth largest hoga wo top pe hoga yaani 0th index pe
        return ans[0]
        
        
        