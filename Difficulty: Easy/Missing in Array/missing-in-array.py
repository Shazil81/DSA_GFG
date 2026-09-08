class Solution:
    def missingNum(self, arr):
        total = sum(arr)
        n = len(arr) + 1
        return n*(n+1)//2 - total