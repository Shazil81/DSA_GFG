class Solution:
    def maximumFrequency(self, s):
        words = s.split()
        hashmap = {}
        for word in words:
            hashmap[word] = hashmap.get(word, 0) + 1
        
        sorted_items = sorted(hashmap.items(), key = lambda x : -x[1])
        
        res = f"{sorted_items[0][0]} {sorted_items[0][1]}"
        
        return res
        