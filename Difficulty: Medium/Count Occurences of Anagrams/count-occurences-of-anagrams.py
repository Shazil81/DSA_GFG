class Solution:

	def search(self,p, s):
	    # bs ye question me hmlog count krenge instead of index ko find krne k
	    # Optimal approach (Sliding Window + Hashmap)
        m = len(p)
        n = len(s)
        res = 0
        # edge case
        if m > n:
            return res
        
        # p ka chars ko hashmap me daal do
        p_map = {}
        for char in p:
            p_map[char] = p_map.get(char, 0) + 1
        
        # initial window bna lenge
        s_map = {}
        for i in range(0, m):
            s_map[s[i]] = s_map.get(s[i], 0) + 1
        
        # agar pehla window me anagram mila to count kr lenge
        if s_map == p_map:
            res += 1
        
        # ab agla window me hm dekhenge
        for i in range(m, n):
            # add krenge s_map me s ka chars ko
            s_map[s[i]] = s_map.get(s[i], 0) + 1
            # old char ko remove krenge
            old_char = s[i-m] # sliding window ka ek concept ki jitna length hoga chhota wala ka utna hi i se minus kr k pichhe jayenge last wala milega
            if s_map[old_char] == 1:
                del s_map[old_char]
            else:
                s_map[old_char] -= 1
            
            # Compare kr lena hai hashmap ek particular window ka agar equal hoga to count kr lenge
            if s_map == p_map:
                res += 1
        
        return res
	    