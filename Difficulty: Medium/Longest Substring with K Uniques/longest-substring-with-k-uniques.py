class Solution:
    def longestKSubstr(self, s, k):
        # Optimal solution by using two pointers + sliding window
        my_dict = {} # dict use kiya
        left = 0
        right = 0
        maxi = -1
        n = len(s)
        while right < n:
            my_dict[s[right]] = my_dict.get(s[right], 0) + 1
            if len(my_dict) > k:
                my_dict[s[left]] -= 1
                if my_dict[s[left]] == 0:
                    del my_dict[s[left]]
                left += 1
            if len(my_dict) == k:
                maxi = max(maxi, right-left+1)
            right += 1
        
        return maxi
        
        
        