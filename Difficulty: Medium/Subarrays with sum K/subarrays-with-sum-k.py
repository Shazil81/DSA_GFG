class Solution:
    def cntSubarrays(self, arr, k):
        # prefix sum + hashing use hoga
        n = len(arr)
        hashmap = {}
        count = 0
        curr_sum = 0
        
        for i in range(n):
            curr_sum += arr[i]
            
            if curr_sum == k:
                count += 1
            
            remaining = curr_sum - k
            if remaining in hashmap:
                count += hashmap[remaining]
            
            if curr_sum in hashmap:
                hashmap[curr_sum] += 1
                
            else:
                hashmap[curr_sum] = 1
        
        return count
            
        