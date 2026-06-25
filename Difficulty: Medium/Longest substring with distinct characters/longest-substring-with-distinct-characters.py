class Solution:
    def longestUniqueSubstr(self, s):
        # Optimal solution by using two pointers
        my_dict = {} # dict use kiya
        left = 0
        right = 0
        maxi = 0
        n = len(s)
        while right < n:
            if s[right] in my_dict:
                # agar mera dict me hoga to hm kya krenge ki left ko jha pe mila h us index se ek aage badha denge
                left = max(left, my_dict[s[right]]+1) # wapas pichhe nhi jane k liye max use kiya kyun ki ho skta h left mera aage ho or koi aisa char aage me mile jo left k pichhe ho to hm kyun jayenge pichhe
            # two pointers me right-left+1 ek window length ho jata h  
            maxi = max(maxi, right-left+1)
            my_dict[s[right]] = right # dict me index ko store kr dena
            right+=1
        return maxi
        