import heapq
class Solution:

    def canRearrange(self, s):
        # hashmap + heap

        hashmap = {}
        for ch in s:
            hashmap[ch] = hashmap.get(ch, 0) + 1
        
        max_heap = []
        for key, value in hashmap.items():
            heapq.heappush(max_heap, (-value, key))
        
        res = []
        prev_char = ""
        prev_count = 0
        
        while max_heap:
            count, char = heapq.heappop(max_heap)
            res.append(char)

            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))
            
            prev_count = count + 1
            prev_char = char
        
        ans = "".join(res)

        if len(s) == len(ans):
            return ans
        
        else:
            return ""
