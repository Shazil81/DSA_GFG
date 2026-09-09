class Solution:
    def isPowerofTwo(self, n):
        # to bit se kya hota hai ki bs ek hi hona chahiye 1 wohi hoga 2 ka power
        if n == 0:
            return False

        return n & (n-1) == 0