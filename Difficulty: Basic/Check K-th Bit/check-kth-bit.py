class Solution:
    def checkKthBit(self, n, k):
        # left Shift se krte hain

        if n & (1<<k) != 0:
            return True
        else:
            return False
        