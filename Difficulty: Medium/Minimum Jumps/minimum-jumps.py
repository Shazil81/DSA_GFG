class Solution:
    def minJumps(self, arr: list[int]) -> int:
        # Greedy approach hai logic hai i+arr[i]
        jump = 0
        left = 0
        right = 0
        n = len(arr)
        while right < n - 1:
            farthest = 0
            for i in range(left, right+1):
                farthest = max(farthest, i+arr[i])
            if farthest <= right:
                return -1
            left = right+1
            right = farthest
            jump+=1  
        return jump