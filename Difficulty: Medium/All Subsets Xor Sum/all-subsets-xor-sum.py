class Solution:
    def subsetXORSum(self, arr):
        # ye ek formula based question hai
        n = len(arr)

        or_all = 0
        for num in arr:
            or_all |= num

        return or_all * (1 << (n - 1))  # or of all elements * 2 ^(n-1)
